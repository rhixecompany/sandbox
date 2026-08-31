---
name: hermes-diagnostic
description: Run a full Hermes Agent diagnostic sweep — doctor, security, status, insights, logs (list/errors/desktop/gateway/gui/agent), and bun run check. Produces a single report.
trigger: /hermes-diagnostic
version: 1.0.0
author: Hermes Agent
license: MIT
tags: 
metadata: 
hermes: 
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
title: Hermes Diagnostic Sweep
---

# Hermes Diagnostic Sweep

Run a comprehensive health check on Hermes Agent.

## Steps

1. **Run the diagnostic harness**:
   ```bash
   python scripts/hermes_diagnostic.py --skip-fix --timeout 60
   ```
   (Skip `--skip-fix` to also run `hermes doctor --fix` — only after committing current state.)

2. **Check the report** at `.hermes/plans/hermes-diagnostic-YYYY-MM-DD_HHMMSS/report.md`:
   - 12 commands total (11 if no `package.json` exists in SandBox)
   - Each shows: exit code, elapsed, OK/FAIL
   - FAIL section shows stderr tail

3. **For each FAIL**, decide:
   - `doctor FAIL` — `hermes doctor --fix` (after `git add` of current state)
   - `security FAIL` — `npm audit fix` or update dep
   - `status WARN` — add missing API key via `hermes auth add <provider>`
   - `logs-X FAIL` — read sample errors, file bug or document
   - `bun-run-check FAIL` — run `bun run check` directly

4. **Re-run** to confirm green:
   ```bash
   python scripts/hermes_diagnostic.py --skip-fix --timeout 60
   ```

5. **Pair with log analysis** for deeper investigation:
   ```bash
   python scripts/log_analysis.py
   ```

## Output

- `report.json` — machine-readable per-command results
- `report.md` — human-readable summary table + failures

## Verification

- [ ] All 12 commands run (or 11 without package.json)
- [ ] FAILs reviewed
- [ ] No new warnings introduced

## See also

## Goal
Run a full Hermes Agent diagnostic sweep — doctor, security, status, insights, logs (list/errors/desktop/gateway/gui/agent), and bun run check. Produces a single report.

## Context

## Workflow

<content>

<content>

<content>

- `~/AppData/Local/hermes/skills/devops/hermes-diagnostic-repair/SKILL.md` (full skill)
- `~/AppData/Local/hermes/skills/devops/log-analysis-and-triage/SKILL.md`
```
# Prompt template
Execute the workflow defined in this file.
```
