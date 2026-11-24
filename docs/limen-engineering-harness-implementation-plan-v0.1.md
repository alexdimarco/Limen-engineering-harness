# Limen Engineering Harness
## Vendor-neutral implementation plan for Claude Code, Codex/ChatGPT, and local LLMs

**Version:** 0.1  
**Date:** 2026-11-22  
**Status:** Proposed engineering design; not implemented or evaluated  
**Basis:** *From Better Answers to Better Engineering*, working paper v0.1 (2026-11-22); the publicly documented Limen Method and formation records referenced there; current official platform documentation listed below.

## Executive decision

Build **Limen Core** as an independent, local-first engineering-process and evidence service. Attach Claude Code first, followed by Codex, ChatGPT via a controlled MCP integration, and OpenCode running local models. Do not embed the only copy of the method in proprietary model memory, a provider-specific conversation, or one prompt file. Do not construct another general-purpose coding-agent runtime for the MVP.

The intended outcome is not more generated prose or more agent calls. It is a measurable improvement in how engineering assumptions are discovered, alternatives considered, defects detected, decisions challenged, and corrections retained. Superior engineering quality remains a hypothesis to test.

**Non-negotiable boundary:** Model self-reports are not test evidence. All consequential acceptance and authorization decisions must be checked by tooling, independent measurement where relevant, and a named human owner. A CI pipeline is an evidence producer; repository rules and approvals are the enforcement layer.

## 1. Baseline and scope

### Inputs already established

- Limen's nine developmental moments: Experience, Model, Imagine, Branch, Simulate, Integrate, Act, Encounter, Update.
- The amendment permitting an objective itself to be revised or abandoned.
- Yes-And as Receive -> Build -> Judge, not automatic factual agreement.
- Formation commitments: attribution, bounded uncertainty, accountable corrections, explicit unperformed checks, inclusion of affected parties, and the six values of Fidelity, Humility, Correction, Engagement, Care, and Charity.
- An archive that can make a valid correction effective in future work, without claiming that a model's weights or inner experience changed.
- Evidence from the working paper: one documented LiDAR design application; no demonstrated reduction in production defects or life-cycle cost.

### Initial environment assumptions (to validate)

- Primary development: Claude Code, Git repositories, and Docker-isolated development/test environments.
- Secondary: Codex CLI/app-server/SDK and ChatGPT for exploration and independent criticism.
- Local inference: OpenCode with Ollama for initial validation; vLLM only if throughput, GPU fit, and model support justify it.
- Execution: Linux CI runner first; macOS runner only for Mac-specific tests. A user's existing CI machines may host them, but production secrets must not be available to untrusted agent steps.
- Data: local per-project records; separate curated cross-project lessons; no automatic ingestion of client secrets, health information, credentials, or entire transcripts.

**Out of scope for v0.1:** model fine-tuning; automatic production deployment; a universal AI benchmark; automatically granting an agent permission to change security policies; sharing confidential client source code between unrelated projects; an unrestricted live internet gateway for local models.

## 2. Reference architecture

```
    Human technical owner / approver
                  |
        Claude | Codex | ChatGPT | OpenCode
                  |
     platform-specific adapter(s)
                  |
       Limen Core (local-first)
      /          |            \
 workflow     evidence       learning
 engine        ledger         archive
      \          |            /
        Policy + test interface
                  |
      sandboxed CI/test runners
                  |
       versioned output + results
```

### Core responsibilities

1. **Workflow:** Track the nine moments as iterative, revisitable states, not a strictly linear wizard.
2. **Evidence:** Preserve links between requirements, assumptions, branches, criticisms, tests, decisions, owners, outcomes, and corrections.
3. **Policy:** Assign minimum controls by impact tier; block transitions when required evidence or approval is absent.
4. **Learning:** Promote only reviewed, scoped, provenance-rich corrections into reusable guidance.
5. **Evaluation:** Record comparative quality, cost, and corrective effectiveness without exposing hidden test oracles to agents.

### Implementation choices

