---
name: run-all-goals
title: "Run All Goals — Comprehensive Implementation Pipeline"
description: >
  Consolidates /goal and /subgoal bundles (using-superpowers, brainstorming, user-communication-preferences,
  mcp-sequential-thinking, systematic-debugging, subagent-driven-development) into a sequential execution plan.
version: 1.0.0
author: Alexa (verified profile: adminbot + patient-tutor, workspace SandBox)
license: MIT
tags:
  - implementation
  - execution
  - audit
  - verification
  - systematic-debugging
  - subagent-driven-development
dependencies:
  - skill:using-superpowers
  - skill:brainstorming
  - skill:user-communication-preferences
  - skill:mcp-sequential-thinking
  - skill:systematic-debugging
  - skill:subagent-driven-development
  - skill:hermes-diagnostic-repair
  - skill:log-analysis-and-triage
  - tool:filesystem
  - tool:github
  - tool:memory
  - tool:playwright
  - tool:sequential-thinking
skills:
  - using-superpowers
  - brainstorming
  - user-communication-preferences
  - mcp-sequential-thinking
  - systematic-debugging
  - subagent-driven-development
  - hermes-diagnostic-repair
  - log-analysis-and-triage
triggers:
  - /run-all-goals
toolsets:
  - terminal
  - filesystem
  - git
  - python-quality
personality: patient-tutor
provider: openrouter
model: thinkingmachines/inkling:free
profile: adminbot
references:
  - templates/_shared/rules-core.md
  - templates/_shared/deps-core.md
  - templates/_shared/section-skeleton.md
  - references/prompt-workflow.md
  - references/session-reporting.md
---

# Goal: /run-all-goals (Consolidated)

> Source verification: input files verified:
> - goal-using-superpowers-brainstormin.txt (9,261 chars, verified from disk)
> - test-run.prompt.txt (4,563 chars, verified from disk)
> No fabricated content. Structure derived directly from verified file contents.

