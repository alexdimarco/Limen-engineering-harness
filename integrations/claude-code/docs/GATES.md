# Engineering assurance tiers (Limen MVP)

| Tier | Examples | Minimum local evidence | Remaining external control |
|---|---|---|---|
| 0 | Documentation, visual naming | Objective | Review as appropriate |
| 1 | Ordinary feature or refactor | Requirement, decision, successful tool-run check, encounter observation | Code review, protected CI as needed |
| 2 | Auth, security, networking, data migration | Tier 1 plus assumption, two alternatives, disposed criticism, adverse scenario, named risk owner | Human approval, negative tests, protected CI, threat-model review |
| 3 | Safety, financial transfer, irreversible or production security change | Local starter **always rejects acceptance** | Independent specialist and protected release governance |

## Non-bypassable boundaries are NOT implemented by the local hook

The Claude Code PreToolUse hook in this package is an advisory `ask` prompt for common `git commit`, `git push` (also with git's own options before the subcommand, such as `git -C <dir> commit`), `terraform apply`, `kubectl apply|delete`, and `helm upgrade` command patterns. In the limen-engineering plugin (from 0.2.0) the same hook acts only in a repository that already keeps a `.limen/` record and uses the plugin's own `limen.py`. It can be bypassed by aliases, another tool, a shell wrapper or direct system access. Its presence is **not** a security control or an assurance of safe deployments. Configure repository branch protection, CI required checks, isolated runner permissions and external approvals separately.

The local evidence log hash detects accidental modification of a log without updating its record. It is **not tamper-proof** when an agent can modify both the log and the record. Do not grant this starter access to production secrets. Successful tests do not automatically prove security, quality, or specification completeness.

Follow the Limen commitments: Fidelity, Humility, Correction, Engagement, Care, Charity. For disputed claims preserve source attribution, uncertainty, opposing evidence and what would change the decision.
