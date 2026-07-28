---
name: typescript-mcp-server-generator
title: Generate TypeScript MCP Server
description: 'Generate a complete MCP server project in TypeScript with tools, resources, and proper configuration.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
  - web
scripts: []
skills: []
formatter: default
plan: None
tags:
  - backend
  - configuration
  - generator
  - mcp
  - ml
  - prompts
  - specification
  - typescript
trigger: /typescript-mcp-server-generator
dependencies: []
metadata:
  hermes: {}
---
## GoalGenerate a complete MCP server project in TypeScript with tools, resources, and proper configuration.

## ContextUse when you need to work on the current workspace or task.

## Inputs- The current workspace, repo, or document state.- The specific request, diff, spec, or files provided by the user.- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs- A complete result that matches the prompt's purpose.- A concise verification note when the task benefits from one.

## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Follow the prompt literally and prefer evidence from the current workspace.- Keep the response structured, deterministic, and easy to act on.- Avoid changing unrelated files or adding unnecessary scope.- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake- Read the request and identify the exact scope.- Locate the relevant files, diffs, or references.

### Phase 2: Execute- Perform the requested work with the smallest safe change set.- Keep the steps explicit and reproducible.

### Phase 3: Verify- Check the result against the goal, rules, and inputs.- Confirm the output is usable and complete.

### Phase 4: Hand off- Return the final artifact or findings clearly.- Stop once the requested result is delivered.

## Requirements1. **Project Structure**: Create a new TypeScript/Node.js project with proper directory structure2. **NPM Packages**: Include @modelcontextprotocol/sdk, zod@3, and either express (for HTTP) or stdio support3. **TypeScript Configuration**: Proper tsconfig.json with ES modules support4. **Server Type**: Choose between HTTP (with Streamable HTTP transport) or stdio-based server5. **Tools**: Create at least one useful tool with proper schema validation6. **Error Handling**: Include comprehensive error handling and validation

## Implementation Details> - Initialize with `npm init` and create package.json> - Install dependencies: `@modelcontextprotocol/sdk`, `zod@3`, and transport-spec> **Full content:** `templates/typescript-mcp-server-generator/implementation_details.md`

## Example Tool Types to Consider- Data processing and transformation- External API integrations- File system operations (read, search, analyze)- Database queries- Text analysis or summarization (with sampling)- System information retrieval

## Configuration Options- **For HTTP Servers**:  - Port configuration via environment variables  - CORS setup for browser clients  - Session management (stateless vs stateful)  - DNS rebinding protection for local servers- **For stdio Servers**:  - Proper stdin/stdout handling  - Environment-based configuration  - Process lifecycle management

## Testing Guidance- Explain how to run the server (`npm start` or `bunx tsx server.ts`)- Provide MCP Inspector command: `npx @modelcontextprotocol/inspector`- For HTTP servers, include connection URL: `http://localhost:PORT/mcp`- Include example tool invocations- Add troubleshooting tips for common issues

## Additional Features to Consider- Sampling support for LLM-powered tools- User input elicitation for interactive workflows- Dynamic tool registration with enable/disable capabilities- Notification debouncing for bulk updates- Resource links for efficient data referencesGenerate a complete, production-ready MCP server with comprehensive documentation, type safety, and error handling.

## Template ReferencesTemplates in `templates/typescript-mcp-server-generator/`:- `implementation_details.md`- `phases.md`

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


## Context

Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.


## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Read existing code before writing new code.
- Match project conventions and style.
- Add tests for new functionality.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State clearly when something fails.


## Phases

### Phase 1: Intake
- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute
- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify
- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off
- Return final artifact or findings clearly.
- Stop once the requested result is delivered.


## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.


## Verification Checklist

| # | Gate | Criterion |
|---|------|-----------|
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |


## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Goal

Generate a complete MCP server project in TypeScript with tools, resources, and proper configuration.


## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.


## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
|-------|---------|
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


