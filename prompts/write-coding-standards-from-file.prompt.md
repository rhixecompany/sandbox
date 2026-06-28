---
toolsets:
  - createFile
  - editFiles
  - web/fetch
  - githubRepo
  - search
  - testFailure
license: MIT
author: Hermes Agent
version: 1.0.0
title: Write Coding Standards From File
name: write-coding-standards-from-file
description: "Write a coding standards document for a project using the coding styles from the file(s) and/or folder(s) passed as arguments in the prompt."
tags: []
---


## Goal

Write a coding standards document for a project using the coding styles from the file(s) and/or folder(s) passed as arguments in the prompt.

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

## Rules and Configuration

> Below is a set of quasi-configuration `boolean` and `string[]` variables. Condit
> Parameters for the prompt have a text definition. There is one required paramete

> **Full content:** `templates/write-coding-standards-from-file/rules_and_configuration.md`

## Variable and Parameter Configuration Conditions

> ### `${fileName}.length > 1 || ${folderName} != undefined`
> - If true, toggle `${fixInconsistencies}` to false.

> **Full content:** `templates/write-coding-standards-from-file/variable_and_parameter_configu.md`

## **if** `${fetchStyleURL} == true`

> Depending on the programming language, for each link in list below, run `#fetch 
> - [C Style Guide](https://users.ece.cmu.edu/~eno/coding/CCodingStandard.html)

> **Full content:** `templates/write-coding-standards-from-file/if_fetchstyleurl__true.md`

## Coding Standards Templates

### `"m", "minimal"`

````text
    ```markdown
    ## 1. Introduction
    *   **Purpose:** Briefly explain why the coding standards are being established (e.g., to improve code quality, maintainability, and team collaboration).
    *   **Scope:** Define which languages, projects, or modules this specification applies to.

    ## 2. Naming Conventions
    *   **Variables:** `camelCase`
    *   **Functions/Methods:** `PascalCase` or `camelCase`.
    *   **Classes/Structs:** `PascalCase`.
    *   **Constants:** `UPPER_SNAKE_CASE`.

    ## 3. Formatting and Style
    *   **Indentation:** Use 4 spaces per indent (or tabs).
    *   **Line Length:** Limit lines to a maximum of 80 or 120 characters.
    *   **Braces:** Use the "K&R" style (opening brace on the same line) or the "Allman" style (opening brace on a new line).
    *   **Blank Lines:** Specify how many blank lines to use for separating logical blocks of code.

    ## 4. Commenting
    *   **Docstrings/Function Comments:** Describe the function's purpose, parameters, and return values.
    *   **Inline Comments:** Explain complex or non-obvious logic.
    *   **File Headers:** Specify what information should be included in a file header, such as author, date, and file description.

    ## 5. Error Handling
    *   **General:** How to handle and log errors.
    *   **Specifics:** Which exception types to use, and what information to include in error messages.

    ## 6. Best Practices and Anti-Patterns
    *   **General:** List common anti-patterns to avoid (e.g., global variables, magic numbers).
    *   **Language-specific:** Specific recommendations based on the project's programming language.

    ## 7. Examples
    *   Provide a small code example demonstrating the correct application of the rules.
    *   Provide a small code example of an incorrect implementation and how to fix it.

    ## 8. Contribution and Enforcement
    *   Explain how the standards are to be enforced (e.g., via code reviews).
    *   Provide a guide for contributing to the standards document itself.
    ```
````

### `"v", verbose"`

````text
    ```markdown

    # Style Guide

    This document defines the style and conventions used in this project.
    All contributions should follow these rules unless otherwise noted.

    ## 1. General Code Style

    - Favor clarity over brevity.
    - Keep functions and methods small and focused.
    - Avoid repeating logic; prefer shared helpers/utilities.
    - Remove unused variables, imports, code paths, and files.

    ## 2. Naming Conventions

    Use descriptive names. Avoid abbreviations unless well-known.

    | Item            | Convention           | Example            |
    |-----------------|----------------------|--------------------|
    | Variables       | `lower_snake_case`   | `buffer_size`      |
    | Functions       | `lower_snake_case()` | `read_file()`      |
    | Constants       | `UPPER_SNAKE_CASE`   | `MAX_RETRIES`      |
    | Types/Structs   | `PascalCase`         | `FileHeader`       |
    | File Names      | `lower_snake_case`   | `file_reader.c`    |

    ## 3. Formatting Rules

    - Indentation: **4 spaces**
    - Line length: **max 100 characters**
    - Encoding: **UTF-8**, no BOM
    - End files with a newline

    ### Braces (example in C, adjust for your language)

        ```c
        if (condition) {
            do_something();
        } else {
            do_something_else();
        }
        ```

    ### Spacing

    - One space after keywords: `if (x)`, not `if(x)`
    - One blank line between top-level functions

    ## 4. Comments & Documentation

    - Explain *why*, not *what*, unless intent is unclear.
    - Keep comments up-to-date as code changes.
    - Public functions should include a short description of purpose and parameters.

    Recommended tags:

        ```text
        TODO: follow-up work
        FIXME: known incorrect behavior
        NOTE: non-obvious design decision
        ```

    ## 5. Error Handling

    - Handle error conditions explicitly.
    - Avoid silent failures; either return errors or log them appropriately.
    - Clean up resources (files, memory, handles) before returning on failure.

    ## 6. Commit & Review Practices

    ### Commits
    - One logical change per commit.
    - Write clear commit messages:

        ```text
        Short summary (max ~50 chars)
        Optional longer explanation of context and rationale.
        ```

    ### Reviews
    - Keep pull requests reasonably small.
    - Be respectful and constructive in review discussions.
    - Address requested changes or explain if you disagree.

    ## 7. Tests

    - Write tests for new functionality.
    - Tests should be deterministic (no randomness without seeding).
    - Prefer readable test cases over complex test abstraction.

    ## 8. Changes to This Guide

    Style evolves.
    Propose improvements by opening an issue or sending a patch updating this document.
    ```
````


## Template References

Detailed templates in `templates/write-coding-standards-from-file/`:
- `if_fetchstyleurl__true.md`
- `rules_and_configuration.md`
- `variable_and_parameter_configu.md`
