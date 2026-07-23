# Phases

> Extracted from `generator-orchestrator.prompt.md`.

## Phases

### Phase 1: Discovery

| Field | Details |
| --- | --- |
| Goal | Inventory and classify the 11 root generator prompts by role and dependency. |
| Inputs | Prompt inventory from `.github/prompts` and explicit root generator list. |
| Outputs | Classification map: analysis, documentation, code-generation; dependency edge list. |
| Validation | Confirm exactly 11 root prompts are in scope and no excluded prompt is referenced. |

### Phase 2: Contract Design

| Field | Details |
| --- | --- |
| Goal | Define deterministic orchestration contract (inputs, defaults, outputs, and mode behavior). |
| Inputs | User parameters and deterministic default matrix. |
| Outputs | Normalized run configuration and expected output schema. |
| Validation | Verify full, quick, and custom modes each resolve to unambiguous stage plans. |

### Phase 3: Execution Graph

| Field | Details |
| --- | --- |
| Goal | Execute Stage A-E graph with dependency-aware ordering and gates. |
| Inputs | Normalized run configuration and dependency graph from prior phases. |
| Outputs | Generated docs/code artifacts and per-stage gate results. |
| Validation | Each stage references only artifacts from completed prerequisite stages. |

### Phase 4: Safety and Recovery

| Field | Details |
| --- | --- |
| Goal | Apply fallback, retry, degraded-mode, and handoff-fail policies consistently. |
| Inputs | Stage outputs, validation failures, and ambiguity signals. |
| Outputs | Retry logs, degraded-mode warnings, and remediation checklist when required. |
| Validation | Confirm ambiguous detection, missing sections, and inconsistency cases are all handled explicitly. |

### Phase 5: Verification and Handoff

| Field | Details |
| --- | --- |
| Goal | Consolidate artifacts, run consistency validation, and issue final pass/fail handoff decision. |
| Inputs | Complete stage outputs and all gate reports. |
| Outputs | Final artifact manifest, consistency results, and execution summary. |
| Validation | Fail handoff if cross-document inconsistencies remain unresolved. |
