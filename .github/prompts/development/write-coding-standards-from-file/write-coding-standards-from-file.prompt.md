---
name: write-coding-standards-from-file
title: Write Coding Standards from File
description: Generate a coding standards document for a project derived from the styles found in the supplied source files and folders, with variable/parameter configuration support.
trigger: /write-coding-standards-from-file
category: development
version: 1.0.0
author: Hermes Agent
tags: 
metadata: 
hermes: 
profile: code-architect
priority: medium
copilot: 
model_required: sonnet
opencode: 
enabled: true
codex: 
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
license: MIT
---

## Table of Contents

## Goal
Generate a coding standards document for a project derived from the styles found in the supplied source files and folders, with variable/parameter configuration support.

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand off](#phase-4:-hand-off)
- [Rules and Configuration](#rules-and-configuration)
- [Variable and Parameter Configuration Conditions](#variable-and-parameter-configuration-conditions)
  - [`$](#`$)
- [**if** `${fetchStyleURL} == true`](#**if**-`${fetchstyleurl}-==-true`)
- [Coding Standards Templates](#coding-standards-templates)
  - [`"m", "minimal"](#`"m"-"minimal")
- [1. Introduction](#1-introduction)
- [2. Naming Conventions](#2-naming-conventions)
- [3. Formatting and Style](#3-formatting-and-style)
- [4. Commenting](#4-commenting)
- [5. Error Handling](#5-error-handling)
- [6. Best Practices and Anti-Patterns](#6-best-practices-and-anti-patterns)
- [7. Examples](#7-examples)
- [8. Contribution and Enforcement](#8-contribution-and-enforcement)
  - [`"v", verbose"](#`"v"-verbose")
- [1. General Code Style](#1-general-code-style)
- [2. Naming Conventions](#2-naming-conventions)
- [3. Formatting Rules](#3-formatting-rules)
  - [Braces (example in C, adjust for your language)](#braces-example-in-c-adjust-for-your-language)
  - [Spacing](#spacing)
- [4. Comments & Documentation](#4-comments-&-documentation)
- [5. Error Handling](#5-error-handling)
- [6. Commit & Review Practices](#6-commit-&-review-practices)
  - [Commits](#commits)
  - [Reviews](#reviews)
- [7. Tests](#7-tests)
- [8. Changes to This Guide](#8-changes-to-this-guide)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand off](#phase-4:-hand-off)
- [Rules and Configuration](#rules-and-configuration)
- [Variable and Parameter Configuration Conditions](#variable-and-parameter-configuration-conditions)
- [`$](#`$)
- [**if** `${fetchStyleURL} == true`](#**if**-`${fetchstyleurl}-==-true`)
- [Coding Standards Templates](#coding-standards-templates)
- [`"m", "minimal"](#`"m"-"minimal")
- [1. Introduction](#1-introduction)
- [2. Naming Conventions](#2-naming-conventions)
- [3. Formatting and Style](#3-formatting-and-style)
- [4. Commenting](#4-commenting)
- [5. Error Handling](#5-error-handling)
- [6. Best Practices and Anti-Patterns](#6-best-practices-and-anti-patterns)
- [7. Examples](#7-examples)
- [8. Contribution and Enforcement](#8-contribution-and-enforcement)
- [`"v", verbose"](#`"v"-verbose")
- [1. General Code Style](#1-general-code-style)
- [2. Naming Conventions](#2-naming-conventions)
- [3. Formatting Rules](#3-formatting-rules)
- [Braces (example in C, adjust for your language)](#braces-example-in-c-adjust-for-your-language)
- [Spacing](#spacing)
- [4. Comments & Documentation](#4-comments-&-documentation)
- [5. Error Handling](#5-error-handling)
- [6. Commit & Review Practices](#6-commit-&-review-practices)
- [Commits](#commits)
- [Reviews](#reviews)
- [7. Tests](#7-tests)
- [8. Changes to This Guide](#8-changes-to-this-guide)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





Write a coding standards document for a project using the coding styles from the file(s) and/or folder(s) passed as arguments in the prompt.


Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

> Core rules: [`templates/rules-core.md`](templates/rules-core.md)

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.


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

- Return the final artifact or findings .
- Stop once the requested result is delivered.

## Rules and Configuration

> Below is a set of quasi-configuration `boolean` and `string[]` variables. Condit
> Parameters for the prompt have a text definition. There is one required paramete
> **Full content:**

## Variable and Parameter Configuration Conditions

### `$

fileName}.length

> 1 || ${folderName} != undefined`>
>
> - If true, toggle `${fixInconsistencies}` to false.
> **Full content:**

## **if** `${fetchStyleURL} == true`

> Depending on the programming language, for each link in list below, run `#fetch>
>
> - [C Style Guide](https://users.ece.cmu.edu/~eno/coding/CCodingStandard.html)
> **Full content:**

## Coding Standards Templates

### `"m", "minimal"

```text

```

```markdown

## 1. Introduction

***Purpose:** Briefly explain why the coding standards are being established (e.g., to improve code quality, maintainability, and team collaboration).* **Scope:** Define which languages, projects, or modules this specification applies to.

## 2. Naming Conventions

***Variables:** `camelCase`* **Functions/Methods:** `PascalCase` or `camelCase`. ***Classes/Structs:** `PascalCase`.* **Constants:** `UPPER_SNAKE_CASE`.

## 3. Formatting and Style

***Indentation:** Use 4 spaces per indent (or tabs).* **Line Length:** Limit lines to a maximum of 80 or 120 characters. ***Braces:** Use the "K&R" style (opening brace on the same line) or the "Allman" style (opening brace on a new line).* **Blank Lines:** Specify how many blank lines to use for separating logical blocks of code.

## 4. Commenting

***Docstrings/Function Comments:** Describe the function's purpose, parameters, and return values.* **Inline Comments:** Explain complex or non-obvious logic. * **File Headers:** Specify what information should be included in a file header, such as author, date, and file description.

## 5. Error Handling

***General:** How to handle and log errors.* **Specifics:** Which exception types to use, and what information to include in error messages.

## 6. Best Practices and Anti-Patterns

***General:** List common anti-patterns to avoid (e.g., global variables, magic numbers).* **Language-specific:** Specific recommendations based on the project's programming language.

## 7. Examples

*Provide a small code example demonstrating the correct application of the rules.* Provide a small code example of an incorrect implementation and how to fix it.

## 8. Contribution and Enforcement

*Explain how the standards are to be enforced (e.g., via code reviews).* Provide a guide for contributing to the standards document itself. ```````

### `"v", verbose"

```

```text

```

```markdown

# Style Guide

This document defines the style and conventions used in this project. All contributions should follow these rules unless otherwise noted.

## 1. General Code Style

- Favor clarity over brevity. - Keep functions and methods small and focused. - Avoid repeating logic; prefer shared helpers/utilities. - Remove unused variables, imports, code paths, and files.

## 2. Naming Conventions

Use descriptive names. Avoid abbreviations unless well-known.
| Item | Convention | Example | |-----------------|----------------------|--------------------| | Variables | `lower_snake_case` | `buffer_size` | | Functions | `lower_snake_case()` | `read_file()` | | Constants | `UPPER_SNAKE_CASE` | `MAX_RETRIES` | | Types/Structs | `PascalCase` | `FileHeader` | | File Names | `lower_snake_case` | `file_reader.c` |

## 3. Formatting Rules

- Indentation: **4 spaces** - Line length: **max 100 characters** - Encoding: **UTF-8**, no BOM - End files with a newline

### Braces (example in C, adjust for your language)

```

```c

if (condition) { do_something(); } else { do_something_else(); }
```

### Spacing

- One space after keywords: `if (x)`, not `if(x)` - One blank line between top-level functions

## 4. Comments & Documentation

- Explain *why*, not *what*, unless intent is unclear. - Keep comments up-to-date as code changes. - Public functions should include a short description of purpose and parameters. Recommended tags: ```text TODO: follow-up work FIXME: known incorrect behavior NOTE: non-obvious design decision```

## 5. Error Handling

- Handle error conditions explicitly. - Avoid silent failures; either return errors or log them appropriately. - Clean up resources (files, memory, handles) before returning on failure.

## 6. Commit & Review Practices

### Commits

- One logical change per commit. - Write clear commit messages: ```text Short summary (max ~50 chars) Optional longer explanation of context and rationale.```

### Reviews

- Keep pull requests reasonably small. - Be respectful and constructive in review discussions. - Address requested changes or explain if you disagree.

## 7. Tests

- Write tests for new functionality. - Tests should be deterministic (no randomness without seeding). - Prefer readable test cases over complex test abstraction.

## 8. Changes to This Guide

Style evolves.
Propose improvements by opening an issue or sending a patch updating this document. ```````

## Template References

Detailed templates in `templates/`:- `if_fetchstyleurl__true.md`- `rules_and_configuration.md`- `variable_and_parameter_configu.md`

## Personas

See [`templates/personas.md`](templates/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/personality.md`](templates/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Best Practices

See [`templates/best-practices.md`](templates/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/deps-core.md`](templates/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/skills-table-core.md`](templates/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section

## Related Prompts

## Workflow

<content>

Same-family prompts:

- [`write-tests.prompt.md`](write-tests.prompt.md)
