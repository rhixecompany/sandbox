---
title: "Hermes Doctor Diagnostic Pipeline — Implementation Plan"
description: "Step-by-step task list for the diagnostic pipeline build."
date: 2026-08-28
author: Hermes Agent
status: completed
---

# Implementation Plan

| # | Task | File | Status |
| - | ---- | ---- | ------ |
| 1 | Read existing skills for pattern catalog | `devops/hermes-diagnostic-repair`, `devops/log-analysis-and-triage` | ✓ |
| 2 | Confirm pre-state: doctor/security/bun all green | n/a (terminal) | ✓ |
| 3 | Write `scripts/hermes_doctor.py` (~330 lines, stdlib only) | `scripts/hermes_doctor.py` | ✓ |
| 4 | Test --doctor-only --no-bun run (5 commands) | n/a (terminal) | ✓ |
| 5 | Fix Pyright type errors (dict narrowing in render_markdown) | `scripts/hermes_doctor.py` | ✓ |
| 6 | Re-run after type fix | n/a (terminal) | ✓ |
| 7 | Write skill `hermes-doctor-pipeline` | `~/AppData/Local/hermes/skills/devops/hermes-doctor-pipeline/SKILL.md` | ✓ |
| 8 | Write prompt `hermes-doctor` | `.github/prompts/hermes-doctor.prompt.md` | ✓ |
| 9 | Write SPEC.md | `.hermes/plans/hermes-doctor-2026-08-28/SPEC.md` | ✓ |
| 10 | Write PLAN.md | `.hermes/plans/hermes-doctor-2026-08-28/PLAN.md` | ✓ |
| 11 | Write implementation-plan.md (this file) | `.hermes/plans/hermes-doctor-2026-08-28/implementation-plan.md` | ✓ |
| 12 | V1: `python -m py_compile scripts/hermes_doctor.py` | n/a | ✓ |
| 13 | V2: full battery run (12 commands) | n/a | pending |
| 14 | V3: report.json valid + schema=1 | n/a | pending |
| 15 | V4: report.md tables present | n/a | pending |
| 16 | V5: `bun run lint` clean | n/a | pending |
| 17 | V6: skill auto-discovered | n/a | pending |
| 18 | V7: prompt file exists | n/a | pending |
| 19 | V8: all 12 commands ran | n/a | pending |

## Verification Commands

```bash
# V1
python -m py_compile scripts/hermes_doctor.py

# V2 (full battery — ~90s)
python scripts/hermes_doctor.py --no-bun

# V3
python -c "import json; d=json.load(open('.hermes/plans/diagnostic-2026-08-28/report.json')); print(d['schema_version'])"

# V4
grep -c "## Summary" .hermes/plans/diagnostic-2026-08-28/report.md
grep -c "## Per-command results" .hermes/plans/diagnostic-2026-08-28/report.md

# V5
./node_modules/.bin/eslint scripts/hermes_doctor.py  # if eslint config covers .py, skip
python -m py_compile scripts/hermes_doctor.py  # already V1

# V6
hermes skills list | grep hermes-doctor

# V7
test -f .github/prompts/hermes-doctor.prompt.md

# V8
python -c "import json; d=json.load(open('.hermes/plans/diagnostic-2026-08-28/report.json')); print(len(d['results']))"
```

## Definition of Done

- [ ] All 19 tasks completed
- [ ] All 8 verification gates PASS
- [ ] No new lint errors introduced
- [ ] Script re-runnable (idempotent)
- [ ] Plan trio committed to git
