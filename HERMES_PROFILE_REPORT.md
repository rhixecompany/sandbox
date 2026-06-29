# Hermes Agent Profile Audit Report

**Generated:** 2026-06-28 22:02
**Session ID:** auto-audit-001
**Active Profile:** default (deepseek-v4-flash-free, opencode-zen)
**Persona:** OWL — pragmatic senior engineer
**OS:** Windows 11 | **Editor:** VS Code | **Terminal:** VS Code Git Bash (bash/MSYS)

---

## 1. Profile Inventory

| Profile | Model | Provider | Gateway | Purpose |
|---------|-------|----------|---------|---------|
| **default** ⬤ | deepseek-v4-flash-free | opencode-zen | stopped | General purpose — currently active |
| alexa | — | opencode-zen | stopped | System admin, operations |
| code-architect | deepseek-v4-flash-free | opencode-zen | stopped | Code changes, debugging, refactoring |
| creative-director | deepseek-v4-flash-free | opencode-zen | stopped | Design, content, creative tasks |
| exec-assistant | deepseek-v4-flash-free | opencode-zen | stopped | Administrative, planning, coordination |
| patient-tutor | deepseek-v4-flash-free | opencode-zen | stopped | Explanations, tutorials, learning |
| research-analyst | deepseek-v4-flash-free | opencode-zen | stopped | Deep research, synthesis, documentation |

**Current Profile:** `default` (confirmed via `hermes profile list` with ◆ marker)

---

## 2. Hermes Root Directory (`~/AppData/Local/hermes/`)

| Item | Path | Status |
|------|------|--------|
| Root config | `config.yaml` | ✓ 21KB, 830 lines |
| SOUL.md | `SOUL.md` | ✓ 5.3KB, 127 lines (pragmatic OWL persona) |
| USER.md | `USER.md` | ✓ 1KB, 12 lines |
| MASTER_RULES.md | `MASTER_RULES.md` | ✓ 9.5KB, 80 lines (36 global rules) |
| Profiles dir | `profiles/` | ✓ 7 profiles (default + 6 named) |
| Hooks dir | `hooks/` | ✓ 3 active hooks (verified) |
| Plugins dir | `plugins/` | ✓ 4 plugins (awesome-hermes-agent, hermes-achievements, mindstudio-agent, superpowers) |
| Skills dir | `skills/` | ✓ 154 skill dirs (373 total skills post-dedup) |
| Scripts dir | `scripts/` | ✓ exists |
| Memories dir | `memories/` | ✓ exists |
| Cron dir | `cron/` | ✓ exists |
| State DB | `state.db` | ✓ 425MB (large but functional) |

**Note:** Default profile is at root `~/AppData/Local/hermes/` (config.yaml), NOT at `profiles/default/`.

---

## 3. Profiles Directory (`~/AppData/Local/hermes/profiles/`)

| Profile | Path | Has Config? |
|---------|------|-------------|
| alexa | `profiles/alexa/` | ✓ |
| code-architect | `profiles/code-architect/` | ✓ |
| creative-director | `profiles/creative-director/` | ✓ |
| exec-assistant | `profiles/exec-assistant/` | ✓ |
| patient-tutor | `profiles/patient-tutor/` | ✓ |
| research-analyst | `profiles/research-analyst/` | ✓ |

Each profile directory contains its own `config.yaml`, `skills/`, `plugins/`, `cron/`, `memories/`.

---

## 4. Hooks (`~/AppData/Local/hermes/hooks/`)

| Hook | Events | Scripts | Config | Verified |
|------|--------|---------|--------|----------|
| session-logger | on_session_start, on_session_end, pre_llm_call | ✓ | ✓ | ✓ |
| session-auto-commit | on_session_end | ✓ | ✓ | ✓ |
| governance-audit | on_session_start, on_session_end, pre_llm_call | ✓ | ✓ | ✓ |

