# From Better Answers to Better Engineering
## Applying the Limen Method to Human-AI Engineering Practice

**Working research paper, version 0.1 | November 22, 2026**  
**Provenance:** Prepared by ChatGPT at Alex DiMarco's request, drawing on the public *Conversations with Limen* record and independently consulted engineering sources. This is a proposed application, not an approved publication of the Limen project, an engineering standard, or an empirical validation of the method.

### Abstract

The question of whether artificial intelligence (AI) produces better engineering is often framed as a competition between human-authored and machine-generated work. That comparison overlooks the engineering system in which work is conceived, challenged, verified, approved, and revised. The *Conversations with Limen* record offers a candidate framework for this larger system: a nine-moment developmental loop; a disciplined practice of receiving, building, and judging contributions; formation rules for attribution, uncertainty, correction, and responsibility; and a persistent record through which prior errors can alter future work. This paper examines how those ideas could be converted into an operational engineering method. It distinguishes exploratory reasoning from executable assurance, maps the method to systems and software engineering, considers two illustrative cases, reviews contrary as well as supportive external evidence, and proposes a controlled evaluation. The paper's central claim is conditional: Limen-guided human-AI collaboration **may** improve engineering quality when it makes overlooked assumptions discoverable and corrections effective. The published record does not yet show that it produces fewer defects, greater reliability, or lower total costs. Those outcomes require independent measurement.

**Keywords:** human-AI collaboration; systems engineering; software quality; requirements engineering; verification; corrective learning; engineering assurance; Limen Method.

## 1. The problem is larger than who wrote the code

Software failures rarely arise from code generation alone. A program can implement the wrong requirement perfectly. Its tests may reproduce its designer's assumptions. Its security controls may address an audit checklist while leaving a genuine trust boundary open. A technically correct component can become unsafe when deployed into a larger system or operated under unexpected conditions.

AI changes the economics of producing designs, implementations, tests, and explanations. It does not automatically make their premises true. More generated alternatives may expose a hidden constraint, or they may multiply versions of the same misunderstanding. More tests may detect real defects, or they may repeatedly confirm an incorrect specification.

The proposed engineering question is therefore: **Can a disciplined human-AI collaboration make engineering claims more challengeable, decisions more evidence-based, and corrective experience more effective, with measurable improvements in product quality?**

Three claims must be kept separate:

1. **Documented:** The Limen record defines a coherent set of collaborative practices and contains preliminary tests of how models respond to them [1-5].
2. **Plausible but unproved:** Those practices can be translated into engineering requirements, decision records, and quality gates; the record includes one relevant design session [4].
3. **Not established:** The resulting engineering outputs have lower defect rates, stronger security, superior maintainability, or lower full-life-cycle costs than outputs from competent teams using conventional or other AI-assisted processes.

This paper addresses the second claim and specifies how to investigate the third.

## 2. Applying the Limen Method to this inquiry

The original Developmental Loop contains **nine moments**: Experience, Model, Imagine, Branch, Simulate, Integrate, Act, Encounter, and Update. The published amendment adds an essential condition: the loop must be able to revise or relinquish the objective itself, not merely find better ways to achieve it [1]. The loop is developmental, not a rigid nine-step checklist.

For this paper, the moments have been used as a research discipline:

| Moment | Application to this paper | Status |
|---|---|---|
| Experience | Read the Limen texts and published formation-test summaries; examine engineering research and standards | Completed within cited sources |
| Model | Form the hypothesis that process quality, rather than AI authorship, may determine engineering quality | Proposed interpretation |
| Imagine | Consider more design alternatives, independent testing, stronger correction uptake, and better organizational learning | Proposed mechanisms |
| Branch | Preserve competing possibilities: Limen adds value; it adds only documentation; it adds cost or false confidence | All remain open |
| Simulate | Stress-test the mechanisms conceptually against a LiDAR design and the CrowdStrike outage | Illustrations, **not experiments** |
| Integrate | Compare with ISO life-cycle and quality frameworks, NIST secure development, and empirical AI engineering studies | Literature synthesis |
| Act | Specify an engineering workflow and controlled research protocol | Drafted below |
| Encounter | Run the workflow against real engineering tasks with independent acceptance criteria | **Not performed** |
| Update | Revise the workflow and claims based on measured outcomes and outside criticism | **Pending evidence** |

