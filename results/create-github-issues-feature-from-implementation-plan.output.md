# Create GitHub Issues from Implementation Plan — Dry-Run & Real Execution

## Source
- **Prompt:** `prompts/create-github-issues-feature-from-implementation-plan.prompt.md`
- **Plan:** `plan/prompt-orchestration-comprehensive-plan.md` (Phases 0–4, "Ready for execution")

## Credentials Status
- `gh auth`: Logged in as `rhixecompany` ✅
- Remote: `github.com/rhixecompany/sandbox.git`
- Existing issues: #1 (resource staleness), #2 (failed runs) — unrelated, no dedup needed

## Issues Created (Real — API)

| # | Title | URL | Phase |
|---|-------|-----|-------|
| 3 | [plan][phase-0] Verification gate: confirm prompts, templates, scripts, git & profile | https://github.com/rhixecompany/sandbox/issues/3 | Phase 0 |
| 4 | [plan][phase-1] Audit, categorize, dedupe, judge & remediate 370+ local skills | https://github.com/rhixecompany/sandbox/issues/4 | Phase 1 |
| 5 | [plan][phase-2] Generate agent context files & validate VS Code JSON configs | https://github.com/rhixecompany/sandbox/issues/5 | Phase 2 |
| 6 | [plan][phase-3] Bidirectional sync Hermes <-> Copilot <-> Codex (zero drift) | https://github.com/rhixecompany/sandbox/issues/6 | Phase 3 |
| 7 | [plan][phase-4] Inventory, benchmark & compare 7 authorized LLM providers | https://github.com/rhixecompany/sandbox/issues/7 | Phase 4 |

## Labels
Repo has no `feature`/`chore` labels (only standard GitHub set). Labels omitted; issues created without them.

## Templates
No `feature_request.yml` or `chore_request.yml` templates exist in `.github/ISSUE_TEMPLATE/`. Fell back to `gh issue create` with markdown body files.

## Issue Body Files (Intermediate)
Written to `results/gh-issue-bodies/` (5 `.md` files, one per phase) — retained for reference.

## Verification
- ✅ 5 issues created (3 → 7), zero duplicate with existing issues #1–#2
- ✅ Each maps to exactly one implementation plan phase from `plan/prompt-orchestration-comprehensive-plan.md`
- ✅ Each body includes: Objective, Source Plan ref, Deliverables, Sub-phases, Success Criteria, Safety Gates, Dependencies