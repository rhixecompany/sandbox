---
title: "Comprehensive Reimplementation Master Plan — Diagnostic + Skills Update + 6 Judge Skills"
description: "Master plan that fully implements/reimplements: diagnostic sweep, hermes skills check + update, skill-judge on self + 6 new judge skills (specs/plans/prompts/scripts/hooks/plugins), raised to ≥95/100. Closes the carried-over open items from 2026-08-29."
date: 2026-08-31
author: Hermes Agent
profile: default
model: minimax/minimax-m3:free
status: in_progress
extends:
  - 2026-08-29_full-audit-remediation.md
  - 2026-08-31_six-judge-skills.md
supersedes_scope_fragments:
  - 2026-08-31_six-judge-skills.md
---

# Comprehensive Reimplementation Master Plan — 2026-08-31

## Goal

Fully implement, reimplement, and close ALL open items from the user's 3-subgoal request:

1. **Diagnostic sweep** — `hermes doctor && --fix && security audit && status && insights && logs ×5 && bun run check`, then `/systematic-debugging` to clear bugs/warnings.
2. **Hub skills check + update** — `hermes skills check` → `hermes skills update` (apply any available upstream updates).
3. **Judge skills, ≥95/100** — `/skill-judge` on `skill-judge` itself, build/raise the 6 new judge skills (specs/plans/prompts/scripts/hooks/plugins), each ≥95/100.

## Current Context (verified live)

| Field | Value | Source |
|---|---|---|
| Session | 2026-08-31 15:22 WCAST | `date` |
| Profile | `default` (active gateway) | `hermes profile list` |
| Model | `minimax/minimax-m3:free` (openrouter) | config dump |
| Repo | `~/Desktop/SandBox` (rhixecompany/sandbox) | `pwd` |
| Working tree | clean (last commit 54d1ba6f) | `git status` |
| Branch | `clean-development` | `git status` |
| 14-skill stack | All loaded this turn | `skill_view` × 14 |
| `.hermes/specs/` | **does not exist** | `ls` |
| Last diagnostic | **2026-08-31 13:35** — 11/11 OK | `.hermes/plans/hermes-diagnostic-2026-08-31_133528/report.md` |
| Last 6-judge build | **2026-08-31 13:45** — 6/6 at 100/100 | `judge_results/six_judges_scores.md` |
| SESSION_REPORT.md | Real rolling summary (not a stub) | `read_file` |

## Carried-over open items (4)

1. **PR #12 merge** — user-owned (protected `development` branch)
2. **Provider auth failures** — deepseek 401, opencode-zen 401, gemini 402 — user-owned
3. **2 hub skill updates** — `agentmemory-hooks`, `data-migration-scripts` — addressed in Subgoal 2 (was deferred last turn)
4. **Submodule `node_modules`** (~2.4 GB) — user-owned

## Subgoal Decomposition

### Subgoal 1 — Diagnostic sweep (idempotent re-run)

| Step | Action | Verification |
|---|---|---|
| 1.1 | `hermes doctor` (no flags) | exit 0 |
| 1.2 | `hermes doctor --fix` | exit 0; report what was fixed |
| 1.3 | `hermes security audit` | exit 0 |
| 1.4 | `hermes status` | clean status |
| 1.5 | `hermes insights` | metrics dump |
| 1.6 | `hermes logs list` | count + recent |
| 1.7 | `hermes logs errors` | errors count |
| 1.8 | `hermes logs desktop` | desktop log health |
| 1.9 | `hermes logs gateway` | gateway log health |
| 1.10 | `hermes logs gui` | gui log health |
| 1.11 | `hermes logs agent` | agent log health |
| 1.12 | `bun run check` (lint + format + markdownlint + spellcheck) | 0 errors |
| 1.13 | Capture to `.hermes/plans/hermes-diagnostic-<ts>/report.{json,md}` | file exists |
| 1.14 | If any diagnostic step reports non-zero, apply `/systematic-debugging` to find root cause before fixing | iron law |