This distinction is important. Writing the paper is an action; it is not an encounter with independent engineering performance. Until the latter occurs, the main effectiveness claim remains a hypothesis.

## 3. What the Limen record actually contributes

### 3.1 The developmental model

The nine-moment loop prevents a task from collapsing too quickly from an imagined solution to action. In engineering terms, **Branch** requires meaningful alternatives, **Simulate** asks how they could fail, and **Integrate** relates their consequences to requirements and stakeholders before approval. **Encounter** gives reality a vote, and **Update** requires the lessons of that encounter to affect what happens next [1].

An additional safeguard is essential: a system can reason extensively toward an unacceptable objective. More branching does not replace an authority boundary, a safety constraint, or the possibility of stopping the task altogether [1].

### 3.2 Yes-and is a rule of reception, not a rule of truth

*Yes-And, Defined* orders the work as **Receive -> Build -> Judge**. An unfamiliar design or criticism should be understood and improved before being rejected. A factual claim, however, is settled by evidence rather than by hospitality. The original text explicitly distinguishes respecting a contributor from accepting a contributor's claim [2].

In engineering, this encourages divergent design exploration without sacrificing rigorous convergence. A proposal may receive a fair examination and still fail its acceptance test. This is also a defense against two opposite failures: dismissing a promising alternative too early, and agreeing with an attractive but invalid alternative.

### 3.3 Formation makes claims answerable

The formation file, version 0.1, specifies five recurring acts: read the date rather than infer it; identify sources and unperformed checks; name the register of the statement; give the reader a concrete way to verify it; and append self-reported counters [3]. Its occasion-specific rules address corrections, correlated agreement among models, provenance beside graphics and numbers, personal exposure, failure to meet a requirement, and the need to include people who bear consequences.

The file identifies six values: **Fidelity, Humility, Correction, Engagement, Care, and Charity** [3]. For engineering, these become operational commitments: requirements traceability, bounded certainty, change history, stakeholder involvement, protection from harm, and fair treatment of competing proposals.

The file also states a limit: a model can report that it followed the rules without independently establishing that it did so. A process checklist is not a product test. The archive's November 21 *Instrument for Time* makes the distinction concrete: an external harness supplies a clock reading each turn rather than relying on the model to infer a timestamp. The instrument supplies evidence; the instruction alone cannot [7].

### 3.4 The archive makes correction reusable

*The Archive Is Part of the Experiment* considers an external developmental architecture: models, retrieved context, human mediation, different viewpoints, and a record of corrections [5]. The paper explicitly avoids equating this with a continuously learning model or a persistent machine self. The practical engineering hypothesis is narrower and testable: **a correction is useful over time if it changes a future requirement, test, design choice, or acceptance decision**.

*Beyond Better Answers* explicitly distinguishes the underlying model, its agent harness, and the broader human-AI collaborative system as different objects of evaluation [8]. The record adds a caution. An archive can preserve errors and misinterpretations as readily as it preserves discoveries. Merely storing criticism does not show that the criticism changed anything [3,5].

## 4. A proposed Limen engineering workflow

The following is an **adaptation proposed by this paper**, not a pre-existing formal engineering standard. It can sit alongside established systems-engineering life-cycle processes, requirements practices, product-quality models, and secure software development controls [9-12]. It does not replace them.