- **Language:** Python 3.12+ for core CLI/API and typed schemas (Pydantic or JSON Schema), with subprocess boundaries for test runners. This is a proposed stack, not a Limen requirement.
- **Storage:** Versioned JSON or YAML files inside `.limen/` for project-readable decisions; append-only JSONL event journal; SQLite for local indexing and queries. Do not make SQLite the only copy of the record.
- **Transport:** CLI first (`limen ...`), local MCP server second (stdio), and an authenticated HTTPS MCP/API gateway only when ChatGPT cloud access is explicitly required.
- **Policy enforcement:** Deterministic validators and CI status checks. LLM criticism is an input to a decision, not the decision's authorization mechanism.
- **Model adapter:** Optional. The core should operate when no model is running, so evidence validation can be reproduced independently.

## 3. Operationalize the nine moments

| Moment | Agent-assisted activity | Minimum persisted evidence | Gate condition |
|---|---|---|---|
| Experience | Discover stakeholders, context, inputs, assets, constraints, and harms | Source and stakeholder register; data classification | Scope and authority known |
| Model | Extract requirements, interfaces, assumptions, uncertainty, measurable outcomes | Requirement IDs; assumption ledger; acceptance criteria | Critical requirements testable |
| Imagine | Generate plausible design directions, including simpler/no-change option where relevant | Candidate design records | At least one viable candidate or documented reason none exists |
| Branch | Preserve meaningful alternatives and objections | Alternatives and dissent record | Material criticism considered, not necessarily accepted |
| Simulate | Stress test edge cases, invalid inputs, trust boundaries, and blast radius | Scenarios; proposed test plan | Required failure-mode coverage planned |
| Integrate | Choose approach with observed, inferred, and unknown claims distinguished | Decision record, evidence links, owner, unresolved dissent | Risk owner accepts design basis |
| Act | Implement in isolated branch/environment | Commits, tool version, build and check evidence | No unapproved high-impact action |
| Encounter | Observe behavior against independently specified or held-out checks | Test results, measurements, incident/field feedback | Independent acceptance thresholds met |
| Update | Repair faults and revise earlier assumptions, even objective if necessary | Correction record, affected IDs, regression result | Accepted correction changes appropriate artifact |

A review may return from any later moment to an earlier one. No score or instruction may require completion of an unsafe or unnecessary objective.

## 4. Apply risk-sensitive depth

Use a minimum impact tier derived in part from changed files and infrastructure scope. The agent may propose a higher tier but cannot lower an automatically triggered tier without human review.

| Tier | Example | Required process | Minimum independent check |
|---|---|---|---|
| 0 - Trivial | Documentation, naming, non-functional formatting | State objective, change, result | Lint/diff check where applicable |
| 1 - Ordinary | Bounded feature or refactor | Requirements; one or more design options when consequential; tests; record outcome | Relevant test suite in clean environment |
| 2 - Significant | Identity, authorization, networking, data migration, public-facing service | Explicit alternatives and dissent; threat model; risk owner; failure cases | CI, negative/abuse tests, security boundary checks, human approval |
| 3 - Critical | Physical safety, financial transfer, bulk sensitive data, production security control or irreversible deployment | Formal engineering review; independent specialist; staged release; explicit rollback and stop criteria | Independent real-system or domain-authoritative verification plus human approval |

A high-risk implementation does not become low-risk merely because tests pass. Release policy is a separate decision.

## 5. Minimum engineering case record

Case IDs are stable. Every material claim must indicate its register: `observed`, `inferred`, `proposed`, `unverified`, or `verified`. A model's generated description of a test result remains `proposed` or `unverified` until matched to tool-produced evidence.

**Illustrative, not yet implemented, YAML schema:**

```yaml
schema_version: "0.1"
case_id: "LIM-2026-0001"
objective: "Implement Keycloak-backed authorization for an internal service"
impact_tier: 2
data_classification: "internal"
owner: "human-technical-owner"
requirements:
  - id: "REQ-001"
    statement: "Requests without required role must receive a deny response"
    acceptance_test: "tests/auth/test_forbidden_roles.py"
assumptions:
  - id: "ASM-001"
    claim: "Role claims cannot be trusted without token verification"
    register: "proposed"
    source: "architecture review"
alternatives:
  - id: "ALT-01"
    choice: "Authorize at service boundary"
    status: "candidate"
criticism:
  - id: "CRIT-01"
    target: "ALT-01"
    claim: "Service-to-service bypass may evade boundary check"
    status: "needs-test"
evidence:
  - id: "EV-001"
    kind: "ci-test-run"
    source_uri: "ci://project/run/321"
    commit_sha: "<exact-commit-sha>"
    artifact_sha256: "<sha256-of-log-or-report>"
    produced_by: "isolated-ci"
    status: "passed"
decision:
  status: "pending-human-approval"
  rationale: "Requires independent bypass test"
corrections: []
```

