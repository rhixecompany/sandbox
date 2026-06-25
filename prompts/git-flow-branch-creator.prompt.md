---
toolsets: ["runCommands/runInTerminal", "runCommands/getTerminalOutput"]
license: MIT
author: Hermes Agent
version: 1.0.0
title: Git Flow Branch Creator
name: git-flow-branch-creator
description: "Intelligent Git Flow branch creator that analyzes git status/diff and creates appropriate branches following the nvie Git Flow branching model."
---

## Goal

Intelligent Git Flow branch creator that analyzes git status/diff and creates appropriate branches following the nvie Git Flow branching model.

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

Detailed templates in `templates/git-flow-branch-creator/`:
- `legacy_prompt_details.md`
