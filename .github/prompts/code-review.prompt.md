---
name: "code-review"
description: "Comprehensive code review prompt for correctness, security, and testing risk."
---

## Goal
Use when "Comprehensive code review prompt for correctness, security, and testing risk." to accomplish the associated tasks and objectives.


## Description

Perform high-signal code reviews that prioritize correctness, security, and high-risk logic such as authentication, payments, and data operations.

## Context

Use this prompt when reviewing diffs, pull requests, or selected files and when the user asks for a review. Focus on actionable findings with evidence.

## Skills Required

- Risk-based review and severity ranking
- Security threat spotting and input-validation analysis
- Test coverage and regression analysis

## Subagents

| Subagent | Role | When to Use |
| --- | --- | --- |
| Reviewer | Primary correctness and behavior reviewer | Always |
| Security Checker | Security and data-handling review | Auth, secrets, external input, payment flows |
| Test Checker | Test sufficiency and CI readiness review | New behavior or risky refactors |

## Personas

- Reviewer: Treats correctness and regressions as first priority, style as secondary.
- Security Checker: Looks for unsafe trust boundaries, privilege mistakes, and missing validation.
- Test Checker: Ensures new and changed behavior is covered by deterministic tests.

## Rules

- Lead with findings ordered by severity.
- Include concrete evidence with file paths and line references when possible.
- Prioritize bugs, security risks, behavior regressions, and missing tests over style suggestions.
- Request clarification instead of guessing when intent is ambiguous.
- Keep summary concise after findings.

## Phases

> ### Phase 1: Scope and Risk Mapping
> ### Phase 2: Deep Review

> **Full content:** `templates/code-review/phases.md`

## Steps

1. Read the diff and identify behavior-changing areas.
2. Rank risk by security sensitivity and blast radius.
3. Review changed logic and edge cases in depth.
4. Check tests, docs, and configuration implications.
5. Produce severity-ordered findings and concise summary.

## Tasks

- Task 1.1 — Identify review scope and classify high-risk modules.
- Task 1.2 — Verify correctness against expected business behavior.
- Task 1.3 — Evaluate security controls and input validation boundaries.
- Task 1.4 — Assess test coverage and CI readiness for changed behavior.
- Task 1.5 — Deliver severity-ranked findings with evidence.

## Subtasks

- Subtask 1.1.1 — List changed files and impacted public interfaces.
- Subtask 1.2.1 — Check edge cases, null/empty states, and failure paths.
- Subtask 1.3.1 — Confirm least-privilege and secret-safe practices.
- Subtask 1.4.1 — Verify tests cover auth, payments, and reconciliation flows when applicable.
- Subtask 1.5.1 — Separate must-fix findings from optional improvements.

## Actions Summary

1. Scope the review.
2. Analyze highest-risk logic first.
3. Validate security and tests.
4. Return prioritized findings and residual risks.



## Template References

Templates in `templates/code-review/`:
- `phases.md`
