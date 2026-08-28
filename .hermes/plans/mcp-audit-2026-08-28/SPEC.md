---
title: MCP Server Audit, Registry & Sync — Specification
plan: .hermes/plans/mcp-audit-2026-08-28/PLAN.md
generated: 2026-08-28
profile: adminbot
model: minimax/minimax-m3:free
status: draft → ready
---

# SPEC — MCP Server Audit, Registry & Sync

## 1. Problem Statement

The SandBox workspace has MCP server definitions spread across **5 config files** with no single source of truth:

| File | Servers | Format | Owner |
|------|---------|--------|-------|
| `opencode.json` | 25 | opencode schema (`mcp.<name>.command`) | OpenCode |
| `.codex/mcp.json` | 30 | MCP std (`mcpServers.<name>`) | Codex CLI |
| `.copilot/mcp.json` | 30 | MCP std (pretty-printed) | GitHub Copilot |
| `.vscode/mcp.json` | 19 | MCP std (subset) | VS Code |
| `~/AppData/Local/hermes/config.yaml` (mcp_servers) | 25 | Hermes (npx std + http) | Hermes Agent |

**Issues observed (baseline 2026-08-28 17:30):**

1. `opencode.json` points to **non-existent scripts** for `python-quality`, `tooling-lint`, `tooling-config` — wrong filenames (`python_quality_server.py` vs actual `python_quality_mcp_server.py` on disk). 3 local MCP servers "parked" at startup.
2. `hermes doctor` warns: **Config version outdated (v38 → v39)**.
3. `hermes mcp list` reports **3 servers disabled** (atlassian, docs, postgres) but they are still present in codex/copilot/vscode configs.
4. `bun run check` fails: `format:check` rejects `.omo/run-continuation/ses_*.json` (runtime artifacts not in `.prettierignore`).
5. Default model `nvidia/nemotron-3-ultra-550b-a55b:free` returns **HTTP 404** (model retired from OpenRouter) — all fresh sessions fail immediately.
6. 13 uncommitted files in `projects/*` causing `session-auto-commit` hook to fail.
7. `hermes doctor --fix` fixes 1 of these (config version); the rest need manual work.

## 2. Goals

| # | Goal | Priority |
|---|------|----------|
| G1 | Single source of truth for all MCP server definitions | MUST |
| G2 | Deterministic sync to 4 disk configs (opencode/codex/copilot/vscode) + hermes config | MUST |
| G3 | Audit script that loads registry, tests every server, emits structured report | MUST |
| G4 | Fix the 3 broken local MCP server script paths in `opencode.json` | MUST |
| G5 | Update default model in hermes config to a verified-working model | MUST |
| G6 | Add `.omo/` to `.prettierignore` so `bun run check` passes | MUST |
| G7 | One umbrella skill `mcp-audit-orchestrator` to run the loop | MUST |
| G8 | Reusable Python + TS scripts in `scripts/` for CI and local use | MUST |
| G9 | Verify zero new warnings introduced; existing non-fixable warnings documented | SHOULD |

## 3. Non-Goals

- Fix the Hermes `PluginContext.register_flask_app` bug (upstream — document only).
- Restore Honcho credits (account action — document only).
- Sync Telegram bot plugins (out of scope; cosmetic).
- Change anything in `projects/*` (working tree churn is the user's, not mine).

## 4. Design

### 4.1 Registry Schema (`.mcp/registry.json`)

```json
{
  "$schema": "https://sandbox.local/schemas/mcp-registry.v1.json",
  "version": 1,
  "defaults": {
    "env_resolution": "${env:VAR_NAME}",
    "workspace_root": "C:/Users/Alexa/Desktop/SandBox",
    "python_runtime": "C:/Users/Alexa/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe",
    "package_runner": "bunx"
  },
  "servers": {
    "<name>": {
      "type": "stdio" | "http" | "sse",
      "command"?: "string",        // for stdio (string, not array)
      "args"?: ["string"],
      "url"?: "https://...",       // for http/sse
      "env"?: { "KEY": "value-or-${env:VAR}" },
      "enabled"?: true|false,      // mirror to hermes mcp_servers
      "description": "...",
      "tags": ["code", "browser", ...]
    }
  }
}
```

**Authoritative list — 25 servers**, derived from hermes `mcp list` (✓ enabled) + 3 disabled (kept for visibility, marked `enabled: false`).

### 4.2 Sync Algorithm

```
registry → for each target:
  - opencode.json:  mcp.<name> = { command, args, enabled, type, env? }
  - .codex/mcp.json:  mcpServers.<name> = { command, args, type, env? }
  - .copilot/mcp.json:  same as codex (pretty-printed)
  - .vscode/mcp.json:  servers.<name> = same (subset only; full list)
  - hermes config.yaml:  mcp_servers.<name> = { command: [bin, ...args] OR { url, type: http } }
```

### 4.3 Audit Algorithm

For each server in registry:
- **stdio**: spawn `bunx --version` (or check binary path exists), env-resolve `${env:...}` placeholders
- **http/sse**: HEAD/GET to URL, expect 2xx/4xx (not 5xx, not network error)
- **disabled**: skip, mark `⊘`
- Emit `.hermes/plans/mcp-audit-2026-08-28/audit-report.json` + `.md`

### 4.4 Skill Layout

```
mcp-audit-orchestrator/
├── SKILL.md                          (≤250 lines, workflow)
├── references/
│   ├── registry-spec.md              (schema docs)
│   ├── sync-targets.md               (per-target quirks)
│   └── audit-results.md              (interpreting report)
├── scripts/
│   ├── mcp_audit.py                  (loads registry, tests servers)
│   ├── mcp_sync.py                   (writes 4 disk configs)
│   └── mcp_sync.ps1                  (PowerShell wrapper for hermes doctor --fix pipeline)
└── templates/
    ├── registry.json                 (skeleton)
    └── server-entry.json             (one server template)
```

## 5. Verification Gates

Each gate is a hard check; cannot skip.

| Gate | Pass condition |
|------|---------------|
| V1 | `python scripts/mcp_audit.py --registry .mcp/registry.json` exits 0, report generated |
| V2 | `python scripts/mcp_sync.py --registry .mcp/registry.json` exits 0, all 4 files updated |
| V3 | `hermes mcp list` shows same 22 enabled + 3 disabled as baseline |
| V4 | `hermes doctor` shows no new warnings vs pre-session baseline |
| V5 | `bun run check` exits 0 (lint + format + markdownlint + spellcheck) |
| V6 | `python -c "import json; json.load(open('.mcp/registry.json'))"` succeeds (valid JSON) |
| V7 | All 4 disk configs pass `python -c "import json; json.load(open(p))"` |
| V8 | SESSION_REPORT.md updated with this session's results |

## 6. Risks

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| opencode.json format drift breaks sync | M | Use opencode.json parser, not regex |
| Hermes `mcp_servers` schema is different from codex stdio | M | Tested in baseline; sync handles both forms |
| Registry grows stale again | M | Skill workflow includes `regenerate` from `hermes mcp list --json` |
| User's `projects/*` working tree conflicts | L | Never touch projects/*; only touch MCP configs |

## 7. Open Questions

- Q1: Should `.github/mcp.json` (Copilot) be the registry, or `.mcp/registry.json`? → **Decision: `.mcp/registry.json`** (Copilot expects its own format; registry is internal).
- Q2: What to do with the 3 disabled servers (atlassian, docs, postgres)? → **Decision: keep in registry, `enabled: false`**, allow easy re-enable.
