---
name: mcp-audit
title: "MCP Server Audit & Sync"
description: "Use when configuring, debugging, fixing, or syncing MCP servers across opencode/codex/copilot/vscode/hermes. Runs audit + sync + report loop against a single-source-of-truth registry."
trigger: /mcp-audit
agent: adminbot
model: minimax/minimax-m3:free
tools: [terminal, read_file, write_file, patch, search_files, skill_view]
metadata:
  hermes:
    tags: [mcp, audit, sync, devops]
---
## Table of Contents

## Goal

## Context

## Phases


# /mcp-audit — Run MCP Server Audit + Sync

## When to Invoke

- "Sync MCP configs"
- "Audit MCP servers"
- "Fix MCP server not connecting"
- "Show me which MCP servers work"
- "Add a new MCP server"

## Workflow

The agent must execute these phases in order, with verification gates between each. Do not skip phases.

### Phase 1: Discover

```bash
ls -la .mcp/registry.json opencode.json .codex/mcp.json .copilot/mcp.json .vscode/mcp.json
hermes mcp list
```

Verify `.mcp/registry.json` exists. If not, copy from skill template at
`~/AppData/Local/hermes/skills/mcp/mcp-audit-orchestrator/templates/registry.json`.

### Phase 2: Sync (only if registry changed)

```bash
python scripts/mcp_sync.py --registry .mcp/registry.json --dry-run   # preview
python scripts/mcp_sync.py --registry .mcp/registry.json            # apply
```

Targets updated: `opencode.json`, `.codex/mcp.json`, `.copilot/mcp.json`, `.vscode/mcp.json`.

Hermes config.yaml is NOT auto-edited. For Hermes, use `hermes mcp add/remove` or pass `--hermes-diff` to see what would change.

### Phase 3: Audit

```bash
python scripts/mcp_audit.py --registry .mcp/registry.json
```

Output: `.hermes/plans/mcp-audit-<date>/audit-report.{json,md}`

Parse the report. Any **FAIL** status means a real problem; **WARN** is usually benign (DNS or env).

### Phase 4: Hermes health

```bash
hermes doctor
hermes mcp list | wc -l   # must match registry enabled count
```

### Phase 5: Report

Summarize in 5-10 lines:
- Total servers
- PASS / WARN / FAIL / SKIP counts
- Any FAILs that need manual fix
- Any new servers added to disk configs
- Any servers that need `hermes mcp add` to register with Hermes

## Hard Rules

1. **Never** edit `opencode.json` / `.codex/mcp.json` / `.copilot/mcp.json` / `.vscode/mcp.json` directly. Edit `.mcp/registry.json` then sync.
2. **Never** edit `~/AppData/Local/hermes/config.yaml` directly. Use `hermes mcp add/remove`.
3. **Never** commit changes to disk configs without first running `mcp_sync.py` — they should be reproducible.
4. **Never** mark a task complete if `mcp_audit.py` returns FAIL.
5. **Never** delete a server from the registry without first confirming with the user.

## Reference

- Skill: `mcp-audit-orchestrator` (load with `skill_view name="mcp\mcp-audit-orchestrator"`)
- Plan: `.hermes/plans/mcp-audit-<date>/`
- Spec: `.hermes/plans/mcp-audit-<date>/SPEC.md`

## Verification Checklist

- [ ] `mcp_audit.py` exits 0 (no FAIL)
- [ ] `mcp_sync.py` reports 4 targets synced
- [ ] `hermes mcp list` shows same enabled count as registry
- [ ] `hermes doctor` shows no new MCP warnings vs baseline
- [ ] All 4 disk configs pass `json.load()` (valid JSON)
- [ ] Report written to `.hermes/plans/mcp-audit-*/`
- [ ] SESSION_REPORT.md updated