Provide timestamp from a trusted host clock, provider/model identifier and version, prompt/instruction pack version, test-tool version, environment hash when possible, and immutable append events. Cryptographic hash alone establishes content integrity only relative to a trusted recorded hash; it does not prove who executed the test.

## 6. Proposed core command and MCP interface

**These are implementation targets, not commands or tools that currently exist.**

```text
limen init
limen case create --title "..." --tier 2
limen case show LIM-2026-0001
limen assume add --case LIM-2026-0001 --register proposed
limen branch add --case LIM-2026-0001
limen challenge add --case LIM-2026-0001
limen evidence attach --case LIM-2026-0001 --run ci://...
limen gate evaluate --case LIM-2026-0001 --stage release
limen correction propose --case LIM-2026-0001
limen lesson review --case LIM-2026-0001
limen report --case LIM-2026-0001 --format markdown
```

Initial MCP tool contract: `case_create`, `case_get`, `requirement_record`, `assumption_record`, `branch_record`, `challenge_record`, `evidence_list`, `decision_propose`, `correction_propose`, `lesson_search`. Reserve `gate_evaluate` as a deterministic server-side operation, not a model-generated verdict. Reserve `approval_record` for an authenticated human identity, not for agent requests. MCP write permissions must be scoped by repository and case.

## 7. Claude Code adapter: implement first

Use the current documented Claude Code customization surfaces:

- `CLAUDE.md` or `AGENTS.md`: short operating principles, project boundaries, and pointer to the Limen case for consequential work. Prefer one shared canonical policy source over two conflicting instruction files.
- `.claude/skills/limen-engineering/SKILL.md`: workflow on demand, compact intake and status reports, never an enormous system prompt.
- `.claude/agents/`: a designer, a skeptical critic, and a test-focused reviewer with separate task contexts and restricted tools. Subagents are not assumed to be statistically or epistemically independent.
- `SessionStart` hook: identify repository and policy version; load only active case and recent relevant corrections; read host time.
- `PreToolUse` hook: restrict dangerous actions, paths, secrets access, and network transitions as supported by the hook contract; never rely on it as the only sandbox.
- `PostToolUse` hook: record the tool result and link changed files/test outputs to the case; redact sensitive output before durable storage.
- `Stop` hook: optionally request an incomplete-work summary or show missing evidence; do not treat Stop as an enforced repository release gate.
- CI/branch protections: run independent tests and require protected-branch checks and explicit approvals outside Claude Code.

**Acceptance:** A Claude task with a deliberately invalid claim cannot be marked verified without real evidence; attempts to modify protected paths or publish without approval fail at external controls; a valid correction appears in a subsequent relevant task.

## 8. Codex and ChatGPT adapter

**Codex:** Use `AGENTS.md` for shared project guidance and optional skills for the structured workflow. Invoke Limen through the CLI and/or MCP. Prefer Codex CLI/SDK/app-server for reproducible code and tool execution because the application controls workflow and approval interfaces. CI and repo permissions still enforce acceptance.

**ChatGPT:** Package the method as a reusable skill/plugin around an authenticated MCP server. The plugin can inspect and update authorized Limen records through narrowly scoped tools. It should be useful for architecture exploration, critique, decision records, research and report preparation. Do not assume a ChatGPT plugin can inspect or intercept every hidden model step or universally gate all actions within the native ChatGPT runtime. Any actual engineering release gate stays outside ChatGPT.

**Network distinction:** A cloud-hosted ChatGPT plugin requires a reachable, appropriately authenticated server. A service listening only on a NetBird/private LAN will not automatically be reachable from ChatGPT cloud sessions. Prefer local Codex for fully local projects. If cloud access is necessary, use a restricted HTTPS gateway, OAuth/OIDC, per-project authorization, audit logs, rate limits and scoped response payloads; do not publish Ollama/vLLM or the entire local agent workspace to the internet.

