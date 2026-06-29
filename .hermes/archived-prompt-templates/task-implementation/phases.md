# Phases

> Extracted from `task-implementation.prompt.md`.

## Phases

### Phase 1: Plan Intake and Context Preparation

| Field | Details |
| --- | --- |
| Goal | Fully understand plan scope, details, and tracking expectations before edits. |
| Inputs | Plan files, details files, changes files, referenced source files. |
| Outputs | Sequenced execution roadmap and dependency confirmation. |
| Validation | No task starts without verified plan-details context and file references. |

### Phase 2: Ordered Task Implementation

| Field | Details |
| --- | --- |
| Goal | Implement each task fully with working, validated behavior. |
| Inputs | Task-specific details, existing code patterns, dependencies. |
| Outputs | Completed task implementation and updated checklist status. |
| Validation | Task requirements are met and validated before moving forward. |

### Phase 3: Progressive Tracking and Release Readiness

| Field | Details |
| --- | --- |
| Goal | Keep changes file synchronized and release-ready throughout execution. |
| Inputs | Implemented task deltas, divergence/blocker events, validation outcomes. |
| Outputs | Accurate Added/Modified/Removed tracking and final release summary. |
| Validation | Changes log reflects true state and includes required blockers/divergence notes. |
