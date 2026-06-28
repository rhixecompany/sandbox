---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Project Folder Structure Blueprint Generator
name: folder-structure-blueprint-generator
description: "Comprehensive technology-agnostic prompt for analyzing and documenting project folder structures. Auto-detects project types (.NET, Java, React, Angular, Python, Node.js, Flutter), generates detailed blueprints with visualization options, naming conventions, file placement patterns, and extension templates for maintaining consistent code organization across diverse technology stacks."
tags: []
---

## Goal

Comprehensive technology-agnostic prompt for analyzing and documenting project folder structures. Auto-detects project types (.NET, Java, React, Angular, Python, Node.js, Flutter), generates detailed blueprints with visualization options, naming conventions, file placement patterns, and extension templates for maintaining consistent code organization across diverse technology stacks.

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

## Configuration Variables

> ${PROJECT_TYPE="Auto-detect|.NET|Java|React|Angular|Python|Node.js|Flutter|Other
> <!-- Select primary technology -->

> **Full content:** `templates/folder-structure-blueprint-generator/configuration_variables.md`

## Generated Prompt

> "Analyze the project's folder structure and create a comprehensive 'Project_Fold
> ### Initial Auto-detection Phase

> **Full content:** `templates/folder-structure-blueprint-generator/generated_prompt.md`

## Template References

Detailed templates in `templates/folder-structure-blueprint-generator/`:
- `configuration_variables.md`
- `generated_prompt.md`
