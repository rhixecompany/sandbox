---
title: "Hermes Diagnostic + Log Analysis"
description: "Run the full Hermes platform diagnostic battery plus log analysis. Emits report.md, report.json, and triage recommendations. Use for post-config-change verification, weekly health checks, or pre-deployment pre-flight."
mode: single
---

# Hermes Diagnostic + Log Analysis

## When to Use

- After any config / hook / plugin / MCP / model change
- Weekly health review
- Pre-deployment pre-flight
- Post-incident root-cause sweep
- When `hermes doctor` or `bun run check` shows warnings

## What it does

Runs the full diagnostic battery (12 commands) and the log analyzer (6 streams, 24h lookback). Emits a single report pair per run.

## Steps

### 1. Verify prerequisites

```bash
which hermes bun python
hermes doctor --version
```

All three must resolve. If `bun` is missing, run with `--no-bun`.

### 2. Run diagnostic

```bash
cd ~/Desktop/SandBox
python scripts/hermes_diagnostic.py
```

Output: `.hermes/plans/diagnostic-<ts>/{report.md, report.json, failures.md, sweep.log}`

Read `report.md` first. If `failures.md` is non-empty, jump to repair.

### 3. Run log analysis

```bash
python scripts/log_analysis.py --since 24
```

Output: `.hermes/plans/log-analysis-<ts>/{report.md, report.json, clusters.md, top-errors.md}`

Read `report.md` cluster counts and recommendations. Cross-reference with diagnostic failures.

### 4. Repair (if needed)

For each finding in `failures.md` + each non-empty cluster in log analysis:
- `auth` cluster > 0 → `hermes auth list`; check for 401/403 → rotate stale keys
- `disk` cluster > 0 → run disk cleanup before any further writes
- `network` cluster > 0 → identify endpoint from `clusters.md` → `Test-NetConnection`
- `timeout` cluster > 0 → add `--timeout` flags or break commands into smaller units
- `error` cluster > 0 → check `top-errors.md` for repeating patterns

### 5. Re-verify

Re-run both scripts. On a healthy platform:
- `hermes_diagnostic.py` exits 0
- `log_analysis.py` shows empty `auth`/`disk`/`network` clusters (warnings/errors may exist as baseline)

### 6. Commit results (optional)

```bash
git add .hermes/plans/diagnostic-<ts>/ .hermes/plans/log-analysis-<ts>/
git commit -m "chore: weekly hermes health sweep (diagnostic + logs)"
```

## Verification

- [ ] `python scripts/hermes_diagnostic.py` exits 0
- [ ] `python scripts/log_analysis.py` exits 0
- [ ] `report.md` files exist and are non-empty
- [ ] No NEW failures introduced (compare to previous week's sweep)
- [ ] All repair actions documented in commit message body

## Pitfalls

- Don't run with `--fix` until you've reviewed the dry-run output
- `hermes doctor --fix` modifies config.yaml — review diffs
- Some warnings are pre-existing baseline; compare to last green run
- Schedule weekly, not daily, to avoid alert fatigue
- Log analysis window: 24h is default; 168h for weekly trend
