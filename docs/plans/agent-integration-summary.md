# ACPX Agent Integration Summary

**Date:** June 1, 2026
**Scope:** Integrate Qwen Code, OpenCode, and GitHub Copilot CLI as ACPX coding agents

## What Was Done

### Phase 1: Discovery & Research
- Web-searched and extracted README from all three repos
- Verified all agents already installed (pre-existing)
- Identified auth/config state for each agent

### Phase 2: Configuration

**Hermes config.yaml** (`C:\Users\Alexa\AppData\Local\hermes\config.yaml`):
- Added `qwen-code` provider (OpenRouter API, chat_completions mode)
- Added `opencode-acp` provider (acp://opencode protocol)
- Added both to `fallback_providers` list
- Verified config check passes

**OpenCode** (`~/.config/opencode/`):
- Updated `hooks.json` with ACPX session lifecycle hooks
- Auth: 3 providers configured (GitHub Copilot, Google, OpenCode Zen)
- Model prefix `opencode/` documented

**Qwen Code** (`~/.qwen/`):
- Created `mcp-servers.json` with shared MCP servers (filesystem, sequential-thinking, context7, gh_grep)
- Auth: OpenRouter API key configured in settings.json
- Verified smoke test: `QWEN_SMOKE_OK`

**SandBox Project**:
- Created `.opencode.json` with project-level OpenCode config
- Created `.opencode/rules/acpx-integration.md` with local notes
- Updated `AGENTS.md` with ACPX section

### Phase 3: Skills Created/Updated

| Skill | Type | Purpose |
|-------|------|---------|
| `qwen-code` | NEW | Qwen Code ACPX integration patterns |
| `copilot-cli` | NEW | Copilot CLI ACPX integration with rate limit mgmt |
| `opencode` | UPDATED | ACPX server mode, agent selection, model prefix pitfalls |
| `acpx-agent-routing` | NEW | Task-to-agent routing table for all 3 agents |

### Phase 4: Plans & Specs

- `docs/plans/agent-integration-plan.md` — 5-phase implementation plan
- `docs/plans/agent-integration-specs.md` — Feature spec with acceptance criteria

## Agent Status

| Agent | Version | Auth | Working? | Notes |
|-------|---------|------|----------|-------|
| Qwen Code | 0.17.0 | OpenRouter API key | YES | Smoke test passed |
| OpenCode | 1.15.12 | 3 providers | PARTIAL | `run` model prefix issue, ACP server works |
| Copilot CLI | 1.0.33 | GH token | RATE-LIMITED | Weekly limit hit June 1, 2026 |

## Known Issues

1. **Copilot CLI**: Weekly rate limit exhausted (resets ~June 8). Use OpenCode/Qwen Code as fallbacks.
2. **OpenCode `run`**: Model names require `opencode/` prefix. `run` command may time out on slow providers.
3. **Qwen OAuth**: Discontinued April 2026. Must use API key (OpenRouter) or local model.
4. **bun-pty**: Unavailable on this Windows install. PTY tools disabled but CLI modes work.

## Files Changed

**In SandBox repo:**
- `AGENTS.md` — Added ACPX Coding Agent Integration section
- `.opencode.json` — New project-level OpenCode config
- `.opencode/rules/acpx-integration.md` — New ACPX integration notes
- `docs/plans/agent-integration-plan.md` — New plan document
- `docs/plans/agent-integration-specs.md` — New spec document

**In Hermes config (not in repo):**
- `config.yaml` — Added qwen-code, opencode-acp providers + fallbacks
- `skills/autonomous-ai-agents/qwen-code/SKILL.md` — New skill
- `skills/autonomous-ai-agents/copilot-cli/SKILL.md` — New skill
- `skills/autonomous-ai-agents/opencode/SKILL.md` — Updated
- `skills/autonomous-ai-agents/acpx-agent-routing/SKILL.md` — New skill
- `.config/opencode/hooks/hooks.json` — Updated with ACPX hooks
- `.qwen/mcp-servers.json` — New MCP server config
