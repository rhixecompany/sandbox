---
toolsets: ["changes", "search/codebase", "edit/editFiles", "problems"]
license: MIT
author: Hermes Agent
version: 1.0.0
title: Add TypeSpec API Operations
name: typespec-api-operations
mode: "agent"
description: "Add GET, POST, PATCH, and DELETE operations to a TypeSpec API plugin with proper routing, parameters, and adaptive cards"
tags:
  - api
  - ml
  - prompts
  - specification
  - typescript
  - typespec
  - m365-copilot
  - api-plugin
  - rest-operations
  - crud
metadata:
  hermes:
    related_skills: []
    tags:
    - typespec-api-operations.prompt

trigger: typespec-api-operations

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - typespec-api-operations.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - typespec-api-operations.prompt

## Goal

Add GET, POST, PATCH, and DELETE operations to a TypeSpec API plugin with proper routing, parameters, and adaptive cards.

## Context

Use when you need to typespec api operations for the current workspace or task.

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

## Adding GET Operations

> ### Simple GET - List All Items
> @get op listItems(): Item[];

> **Full content:** `templates/typespec-api-operations/adding_get_operations.md`

## Adding POST Operations

> ### Simple POST - Create Item
> * @param item The item to create

> **Full content:** `templates/typespec-api-operations/adding_post_operations.md`

## Adding PATCH Operations

> ### Simple PATCH - Update Item
> * Update an existing item.

> **Full content:** `templates/typespec-api-operations/adding_patch_operations.md`

## Adding DELETE Operations

> * @param id The ID of the item to delete
> @route("/items/{id}")

> **Full content:** `templates/typespec-api-operations/adding_delete_operations.md`

## Complete CRUD Example

> ### Define the Service and Models
> @server("https://api.example.com")

> **Full content:** `templates/typespec-api-operations/complete_crud_example.md`

## Advanced Features

> ### Multiple Query Parameters
> @query userId?: integer,

> **Full content:** `templates/typespec-api-operations/advanced_features.md`

## Testing Prompts

After adding operations, test with these prompts:

**GET Operations:**

- "List all items and show them in a table"
- "Show me items for user ID 1"
- "Get the details of item 42"

**POST Operations:**

- "Create a new item with title 'My Task' for user 1"
- "Add an item: title 'New Feature', description 'Add login'"

**PATCH Operations:**

- "Update item 10 with title 'Updated Title'"
- "Change the status of item 5 to completed"

**DELETE Operations:**

- "Delete item 99"
- "Remove the item with ID 15"

## Best Practices

> - Use descriptive parameter names: `userId` not `uid`
> - Be consistent across operations

> **Full content:** `templates/typespec-api-operations/best_practices.md`

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

Detailed templates in `templates/typespec-api-operations/`:
- `adding_delete_operations.md`
- `adding_get_operations.md`
- `adding_patch_operations.md`
- `adding_post_operations.md`
- `advanced_features.md`
- `best_practices.md`
- `complete_crud_example.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
