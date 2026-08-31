---
name: python-mcp-server-generator
title: Python MCP Server Generator
description: Generate a complete Python MCP server project with tools, resources, type-safe configuration, and proper stdio or HTTP transport setup.
trigger: /python-mcp-server-generator
version: 1.0.0
author: Hermes Agent
tags: [python, mcp, server, generator, tooling, automation]
metadata: 
hermes: 
profile: code-architect
priority: medium
copilot: 
model_required: sonnet
opencode: 
enabled: true
codex: 
date: 2026-08-25
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
license: MIT
---

## Table of Contents

## Goal
Generate a complete Python MCP server project with tools, resources, type-safe configuration, and proper stdio or HTTP transport setup.

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
- [Requirements](#requirements)
- [Implementation Details](#implementation-details)
- [Example Tool Types to Consider](#example-tool-types-to-consider)
- [Configuration Options](#configuration-options)
- [Test](#test)
- [Additional Features to Consider](#additional-features-to-consider)
- [Best Practices](#best-practices)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Related Prompts](#related-prompts)
- [Hooks](#hooks)
- [Scripts](#scripts)



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
- [Requirements](#requirements)
- [Implementation Details](#implementation-details)
- [Example Tool Types to Consider](#example-tool-types-to-consider)
- [Configuration Options](#configuration-options)
- [Test](#test)
- [Additional Features to Consider](#additional-features-to-consider)
- [Best Practices](#best-practices)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Related Prompts](#related-prompts)
- [Hooks](#hooks)
- [Scripts](#scripts)





Generate a complete MCP server project in Python with tools, resources, and proper configuration.


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

## Requirements

1. **Project Structure**: Create a new Python project with proper structure using uv
2. **Dependencies**: Include mcp[cli] package with uv
3. **Transport Type**: Choose between stdio (for local) or streamable-http (for remote)
4. **Tools**: Create at least one useful tool with proper type hints
5. **Error Handling**: Include comprehensive error handling and validation

## Implementation Details

> - Initialize with `uv init project-name`
> - Add MCP SDK: `uv add "mcp[cli]"`

## Example Tool Types to Consider

- Data processing and transformation- File system operations (read, analyze, search)- External API integrations- Database queries- Text analysis or generation (with sampling)- System information retrieval- Math or scientific calculations

## Configuration Options

- **For stdio Servers**: - Simple direct execution - Test with `uv run mcp dev server.py` - Install to Claude: `uv run mcp install server.py`- **For HTTP Servers**: - Port configuration via environment variables - Stateless mode for scalability: `stateless_http=True` - JSON response mode: `json_response=True` - CORS configuration for browser clients - Mounting to existing ASGI servers (Starlette/FastAPI)

## Test

ing Guidance- Explain how to run the server: - stdio: `python server.py` or `uv run server.py` - HTTP: `python server.py` then connect to `http://localhost:PORT/mcp`- Test with MCP Inspector: `uv run mcp dev server.py`- Install to Claude Desktop: `uv run mcp install server.py`- Include example tool invocations- Add troubleshooting tips

## Additional Features to Consider

- Context usage for logging, progress, and notifications- LLM sampling for AI-powered tools- User input elicitation for interactive workflows- Lifespan management for shared resources (databases, connections)- Structured output with Pydantic models- Icons for UI display- Image handling with Image class- Completion support for better UX

## Best Practices

- Use type hints everywhere - they're not optional
- Return structured data when possible
- Log to stderr (or use Context logging) to avoid stdout pollution
- Clean up resources properly
- Validate inputs early
- Provide clear error messages
- Test tools independently before LLM integrationGenerate a complete, production-ready MCP server with type safety, proper error handling, and comprehensive documentation.

## Template References

Templates in `templates/python-mcp-server-generator/`:- `implementation_details.md`- `phases.md`

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

## Related Prompts

Other language variants of this MCP server generator:

| Language | Prompt |
| ---------- | -------- |
| TypeScript | [`typescript-mcp-server-generator.prompt.md`](typescript-mcp-server-generator.prompt.md) |
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

## Workflow

<content>

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section
```
# Prompt template
Execute the workflow defined in this file.
```
