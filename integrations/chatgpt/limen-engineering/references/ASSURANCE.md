# Limen engineering assurance — v0.1

Risk tiers refer to potential harm and irreversibility, not the model's confidence.

| Tier | Change class | Minimum work | Evidence standard |
|---|---|---|---|
| 0 | Cosmetic documentation, trivial naming | State objective and result | Inspect diff, optional check |
| 1 | Ordinary bounded feature, refactor | Testable requirement, selected approach, tests, observed outcome | Executed relevant tests or openly unverified |
| 2 | Identity/auth, networking, migrations, security boundaries, externally available services | Register assumptions, two distinct alternatives, criticism and disposition, adverse scenario, named risk owner | Negative tests, real interface behaviour, independent reviewer, protected CI where applicable |
| 3 | Physical safety, money transfers, critical production security, irreversible/bulk sensitive data operations | Formal review, independent specialist, rollback/stop criteria | External authority and human approval; **no automated pass** |

## The limits of an assistant's evidence

- **Proposed:** A test plan, generated test snippet or claim about the expected result.
- **Observed:** A visible output from an executed test or a grounded measurement, with date, environment, inputs and source.
- **Verified:** A result with appropriate independent or authoritative checks; do not use this label for claims solely based on the model's own output.
- **Unverified:** No reliable execution or authoritative data available.

For significant work, prefer held-out acceptance checks defined outside the implementation agent's context. Separate baseline from inference; a passing test is never proof that all relevant properties have been tested. Retain dissent and unperformed checks.

Security outcome is distinct from paper compliance: producing a threat model does not show that access boundaries hold. A checklist cannot enforce repository permissions, CI protection, secret segregation, or release approval.
