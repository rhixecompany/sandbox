---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Generate TypeScript MCP Server
name: typescript-mcp-server-generator
description: "Generate a complete MCP server project in TypeScript with tools, resources, and proper configuration"
tags:
  - backend
  - configuration
  - generator
  - mcp
  - ml
  - prompts
  - specification
  - typescript
  - documentation
  - mcp
  - nextjs
  - planning
  - specification
  - typescript
metadata:
  hermes:
    related_skills: []
    tags:
    - typescript-mcp-server-generator.prompt

trigger: typescript-mcp-server-generator

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - typescript-mcp-server-generator.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - typescript-mcp-server-generator.prompt

## Goal

Generate a complete MCP server project in TypeScript with tools, resources, and proper configuration.

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

## Requirements

1. **Project Structure**: Create a new TypeScript/Node.js project with proper directory structure
2. **NPM Packages**: Include @modelcontextprotocol/sdk, zod@3, and either express (for HTTP) or stdio support
3. **TypeScript Configuration**: Proper tsconfig.json with ES modules support
4. **Server Type**: Choose between HTTP (with Streamable HTTP transport) or stdio-based server
5. **Tools**: Create at least one useful tool with proper schema validation
6. **Error Handling**: Include comprehensive error handling and validation

## Implementation Details

> - Initialize with `npm init` and create package.json
> - Install dependencies: `@modelcontextprotocol/sdk`, `zod@3`, and transport-spec

> **Full content:** `templates/typescript-mcp-server-generator/implementation_details.md`

## Example Tool Types to Consider

- Data processing and transformation
- External API integrations
- File system operations (read, search, analyze)
- Database queries
- Text analysis or summarization (with sampling)
- System information retrieval

## Configuration Options

- **For HTTP Servers**:
  - Port configuration via environment variables
  - CORS setup for browser clients
  - Session management (stateless vs stateful)
  - DNS rebinding protection for local servers
- **For stdio Servers**:
  - Proper stdin/stdout handling
  - Environment-based configuration
  - Process lifecycle management

## Testing Guidance

- Explain how to run the server (`npm start` or `bunx tsx server.ts`)
- Provide MCP Inspector command: `npx @modelcontextprotocol/inspector`
- For HTTP servers, include connection URL: `http://localhost:PORT/mcp`
- Include example tool invocations
- Add troubleshooting tips for common issues

## Additional Features to Consider

- Sampling support for LLM-powered tools
- User input elicitation for interactive workflows
- Dynamic tool registration with enable/disable capabilities
- Notification debouncing for bulk updates
- Resource links for efficient data references

Generate a complete, production-ready MCP server with comprehensive documentation, type safety, and error handling.


## Template References

Templates in `templates/typescript-mcp-server-generator/`:
- `implementation_details.md`
- `phases.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