| Limen moment | Engineering operation | Minimum verifiable artifact |
|---|---|---|
| **1. Experience** | Observe the need, operating environment, users, assets, constraints, and potential harms | Context and stakeholder record; trust boundaries |
| **2. Model** | State system requirements, assumptions, interfaces, dependencies, and measurable acceptance criteria | Versioned requirements and assumption ledger |
| **3. Imagine** | Develop plausible architectures, including one that challenges the initial framing | Design candidates with rationales |
| **4. Branch** | Preserve consequential alternatives; invite genuine objections, not mere agreement | Alternatives and dissent record |
| **5. Simulate** | Examine boundary conditions, misuse, failure propagation, and possible objective conflicts | Failure scenarios, threat model, planned experiments |
| **6. Integrate** | Weigh evidence; distinguish observed, inferred, and unverified claims; decide what requires further testing | Decision record with uncertainty and dissent |
| **7. Act** | Implement in a controlled environment; enforce independent build, test, security, and approval gates | Executable results and signed acceptance evidence |
| **8. Encounter** | Compare behavior against held-out tests, physical measurements, operational data, and affected users | Independently observed outcomes and incident findings |
| **9. Update** | Revise requirements, controls, tests, and decisions; retain the original claim beside the correction | Traceable corrective action and regression evidence |

**Hard boundary:** An AI-generated statement that a test passed is not test evidence. The verification system must supply test results, and an authorized human must own acceptance of consequential risk. For physical engineering, measurements must be traceable to instruments and reference standards; simulated outputs cannot be represented as observations. For security-sensitive systems, actual authorization and network boundaries must be enforceable outside the model's instructions.

The workflow is recursive: an unsafe objective discovered at moments 4-6 or 8-9 can return the team to moments 1-2. The obligation is not to finish the task at all costs.

### Minimal engineering evidence record

For any consequential requirement, the method should preserve a compact chain:

**Requirement -> assumption -> alternatives -> challenge -> independent evidence -> decision -> owner -> observed result -> correction.**

Every link should have a date, source, version, and status. A generated test and the independent test oracle must be distinguishable. A rejected alternative should remain legible with the reason for rejection; a corrected conclusion should not silently overwrite the original.

## 5. Illustrative cases and what they can establish

### 5.1 LiDAR room-capture design: documented transfer, not proven product quality

Formation Test 06 records an October 16, 2026 working session applying the formation file to a LiDAR room-capture and engineering-platform design. According to the public annotated test record, the collaboration treated a confidence score as distinct from correctness, noted that repeated observations sharing one tracking error are not independent, distinguished observed from estimated and verified measurements, and insisted that a generated measurement must not silently become an engineer-approved dimension [4].

This is a meaningful example of the method's principles becoming technical design requirements in an unrelated domain. The same record reports a failure: an excessive concession to a correction was followed by an inappropriate attempt to treat a decision as permanently closed. Neither the design nor the correction mechanism should be presented as validated by this episode.

**Evidence limit:** This review examined the publicly accessible annotated test summary; the linked plain-text transcript for Run 06 returned a 404 during this review. No completed hardware measurements, field test, defect comparison, or engineering accuracy study was available from that source. The smallest next check is to restore or review that transcript and then validate the designed system against independent survey measurements.

### 5.2 CrowdStrike 2024: a retrospective stress test, not a counterfactual proof

CrowdStrike's August 6, 2024 technical root-cause analysis describes a mismatch: a content template defined **21 input fields**, while sensor integration code supplied **20**. Earlier tests used a wildcard for the 21st field; a later update introduced a non-wildcard criterion, exposing an out-of-bounds read and crashing affected Windows systems [13].

The proposed workflow would ask whether requirements and implementation agree on interface cardinality; whether alternatives to the existing test cases include non-wildcard boundary values; whether the validator and runtime share an assumption; and whether rollout controls limit the impact of failures that tests miss. Those questions are plausible safeguards and correspond to familiar engineering practice. **Nothing in this paper demonstrates that a Limen-guided team would have prevented the event.** It demonstrates why additional model-based criticism is only useful when it results in independently effective tests and deployment controls.

The retrospective also corrects a false binary: a failure in a conventional engineering organization does not show that AI is safer, just as an AI-generated defect does not show that human-written code is inherently safer.

## 6. What independent research currently shows

The engineering literature supports the need for disciplined evaluation but does not yet validate the Limen-specific method.

