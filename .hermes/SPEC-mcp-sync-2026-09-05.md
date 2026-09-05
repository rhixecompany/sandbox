# MCP Server Ecosystem — Specification

**Workspace:** C:\Users\Alexa\Desktop\SandBox
**Generated:** 2026-09-05
**Scope:** All MCP (Model Context Protocol) server configurations across the four agent platforms used in this workspace.

---

## 1. Overview

MCP servers give LLM agents standardized access to tools, resources, and prompts. This workspace runs four agent platforms side-by-side, each with its own MCP configuration format:

| Platform | Config Path(s) | Schema Root |
|----------|----------------|-------------|
| **Hermes Agent** (default profile) | `~/.hermes/...` (managed by `hermes mcp` CLI; canonical source = `hermes mcp list`) | hermes-internal store |
| **OpenCode** | workspace `opencode.json` (root `mcp.*` block) + user `~/.config/opencode/opencode.json` (merged at runtime) | `https://opencode.ai/config.json` |
| **GitHub Copilot CLI** | workspace `.github/mcp.json` (`mcpServers.*` block) | copilot-internal |
| **Codex CLI** | workspace `.codex/mcp.json` (`mcpServers.*` block) + global OpenAI-managed | codex-internal |
| **VS Code MCP** | `.vscode/mcp.json` (`servers.*` block, schema is identical to Copilot's) | vscode-internal |

Hermes MCP servers are configured by `hermes mcp add` and stored in the hermes install directory (`~/.hermes/...`). They are NOT read from any workspace file. OpenCode uses `opencode.json`, and `~/.config/opencode/opencode.json` (user-global) is merged into the workspace config at runtime.

### 1.1 Schema Translation Matrix

| Field | opencode.json | .github/mcp.json / .codex/mcp.json / .vscode/mcp.json | hermes mcp list |
|-------|---------------|-------------------------------------------------------|----------------|
| Top-level key | `mcp` | `mcpServers` (github/codex) / `servers` (vscode) | (CLI command) |
| HTTP server | `{type: "remote", url: "..."}` | `{type: "http", url: "..."}` | `{type: "http", url: "..."}` |
| Stdio server | `{type: "local", command: [...], env: {...}}` | `{type: "stdio", command: "...", args: [...], env: {...}}` | `{type: "stdio", command: "...", args: [...], env: {...}}` |
| Disabled flag | `enabled: false` | absent from file + listed in `disabledServers[]` (github only) or simply omitted | `enabled: false` |
| Bearer token env | `url: "...${env:KEY}..."` | `url: "...${env:KEY}..."` or `env: { KEY: "..." }` | `headers: {Authorization: "Bearer ${env:KEY}"}` |
| Per-server env vars | `env: { KEY: "${env:KEY}" }` | `env: { KEY: "${env:KEY}" }` | `env: { KEY: "${env:KEY}" }` |

### 1.2 Disabled List Convention

- `opencode.json` and `.github/mcp.json` use `disabledServers: []` arrays (GitHub convention).
- `opencode.json` and `.codex/mcp.json` use per-server `enabled: false`.
- `.vscode/mcp.json` has no disabled convention; disabled servers are simply omitted.
- Hermes uses per-server `enabled: false`.

The canonical workspace source of truth is `opencode.json` (per the existing audit + sync script).

---

## 2. Current Server Inventory (post-2026-08-28-audit)

### 2.1 Hermes MCP store (per `hermes mcp list`)

27 enabled, 5 disabled, 32 total.

### 2.2 Workspace Configs

| Platform | Servers | Same as Hermes? |
|----------|---------|-----------------|
| opencode.json | 29 entries (26 enabled + 3 disabled) | Close, but missing 3 hermes-only servers: `alexanderrhixe30`, `everart` (DNS fail in hermes), and `time` is in opencode; `stripe`/`plaid`/`everart` are placeholders |
| .codex/mcp.json | 29 entries (matches opencode.json) | Yes |
| .github/mcp.json | 22 enabled + 3 disabled | Missing several: atlassian, evals, time, stripe, plaid, everart, anthropic-resources, alexanderrhixe30, copilot_mcp_server |
| .vscode/mcp.json | 29 entries (no disabled field) | Yes (everything enabled, including atlassian/docs/postgres) |

### 2.3 Server Categorization (2026-09-05 runtime check)

| Category | Servers | Status |
|----------|---------|--------|
| **HTTP MCP — verified runtime** | context7, parallel-search, tavily, mindstudio, honcho, neon, sentry, smithery | 200/401 with valid JSON-RPC `initialize` (working at runtime with bearer auth) |
| **HTTP MCP — dead endpoints** | anthropic-resources (404), stripe (404), plaid (DNS), everart (DNS), parallel-task (405 wrong URL), atlassian (disabled, 401 = needs OAuth) | Should be disabled or removed |
| **Local MCP — verified local command** | ast-grep, code-sandbox, django, evals, fetch, filesystem, github, memory, mcp-docker, playwright, postgres, pytest, python-quality, sequential-thinking, time, tooling-config, tooling-lint | Working |
| **Hermes-specific** | copilot_mcp_server, alexanderrhixe30 | Hermes-only; not in workspace configs |

---

## 3. Defects and Inconsistencies

### 3.1 Sync Script Bug (CRITICAL)

**File:** `C:\Users\Alexa\Desktop\SandBox\scripts\sync-mcp-configs.ps1`
**Bug:** Line 20, 21, 162, 163 reference `$workspaceRoot/.copilot/mcp.json`.
**Reality:** The actual GitHub Copilot config file is `$workspaceRoot/.github/mcp.json`. The `.copilot/mcp.json` path does not exist on disk.
**Effect:** The sync script silently skips sync to Copilot (the `[OK] .copilot/mcp.json: Already in sync` message is misleading — the file doesn't exist, so it actually reads nothing and writes nothing).

### 3.2 Validation Script False Positives

**File:** `scripts/validate-mcp-servers.py`
**Bug:** Uses `HEAD` HTTP requests on remote MCP URLs.
**Effect:** Many real MCP servers reject HEAD with `405 Method Not Allowed` or `404 Not Found` even when they accept POST with a valid JSON-RPC `initialize` body. This makes the validator report `context7`, `parallel-search`, `smithery`, `tavily`, `honcho`, `neon`, `sentry`, `mcp-docker` (when probed without auth) as broken, even though they actually work at runtime.
**Fix direction:** Replace HEAD probes with `POST` of JSON-RPC `initialize` and accept any 2xx response as "working."

### 3.3 Dead MCP Endpoints (CRITICAL — clean up)

| Server | URL | Status |
|--------|-----|--------|
| `anthropic-resources` | `https://resources.anthropic.com/mcp` | 404 — does not exist |
| `stripe` | `https://mcp.stripe.com/mcp` | 404 — Stripe MCP not released yet (or URL wrong) |
| `plaid` | `https://mcp.plaid.com/mcp` | DNS fail — `mcp.plaid.com` does not resolve |
| `everart` | `https://mcp.everart.ai/mcp` | DNS fail — `mcp.everart.ai` does not resolve |
| `parallel-task` | `https://task-mcp.parallel.ai/mcp` | 405 wrong endpoint (correct one is task-mcp.parallel.ai/mcp but it may not exist) |

**Fix direction:** Mark these as `enabled: false` in all configs where they exist. Add a one-line note in `opencode.json` documenting why. Do NOT delete the entries — preserves audit trail.

### 3.4 Hermes Workspace Coupling Gap

Hermes Agent reads MCP servers from its own internal store (`~/.hermes/...`), not from any workspace file. This means:
- The workspace `opencode.json` is the canonical source for **OpenCode only**.
- Hermes must be configured separately via `hermes mcp add` (it is).
- A workspace change to `opencode.json` does NOT auto-propagate to Hermes.

**Fix direction:** Document this in the new `hermes-mcp-sync` skill. Add a note to `AGENTS.md` that Hermes MCP store is its own thing and not synced from any workspace file.

### 3.5 Schema Mismatches Across Platforms

| Issue | Where | Fix |
|-------|-------|-----|
| `type: "remote"` (opencode) vs `type: "http"` (others) | opencode.json | Document; both forms work in their respective parsers. Do NOT change. |
| `mcp-server-fetch-typescript` (opencode/codex/vscode) vs `mcp-server-fetch-tools` (github) | .github/mcp.json | Update github to use the canonical name to match other configs |
| `python_quality_mcp_server.py` (opencode/codex/vscode) vs `python_quality_server.py` (github + projects/Python-projects) | .github/mcp.json + projects/Python-projects/.mcp.json | Update github/projects to canonical filename; both files exist on disk actually so this is a doc/inventory issue |
| `tooling_lint_mcp_server.py` vs `tooling_lint_server.py` | .github/mcp.json + projects/Python-projects/.mcp.json | Same as above |
| `bunx` (opencode/codex/vscode) vs `npx.cmd` (github) | .github/mcp.json | Both work; no fix needed |

### 3.6 Disabled-Server Inconsistency

- Hermes disables: `atlassian`, `docs`, `pytest`, `django` (5 disabled)
- opencode.json disables: `atlassian`, `docs`, `postgres` (3 disabled)
- .codex/mcp.json disables: `atlassian`, `docs`, `postgres` (3 disabled)
- .github/mcp.json disables: `atlassian`, `docs`, `postgres` (3 disabled)
- .vscode/mcp.json: no disabled flag — all 29 servers active (including `atlassian`, `docs`, `postgres` which are non-functional)

**Fix direction:** Set `enabled: false` for `atlassian`, `docs`, `postgres` in `.vscode/mcp.json` for parity with the other 3 platforms. Do not change hermes (intentional hermes profile config).

---

## 4. Goals

### 4.1 Functional Goals

1. **G1 — Fix the sync script** so it actually syncs to `.github/mcp.json` (the real Copilot config).
2. **G2 — Mark dead endpoints as disabled** in all workspace configs.
3. **G3 — Replace HEAD validation with JSON-RPC initialize POST** to eliminate false positives.
4. **G4 — Sync all 3 workspace configs to the same enabled-server set.**
5. **G5 — Verify each MCP server works at runtime** via live tool calls (where possible in this hermes session).
6. **G6 — Document the MCP lifecycle** in a reusable skill.

### 4.2 Non-Functional Goals

1. **NF1 — Idempotent operations**: Sync script and validation script can be run multiple times safely.
2. **NF2 — Audit trail preserved**: Disabled servers stay in the config files with `enabled: false` and a `notes` field documenting why.
3. **NF3 — Hermetic validation**: Validation script must work without making destructive changes.

---

## 5. Acceptance Criteria

The goal is complete when:

- [ ] `scripts/sync-mcp-configs.ps1` runs end-to-end and modifies `.github/mcp.json` (the real file), not a phantom `.copilot/mcp.json`.
- [ ] All 5 dead endpoints (`anthropic-resources`, `stripe`, `plaid`, `everart`, `parallel-task`) have `enabled: false` in every workspace config where they exist.
- [ ] `atlassian`, `docs`, `postgres` have `enabled: false` in `.vscode/mcp.json` for parity.
- [ ] `scripts/validate-mcp-servers.py` reports 0 false positives — i.e. it does NOT mark `context7`, `parallel-search`, `smithery`, `tavily` as broken.
- [ ] `scripts/validate-mcp-servers.py` correctly identifies `mcp-docker` (which requires a live Docker daemon) without false-negative flagging when it's actually running.
- [ ] A live hermes session can call at least 3 currently-loaded MCP tools without error (proof of runtime).
- [ ] A new `hermes-mcp-sync` SKILL.md exists in `~/.opencode/skills/` (or workspace equivalent) documenting the workflow.
- [ ] A `PLAN.md` file exists at workspace root documenting the implementation steps.
- [ ] The updated `.hermes/mcp-validation-report.md` reflects the new state.
- [ ] No new secrets are introduced; existing env-var indirection (`${env:KEY}`) is preserved.
