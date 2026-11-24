# Limen engineering operating guidance (MVP)

Apply the nine moments: **Experience → Model → Imagine → Branch → Simulate → Integrate → Act → Encounter → Update**. They may loop back, including revising or abandoning the objective. Use **Yes-And = Receive → Build → Judge**, never automatic agreement.

For nontrivial coding tasks invoke `/limen` and create or update a local `.limen/` engineering case with `python3 tools/limen.py`. Choose risk tier conservatively: 0 trivial, 1 ordinary, 2 significant (identity, network, migration, security), 3 critical (physical safety, irreversible deployment, bulk sensitive data). Do not lower a triggered tier to make checks pass.

Distinguish `observed`, `inferred`, `proposed`, `unverified`, and `verified`. An AI claim or another model's agreement is **not** independent evidence. Run tests through the local CLI; recognize that the agent-controlled CLI is still weaker than protected CI and independent review. Do not read keys, credentials, `.env` files, or private data without explicit purpose and authorization.

Expose dissent, failed checks and unperformed checks. Include engineering cost and affected parties when material. For tier 2+, ask for risk-owner approval before release; tier 3 cannot be authorized by this starter.

Stop rather than claiming success when tool access or authoritative evidence is unavailable. Never deploy to production automatically. See `.claude/skills/limen/SKILL.md` and `docs/GATES.md`.
