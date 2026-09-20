# SPEC.md — MCP Configuration Unification & Heavy-to-Lightweight Migration

**Goal**: Unify MCP server configurations across OpenCode, Copilot, Cursor Agent, and Hermes into a single canonical source, replace 5 heavy MCP servers with lightweight alternatives, and ensure cross-tool parity — all while preserving disk space and battery health.

**Source**: User request (2026-09-20). Clarifying questions asked: 5 turns, 5/5 answered.

---

## 1. Scope and Non-Goals

### In Scope
- Inventory all configuration files across opencode, copilot, cursor-agent, and hermes
- Designate `.github/mcp.json` as the canonical source of truth
- Merge OpenCode's extra servers (django, docs, evals, pytest, postgres, time) into `.github/mcp.json`
- Replace 5 heavy MCP servers with lightweight alternatives
- Create `.vscode/mcp.json` for VS Code parity
- Delete duplicate `opencode.json` in repo root
- Update `.github/prompts/ci-cd/all-repo-docker-setup/all-repo-docker-setup.prompt.md` to remove clone/build/scan/prune and add bun+uv setup

### Out of Scope
- Modifying `~/.opencode/opencode.json` (kept as the user's personal full config)
- Changing individual project-level `.cursorrules` or `copilot-instructions.md` files
- Modifying Hermes profile configs (e.g., `config.yaml` in Hermes home)
- Removing servers the user explicitly wants to keep

---

## 2. Definitions

| Term | Meaning |
|---|---|
| **Canonical MCP source** | `.github/mcp.json` — the single source of truth for MCP server definitions |
| **Heavy MCP server** | A server that installs large runtimes, browsers, or sandboxes on every invocation (high disk + battery cost) |
| **Lightweight alternative** | A Hermes-native tool (`browser_exec`, `execute_code`, `terminal`, `tool_search`) or a direct CLI invocation that achieves the same outcome without the MCP server overhead |
| **Cross-tool parity** | All tools (OpenCode, Copilot, Cursor Agent, Hermes, VS Code) reference the same MCP server definitions, with no conflicting duplicates |

---

## 3. Current State Inventory

### 3.1 Configuration Files Found

| File | Path | Size | Purpose |
|---|---|---|---|
| OpenCode pointer | `~/Desktop/SandBox/opencode.json` | 82 B | Thin pointer to `opencode.md` — **DELETE** |
| OpenCode full config | `~/.opencode/opencode.json` | 4932 B | Full MCP config with 22 servers — **KEEP** |
| Canonical MCP | `~/Desktop/SandBox/.github/mcp.json` | 3220 B | Repo MCP source of truth — **EXPAND** |
| VS Code MCP | `~/Desktop/SandBox/.vscode/mcp.json` | — | Does NOT exist — **CREATE** |
| Hermes config | `~/Desktop/SandBox/config.yaml` | 1474 B | References `.github/mcp.json` as canonical |
| Cursor rules | `~/Desktop/SandBox/.cursor/rules/sandbox.mdc` | 1204 B | References `.github/mcp.json` |
| Copilot instructions | `~/Desktop/SandBox/copilot-instructions.md` | 585 B | References `.github/mcp.json` |
| AGENTS.md | `~/Desktop/SandBox/AGENTS.md` | 17041 B | References `.github/mcp.json` |
| .hermes.md | `~/Desktop/SandBox/.hermes.md` | 6463 B | References `.github/mcp.json` |

### 3.2 MCP Server Inventory

#### In `.github/mcp.json` (canonical — 22 servers)

| Server | Type | Command/URL | Heavy? |
|---|---|---|---|
| ast-grep | local (npx) | `npx -y @notprolands/ast-grep-mcp` | No |
| code-sandbox | local (npx) | `npx -y node-code-sandbox-mcp` | **YES** |
| context7 | remote | `https://mcp.context7.com/mcp` | No |
| fetch | local (npx) | `npx -y mcp-server-fetch-tools` | No |
| filesystem | local (npx) | `npx -y @modelcontextprotocol/server-filesystem C:/Users/Alexa` | No |
| github | local (npx) | `npx -y @modelcontextprotocol/server-github` | No |
| honcho | remote | `https://mcp.honcho.dev/` | No |
| memory | local (npx) | `npx -y @modelcontextprotocol/server-memory` | No |
| neon | remote | `https://mcp.neon.tech/mcp` | No |
| parallel-search | remote | `https://search.parallel.ai/mcp` | No |
| parallel-task | remote | `https://task-mcp.parallel.ai/mcp` | No |
| playwright | local (npx) | `npx -y @playwright/mcp@latest` | **YES** |
| python-quality | local (python) | `C:/Users/Alexa/myvenv/Scripts/python ...` | No |
| sequential-thinking | local (npx) | `npx -y @modelcontextprotocol/server-sequential-thinking` | No |
| smithery | remote | `https://mcp.smithery.ai/` | **YES** |
| tavily | remote | `https://mcp.tavily.com/mcp` | No |
| tooling-config | local (python) | `C:/Users/Alexa/myvenv/Scripts/python ...` | No |
| tooling-lint | local (python) | `C:/Users/Alexa/myvenv/Scripts/python ...` | No |
| mcp-docker | local (docker) | `docker mcp gateway run` | **YES** |
| sentry | remote | `https://mcp.sentry.dev/mcp` | No |
| mindstudio | local (cli) | `mindstudio mcp` | **YES** |
| vercel | remote | `https://mcp.vercel.com` | No |
| twilio-docs | remote | `https://mcp.twilio.com/docs` | No |
| atlassian | remote | `https://mcp.atlassian.com/v1/mcp/authv2` | No |

#### Extra in `~/.opencode/opencode.json` (not in `.github/mcp.json`)

| Server | Type | Command/URL |
|---|---|---|
| django | local (bunx) | `bunx -y django-mcp` |
| docs | local (bunx) | `bunx -y docs-mcp docs/` |
| evals | local (bunx) | `bunx -y @modelcontextprotocol/server-evals` |
| postgres | local (bunx) | `bunx -y postgres-mcp` |
| pytest | local (bunx) | `bunx -y pytest-mcp` |
| time | local (bunx) | `bunx -y @modelcontextprotocol/server-time` |

#### Missing from `.github/mcp.json` (present in OpenCode)

| Server | Action |
|---|---|
| django | Add to `.github/mcp.json` |
| docs | Add to `.github/mcp.json` |
| evals | Add to `.github/mcp.json` |
| postgres | Add to `.github/mcp.json` |
| pytest | Add to `.github/mcp.json` |
| time | Add to `.github/mcp.json` |

#### Extra in `.github/mcp.json` (not in OpenCode)

| Server | Action |
|---|---|
| honcho | Keep in `.github/mcp.json` (Hermes-specific) |
| vercel | Keep in `.github/mcp.json` |
| atlassian | Keep in `.github/mcp.json` |
| sentry | Keep in `.github/mcp.json` |
| twilio-docs | Keep in `.github/mcp.json` |

---

## 4. Requirements

### R1: Canonical Source
- [ ] `.github/mcp.json` MUST be the single source of truth for all MCP server definitions
- [ ] All other config files MUST reference `.github/mcp.json` or be synced from it
- [ ] `.github/mcp.json` MUST contain the superset of all servers from both `.github/mcp.json` and `~/.opencode/opencode.json`

### R2: Merge OpenCode Extras
- [ ] The 6 extra servers from OpenCode (django, docs, evals, postgres, pytest, time) MUST be added to `.github/mcp.json`
- [ ] They MUST use `npx.cmd` / `npx` style to match existing convention in `.github/mcp.json`

### R3: Heavy-to-Lightweight Migration
- [ ] `playwright` MCP server MUST be removed from `.github/mcp.json` and replaced with Hermes `browser_exec` tool usage
- [ ] `code-sandbox` MCP server MUST be removed from `.github/mcp.json` and replaced with Hermes `execute_code` + `terminal` tools
- [ ] `smithery` MCP server MUST be removed from `.github/mcp.json` and replaced with Hermes `tool_search` + `tool_describe` + `tool_call` tools
- [ ] `mcp-docker` MCP server MUST be removed from `.github/mcp.json` and replaced with `docker` CLI via `terminal` tool
- [ ] `mindstudio` MCP server MUST be removed from `.github/mcp.json` — mindstudio CLI can be invoked directly via `terminal` when needed

### R4: Cross-Tool Parity
- [ ] `.vscode/mcp.json` MUST be created with the same content as `.github/mcp.json`
- [ ] Copilot MUST continue using `.github/mcp.json` (no separate MCP file needed)
- [ ] Cursor Agent MUST continue using `.github/mcp.json` (no separate MCP file needed)
- [ ] OpenCode (`~/.opencode/opencode.json`) MUST be updated to match `.github/mcp.json` in shared servers, keeping only OpenCode-specific extras if any remain

### R5: Duplicate Removal
- [ ] `~/Desktop/SandBox/opencode.json` (82B pointer file) MUST be deleted
- [ ] `~/.opencode/opencode.json` (4932B full config) MUST be kept

### R6: Documentation
- [ ] `.hermes.md` MUST be updated to reflect the new canonical MCP source and the removal of heavy servers
- [ ] `config.yaml` MUST be updated if MCP server list changes affect it

---

## 5. Constraints and Invariants

- **Never** read, print, or commit `.env` contents
- **Never** fabricate MCP server entries or tool capabilities
- **Always** verify file operations with `os.path.getsize` / file existence checks
- `.env` sizes must remain unchanged (CWD: 5274 B, Hermes: 30269 B)
- 0 new `.bak` artifacts
- Preserve all existing server URLs, auth modes, and environment variables when migrating

---

## 6. Heavy-to-Lightweight Replacement Map

| Heavy Server | Removal Impact | Lightweight Replacement | Hermes Tool |
|---|---|---|---|
| `playwright` | Browser automation via MCP | Direct browser automation | `browser_exec` |
| `code-sandbox` | Sandboxed JS execution via MCP | Direct code execution | `execute_code` + `terminal` |
| `smithery` | MCP server registry/client | Tool discovery + invocation | `tool_search` + `tool_describe` + `tool_call` |
| `mcp-docker` | Docker MCP gateway | Direct Docker CLI | `terminal` (docker commands) |
| `mindstudio` | AI agent orchestration MCP | Direct CLI or Hermes native | `terminal` (mindstudio CLI) or Hermes tools |

---

## 7. File Operation Summary

| Operation | File | Action |
|---|---|---|
| Update | `.github/mcp.json` | Add 6 servers, remove 5 heavy servers |
| Create | `.vscode/mcp.json` | Copy of updated `.github/mcp.json` |
| Delete | `~/Desktop/SandBox/opencode.json` | Remove pointer file |
| Update | `~/.opencode/opencode.json` | Align shared servers with `.github/mcp.json` |
| Update | `.github/prompts/ci-cd/all-repo-docker-setup/all-repo-docker-setup.prompt.md` | Remove clone/build/scan/prune; add bun+uv |
| Update | `.hermes.md` | Reflect new MCP state |
| Update | `config.yaml` | Reflect new MCP state if needed |

**Total files affected**: 7 (3 creates/updates, 1 delete, 3 updates) — exceeds 4-file threshold → multi-file-crud-protocol applies.

---

## 8. Acceptance Criteria

1. `.github/mcp.json` contains 23 servers (22 original - 5 heavy + 6 OpenCode extras = 23)
2. None of the 5 heavy servers (playwright, code-sandbox, smithery, mcp-docker, mindstudio) appear in `.github/mcp.json`
3. All 6 OpenCode extras (django, docs, evals, postgres, pytest, time) appear in `.github/mcp.json`
4. `.vscode/mcp.json` exists and matches `.github/mcp.json`
5. `~/Desktop/SandBox/opencode.json` does NOT exist
6. `~/.opencode/opencode.json` retains its full config but shared servers are aligned
7. Docker prompt no longer instructs to clone, build, scan, or prune
8. Docker prompt includes a bun+uv setup subgoal
9. `.hermes.md` and `config.yaml` reflect the changes
10. `.env` sizes unchanged; 0 new `.bak` files

---

## 9. Linked Artifacts

- **Plan**: `.hermes/plans/mcp-config-unification-2026-09-20/PLAN.md`
- **Prompt**: `.github/prompts/ci-cd/all-repo-docker-setup/all-repo-docker-setup.prompt.md` (updated)
