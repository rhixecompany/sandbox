---
toolsets: ["execute/runInTerminal", "execute/getTerminalOutput"]
license: MIT
author: Hermes Agent
version: 1.0.0
title: Conventional Commit
name: conventional-commit
description: "Prompt and workflow for generating conventional commit messages using a structured XML format. Guides users to create standardized, descriptive commit messages in line with the Conventional Commits specification, including instructions, examples, and validation."
tags:
  - frontend
  - ml
  - prompts
  - specification
  - typescript
  - workflow
  - database
  - documentation
  - drizzle
  - orchestration
  - planning
  - specification
  - workflow
metadata:
  hermes:
    related_skills: []
    tags:
    - conventional-commit.prompt

trigger: conventional-commit

---
metadata:
  hermes:
    related_skills: []
    tags:
    - conventional-commit.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - conventional-commit.prompt

## Goal

Prompt and workflow for generating conventional commit messages using a structured XML format. Guides users to create standardized, descriptive commit messages in line with the Conventional Commits specification, including instructions, examples, and validation.

## Context

Use when you need to conventional commit for the current workspace or task.

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

Templates in `templates/conventional-commit/`:
- `legacy_prompt_details.md`
- `phases.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
