---
license: MIT
version: 1.0.0
title: Playwright Generate Test
name: "playwright-generate-test"
description: "Generate a Playwright test from a scenario, validate it against the app, and iterate until it passes."
trigger: /playwright-generate-test
author: "Alexa"
created: "2026-05-25T10:50:21.952313Z"
compatibility:
  - hermes
  - copilot
  - opencode
mcp_generator: None
skill_stub: True
tags: []
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

> ### Phase 1: Gather the scenario
> **Goal:** understand the behavior that needs to be tested.

> **Full content:** `templates/playwright-generate-test/phases.md`

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


## Template References

Templates in `templates/playwright-generate-test/`:
- `phases.md`
