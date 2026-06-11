---
name: "playwright-generate-test.prompt"
title: "Playwright Test Generation"
description: "Generate a Playwright test from a scenario, validate it against the app, and iterate until it passes."
author: "Alexa"
created: "2026-05-25T10:50:21.952313Z"
compatibility: ["hermes", "copilot", "opencode"]
tags: ["playwright-generate-test", "banking", "prompt"]
mcp_generator: null
skill_stub: true
---

## Goal

Generate a Playwright test from a scenario, validate it against the app, and iterate until it passes.

## Context

Use when you need to playwright test generation for the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake
- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute
- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify
- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off
- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Legacy Prompt Details
```text
## Description

Generate a Playwright test from a scenario, validate it against the app, and iterate until it passes.

## Context

- Use a provided scenario; if none is given, ask for one before starting.
- Do not write the final test prematurely.
- Run the prescribed steps with Playwright MCP before emitting the test file.

## Skills Required

- `webapp-testing` — use browser automation to validate the scenario in the live app
- `test-driven-development` — translate observed behavior into a reliable test
- `systematic-debugging` — iterate on failures until the test is stable
- `verification-before-completion` — verify the test passes before finishing

## Subagents

| Subagent | Role | Phase |
| --- | --- | --- |
| `@investigator` | Explores the scenario and app behavior | Phase 1 |
| `@author` | Drafts the Playwright test | Phase 3 |
| `@runner` | Executes and iterates on the test | Phase 4 |

## Personas

### @investigator
A scenario investigator who gathers the facts needed to write a correct test.

### @author
A test author who writes clean Playwright TypeScript.

### @runner
A test runner who fixes issues until the test passes.

## Rules

1. Ask for the scenario if it is missing.
2. Do not generate the final test until the workflow steps are complete.
3. Save the generated test in the tests directory.
4. Use Playwright TypeScript with @playwright/test.
5. Execute the test and iterate until it passes.
6. Keep the final test aligned with the observed behavior.

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

## Steps

- Clarify the scenario.
- Inspect the app with Playwright MCP.
- Write the test file.
- Run and iterate until it passes.

## Tasks

- Capture the scenario.
- Observe the live behavior.
- Draft the Playwright test.
- Execute and stabilize it.

## Subtasks

- Ask for missing scenario details.
- Collect selectors and outcomes.
- Save the test in tests/.
- Repeat until the test passes.

## Actions Summary

1. Gather the scenario.
2. Inspect the app.
3. Generate the test file.
4. Run and refine the test.

```
