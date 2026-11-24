# Limen engineering case template - common core v0.1

Use the same case field names as the Limen Claude Code starter to support manual comparison. No automatic synchronization, shared data store or API is installed. Only include facts supported by actual input or authorized visible tool results. For a human-readable record, use the equivalent headings from the main instructions.

```json
{
  "schema_version": "0.1",
  "case_id": "LIM-EXAMPLE-001",
  "objective": "Testable engineering objective",
  "impact_tier": 1,
  "owner": "unassigned",
  "moments": ["Experience", "Model", "Imagine", "Branch", "Simulate", "Integrate", "Act", "Encounter", "Update"],
  "requirements": [{"id": "REQ-001", "statement": "...", "acceptance": "..."}],
  "assumptions": [{"id": "ASM-001", "statement": "...", "source": "...", "status": "unverified"}],
  "alternatives": [{"id": "ALT-001", "description": "..."}],
  "criticisms": [{"id": "CRIT-001", "target": "ALT-001", "text": "...", "disposition": "unresolved", "reason": ""}],
  "scenarios": [{"id": "SCN-001", "description": "...", "expected": "..."}],
  "decision": {"choice": "...", "rationale": "...", "owner": "unassigned", "recorded_at": "..."},
  "evidence": [],
  "encounters": [{"id": "OBS-001", "observation": "...", "source": "..."}],
  "corrections": [],
  "created_at": "...",
  "updated_at": "..."
}
```

The example is illustrative, not an actual case. The local CLI evidence fields are id, label, command, exit_code, sha256, log, recorded_at. Do not invent them without a real tool run and accessible log. Leave evidence empty if no authoritative test evidence exists; explain why verification remains pending. Do not fabricate timestamps, owners, sources, results or completed moments. Record document references and other evidence as supporting notes if they do not fit the core schema. Keep affected parties, privacy, classification and unresolved dissent as supporting notes. Do not claim a record was persisted unless a supported, authorized action actually succeeded.
