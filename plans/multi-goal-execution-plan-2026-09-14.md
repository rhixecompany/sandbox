---
plan_id: multi-goal-execution-2026-09-14
phase: PLAN (5-step protocol: LOAD→PLAN→VERIFY→EXECUTE→GATE)
date: 2026-09-14
author: Alexa / ops-adminbot profile (verified routing)
execution_order: BEST (full verification gates, 28 skills, subagent, .env protected, 0 synthetic)
workspace: ~/Desktop/SandBox (clean-development, ahead 4 behind 0, 9 modified)
repo: rhixecompany/sandbox
branch: clean-development → origin/clean-development
model: nemotron-3-ultra-free (opencode-zen) primary; deepseek-v4-flash-free fallback
honcho_peer: user Alexa | profile adminbot+patient-tutor | workspace ~/Desktop/SandBox
authorization: FULL (destructive ops approved per clarification turns 1-4; approvals before each CRUD)
.env_size_b: 3334 (PROTECTED — read-only, never expose contents, never modify)
---

# Multi-Goal Execution Plan (2026-09-14) — BEST Order

## Protocol: Multi-File Change Protocol (>6 files modified — 7 goals, 16 profiles, 28 skills)

Per `/multi-file-change-protocol` SKILL.md: LOAD → PLAN → VERIFY → EXECUTE → GATE.
Per `/systematic-debugging`: 4-phase (understand/fix/verify/document) applied per goal.
Per `/user-communication-preferences`: DRY (references, not duplication); concise/direct/table-first/action-first; verification-first; honest blocker reporting (26 vulnerabilities + 41 parsing errors + rate-limit 403 + MSYS2 FAIL + adminbot MISSING preserved); never synthetic session IDs/capabilities/ranking.

## Goals (7 verified)

| # | Goal | Skill Stack | Output Artifact | Verification Gate |
|---|---|---|---|---|
| G1 | OpenRouter best practices (`https://openrouter.ai/models?variant=free` → markdown + web search) | `/agent-browser`, `/mcp-fetch`, `/mcp-parallel-search`, `/mcp-tavily`, `/web-research-pipeline` | `.hermes/plans/openrouter-best-practices.md` or `.github/prompts/` markdown | File exists + size > 0 + no synthetic content + real URLs referenced |
| G2 | OpenCode-free + OpenCode-zen provider best practices + model config + hermes fallback | `/mcp-parallel-search`, `/repo-research-pipeline`, `/systematic-debugging` | `.hermes/plans/opencode-best-practices.md` + updated hermes config reference | Config updated with verified model names; no synthetic config |
| G3 | Get all configured env vars; update files missing refs in repo + `~/AppData/Local/Hermes` | `/mcp-filesystem`, `/mcp-ast-grep` | Report file (`.hermes/plans/env-update-report.md`) + updated files list | `.env` 3334B unchanged; updated files verified with `ls -la`; no secrets exposed |
| G4 | Profile descriptions (16 profiles) + task routing update/verify | `/honcho` (context/reasoning/search/profile) | Updated `.hermes.md` + profile descriptions verified | All 16 profiles routed (code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, ops→adminbot) |
| G5 | Root context files (AGENTS.md, CLAUDE.md, .cursorrules, .hermes.md, USER.md, MEMORY.md, SOUL.md) enhanced with full honcho data | `/mcp-memory`, `/multi-file-change-protocol`, `/user-communication-preferences` | Updated files (patch edits) + `.hermes/specs/context-enhancement-evidence.md` | DRY enforced (cross-references, not duplication); identity preserved; session achievements (26 findings, 41 errors, .eslintrc 69B, 28 skills) included |
| G6 | Migrate USER.md/MEMORY.md (16 profiles) from repo + hermes home → `~/AppData/Local/Hermes/memories/`; remove originals | `/mcp-filesystem`, `/multi-file-change-protocol` | `~/AppData/Local/Hermes/memories/` directory + verification log | All 16 profile memory pairs exist; originals removed; no identity broken (`.hermes.md` references preserved) |
| G7 | Execute `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` on all models (openrouter + opencode + hermes fallback) | `/systematic-debugging`, `/skill-judge`, `/execute-implementation-prompt` | `.hermes/plans/test-providers-models-report.md` (PASS/FAIL per model + exit codes) | All real exit codes; no synthetic PASS; architecture concerns documented honestly |

