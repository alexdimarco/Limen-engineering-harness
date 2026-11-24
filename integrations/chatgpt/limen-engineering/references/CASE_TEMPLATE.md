# Limen engineering case template — common core format

This starter uses the **same case field names** as the Claude Code local CLI, so individual cases can be compared. No automatic synchronization, API, or shared data store has been installed. ChatGPT should produce structured records only for facts supported by the conversation, tool outputs and attachments.

```json
{
  "schema_version": "0.1",
  "case_id": "LIM-EXAMPLE-001",
  "objective": "Testable engineering objective",
  "impact_tier": 1,
  "owner": "human-technical-owner",
  "moments": ["Experience", "Model", "Imagine", "Branch", "Simulate", "Integrate", "Act", "Encounter", "Update"],
  "requirements": [{"id": "REQ-001", "statement": "...", "acceptance": "..."}],
  "assumptions": [{"id": "ASM-001", "statement": "...", "source": "...", "status": "unverified"}],
  "alternatives": [{"id": "ALT-001", "description": "..."}],
  "criticisms": [{"id": "CRIT-001", "target": "ALT-001", "text": "...", "disposition": "unresolved", "reason": ""}],
  "scenarios": [{"id": "SCN-001", "description": "...", "expected": "..."}],
  "decision": {"choice": "...", "rationale": "...", "owner": "human-technical-owner", "recorded_at": "..."},
  "evidence": [],
  "encounters": [{"id": "OBS-001", "observation": "...", "source": "..."}],
  "corrections": [],
  "created_at": "...",
  "updated_at": "..."
}
```

Evidence records in the local CLI have `id`, `label`, `command`, `exit_code`, `sha256`, `log`, `recorded_at`. In ChatGPT, **do not invent these fields** without a real tool run and accessible log. Leave `evidence: []` if no authoritative test was performed; explain why the result remains unverified. Never fill timestamps with fabricated observations.

For notes about affected parties, data classification, privacy, interpretation of sources and unresolved dissent, preserve those separately in the analysis or in an explicitly marked supporting note. The CLI v0.1 stores only this minimum core; expanding its schema is a later project.

The CLI's `check` is a **local readiness indicator**, not a release approval. Only trusted CI with protected approvals can supply an enforceable external status.
