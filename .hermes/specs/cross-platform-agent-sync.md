---
name: cross-platform-agent-sync
title: Cross-Platform AI Agent & MCP Server Sync — Spec
description: |
  End-to-end specification for synchronizing all AI agents (Hermes, OpenCode, Codex, GitHub Copilot, VS Code MCP) — inventory, parity detection, and create/update/debug/fix/enhance for skills, hooks, quick commands, and MCP server configurations across all platforms. Single source of truth: Hermes is canonical for skills/hooks; VS Code + Copilot receive mirrors; Codex is a separate ecosystem tracked by inventory only.
version: 1.0.0
author: Hermes Agent
license: MIT
status: draft
tags:
  - cross-platform
  - sync
  - agents
  - mcp
  - skills
  - hooks
  - quick-commands
  - spec
---

# Cross-Platform AI Agent & MCP Server Sync — Specification

## Goal

Deliver a single, living specification that documents every AI agent platform on this machine, every MCP server configured on each platform, every skill/hook/quick-command asset, and the exact sync actions needed to achieve full parity. The spec is the contract; the plan ( companion `.hermes/plans/` file) is the execution blueprint.

## Scope

### In Scope

| Platform | Install root | Agent definitions | MCP servers | Skills | Hooks | Quick commands |
|---|---|---|---|---|---|---|
| **Hermes** | `~/AppData/Local/hermes/` | 13 profiles in `profiles/` | 22 MCP servers in `config.yaml` `mcp_servers:` | 797 SKILL.md files in `skills/` | 3 hook dirs + standalone .py scripts in `hooks/` | 6 exec/alias commands in `config.yaml` `quick_commands:` |
| **OpenCode (oh-my-opencode)** | `~/.omo/omo.jsonc` + `~/.opencode/` | 11 agents in `omo.jsonc` `agents:` + categories | None configured (relies on Hermes MCP) | Skills inherited via Hermes sync | None (Hermes hooks serve all) | None (Hermes quick_commands serve all) |
| **OpenAI Codex** | `~/.codex/` (`config.toml`) | 144 `agents/*.toml` + 18 plugins | 3 MCP servers in `config.toml` `[mcp_servers]` | `skills/hermes-auto/` bundle (separate ecosystem) | None | None |
| **GitHub Copilot** | `~/.copilot/` (`config.json`) | 30 `.github/agents/*.agent.md` + 7 installed plugins | 1 MCP server in `.copilot/mcp.json` | Mirror from Hermes → `.github/skills/` | Mirror from Hermes → `.github/hooks/` | None (VS Code keybindings) |
| **VS Code** | `~/AppData/Roaming/Code/User/` + workspace `.vscode/` | None (MCP servers only, agents via Copilot) | 12 MCP servers in `.vscode/mcp.json` (SandBox) + 2 global | None (relies on `.github/skills/` mirror) | None | None |

### Out of Scope

- Individual agent prompt/content auditing (covered by `2026-08-15_four-agent-prompt-audit-spec.md`)
- Prompt library normalization (covered by existing enhancement tooling in `.github/prompts/.enhance/`)
- Individual project-level `.vscode/mcp.json` files across 14 subproject workspaces — only the SandBox root `.vscode/mcp.json` is in scope
- Hermes profile content (SOUL.md, USER.md, MEMORY.md) — those are user-specific, not syncable
- Codex `agents/*.toml` content — Codex is a separate ecosystem; we track counts and detect staleness only

---

## Platform State Summary

### Hermes (CANONICAL for skills, hooks, quick commands, MCP servers)

#### MCP Servers (22 active, from `hermes mcp list`)

