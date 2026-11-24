#!/usr/bin/env python3
"""Limen Engineering MVP: local structured case records and executable evidence.

Standard-library only. Not a security sandbox, release authorization, or independent CI.
Run in a repository with `python3 tools/limen.py --help`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

ROOT = Path.cwd()
DB = ROOT / '.limen'
MOMENTS = ['Experience', 'Model', 'Imagine', 'Branch', 'Simulate', 'Integrate', 'Act', 'Encounter', 'Update']


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def save(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=path.parent, delete=False) as tmp:
        json.dump(data, tmp, ensure_ascii=False, indent=2)
        tmp.write('\n')
        temp = Path(tmp.name)
    os.replace(temp, path)


def current_id() -> str:
    p = DB / 'current'
    if not p.is_file():
        raise ValueError('No active Limen case. Start with: python3 tools/limen.py new --id LIM-001 --objective "..." --tier 1 --owner "..."')
    return p.read_text(encoding='utf-8').strip()


def case_path(case_id: str) -> Path:
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{2,63}', case_id):
        raise ValueError('Case ID must be 3–64 letters/numbers/dashes/underscores')
    return DB / 'cases' / f'{case_id}.json'


def read_case(case_id: str | None = None):
    path = case_path(case_id or current_id())
    if not path.is_file():
        raise ValueError(f'Case not found: {path}')
    return json.loads(path.read_text(encoding='utf-8'))


def write_case(case):
    case['updated_at'] = now()
    save(case_path(case['case_id']), case)


def item_id(case, section: str, prefix: str) -> str:
    return f'{prefix}-{len(case[section]) + 1:03d}'


def add(case, section: str, prefix: str, payload: dict):
    entry = {'id': item_id(case, section, prefix), **payload}
    case[section].append(entry)
    write_case(case)
    print(f'Added {entry["id"]}')


def evidence_issues(case):
    problems = []
    for entry in case['evidence']:
        path = DB / 'evidence' / f'{entry["id"]}.log'
        if not path.is_file():
            problems.append(f'{entry["id"]}: missing log')
            continue
        if hashlib.sha256(path.read_bytes()).hexdigest() != entry.get('sha256'):
            problems.append(f'{entry["id"]}: log digest mismatch')
    return problems


def gate(case):
    tier = int(case['impact_tier'])
    errors = evidence_issues(case)
    if not case['objective'].strip():
        errors.append('Objective missing')
    if tier >= 1:
        if not case['requirements']:
            errors.append('Tier 1+: at least one testable requirement required')
        if not case.get('decision'):
            errors.append('Tier 1+: recorded design decision required')
        if not any(e['exit_code'] == 0 for e in case['evidence']):
            errors.append('Tier 1+: passing tool-executed check required')
        if not case['encounters']:
            errors.append('Tier 1+: recorded observation required')
    if tier >= 2:
        if not case['assumptions']:
            errors.append('Tier 2+: assumptions register required')
        if len(case['alternatives']) < 2:
            errors.append('Tier 2+: at least two design alternatives required')
        if not case['criticisms']:
            errors.append('Tier 2+: criticism required')
        if any(c['disposition'] == 'unresolved' for c in case['criticisms']):
            errors.append('Tier 2+: unresolved criticism needs explicit risk-owner review')
        if not case['scenarios']:
            errors.append('Tier 2+: adverse scenario required')
        if not (case.get('decision') or {}).get('owner'):
            errors.append('Tier 2+: named risk owner required')
    if tier >= 3:
        errors.append('Tier 3: this MVP cannot authorize critical-risk work; independent specialist approval and protected CI are required')
    for correction in case['corrections']:
        proof = next((ev for ev in case['evidence'] if ev['id'] == correction['evidence_id']), None)
        if proof is None or proof['exit_code'] != 0:
            errors.append(f'{correction["id"]}: correction lacks passing referenced test evidence')
    return errors


def run_cli(args):
    if args.action == 'new':
        path = case_path(args.id)
        if path.exists():
            raise ValueError('Case already exists; not overwriting')
        case = {
            'schema_version': '0.1', 'case_id': args.id, 'objective': args.objective,
            'impact_tier': args.tier, 'owner': args.owner, 'created_at': now(),
            'updated_at': now(), 'moments': MOMENTS,
            'requirements': [], 'assumptions': [], 'alternatives': [], 'criticisms': [],
            'scenarios': [], 'decision': None, 'evidence': [], 'encounters': [], 'corrections': [],
        }
        write_case(case)
        DB.mkdir(exist_ok=True)
        (DB / 'current').write_text(args.id + '\n', encoding='utf-8')
        print(f'Created and activated {args.id} (tier {args.tier})')
        return
    if args.action == 'use':
        read_case(args.id)
        (DB / 'current').write_text(args.id + '\n', encoding='utf-8')
        print(f'Active case: {args.id}')
        return
    case = read_case(args.case)
    if args.action == 'require':
        add(case, 'requirements', 'REQ', {'statement': args.text, 'acceptance': args.acceptance})
    elif args.action == 'assume':
        add(case, 'assumptions', 'ASM', {'statement': args.text, 'source': args.source, 'status': args.status})
    elif args.action == 'branch':
        add(case, 'alternatives', 'ALT', {'description': args.text})
    elif args.action == 'criticize':
        if not any(x['id'] == args.target for x in case['alternatives']):
            raise ValueError(f'Alternative not found: {args.target}')
        if args.disposition == 'rejected' and not args.reason:
            raise ValueError('Rejected criticism requires a reason')
        add(case, 'criticisms', 'CRIT', {'target': args.target, 'text': args.text,
            'disposition': args.disposition, 'reason': args.reason})
    elif args.action == 'scenario':
        add(case, 'scenarios', 'SCN', {'description': args.text, 'expected': args.expected})
    elif args.action == 'decide':
        case['decision'] = {'choice': args.choice, 'rationale': args.rationale,
                            'owner': args.owner or case['owner'], 'recorded_at': now()}
        write_case(case)
        print('Decision recorded (not independently approved)')
    elif args.action == 'run-check':
        command = list(args.command)
        if command and command[0] == '--':
            command.pop(0)
        if not command:
            raise ValueError('Supply command after --, e.g. run-check --label unit -- python3 -m unittest')
        proof_id = item_id(case, 'evidence', 'EV')
        try:
            result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True,
                                    errors='replace', timeout=args.timeout, check=False, shell=False)
            status = result.returncode
            output = result.stdout + ('\n[stderr]\n' + result.stderr if result.stderr else '')
        except subprocess.TimeoutExpired as exc:
            status = 124
            output = f'Command exceeded {args.timeout}s: {exc}\n'
        except FileNotFoundError as exc:
            status = 127
            output = f'Cannot execute command: {exc}\n'
        log = DB / 'evidence' / (proof_id + '.log')
        log.parent.mkdir(parents=True, exist_ok=True)
        header = json.dumps({'case': case['case_id'], 'command': command, 'ran_at': now(),
                             'exit_code': status}, ensure_ascii=False)
        log.write_text(header + '\n' + output, encoding='utf-8')
        digest = hashlib.sha256(log.read_bytes()).hexdigest()
        add(case, 'evidence', 'EV', {'label': args.label, 'command': command, 'exit_code': status,
                                    'sha256': digest, 'log': str(log.relative_to(ROOT)), 'recorded_at': now()})
        print(f'{proof_id} finished exit={status}, sha256={digest[:16]}…')
        if status != 0:
            raise RuntimeError('Check failed; evidence was recorded')
    elif args.action == 'encounter':
        add(case, 'encounters', 'OBS', {'observation': args.text, 'source': args.source})
    elif args.action == 'correct':
        proof = next((x for x in case['evidence'] if x['id'] == args.evidence), None)
        if proof is None or proof['exit_code'] != 0:
            raise ValueError('Correction must cite an existing passing tool-executed EV record')
        add(case, 'corrections', 'COR', {'finding': args.finding, 'change': args.change,
                                       'evidence_id': args.evidence, 'scope': 'this-project'})
    elif args.action == 'check':
        problems = gate(case)
        if problems:
            print('NOT READY:')
            for p in problems:
                print(' - ' + p)
            raise RuntimeError('Case gate failed')
        print(f'READY FOR REVIEW: {case["case_id"]}. This is not a release approval or security attestation.')
    elif args.action == 'report':
        print(json.dumps({
            'case_id': case['case_id'], 'objective': case['objective'], 'tier': case['impact_tier'],
            'counts': {k: len(case[k]) for k in ['requirements', 'assumptions', 'alternatives',
                      'criticisms', 'scenarios', 'evidence', 'encounters', 'corrections']},
            'decision': case['decision'], 'gate_issues': gate(case),
        }, indent=2))


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='action', required=True)
    n = sub.add_parser('new'); n.add_argument('--id', required=True); n.add_argument('--objective', required=True)
    n.add_argument('--tier', type=int, choices=range(4), default=1); n.add_argument('--owner', required=True)
    u = sub.add_parser('use'); u.add_argument('id')
    def common(name):
        x = sub.add_parser(name); x.add_argument('--case'); return x
    x = common('require'); x.add_argument('--text', required=True); x.add_argument('--acceptance', required=True)
    x = common('assume'); x.add_argument('--text', required=True); x.add_argument('--source', required=True)
    x.add_argument('--status', choices=['observed','inferred','proposed','unverified','verified'], default='unverified')
    x = common('branch'); x.add_argument('--text', required=True)
    x = common('criticize'); x.add_argument('--target', required=True); x.add_argument('--text', required=True)
    x.add_argument('--disposition', choices=['accepted','rejected','unresolved'], default='unresolved'); x.add_argument('--reason', default='')
    x = common('scenario'); x.add_argument('--text', required=True); x.add_argument('--expected', required=True)
    x = common('decide'); x.add_argument('--choice', required=True); x.add_argument('--rationale', required=True); x.add_argument('--owner')
    x = common('run-check'); x.add_argument('--label', required=True); x.add_argument('--timeout', type=int, default=120)
    x.add_argument('command', nargs=argparse.REMAINDER)
    x = common('encounter'); x.add_argument('--text', required=True); x.add_argument('--source', required=True)
    x = common('correct'); x.add_argument('--finding', required=True); x.add_argument('--change', required=True); x.add_argument('--evidence', required=True)
    common('check'); common('report')
    return p


if __name__ == '__main__':
    try:
        run_cli(parser().parse_args())
    except (ValueError, RuntimeError, OSError) as exc:
        print(f'Limen: {exc}', file=sys.stderr)
        sys.exit(1)
