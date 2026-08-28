---
title: MCP Audit — Implementation Plan
plan: .hermes/plans/mcp-audit-2026-08-28/PLAN.md
spec: .hermes/plans/mcp-audit-2026-08-28/SPEC.md
status: ready
---

# Implementation Plan — Step by Step

> **Strict sequential.** Complete T(N) and verify before T(N+1).

## T1 · Create registry — `.mcp/registry.json`

**Inputs:** `hermes mcp list` (25 servers)
**Output:** `C:\Users\Alexa\Desktop\SandBox\.mcp\registry.json`
**Verify:** `python -c "import json; json.load(open('.mcp/registry.json'))"` exits 0

## T2 · Patch opencode.json script paths

**File:** `opencode.json`
**Diffs:**
- `python-quality.command` → fix filename to `python_quality_mcp_server.py`
- `tooling-lint.command` → fix filename to `tooling_lint_mcp_server.py`
- `tooling-config.command` → fix filename to `tooling_config_mcp_server.py`

**Verify:** `grep -c "_server.py" opencode.json` = 0 (none should remain after fix)

## T3 · Add `.omo/` to `.prettierignore`

**File:** `.prettierignore`
**Add:** `.omo/` and `.omo/**`
**Verify:** `bun run format:check` no longer complains about `.omo/run-continuation/`

## T4 · Update hermes default model

**Command:** `hermes config set model.default minimax/minimax-m3:free`
**Verify:** `hermes config show` shows new default in Model section

## T5 · Write `scripts/mcp_audit.py`

**Path:** `C:\Users\Alexa\Desktop\SandBox\scripts\mcp_audit.py`
**Args:** `--registry .mcp/registry.json --output .hermes/plans/mcp-audit-2026-08-28/audit-report.{json,md}`
**Verify:** Exits 0; report has 25 rows; counts sum to total

## T6 · Write `scripts/mcp_sync.py`

**Path:** `C:\Users\Alexa\Desktop\SandBox\scripts\mcp_sync.py`
**Args:** `--registry .mcp/registry.json [--dry-run]`
**Verify (dry-run):** Reports no changes needed (clean baseline) or lists intended edits

## T7 · Write skill `mcp-audit-orchestrator`

**Path:** `C:\Users\Alexa\AppData\Local\hermes\skills\mcp\mcp-audit-orchestrator\`
**Files:** SKILL.md, references/*.md, scripts/*, templates/*
**Verify:** `skill_view(name='mcp\mcp-audit-orchestrator')` returns full content

## T8 · Write prompt `.github/prompts/mcp-audit.prompt.md`

**Path:** `C:\Users\Alexa\Desktop\SandBox\.github\prompts\mcp-audit.prompt.md`
**Verify:** File exists, contains sections: frontmatter, role, workflow, verification

## T9 · Final verification sweep

```
python scripts/mcp_audit.py
python scripts/mcp_sync.py --dry-run
hermes doctor
hermes mcp list | wc -l       # should be 25
bun run check                 # lint + format + md + spell
```

Pass criteria: all 0 exit, no NEW warnings vs baseline.

## T10 · Update SESSION_REPORT.md

Standard fields appended; old content preserved; this session appended as new section.
