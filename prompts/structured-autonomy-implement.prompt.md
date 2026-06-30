---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "sa-implement"
title: "Sa Implement"
description: "Structured Autonomy Implementation Prompt"
trigger: sa-implement
tags:
  - ml
  - prompts
  - specification
  - typescript
  - hermes
metadata:
  hermes:
    related_skills: []
    tags:
    - structured-autonomy-implement.prompt

---
metadata:
  hermes:
    related_skills: []
    tags:
    - structured-autonomy-implement.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - structured-autonomy-implement.prompt

## Goal

Structured Autonomy Implementation Prompt.

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

## Template References

Templates in `templates/structured-autonomy-implement/`:
- `legacy_prompt_details.md`
- `phases.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
