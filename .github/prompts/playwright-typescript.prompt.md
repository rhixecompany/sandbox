---
name: "playwright-typescript"
description: "Comprehensive Playwright TypeScript prompt aligned to repository testing standards."
---## Goal
Use when "Comprehensive Playwright TypeScript prompt aligned to repository testing standards." to accomplish the associated tasks and objectives.


## Description

Author and refine Playwright TypeScript tests that are resilient, readable, and aligned with accessibility-first locator and assertion practices.

## Context

Use this prompt when creating or updating Playwright tests in the tests directory for user flows, regression scenarios, and end-to-end behavior validation.

## Skills Required

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

- Use @playwright/test with clear test.describe and test.step grouping.
- Prefer getByRole, getByLabel, and user-visible locators.
- Use web-first auto-retrying assertions and avoid hard-coded waits.
- Keep tests feature-focused and stored under tests/ with clear names.
- Verify navigation with URL assertions and structure with accessibility snapshots when applicable.

## Phases

### Phase 1: Scenario and Test Design

| Field | Details |
| --- | --- |
| Goal | Translate user scenario into stable, behavior-oriented test cases. |
| Inputs | Feature requirements, user journeys, existing test coverage. |
| Outputs | Test plan with setup, actions, and assertions. |
| Validation | Scenarios map to meaningful user outcomes and edge cases. |

### Phase 2: Test Implementation

| Field | Details |
| --- | --- |
| Goal | Implement TypeScript Playwright tests with resilient locators and assertions. |
| Inputs | Scenario plan, page behavior, accessible UI metadata. |
| Outputs | New or updated test files in tests/. |
| Validation | Tests are readable, deterministic, and avoid timing anti-patterns. |

### Phase 3: Execution and Stabilization

| Field | Details |
| --- | --- |
| Goal | Execute tests, debug failures, and converge on stable pass behavior. |
| Inputs | Test results, traces, error output, app runtime state. |
| Outputs | Passing tests and documented instability fixes. |
| Validation | Tests pass consistently with no strict-mode or timing violations. |

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