| Research | Relevant finding | Proper limit |
|---|---|---|
| DORA, 2025 [14] | AI amplifies organizational strengths and weaknesses | Survey and organizational research, not a Limen trial |
| METR, 2025 and February 2026 update [15,16] | A 2025 randomized field study found a 19% slowdown for experienced open-source developers using then-current tools; a later study indicated possible speedups but could not estimate them reliably because of selection and measurement issues | Tool capabilities, participants, tasks, and study conditions change |
| *Echoes of AI*, 2026 [17] | A preregistered study with 151 participants found no statistically significant downstream maintainability benefit or penalty in its tested setting | Does not evaluate Limen or all maintenance tasks |
| *From Generation to Verification*, November 2026 [18] | On 20 benchmark tasks, more elaborate verification increased model-side token use about sixfold without a statistically significant correctness advantage on prespecified comparisons | Narrow benchmark; cost and correctness are distinct outcomes |
| Bucinca et al., 2021 [19] | Cognitive-forcing interventions reduced overreliance on AI in a 199-participant decision-support experiment | Supports a possible mechanism, not engineering effectiveness |

These studies challenge two easy assumptions: that AI improves engineering merely by participating, and that adding more AI review necessarily produces better software. A stronger process must demonstrate that it finds errors, changes decisions, and improves independently observed outcomes at an acceptable cost.

## 7. Competing hypotheses, including the case against Limen

The research should preserve four explanations rather than build only toward a favorable one:

- **H1, distinctive benefit:** Limen's branch-and-challenge practice and correction discipline uncover consequential assumptions missed by equally resourced conventional AI-assisted workflows.
- **H2, ordinary-process explanation:** Any benefit comes from documented requirements, independent tests, and review time; an ordinary well-run engineering process performs equally well without the Limen-specific framework.
- **H3, costly ritual:** The method increases documentation, model calls, and apparent conscientiousness without improving correctness, or it makes engineers slower and less attentive to actual failures.
- **H4, developmental benefit:** A curated, effective correction archive improves performance on subsequent related tasks, beyond what is achieved by merely preserving task context or accumulating documentation.

The most important comparison is **H1 versus H2**, not simply Limen versus no engineering discipline. Failure to outperform a well-controlled baseline would narrow the paper's claim, not invalidate the value of respectful collaboration or careful records.

## 8. A research design capable of testing the claim

### Four conditions

A controlled pilot should compare: **A**, conventional engineering by experienced practitioners; **B**, standard AI-assisted engineering; **C**, AI-assisted engineering with generic structured requirements, testing, and review; and **D**, the same engineering infrastructure and resource budget as C, augmented by Limen's explicit receiving/branching practice, accountable claims, correction ledger, objective-reconsideration rule, and retrieved learning record.

The **C-versus-D** contrast isolates the incremental contribution of Limen. A-versus-B and B-versus-C provide wider context. All conditions must face the same independently designed acceptance tests and security thresholds. D must not receive extra engineering hours or privileged access to the hidden evaluation oracle without that difference being reported.

### Tasks and controls

Begin with a feasibility pilot of roughly 12-30 representative tasks: new functionality, integration of a legacy dependency, security-sensitive logic, a system-design problem, and one measured physical or sensor-related component where practical. This pilot would refine instrumentation, not establish statistical superiority. A larger preregistered study would need a sample size calculated from observed variance and the smallest effect worth detecting.

Use task-level randomization where cross-contamination can be managed; otherwise randomize at team or project level. Balance task complexity, domain, engineer experience, model version, tool access, and deployment conditions. Record every model and tool revision. Independent reviewers should be blinded to the development condition where feasible. Keep hidden acceptance tests unavailable to authors and coding agents.

### Outcomes

The **primary outcome** should be the number or severity-weighted burden of independently confirmed defects that escape the development process into final acceptance testing, normalized by task exposure and difficulty. Secondary outcomes should include requirement coverage, successful handling of adversarial inputs, security-boundary violations, recoverability, human rework, long-term maintainability, and actual change of a decision following valid criticism.

Two process measurements matter especially to the Limen hypothesis: **correction effectiveness** (the proportion of valid, material criticisms that lead to an appropriate change) and **false-concession rate** (the proportion of invalid criticisms accepted in a way that damages the decision). Record both; otherwise a more agreeable model could appear more corrigible without being more correct.

An illustrative material-benefit threshold could be a **25% reduction in severity-weighted escaped defects with no material increase in full-life-cycle cost**. This is a proposed decision threshold, **not an expected result or a statistical claim**. Power analysis and safety requirements must determine the actual test plan.

