# Hermes Health Sweep — Comprehensive Implementation Plan

> Generated: 2026-09-04 | Session: hermes-health-sweep | Status: IN_PROGRESS

## Goal

Bring every Hermes-managed asset (desktop, desktop-plugins, plugins, hooks, scripts, agents) up to verified ≥95/100 audit score with full root-cause remediation, while producing a reusable skill artifact that automates future sweeps.

## Scope

| Target | Path | Items | Current | Target |
|---|---|---|---|---|
| Desktop | `~/.hermes/desktop/` | 1 (state) | n/a | n/a |
| Desktop-plugins | `~/.hermes/desktop-plugins/` | 8 dirs | mixed (5 valid, 3 broken) | 5 valid + 3 classified |
| Plugins | `~/.hermes/plugins/` | 12 dirs | 12/12 ≥95 | maintain |
| Hooks | `~/.hermes/hooks/` | 7 files | 7/7 ≥95 + 4 warnings | 7/7 + 0 warnings |
| Scripts | `~/.hermes/scripts/` | 217 files | 169/217 ≥95 (77.9 avg) | ≥200/217 ≥95 (≥85 avg) |
| Agents | `~/.hermes/agents/` | 7 files | unknown | ≥95 each |

## Phases

### Phase 1: Discovery ✓ COMPLETE
- Enumerated targets; ran hermes doctor, hooks doctor, hooks-judge, plugins-judge, scripts-judge
- Captured 2026-09-04 baselines (hooks 97.1, plugins 95.3, scripts 77.9)

### Phase 2: Root Cause Analysis ✓ COMPLETE
- Categorized all 48 script failures, 4 hook warnings, 3 broken desktop-plugin dirs
- Findings logged above (see Findings table)

### Phase 3: Fix Execution ⏳ IN PROGRESS
- Hook allowlist re-validation (4 hooks modified-since-approval)
- Scripts: batch remediation targeting the 48 <70 scripts
- Desktop-plugins: classify + remove 3 broken dirs, fix session-manager double-import
- Agents: run audit + remediate if needed

### Phase 4: Verification ⏳ PENDING
- Re-run all judges, confirm ≥95 thresholds
- Capture final numbers, write SESSION_REPORT.md

### Phase 5: Skill Artifact ⏳ PENDING
- Create `hermes-health-sweep` skill that automates this entire pipeline
- Place at `~/.hermes/skills/devops/hermes-health-sweep/SKILL.md`
- Provide re-runnable scripts at `~/.hermes/skills/devops/hermes-health-sweep/scripts/`

## Milestones

| # | Milestone | Verification |
|---|---|---|
| M1 | Discovery complete | All judges run, baseline captured |
| M2 | All hook warnings cleared | `hermes hooks doctor` shows 0 warnings |
| M3 | Scripts ≥85 avg | `scripts-judge` ≥85 avg, ≥200/217 PASS |
| M4 | Desktop-plugins cleaned | 5 valid + 3 classified/removed |
| M5 | Agents audited | All ≥95 |
| M6 | Skill artifact created | `~/.hermes/skills/devops/hermes-health-sweep/` on disk |
| M7 | SESSION_REPORT.md updated | Full session record committed |

## Resource Allocation

| Resource | Use |
|---|---|
| `hermes doctor` / `hooks doctor` / `plugins doctor` | Health verification |
| `python scripts/judge.py` (5 judge skills) | Scoring per dimension |
| `node --check` | Plugin JS syntax |
| `delegate_task` subagents | Parallel fix dispatch |
| `git` (SandBox repo) | Rollback + commit |
| `hermes hooks revoke + re-add` | Allowlist refresh |

## Timelines

| Phase | Target | Actual |
|---|---|---|
| Phase 1: Discovery | 10 min | 8 min ✓ |
| Phase 2: Root Cause | 5 min | 4 min ✓ |
| Phase 3: Fix Execution | 30 min | in progress |
| Phase 4: Verification | 10 min | — |
| Phase 5: Skill Artifact | 20 min | — |

## Risk & Mitigation

| Risk | Likelihood | Mitigation |
|---|---|---|
| Allowlist re-approval fails on Windows | low | Use exact-match command strings |
| Subagent modifies wrong file | low | Absolute paths + context injection |
| Destructive plugin removal breaks UI | medium | First move to `desktop-plugins/quarantine/`, don't delete immediately |
| Scripts-judge patches collapse syntax | low | Targeted patch only, never scripted regex on .py |