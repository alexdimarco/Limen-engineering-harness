#!/usr/bin/env python3
"""Claude Code demonstration hook: prompts for review, not a security perimeter."""
import json
import os
from pathlib import Path
import re
import subprocess
import sys


def decide(payload, project):
    if payload.get('tool_name') != 'Bash':
        return None
    command = payload.get('tool_input', {}).get('command', '')
    if not isinstance(command, str):
        return None
    # Best-effort heuristics: shell aliases, wrappers, and other tools can bypass these.
    release = re.search(r'\b(?:git\s+push|terraform\s+apply|kubectl\s+(?:apply|delete)|helm\s+upgrade)\b', command)
    commit = re.search(r'\bgit\s+commit\b', command)
    if not (release or commit):
        return None
    gate = subprocess.run([sys.executable, str(project / 'tools' / 'limen.py'), 'check'],
                          cwd=project, capture_output=True, text=True, timeout=8, check=False)
    if release:
        detail = 'Consequential command requires an explicit human approval and external release protections.'
        if gate.returncode:
            detail += ' Limen local case is also NOT READY. ' + gate.stdout[-600:]
        return detail
    if gate.returncode:
        return 'Limen case not ready for commit: ' + gate.stdout[-700:] + '. Proceed only after reviewing this gap.'
    return None


def main():
    try:
        payload = json.load(sys.stdin)
        project = Path(os.environ.get('CLAUDE_PROJECT_DIR', os.getcwd()))
        reason = decide(payload, project)
        if reason:
            print(json.dumps({'hookSpecificOutput': {
                'hookEventName': 'PreToolUse', 'permissionDecision': 'ask',
                'permissionDecisionReason': reason[:1000]}}))
    except Exception as exc:
        # Fail open, visibly: this informational hook is not a security mechanism.
        print(f'Limen advisory hook failed: {exc}', file=sys.stderr)


if __name__ == '__main__':
    main()
