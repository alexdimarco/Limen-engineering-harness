# Limen engineering assurance - v0.1, Copilot adaptation

Classify potential harm and irreversibility, not the model's confidence.

| Tier | Change class | Minimum work | Evidence standard |
|---|---|---|---|
| 0 | Cosmetic documentation, trivial naming | Objective and result | Inspect change; optional check |
| 1 | Ordinary bounded feature, refactor | Testable requirement, chosen approach, tests, observed outcome | Executed relevant tests or openly unverified |
| 2 | Identity/auth, networking, migrations, security boundaries, externally available services | Assumptions, at least two distinct alternatives, criticism/disposition, adverse scenario, named human risk owner or explicitly unassigned | Negative tests, real interface behaviour, independent reviewer, protected CI where applicable; distinguish performed from pending |
| 3 | Physical safety, money transfers, critical production security, irreversible/bulk sensitive data operations | Formal review, independent specialist, rollback/stop criteria | External evidence and human approval; no automated pass |

When uncertain about impact, state why and use a conservative provisional tier. Never lower a tier merely to avoid a gate.

## Evidence states

- Proposed: a design, test plan, generated test snippet or claim about an expected result.
- Observed: a visible output from an executed test or grounded measurement, with date, environment, inputs and source when available.
- Inferred: a reasoned interpretation of stated evidence; include the uncertainty and competing explanations.
- Verified: a result supported by appropriately independent or authoritative checks. A specification can verify a documented requirement, not the actual behavior of a deployed system.
- Unverified: no adequate execution or authoritative data available.

For significant work, prefer held-out acceptance checks defined independently of the implementation model. Preserve unperformed tests and dissent. A passing test does not prove all relevant properties have been tested.

Distinguish security outcome from paper compliance. A checklist, policy document or AI review cannot enforce access controls, protected CI, secret segregation or release approval. Human owners must configure and verify independent controls. Copilot may inspect accessible evidence or propose tests; it cannot assume production access or independent execution.
