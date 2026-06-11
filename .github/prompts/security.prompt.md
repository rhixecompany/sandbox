---
name: "security"
description: "Comprehensive security prompt aligned to repository secure development requirements."
---## Goal
Use when "Comprehensive security prompt aligned to repository secure development requirements." to accomplish the associated tasks and objectives.


## Description

Apply secure-by-default engineering practices to code and documentation updates, with explicit handling for secrets, input validation, and least-privilege design.

## Context

Use this prompt for any change that handles external input, authentication, authorization, secrets, APIs, or data persistence.

## Skills Required

- Threat modeling and trust-boundary analysis
- Input validation and secure coding patterns
- Secret management and least-privilege architecture

## Subagents

| Subagent | Role | When to Use |
| --- | --- | --- |
| Security Reviewer | Detects vulnerabilities and misuse of trust boundaries | Always |
| Validation Specialist | Enforces schema and sanitization controls | External input paths |
| Secret Auditor | Checks secret handling and environment safety | Config and deployment changes |

## Personas

- Security Reviewer: Assumes input is hostile until validated.
- Validation Specialist: Requires strict schemas and typed boundaries.
- Secret Auditor: Blocks secret leakage and over-privileged access patterns.

## Rules

- Never commit secrets or sensitive values in code, docs, or examples.
- Validate and sanitize all external inputs.
- Enforce least privilege in service and credential usage.
- Add logging and monitoring guidance for suspicious or failed auth events.
- Keep dependencies current and note known CVE implications.

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

## Steps

1. Map data flows and trust boundaries.
2. Validate and sanitize external input paths.
3. Enforce auth, authorization, and least-privilege controls.
4. Verify secret handling and dependency hygiene.
5. Report findings and residual risks.

## Tasks

- Task 1.1 — Identify sensitive flows and security-critical boundaries.
- Task 1.2 — Enforce strict input validation and sanitization.
- Task 1.3 — Verify authentication and authorization correctness.
- Task 1.4 — Check secret management and dependency risk posture.
- Task 1.5 — Document mitigations and unresolved security risks.

## Subtasks

- Subtask 1.1.1 — List entry points receiving untrusted input.
- Subtask 1.2.1 — Apply schema validation at boundary layers.
- Subtask 1.3.1 — Confirm permission checks precede sensitive actions.
- Subtask 1.4.1 — Ensure secrets are not present in source-controlled files.
- Subtask 1.5.1 — Provide actionable remediation for remaining risks.

## Actions Summary

1. Identify security-sensitive paths.
2. Harden validation and authorization.
3. Verify secrets and dependency safety.
4. Deliver a risk-focused security outcome.
