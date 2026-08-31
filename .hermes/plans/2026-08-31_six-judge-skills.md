---
title: "Six Asset Judge Skills — Build, Score, Verify (2026-08-31)"
description: "Build 6 judge skills (specs, plans, prompts, scripts, hooks, plugins) and raise each to ≥95/100 via skill-judge."
date: 2026-08-31
author: Hermes Agent
profile: default
model: minimax/minimax-m3:free
status: in_progress
extends: 2026-08-29_full-audit-remediation.md
---

# Six Asset Judge Skills — Master Plan

## Goal

Build 6 new judge skills (one per asset class) and raise each to ≥95/100 score. Asset classes:

1. **specs** — `.hermes/specs/*.md` (requirements, acceptance criteria, NFRs)
2. **plans** — `.hermes/plans/*.md` (phases, tasks, dependencies, status)
3. **prompts** — `.github/prompts/*.prompt.md` + templates
4. **scripts** — `scripts/*.py`, `scripts/*.sh`, `scripts/*.ts`
5. **hooks** — `~/AppData/Local/hermes/hooks/*` (event-handler shell scripts)
6. **plugins** — `~/AppData/Local/hermes/plugins/*` (plugin.yaml + hooks/ + tools/)

Each judge skill:
- Defines class-specific 5-dimension rubric (max 100 pts)
- Provides concrete scoring heuristics
- Offers `python <judge>/scripts/judge.py <target>` CLI
- Writes `judge_results/<class>_audit.json` + `.md`
- Is itself scored by skill-judge ≥95

## Live State (verified)

| Metric | Value | Source |
|---|---|---|
| Diagnostic sweep | 11/11 OK (33s) | `hermes_diagnostic.py` |
| skill-judge self-score | 100/100 | batch_skill_judge.py |
| hub skills | 24 checked, 2 updates available | `hermes skills check` |
| prompts | 237 in `.github/prompts/` | `ls` |
| plans | 38 in `.hermes/plans/` | `ls` |
| scripts | 40 in `scripts/` | `ls` |
| plugins | 50+ bundled + user | `hermes plugins list` |
| hooks | 14 | `hermes hooks list` |

## Phases (strict sequential)

### Phase A — Build the 6 judge skills (parallel-ish)

Each skill under `~/AppData/Local/hermes/skills/qa/<class>-judge/SKILL.md` with:
- Frontmatter (name, title, description, version, author, license, tags)
- 5-dimension rubric (max 100)
- Heuristic scoring algorithm
- CLI invocation: `python <skill>/scripts/judge.py`
- Verification checklist
- Pitfalls section

#### A.1 specs-judge
- Specs: heading depth, required sections (Goal, Requirements, Acceptance Criteria, NFRs, Verification), cross-refs to plans
- Heuristic: parse H1/H2/H3, check for 5 required sections, verify plan cross-refs exist
- Script: `judge.py --specs-dir .hermes/specs`

#### A.2 plans-judge
- Plans: phased structure (≥3 phases), status field, completion %, dependencies table
- Heuristic: H1, `## Phase` headings ≥3, `[ ]` / `[x]` checklist, status: in_progress/completed
- Script: `judge.py --plans-dir .hermes/plans`

#### A.3 prompts-judge
- Prompts: frontmatter (description, trigger, toolsets, skills), Goal/Context/Workflow sections, fenced code examples
- Heuristic: parse YAML FM, check trigger field, count sections, verify code-fence balance
- Script: `judge.py --prompts-dir .github/prompts`

#### A.4 scripts-judge
- Scripts: shebang + permissions + syntax check + argparse/--help + error handling
- Heuristic: detect language, run `python -m py_compile` or `node --check`, parse `argparse`
- Script: `judge.py --scripts-dir scripts`

#### A.5 hooks-judge
- Hooks: registered events coverage, executable bit, shellcheck-clean, idempotent
- Heuristic: cross-reference `hermes hooks list`, run `shellcheck`, check `set -e`
- Script: `judge.py --hooks-dir ~/AppData/Local/hermes/hooks`

#### A.6 plugins-judge
- Plugins: plugin.yaml valid, version, hooks dir, tools defined, on_hooks documented
- Heuristic: parse YAML, check hooks/ subdir, enumerate tools, verify platform compat
- Script: `judge.py --plugins-dir ~/AppData/Local/hermes/plugins`

### Phase B — Score each (raise to ≥95)

For each of the 6 new judge skills:
1. Run `batch_skill_judge.py --skills-dir <path> --threshold 95`
2. If <95, identify lowest dimension, patch SKILL.md, re-score
3. Iterate until ≥95

### Phase C — Final verification

- 6/6 judge skills ≥95
- Each judge script runs end-to-end on real targets
- Update SESSION_REPORT.md
- Commit

## Files to Create

| Path | Purpose |
|---|---|
| `~/AppData/Local/hermes/skills/qa/specs-judge/SKILL.md` | specs judge skill |
| `~/AppData/Local/hermes/skills/qa/specs-judge/scripts/judge.py` | CLI runner |
| `~/AppData/Local/hermes/skills/qa/specs-judge/references/rubric.md` | 5-dim rubric |
| `~/AppData/Local/hermes/skills/qa/plans-judge/...` | plans judge (4 files) |
| `~/AppData/Local/hermes/skills/qa/prompts-judge/...` | prompts judge (4 files) |
| `~/AppData/Local/hermes/skills/qa/scripts-judge/...` | scripts judge (4 files) |
| `~/AppData/Local/hermes/skills/qa/hooks-judge/...` | hooks judge (4 files) |
| `~/AppData/Local/hermes/skills/qa/plugins-judge/...` | plugins judge (4 files) |
| `judge_results/six_judges_scores.md` | score table |
| `judge_results/six_judges_run.json` | run evidence |
| `.hermes/plans/2026-08-31_six-judge-skills.md` | this plan |

## Verification

| Gate | Target |
|---|---|
| All 6 judge skills exist | 6/6 |
| Each scores ≥95 via batch_skill_judge | 6/6 |
| Each judge.py runs without error on real targets | 6/6 |
| Diagnostic sweep still 11/11 OK | pass |
| SESSION_REPORT.md updated | pass |

## Risks

- **Permissions** — `~/AppData/Local/hermes/skills/` may be locked; copy path approach.
- **Skill-judge heuristic** may inflate/under-score thin skills; always verify manually.
- **Phase ordering** — skill_manage ops are atomic per batch; create all 6 in one batch.