**Decision rule:** If all 13 commands exit 0 and `bun run check` is clean, declare ✓ without re-running fixes. Last run was 13:35, only ~2h old.

### Subgoal 2 — Hub skills check + update

| Step | Action | Verification |
|---|---|---|
| 2.1 | `hermes skills check` | list available updates |
| 2.2 | `hermes skills update` (auto-apply) | capture updated skills + new SHA |
| 2.3 | `hermes skills audit` (post-update) | confirm no regressions |
| 2.4 | If a skill breaks post-update, apply `/systematic-debugging` to revert or patch | |

**Safety:** `hermes skills update` is non-destructive (downloads to `~/AppData/Local/hermes/skills/hub-cache/`); if anything breaks, `hermes skills rollback <skill>`.

### Subgoal 3 — Judge skills: score self + 6 new judges at ≥95

| Step | Action | Verification |
|---|---|---|
| 3.1 | Locate `skill-judge` skill path | `find ~/AppData/Local/hermes/skills/qa/skill-judge` |
| 3.2 | `python batch_skill_judge.py --skills-dir <skill-judge-dir> --threshold 95` | self.json score ≥95 |
| 3.3 | For each of the 6 judge skills (`specs`, `plans`, `prompts`, `scripts`, `hooks`, `plugins`): run `batch_skill_judge.py --skills-dir <dir> --threshold 95` | 6 self_score.json files ≥95 |
| 3.4 | For any judge <95: read judge_results, identify lowest dimension, patch SKILL.md, re-score | iterate until ≥95 |
| 3.5 | Verify each judge CLI runs end-to-end on real targets | 6 audit.{json,md} files |
| 3.6 | Aggregate scores → `judge_results/six_judges_scores.md` | file exists |

**Targets from last turn (already 100/100):**

| Judge | Score | CLI Real Target | Note |
|---|---|---|---|
| specs-judge | 100 | n/a (`.hermes/specs/` dir absent) | ✓ no-op acceptable |
| plans-judge | 100 | 62 plans, avg 42.0, 3/62 pass | ✓ |
| prompts-judge | 100 | 233 prompts, avg 80.4, 233/233 pass | ✓ |
| scripts-judge | 100 | 34 scripts, avg 81.1, 26/34 pass | ✓ |
| hooks-judge | 100 | 7 hooks, avg 29.6, 0/7 pass | ✓ |
| plugins-judge | 100 | 12 plugins, avg 80.0, 12/12 pass | ✓ |

**Re-run decision:** All 6 are already at 100. Re-running `batch_skill_judge.py` is idempotent — produces same result + new timestamp. Just refresh `judge_results/` files to today's timestamp.

## Specs Artifacts (per multi-file change protocol)

Per Rule #1 ("create comprehensive implementation specs,plan,prompt,scripts,skills"), this master plan IS the spec. Linked:

| Artifact | Purpose |
|---|---|
| `.hermes/plans/2026-08-31_152242-comprehensive-reimplementation-master.md` | This file (master plan + spec) |
| `.hermes/plans/2026-08-31_six-judge-skills.md` | Scope fragment (superseded by this) |
| `.hermes/plans/hermes-diagnostic-<ts>/report.md` | Diagnostic run output |
| `judge_results/six_judges_scores.md` | 6-judge aggregated scores |
| `SESSION_REPORT.md` | Updated rolling summary |

## Files Likely to Change

| Path | Change |
|---|---|
| `SESSION_REPORT.md` | Append 2026-08-31 session entry |
| `.hermes/plans/2026-08-31_152242-comprehensive-reimplementation-master.md` | Created (this file) |
| `.hermes/plans/hermes-diagnostic-<ts>/report.{json,md}` | Created by diagnostic run |
| `judge_results/<judge>_self_score.{json,md}` × 6 | Refreshed |
| `judge_results/six_judges_scores.md` | Refreshed |
| `~/AppData/Local/hermes/skills/hub-cache/` | Possibly updated by `hermes skills update` |
| `git: new commit on `clean-development`` | Non-destructive, with rollback path |

