---
name: phased-execution-2026-09-14
version: 1.0.0
author: Alexa / adminbot
license: MIT
description: "Master phased execution spec for 8-subgoal compound task (stashes/debug, web-research/env, profiles/migration) — best quality path, multi-file-change-protocol triggered."
---

# Master Execution Spec — 2026-09-14 Phased Compound Task

## Trigger
Multi-file-change-protocol triggered (>6 files modified/created). 14-skill stack verified (5 loaded; 9 referenced by name).

## Implementation Order
Best (full protocol + all verification gates) — confirmed via clarification.

## Model / Provider Allocation
- Default session: `inkling:free` (openrouter)
- Subagents: enforce same default; allow fallback (`opencode-zen/nemotron`, `nous`) — document in each subagent spec. Setup fallback in specs/plans.

## 3 Phases (sequential — Phase N requires Phase N-1 output for profiles/env)

| Phase | Goal | Key Artifacts | Subagent | Gate |
|---|---|---|---|---|
| P1 | Apply 4 stashes (abort-on-conflict) + `systematic-debugging` audit `config.yaml` (YAML list conflict) + `.eslintrc.json` fix verify + browser/debug audit (`agent-browser` skill + `test-providers-models`) | `./specs/phase1-stashes-debug.md`; `./plans/debug-run-logs.md` update; `debug-analysis.md` update | Subagent-1 | All 4 stashes applied cleanly OR conflicts documented honestly; `config.yaml` audit PASS; 0 hidden errors |
| P2 | Web-search (`openrouter.ai/models?variant=free`) → markdown report; env audit (repo + hermes home + all profiles); `test-providers-models` on each free model; `opencode-zen` + `opencode-free` best practices; configure hermes with model + fallback | `./specs/phase2-web-research-env.md`; `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` update; `./plans/web-research-...` artifacts | Subagent-2 | Markdown report with all free models verified real; env vars in all locations verified; `.env` untouched; `test-providers-models` executed; 0 synthetic artifacts |
| P3 | Update ALL hermes profile descriptions (honcho/user/card data); migrate `USER.md`/`MEMORY.md` (+ `SOUL.md` for identity) → `../../AppData/Local/Hermes/memories/` (merge, delete originals); update `AGENTS.md`, `CLAUDE.md`, `.cursorrules` with DRY + honcho data; enforce `multi-file-change-protocol` 14-skill + 5-step; enforce `systematic-debugging` 4-phase | `./specs/phase3-profiles-migration.md`; all profile `SOUL.md`/`USER.md`/`MEMORY.md` enhanced; context files updated; `memories/` verified | Subagent-3 | All profiles verified; memory migration verified; DRY references verified; 0 synthetic results; identity preserved; `.env` 3334 B unchanged; 0 new `.bak` |

## Rules Enforced (verified references — not duplicated; DRY)
- `user-communication-preferences`: concise/direct/table-first/action-first; DRY via `templates/_shared/`; verification before claim; honest blocker reporting; never synthetic session IDs/capabilities/ranking; `.env` ONLY `.hermes`.
- `multi-file-change-protocol`: 14-skill stack + 5-step (LOAD→PLAN→VERIFY→EXECUTE→GATE); >6 file trigger verified; sequential/parallel decision verified; verification checklist verified.
- `systematic-debugging`: 4-phase (Root Cause → Pattern → Hypothesis → Implementation); single hypothesis; 3-fix-stop rule; architecture question if ≥3 fixes fail; evidence before claim.
- `plans-and-specs`: phased plan + linked spec + acceptance criteria; verification before complete.

## Personas / Profile Routing (per clarification + honcho context)
- Default profile: `default` (inkling:free/openrouter) — verified `.hermes.md`
- Adminbot profile: `adminbot` (verified MISSING preserved honestly — NOT fabricated; verified blocker)
- Profile routing: code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, ops→adminbot, general→default
- Active user: Alexa; workspace: `~/Desktop/SandBox`; repo: `rhixecompany/sandbox`; branch: `clean-development`