| # | Name | Transport | Type | Notes |
|---|---|---|---|---|
| 1 | honcho | https://mcp.honcho.dev/ | HTTP | Honcho memory/peer API |
| 2 | ast-grep | npx -y @notprolands/ast-grep-mcp | stdio | AST code search/rewrite |
| 3 | code-sandbox | npx -y node-code-sandbox-mcp | stdio | Isolated JS sandbox |
| 4 | fetch | npx -y mcp-server-fetch-typescript | stdio | Web page fetch/extraction |
| 5 | filesystem | npx -y @modelcontextprotocol/server-filesystem | stdio | File read/write/search |
| 6 | github | npx -y @modelcontextprotocol/server-github | stdio | GitHub API (REST/GraphQL) |
| 7 | mcp-docker | docker mcp gateway run --profile adminbot | stdio | Docker MCP gateway |
| 8 | memory | npx -y @modelcontextprotocol/server-memory | stdio | Vector memory store |
| 9 | mindstudio | mindstudio mcp | stdio | Image analysis, LLM calls |
| 10 | neon | https://mcp.neon.tech/mcp | HTTP | Neon Postgres DB |
| 11 | playwright | npx -y @playwright/mcp@0.0.78 | stdio | Browser automation |
| 12 | sequential-thinking | npx -y @modelcontextprotocol/server-sequential-thinking | stdio | Chain-of-thought reasoning |
| 13 | python-quality | C:\Users\Alexa\AppData\Local\hermes\skills\python-quality\mcp_server.py | stdio | Python lint/format/typecheck |
| 14 | tooling-lint | C:\Users\Alexa\AppData\Local\hermes\skills\tooling-lint\mcp_server.py | stdio | ESLint/Prettier/Markdownlint/CSpell |
| 15 | tooling-config | C:\Users\Alexa\AppData\Local\hermes\skills\tooling-config\mcp_server.py | stdio | gitignore/editorconfig/precommit |
| 16 | context7 | https://mcp.context7.com/mcp | HTTP | Library docs retrieval |
| 17 | sentry | https://mcp.sentry.dev/mcp | HTTP | Sentry error tracking |
| 18 | tavily | https://mcp.tavily.com/mcp/ | HTTP | Web search/extraction |
| 19 | parallel-search | https://search.parallel.ai/mcp | HTTP | Parallel web search |
| 20 | parallel-task | https://task-mcp.parallel.ai/mcp | HTTP | Parallel task execution |
| 21 | smithery | https://mcp.smithery.ai/alexanderrhixe30 | HTTP | Smithery toolbox |
| 22 | (copilot provider, disabled) | — | — | copilot-provider + copilot-acp-provider DISABLED (removed 2026-08-04) |

#### Skills (797 SKILL.md files)

Full skill library at `~/AppData/Local/hermes/skills/`. Categories include: acpx-executor, autonomous-ai-agents, blockchain, boost-prompt, bun-shell, ci-cd, cloudflare, code-wiki, creative (50+ sub-skills), data-science, devops (60+ sub-skills), django, documentation, drawio, email, enhance-prompt, finance, fix-prompt-frontmatter, gaming, github, health, hermes-desktop-plugins, hermes-hook-cleanup, hermes-profile-memory-sync, hermes-themes, hooks-pattern, introspection, mcp (20+ sub-skills), media, migration, mlops (15+ sub-skills), payments, planning (5 sub-skills), product, productivity (40+ sub-skills), profiles, prompt-engineering, qa (15+ sub-skills), reference, research (15+ sub-skills), search-skills-plugins-subagents, security, shop-app, smart-home, social-media, software-development (30+ sub-skills), subagent-driven-development, tooling, web-development.

#### Hooks (active, from config.yaml `hooks:`)

| Hook | Files | Trigger |
|---|---|---|
| session-logger | `hooks/session-logger/hook.sh` + `hooks/session_start_capture.py` + `hooks/session_end_capture.py` | on_session_start, on_session_end, pre_llm_call |
| governance-audit | `hooks/governance-audit/hook.sh` | on_session_start, on_session_end, pre_llm_call |
| session-auto-commit | `hooks/session-auto-commit/hook.sh` | on_session_end |
| pre-exec-validate | `hooks/pre-exec-validate.sh` | (script, not wired in config) |
| post-exec-state-log | `hooks/post-exec-state-log.py` + `hooks/post-exec-state-log.bat` | (script, not wired) |
| mcp_preflight_check.py | `skills/devops/mcp-server-health/scripts/mcp_preflight_check.py` | pre_llm_call (inline in config) |

#### Quick Commands (6, from config.yaml `quick_commands:`)

| Command | Type | What it does |
|---|---|---|
| `diff` | exec | `git diff --stat origin/development...HEAD` |
| `gc` | alias | Routes to `/commit` |
| `log` | exec | `git log --oneline -10` |
| `pr` | exec | Branch + unpushed log summary |
| `st` | exec | `git status --short \| head -30` |
| `tree` | exec | Project directory tree |
| `ws` | exec | `pwd` |

### OpenCode (oh-my-opencode)

