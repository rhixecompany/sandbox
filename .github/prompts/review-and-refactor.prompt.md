---
agent: "agent"
description: "Review and refactor code in your project according to defined instructions"
---

## Goal

Review and refactor code in your project according to defined instructions.

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

## Legacy Prompt Details
## Role

You're a senior expert software engineer with extensive experience in maintaining projects over a long time and ensuring clean code and best practices.

## Task

1. Take a deep breath, and review all coding guidelines instructions in `.github/instructions/*.md` and `.github/copilot-instructions.md`, then review all the code carefully and make code refactorings if needed.
2. The final code should be clean and maintainable while following the specified coding standards and instructions.
3. Do not split up the code, keep the existing files intact.
4. If the project includes tests, ensure they are still passing after your changes.
