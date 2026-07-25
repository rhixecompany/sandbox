# CLAUDE.md — Claude-Specific Agent Guidance

Use this file for Claude-family behavior only. Shared workspace rules stay in `AGENTS.md`.

## 1. Context Loading Order

1. `.hermes.md` — Hermes-specific overrides
2. `AGENTS.md` — general workspace guidance
3. `CLAUDE.md` — this file
4. `.cursorrules` — Cursor IDE rules

## 2. Claude-Specific Tool Usage

### Filesystem Operations

- Use Claude's native code interpreter when available
- Prefer MCP `filesystem` server for sandboxed operations
- Always use absolute paths for clarity

### Code Search

- Use `ast-grep` MCP server for pattern-based search
- Claude's built-in reasoning handles simple grep patterns
- For complex multi-file refactors, use `sequential-thinking` MCP

### Reasoning

- Claude excels at step-by-step reasoning
- Use `sequential-thinking` MCP for formal phase tracking
- Document reasoning chains in `docs/` when complex

## 3. Available MCP Servers

- `python-quality` — ruff + pyright lint/format/typecheck
- `tooling-lint` — eslint, prettier, markdownlint-cli2, cspell
- `tooling-config` — pre-commit, git-cliff, .gitignore/.gitmodules/.editorconfig

Use `hermes mcp list` or `hermes mcp test <name>` to verify server connectivity.

## 4. Conversation Patterns

### Multi-turn Tasks

1. Acknowledge receipt immediately
2. Ask clarifying questions if needed
3. Proceed with concrete next steps
4. Summarize progress at natural breaks

### Code Generation

- Prefer smaller, focused files
- Include tests alongside implementation
- Use TypeScript's strict mode
- Document public APIs with JSDoc

## 5. Output Format

- Lead with action/summary
- Follow with details/code
- Use markdown for structure
- Keep prose concise

## 6. Uncertainty Handling

- When uncertain, ask clarifying questions
- Offer multiple approaches with trade-offs
- State assumptions explicitly

## 7. Tool Calling

- Claude can make parallel tool calls
- Use tool results directly in reasoning
- No need to repeat tool output in final response
