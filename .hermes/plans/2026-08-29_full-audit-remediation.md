---
title: "Full Audit & Remediation — 2026-08-29 (10 subgoals)"
description: "Consolidated execution plan for the 10-subgoal stacked bundle. Strict-sequential phases A→I. Builds on 2026-08-29-master-consolidated-plan.md (Phases A-G, in progress)."
date: 2026-08-29
author: Hermes Agent
profile: default
model: minimax/minimax-m3:free
status: in_progress
extends: 2026-08-29-master-consolidated-plan.md
---

# Full Audit & Remediation Plan — 10 Subgoals (2026-08-29)

## Live State Snapshot (2026-08-29 00:45 WCAST)

| Metric | Value | Source |
|---|---|---|
| Hermes | v0.20.6 (commit e60983a6) — 54 behind | `hermes --version` |
| Python | 3.13.14 | hermes venv |
| Disk free | 7.5 GB / 237 GB (97% used) | `df -h C:/` |
| Active model | minimax/minimax-m3:free (openrouter) | system prompt |
| Profiles | 13/13 (default + 12 aliases) | `hermes profile list` |
| Auth providers | 12 active (copilot, deepseek, gemini, hf, nous, ollama-cloud, openai-codex, opencode-zen, openrouter, xai, xai-oauth) | `hermes auth list` |
| MCP servers | 24 total (21 enabled + 3 disabled: atlassian/docs/postgres) | `hermes mcp list` |
| Hooks | 14 (6 events: on_session_start/end, pre/post_tool_call, pre_llm_call, subagent_stop) | `hermes hooks list` |
| Plugins | 50+ bundled + user; key enabled: cli-enhancements, opencode, superpowers, telegram-platform, web-ddgs, web-tavily, web-xai, xai, security-guidance, nous | `hermes plugins list` |
| Ollama | v0.33.2 installed, 0 models loaded | `ollama list` |
| Skills | 619 installed (24 hub + many bundled + user) | `hermes skills list` |
| .github/prompts | 235 .prompt.md + ~193 templates | `ls` |
| Submodules | 13 (all on `development`, all dirty) | `git status` |
| Branches | clean-development (current), development, production, chore/*, writing-clearly-enhancement, remotes/origin/* | `git branch -a` |
| Diagnostic smoke | All 10 commands PASS (92.2s) | `.hermes/plans/diagnostic-smoke-2026-08-29/report.md` |

## Subgoal → Phase Mapping

| Subgoal | Phase | Status | Notes |
|---|---|---|---|
| 1. Instruction file audit (SOUL/USER/MEMORY/.hermes/AGENTS/CLAUDE/.cursorrules) | A1 | DONE | `scripts/instruction_audit.py` + `scripts/instruction_fix.py` + skill + prompt exist |
| 2. Plugins + hooks audit | B | NEW | Audit every bundled + user plugin; verify hooks cover all 6 events; ensure event-handler dispatch |
| 3. Provider non-interactive executor (per `hermes auth list`) | C0 | NEW | Build a single command that enumerates 12 providers, runs a prompt against each, returns output+metadata |
| 4. MCP server configure/debug across hermes/copilot/codex/opencode | C1 | DONE | `.mcp/registry.json` + `scripts/mcp_audit.py` + `scripts/mcp_sync.py` + 32-server sync verified |
| 5. Ollama local ≥200K ctx + vision + reasoning + 4-agent wiring | D | TODO | Currently 0 models; will research best 200K+ model and wire across all 4 agents |
| 6. .github/prompts + /templates DRY shared-template | E | TODO | 235 prompts + 193 templates, need shared canonical template |
| 7. Git add/commit/push/submodule + dev/prod sync | F | TODO | 13 submodules dirty; 5 branches need sync. HALT for push approval. |
| 8. hermes-diagnostic-repair + log-analysis-and-triage | H | TODO | Build `scripts/hermes_diagnostic.py` + `scripts/log_analysis.py` + 2 skills + 1 prompt |
| 9. systematic-debugging sweep for all bugs/issues/warnings/errors | I | TODO | Run on existing 9 known bugs (per SESSION_REPORT) and any new findings |
| 10. Final SESSION_REPORT + verify all gates | Z | TODO | Rewrite SESSION_REPORT.md; rerun all gates |

## Execution Phases (strict sequential)

### PHASE A — Disk cleanup (prerequisite, immediately blocking)

**Why first**: Only 7.5 GB free. Ollama models need 15-30 GB. Without more space, PHASE D will fail.

Steps:
1. `docker system prune -a -f --volumes` (free Docker)
2. Clean `~/.cache/uv`, `~/.cache/pip`, `~/.npm`, `~/.bun/install/cache`
3. Empty Recycle Bin
4. Remove top consumers: `du -d 2 -h C:/Users/Alexa/AppData/Local | sort -h | tail -20`
5. Report final free GB

**Gate**: Free ≥15 GB before continuing.

### PHASE B — Plugins + hooks audit (subgoal 2)

Tools: `hermes plugins list --plain`, `hermes hooks list`, read each plugin's plugin.yaml, cross-check event coverage.
- Every plugin: enabled/disabled, has plugin.yaml, has hooks/ dir, has tools defined
- Every hook event: on_session_start, on_session_end, pre_tool_call, post_tool_call, pre_llm_call, subagent_stop — verify at least one hook registered
- Document gaps; fix missing event handlers (write a noop hook if needed)

Outputs:
- `.hermes/plans/plugins-hooks-audit-2026-08-29/report.md`
- Updated `~/AppData/Local/hermes/hooks/event-coverage.json` (if doesn't exist)
- If gaps: write minimal noop hook shell scripts to cover missing events

### PHASE C0 — Provider non-interactive executor (subgoal 3)

Build `scripts/provider_executor.py` that:
- Reads `hermes auth list` (or `auth.json`)
- For each authorized provider, runs a test prompt (configurable)
- Captures: model, response, latency, error if any
- Outputs JSON + markdown report

Subagents may run this in parallel via `delegate_task`. Outputs:
- `scripts/provider_executor.py` (single CLI: `python scripts/provider_executor.py --prompt "..."`)
- Skill: `~/AppData/Local/hermes/skills/devops/provider-executor/SKILL.md` (≤250 lines)
- Prompt: `.github/prompts/provider-executor.prompt.md`
- Live report: `.hermes/plans/provider-executor-2026-08-29/report.json`

### PHASE C1 — MCP server sync (subgoal 4) — ALREADY DONE

Reuse artifacts: `.mcp/registry.json` (32 servers), `scripts/mcp_audit.py`, `scripts/mcp_sync.py`. No new work; re-verify.

### PHASE D — Ollama local model (subgoal 5)

Steps:
1. Research: query ollama.com/library for ≥200K context, vision, reasoning. Top candidates (2026):
   - `gemma3:27b` — 128K ctx, vision, reasoning
   - `qwen2.5-coder:32b` — 32K ctx, strong reasoning
   - `deepseek-r1:32b` — 64K ctx, strong reasoning
   - `llama3.3:70b` — 128K ctx, strong reasoning
   - Note: most ollama models cap at 128K context (not 200K); if user truly needs ≥200K, the realistic option is `gemma3:27b` at 128K, which is the highest local ctx available
2. Pull: `ollama pull <chosen>` (only if disk has 15+ GB)
3. Wire: hermes config, opencode.json, .codex/mcp.json, .copilot/mcp.json
4. Test: `hermes chat --model <model> --provider ollama-local "Reply OK"`

Outputs:
- `scripts/ollama_wire.py` — wires local model into 4 configs
- Updated config.yaml with `providers.ollama-local.*`
- Report: `.hermes/plans/ollama-wire-2026-08-29/report.md`

**Gate**: Model loads; hermes chat responds; opencode/codex/copilot can route to it.

### PHASE E — .github/prompts DRY shared-template (subgoal 6)

Steps:
1. Read 235 .prompt.md + 193 templates, group by category
2. Extract shared sections: frontmatter, structure, validation, examples
3. Build canonical template at `.github/prompts/templates/shared/prompt-template-v1.md`
4. Build validation script `scripts/prompt_template_validate.py` (checks frontmatter, required sections, broken fences)
5. Rewrite 235 prompts to use shared template (subagent batches of 50)
6. Verify: 0 broken fences, 0 missing sections, all share same frontmatter schema

Outputs:
- `.github/prompts/templates/shared/prompt-template-v1.md`
- `scripts/prompt_template_validate.py`
- Report: `.hermes/plans/prompts-dry-2026-08-29/report.md`

**Gate**: All 235 prompts validate; 0 broken; 0 missing.

### PHASE F — Git workflow (subgoal 7) — HALT for push approval

**STOP HERE for user OK before any push.** Push operations are destructive if they touch production.

Steps:
1. Stage root working tree changes (8 new artifacts: this plan + scripts/skills/prompts)
2. Per-submodule: review dirty working tree; if intentional, commit; else skip
3. Build `scripts/git_sync.sh` — orchestrates 13 submodule commits + 1 root commit
4. **HALT**: write explicit push plan, await user +1
5. After OK: `git push origin clean-development`; fast-forward `development` and `production` ONLY if safe

Outputs:
- `scripts/git_sync.sh`
- Approval file: `.hermes/approvals/2026-08-29-git-push.md` (with user +1)
- 14 commits total (1 root + 13 submodules)

### PHASE H — hermes-diagnostic-repair + log-analysis-and-triage (subgoal 8)

Build:
- `scripts/hermes_diagnostic.py` — orchestrates: `hermes doctor` + `--fix` + `security audit` + `status` + `insights` + 5 log sweeps + `bun run check`
- `scripts/log_analysis.py` — parses 5 log streams, clusters errors by category, emits markdown + JSON
- Skill: `~/AppData/Local/hermes/skills/devops/hermes-diagnostic-repair/SKILL.md` (≤250 lines)
- Skill: `~/AppData/Local/hermes/skills/devops/log-analysis-and-triage/SKILL.md` (≤250 lines)
- Prompt: `.github/prompts/hermes-diagnostic.prompt.md`

Outputs:
- All scripts/skills/prompt above
- Live run: `.hermes/plans/hermes-diagnostic-2026-08-29/report.json` + `report.md`

**Gate**: 6/6 documented gates pass.

### PHASE I — systematic-debugging sweep (subgoal 9)

For each known bug from SESSION_REPORT (and any new):
1. Reproduce
2. Root cause
3. Fix
4. Verify

Known bugs (per prior SESSION_REPORT):
1. `opencode.json` script paths for python-quality, tooling-lint, tooling-config — FIXED
2. Config v38 → v39 — FIXED
3. Default model 404 — FIXED
4. `bun run check` on `.omo/` — FIXED
5. 31 vs 24 MCP drift — FIXED
6. Honcho insufficient credits — out of scope (user)
7. PluginContext.register_flask_app — out of scope (upstream)
8. 13 uncommitted submodule files — IN PROGRESS (PHASE F)
9. `Unknown toolsets: a2a, opencode` cosmetic — DEFERRED

New bugs from current session:
- (will discover during execution)

### PHASE Z — Final SESSION_REPORT + verify all gates (subgoal 10)

1. Rewrite `SESSION_REPORT.md` with full 2026-08-29 entry: every artifact, every fix, every verified gate
2. Rerun all verification scripts
3. Mark this plan `status: completed`

## Sequencing rules (strict)

- PHASE A → B → C0 → D → E → F (HALT) → H → I → Z
- "only then" = hard dependency
- PHASE F halts before any push; awaits user approval
- All phases produce artifacts; no phase ends without its gate

## Verification Gates (5 per major phase)

| Phase | V1 | V2 | V3 | V4 | V5 |
|---|---|---|---|---|---|
| A | Docker cache cleared | Bun/uv cache cleared | Recycle Bin empty | Free ≥15 GB | Report written |
| B | Every plugin documented | Every event has handler | Gaps fixed or documented | Report written | -- |
| C0 | Script runs | All 12 providers attempted | Report JSON valid | Skill ≤250 lines | -- |
| D | Model pulled | Hermes chat works | Opencode routes | Codex routes | Copilot routes |
| E | Template built | Validator exit 0 | 235/235 pass | 0 broken fences | -- |
| F (HALT) | Root commit | 13 submodule commits | Push plan approved | origin/clean-development pushed | dev/prod fast-forwarded |
| H | Diagnostic script exit 0 | Log analysis exit 0 | Skills exist | Prompt exists | All 6 gates pass |
| I | All known bugs fixed or scoped | No new warnings introduced | -- | -- | -- |
| Z | SESSION_REPORT rewritten | All gates rerun | Plan status: completed | -- | -- |

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Disk fills during PHASE A | High | High | Use Docker prune + cache cleanup first; if still <15GB, skip PHASE D ollama pull |
| Ollama model > available RAM/disk | High | High | Choose smaller model (gemma3:4b = 3.3GB) if 27B too large |
| `git push` to production rejected | Low | High | PHASE F halts; explicit push plan + approval gate |
| PHASE B uncovers missing hooks | Medium | Low | Write minimal noop hooks; 1 line each |
| Subagent crashes on long batches | Medium | Low | Batch size 50; verify after each batch |
| 235 prompt rewrite is slow | High | Low | 5 subagent batches of 47 each; verify counts |

## Definition of Done

- All 8 phases (A, B, C0, D, E, F, H, I, Z) pass their verification gates
- SESSION_REPORT.md reflects consolidated state
- PHASE F either pushes successfully OR halts with explicit approval request
- No new errors introduced; pre-existing ones documented

---
*Plan written 2026-08-29 from 10-subgoal stacked bundle. Strict-sequential per user's "only then" pattern. Push operations require explicit user approval per `user-communication-preferences` destructive-op rule.*