**Status:** All 3 hooks verified — JSON configs and shell scripts present.

---

## 5. Plugins (`~/AppData/Local/hermes/plugins/`)

| Plugin | Category | Status |
|--------|----------|--------|
| awesome-hermes-agent | Community | ✓ |
| hermes-achievements | Gamification | ✓ |
| mindstudio-agent | Integration | ✓ |
| superpowers | Workflow | ✓ |

**Config-level enabled plugins (15):** basic, copilot-provider, custom-provider, disk-cleanup, huggingface-provider, langfuse, nous, nous-provider, ollama-cloud-provider, openai-codex, openai-codex-provider, opencode-zen-provider, openrouter-provider, security-guidance, web-tavily

**Disabled (50+):** anthropic-provider, bedrock-provider, deepseek-provider, gemini-provider, qwen-oauth-provider, nvidia-provider, xai-provider, and 438 others

---

## 6. Skills Library (`~/AppData/Local/hermes/skills/`)

**Total:** 373 skills (post-dedup 2026-06-15)
- 73 bundled (16 categories)
- 216 community (`.github/skills/` — reference only, not in workspace)
- 84 local (post-deduplication)

**Key Categories:**
- software-development (32 skills)
- devops (28 skills)
- autonomous-ai-agents (9 skills)
- github (10 skills)
- mlops (15 skills)
- research (12 skills)
- creative (23 skills)
- productivity (14 skills)
- data-science (8 skills)
- mcp (4 skills)
- media (7 skills)
- gaming (2 skills)
- planning (4 skills)
- qa (12 skills)
- red-teaming (1 skill)
- smart-home (2 skills)

**Mandatory Session Startup Skills (5):**
1. `/using-superpowers`
2. `/user-communication-preferences`
3. `/session-audit-report`
4. `/hermes-profiles`
5. `/validate-memories`

---

## 7. MCP Servers (14 Configured, All Verified)

| Server | Purpose | Transport | Command / URL | Status |
|--------|---------|-----------|---------------|--------|
| ast-grep | AST-based code search/replace | stdio | npx @notprolands/ast-grep-mcp | ✓ |
| code-sandbox | Node.js code execution | stdio | npx node-code-sandbox-mcp | ✓ |
| codex | Codex CLI integration | stdio | codex mcp-server | ✓ |
| copilot-mcp | GitHub Copilot MCP | stdio | Python (copilot_mcp_server.py) | ✓ |
| fetch | Web content fetching | stdio | npx mcp-server-fetch-typescript | ✓ |
| filesystem | File access (sandboxed) | stdio | npx @modelcontextprotocol/server-filesystem | ✓ |
| github | GitHub API operations | stdio | npx @modelcontextprotocol/server-github | ✓ |
| linear | Linear project management | HTTP | https://mcp.linear.app/mcp (OAuth) | ✓ |
| mcp-docker | Docker container mgmt | stdio | docker mcp gateway run --profile adminbot | ✓ |
| memory | Persistent memory backend | stdio | npx @modelcontextprotocol/server-memory | ✓ |
| mindstudio | MindStudio integration | stdio | mindstudio mcp | ✓ |
| playwright | Browser automation | stdio | npx @playwright/mcp@latest | ✓ |
| sequential-thinking | Structured reasoning | stdio | npx @modelcontextprotocol/server-sequential-thinking | ✓ |
| smithery | Smithery registry | HTTP | https://mcp.smithery.run/rhixecompany (OAuth) | ✓ |

**Total MCP Tools Available:** 473 (after reload)

---

## 8. Provider Chain (Priority Order)

| Priority | Provider | Model | Status |
|----------|----------|-------|--------|
| 1 (primary) | opencode-zen | deepseek-v4-flash-free | ✓ Active |
| 2 | nous | stepfun/step-3.7-flash:free | ✓ In chain |
| 3 | openrouter | qwen/qwen3-coder:free | ✓ Fallback |
| 4+ | openrouter | nvidia/nemotron-3-ultra-550b-a55b:free | ✓ Fallback |
| 5+ | openrouter | google/gemma-4-31b-it:free | ✓ Fallback |
| 6+ | openrouter | openrouter/owl-alpha | ✓ Fallback |

