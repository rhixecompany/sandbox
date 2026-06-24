# Phases

> Extracted from `playwright-generate-test.prompt.md`.

## Phases

### Phase 1: Gather the scenario
**Goal:** understand the behavior that needs to be tested.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Read the scenario or ask for it | Test brief |
| 1.2 | Identify the expected user outcome | Behavior map |
| 1.3 | Note constraints and edge cases | Test scope |

#### Tasks
- Clarify the scenario.
- Capture the important behavior.
- Avoid writing code too early.

### Phase 2: Inspect the app
**Goal:** use Playwright MCP to observe the relevant flows.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Drive the scenario in the browser | Interaction notes |
| 2.2 | Capture the UI state and selectors | Locator notes |
| 2.3 | Record failures or important signals | Evidence |

#### Tasks
- Observe the real behavior.
- Collect selectors and outcomes.
- Re-run critical interactions when needed.

### Phase 3: Draft the test
**Goal:** write the Playwright TypeScript test from the gathered evidence.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Translate the observed flow into test steps | Draft test |
| 3.2 | Save the file in the tests directory | Test file |
| 3.3 | Check the test against the scenario | Draft validation |

#### Tasks
- Write a clear, stable test.
- Use the smallest reliable selector set.
- Keep the test behavior-focused.

### Phase 4: Run and iterate
**Goal:** make the test pass and stop only when it is stable.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 4.1 | Execute the test file | Run result |
| 4.2 | Fix failures and rerun | Stable test |
| 4.3 | Verify the final pass | Completed test |

#### Tasks
- Iterate until the test passes.
- Adjust selectors or waits only when needed.
- End with a validated test file.
