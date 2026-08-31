---
title: "Comprehensive Reimplementation Master Plan — 2026-08-31 Evening"
description: "Consolidated execution plan for 10 subgoals: identity/instruction triage, plugins/hooks enablement, authorized-provider non-interactive scripts/skills/hooks, MCP + .github/mcp.json canonical setup, prompt library DRY shared-template repair, git sync automation, diagnostic+debug sweep, hub skill updates, and judge-skill revalidation to ≥95."
date: 2026-08-31
author: Hermes Agent
profile: default
model: stepfun/step-3.7-flash:free
status: in_progress
supersedes:
  - 2026-08-31_152242-comprehensive-reimplementation-master.md
  - 2026-08-31_152354-hermes-diagnostic-2026-08-31_152354.md
---

# Comprehensive Reimplementation Master Plan — 2026-08-31 Evening

## Snapshot (live state at 2026-08-31 18:xx WCAST)

| Metric | Value | Source |
|---|---|---|
| Workspace | `C:\Users\Alexa\Desktop\SandBox` | session context |
| Hermes home | `C:\Users\Alexa\AppData\Local\hermes` | live inspection |
| Git branch | `clean-development` | `git branch --show-current` |
| Last commit | `c43c80a0` | `git log -1` |
| Untracked | 5 files in `judge_results/` + `.hermes-tmp.*` | `git status --short` |
| Profiles | 14 listed (`default` + 13 aliases) | `hermes profile list` |
| Active model | `stepfun/step-3.7-flash:free` via `nous` | `hermes config show` |
| Authorized providers | copilot, deepseek, gemini, huggingface, minimax-oauth, nous, ollama-cloud, openai-api, openai-codex, opencode-zen, openrouter, xai, xai-oauth | `hermes auth list` |
| Plugins | 14 plugins with manifests under Hermes `plugins/` + repo `.github/hooks/` | live inspection |
| Hooks | 14 shell hooks active for 6 events | `hermes hooks list` |
| MCP servers | 21 enabled, 3 disabled | `hermes mcp list` |
| Repo prompts | 236 `.prompt.md` files | `find .github/prompts -maxdepth 1 -type f` |
| Template dirs | 455 entries under `.github/prompts/templates` | `find .github/prompts/templates` |

## Clarified Scope

| Item | Decision |
|---|---|
| Provider automation scope | authorized providers only |
| Local model cleanup scope | Ollama CLI and local models only |
| `.github/mcp.json` | create canonical file and align references |

## Goals

| # | Subgoal | Parallelizable | Notes |
|---|---|---|---|
| 1 | Triage, debug, fix, verify identity/instruction files across repo, Hermes root, and all profiles | Yes | SOUL/USER/MEMORY/.hermes/AGENTS/CLAUDE/.cursorrules |
| 2 | Check, debug, fix, verify plugins and hooks; enable all possible events | Partial | Hermes plugins + `.github/hooks` |
| 3 | Authorized-provider non-interactive scripts/skills/hooks | Yes | read-only `hermes auth list` inventory first |
| 4 | MCP + canonical `.github/mcp.json` setup across Hermes/Copilot/Codex/OpenCode | Partial | audit then enable/repair |
| 5 | Prompt library DRY repair, validation, shared-template enforcement | Yes | category-based |
| 6 | Git add/commit/push/submodule + sync development/production automation | Checkpoint | requires explicit approval before push |
| 7 | Diagnostic + systematic debug sweep | After 1/2/4 | doctor, audit, logs, bun check |
| 8 | Hub skill updates | After 7 | `hermes skills check/update` |
| 9 | Judge-skill revalidation to ≥95 | After 8 | specs/plans/prompts/scripts/hooks/plugins judges |
| 10 | Ollama local cleanup only | After 7 | uninstall/remove models/data |

## Execution Order

### Phase 0 — Plan, Approvals, Inventory
- Save this plan to `.hermes/plans/`
- Capture exact plugin/hook/MCP/prompt inventory
- Build approved execution queue
- Approval gate: destructive git push and destructive Ollama removal

### Phase 1 — Identity/Instruction Triage (Goal 1)
- Audit root + Hermes root + all 14 profile instruction files
- Normalize DRY references, remove duplication, align preferences
- Validate with `prompts-judge`/`specs-judge` where applicable

### Phase 2 — Plugins/Hooks Enablement (Goal 2)
- Enable/repair repo `.github/hooks` and Hermes plugins/hooks
- Register event handlers for all supported lifecycle events
- Verify with `plugins-judge`/`hooks-judge`

### Phase 3 — Provider Automation (Goal 3)
- Inventory authorized providers
- Create non-interactive scripts/skills/hooks to execute requests
- Emit structured result: provider, context, max-output, capabilities

### Phase 4 — MCP Canonical Config (Goal 4)
- Create `.github/mcp.json` if missing
- Cross-check Hermes/Copilot/Codex/OpenCode configs
- Repair broken servers, test enabled set

### Phase 5 — Prompt Library DRY Repair (Goal 5)
- Categorize prompts
- Create shared canonical templates under `.github/prompts/templates/_shared/`
- Repair/fix/validate references and docs

### Phase 6 — Git Sync Automation (Goal 6)
- Implement verified git automation scripts
- Commit, push, submodule sync, checkout development/production
- Approval gate before any push

### Phase 7 — Diagnostic + Debug (Goal 7)
- Run `hermes doctor && hermes doctor --fix && hermes security audit && hermes status && hermes insights && bun run check`
- Run log sweeps
- Fix blockers before proceeding to 8/9/10

### Phase 8 — Hub Skill Updates (Goal 8)
- `hermes skills check`
- Update eligible skills
- Re-run quick verification

### Phase 9 — Judge Revalidation (Goal 9)
- Run judge skills on specs/plans/prompts/scripts/hooks/plugins
- Improve scores to ≥95
- Re-run until threshold met

### Phase 10 — Ollama Cleanup (Goal 10)
- Stop/remove Ollama CLI models/data only
- Verify Docker Model Runner untouched

## Verification Gates

| Goal | V1 | V2 | V3 | V4 | V5 |
|---|---|---|---|---|---|
| 1 | triage report | DRY diff | validation pass | -- | -- |
| 2 | plugins-judge score | hooks-judge score | event coverage report | -- | -- |
| 3 | provider inventory | script smoke tests | structured output sample | -- | -- |
| 4 | `.github/mcp.json` exists | MCP test pass | config parity report | -- | -- |
| 5 | shared template created | prompt audit clean | category coverage report | -- | -- |
| 6 | git automation tested dry-run | approval recorded | commit/push success or halted cleanly | -- | -- |
| 7 | doctor clean | security audit clean | bun check clean | logs reviewed | -- |
| 8 | update list captured | updates applied | re-check clean | -- | -- |
| 9 | judge scores ≥95 | re-run report | -- | -- | -- |
| 10 | ollama removed | docker runner untouched | disk reclaim reported | -- | -- |

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Destructive push blocked by branch protection | Medium | High | halt + approval record + dry-run first |
| Provider script automation triggers rate limits | Medium | Medium | authorized only, retry/backoff |
| Prompt template rewrite breaks references | Medium | High | category batches + validation after each batch |
| Disk/time limits on judge reruns | Medium | Medium | target lowest-score artifacts first |
| Ollama removal removes needed assets | Low | Medium | confirm Docker runner untouched; keep scripts |

## Definition of Done

- All 10 goals pass their verification gates or have explicit halted/reported blockers
- Plan marked `status: completed`
- User has approval artifacts for destructive steps
- No unexplained warnings left open from goals 1-7 before moving to 8-10