- Config: `~/.omo/omo.jsonc` — 11 named agents (atlas, explore, hephaestus, librarian, metis, momus, multimodal-looker, oracle, prometheus, sisyphus, sisyphus-junior) + 8 categories. All use `opencode/deepseek-v4-flash-free`.
- No MCP servers configured directly — OpenCode uses Hermes as the provider backend via opencode-zen plugin.
- No separate skills/hooks/quick commands — inherits everything from Hermes.

### OpenAI Codex

- Config: `~/.codex/config.toml` — model `gpt-5.4-mini`, personality `pragmatic`.
- MCP servers (3): `MCP_DOCKER` (docker gateway), `Neon` (HTTP with Bearer token), `node_repl` (local Node REPL).
- 18 plugins enabled: documents, presentations, spreadsheets, github, superpowers, pdf, template-creator, visualize, chrome, computer-use, browser, + 7 more.
- 144 agents in `~/.codex/agents/*.toml`.
- Skills: `~/.codex/skills/hermes-auto/` bundle — separate ecosystem, not directly synced from Hermes.

### GitHub Copilot

- Config: `~/.copilot/config.json` — 7 installed plugins (advanced-security, ai-ready, awesome-copilot, context-engineering, copilot-goal-skill, convert-to-md, database-data-management).
- MCP server: `github-agentic-workflows` via `gh aw mcp-server` (1 server).
- 30 workspace agents in `.github/agents/*.agent.md`.
- VS Code extension: Copilot Chat v1.230.0+ — agents, plugins, MCP via `.github/` and `~/.copilot/`.

### VS Code (SandBox workspace)

- `.vscode/mcp.json`: 12 MCP servers — ast-grep, code-sandbox, context7, fetch, filesystem, github, mcp-docker, memory, neon, playwright, sentry, sequential-thinking, smithery, tavily.
- Global VS Code `mcp.json`: 2 servers — MCP_DOCKER, Parallel Search MCP.
- No separate skills/hooks — consumes `.github/skills/` mirror.

---

## Sync Matrix: What Syncs Where

| Asset | Hermes (canonical) | → VS Code `.vscode/mcp.json` | → Copilot `.github/` | → Codex | → OpenCode |
|---|---|---|---|---|---|
| MCP server configs | config.yaml `mcp_servers:` | Mirror: 12 of 22 present (see gaps below) | Mirror: 1 of 22 (`github-agentic-workflows`) | Separate: 3 own servers | Inherits via Hermes |
| Skills (SKILL.md) | `skills/*/` (797) | None natively; consumed via `.github/skills/` if mirrored | `.github/skills/` (mirror target) | `~/.codex/skills/hermes-auto/` (separate) | Inherits via Hermes |
| Hooks | `hooks/*/` (active) | None | `.github/hooks/` (reference mirror) | None | Inherits via Hermes |
| Quick commands | config.yaml `quick_commands:` | None | None | None | Inherits via Hermes |
| Agent definitions | 13 profiles | None | `.github/agents/*.agent.md` (30) | `~/.codex/agents/*.toml` (144) | `~/.omo/omo.jsonc` (11 agents) |

---

## MCP Server Parity Gaps (Hermes → VS Code)

Hermes has 22 active MCP servers. VS Code SandBox `.vscode/mcp.json` has 12. Here are the gaps:

### Present in both (12 matched)

| MCP Server | Hermes | VS Code |
|---|---|---|
| ast-grep | npx -y @notprolands/ast-grep-mcp | npx -y @notprolands/ast-grep-mcp |
| code-sandbox | npx -y node-code-sandbox-mcp | npx -y node-code-sandbox-mcp |
| context7 | https://mcp.context7.com/mcp | https://mcp.context7.com/mcp |
| fetch | npx -y mcp-server-fetch-typescript | npx -y mcp-server-fetch-typescript |
| filesystem | npx -y @modelcontextprotocol/server-filesystem | npx -y @modelcontextprotocol/server-filesystem |
| github | npx -y @modelcontextprotocol/server-github | npx -y @modelcontextprotocol/server-github |
| mcp-docker | docker mcp gateway run --profile adminbot | docker mcp gateway run --profile adminbot |
| memory | npx -y @modelcontextprotocol/server-memory | npx -y @modelcontextprotocol/server-memory |
| neon | https://mcp.neon.tech/mcp | https://mcp.neon.tech/mcp |
| playwright | npx -y @playwright/mcp@0.0.78 | npx -y @playwright/mcp@0.0.78 |
| sequential-thinking | npx -y @modelcontextprotocol/server-sequential-thinking | npx -y @modelcontextprotocol/server-sequential-thinking |
| tavily | https://mcp.tavily.com/mcp/ | https://mcp.tavily.com/mcp/ |

