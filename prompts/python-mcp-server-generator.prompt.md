---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Generate Python MCP Server
name: python-mcp-server-generator
description: "Generate a complete MCP server project in Python with tools, resources, and proper configuration"
tags:
  - backend
  - configuration
  - generator
  - mcp
  - ml
  - prompts
  - python
  - specification
  - typescript
  - documentation
  - mcp
  - planning
  - python
  - specification
---

## Goal

Generate a complete MCP server project in Python with tools, resources, and proper configuration.

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

1. **Project Structure**: Create a new Python project with proper structure using uv
2. **Dependencies**: Include mcp[cli] package with uv
3. **Transport Type**: Choose between stdio (for local) or streamable-http (for remote)
4. **Tools**: Create at least one useful tool with proper type hints
5. **Error Handling**: Include comprehensive error handling and validation

## Implementation Details

> - Initialize with `uv init project-name`
> - Add MCP SDK: `uv add "mcp[cli]"`

> **Full content:** `templates/python-mcp-server-generator/implementation_details.md`

## Example Tool Types to Consider

- Data processing and transformation
- File system operations (read, analyze, search)
- External API integrations
- Database queries
- Text analysis or generation (with sampling)
- System information retrieval
- Math or scientific calculations

## Configuration Options

- **For stdio Servers**:
  - Simple direct execution
  - Test with `uv run mcp dev server.py`
  - Install to Claude: `uv run mcp install server.py`
- **For HTTP Servers**:
  - Port configuration via environment variables
  - Stateless mode for scalability: `stateless_http=True`
  - JSON response mode: `json_response=True`
  - CORS configuration for browser clients
  - Mounting to existing ASGI servers (Starlette/FastAPI)

## Testing Guidance

- Explain how to run the server:
  - stdio: `python server.py` or `uv run server.py`
  - HTTP: `python server.py` then connect to `http://localhost:PORT/mcp`
- Test with MCP Inspector: `uv run mcp dev server.py`
- Install to Claude Desktop: `uv run mcp install server.py`
- Include example tool invocations
- Add troubleshooting tips

## Additional Features to Consider

- Context usage for logging, progress, and notifications
- LLM sampling for AI-powered tools
- User input elicitation for interactive workflows
- Lifespan management for shared resources (databases, connections)
- Structured output with Pydantic models
- Icons for UI display
- Image handling with Image class
- Completion support for better UX

## Best Practices

- Use type hints everywhere - they're not optional
- Return structured data when possible
- Log to stderr (or use Context logging) to avoid stdout pollution
- Clean up resources properly
- Validate inputs early
- Provide clear error messages
- Test tools independently before LLM integration

Generate a complete, production-ready MCP server with type safety, proper error handling, and comprehensive documentation.


## Template References

Templates in `templates/python-mcp-server-generator/`:
- `implementation_details.md`
- `phases.md`
