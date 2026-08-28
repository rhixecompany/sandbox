---
title: MCP Audit Implementation Plan
generated: 2026-08-28
profile: adminbot
model: minimax/minimax-m3:free
status: ready → executing
---

# PLAN — MCP Audit, Registry & Sync

## Sequencing (strict; "only then" is a hard constraint)

```
[1] Write SPEC.md (this plan's parent doc)
    ↓ only then
[2] Create .mcp/registry.json (single source of truth, 25 servers)
    ↓ only then
[3] Fix opencode.json script paths (3 servers: python-quality, tooling-lint, tooling-config)
    ↓ only then
[4] Add .omo/ to .prettierignore (fix bun run check)
    ↓ only then
[5] Update hermes default model (config set, not yaml edit)
    ↓ only then
[6] Write scripts/mcp_audit.py (test every server in registry)
    ↓ only then
[7] Write scripts/mcp_sync.py (sync registry → 4 disk configs)
    ↓ only then
[8] Run audit → generate report → review
    ↓ only then
[9] Run sync → verify 4 configs match registry
    ↓ only then
[10] Run hermes doctor + bun run check (verify gates)
    ↓ only then
[11] Create skill mcp-audit-orchestrator (SKILL.md + references + scripts)
    ↓ only then
[12] Create .github/prompts/mcp-audit.prompt.md
    ↓ only then
[13] Update SESSION_REPORT.md with all results
```

## Task Breakdown

### T1 — Registry (`.mcp/registry.json`)

- Source of truth: `hermes mcp list` (25 servers, 22 enabled + 3 disabled)
- Include: name, type, command/args, url, env, enabled, description, tags
- Validate with `python -c "import json; json.load(open('.mcp/registry.json'))"`
- Authoring: 1 file, ~150 lines

### T2 — opencode.json script-path fix

3 servers in `opencode.json` reference wrong filenames:

| Server | Wrong | Right |
|--------|-------|-------|
| python-quality | `python_quality_server.py` | `python_quality_mcp_server.py` |
| tooling-lint | `tooling_lint_server.py` | `tooling_lint_mcp_server.py` |
| tooling-config | `tooling_config_server.py` | `tooling_config_mcp_server.py` |

After fix → `hermes mcp test` should connect to all 3.

### T3 — .prettierignore — add `.omo/`

```
.omo/
.omo/**
```

### T4 — Hermes default model

Current default: `nvidia/nemotron-3-ultra-550b-a55b:free` → 404 on OpenRouter.
Candidates verified working this session:
- `minimax/minimax-m3:free` — what just worked (current model)
- `deepseek-v4-flash-free` — alternative

Decision: Update default to `minimax/minimax-m3:free` via `hermes config set`.

### T5 — `scripts/mcp_audit.py`

- Loads `.mcp/registry.json`
- For each stdio: resolves `${env:...}`, checks `command` path, `bunx --version` smoke
- For each http/sse: HEAD/GET, accepts 2xx/4xx
- Emits JSON + Markdown report to `.hermes/plans/mcp-audit-2026-08-28/audit-report.{json,md}`

### T6 — `scripts/mcp_sync.py`

- Reads registry
- Writes:
  - `opencode.json` (preserves non-mcp keys: `model`, `plugin`, `small_model`)
  - `.codex/mcp.json` (mcpServers)
  - `.copilot/mcp.json` (pretty-printed mcpServers)
  - `.vscode/mcp.json` (servers + inputs)
- For hermes config.yaml: NOT auto-edited (user must `hermes mcp add ...` or accept drift)

### T7 — Skill `mcp-audit-orchestrator`

Path: `~/AppData/Local/hermes/skills/mcp/mcp-audit-orchestrator/`
- SKILL.md ≤250 lines: workflow, when-to-use, verification checklist
- references/registry-spec.md
- references/sync-targets.md
- references/audit-results.md
- scripts/mcp_audit.py (symlink or copy)
- scripts/mcp_sync.py (symlink or copy)
- templates/registry.json
- templates/server-entry.json

### T8 — Prompt `.github/prompts/mcp-audit.prompt.md`

Single-shot agent prompt that, when invoked, runs the full audit+sync+report loop.

### T9 — Verification sweep

```
hermes doctor           # baseline + after
hermes mcp list         # enabled count stable
bun run check           # lint + format + markdownlint + spellcheck
python scripts/mcp_audit.py
python scripts/mcp_sync.py --dry-run   # should be no-op
```

### T10 — SESSION_REPORT.md update

Standard fields: session_id, timestamp, profile=adminbot, model=minimax/minimax-m3:free, work done, files changed, verification results.

## Effort Estimate

| Task | Est |
|------|-----|
| T1 registry | 5 min |
| T2 opencode patch | 2 min |
| T3 prettierignore | 1 min |
| T4 hermes model | 2 min |
| T5 audit script | 10 min |
| T6 sync script | 10 min |
| T7 skill | 8 min |
| T8 prompt | 3 min |
| T9 verify | 5 min |
| T10 report | 2 min |
| **Total** | ~50 min |

## Stop Conditions

- **Continue until** all of V1–V8 pass
- **Stop & ask** if any hermes CLI command fails with a non-recoverable error
- **Stop & document** if a warning is non-fixable in this session (e.g. Honcho credits)
