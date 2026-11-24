# Limen Engineering — Claude Code starter (v0.1)

This is a **working local prototype**, not a complete engineering harness. It implements the nine-moment inquiry process, structured local cases, risk-tiered checks, tool-executed test evidence and an advisory Claude Code hook.

## Install into a test repository

1. Extract this ZIP to a temporary folder. Copy `tools/`, `.claude/skills/limen/`, `.claude/hooks/pretool.py`, and `docs/` into the root of your chosen repository. Merge, **do not replace**, existing `CLAUDE.md` and `.claude/settings.json`; add the displayed skill guidance and `PreToolUse` hook stanza to those existing files.
2. Require **Python 3.10+** (`python3 --version`). No third-party libraries are needed.
3. Run `python3 tools/limen.py --help`.
4. Start Claude Code in the repository and invoke `/limen` during a nontrivial engineering task. In desktop or cloud sessions confirm `.claude/settings.json` and the hook actually loaded using Claude Code's `/doctor`.
5. Treat the `ask` hook as review friction, not enforceable access control. Put `python3 tools/limen.py check` in protected CI for an actual required status check, and protect the branch outside Claude.

## Example from a clean repository

```sh
python3 tools/limen.py new --id LIM-DEMO1 --objective 'Build a safe parser' --tier 1 --owner 'human-engineer'
python3 tools/limen.py require --text 'Reject malformed input' --acceptance 'Negative tests pass'
python3 tools/limen.py branch --text 'Simple strict parser'
python3 tools/limen.py decide --choice 'Simple strict parser' --rationale 'Smallest auditable surface' --owner 'human-engineer'
python3 tools/limen.py run-check --label unit -- python3 -m unittest discover -s tests
python3 tools/limen.py encounter --text 'Unit tests completed; inspect failures and coverage gaps' --source EV-001
python3 tools/limen.py check
python3 tools/limen.py report
```

The example assumes a working test suite. A recorded success does **not** imply untested requirements are satisfied. For tier 2, add assumptions, two alternatives, criticism, adverse scenarios and independent security review. Tier 3 is intentionally never auto-approved.

## Records and privacy

`.limen/cases/*.json` tracks decisions; `.limen/evidence/*.log` tracks executed output; `.limen/current` selects a case. Do not commit secrets or sensitive client output into these files. Put `.limen/evidence/` in `.gitignore` unless logs are intentionally reviewed and sanitized. Redact before sharing. The current store is not append-only, independently authenticated or suitable for regulated audit evidence.

## Compatibility notes

- Claude Code hooks/skills: <https://code.claude.com/docs/en/hooks> and <https://code.claude.com/docs/en/skills>
- Skills and hooks do not guarantee the agent follows instructions; validate paths with local tests.
- Does not install, replace or modify anything in your existing project automatically.

## Suggested pilot

Repeat one bounded change with normal Claude Code and with Limen, using the same independent acceptance tests. Compare defects found, untested assumptions, additional verification effort, rework and human time. A single comparison is exploratory, not proof of superiority.
