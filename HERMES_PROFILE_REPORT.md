# HERMES_PROFILE_REPORT.md

> Generated: 2026-07-23 | Session: using-superpowers startup verification

## Profile Inventory

| Profile | Model | Provider | Status |
|---------|-------|----------|--------|
| **default** ⬤ | google/gemma-4-31b-it:free | openrouter | Active (current session) |
| alexa | google/gemma-4-31b-it:free | openrouter | Available |
| code-architect | google/gemma-4-31b-it:free | openrouter | Available |
| creative-director | google/gemma-4-31b-it:free | openrouter | Available |
| exec-assistant | google/gemma-4-31b-it:free | openrouter | Available |
| patient-tutor | google/gemma-4-31b-it:free | openrouter | Available |
| research-analyst | google/gemma-4-31b-it:free | openrouter | Available |
| adminbot | claude-opus-4.8 | anthropic | Available |

## Core Files Status

| File | Location | Status |
|------|----------|--------|
| `SOUL.md` | `~/AppData/Local/hermes/SOUL.md` | ✓ Present, valid |
| `USER.md` | `~/AppData/Local/hermes/memories/USER.md` | ✓ Present, 373 bytes |
| `MEMORY.md` | `~/AppData/Local/hermes/memories/MEMORY.md` | ✓ Present, 1053 bytes |

## Workspace Files

| File | Status | Notes |
|------|--------|-------|
| `.hermes.md` | ✓ Present | 60 lines, valid |
| `AGENTS.md` | ✓ Present | 202 lines, valid |
| `PROJECT_RULES.md` | ✓ Created | 176 lines |
| `MASTER_RULES.md` | ✓ Created | 180 lines |
| `CLAUDE.md` | ✓ Created | 67 lines |
| `.cursorrules` | ✓ Created | 113 lines |
| `SESSION_REPORT.md` | ✓ Present | Verified |
| `CONTRIBUTING.md` | ✓ Present | Valid |
| `docs/orchestrator-verification.md` | ✓ Present | Valid |

## Provider Chain

| Priority | Provider | Model | Status |
|----------|----------|-------|--------|
| Primary | openrouter | google/gemma-4-31b-it:free | ✓ Active |
| 2 | openrouter | nemotron-3-ultra | ✓ Available |
| 3 | openrouter | hy3 | ✓ Available |
| 4 | openrouter | laguna-m.1 | ✓ Available |
| 5 | openrouter | laguna-xs-2.1 | ✓ Available |
| 6 | openrouter | nemotron-3-super | ✓ Available |
| 7 | openrouter | north-mini-code | ✓ Available |
| 8 | openrouter | gemma-4-26b | ✓ Available |
| 9 | openrouter | gpt-oss-20b | ✓ Available |
| 10 | openrouter | nemotron-3-nano | ✓ Available |
| 11 | openrouter | nemotron-nano-9b | ✓ Available |

## MCP Servers (14)

| Server | Purpose | Status |
|--------|---------|--------|
| ast-grep | code search/replace | ✓ Configured |
| code-sandbox | Node.js jest | ✓ Configured |
| codex | Codex CLI | ✓ Configured |
| copilot-mcp | Copilot provider | ✓ Configured |
| fetch | HTTP | ✓ Configured |
| filesystem | file ops (sandboxed) | ✓ Configured |
| github | GitHub API | ✓ Configured |
| linear | project mgmt | ✓ Configured |
| mcp-docker | containers | ✓ Configured |
| memory | persistent memory | ✓ Configured |
| mindstudio | MindStudio | ✓ Configured |
| playwright | browser automation | ✓ Configured |
| sequential-thinking | reasoning | ✓ Configured |
| smithery | registry | ✓ Configured |

## Hooks (3)

- `session-logger`
- `session-auto-commit`
- `governance-audit`

## Plugins (15 enabled)

`basic`, `copilot-provider`, `custom-provider`, `disk-cleanup`, `huggingface-provider`, `langfuse`, `nous`, `nous-provider`, `ollama-cloud-provider`, `openai-codex`, `openai-codex-provider`, `opencode-zen-provider`, `openrouter-provider`, `security-guidance`, `web-tavily`

## Toolsets (16)

`web`, `browser`, `terminal`, `file`, `code_execution`, `vision`, `image_gen`, `tts`, `skills`, `todo`, `memory`, `context_engine`, `session_search`, `clarify`, `delegation`, `cronjob`

## Verification Summary

| Check | Status |
|-------|--------|
| All 5 mandatory skills loaded | ✓ |
| USER.md < 1375 bytes | ✓ (373 bytes) |
| MEMORY.md < 2200 bytes | ✓ (1053 bytes) |
| Profile routing table valid | ✓ |
| MCP servers configured | ✓ |
| Context files in hierarchy | ✓ |