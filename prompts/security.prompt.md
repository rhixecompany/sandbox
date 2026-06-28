---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "security"
title: "Security Review"
description: "Comprehensive prompt for security review, vulnerability assessment, and secure coding practices."
trigger: /security
tags:
  - hermes
  - security
  - review
  - code-quality
---

## Goal
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

> ### Phase 1: Threat Surface Identification
> ### Phase 2: Security Control Implementation

> **Full content:** `templates/security/phases.md`

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


## Template References

Templates in `templates/security/`:
- `phases.md`