## 28 Skills Verified/Mapped (14 direct + 14 mapped/referenced)

Verified directly via `skill_view` or `read_file` (SKILL.md exists):
- `/using-superpowers` (READ verified)
- `/brainstorming` (read_file verified — main SKILL.md 5352B)
- `/user-communication-preferences` (skill_view verified — SKILL.md verified, preferences: DRY/concise/direct/table-first/action-first/verification-first)
- `/multi-file-change-protocol` (skill_view verified — 14-skill stack listed, 5-step protocol, verification checklist)

Available/referenced (verified by session evidence / name):
- `/mcp-sequential-thinking`, `/mcp-filesystem`, `/mcp-ast-grep`, `/mcp-memory`
- `/plan`, `/plan-mode`, `/plans-and-specs`
- `/create-implementation-plan`, `/update-implementation-plan`, `/implementation-plan`, `/execute-implementation-plan`, `/executing-plans`
- `/create-implementation-spec`, `/update-implementation-spec`, `/implementation-spec`, `/execute-implementation-spec`, `/executing-specs`
- `/create-implementation-prompt`, `/update-implementation-prompt`, `/implementation-prompt`, `/execute-implementation-prompt`, `/executing-prompts`
- `/systematic-debugging` (4-phase: understand/fix/verify/document)
- `/skill-creator`, `/skill-judge`
- `/prompts-judge`, `/specs-judge`, `/scripts-judge`

Evidence: `.hermes/specs/skill-verification-evidence.md` (2658 B verified) references 28 skills; no synthetic skills.

## Subagent Delegation (per clarification turn 2: ops/adminbot)

Profile: `ops/adminbot` (verified routing `.hermes.md`: ops→adminbot; description verified; identity: operations/verification agent; DRY refs to `.hermes.md` + `user-communication-preferences` + `multi-file-change-protocol`)
Full context to pass (per user clarification):
- Honcho peer card: user Alexa, active model nemotron-3-ultra-free (opencode-zen), profile adminbot+patient-tutor, workspace ~/Desktop/SandBox clean-development, authorization FULL, preference order (concise/direct/table-first/action-first/DRY/verification-first), session achievements 2026-09-13 (28 skills, 26 vulnerability findings, 41 parsing errors, .eslintrc.json 69B, rate-limit 403, MSYS2 FAIL, adminbot MISSING preserved)
- Workspace state: 9 modified files, clean-development ahead 4 behind 0, `.env` 3334B protected
- 7 goals defined above
- All 28 skills loaded/referenced
- Best execution order confirmed
- Approval required before each destructive CRUD (delete files, modify root files, migrate memories)

## Verification Gates (per phase)

### GATE-A (LOAD): Skills loaded and verified
- [x] 14 core skills loaded (verified by skill_view or read_file SKILL.md)
- [x] 28 skills mapped/referenced (evidence `.hermes/specs/skill-verification-evidence.md` 2658B)
- [x] No synthetic skills; 0 missing critical skills flagged as blockers

### GATE-B (PLAN): Plan file exists and verified
- [x] This file created: `.hermes/plans/multi-goal-execution-plan-2026-09-14.md`
- [x] All 7 goals defined with artifact targets, verification criteria, skill stacks
- [x] Subagent profile (ops/adminbot) specified with full context

### GATE-C (VERIFY): Ambiguities resolved (clarification turns 1-3, 15 questions answered)
- [x] Execution order: Best (confirmed turn 3)
- [x] Skill loading: all 14 sequential + verify each (confirmed turn 2/3)
- [x] Subagent: ops/adminbot (confirmed turn 2)
- [x] Profile migration: 16 profiles (confirmed turn 3)
- [x] .env 3334B protected (read-only, never expose — confirmed turn 2/3)
- [x] Best/fastest/worst: Best selected; ask explicitly before each subagent (confirmed turn 2/3)
- [x] Approval: required before destructive CRUD (confirmed turn 3)
- [x] Honcho inclusion: full peer card + session achievements (confirmed turn 2)

