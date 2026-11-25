# limen-engineering (Claude Code plugin)

The `/limen` skill of the Limen Engineering Harness, packaged as a Claude Code plugin.

- **Skill:** `skills/limen/SKILL.md`, the nine moments, the risk tiers and the evidence rules. It runs only when you
  type it: `/limen-engineering:limen` (or `/limen` when no other command has that name), optionally followed by the
  task.
- **Case recorder:** `tools/limen.py`, standard-library Python 3 (tested with 3.9.6). It keeps decisions and
  tool-run test evidence in `.limen/` in the folder it runs from. It is a byte-for-byte copy of
  `integrations/claude-code/tools/limen.py`; a unit test in `integrations/claude-code/tests/` keeps the two identical.
- **No hook.** The advisory commit check of the copy-in starter (`integrations/claude-code/.claude/hooks/pretool.py`) is
  not part of this plugin.

## Install

```sh
claude plugin marketplace add alexdimarco/Limen-engineering-harness
claude plugin install limen-engineering@limen-engineering-harness
```

## Limits

The recorder is not a security sandbox, a release authorization or independent CI. Its records are local, editable by
the agent that writes them, and not suitable as regulated audit evidence. See `docs/GATES.md` in
`integrations/claude-code/`.

MIT licence (see `LICENSING.md` at the repository root).
