---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Create TypeSpec API Plugin
name: typespec-create-api-plugin
mode: "agent"
tools: ["changes", "search/codebase", "edit/editFiles", "problems"]
description: "Generate a TypeSpec API plugin with REST operations, authentication, and Adaptive Cards for Microsoft 365 Copilot"
model: "gpt-4.1"
tags: []
  - typespec
  - m365-copilot
  - api-plugin
  - rest-api
---

## Goal

Generate a TypeSpec API plugin with REST operations, authentication, and Adaptive Cards for Microsoft 365 Copilot.

## Context

Use when you need to typespec create api plugin for the current workspace or task.

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

## Requirements

> Generate TypeSpec files with:
> ### main.tsp - Agent Definition

> **Full content:** `templates/typespec-create-api-plugin/requirements.md`

## Authentication Options

> Choose based on API requirements:
> 1. **No Authentication** (Public APIs)

> **Full content:** `templates/typespec-create-api-plugin/authentication_options.md`

## Function Capabilities

> ### Confirmation Dialog
> type: "AdaptiveCard",

> **Full content:** `templates/typespec-create-api-plugin/function_capabilities.md`

## Best Practices

1. **Operation Names**: Use clear, action-oriented names (listProjects, createTicket)
2. **Models**: Define TypeScript-like models for requests and responses
3. **HTTP Methods**: Use appropriate verbs (@get, @post, @patch, @delete)
4. **Paths**: Use RESTful path conventions with @route
5. **Parameters**: Use @path, @query, @header, @body appropriately
6. **Descriptions**: Provide clear descriptions for model understanding
7. **Confirmations**: Add for destructive operations (delete, update critical data)
8. **Cards**: Use for rich visual responses with multiple data items

## Workflow

Ask the user:

1. What is the API base URL and purpose?
2. What operations are needed (CRUD operations)?
3. What authentication method does the API use?
4. Should confirmations be required for any operations?
5. Do responses need Adaptive Cards?

Then generate:

- Complete `main.tsp` with agent definition
- Complete `actions.tsp` with API operations and models
- Optional `cards/card.json` if Adaptive Cards are needed


## Template References

Templates in `templates/typespec-create-api-plugin/`:
- `authentication_options.md`
- `function_capabilities.md`
- `phases.md`
- `requirements.md`
- `workflow.md`