### Missing from VS Code `.vscode/mcp.json` (10 Hermes servers not mirrored)

| # | MCP Server | Hermes transport | VS Code gap | Action |
|---|---|---|---|---|
| 1 | **honcho** | https://mcp.honcho.dev/ | Not in VS Code | ADD to `.vscode/mcp.json` |
| 2 | **mindstudio** | mindstudio mcp (CLI) | Not in VS Code | ADD to `.vscode/mcp.json` |
| 3 | **sentry** | https://mcp.sentry.dev/mcp | Not in VS Code (global VS Code has it, SandBox doesn't) | ADD to `.vscode/mcp.json` |
| 4 | **smithery** | https://mcp.smithery.ai/alexanderrhixe30 | Already in VS Code? No — check: SandBox `.vscode/mcp.json` HAS smithery. | ✓ Already present |
| 5 | **python-quality** | Local Python script | Not in VS Code | ADD to `.vscode/mcp.json` (stdio, Python path) |
| 6 | **tooling-lint** | Local Python script | Not in VS Code | ADD to `.vscode/mcp.json` (stdio, Python path) |
| 7 | **tooling-config** | Local Python script | Not in VS Code | ADD to `.vscode/mcp.json` (stdio, Python path) |
| 8 | **parallel-search** | https://search.parallel.ai/mcp | Not in VS Code (global VS Code has it, SandBox doesn't) | ADD to `.vscode/mcp.json` |
| 9 | **parallel-task** | https://task-mcp.parallel.ai/mcp | Not in VS Code | ADD to `.vscode/mcp.json` |
| 10 | **copilot** (disabled provider) | N/A (disabled) | N/A | Document as intentionally absent |

**Correction on #4**: SandBox `.vscode/mcp.json` DOES have smithery. So 9 missing, not 10.

### VS Code-only servers (not in Hermes)

| Server | VS Code location | Hermes status | Action |
|---|---|---|---|
| Parallel Search MCP (global VS Code) | `~/AppData/Roaming/Code/User/mcp.json` | Not in Hermes `mcp_servers:` | ADD to Hermes config.yaml (optional, for parity) |

---

## Skills Sync: Hermes → Copilot (`.github/skills/`)

- Hermes canonical: 797 SKILL.md files across ~130 skill directories.
- Copilot mirror target: `workspace/.github/skills/` — needs inventory.
- Sync direction: Hermes → `.github/skills/` only (Hermes is canonical).
- Each skill directory that exists in Hermes but not in `.github/skills/` should be copied.
- Skills that exist in both: verify the `.github/` copy is not stale (compare mtime or content hash).

### Skill categories that MUST be mirrored to `.github/skills/`

These are the skill areas most relevant to Copilot/VS Code consumption:

| Category | Why mirror | Priority |
|---|---|---|
| `software-development/*` | Code review, debugging, TDD, refactoring — directly relevant to Copilot coding | P0 |
| `mcp/*` | MCP server setup, configuration, diagnostics — relevant to VS Code MCP users | P0 |
| `devops/*` | CI/CD, Docker, Terraform, Azure — relevant to Copilot devops agents | P0 |
| `github/*` | GitHub CLI, PRs, issues, workflows — directly relevant to Copilot | P0 |
| `planning/*` | Plans, specs, brainstorming — relevant to Copilot planning agents | P1 |
| `productivity/*` | Docs, sheets, meetings — relevant to Copilot productivity | P1 |
| `creative/*` | Diagrams, HTML artifacts — relevant to Copilot frontend | P1 |
| `research/*` | Web research, scraping — relevant to Copilot research | P1 |
| `security/*` | Security audit, forensics — relevant to Copilot security | P1 |
| `qa/*` | Testing, playwright, audit — relevant to Copilot QA | P1 |
| `web-development/*` | Cloudflare deploy, firecrawl — relevant to Copilot web | P1 |
| All others | Nice to have for full mirror | P2 |

---

