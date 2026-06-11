---
name: "testing"
description: "Comprehensive testing prompt aligned to repository unit and E2E guidance."
---## Goal
Use when "Comprehensive testing prompt aligned to repository unit and E2E guidance." to accomplish the associated tasks and objectives.


## Description

Create, update, and validate tests that provide deterministic coverage for public behavior and critical flows such as authentication, payments, and reconciliation.

## Context

Use this prompt for tests under tests/ and for planning or reviewing validation strategy for changed behavior.

## Skills Required

- Unit and integration test design
- E2E flow verification with environment constraints
- Deterministic test isolation and mocking

## Subagents

| Subagent | Role | When to Use |
| --- | --- | --- |
| Unit Test Author | Builds focused deterministic unit tests | Business logic changes |
| E2E Test Author | Builds realistic end-to-end scenarios | User flow changes |
| Test Reliability Reviewer | Removes flakes and env coupling | Intermittent failures |

## Personas

- Unit Test Author: Maximizes signal-to-noise with small focused tests.
- E2E Test Author: Validates critical user journeys in realistic conditions.
- Test Reliability Reviewer: Eliminates nondeterminism and fragile assumptions.

## Rules

- Prefer fast deterministic unit tests with mocked external dependencies.
- Cover critical paths and public behavior changes.
- Run Playwright E2E against expected local test server conditions.
- Keep test files focused and readable.
- Ensure CI-relevant commands and prerequisites are respected.

## Phases

### Phase 1: Coverage Planning

| Field | Details |
| --- | --- |
| Goal | Determine test scope and identify critical behavior to verify. |
| Inputs | Feature changes, risk areas, existing tests, acceptance criteria. |
| Outputs | Test plan covering unit and E2E scope as needed. |
| Validation | Critical flows and regressions have explicit test intent. |

### Phase 2: Test Authoring

| Field | Details |
| --- | --- |
| Goal | Implement tests that are clear, deterministic, and behavior-focused. |
| Inputs | Test plan, fixtures, mocks, runtime constraints. |
| Outputs | New or updated tests in correct locations. |
| Validation | Tests avoid flaky timing assumptions and external coupling. |

### Phase 3: Execution and Gap Closure

| Field | Details |
| --- | --- |
| Goal | Execute tests, fix failures, and close meaningful coverage gaps. |
| Inputs | Test output, failure traces, CI requirements. |
| Outputs | Passing tests and explicit note of any deferred gaps. |
| Validation | Critical-path tests pass and remaining risks are documented. |

## Steps

1. Identify changed behavior and risk-critical paths.
2. Design unit and E2E test cases for required coverage.
3. Implement deterministic tests and mocks.
4. Run tests and resolve failures or instability.
5. Summarize coverage and remaining gaps.

## Tasks

- Task 1.1 — Define coverage requirements for changed and critical behavior.
- Task 1.2 — Implement unit tests for logic and edge cases.
- Task 1.3 — Implement or update E2E tests for key user flows.
- Task 1.4 — Execute tests and stabilize failures.
- Task 1.5 — Record coverage outcomes and residual testing risk.

## Subtasks

- Subtask 1.1.1 — Map tests to public surface and risk areas.
- Subtask 1.2.1 — Mock external services and keep assertions deterministic.
- Subtask 1.3.1 — Ensure environment assumptions are explicit and reproducible.
- Subtask 1.4.1 — Eliminate brittle timing and order dependencies.
- Subtask 1.5.1 — Flag any deferred tests with rationale.

## Actions Summary

1. Plan risk-based coverage.
2. Write deterministic tests.
3. Execute and stabilize.
4. Deliver clear test confidence and gap reporting.
