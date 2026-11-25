#!/usr/bin/env python3
"""Claude Code advisory hook for the Limen harness: prompts for review, not a security perimeter.

Before a `git commit`, or a release-like command (`git push`, `terraform apply`, `kubectl apply|delete`,
`helm upgrade`), it runs `limen.py check` and, if the case is not ready, asks the person with the reason.
Release-like commands always ask. Heuristics only: aliases, wrappers and other tools get around it.

It runs two ways:
- the copy-in starter (a hook in the project's .claude/settings.json): the project's own tools/limen.py;
- the limen-engineering plugin (CLAUDE_PLUGIN_ROOT is set): the plugin's own tools/limen.py, never the
  project's, and only in a repository that already keeps a Limen record (.limen/), so other projects are
  left alone.
The same file is used by both; a unit test keeps the two copies identical.
"""
import json
import os
from pathlib import Path
import re
import subprocess
import sys

# git's own options may come before the subcommand: git -C <dir> commit, git -c k=v push, git --no-pager commit.
_ARG = r'''(?:"[^"]*"|'[^']*'|\S+)'''
_GIT_OPTIONS = (r'(?:\s+(?:-[Cc]\s+' + _ARG + r'|--(?:git-dir|work-tree|namespace|exec-path|config-env)(?:=|\s+)'
                + _ARG + r'|--[\w-]+(?:=\S+)?|-[A-Za-z]))*')
_END = r'(?![\w-])'                      # a whole subcommand: `commit`, not `commit-graph`
RELEASE = re.compile(r'\bgit' + _GIT_OPTIONS + r'\s+push' + _END
                     + r'|\bterraform\s+apply' + _END + r'|\bkubectl\s+(?:apply|delete)' + _END
                     + r'|\bhelm\s+upgrade' + _END)
COMMIT = re.compile(r'\bgit' + _GIT_OPTIONS + r'\s+commit' + _END)


def find_root(start):
    """The same rule as limen.py: the nearest folder holding .limen/ or .git, else `start`."""
    start = Path(start).resolve()
    for folder in (start, *start.parents):
        if (folder / '.limen').is_dir() or (folder / '.git').exists():
            return folder
    return start


def gap_of(tool, start):
    """What `limen.py check` says is missing, as one line; None when the case is ready."""
    if not tool.is_file():
        return f'the Limen tool was not found at {tool}.'
    gate = subprocess.run([sys.executable, str(tool), 'check'], cwd=start, capture_output=True,
                          text=True, timeout=8, check=False)
    if gate.returncode == 0:
        return None
    # The tool prints the unmet items on stdout and its error (such as "No active Limen case") on stderr.
    text = ' '.join((gate.stdout + '\n' + gate.stderr).split())
    return text[-700:] or f'limen.py check exited {gate.returncode} without a message.'


def decide(payload, env):
    if payload.get('tool_name') != 'Bash':
        return None
    command = (payload.get('tool_input') or {}).get('command', '')
    if not isinstance(command, str):
        return None
    release = RELEASE.search(command)
    if not (release or COMMIT.search(command)):
        return None
    start = Path(payload.get('cwd') or env.get('CLAUDE_PROJECT_DIR') or os.getcwd())
    plugin = env.get('CLAUDE_PLUGIN_ROOT')
    if plugin:
        if not (find_root(start) / '.limen').is_dir():
            return None
        tool = Path(plugin) / 'tools' / 'limen.py'
    else:
        tool = Path(env.get('CLAUDE_PROJECT_DIR') or start) / 'tools' / 'limen.py'
    gap = gap_of(tool, start)
    if release:
        detail = 'Consequential command: it needs an explicit human approval and release protections outside Claude.'
        return detail + (' The Limen case is also NOT READY: ' + gap if gap else '')
    if gap:
        return 'Limen case not ready for commit: ' + gap + ' Proceed only after reviewing this gap.'
    return None


def main():
    try:
        payload = json.load(sys.stdin)
        reason = decide(payload, os.environ)
        if reason:
            print(json.dumps({'hookSpecificOutput': {
                'hookEventName': 'PreToolUse', 'permissionDecision': 'ask',
                'permissionDecisionReason': reason[:1000]}}))
    except Exception as exc:
        # Fail open, visibly: this informational hook is not a security mechanism.
        print(f'Limen advisory hook failed: {exc}', file=sys.stderr)


if __name__ == '__main__':
    main()