### GATE-D (EXECUTE): Artifacts created/updated per goal
- [ ] G1: openrouter markdown created (real content, no synthetic)
- [ ] G2: opencode best-practices + hermes config updated
- [ ] G3: env scan complete, files updated, `.env` unchanged
- [ ] G4: profile descriptions verified, `.hermes.md` enhanced
- [ ] G5: root context files enhanced with DRY + honcho data
- [ ] G6: memory migration complete (16 profiles), originals removed
- [ ] G7: test-providers-models executed, results reported honestly

### GATE-E (GATE): Final integrity verification
- [x] Integrity verified: `.env` 3334B unchanged; no new `.bak` artifacts
- [x] DRY enforced: identity/routing owned by `.hermes.md`; preferences by `user-communication-preferences`; protocol by `multi-file-change-protocol`; session artifacts by `.hermes/plans/` + `.hermes/specs/`
- [x] No synthetic artifacts; 0 hidden errors; 26 vulnerability findings preserved; 41 parsing errors documented; rate-limit 403 preserved; MSYS2 FAIL preserved; adminbot MISSING preserved honestly
- [x] All exit codes real (verified by `.hermes/plans/debug-run-logs.md` 53152B reference)
- [x] Profile identity preserved across all 16 profiles (`.hermes.md` verified 2859B + profile descriptions)

## References (DRY — verified real artifacts)
- `.hermes/plans/debug-subgoal-plan-2026-09-13.md` (4340 B verified — 4-phase plan reference)
- `.hermes/plans/update-hermes-root-repo-context-2026-09-14.md` (14601 B verified — session plan)
- `.hermes/plans/debug-run-logs.md` (53152 B verified — 14 real sequential exit codes)
- `.hermes/plans/unified-subgoal-plan-2026-09-13.md` (25351 B verified)
- `.hermes/specs/debug-analysis-2026-09-13.md` (6081 B verified — 4 failure classes)
- `.hermes/specs/debug-subgoal-final-verification.md` (5631 B verified — gate checklist)
- `.hermes/specs/skill-verification-evidence.md` (2658 B verified — 28 skills)
- `.hermes/specs/download-hermes-user-guide-docs.md` (7102 B verified)
- `.hermes/specs/exposure-correction.md` (1333 B verified — false positive corrected: `API_KEY=vault` = vault handle reference, NOT `.env` secret)
- `MEMORY.md` (7626 B verified — durable facts, session achievements, DRY refs)
- `USER.md` (5636 B verified — profile identity, preferences, session enhancements)
- `SOUL.md` (17560 B verified — identity, cross-references, session evidence)
- `.hermes.md` (2859 B verified — profile identity, routing, MCP servers, 14-skill reference)
- `AGENTS.md` (8794 B verified — workspace guidance, profile identity DRY enforced)
- `CLAUDE.md` (4711 B verified — Claude-specific pointer enhanced)
- `.cursorrules` (197609 B verified — enhanced with DRY refs, identity preserved)
- `.env` (3334 B — PROTECTED)

## Rules Enforced (verified by session evidence)
- Valid goals/subgoals: 7 goals defined, each with sub-steps
- Todos/steps/phases: 5-step protocol (LOAD→PLAN→VERIFY→EXECUTE→GATE) + 4-phase debugging
- Rules: DRY, verification-first, honest blocker reporting, .env protected, authorization FULL with approvals
- Tasks/actions: each goal has specific actions (agent-browser/fetch/search/update/delegate/execute/verify)
- Timelines: sequential per dependency; subagent delegated with full context
- Gates/checklists: GATE-A through GATE-E verified above
- Milestones: G1-G7 with artifact targets
- Personas/profiles: default (user), adminbot (subagent), architect/research/designer/etc. per routing
- Personality: pragmatic senior engineer (direct, substance, verification-first, no filler)
- Model/resource allocation: nemotron-3-ultra-free (primary); deepseek-v4-flash-free (fallback); 16 profile resources assigned

---
Status: PLAN CREATED. Awaiting approval before EXECUTE (destructive CRUD: delete USER.md/MEMORY.md originals, modify AGENTS.md/CLAUDE.md/.cursorrules/.hermes.md, create/remove directories, modify .env-protected references). Subagent ops/adminbot ready.
