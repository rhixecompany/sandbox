---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Code Exemplars Blueprint Generator
name: code-exemplars-blueprint-generator
description: "Technology-agnostic prompt generator that creates customizable AI prompts for scanning codebases and identifying high-quality code exemplars. Supports multiple programming languages (.NET, Java, JavaScript, TypeScript, React, Angular, Python) with configurable analysis depth, categorization methods, and documentation formats to establish coding standards and maintain consistency across development teams."
---

## Goal

Technology-agnostic prompt generator that creates customizable AI prompts for scanning codebases and identifying high-quality code exemplars. Supports multiple programming languages (.NET, Java, JavaScript, TypeScript, React, Angular, Python) with configurable analysis depth, categorization methods, and documentation formats to establish coding standards and maintain consistency across development teams.

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

${PROJECT_TYPE="Auto-detect|.NET|Java|JavaScript|TypeScript|React|Angular|Python|Other"} <!-- Primary technology -->
${SCAN_DEPTH="Basic|Standard|Comprehensive"} <!-- How deeply to analyze the codebase --> ${INCLUDE_CODE_SNIPPETS=true|false} <!-- Include actual code snippets in addition to file references -->
${CATEGORIZATION="Pattern Type|Architecture Layer|File Type"} <!-- How to organize exemplars --> ${MAX_EXAMPLES_PER_CATEGORY=3} <!-- Maximum number of examples per category -->
${INCLUDE_COMMENTS=true|false} <!-- Include explanatory comments for each exemplar -->

## Generated Prompt

> "Scan this codebase and generate an exemplars.md file that identifies high-quali
> ### 1. Codebase Analysis Phase

> **Full content:** `templates/code-exemplars-blueprint-generator/generated_prompt.md`

## Expected Output

Upon running this prompt, GitHub Copilot will scan your codebase and generate an exemplars.md file containing real references to high-quality code examples in your repository, organized according to your selected parameters.


## Template References

Detailed templates in `templates/code-exemplars-blueprint-generator/`:
- `generated_prompt.md`
