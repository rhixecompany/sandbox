---
name: typespec-api-operations
title: TypeSpec API Operations
description: Add GET, POST, PATCH, and DELETE operations to a TypeSpec API plugin with proper routing, parameters, and adaptive cards for Microsoft 365 Copilot.
trigger: /typespec-api-operations
version: 1.0.0
author: Hermes Agent
tags:
  - typespec
  - api
  - rest
  - m365-copilot
  - crud
  - generator
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
toolsets:
  - file
  - terminal
skills:
  - skill:using-superpowers
dependencies: []
formatter: markdown
license: MIT
---
## Table of Contents

## Goal

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
- [Adding GET Operations](#adding-get-operations)
  - [Simple GET](#simple-get)
- [Adding POST Operations](#adding-post-operations)
  - [Simple POST](#simple-post)
- [Adding PATCH Operations](#adding-patch-operations)
  - [Simple PATCH](#simple-patch)
- [Adding DELETE Operations](#adding-delete-operations)
- [Complete CRUD Example](#complete-crud-example)
  - [Define the Service and Models](#define-the-service-and-models)
- [Advanced Features](#advanced-features)
  - [Multiple Query Parameters](#multiple-query-parameters)
- [Test](#test)
- [Best Practices](#best-practices)
- [Common Issues](#common-issues)
  - [Issue: Parameter not showing in Copilot](#issue:-parameter-not-showing-in-copilot)
  - [Issue: Adaptive card not rendering](#issue:-adaptive-card-not-rendering)
  - [Issue: Confirmation not appearing](#issue:-confirmation-not-appearing)
  - [Issue: Model property not appearing in response](#issue:-model-property-not-appearing-in-response)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
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
- [Adding GET Operations](#adding-get-operations)
- [Simple GET](#simple-get)
- [Adding POST Operations](#adding-post-operations)
- [Simple POST](#simple-post)
- [Adding PATCH Operations](#adding-patch-operations)
- [Simple PATCH](#simple-patch)
- [Adding DELETE Operations](#adding-delete-operations)
- [Complete CRUD Example](#complete-crud-example)
- [Define the Service and Models](#define-the-service-and-models)
- [Advanced Features](#advanced-features)
- [Multiple Query Parameters](#multiple-query-parameters)
- [Test](#test)
- [Best Practices](#best-practices)
- [Common Issues](#common-issues)
- [Issue: Parameter not showing in Copilot](#issue:-parameter-not-showing-in-copilot)
- [Issue: Adaptive card not rendering](#issue:-adaptive-card-not-rendering)
- [Issue: Confirmation not appearing](#issue:-confirmation-not-appearing)
- [Issue: Model property not appearing in response](#issue:-model-property-not-appearing-in-response)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





Add GET, POST, PATCH, and DELETE operations to a TypeSpec API plugin with proper routing, parameters, and adaptive cards.


Use when you need to typespec api operations for the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

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

## Adding GET Operations

### Simple GET

- List All Items

>
> @get op listItems(): Item[];
> **Full content:**

## Adding POST Operations

### Simple POST

- Create Item

>
> - @param item The item to create
> **Full content:**

## Adding PATCH Operations

### Simple PATCH

- Update Item

>
> - Update an existing item.
> **Full content:**

## Adding DELETE Operations

> - @param id The ID of the item to delete
> @route("/items/{id}")
> **Full content:**

## Complete CRUD Example

### Define the Service and Models

> @server("<https://api.example.com>")

## Advanced Features

### Multiple Query Parameters

> @query userId?: integer,

## Test

ing PromptsAfter adding operations, test with these prompts:**GET Operations:**- "List all items and show them in a table"- "Show me items for user ID 1"- "Get the details of item 42"**POST Operations:**- "Create a new item with title 'My Task' for user 1"- "Add an item: title 'New Feature', description 'Add login'"**PATCH Operations:**- "Update item 10 with title 'Updated Title'"- "Change the status of item 5 to completed"**DELETE Operations:**- "Delete item 99"- "Remove the item with ID 15"

## Best Practices

> - Use descriptive parameter names: `userId` not `uid`
> - Be consistent across operations

## Common Issues

### Issue: Parameter not showing in Copilot

**Solution**: Check parameter is properly decorated with `@query`, `@path`, or `@body`

### Issue: Adaptive card not rendering

**Solution**: Verify file path in `@card` decorator and check JSON syntax

### Issue: Confirmation not appearing

**Solution**: Ensure `@capabilities` decorator is properly formatted with confirmation object

### Issue: Model property not appearing in response

**Solution**: Check if property needs `@visibility(Lifecycle.Read)` or remove it if it should be writable

## Template References

Detailed templates in `templates/typespec-api-operations/`:- `adding_delete_operations.md`- `adding_get_operations.md`- `adding_patch_operations.md`- `adding_post_operations.md`- `advanced_features.md`- `best_practices.md`- `complete_crud_example.md`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

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

Same-family prompts:

- [`typespec-create-agent.prompt.md`](typespec-create-agent.prompt.md)
- [`typespec-create-api-plugin.prompt.md`](typespec-create-api-plugin.prompt.md)