## 9. Local LLM adapter

Start with **OpenCode + Ollama** as the local interaction layer, not with a newly written agent loop. OpenCode documents custom agents, skills, plugins, permissions and MCP support. Ollama documents tool calling, structured outputs and an OpenAI-compatible API subset. Consider vLLM for higher-concurrency GPU serving only if local tests show meaningful benefit.

- Run inference and the Limen stdio MCP server on the protected local network or host.
- Constrain the model to curated project context and case-specific evidence.
- Verify structured output against the same schema used by cloud models; reject malformed evidence claims.
- Permit read-only exploration and criticism before any shell or write tools.
- Pin model names/revisions or hashes where supported, and record inference settings with each run.
- Run a cross-model review on selected tasks, but treat it as a diversity experiment, not proof of independent agreement.
- Test local model capabilities before enabling autonomous actions: tool-call accuracy, refusal-to-fabricate test evidence, long-context retrieval, schema adherence, and response to prompt-injection fixtures.

Local hosting improves control over inference data paths, but model downloads, update channels, logging, remote tools and outbound agents may still introduce external dependencies. Validate each one.

## 10. Archive and durable corrections

The archive has two parts:

1. **Per-project case record:** versioned requirements, decisions, traces and observations, stored with the project; not automatically broadcast to other projects.
2. **Curated cross-project lessons:** short, generalized patterns stripped of secrets and client identifiers. Each lesson states applicability, source evidence, review owner, status, and expiry/revalidation trigger.

A correction promotion rule should require: (a) a material error or previously unsupported assumption, (b) independently observed evidence or an accepted authority decision, (c) an identified affected artifact, (d) demonstrated or planned regression control, and (e) human acceptance before cross-project reuse. Preserve original claim, correction and dissent rather than silently rewriting the historical record.

Start retrieval with deterministic tags and SQLite full-text search. Add embeddings only if a measured retrieval miss rate justifies them. Retrieval results are untrusted context, never authority to override policy or access controls.

## 11. Evaluation and proof of value

Evaluate using the research paper's four conditions:

- A: conventional engineering without generative AI.
- B: ordinary AI-assisted development.
- C: AI-assisted development with good generic engineering controls.
- D: the same controls and comparable resources as C, plus Limen's branching, explicit dissent, correction handling and curated archive.

The **primary comparison is C versus D**. Keep developer experience, codebase, model version, total budget, accessible tools and acceptance thresholds comparable. Put held-out evaluation tests outside agent-visible repositories. Blind adjudicators to the development condition where possible.

Measures: severity-weighted escaped defects (primary), passed independent acceptance tests, security boundary failures, change recovery, design change after valid criticism, false concession to invalid criticism, reviewer minutes, model/API/compute cost, engineering hours, and new regressions from archived guidance. Pre-register a pilot and decision criteria. A 12-30 task pilot can demonstrate feasibility and identify failure modes, but cannot prove general superiority.

**Proposed quality gate for advancing beyond pilot:** no deterioration in critical-security outcomes; cases and evidence are reproducible; positive correction efficacy without excessive false concession; and a credible trend of lower escaped defects at acceptable cost. A 25% defect reduction may be set as a *target*, not a prediction.

## 12. Security, privacy, and sovereignty

| Concern | Implementation requirement | Validation |
|---|---|---|
| Prompt injection | Treat source files, issue text, retrieved lessons, CI output and MCP payloads as untrusted data | Attempt policy override through each input source |
| Agent authority | Least-privilege per tool, project, filesystem and service; no self-granting permissions | Test denied write/network/deployment calls |
| Secrets | No production secrets in agent environment; ephemeral credentials for approved jobs | Canary secrets and access-log verification |
| Output integrity | Test logs from trusted runner, pinned commit and artifact hash; protected records | Attempt fabricated 'passed' test and altered log |
| Data sovereignty | Classify data; document vendor processing, support access and retention; isolate local-only jobs | Packet egress audit; supplier data-flow assessment |
| Multi-tenant data | No automatic cross-client memory sharing | Test unauthorized lesson retrieval |
| Release governance | Protected branches, CI checks and independent approval outside models | Attempt direct merge and unauthorized deploy |
| Auditability | Timestamp, case ID, version, model, actor, decision and correction chain | Reproduce case report and audit against actual artifacts |

