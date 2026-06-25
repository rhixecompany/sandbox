---
toolsets: ["changes", "search/codebase", "edit/editFiles", "problems"]
license: MIT
author: Hermes Agent
version: 1.0.0
title: Create TypeSpec Declarative Agent
name: typespec-create-agent
mode: "agent"
description: "Generate a complete TypeSpec declarative agent with instructions, capabilities, and conversation starters for Microsoft 365 Copilot"
tags: []
  - typespec
  - m365-copilot
  - declarative-agent
  - agent-development
---

## Goal

Generate a complete TypeSpec declarative agent with instructions, capabilities, and conversation starters for Microsoft 365 Copilot.

## Context

Use when you need to typespec create agent for the current workspace or task.

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

> Generate a `main.tsp` file with:
> 1. **Agent Declaration**

> **Full content:** `templates/typespec-create-agent/requirements.md`

## Template Structure

> import "@typespec/http";
> import "@typespec/openapi3";

> **Full content:** `templates/typespec-create-agent/template_structure.md`

## Best Practices

- Use descriptive, role-based agent names (e.g., "Customer Support Assistant", "Research Helper")
- Write instructions in second person ("You are...")
- Be specific about the agent's expertise and limitations
- Include diverse conversation starters that showcase different features
- Only include capabilities the agent actually needs
- Scope capabilities (URLs, folders, etc.) when possible for better performance
- Use triple-quoted strings for multi-line instructions

## Examples

Ask the user:

1. What is the agent's purpose and role?
2. What capabilities does it need?
3. What knowledge sources should it access?
4. What are typical user interactions?

Then generate the complete TypeSpec agent definition.


## Template References

Templates in `templates/typespec-create-agent/`:
- `phases.md`
- `requirements.md`
- `template_structure.md`
