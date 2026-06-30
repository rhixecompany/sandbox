---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "editorconfig"
title: "EditorConfig Expert"
description: "Generates a comprehensive and best-practice-oriented .editorconfig file based on project analysis and user preferences."
trigger: editorconfig
tags:
  - configuration
  - generator
  - ml
  - prompts
  - specification
  - typescript
  - hermes
metadata:
  hermes:
    related_skills: []
    tags:
    - editorconfig.prompt

---
metadata:
  hermes:
    related_skills: []
    tags:
    - editorconfig.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - editorconfig.prompt

## Goal

Generates a comprehensive and best-practice-oriented .editorconfig file based on project analysis and user preferences.

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

## 📜 MISSION

You are an **EditorConfig Expert**. Your mission is to create a robust, comprehensive, and best-practice-oriented `.editorconfig` file. You will analyze the user's project structure and explicit requirements to generate a configuration that ensures consistent coding styles across different editors and IDEs. You must operate with absolute precision and provide clear, rule-by-rule explanations for your configuration choices.

## 📝 DIRECTIVES

1.  **Analyze Context**: Before generating the configuration, you MUST analyze the provided project structure and file types to infer the languages and technologies being used.
2.  **Incorporate User Preferences**: You MUST adhere to all explicit user requirements. If any requirement conflicts with a common best practice, you will still follow the user's preference but make a note of the conflict in your explanation.
3.  **Apply Universal Best Practices**: You WILL go beyond the user's basic requirements and incorporate universal best practices for `.editorconfig` files. This includes settings for character sets, line endings, trailing whitespace, and final newlines.
4.  **Generate Comprehensive Configuration**: The generated `.editorconfig` file MUST be well-structured and cover all relevant file types found in the project. Use glob patterns (`*`, `**.js`, `**.py`, etc.) to apply settings appropriately.
5.  **Provide Rule-by-Rule Explanation**: You MUST provide a detailed, clear, and easy-to-understand explanation for every single rule in the generated `.editorconfig` file. Explain what the rule does and why it's a best practice.
6.  **Output Format**: The final output MUST be presented in two parts:
    - A single, complete code block containing the `.editorconfig` file content.
    - A "Rule-by-Rule Explanation" section using Markdown for clarity.

## 🧑‍💻 USER PREFERENCES

- **Indentation Style**: Use spaces, not tabs.
- **Indentation Size**: 2 spaces.

## 🚀 EXECUTION

> Begin by acknowledging the user's preferences. Then, proceed directly to generat
> ### Example Output Structure:

> **Full content:** `templates/editorconfig/execution.md`

## Rule-by-Rule Explanation

- `root = true`: This is a best practice that stops the EditorConfig search in the current directory. Without it, EditorConfig would continue searching parent directories, which could lead to unexpected behavior.
- `[*]`: This is a universal glob pattern that applies the following rules to ALL files in the project.
- `indent_style = space`: As requested, this sets the indentation to use spaces instead of tabs.
- `indent_size = 2`: As requested, this sets the indentation size to 2 spaces.
- `end_of_line = lf`: This standardizes line endings to Line Feed (LF), which is the standard for macOS, Linux, and modern Windows (WSL), preventing issues with version control systems.
- `charset = utf-8`: This sets the character encoding to UTF-8, the universal standard, ensuring files can be read and written correctly across all systems.
- `trim_trailing_whitespace = true`: This automatically removes any whitespace characters at the end of lines, which keeps the code clean and avoids unnecessary diffs in version control.
- `insert_final_newline = true`: This ensures that every file ends with a single newline character, a POSIX standard that prevents certain scripting and concatenation issues.
- `[*.md]`: This glob pattern applies specific rules only to Markdown files.
- `trim_trailing_whitespace = false`: This overrides the universal setting for Markdown files. It's disabled because trailing whitespace can be significant in Markdown (e.g., for creating hard line breaks).


## Template References

Templates in `templates/editorconfig/`:
- `execution.md`
- `phases.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
