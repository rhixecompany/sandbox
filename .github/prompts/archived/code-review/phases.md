# Phases

> Extracted from `code-review.prompt.md`.

## Phases

### Phase 1: Scope and Risk Mapping

| Field | Details |
| --- | --- |
| Goal | Understand change scope and identify high-risk areas before deep review. |
| Inputs | Diff, changed files, related tests, architecture context. |
| Outputs | Scoped review plan and prioritized risk checklist. |
| Validation | Scope boundaries and risk categories are explicitly listed. |

### Phase 2: Deep Review

| Field | Details |
| --- | --- |
| Goal | Evaluate correctness, security, and maintainability of changed behavior. |
| Inputs | Implementation files, tests, configuration changes, dependency changes. |
| Outputs | Verified findings with severity and evidence. |
| Validation | Each finding has rationale and impact; false positives are filtered out. |

### Phase 3: Testing and Delivery Check

| Field | Details |
| --- | --- |
| Goal | Ensure tests and verification are sufficient for the change risk level. |
| Inputs | Existing tests, newly added tests, CI expectations. |
| Outputs | Test-gap findings and release-readiness note. |
| Validation | Critical flows are covered or explicitly marked as risk gaps. |