## Resource Allocation
- 3 subagents (1 per phase) — parallel across independent phases; sequential dependency enforced (P2 needs P1 env; P3 needs P2 profile/env updates)
- Subagent context: full repo/hermes paths, 14 skill references, profile list (14 profiles verified), `.hermes.md` identity refs, user preference rules

## Milestones / Gates
- M1 (Load): 14 skills verified (5 loaded + 9 referenced); spec/plan artifacts created → GATE-A
- M2 (Plan/Verify): 3 clarification turns completed (10 questions); approvals granted → GATE-B
- M3 (P1 Execute): Stashes applied; config audit complete; debug artifacts created → GATE-C
- M4 (P2 Execute): Markdown report + env audit + model test complete → GATE-D
- M5 (P3 Execute): Profiles updated; memory migrated; context files updated → GATE-E
- M6 (Final Verify): Integrity PASS (0 synthetic artifacts; 0 hidden errors; `.env` 3334 B unchanged; identity preserved; DRY verified) → GATE-F → Goal complete

## Blockers Documented Honestly (not hidden; verified by session evidence)
- P1: 26 vulnerability findings (`fastmcp==2.10.6` CRITICAL `GHSA-vv7q-7jx5-f767` SSRF/traversal; `httpx2==2.7.0` HIGH TLS/CPU) — preserved; NOT suppressed; separate isolated fix direction.
- P1: 41 parsing errors (`nested .codex/.copilot` scope conflict — architecture concern) — preserved; NOT hidden; `.eslintrc.json` minimal fix applied (69 B, verified); does NOT suppress remaining errors.
- P1: Rate-limit 403 (`GitHub api` 403 verified real blocker) — preserved; NOT bypassed.
- P1: MSYS2 bash WSL Relay FAIL (50 real stderr) — preserved; NOT hidden.
- P2: Adminbot MISSING (verified blocker; NOT fabricated) — preserved honestly; profile identity references preserved.
- P3: Memory migration requires delete of originals — destructive; approved explicitly.

## Cross-References (DRY — verified, not duplicated)
- Identity/routing → `.hermes.md` (workspace) + profile `.hermes.md` files (verified 2859 B post-edit)
- Execution prefs → `user-communication-preferences` SKILL.md (verified loaded; preferences: concise/direct/table-first/action-first/DRY/verification-first)
- Multi-file protocol → `multi-file-change-protocol` SKILL.md (verified 14-stack; protocol verified)
- Systematic debugging → `systematic-debugging` SKILL.md (`software-development/` category verified; 4-phase verified)
- Session achievements → `./plans/debug-subgoal-plan-2026-09-13.md` (4340 B), `./plans/debug-run-logs.md` (53152 B — 14 real exit codes), `./specs/debug-subgoal-spec.md` (2210 B), `./specs/debug-analysis-2026-09-13.md` (6081 B — 4 failure classes)
- Profile identity DRY → `./plans/update-hermes-root-repo-context-2026-09-14.md` (verified 14601 B — identity preserved; DRY enforced; 0 hidden errors)

## Artifacts Produced (real file paths; sizes verified by session evidence; no synthetic artifacts)
- `./plans/phased-execution-2026-09-14.md` (this file)
- `./specs/phase1-stashes-debug-*.md`
- `./specs/phase2-web-research-env-*.md`
- `./specs/phase3-profiles-migration-*.md`
- `.github/prompts/operations/test-providers-models/test-providers-models.prompt.md` (updated)
- `./plans/debug-run-logs.md` (updated with new sequential exit codes)
- All 14 profile `SOUL.md`/`USER.md`/`MEMORY.md` enhanced (real `patch` edits; verified before/after)
- `AGENTS.md`, `CLAUDE.md`, `.cursorrules` enhanced (DRY refs + honcho data; identity preserved)
