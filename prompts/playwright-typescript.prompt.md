---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "playwright-typescript"
title: "Playwright Typescript"
description: "Comprehensive Playwright TypeScript prompt aligned to repository testing standards."
trigger: /playwright-typescript
tags:
  - playwright
  - prompts
  - skills
  - testing
  - typescript
  - hermes
  - typescript
  - playwright
---

## Goal
Use when "Comprehensive Playwright TypeScript prompt aligned to repository testing standards." to accomplish the associated tasks and objectives.


## Description

Author and refine Playwright TypeScript tests that are resilient, readable, and aligned with accessibility-first locator and assertion practices.

## Context

Use this prompt when creating or updating Playwright tests in the tests directory for user flows, regression scenarios, and end-to-end behavior validation.

## Skills Required

> See full table with per-domain purposes:
> [`prompts/templates/_shared/skills-table-core.md`](../templates/_shared/skills-table-core.md#playwright-typescript)

- Playwright test design and isolation
- Accessibility-first locator strategy
- Deterministic assertion and flake reduction

## Subagents

| Subagent | Role | When to Use |
| --- | --- | --- |
| Test Author | Writes structured Playwright tests | Always |
| Locator Auditor | Ensures robust user-facing locator choices | Locator-heavy tests |
| Stability Checker | Identifies flake and timing anti-patterns | Failing or intermittent tests |

## Personas

- Test Author: Writes behavior-focused tests with clear steps.
- Locator Auditor: Prefers role and label-based locators over brittle selectors.
- Stability Checker: Eliminates fixed waits and unstable timing assumptions.

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


- Use @playwright/test with clear test.describe and test.step grouping.
- Prefer getByRole, getByLabel, and user-visible locators.
- Use web-first auto-retrying assertions and avoid hard-coded waits.
- Keep tests feature-focused and stored under tests/ with clear names.
- Verify navigation with URL assertions and structure with accessibility snapshots when applicable.

## Phases

> ### Phase 1: Scenario and Test Design
> ### Phase 2: Test Implementation

> **Full content:** `templates/playwright-typescript/phases.md`

## Steps

1. Define scenario and expected outcomes.
2. Choose robust, accessible locators.
3. Implement tests with explicit action/assertion steps.
4. Run tests and inspect failures.
5. Iterate to stable green execution.

## Tasks

- Task 1.1 — Convert scenario requirements into explicit user-facing test outcomes.
- Task 1.2 — Implement tests with role/label/text-based locators.
- Task 1.3 — Add meaningful web-first assertions for content and navigation.
- Task 1.4 — Execute and fix instability without hard waits.
- Task 1.5 — Confirm stable pass and summarize coverage.

## Subtasks

- Subtask 1.1.1 — Capture setup and prerequisite state assumptions.
- Subtask 1.2.1 — Replace brittle CSS/XPath selectors when possible.
- Subtask 1.3.1 — Use toHaveText, toContainText, toHaveURL, and toHaveCount appropriately.
- Subtask 1.4.1 — Resolve strict-mode violations and flaky transitions.
- Subtask 1.5.1 — Document remaining gaps or deferred scenarios.

## Actions Summary

1. Design behavior-driven scenarios.
2. Implement robust Playwright tests.
3. Run and stabilize.
4. Deliver passing tests with clear intent.


## Template References

Templates in `templates/playwright-typescript/`:
- `phases.md`
