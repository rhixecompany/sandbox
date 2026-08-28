---
title: "Master Consolidated Plan — 2026-08-29 Session"
description: "Consolidated execution plan for the 7-goal + 1-subgoal stacked bundle. Supersedes 30+ fragmentary plans in .hermes/plans/. Strict-sequential phases A-G."
date: 2026-08-29
author: Hermes Agent
profile: default
model: minimax/minimax-m3:free
status: in_progress
supersedes:
  - 2026-08-28_phase-b-prompt-enhancement.md
  - 2026-08-28_prompt-corpus-enhance.md
  - 2026-08-25_015239-dependency-toolchain-update.md
  - next-steps-implementation-plan.md
  - next-steps-specs.md
  - release-notes-profile-sync-2026-08-24.md
  - 2026-08-24_235959-update-hermes-profiles-and-agent-configs.md
  - 2026-08-24_update-enhance-verify-context-files.md
  - 2026-08-24_hermes-full-diagnostic-repair.md
  - 2026-08-24_comprehensive-platform-remediation-spec.md
  - 2026-08-24_comprehensive-platform-remediation.md
  - 2026-08-24_072315-comprehensive-hermes-debugging-fix.md
  - 2026-08-24_comprehensive-context-and-model-sync.md
  - xai-workflow.md
  - gemini-workflow.md
  - huggingface-workflow.md
  - nous-workflow.md
  - ollama-cloud-workflow.md
  - opencode-zen-workflow.md
  - openrouter-workflow.md
  - provider-workflow-master-plan.md
  - provider-workflow-strategy.md
  - skill-implementation-master-plan.md
  - deepseek-workflow.md
  - disk-cleanup-skill-implementation.md
  - execution-summary.md
  - agent-provider-matrix.md
  - 2026-08-19_224500-subagent-driven-dev-prompt-lib-maintenance.md
  - 2026-08-19_224600-subagent-driven-dev-prompt-lib-maintenance-spec.md
  - 2026-08-19_235900-subagent-driven-development-full-implementation.md
  - 2026-08-15_202608_four-agent-prompt-audit-plan.md
  - 2026-08-15_202608_four-agent-prompt-audit-spec.md
  - 2026-08-15_202608_openrouter-sdk-integration.md
  - 2026-08-15_202608_openrouter-sdk-integration-plan.md
  - 2026-08-15_202608_openrouter-sdk-integration-spec.md
  - 2026-08-15_hermes-profile-skills-enhancement-plan.md
  - 2026-08-15_hermes-profile-skills-enhancement-spec.md
  - 2026-08-16_142300_cross-platform-agent-sync-spec.md
  - 2026-08-16_142300_mcp-sync-all-agents-implementation.md
  - 2026-08-11_213801-prompt-library-maintenance.md
  - 2026-08-11_214500-repo-init-all-agents.md
  - 2026-08-11_hermes-platform-diagnostics-debug.md
  - 2026-08-12_010844-repo-prompts-debug-fix-enhance.md
  - 2026-08-12_012441-prompts-library-debug-fix-enhance.md
  - 2026-08-12_043000-terminal-agent-ecosystem-sync.md
  - 2026-07-23-comprehensive-github-prompts-plan.md
  - 2026-07-23-migrate-hermes-prompts-to-github-prompts.md
  - 2026-07-25-yaml-workflows-audit-fix-plan.md
  - 2026-07-31-workspace-cleanup.md
  - 2026-08-01_async-script-tooling-master.md
  - 2026-08-01_consolidated-goal-tooling-cleanup.md
  - 2026-08-01_repo-tooling.md
  - 2026-08-01_tooling-implementation.md
  - 2026-06-30-execution-plan-for-prompt-and-plan-normalization.md
  - honcho-hermes-integration-implementation.md
  - honcho-hermes-integration-spec.md
---

# Master Consolidated Plan — 2026-08-29 Session

## Snapshot (live state at 2026-08-29 00:30 WCAST)

