---
goal: "Design-MD feature scope execution + skills overhaul (98+ score) for combined init"
version: 1.0
date_created: 2026-09-19
last_updated: 2026-09-19
owner: Alexa
status: In progress
---
# Plan — design-md-20260919-212743

## 1. Requirements & Constraints
- Design-MD feature scope (`docs/scope/design-md.md`) completed per `scope` skill.
- Skills overhaul: generate `local-skills.txt` (done: 1128 lines, 1060 unique, 31 duplicates, 0 uncategorized after inspection — 2 skills `agentic-workflow` and `weather-plugin` have empty categories and must be assigned or deleted per gate).
- Skill-judge audit: all categorized skills ≥98 (current workspace categories verified: agent-development: 41, creative: 75, development: 445, devops: 146, mcp: 62, etc. — 34 categories total).
- Integrity: `.env` 30381 B unchanged; identity preserved; 0 synthetic artifacts; blockers documented honestly.

## 2. Implementation Steps (Tracer Bullet)
1. Confirm destructive deletion list (agentic-workflow, weather-plugin, 31 duplicate candidates — show to user via clarify gate).
2. Confirm categories for skill-judge audit (use workspace categories from `local-skills.txt`).
3. Execute skills migration/deletion (add categories, delete unconfirmed duplicates).
4. Create design-md artifacts (spec, plan, prompts, STATUS).
5. Run skill-judge audit; document scores.
6. Update STATUS.md (all artifacts + skills) to Completed.

## 3. Verification Gates
- [ ] Confirm destructive deletion list.
- [ ] Confirm categories.
- [ ] Confirm design-md artifacts present.
- [ ] Skill-judge audit executed (score ≥98).
- [ ] STATUS.md updated.
- [ ] Integrity verified (`.env` unchanged, identity preserved, no synthetic artifacts).

## 4. Blockers / Integrity (honest)
- `default` profile MISSING; `alexa-alias` MISSING; `adminbot` MISSING (honest — preserved from session 20260919_210743).
- MSYS2 FAIL; rate-limit 403; vision REJECTS; 26 vulnerability findings; 41 parsing errors.
- `web-research-628` remaining batches; 39 paste tasks (`.hermes/results/pastes-triage-2026-09-19.md`).
- No `.bak` artifacts; no commit/push.