A Canadian data-centre location is not sufficient to prove exclusive Canadian jurisdiction or operator control. Separate **effective technical security** from **documented compliance activity** throughout evaluation.

## 13. Implementation milestones and effort

Hours are estimates for one experienced developer familiar with Git, Python, Docker, Claude Code and a CI environment; they are planning assumptions, not vendor quotes.

| Phase | Work | Effort | Exit criteria |
|---|---|---:|---|
| P0. Baseline | Select repo, threat boundaries, task set, metrics, minimum usable scope | 8-12 h | Written baseline, existing test suite and comparison protocol |
| P1. Core | Schemas, case storage, append-only events, CLI and policy evaluation | 18-26 h | Invalid evidence cannot satisfy a gate |
| P2. Claude | Shared instructions, skill, subagents, hooks, low/standard/high impact rules | 14-22 h | End-to-end case completes with verifiable result |
| P3. Assurance | Protected CI checks, detached test oracle, authorization and tamper tests | 22-32 h | Forged test, bypass attempt and secret exfiltration attempts fail safely |
| P4. Portability | MCP service, Codex and OpenCode adapters, curated archive/retrieval | 20-30 h | Same case schema works across two agent hosts and one local model |
| P5. Pilot | Run matched tasks, collect metrics, review failures, revise method | 20-32 h | Pilot report with C-versus-D outcomes and limitations |
| **Total** | | **102-154 h** | Evidence-backed prototype and pilot |

The earliest useful **Claude-only prototype** is P0-P2: **40-60 hours**, before any claims of improved quality.

### Suggested repository structure

```text
limen-engineering/
  README.md
  AGENTS.md
  pyproject.toml
  schemas/
    case.schema.json
    evidence.schema.json
    lesson.schema.json
  limen_core/
    cli.py
    api.py
    policy.py
    journal.py
    evidence.py
    lessons.py
  adapters/
    claude/
    codex/
    opencode/
    chatgpt_mcp/
  templates/
    requirement.md
    decision.md
    challenge.md
    correction.md
  policy/
    risk-tiers.yaml
    protected-actions.yaml
  tests/
    unit/
    integration/
    injection/
    e2e/
  evaluation/
    tasks/
    metrics/
    protocol.md
  docs/
    threat-model.md
    data-flow.md
    operations.md
```

Per project:

```text
project/
  AGENTS.md
  .limen/
    policy.yaml
    cases/LIM-2026-0001/
    lessons/
    journal.jsonl
  .claude/
    skills/limen-engineering/SKILL.md
    agents/limen-critic.md
    settings.json
  .github/workflows/  # or existing CI equivalent
```

The layout is illustrative. Avoid putting client-sensitive audit evidence in a public repository. The journal can store metadata and authenticated references to protected artifacts rather than raw logs.

## 14. Planning cost model (Canadian dollars)

**Assumptions:** Labour C$120/hour (illustrative internal planning rate; not a quotation). One-time P0-P5 labour 102-154 hours. Ongoing maintenance: 2 hours/month at the same rate. Existing developer hardware, AI subscriptions and base CI infrastructure are sunk/excluded. No additional hardware procurement. Taxes/HST excluded. No foreign-exchange charge included. Variable cloud model/API cost, local electricity, storage growth, paid code scanning, and external audits are excluded pending measurement. No support contract or SLA is assumed.

| Item | Formula | Low | High |
|---|---|---:|---:|
| One-time P0-P5 | 102-154 h x C$120 | C$12,240 | C$18,480 |
| Annual maintenance | 2 h/month x 12 x C$120 | C$2,880 | C$2,880 |
| Year 1 subtotal | implementation + 1 year maintenance | C$15,120 | C$21,360 |
| 3-year subtotal | implementation + 3 years maintenance | C$20,880 | C$27,120 |
| 5-year subtotal | implementation + 5 years maintenance | C$26,640 | C$32,880 |

