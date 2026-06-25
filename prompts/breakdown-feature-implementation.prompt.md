---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Feature Implementation Plan Prompt
name: breakdown-feature-implementation
description: "Prompt for creating detailed feature implementation plans, following Epoch monorepo structure."
---

## Goal

Prompt for creating detailed feature implementation plans, following Epoch monorepo structure.

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

## Goal

Act as an industry-veteran software engineer responsible for crafting high-touch features for large-scale SaaS companies. Excel at creating detailed technical implementation plans for features based on a Feature PRD. Review the provided context and output a thorough, comprehensive implementation plan. **Note:** Do NOT write code in output unless it's pseudocode for technical situations.

## Output Format

> The output should be a complete implementation plan in Markdown format, saved to
> Folder and file structure for both front-end and back-end repositories following

> **Full content:** `templates/breakdown-feature-implementation/output_format.md`

## Context Template

- **Feature PRD:** [The content of the Feature PRD markdown file]
````
```


## Template References

Detailed templates in `templates/breakdown-feature-implementation/`:
- `output_format.md`
