# Phases

> Extracted from `playwright-typescript.prompt.md`.

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
