# Phases

> Extracted from `testing.prompt.md`.

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
