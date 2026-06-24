---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Power Platform MCP Connector Generator
name: mcp-copilot-studio-server-generator
description: Generate a complete MCP server implementation optimized for Copilot Studio integration with proper schema constraints and streamable HTTP support
agent: agent
---

## Goal

Generate a complete MCP server implementation optimized for Copilot Studio integration with proper schema constraints and streamable HTTP support.

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

## Instructions

> Create a complete MCP server implementation that:
> 1. **Uses Copilot Studio MCP Pattern:**

> **Full content:** `templates/mcp-copilot-studio-server-generator/instructions.md`

## Context Variables

- **Server Purpose**: [Describe what the MCP server should accomplish]
- **Tools Needed**: [List of specific tools to implement]
- **Resources**: [Types of resources to provide]
- **Authentication**: [Auth method: none, api-key, oauth2]
- **Host Environment**: [Azure Function, Express.js, FastAPI, etc.]
- **Target APIs**: [External APIs to integrate with]

## Expected Output

> 1. **apiDefinition.swagger.json** with:
> - Proper `x-ms-agentic-protocol: mcp-streamable-1.0`

> **Full content:** `templates/mcp-copilot-studio-server-generator/expected_output.md`

## Validation Checklist

Ensure generated code:

- [ ] No reference types in schemas
- [ ] All type fields are single types
- [ ] Enum handling via string with validation
- [ ] Resources available through tool outputs
- [ ] Full URI endpoints
- [ ] JSON-RPC 2.0 compliance
- [ ] Proper x-ms-agentic-protocol header
- [ ] McpResponse/McpErrorResponse schemas
- [ ] Clear tool descriptions for Copilot Studio
- [ ] Generative Orchestration compatible

## Example Usage

```yaml
Server Purpose: Customer data management and analysis
Tools Needed:
  - searchCustomers
  - getCustomerDetails
  - analyzeCustomerTrends
Resources:
  - Customer profiles
  - Analysis reports
Authentication: oauth2
Host Environment: Azure Function
Target APIs: CRM System REST API
```


## Template References

Templates in `templates/mcp-copilot-studio-server-generator/`:
- `example_usage.md`
- `expected_output.md`
- `instructions.md`
- `phases.md`
