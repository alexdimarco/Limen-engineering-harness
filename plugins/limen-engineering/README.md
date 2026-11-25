# limen-engineering (Claude Code plugin)

The `/limen` skill of the Limen Engineering Harness, packaged as a Claude Code plugin.

- **Skill:** `skills/limen/SKILL.md`, the nine moments, the risk tiers and the evidence rules. It runs only when you
  type it: `/limen-engineering:limen` (or `/limen` when no other command has that name), optionally followed by the
  task.
- **Case recorder:** `tools/limen.py`, standard-library Python 3 (tested with 3.9.6 and 3.12). It keeps decisions and
  tool-run test evidence in `.limen/` at the repository root (the nearest folder upwards with `.limen/` or `.git`). It is a byte-for-byte copy of
  `integrations/claude-code/tools/limen.py`; a unit test in `integrations/claude-code/tests/` keeps the two identical.
- **Hook (from 0.2.0):** `hooks/pretool.py`, the starter's advisory check (a byte-for-byte copy, kept identical by a
  test). It acts only in a repository that already keeps a Limen record (`.limen/`), and it uses the plugin's own
  `tools/limen.py`, never the project's. There it asks before `git commit` while the case is not ready (with the
  reason) and always before `git push`, `terraform apply`, `kubectl apply|delete` and `helm upgrade`. It is review
  friction, not access control. Where a managed policy allows only managed hooks (`allowManagedHooksOnly`), Claude
  Code does not run it.

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
