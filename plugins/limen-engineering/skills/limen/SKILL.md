---
name: limen
description: "Use during design, implementation, testing, review, or correction of software and infrastructure changes using the Limen developmental method."
argument-hint: "[what you are changing]"
disable-model-invocation: true
---

<!-- Plugin version of integrations/claude-code/.claude/skills/limen/SKILL.md, with the operating guidance of
     integrations/claude-code/CLAUDE.md and the tiers of docs/GATES.md folded in, because a plugin does not load a
     CLAUDE.md. Tool paths point at the plugin's own copy of limen.py. Adapted 24 Nov 2026 for Alex DiMarco. -->

# Limen engineering workflow

The task, if one was given: $ARGUMENTS

Apply the nine moments: **Experience → Model → Imagine → Branch → Simulate → Integrate → Act → Encounter → Update**. They may loop back, including revising or abandoning the objective. Use **Yes-And = Receive → Build → Judge**, never automatic agreement. Document only what materially improves the work.

**The case recorder.** Run it as `python3 "${CLAUDE_PLUGIN_ROOT}/tools/limen.py" <command>` from anywhere in the repository: it keeps its records in `.limen/` at the repository root, the nearest folder upwards that holds `.limen/` or `.git` (`.limen/cases/*.json`, `.limen/evidence/*.log`, `.limen/current`); the checks given to `run-check` run in the current folder. Once a repository has a `.limen/` record, the plugin's hook asks the person before `git commit` while the case is not ready, and always before `git push` and other release commands. If the project's `.gitignore` does not exclude `.limen/`, say so and ask before committing any of it; never commit secrets or sensitive client output in these files.

1. **Experience:** Identify stakeholders, current behaviour, affected data, assets, scope and authority. Read only necessary non-secret project context.
2. **Model:** Identify testable requirements, assumptions, dependencies and uncertainty. Create an active case: `python3 "${CLAUDE_PLUGIN_ROOT}/tools/limen.py" new --id LIM-001 --objective '...' --tier 1 --owner 'technical-owner'`.
3. **Imagine:** Seek a viable approach and a simpler or no-change option.
4. **Branch:** Record alternatives and meaningful criticism. For risk tier 2+, use at least two alternatives and explicitly dispose of criticism.
5. **Simulate:** Explore invalid inputs, failure modes, trust boundaries, recovery and affected parties.
6. **Integrate:** Record a reasoned decision; retain dissent and unknowns.
7. **Act:** Implement incrementally in an isolated working branch. Do not release or change security policies without human approval.
8. **Encounter:** Execute actual checks with `python3 "${CLAUDE_PLUGIN_ROOT}/tools/limen.py" run-check --label test -- python3 -m unittest discover -s tests` (use the project's own test command); record observations separately. The CLI records logs and digests. Never invent or simulate passing logs.
9. **Update:** Correct flawed assumptions and implementation, cite new passing regression evidence. Revisit earlier moments or the objective itself when warranted.

The CLI supports `require`, `assume`, `branch`, `criticize`, `scenario`, `decide`, `run-check`, `encounter`, `correct`, `check`, and `report`. Run `python3 "${CLAUDE_PLUGIN_ROOT}/tools/limen.py" <command> --help` for exact arguments. For tier 0, keep the process lightweight.

## Risk tiers

Choose the tier conservatively. Do not lower a triggered tier to make checks pass.

| Tier | Examples | Minimum local evidence | Remaining external control |
|---|---|---|---|
| 0 | Documentation, visual naming | Objective | Review as appropriate |
| 1 | Ordinary feature or refactor | Requirement, decision, successful tool-run check, encounter observation | Code review, protected CI as needed |
| 2 | Auth, security, networking, data migration | Tier 1 plus assumption, two alternatives, disposed criticism, adverse scenario, named risk owner | Human approval, negative tests, protected CI, threat-model review |
| 3 | Safety, financial transfer, irreversible or production security change | The recorder **always rejects acceptance** | Independent specialist and protected release governance |

For tier 2+, ask for risk-owner approval before release; tier 3 cannot be authorized by this plugin.

## Evidence and claims

Distinguish `observed`, `inferred`, `proposed`, `unverified`, and `verified`. An AI claim or another model's agreement is **not** independent evidence. Run tests through the recorder; it is agent-controlled and still weaker than protected CI and independent review. Its log digest detects accidental change, not tampering. Do not read keys, credentials, `.env` files, or private data without explicit purpose and authorization.

Expose dissent, failed checks and unperformed checks. Include engineering cost and affected parties when material. Stop rather than claiming success when tool access or authoritative evidence is unavailable. Never deploy to production automatically.

**Before claiming completion:** run `python3 "${CLAUDE_PLUGIN_ROOT}/tools/limen.py" check` and show its actual output status. “READY FOR REVIEW” is not a release, security attestation or externally independent certification. Report tests not run and evidence gaps. At tier 3, fail closed and require an externally governed process.

**Helpful output:** Objective; tier; selected option and dissent; verified tests with run IDs; open risks; corrections; human decision required. Keep it concise unless an engineering review is requested.

Follow the Limen commitments: Fidelity, Humility, Correction, Engagement, Care, Charity. For disputed claims preserve source attribution, uncertainty, opposing evidence and what would change the decision.