## Verification Gates (per multi-file-change protocol)

- [ ] Subgoal 1: 13 commands + `bun run check` all exit 0
- [ ] Subgoal 1: diagnostic report file exists with timestamp ≥ today
- [ ] Subgoal 2: `hermes skills check` ran; updates applied or "none available"
- [ ] Subgoal 2: post-update `hermes skills audit` shows no regression
- [ ] Subgoal 3: skill-judge self-score ≥95
- [ ] Subgoal 3: 6 judge skills each ≥95 (4 already at 100, re-verify)
- [ ] Subgoal 3: 6 judge CLI scripts each ran end-to-end on real targets
- [ ] SESSION_REPORT.md updated
- [ ] `git status` clean (any local changes committed)

## Risks & Trade-offs

| Risk | Mitigation |
|---|---|
| `hermes skills update` breaks a skill | `hermes skills rollback <name>`; verify pre-update SHA |
| Diagnostic step takes >5 min | Run in background with `notify=true` |
| Re-running idempotent judge scores wastes context | Cheap — just refresh files |
| Submodule `selenium_webdriver` fork-retry blip | Already noted as non-blocking; skip |
| Git push blocked by remote auth | Commit locally only; do not push (user-owned action) |

## Profile & Tools

- **Profile**: `default` (matches "general purpose" routing for this master plan)
- **Tools**: `terminal`, `execute_code`, `patch`, `write_file`, `read_file`, `search_files`, `delegate_task`
- **MCP-first**: `mcp__filesystem`, `mcp__ast_grep`, `mcp__memory`, `mcp__sequential-thinking` (deferred — native tools suffice for this deterministic run)

## Phases (Sequential Execution — auto-advance per user standing goal)

| Phase | Subgoals | Output |
|---|---|---|
| **Phase 0** | Verify live state (DONE — this turn) | Live state captured above |
| **Phase 1** | Subgoal 1: diagnostic report | `report.{json,md}` |
| **Phase 2** | Subgoal 2: skills check + update | Updated skills list |
| **Phase 3** | Subgoal 3: judge skills score refresh | `judge_results/*.json` |
| **Phase 4** | Update SESSION_REPORT.md + commit | Clean working tree |

## Standing Goal — Auto-Advance

Per USER.md standing goal + `executing-plans` Phase 3 "auto-advance" rule: when the user provides all phases upfront, execute end-to-end without intermediate confirmation. Only pause if:
- A command exits non-zero and `/systematic-debugging` cannot resolve
- `hermes skills update` introduces a regression that requires a decision
- Any of the 6 judges drops below 95 (would need a fix loop)

---

## Appendix — Last Session Judge Results (2026-08-31 13:45)

| Judge | File | Score | Status |
|---|---|---|---|
| specs-judge | `judge_results/specs-judge_self_score.json` | 100 | ✓ PASS |
| plans-judge | `judge_results/plans-judge_self_score.json` | 100 | ✓ PASS |
| prompts-judge | `judge_results/prompts-judge_self_score.json` | 100 | ✓ PASS |
| scripts-judge | `judge_results/scripts-judge_self_score.json` | 100 | ✓ PASS |
| hooks-judge | `judge_results/hooks-judge_self_score.json` | 100 | ✓ PASS |
| plugins-judge | `judge_results/plugins-judge_self_score.json` | 100 | ✓ PASS |
| skill-judge | `judge_results/skill_judge_self.json` | 100 | ✓ PASS |

Real-target CLI runs from last turn:

| Judge | Files | Avg | Passed |
|---|---|---|---|
| plans | 62 | 42.0 | 3/62 |
| prompts | 233 | 80.4 | 233/233 |
| scripts | 34 | 81.1 | 26/34 |
| hooks | 7 | 29.6 | 0/7 |
| plugins | 12 | 80.0 | 12/12 |
| specs | 0 | n/a | (dir absent) |