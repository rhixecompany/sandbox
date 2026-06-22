# Phases

> Extracted from `security.prompt.md`.

## Phases

### Phase 1: Threat Surface Identification

| Field | Details |
| --- | --- |
| Goal | Identify trust boundaries, sensitive assets, and attack surfaces. |
| Inputs | Changed files, input paths, auth flows, config and dependency updates. |
| Outputs | Risk map with prioritized security concerns. |
| Validation | All external input and sensitive data flows are explicitly traced. |

### Phase 2: Security Control Implementation

| Field | Details |
| --- | --- |
| Goal | Implement or verify controls for validation, authorization, and secret safety. |
| Inputs | Risk map, code paths, policy requirements. |
| Outputs | Hardened implementation and explicit security notes. |
| Validation | Controls are enforced at boundaries and failure handling is deterministic. |

### Phase 3: Verification and Hardening Review

| Field | Details |
| --- | --- |
| Goal | Confirm no obvious vulnerabilities remain in changed scope. |
| Inputs | Updated code, tests, logs, and dependency metadata. |
| Outputs | Security verification summary and residual-risk callouts. |
| Validation | High-risk issues are fixed or explicitly flagged with mitigation path. |
