---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Hermes Breakdown Test
name: hermes-breakdown-test
description: "Hermes-equivalent: generate a test strategy, issue checklist, and QA plan from feature artifacts."
tags: []
---

## Goal

Produce a QA package that turns feature artifacts into a clear test strategy and issue checklist.

## Context

- Use when feature planning needs QA structure and test coverage guidance.
- Prefer concrete, implementation-aware but not implementation-bound test planning.
- Keep the output useful for QA, engineering, and issue triage.
- Align the strategy with the available feature artifacts.

## Inputs

- Feature PRD path
- `technical-breakdown.md`
- `implementation-plan.md` (recommended)

## Outputs

- `/docs/ways-of-work/plan/{epic}/{feature}/test-strategy.md`
- `/docs/ways-of-work/plan/{epic}/{feature}/test-issues-checklist.md`
- `/docs/ways-of-work/plan/{epic}/{feature}/qa-plan.md`

## Rules

1. Include test scope and quality-risk mapping.
2. Use ISTQB-style technique selection where helpful.
3. Map the feature to ISO25010 quality characteristics.
4. Include environment, data, and CI/CD considerations.
5. Provide concrete issue templates for unit, integration, e2e, performance, and security coverage.
6. Include labeling and prioritization guidance.

## Phases

> ### Phase 1: Read the feature artifacts
> **Goal:** understand the feature and the likely QA surface.

> **Full content:** `templates/hermes-breakdown-test/phases.md`

## Actions Summary

1. Read the feature artifacts.
2. Draft the test strategy, checklist, and QA plan.
3. Add risk mapping and coverage guidance.
4. Verify completeness and path correctness.


## Template References

Templates in `templates/hermes-breakdown-test/`:
- `phases.md`