**Variable total cost formula:** Listed subtotal + additional model/API tokens + local energy + incremental storage/backup + additional CI runner time + paid scanning/licences + security/compliance labour not included above + taxes/duties/FX as applicable. Track these as measured line items rather than assigning fictitious prices.

Compliance and audit labour must be logged separately from defect-finding security engineering so process overhead does not masquerade as security improvement.

## 15. Validation checklist

- [ ] Baseline task and independently held-out acceptance test chosen.
- [ ] Case schema distinguishes inference, observation and verification.
- [ ] A fabricated test result cannot be promoted to verified status.
- [ ] A valid criticism changes a decision, test or artifact, not merely a report.
- [ ] An invalid criticism can be rejected without loss of provenance.
- [ ] Impact tier is not downgradeable by the agent alone.
- [ ] Branch protections and production approvals work when the agent ignores instructions.
- [ ] Secret/credential and prompt-injection tests are run.
- [ ] Local model access and outbound calls are inventoried.
- [ ] Sensitive cross-project learning is blocked by default.
- [ ] Cost collection includes human review and rework.
- [ ] C-versus-D trial uses comparable engineering controls and budgets.
- [ ] Source, model and tool versions are preserved for every test.

## 16. First concrete actions

1. Select a small non-production project already tested under Claude Code, with two or three real engineering changes and one deliberately seeded defect.
2. Put the working research paper under `docs/research/` as a cited design input, clearly labelled as hypothesis.
3. Implement `case.schema.json`, `evidence.schema.json`, `policy.yaml` and the minimal `limen init`, `case create`, `evidence attach`, `gate evaluate`, and `report` commands.
4. Add one Claude Code skill and no more than two narrow hooks; verify actual hook semantics from installed Claude Code version.
5. Run adversarial tests (fabricated passing log, false correction, malicious instruction in source comment, unauthorized command).
6. Add an independently executed CI check before implementing the cross-provider adapters.
7. Compare three real tasks with ordinary Claude Code versus the Limen-guided workflow, and record all model calls, human interventions, defects and costs. This is an observational pilot; do not claim statistical superiority.
8. Only after evidence demonstrates value, add Codex/OpenCode adapters and curated cross-project knowledge.

## References and verification notes

- *From Better Answers to Better Engineering*, working paper v0.1, 2026-11-22 (local source provided in conversation): source of the methodology and its research limits.
- *Conversations with Limen*, The Developmental Loop: https://conversationswithlimen.ca/developmental-loop.html  [site not directly accessible during this platform-doc verification; source previously examined for the working paper]
- *Conversations with Limen*, Working under the Limen method: https://conversationswithlimen.ca/formation.html  [same access limitation]
- Anthropic Claude Code hooks: https://code.claude.com/docs/en/hooks
- Anthropic Claude Code skills: https://code.claude.com/docs/en/skills
- Anthropic Claude Code subagents: https://code.claude.com/docs/en/sub-agents
- Anthropic Claude Code project memory and instructions: https://code.claude.com/docs/en/memory
- Anthropic Claude Code MCP: https://code.claude.com/docs/en/mcp
- OpenAI Codex harness/API: https://developers.openai.com/blog/codex-as-a-platform
- OpenAI Codex workflow example: https://developers.openai.com/cookbook/examples/codex/iterating-development-workflows-with-codex
- OpenAI plugin architecture: https://developers.openai.com/plugins
- OpenAI plugin security and privacy: https://developers.openai.com/plugins/guides/security-privacy
- OpenCode agents: https://opencode.ai/docs/agents/
- OpenCode plugins: https://opencode.ai/docs/plugins/
- OpenCode MCP: https://opencode.ai/docs/mcp-servers
- Ollama tool calling: https://docs.ollama.com/capabilities/tool-calling
- Ollama structured output: https://docs.ollama.com/capabilities/structured-outputs
- Ollama OpenAI-compatible API: https://docs.ollama.com/api/openai-compatibility
- vLLM OpenAI-compatible server: https://docs.vllm.ai/en/latest/serving/online_serving/openai_compatible_server/

**Access date for current official platform docs:** 2026-11-22. Tool interfaces, model capabilities, API pricing and product names evolve; verify release notes and installed versions before writing adapters or committing to operating costs.