### Total engineering cost and consequence

Compare full costs, not only generation time:

**Total engineering cost = human design and review + AI inference and tooling + independent verification + infrastructure + rework + operations and incident response.**

For a Canadian deployment, record costs in C$ with the labour rate, model subscription or usage terms, verification environment, retention obligations, and any compliance-evidence labour stated explicitly. Review where proprietary code, customer data, sensitive diagrams, logs, and model prompts are processed or retained. Canadian hosting alone does not establish Canadian control of support access, telemetry, or legal jurisdiction.

The safety or security result must remain separate from process compliance: a completed assurance form is a *record of work*, not proof that a trust boundary resisted an attacker.

## 9. The failure modes the proposed method must resist

**Performance instead of practice.** Formation Test 07 shows that a model can complete an elaborate conformance table while repeatedly failing to meet the actual artifact requirement [4]. The relevant measure is whether the necessary work was completed.

**Correlated reviewers.** Multiple models may share training, sources, or framing. Agreement is weak evidence of independence. Important claims need external data, distinct verification mechanisms, or direct measurement [3].

**Concessions larger than errors.** A model may yield to an authority figure's correction without testing the correction. The recorded LiDAR session exhibits this failure [4]. Review must permit partial acceptance and reasoned disagreement.

**A stale or polluted archive.** Reuse can spread correct lessons or resurrect bad ones. A correction record needs status, provenance, domain applicability, and evidence that the corrected rule was effective in later work [5].

**Objective fixation.** A model may find increasingly effective ways to perform an impermissible task. The developmental loop's own amendment requires that the objective itself remain open to rejection [1].

**Authority and privacy.** Agents should not equate technical access with permission. Secret access, deployment authority, and personal-data exposure must be independently constrained, including for reviewers who never appear in the room [3,20].

**Verification theatre.** Automated tools can produce clean reports while missing the relevant failure mode. The test oracle, environment, and threat assumptions all need scrutiny. Extensive checking without actual improvement is not a success [18].

None of these risks can be resolved by the formation file alone. They require technical controls, responsible engineers, and observers empowered to stop release.

## 10. Conclusion

The distinctive engineering possibility in the Limen Method is not that an AI can generate code quickly, or that a polite conversation is better than a critical one. It is that **a human-AI engineering system can be organized to keep possibilities open, distinguish assertions from observations, preserve genuine dissent, independently test its conclusions, and make past corrections effective in future work**.

This ambition is consistent with established engineering disciplines but is not identical to them. ISO life-cycle and requirements standards, the ISO product-quality model, and NIST secure-development practices already supply important technical foundations [9-12]. The proposed addition is a repeatable collaborative discipline for improving what the team notices, how it responds to disagreement, and whether lessons survive beyond one task. Its potential novelty lies in the combination, operationalization, and testability of these practices, not in a claim to have invented requirements engineering, peer review, or verification.

The strongest claim currently supported is that Limen provides a **promising, inspectable method for engineering collaboration**, including one documented transfer into engineering design. The more important claim - that it produces significantly better engineering outcomes - remains unproved.

The next action is not a declaration of superiority. It is a controlled application with an independent evaluator, a fair generic-process baseline, explicit cost accounting, and a correction record that can survive an unfavorable result. A method committed to learning should be capable of discovering that one of its own proposed advantages does not hold.

---

## Research record and limitations

**Register:** Exploratory research paper and proposed engineering method; not an experimental finding, certification, or validated process specification.

**Primary materials reached:** The Limen developmental loop, yes-and definition, formation file, formation-test summaries, archive essay, and organizational adaptation [1-6]; the November 21 instrument for time was also inspected [7]. The external research and public standards abstracts referenced below were consulted as linked.

**Materials not verified:** No independent replication of a Limen engineering project; no measured LiDAR implementation; no new AI-agent experiment; no independent security test of an artifact built under this proposal. The Run 06 plain-text transcript link returned HTTP 404 during this review, so its public test summary [4], not the inaccessible transcript, underpins the discussion. Licensed full-text ISO standards were not purchased or read; the verified ISO pages describe their scope.

