---
name: audit-skills-judge-fix
title: "Audit Skills Judge Fix"
description: 'Audit, judge, and fix skills in the Hermes library: inventory, dedupe, '
  remediation, consolidation, and final verification.'
version: 1.0.0
license: MIT
author: Hermes Agent
tags:
- audit
- skills
- remediation
- prompt-library-maintenance
trigger: /audit-skills-judge-fix
formatter: default
dependencies:
- skill:using-superpowers
- skill:user-communication-preferences
- skill:verification-before-completion
metadata:
  hermes:
    related_skills:
    - using-superpowers
    - user-communication-preferences
    - verification-before-completion
toolsets:
- file
- terminal
scripts: []
skills: []
plan: ''
---

# Audit Skills Judge Fix

## Context

- **Skills root:** `C:\Users\Alexa\AppData\Local\hermes\skills`
- **Progress artifact:** `docs/orchestrator-progress.md`
- **Verification artifact:** `docs/orchestrator-verification.md`

## Rules

1. Run phases in order; do not reorder.
2. Each phase must pass its gate before advancing.
3. If a referenced script/path is missing, report the exact missing path instead of fabricating work.

## Phases

Full phase instructions live in `templates/audit-skills-judge-fix/phases.md`.

| Order | Phase | Gate |
| --- | --- | --- |
| 1 | Skills Audit & Inventory | inventory artifacts exist and paths are valid |
| 2 | Categorize Skills | 0 empty categories; mapping saved |
| 3 | Deduplicate & Consolidate | duplicates resolved and report written |
| 4 | Judge Skills | all skills scored and results written |
| 5 | Remediate Skills | no skill remains below 80 |
| 6 | Consolidate Umbrella Skills | consolidation report written |
| 7 | Final Verification | final report shows pass with zero unresolved issues |

## Verification Checklist

- [ ] Phase 1 completed and verified
- [ ] Phase 2 completed and verified
- [ ] Phase 3 completed and verified
- [ ] Phase 4 completed and verified
- [ ] Phase 5 completed and verified
- [ ] Phase 6 completed and verified
- [ ] Phase 7 completed and verified
- [ ] Progress logged in `docs/orchestrator-progress.md`
- [ ] Final verification report in `docs/orchestrator-verification.md`
