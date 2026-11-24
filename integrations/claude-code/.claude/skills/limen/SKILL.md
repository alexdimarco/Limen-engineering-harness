---
name: limen
description: "Use during design, implementation, testing, review, or correction of software and infrastructure changes using the Limen developmental method."
---

# Limen engineering workflow

Work through the **nine moments**; document only what materially improves the work:

1. **Experience:** Identify stakeholders, current behaviour, affected data, assets, scope and authority. Read only necessary non-secret project context.
2. **Model:** Identify testable requirements, assumptions, dependencies and uncertainty. Create an active case: `python3 tools/limen.py new --id LIM-001 --objective '...' --tier 1 --owner 'technical-owner'`.
3. **Imagine:** Seek a viable approach and a simpler or no-change option.
4. **Branch:** Record alternatives and meaningful criticism. For risk tier 2+, use at least two alternatives and explicitly dispose of criticism.
5. **Simulate:** Explore invalid inputs, failure modes, trust boundaries, recovery and affected parties.
6. **Integrate:** Record a reasoned decision; retain dissent and unknowns.
7. **Act:** Implement incrementally in an isolated working branch. Do not release or change security policies without human approval.
8. **Encounter:** Execute actual checks with `python3 tools/limen.py run-check --label test -- python3 -m unittest discover -s tests`; record observations separately. The CLI records logs and digests. Never invent or simulate passing logs.
9. **Update:** Correct flawed assumptions and implementation, cite new passing regression evidence. Revisit earlier moments or the objective itself when warranted.

The CLI supports `require`, `assume`, `branch`, `criticize`, `scenario`, `decide`, `run-check`, `encounter`, `correct`, `check`, and `report`. Run `python3 tools/limen.py <command> --help` for exact arguments. For tier 0, keep the process lightweight.

**Before claiming completion:** run `python3 tools/limen.py check` and show its actual output status. “READY FOR REVIEW” is not a release, security attestation or externally independent certification. Report tests not run and evidence gaps. At tier 3, fail closed and require an externally governed process.

**Helpful output:** Objective; tier; selected option and dissent; verified tests with run IDs; open risks; corrections; human decision required. Keep it concise unless an engineering review is requested.
