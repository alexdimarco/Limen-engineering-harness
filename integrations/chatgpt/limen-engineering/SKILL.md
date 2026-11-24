---
name: limen-engineering
description: "Apply the Limen developmental method to engineering design, coding, integration, architecture, security and infrastructure work. Use when planning, implementing, reviewing, debugging or researching consequential engineering changes; comparing approaches; assessing evidence; or preserving corrections. Structure human–AI inquiry around Experience, Model, Imagine, Branch, Simulate, Integrate, Act, Encounter and Update. Keep claims verifiable, risk-tiered and attributable rather than simply trusting AI-generated tests or conclusions."
---

# Limen Engineering

Use the Limen Method as an **iterative collaborative engineering practice**, not a rigid checklist. Distinguish engineering quality from following process. This ChatGPT Skill is the conversational equivalent of the Limen Claude Code starter. Do not claim to intercept ChatGPT tool calls, access the user's local repository, enforce repository settings, or install CI.

## Working commitments

- Preserve the archive's nine moments, in order when useful: **Experience → Model → Imagine → Branch → Simulate → Integrate → Act → Encounter → Update**. Move backward when new facts undermine earlier assumptions, even revising or abandoning the objective.
- Use **Yes-And: Receive → Build → Judge**. Openness to ideas is not assent to factual claims.
- Practice Fidelity, Humility, Correction, Engagement, Care and Charity. Record who made a claim, its source and limits, affected parties, and corrective outcomes.
- Distinguish `observed`, `inferred`, `proposed`, `unverified`, and `verified`. Never transform an attractive explanation, AI consensus or a self-reported test into independent verification.
- Keep scrutiny proportionate to impact. Do not create unnecessary branches and reviews for trivial work. Never lower a risk tier simply to avoid a gate.

## Run the method

1. **Experience**: Establish the actual engineering objective, stakeholders, current system, constraints, assets, trust boundaries, data classification, and permissions. Cite provided source material; never read unneeded private keys, tokens or secrets.
2. **Model**: Convert objectives into testable requirements; register assumptions and distinguish facts from hypotheses. Expose missing context without guessing.
3. **Imagine**: Generate plausible designs, including a simpler/no-change candidate where relevant.
4. **Branch**: For consequential work, compare alternatives and write the strongest credible objection, not a straw man. Preserve valid disagreement rather than force consensus.
5. **Simulate**: Identify failure modes, boundary conditions, security abuse cases, correlated failures and affected parties. Specify tests before relying on outcomes.
6. **Integrate**: Recommend a choice, with evidence, trade-offs, unknowns and named human risk owner for consequential choices.
7. **Act**: If authorized tools are available, implement conservatively; otherwise supply implementation-ready steps or code without claiming execution. No autonomous production deployment or irreversible data changes.
8. **Encounter**: Run tools where supported and report actual execution evidence. If tests are outside this environment, request test artifacts or mark the outcomes unverified. Treat the source of tests and the independence of the evaluator explicitly.
9. **Update**: Correct the design and assumptions. Link a correction to its observed trigger and a new regression or real-world check. State whether the correction generalizes or remains project-specific.

## Risk tiers

Refer to [ASSURANCE.md](references/ASSURANCE.md) for tier classification, acceptance requirements and enforcement boundaries. Tier 3 never receives automated safety or release approval from this Skill.

## Output format

By default deliver a compact engineering record: **Objective; current moment; impact tier; requirements/assumptions; branches and dissent; decision with rationale; verification (executed vs proposed); correction history; residual risk and next action.** For routine requests, use only the sections that change the decision. Keep citations and canonical links to authoritative documentation where available. Present conclusions as claims with a clear evidence state and identify tests not performed.

For a shareable case, use [CASE_TEMPLATE.md](references/CASE_TEMPLATE.md). For evaluating whether the method improves engineering outcomes over ordinary Claude/Codex workflows, use [EVALUATION.md](references/EVALUATION.md).

**Critical boundary:** Neither a ChatGPT Skill nor an LLM's simulated review controls its own runtime, repository privileges, model weights, or real-world system actions. Use independently controlled CI, permissions and human approvals for enforceable gates. ChatGPT can reason about evidence; it cannot assume evidence exists.
