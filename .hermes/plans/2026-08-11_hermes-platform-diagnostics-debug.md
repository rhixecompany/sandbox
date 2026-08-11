---
name: hermes-platform-diagnostics-debug
title: "Hermes Platform Diagnostics & Debug Plan"
author: Alexa
version: 1.0.0
status: in_progress
created: 2026-08-11
tags: [hermes, diagnostics, debugging, plan]
---

# Hermes Platform Diagnostics & Debug Plan

## Goal
Run the full Hermes diagnostic chain in the background (no timeout), then
systematically fix every bug, issue, warning, and error surfaced — root cause
first, per `systematic-debugging`.

## Context / Assumptions
- Host: Windows 11, git-bash/MSYS terminal, cwd `C:\Users\Alexa\Desktop\SandBox`
- Profile: default (deepseek-v4-flash-free / opencode-zen)
- Known prior findings (2026-07-24→08-08): skills hub Windows hash bug
  (`hermes skills update` reports Updated but `skills check` re-flags),
  hook wire-payload shapes fixed, MCP server restorations done.
- `&&` chain means short-circuit on failure: if a command exits non-zero, the
  remaining commands stop. If that happens, run the remainder individually.

## Phase 1 — Background Diagnostic Collection (in progress)
Execute verbatim, background, no timeout, output teed to
`.hermes/diagnostics-2026-08-11.log`:

```bash
hermes doctor && hermes doctor --fix && hermes security audit && hermes status && hermes insights && hermes skills audit && hermes skills check && hermes skills update && hermes logs list && hermes logs errors && hermes logs desktop && hermes logs gateway && hermes logs gui && hermes logs agent
```

## Phase 2 — Triage Findings
Categorize every finding from the log:
- **Actionable** — mismatched configs, dead paths, missing credentials, real
  bugs → fix.
- **Transient** — DNS blips, startup races, retried failures → document, no fix.
- **Cosmetic** — asyncio cleanup warnings, optional tool not-installed notices →
  document, no fix unless trivially safe.

Produce a findings table: severity, category, evidence, proposed action.

## Phase 3 — Systematic Debugging (only after Phase 1/2 complete)
For each actionable issue, follow the 4-phase method:
1. **Root cause** — read the error fully, reproduce, check recent changes,
   gather evidence (logs, state, config).
2. **Pattern analysis** — compare against working examples.
3. **Hypothesis & minimal test** — one variable at a time.
4. **Implement fix** — regression-verify before/after; Rule of Three; question
   architecture after 3 failed fixes.

Rules:
- Config changes via `hermes config set`, never direct YAML edits.
- Prefer root-cause docs/config checks over editing
  `~/AppData/Local/hermes/...` plugin files.
- No `rm -rf` / destructive ops without explicit approval.

## Phase 4 — Re-Verify
- `hermes doctor` → all pass, 0 advisories
- `hermes security audit` → 0 advisories
- `hermes skills check` → no unexpected `update_available` re-flags
- Log chains: no new actionable errors
- Update this plan: mark tasks `[x]`, record lessons learned.

## Files Likely to Change
- `~/AppData/Local/hermes/config.yaml` (via `hermes config set`)
- `~/AppData/Local/hermes/tools/skills_hub.py` / `skills_guard.py` (if skills
  hash bug still live)
- `~/AppData/Local/hermes/hooks/*` (only with verified reproduction)
- `.hermes/plans/*` + `SESSION_REPORT.md` (plan/report artifacts)

## Validation
- Final: `hermes doctor` green + findings table closed + re-run of any fixed
  command shows the error gone.

## Risks / Tradeoffs
- `hermes doctor --fix` and `hermes skills update` are mutating: they may
  rewrite config/skills. Review diffs before/after.
- Background `&&` short-circuit can truncate the diagnostic capture — monitor
  the process and complete any skipped commands manually.