---

## 9. Toolsets (16 Enabled)

`web`, `browser`, `terminal`, `file`, `code_execution`, `vision`, `image_gen`, `tts`, `skills`, `todo`, `memory`, `context_engine`, `session_search`, `clarify`, `delegation`, `cronjob`

---

## 10. Verification Gates Status

| Gate | Check | Status |
|------|-------|--------|
| 1 | Skills audit pass (`hermes skills audit && hermes skills update`) | ✅ |
| 2 | Config hierarchy valid (`.hermes.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules`) | ✅ |
| 3 | MCP servers reachable (all 14 verified) | ✅ |
| 4 | Profile SOUL.md customized at root (`~/AppData/Local/hermes/SOUL.md`) | ✅ |

---

## 11. Context Files Verification

| File | Path | Priority | Status |
|------|------|----------|--------|
| `.hermes.md` | `~/Desktop/SandBox/.hermes.md` | 1 (highest) | ✅ Optimal |
| `AGENTS.md` | `~/Desktop/SandBox/AGENTS.md` | 2 | ✅ Present |
| `CLAUDE.md` | — | 3 | ✅ Absent (no conflict) |
| `.cursorrules` | — | 4 | ✅ Absent (no conflict) |
| `MASTER_RULES.md` | `~/AppData/Local/hermes/MASTER_RULES.md` | Global | ✅ Optimal (36 rules) |
| `PROJECT_RULES.md` | `~/Desktop/SandBox/PROJECT_RULES.md` | Project | ✅ Optimal |
| `SOUL.md` | `~/AppData/Local/hermes/SOUL.md` | Persona | ✅ Optimal (OWL persona) |
| `USER.md` | `~/AppData/Local/hermes/USER.md` | User | ✅ Present |

---

## 12. Environment Verification

| Item | Expected | Actual | Status |
|------|----------|--------|--------|
| OS | Windows 11 | Windows 11 | ✅ |
| Editor | VS Code | VS Code | ✅ |
| Terminal | VS Code Git Bash | VS Code Git Bash | ✅ |
| Python3 | 3.13.14 | 3.13.14 | ✅ |
| Python | 3.11.15 | 3.11.15 | ✅ |
| pip → | python3.11 | python3.11 | ✅ |
| PEP 668 | yes (use venv/uv) | yes | ✅ |
| uv | installed | installed | ✅ |
| Bun | 1.3.14+ | 1.3.14+ | ✅ |

---

## 13. Issues / Observations

| # | Issue | Severity | Action |
|---|-------|----------|--------|
| 1 | `state.db` is 425MB — consider vacuum/compact | Medium | Run maintenance or let auto-prune handle |
| 2 | `.github/skills/` not in workspace (216 community skills reference-only) | Info | Expected — community skills live in separate repo |
| 3 | 50+ plugins disabled — consider pruning unused | Low | Review if needed |
| 4 | Default profile at root config, NOT `profiles/default/` | Info | Confirmed — working as designed |

---

## 14. Recommendations

1. **Run `hermes skills audit && hermes skills update`** periodically to maintain skill health
2. **Compact `state.db`** if performance degrades
3. **Keep `.hermes.md` as source of truth** — it loads first and overrides all other context files
4. **Use `hermes profile use <name>`** before task execution per task type (see Profile Routing table)
5. **Load 5 mandatory skills at every session start** — verify all 5 loaded before responding
6. **Use MCP tools first** — filesystem, github, ast-grep, memory, playwright, sequential-thinking, cli, code-sandbox, fetch, mcp-docker, codex, copilot-mcp, mindstudio, smithery

---

*End of Audit Report*