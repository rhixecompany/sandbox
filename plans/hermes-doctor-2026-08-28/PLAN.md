---
title: "Hermes Doctor Diagnostic Pipeline — PLAN"
description: "Sequential plan for the diagnostic pipeline build (script + skill + prompt + plan trio + verification gates)."
date: 2026-08-28
author: Hermes Agent
status: completed
---

# Hermes Doctor Diagnostic Pipeline — PLAN

## Strategy

Single-session build. The script is small (≤300 lines) and the patterns already exist in `log-analysis-and-triage`. No subagents needed.

## Phases

### P1 — Discovery (no edits)

- Read `devops/hermes-diagnostic-repair` and `devops/log-analysis-and-triage` for pattern catalog
- Confirm battery commands resolve: `hermes doctor`, `hermes security audit`, `hermes logs *`, `bun run check`
- Confirm pre-state: `hermes doctor` → "All checks passed", `hermes security audit` → "No known vulnerabilities", `bun run check` → 0 errors

### P2 — Write script (scripts/hermes_doctor.py)

- Stdlib only
- COMMANDS_FULL list with (label, command, classification_hint)
- `run_one()` — subprocess wrapper, capture exit/stdout/stderr/duration
- `classify_finding()` — regex-based, returns one of 5 buckets
- `build_summary()` — aggregate counts + actionable findings
- `render_markdown()` — human-readable table
- `main()` — argparse, dispatch, exit code logic
- Output: `.hermes/plans/diagnostic-<date>/report.{json,md}`

### P3 — Write skill (~/AppData/Local/hermes/skills/devops/hermes-doctor-pipeline/SKILL.md)

- Trigger: "run hermes diagnostic", "find all hermes bugs", pre-deploy
- Include: battery table, classification taxonomy, quick-start, exit codes, pattern catalog, verification gates, pitfalls
- ≤250 lines (target ≤200)

### P4 — Write prompt (.github/prompts/hermes-doctor.prompt.md)

- Frontmatter: name, title, description, version, author, tags
- Body: when to use, 4-step workflow, flags, pitfalls, verification, see also

### P5 — Write plan trio (.hermes/plans/hermes-doctor-2026-08-28/{SPEC,PLAN,implementation-plan}.md)

- SPEC.md — full design + schema + verification gates
- PLAN.md — this file
- implementation-plan.md — task list with line counts

### P6 — Verify (8 gates)

- V1 `python -m py_compile scripts/hermes_doctor.py`
- V2 Full battery: `python scripts/hermes_doctor.py --no-bun` exits 0
- V3 report.json valid JSON, schema_version=1
- V4 report.md has summary + per-command tables
- V5 `bun run lint` clean
- V6 skill auto-discovered: `hermes skills list | grep hermes-doctor`
- V7 prompt file exists
- V8 all 12 commands run in full battery

## Strict-Sequential Constraints

- P1 → P2 → P3 → P4 → P5 → P6, no skipping
- P6 cannot start until P2-P5 artifacts all exist
- Any V-fail: fix root cause (don't suppress) and re-run full battery

## Estimated Time

- P1: 30s (read skills)
- P2: 5 min (script)
- P3: 3 min (skill)
- P4: 2 min (prompt)
- P5: 3 min (3 plan docs)
- P6: 90s (full battery = 12 commands × ~5-30s each)
- **Total: ~15 min**

## Risk

- Low. All commands are read-only. Script is stdlib-only. Pattern catalog is borrowed from existing skills.

## Rollback

- `git checkout HEAD -- scripts/hermes_doctor.py`
- `rm -rf ~/AppData/Local/hermes/skills/devops/hermes-doctor-pipeline/`
- `rm .github/prompts/hermes-doctor.prompt.md`
- `rm -rf .hermes/plans/hermes-doctor-2026-08-28/`