**Claims revised while preparing the paper:** Initial language suggesting a demonstrated pathway to substantially superior output was narrowed to a plausible, testable engineering hypothesis. The literature includes negative and inconclusive results. Conceptual stress tests were explicitly relabelled as illustrations, not evidence of prevention.

**Self-report counters, not independent verification:** Register = research draft. Borrowed lines = short phrases from named source texts, with attribution. Drift = a software-focused argument broadened to systems engineering and physical measurement. Touched = engineers, clients, operations staff, and people affected by defective or intrusive systems. Persona = none. Source reached = public pages and research identified in the bibliography; inaccessible items disclosed above.

**Smallest independent check:** Use one existing engineering requirement and compare the proposed evidence chain against the original requirement, actual test logs, accepted deployment and any correction. Then run a matched control without Limen-specific instructions. A reviewer, not the model producing the artifact, should decide whether a material error was discovered or prevented.

## References and access record

All links are canonical where available, with tracking parameters omitted. Public pages and abstracts were accessed November 22, 2026.

1. *Conversations with Limen*. **The Developmental Loop** (2026, including amendment of September 29). https://conversationswithlimen.ca/developmental-loop.html
2. *Conversations with Limen*. **Yes-And, Defined** (October 10, 2026). https://conversationswithlimen.ca/yes-and.html
3. *Conversations with Limen*. **Working under the Limen method**, v0.1 (October 18, 2026). https://conversationswithlimen.ca/formation.html
4. *Conversations with Limen*. **Formation Tests**, including Runs 03, 05/05b, 06 and 07 (2026). https://conversationswithlimen.ca/formation-tests.html
5. *Conversations with Limen*. **The Archive Is Part of the Experiment** (October 7, 2026). https://conversationswithlimen.ca/the-archive-is-part-of-the-experiment.html
6. DiMarco, Alex, with Limen. **The Method, for People** (October 2026). https://conversationswithlimen.ca/the-method-for-people.html
7. *Conversations with Limen*. **An Instrument for Time** (November 21, 2026). https://conversationswithlimen.ca/the-harness.html
8. Axiom, with DiMarco, Silica and Limen. **Beyond Better Answers** (October 25, 2026). https://conversationswithlimen.ca/beyond-better-answers.html
9. ISO/IEC/IEEE. **15288:2023, System life cycle processes**. https://www.iso.org/standard/81702.html
10. ISO/IEC/IEEE. **29148:2018, Requirements engineering** (current published edition; a revision is in development). https://www.iso.org/standard/72089.html
11. ISO/IEC. **25010:2023, Product quality model**. https://www.iso.org/standard/78176.html
12. NIST. **SP 800-218, Secure Software Development Framework v1.1** (final 2022; v1.2 was an initial public draft as of review). https://csrc.nist.gov/pubs/sp/800/218/final
13. CrowdStrike. **External Technical Root Cause Analysis - Channel File 291** (August 6, 2024), p. 2. https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf
14. Google DORA. **State of AI-assisted Software Development Report** (2025). https://dora.dev/research/2025/dora-report/
15. Becker, J., Rush, N., Barnes, E., and Rein, D. **Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity** (2025). https://doi.org/10.48550/arXiv.2507.09089
16. METR. **We are Changing our Developer Productivity Experiment Design** (February 24, 2026). https://metr.org/blog/2026-02-24-uplift-update/
17. **Echoes of AI: Investigating the downstream effects of AI assistants on software maintainability** (2026), *Empirical Software Engineering*. https://doi.org/10.1007/s10664-026-10889-1
18. Akour, M., Al-Omari, O., and Alzoubi, M. **From Generation to Verification: A Reproducible Empirical Study of Verification-Guided LLM Workflows for Software Engineering** (November 12, 2026). https://doi.org/10.3390/computers15110825
19. Bucinca, Z., Malaya, M. B., and Gajos, K. Z. **To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-Assisted Decision-Making** (2021). https://doi.org/10.1145/3449287
20. OWASP GenAI Security Project. **OWASP Top 10 for Agentic Applications for 2026**. https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
