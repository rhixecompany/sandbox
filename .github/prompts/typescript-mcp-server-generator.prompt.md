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
plan: null
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

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

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

## Example Tool Types to Consider

- Data processing and transformation- External API integrations- File system operations (read, search, analyze)- Database queries- Text analysis or summarization (with sampling)- System information retrieval

## Configuration Options

- **For HTTP Servers**:  - Port configuration via environment variables  - CORS setup for browser clients  - Session management (stateless vs stateful)  - DNS rebinding protection for local servers- **For stdio Servers**:  - Proper stdin/stdout handling  - Environment-based configuration  - Process lifecycle management

## Test

ing Guidance- Explain how to run the server (`bun run start` or `bunx tsx server.ts`)- Provide MCP Inspector command: `bunx @modelcontextprotocol/inspector`- For HTTP servers, include connection URL: `http://localhost:PORT/mcp`- Include example tool invocations- Add troubleshooting tips for common issues

## Additional Features to Consider

- Sampling support for LLM-powered tools- User input elicitation for interactive workflows- Dynamic tool registration with enable/disable capabilities- Notification debouncing for bulk updates- Resource links for efficient data referencesGenerate a complete, production-ready MCP server with comprehensive documentation, type safety, and error handling.

## Template References

Templates in `templates/typescript-mcp-server-generator/`:- `implementation_details.md`- `phases.md`

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

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

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

## Related Prompts

Other language variants of this MCP server generator:

| Language | Prompt |
| ---------- | -------- |
| Python | [`python-mcp-server-generator.prompt.md`](python-mcp-server-generator.prompt.md) |
| Rust | [`rust-mcp-server-generator.prompt.md`](rust-mcp-server-generator.prompt.md) |
| Go | [`go-mcp-server-generator.prompt.md`](go-mcp-server-generator.prompt.md) |
| Swift | [`swift-mcp-server-generator.prompt.md`](swift-mcp-server-generator.prompt.md) |
| Kotlin | [`kotlin-mcp-server-generator.prompt.md`](kotlin-mcp-server-generator.prompt.md) |
| Java | [`java-mcp-server-generator.prompt.md`](java-mcp-server-generator.prompt.md) |
| C# | [`csharp-mcp-server-generator.prompt.md`](csharp-mcp-server-generator.prompt.md) |
| PHP | [`php-mcp-server-generator.prompt.md`](php-mcp-server-generator.prompt.md) |
| Ruby | [`ruby-mcp-server-generator.prompt.md`](ruby-mcp-server-generator.prompt.md) |

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section