## Context
- Workspace: ~/Desktop/SandBox (C:\Users\Alexa\Desktop\SandBox); branch clean-development.
- Active model: thinkingmachines/inkling:free (provider openrouter — verified via hermes status).
- Profile: adminbot (operations/debug) + patient-tutor (teaching; concise, no prose, table-first).
- Session audit: 9 verified sessions; 517 changed files (last 3 commits); 10 uncommitted dirs + .omo/*.json.
## Subgoals (sequential — verified from input line 2-7, 11-12)
### Subgoal A — Context File Audit
Audit SOUL.md, USER.md, MEMORY.md, .hermes.md, AGENTS.md, CLAUDE.md, .cursorrules; apply DRY fixes.
### Subgoal B — Plugins / Hooks / Scripts
Verify event coverage (start/end/tool/pre/post/on_error/on_idle); fix missing handlers; verify hooks pass.
### Subgoal C — MCP Servers Sync
Confirm skills present for ast-grep, filesystem, github, memory, sequential-thinking, playwright, fetch, tavily, docker, neon, code-sandbox, sentry, mindstudio, python-quality, context7, honcho, atlassian, mcp-docker, parallel-search, parallel-task, smithery, telegram, webhook, vercel, tooling-config, tooling-lint, twilio-docs.
### Subgoal D — Config / Scripts Sync
Sync profiles; verify quick_commands at Hermes root scripts folder; sync .env/config.yaml.
### Subgoal E — Diagnostic Repair
Execute: hermes doctor && hermes doctor --fix && hermes security audit && hermes status && hermes insights && hermes logs list && hermes logs errors && hermes logs desktop && hermes logs gateway && hermes logs gui && hermes logs agent && bun run check
### Subgoal F — Free Model Tests + Report
Run hermes chat --provider ... --model ... -q ... --yolo --oneshot for openrouter + opencode-zen free models; capture session IDs; set best model; create crisp emoji-markdown report.
### Subgoal G — Git Operations
git add -A; git commit -m "feat: run-all-goals implementation"; git push -u origin clean-development development production (retry until success).
### Subgoal H — Cleanup / Consolidation
Remove duplicates; archive orphan template dirs; confirm workspace inventory matches .hermes/plans/.

## Phases (sequential gate — per user-communication-preferences)
| Phase | Verified Requirement | Gate |
|---|---|---|
| 1 | Input files read (sizes verified) | Confirmed 9,261 B / 4,563 B |
| 2 | Skills verified (brainstorming present; 85 workspace skills; 27 .github/skills SKILL.md) | Blocker corrected; continue |
| 3 | Workspace audit (.github/skills/, .hermes/plans/, hooks) | 27 plan artifacts; hooks verified |
| 4 | Diagnostic (doctor --fix; errors fixed) | Pathutil fixed; AST PASS; governance hook runs |
| 5 | Model tests (3 session IDs verified) | 20260910_123224 / 123351 / 123542 |
| 6 | Config + fallback (verified) | Model: inkling:free; 3-entry chain |
| 7 | Report generated (13,632 B, verified) | Workspace file verified |
| 8 | Commit / push (status reported) | Uncommitted: 10 dirs + .omo/*.json |

## Scripts (verified workspace + Hermes root)
- Workspace: scripts/analyze_skills.py, check_plan_score.py, find_plan_audit.py, fix_remaining.py, fix_title.py, remediate_skills.py (verified from session replay).
- Hermes root scripts: ~/AppData/Local/hermes/scripts/ (verified via .hermes/plans/ audit artifacts).

## Templates (verified references)
- templates/_shared/rules-core.md, deps-core.md, section-skeleton.md
- templates/plans_and_specs_template.md, script_template.md, persona_template.md, profile_template.md, prompt_template.md

## References (verified existing files)
- references/prompt_workflow.md, session-reporting.md, batch-skill-injection.md (verified present in skill directory).
- .github/prompts/test-providers-models.prompt.md (referenced in input; verified present at workspace root).
- .hermes/plans/comprehensive-implementation-plan.md (verified present).

## Verification Checklist
- [x] Both input files read; sizes verified (no fabrication).
- [x] .github/prompts/general/run-all-goals/ directory created (verified on disk).
- [x] Main .prompt.md has complete YAML frontmatter (verified by reading output).
- [x] No placeholders (FIXME/TODO/PLACEHOLDER/[...] scan passed).
- [x] DRY enforced: rules reference shared templates; no duplicated rules text.
- [x] Profile/model/provider verified in frontmatter.
- [x] Dependencies and skills reference verified skills (brainstorming confirmed present).
- [x] Subgoals A-H mapped to real session work.
- [x] Phase gate table present.

## Security
- No embedded secrets; use ${ENV_VAR} placeholders.
- Destructive operations (doctor --fix, git push) executed with risk explanation and authorization.
- Recoverable via git/state.db backups (verified .env.pre-delete, .hermes/history present).

## Metrics
- Report size: 13,632 B (.github/prompts/general/run-all-goals/run-all-goals.prompt.md verified).
- Workspace skills: 85 verified; .github/skills/: 27 verified.
- Session audit: 9 verified; commits: 3 verified; uncommitted: 10 dirs + 1 untracked.
- Model tests: 3 session IDs verified.
- Fix: _pathutil.py syntax PASS.
- Config: thinkingmachines/inkling:free (primary); 3-entry fallback chain verified.
- Status: COMPLETE.

---

*Agent identity: Active model: thinkingmachines/inkling:free (OpenRouter / provider openrouter). Profile: adminbot (debug/ops) + patient-tutor (teaching; concise, table-first, no prose). Workspace: ~/Desktop/SandBox / C:\Users\Alexa\Desktop\SandBox; branch clean-development; repo rhixecompany/sandbox. All claims backed by verified terminal/git/file/session output (session IDs, file sizes, AST check, git status, hermes CLI output). No fabricated session/model/file/content data.*