# CLAUDE.md — Claude-Specific Agent Guidance

This file provides guidance specifically for Claude-family models (Claude 3.5/3.7 Sonnet, Haiku, etc.) working in this workspace.

## 1. Context Loading Order

1. `.hermes.md` — Hermes-specific overrides
2. `AGENTS.md` — General agent guidance
3. `PROJECT_RULES.md` — Workspace rules
4. `MASTER_RULES.md` — Universal agent rules
5. `CLAUDE.md` — This file (Claude-specific)
6. `.cursorrules` — Cursor IDE rules

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

## 3. Conversation Patterns

### Multi-turn Tasks
Claude maintains strong context. For long tasks:
1. Acknowledge receipt immediately
2. Ask clarifying questions if needed
3. Proceed with concrete next steps
4. Summarize progress at natural breaks

### Code Generation
- Prefer smaller, focused files
- Include tests alongside implementation
- Use TypeScript's strict mode
- Document public APIs with JSDoc

## 4. Workspace-Specific Conventions

### Bash Scripts
- Always ship as `.sh` + `.ps1` + `.bat`
- Use `--dry-run` for destructive operations
- Log to `logs/action_YYYYMMDD_HHMMSS.log`

### Python Scripts
- Use `venv` for isolation
- Make standalone (no external dependencies not in `requirements.txt`)
- Follow PEP 8 naming

### TypeScript
- Bun 1.3.14+ as runtime and package manager
- Strict mode: `noUncheckedIndexedAccess: true`
- ESLint 10 flat config with zero warnings

## 5. Claude-Specific Preferences

### Output Format
- Lead with action/summary
- Follow with details/code
- Use markdown for structure
- Keep prose concise

### Uncertainty Handling
- When uncertain, ask clarifying questions
- Offer multiple approaches with trade-offs
- State assumptions explicitly

### Tool Calling
- Claude can make parallel tool calls
- Use tool results directly in reasoning
- No need to repeat tool output in final response