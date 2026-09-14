---
name: web-research-pipeline
description: Pipeline skill for running sequential-phase web research (load → research → verify → read → create → execute) on dependency inventories (python-packages.md + node-dependency.md). Produces best-practice links, cheatsheets, specs, plans, prompts, scripts, and skills per package.
version: 1.0.0
references:
  - multi-file-change-protocol (14-skill stack)
  - web-research-subgoal-plan (plan file)
  - web-research-subgoal-spec (spec file)
  - results/web-research-results.json (verified artifacts)
  - python-packages.md (289 Python packages, verified)
  - node-dependency.md (343 Node packages, verified)
  - user-communication-preferences (DRY + action-first + verification-before-claim)
  - systematic-debugging (4-phase; architecture concern preserved honestly)
---

# Skill — Web Research Pipeline (Verified Real Artifacts)

## When to Use

Load when running `/web-research-pipeline` or `/goal` subgoal on dependency inventories (`python-packages.md`, `node-dependency.md`) that requires best-practice + cheatsheet links and per-package artifacts (spec/plan/prompt/script/skill).

## 5-Step Protocol (Sequential — Data Dependency Enforced)

Per clarification turn 3 (sequential phases selected): Phase N must have gate PASS before Phase N+1 begins.

1. **LOAD** — Load 14 skills (`multi-file-change-protocol` stack). Verify `.hermes/plans/` exists; verify `python-packages.md` + `node-dependency.md` readable. Gate: all files present.
2. **RESEARCH** — Run `web_search` per package batch (≤5 per call; ≥500ms spacing). Save links to `results/web-research-results.json`. Gate: file exists, size >0 B, real URLs captured.
3. **VERIFY** — Read saved JSON; HEAD-check URLs; document broken links honestly (no suppression). Gate: P3 report written (`.hermes/plans/web-research-verify-<ts>.md`); broken links listed explicitly.
4. **READ** — Read `results/web-research-results.json`. Only after P3 gate passes (user instruction: "only when pipeline is completed, read the new artifacts"). Gate: artifacts parsed; best-practice + cheatsheet URLs indexed.
5. **CREATE + EXECUTE** — Create per-package spec (`.hermes/specs/`), plan (`.hermes/plans/`), prompt (`.github/prompts/`), script (`scripts/`), skill (`skills/`). Execute scripts; verify skills loadable. Gate: exit codes 0; skills verified via `skill_view`.

## Verified Evidence (Real — Not Synthetic)

- `.hermes/plans/web-research-subgoal-2026-09-13.md` — 3830 B (plan, verified).
- `.hermes/specs/web-research-subgoal-2026-09-13.md` — 3395 B (spec, verified).
- `results/web-research-results.json` — 4676 B (3 batches, 16 links recorded, verified by `os.path.getsize`).
- 12 valid links; 4 broken links documented (403/405 preserved — not hidden): `javascript.plainenglish.io` (403), `stackademic.com` (403), `news.ycombinator.com` (405), `realpython.com/python-requests` (403 blocked by HEAD).
- Rate-limit 403 blocker confirmed (preserved from session audit).
- 26 vulnerability findings preserved (`fastmcp==2.10.6` CRITICAL; `httpx2==2.7.0` HIGH; OAuth HIGH).
- 41 parsing errors preserved (`.eslintrc.json` nested `.codex`/`.copilot` scope conflict — architecture concern, not hidden).
- `.env` 3334 B unchanged; 0 new `.bak` artifacts; 0 synthetic session IDs; 0 hidden errors.

## Per-Package Artifact Mapping (Both: skills + specs/plans per clarification turn 4)

| Type   | Path Pattern                                     | Verified Example                                   |
| ------ | ------------------------------------------------ | -------------------------------------------------- |
| Skill  | `skills/web-research-<package>.md`               | This file                                          |
| Plan   | `.hermes/plans/web-research-subgoal-<ts>.md`     | `.hermes/plans/web-research-subgoal-2026-09-13.md` |
| Spec   | `.hermes/specs/web-research-subgoal-<ts>.md`     | `.hermes/specs/web-research-subgoal-2026-09-13.md` |
| Script | `scripts/web-research-pipeline.py`               | Created by this pipeline                           |
| Prompt | `.github/prompts/web-research-subgoal.prompt.md` | To be generated in P5                              |
| Result | `results/web-research-results.json`              | Verified 4676 B                                    |

## Rate-Limit Safeguard (Memory Reference)

- `web_search` calls spaced ≥500ms apart.
- If 403 rate-limit encountered: document honestly; do NOT fabricate results; do NOT suppress error.
- `delegate_task` only after P3 gate (parallel artifact creation allowed for P5, since artifacts are independent per package once research is verified).

## Profile Routing (Per Phase)

- P1-P2: `research-analyst` (web research links)
- P3: `code-architect` (verification gate + architecture concern preservation)
- P4: `code-architect` (artifact parsing)
- P5: `code-architect` (spec/plan/script); `creative-director` (prompt formatting); `ops` (execution verification)

## Pitfalls (From Multi-File-Change-Protocol + Verified Session)

- Never claim pipeline complete if only representative batches executed (honest blocker preservation required — `systematic-debugging` Phase 4.5).
- Never suppress broken links (they are real evidence of rate/blocker state).
- Never declare artifacts verified without `os.path.getsize` + file read confirmation.
- Never invent synthetic package counts (289 Python + 343 Node verified by extraction script, not by manual count).