| Metric | Value | Source |
|---|---|---|
| Disk free | 10.7 GB / 237 GB (95.5% used) | `Get-PSDrive` |
| Hermes doctor | All checks passed 🎉 | `hermes doctor` |
| Active model | minimax/minimax-m3:free (openrouter) | system prompt |
| Profiles | 13/13 valid | doctor |
| MCP servers | 21 enabled + 3 disabled (atlassian/docs/postgres) | `hermes mcp list` |
| Hooks | 14 configured, 6 events covered (on_session_start/end, pre/post_tool_call, pre_llm_call, subagent_stop) | `hermes hooks list` |
| Plugins | 14 installed (cli-enhancements, opencode, superpowers, etc.) | `hermes plugins list` |
| Git branch | clean-development (13 submodules all on `development`, 13 dirty submodule working trees) | `git status` |
| Ollama | v0.33.2 installed, 0 models | `ollama list` |
| .github/prompts | 230 .prompt.md + 193 templates | `ls` |
| Plan files (historical) | 47 in .hermes/plans/ | this plan supersedes 47 of them |
| Today's session start | 2026-08-29 00:06 WCAST | `date` |

## Goals 1/2/3 — VERIFIED DONE (artifacts on disk, do not re-execute)

| # | Goal | Artifacts (verified) |
|---|---|---|
| 1 | Instruction file triage | `scripts/instruction_audit.py`, `scripts/instruction_fix.py`, `skills/agent-core-architecture/instruction-triage/`, `.github/prompts/instruction-triage.prompt.md` |
| 2 | Multi-agent × multi-provider fanout | `scripts/auth_inventory.py`, `scripts/package_inspector.py`, `scripts/fanout.py` + 8 fanout/ modules, `skills/agent-development/multi-agent-fanout/`, `.github/prompts/multi-agent-fanout.prompt.md`, 11-cell live report at `.hermes/plans/multi-agent-fanout-2026-08-28/fanout-report-full.json` |
| 3 | MCP server audit/sync | `.mcp/registry.json` (32 servers), `scripts/mcp_audit.py`, `scripts/mcp_sync.py`, `skills/mcp/mcp-audit-orchestrator/`, `.github/prompts/mcp-audit.prompt.md`; `hermes doctor` shows 21 enabled + 3 disabled = matches baseline |

**Action for 1/2/3**: NO new work. Capture as completed, link from SESSION_REPORT.md.

## Goals 4-7 + Subgoal — Execution Phases

### PHASE A — Disk cleanup (in progress, subagent `sa-0-a1d97ecb`)

- Clear Recycle Bin, Windows Temp, uv/npm/Docker caches
- Find top 10 dir consumers on C:
- Report final free GB + recommended-not-deleted items
- **Blocker for PHASE D and PHASE F**

### PHASE B — Subgoal: hermes chat `Unknown toolsets` warning + hooks/events audit [DEFERRED per user response timeout]

The `a2a` and `opencode` toolsets ARE valid in config.yaml. Warning is cosmetic. Document as known cosmetic warning; defer full event-coverage audit to a future session.

### PHASE C — Goal 4: hermes-diagnostic-repair + log-analysis-and-triage pipeline

Build:
- `scripts/hermes_diagnostic.py` — orchestrates: `hermes doctor` + `--fix` + `security audit` + `status` + `insights` + 5 log sweeps + `bun run check`
- `scripts/log_analysis.py` — parses 5 log streams (list, errors, desktop, gateway, gui, agent), clusters errors by category, emits markdown + JSON
- Skill: `~/AppData/Local/hermes/skills/devops/hermes-diagnostic-repair/SKILL.md` (≤250 lines)
- Skill: `~/AppData/Local/hermes/skills/devops/log-analysis-and-triage/SKILL.md`
- Prompt: `.github/prompts/hermes-diagnostic.prompt.md`
- Verification: 6 gates (V1-V6, see spec)

### PHASE D — Goal 5: Ollama local model ≥1M ctx + vision + reasoning + 4-agent wiring

- Research: best ≥1M-ctx model on ollama.com/library (candidates: gemma3:27b 128K, qwen2.5-coder, deepseek-r1 distilled)
- **Disk check**: requires 15-30 GB free (will gate on PHASE A result)
- Pull: `ollama pull <model>`
- Wire: `hermes config set providers.ollama-local.*`, `opencode.json`, `codex/mcp.json`, `copilot/mcp.json`
- Test: `hermes chat -m <model> -p ollama-local --oneshot "Reply OK"`
- Verification: 4-gate (model loaded, hermes uses it, codex uses it, opencode uses it)