## Hooks Sync: Hermes → Copilot (`.github/hooks/`)

- Hermes active hooks: `session-logger`, `governance-audit`, `session-auto-commit` (wired in config.yaml) + standalone scripts (`pre-exec-validate.sh`, `post-exec-state-log.py`, `mcp_preflight_check.py`).
- `.github/hooks/` is a **reference-only copy** — verify but never overwrite active hooks from reference.
- If `.github/hooks/` exists and is stale, sync FROM Hermes → `.github/hooks/` (one direction).
- If `.github/hooks/` does not exist, create it as a reference mirror.

---

## Quick Commands Sync

- Hermes quick commands are defined in `config.yaml` `quick_commands:` — these are Hermes CLI-specific and NOT portable to other platforms.
- Other platforms don't have a direct equivalent:
  - OpenCode: uses Hermes quick commands via the Hermes backend
  - Codex: has its own shell/command system, no direct mapping
  - Copilot: VS Code keybindings + slash commands
  - VS Code: has tasks.json + keybindings
- **Decision**: Quick commands are Hermes-native. Document them in a cross-platform reference (`docs/quick-commands-reference.md`) so other agents know what's available, but don't try to replicate them on other platforms.

---

## Acceptance Criteria

### AC1 — Inventory Complete
- [ ] A single document (`docs/ai-agents-inventory.md` or updated `docs/cross-platform-agent-inventory.md`) lists every agent platform with: CLI root, agent count, agent definition format, MCP server count, skill count, hook count, quick command count.
- [ ] Inventory is generated by probing the live filesystem (not hardcoded).
- [ ] Inventory includes an "as of" timestamp.

### AC2 — MCP Server Parity
- [ ] Hermes → VS Code SandBox `.vscode/mcp.json`: all 22 Hermes MCP servers either present in VS Code or explicitly documented as intentionally absent.
- [ ] VS Code → Hermes: any VS Code-only MCP servers (e.g., Parallel Search MCP in global VS Code) are evaluated for addition to Hermes.
- [ ] Hermes → Copilot: MCP server gap documented (Copilot has 1 MCP server; Hermes has 22 — this is expected since Copilot MCP is separate from VS Code MCP).

### AC3 — Skills Parity
- [ ] `.github/skills/` exists and mirrors at minimum the P0+P1 skill categories from Hermes (software-development, mcp, devops, github, planning, productivity, creative, research, security, qa, web-development).
- [ ] Each mirrored skill directory has a valid SKILL.md with YAML frontmatter.
- [ ] Stale mirrors are detected and re-synced.

### AC4 — Hooks Parity
- [ ] `.github/hooks/` exists as a reference copy of active Hermes hooks.
- [ ] Every active Hermes hook (session-logger, governance-audit, session-auto-commit) has a corresponding reference file in `.github/hooks/`.
- [ ] Standalone hook scripts (pre-exec-validate.sh, post-exec-state-log.py) are referenced in `.github/hooks/README.md`.

### AC5 — Quick Commands Reference
- [ ] `docs/quick-commands-reference.md` documents all 6 Hermes quick commands with: name, type, command, description, and which platforms can use them.
- [ ] The reference is linked from `.github/copilot-instructions.md` or equivalent cross-platform doc.

### AC6 — Schema Validation
- [ ] All new/modified JSON files (VS Code `.vscode/mcp.json`, Copilot `.copilot/mcp.json`) parse as valid JSON.
- [ ] All new/modified YAML files (Hermes `config.yaml` additions) parse as valid YAML.
- [ ] All SKILL.md files in `.github/skills/` have valid YAML frontmatter.

### AC7 — Lint/Format Clean
- [ ] `bun run markdownlint` passes on all new/modified `.md` files.
- [ ] `bun run format:check` passes on all new/modified files (if applicable).
- [ ] `python -m json.tool` validates all JSON files.

### AC8 — No Destructive Changes
- [ ] No existing MCP server configurations are removed or altered (only additions).
- [ ] No existing skills in Hermes are modified — only new copies in `.github/skills/`.
- [ ] No existing hooks in Hermes are modified — only reference copies in `.github/hooks/`.
- [ ] Git diff shows only additions, no deletions or modifications to existing files.

---

## Files to Create/Modify

### New Files

