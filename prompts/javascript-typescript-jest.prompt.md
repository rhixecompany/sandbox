---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Javascript Typescript Jest
name: javascript-typescript-jest
description: "Best practices for writing JavaScript/TypeScript tests using Jest, including mocking strategies, test structure, and common patterns."
tags:
  - javascript
  - ml
  - prompts
  - specification
  - testing
  - typescript
  - documentation
  - java
  - javascript
  - nextjs
  - planning
  - specification
  - testing
  - typescript
metadata:
  hermes:
    related_skills: []
    tags:
    - javascript-typescript-jest.prompt

trigger: javascript-typescript-jest

---
metadata:
  hermes:
    related_skills: []
    tags:
    - javascript-typescript-jest.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - javascript-typescript-jest.prompt

## Goal

Best practices for writing JavaScript/TypeScript tests using Jest, including mocking strategies, test structure, and common patterns.

## Context

Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


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

## Common Jest Matchers

- Basic: `expect(value).toBe(expected)`, `expect(value).toEqual(expected)`
- Truthiness: `expect(value).toBeTruthy()`, `expect(value).toBeFalsy()`
- Numbers: `expect(value).toBeGreaterThan(3)`, `expect(value).toBeLessThanOrEqual(3)`
- Strings: `expect(value).toMatch(/pattern/)`, `expect(value).toContain('substring')`
- Arrays: `expect(array).toContain(item)`, `expect(array).toHaveLength(3)`
- Objects: `expect(object).toHaveProperty('key', value)`
- Exceptions: `expect(fn).toThrow()`, `expect(fn).toThrow(Error)`
- Mock functions: `expect(mockFn).toHaveBeenCalled()`, `expect(mockFn).toHaveBeenCalledWith(arg1, arg2)`


## Template References

Templates in `templates/javascript-typescript-jest/`:
- `legacy_prompt_details.md`
- `phases.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