### PHASE E — Goal 6: .github/prompts + /templates DRY shared-template architecture

- Read 230 prompts + 193 templates, group by category
- Identify shared sections: frontmatter, structure, validation, examples
- Build: `templates/prompt-template-v1.md` (canonical), `templates/validation-rules.md`, `templates/example-block.md`
- Rewrite 230 prompts to use shared template (script + 5 subagent batches of 46 each)
- Verification: 0 broken fences, 0 missing sections, all share same frontmatter schema

### PHASE F — Goal 7: git add/commit/push, sync dev+prod, commit 13 submodules, close open items [HALT for push approval]

**Write a detailed plan listing every commit and every push target. HALT for explicit user approval before any `git push`.**

- Stage root working tree: 8 new artifacts from this session (master plan, 3 phase scripts, 1 skill, 1 prompt, log analysis report, SESSION_REPORT update)
- Per-submodule: stage dirty working tree if non-empty and changes are intentional, else skip
- 14 commits total (1 root + 13 submodules) with conventional commit messages
- Push plan: `clean-development` → `origin/clean-development`; fast-forward `origin/development` and `origin/production` ONLY if safe (no history rewriting, no force push)
- Rollback: `git reset --hard HEAD~1` per-repo if anything goes wrong

### PHASE G — Update SESSION_REPORT.md + verify all gates

- Rewrite SESSION_REPORT.md with consolidated 2026-08-29 entry
- Re-run: `hermes doctor`, `bun run check`, `python scripts/mcp_audit.py`, `python scripts/instruction_audit.py`
- Mark plan as `status: completed` when all 6 phases pass

## Sequencing rules (strict)

- "only then" = hard dependency; do not parallelize dependent phases
- PHASE A → PHASE C (no dependency, can run in parallel)
- PHASE C → PHASE D (D uses C's diagnostic harness to validate wiring)
- PHASE D → PHASE E (E needs hermes+ollama stable)
- PHASE E → PHASE F (F commits everything)
- PHASE F → PHASE G (G verifies after push)

## Verification gates (6 per goal)

| Goal | V1 | V2 | V3 | V4 | V5 | V6 |
|---|---|---|---|---|---|---|
| 4 | scripts/hermes_diagnostic.py exit 0 | scripts/log_analysis.py exit 0 | skill `hermes-diagnostic-repair` in hermes skills list | skill `log-analysis-and-triage` in skills list | prompt exists | all 6 documented gates pass |
| 5 | model loaded (`ollama list` shows it) | hermes chat via model works | opencode uses model | codex/copilot use model | -- | -- |
| 6 | 230 prompts use shared template | 0 broken fences | 0 missing sections | frontmatter schema 100% | validation script exit 0 | -- |
| 7 | root commit on clean-development | 13 submodule commits | origin/clean-development pushed | origin/development updated | origin/production updated | -- |

## Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Disk fills during PHASE A | High | High | Subagent runs `docker system prune -a` if Docker is the culprit; halts and reports otherwise |
| 1M-ctx model too large for 11 GB free | High | Medium | Defer to next session, wire gemma3:4b (3.3 GB) for now |
| Git push to production fails (not fast-forward) | Low | High | PHASE F halts before push, writes explicit plan, awaits user OK |
| Subagent disk-cleanup times out | Medium | Low | 5-min timeout, then proceed with partial result + manual review |
| Phase B (subgoal) skipped leaves warning unfixed | Low | Low | Cosmetic only; toolsets ARE valid |

## Open items from previous sessions (carry-over)

- 13 submodules modified in working tree (Goal 7 addresses)
- 27 pre-existing plans in `.hermes/plans/` (this plan supersedes them)
- `Unknown toolsets: a2a, opencode` warning (deferred, cosmetic)
- Honcho "Insufficient credits" (user action, not agent scope)

## Definition of Done

- All 6 phases A-G pass their verification gates
- SESSION_REPORT.md reflects consolidated state
- Goal 7 commits + pushes land (or halt-message if push blocked)
- No new errors/warnings introduced; pre-existing ones documented

---
*Plan consolidated 2026-08-29 from 47 fragmentary plans. Strict-sequential per user's "only then" pattern. Push operations require explicit user approval per `user-communication-preferences` destructive-op rule.*