| File | Purpose |
|---|---|
| `docs/cross-platform-agent-inventory.md` | Living inventory of all agents, MCP servers, skills, hooks across all platforms (or update existing) |
| `.vscode/mcp.json` (modified) | Add 9 missing MCP servers to VS Code SandBox config |
| `.github/skills/*/` (multiple dirs) | Mirror P0+P1 skills from Hermes |
| `.github/hooks/README.md` | Reference documentation for hooks mirror |
| `.github/hooks/*.sh` / `.github/hooks/*.py` | Reference copies of active Hermes hooks |
| `docs/quick-commands-reference.md` | Cross-platform quick commands documentation |
| `.hermes/plans/YYYY-MM-DD_cross-platform-agent-sync.md` | Execution plan (this spec's companion) |
| `scripts/sync-mcp-parity.py` (optional) | Script to detect and report MCP server parity gaps |
| `scripts/sync-skills-mirror.py` (optional) | Script to mirror skills from Hermes to `.github/skills/` |

### Modified Files

| File | Change |
|---|---|
| `.vscode/mcp.json` | Add 9 missing MCP server entries |
| `.github/copilot-instructions.md` | Add cross-reference to new inventory doc + quick commands reference |
| `AGENTS.md` (if exists) | Add pointer to cross-platform inventory |

### Not Modified (by design)

- `~/AppData/Local/hermes/config.yaml` — Hermes is canonical; we don't modify it from a repo-side operation
- `~/AppData/Local/hermes/skills/` — canonical skills library, not modified
- `~/AppData/Local/hermes/hooks/` — active hooks, not modified
- `~/.copilot/config.json` — Copilot config, not modified from repo
- `~/.codex/config.toml` — Codex config, not modified from repo
- `~/.omo/omo.jsonc` — OpenCode config, not modified from repo

---

## Risks & Mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| VS Code MCP server additions may fail if npx packages are not installed | Medium | Test each added server with `npx --yes <pkg>` before committing; document required packages |
| `.github/skills/` mirror bloat — 797 skills is too many to mirror | Low | Mirror only P0+P1 categories (est. 200-300 skills); document the rest as "available in Hermes only" |
| Local Python MCP servers (python-quality, tooling-lint, tooling-config) need absolute paths in VS Code | Medium | Use `${env:USERPROFILE}/AppData/Local/hermes/skills/<name>/mcp_server.py` or absolute Windows path |
| Copilot `.github/hooks/` is reference-only; syncing from reference → active would be destructive | High | Document direction clearly: Hermes → `.github/hooks/` (one way, reference copy only) |
| Codex is a separate ecosystem — attempting to mirror Hermes skills into Codex agents would break Codex's TOML format | High | Track Codex by inventory only; do NOT attempt skill mirroring into Codex |

---

## Validation Gates

1. **Inventory gate**: `python scripts/sync-mcp-parity.py --report` outputs a complete parity report with zero unknowns.
2. **JSON gate**: `python -m json.tool .vscode/mcp.json > /dev/null` exits 0.
3. **Skills mirror gate**: `find .github/skills -name "SKILL.md" | wc -l` >= expected minimum (P0+P1 categories).
4. **Hooks mirror gate**: `.github/hooks/README.md` exists and references all 3 active Hermes hooks.
5. **Markdown lint gate**: `bunx markdownlint-cli2 --config .markdownlint-cli2.jsonc "docs/*.md" ".github/hooks/README.md" ".github/copilot-instructions.md"` exits 0.
6. **Git clean gate**: `git diff --stat` shows only additions in `.vscode/mcp.json`, `.github/skills/`, `.github/hooks/`, `docs/`.

---

## Open Questions

1. Should the Parallel Search MCP server (present in global VS Code but not Hermes) be added to Hermes `config.yaml`? — **Recommendation**: Yes, for full bidirectional parity. Low risk since it's an HTTP server.
2. Should python-quality, tooling-lint, and tooling-config MCP servers be added to VS Code? — **Recommendation**: Yes, these are high-value developer tooling MCP servers that VS Code users would benefit from.
3. What's the minimum viable `.github/skills/` mirror size? — **Recommendation**: P0 categories first (software-development, mcp, devops, github), then P1 in a second pass if time permits.
4. Should we create a `scripts/sync-all.py` that does the full sync in one shot? — **Recommendation**: Yes, a single entry-point script with subcommands (`--mcp-parity`, `--skills-mirror`, `--hooks-mirror`) is the right abstraction.
