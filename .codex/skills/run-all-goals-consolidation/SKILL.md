---
name: run-all-goals-consolidation
version: 1.0.0
description: Consolidate /goal bundles (brainstormin .txt + test-run.prompt.txt) into a single DRY .prompt.md output with verified shared templates/references, authorization gates for destructive subgoals, and real-tool-output verification â not simulated results.
author: Hermes Agent (derived from verified workspace session 2026-09-10)
license: MIT
tags: [run-all-goals, consolidation, verification, authorization, destructive-ops]
dependencies:
  - skill:prompt-management
  - skill:convert-plaintext-to-md
skilled_used:
  - prompt-management (loaded; verified SKILL.md read during session)
  - using-superpowers / brainstorming / user-communication-preferences / mcp-sequential-thinking / subagent-driven-development / systematic-debugging (referenced in .prompt.md; verified present)
references:
  - .github/prompts/general/run-all-goals/templates/_shared/rules-core.md
  - .github/prompts/general/run-all-goals/templates/_shared/deps-core.md
  - .github/prompts/general/run-all-goals/templates/_shared/section-skeleton.md
  - .github/prompts/general/run-all-goals/references/prompt-workflow.md
  - .github/prompts/general/run-all-goals/references/session-reporting.md
  - .github/prompts/general/run-all-goals/references/batch-skill-injection.md
---

# Skill: /run-all-goals Consolidation Pipeline

Always-on rules for this class of task (the user's verified preferences embedded in SKILL.md â not memory):

- Profile identity: user is Alexa, profile=default; routing applies per task (code→architect, research→analyst, ops→adminbot is routing target ONLY — NOT user identity). Communication: concise bullets; result before explanation; table-first.
- Communication: concise bullets first; result (`PASS`/verified B count) before explanation; table-first for comparisons.
- Execution: read â targeted `patch` â verify (not full blind rewrites). Verify gates before claim.
- DRY enforcement: rules/dependencies/sections referenced from `templates/_shared/` (built at `.github/prompts/general/run-all-goals/templates/_shared/`); never duplicated inline.
- Source `.txt` files (`goal-using-superpowers-brainstormin.txt`, `test-run.prompt.txt`): verify at workspace root (`find`/`wc -c` via `terminal` â not `execute_code` which runs at `/tmp/`). Size discrepancy (9,261/4,563 vs 9,277/4,575 B) is CRLF normalization (`core.autocrlf=true` â verified in `.hermes.md`); do NOT invent a different file.

## Procedure (steps in execution order, with real commands)

### 1. Source verification (before any edit)

- `find . -maxdepth 1 -name "*brainstormin*" -o -name "*test-run*prompt*"` â verify both `.txt` files exist at workspace root.
- `wc -c` both; `head -5` both. Confirm first line starts with `/goal ...`. Do not fabricate if `execute_code` reports missing (CWD `/tmp/`).
- Document `test-run.prompt.txt` absence honestly if missing; do not synthesize its content.

### 2. Load required skills

- Confirm `using-superpowers`, `brainstorming` (SKILL.md verified 5,352 B in workspace), `prompt-management` skills present (`skills_list` / file inventory â not memory).
- If `prompt-management` loaded: note it is user-owned; updates must go through `hermes curator adopt prompt-management` (verified refusal message from this session). Do not attempt autonomous patch.

### 3. Build shared artifacts (only when physically missing)

- Check `.github/prompts/templates/_shared/` exists (verified: missing initially; built during this session).
- When missing: build from verified workspace rules (`SOUL.md` identity + cognitive style; `USER.md` profile + preferences; `.hermes.md` environment; project `.github/prompts/` dependency patterns â 29 verified matches), NOT from synthetic content.
- Create: `rules-core.md`, `deps-core.md`, `section-skeleton.md`, `skills-table-core.md`, `verification-checklist.md`, `best-practices.md`. Verify with `ls -l` before claim.
- Create references (`references/prompt-workflow.md`, `session-reporting.md`, `batch-skill-injection.md`) derived from verified `prompt-management` SKILL.md + verified `execution-summary.md` (867 B). Never invent APIs/procedures.

### 4. Consolidate .prompt.md (DRY, verified references)

- Read existing `.prompt.md` (`read_file`; verified 7,606 B before enhancement).
- Apply targeted `patch` (not blind full rewrite): add `references:` links to new shared templates/references; enhance `version` note; add source-verification appendix with real byte counts.
- Map subgoals AâH to actual `.txt` line content (`brainstormin` L1=goal, L2=B, L3=C, L4=D, L14=E, L15=F, L12=G; L10â11=H; `test-run` lines confirm model-test/cleanup).
- Verify with `grep -E 'FIXME:[^[]|TODO:[^[]|PLACEHOLDER|\[SKILL_PRUNED\]'` â only checklist explanation line matches; zero real placeholders.
- Verify `yaml.safe_load` loads references (no duplicate `tags:`; `trigger:` = `/run-all-goals` matches `name:`).

### 5. Authorization gate (always-on for this user â embedded in SKILL.md, not just plan)

Before destructive subgoals E (doctor --fix), F (`--yolo` model chat), G (`git push` to 3 branches), H (archive/delete):

- Confirm user's authorization is recorded (`read_file` of `.hermes/plans/run-all-goals-implementation.md` authorization block or `.prompt.md` authorization appendix).
- If authorization missing: STOP; ask user (`clarify`) â do not proceed. Per SOUL.md Rule 11 (destructive ops need authorization + risk explanation).
- Risk explanation must mention recoverability (`.env.pre-delete` if present; `.hermes/history` if present; git rollback; no backup files per user preference). Verify presence via `ls -1` (document absence honestly â do not claim present if `ls` shows MISSING).

### 6. Execution (sequential gates â per user preference: direct, not blind parallel)

- Subgoals AâD: direct execution; verify outputs (`ls`, `grep`, `hermes status`, `hermes auth list`, `hermes config show`).
- Subgoal E (`hermes doctor` â `doctor --fix`): document real CLI output (verified: 1 npm vulnerability for `agent-browser` found â reported honestly, not hidden). Do not fabricate "all fixed".
- Subgoal F (`hermes chat --yolo --oneshot` for openrouter + opencode-zen free models): capture session IDs from real CLI output; reference verified IDs (`20260910_123224` / `123351` / `123542` from audit); set best model via `hermes config set` / `hermes fallback add`; create emoji-markdown report.
- Subgoal G (`git add -A; git commit ...; git push ...`): if `.git/index.lock` exists (verified blocker in this session), report blocker honestly (`git status` shows staged files; commit blocked; push tracking set). Do not fabricate "commit succeeded".
- Subgoal H (cleanup/archive): verify workspace inventory matches `.hermes/plans/`; archive orphan templates (`git mv` to `.hermes/archived-plan-templates/`); confirm zero duplicates remain (`find` / `git status`).

## Pitfalls (imperative rules â mechanism + why â one clause)

- Read workspace-root `.txt` files via `terminal` (`find`/`head`/`wc -c`), not `execute_code` â `execute_code` runs at `/tmp/`; using it for workspace files produces false "missing" results (verified mechanism from this session).
- Before batch rewrite, verify `yaml.safe_load` â `read_file` returns `1|content` format, not raw YAML; batch regex fixes on parsed content silently corrupt sections (`in_deps` / `in_skills` flags lost â mechanism from audit pitfall).
- When adding shared-template references: only wire when the target `references:` section exists; missing `templates/_shared/` files must be built from verified workspace rules (SOUL.md + `.github/prompts/*` dependency patterns â verified 29 matches) â never fabricated.
- No synthetic session IDs: cite only IDs captured from real `hermes chat` CLI output (`execution-summary.md` verified IDs). Invented IDs become permanent false references that future audits trust.
- `.git/index.lock` blocks commit â document honestly (verified blocker in this session); do not retry the same `git commit` 3 times without checking `ls -l .git/index.lock` first (SOUL.md Fallback Trigger).
- When user approves destructive actions, the authorization must be visible in both `.hermes/plans/` (plan authorization block) AND `.prompt.md` appendix (artifact authorization table) â a single invisible authorization record fails verification on future audit.
- Skill `references/` must be topical (`conversion-patterns.md`, not `2026-09-10-conversion.md`) and extendable â this session's `batch-skill-injection.md` reference was added to `references/` rather than a session file; extend it rather than creating `batch-injection-20260910.md`.

## References (within this skill)

- `.github/prompts/general/run-all-goals/templates/_shared/rules-core.md`
- `.github/prompts/general/run-all-goals/templates/_shared/deps-core.md`
- `.github/prompts/general/run-all-goals/templates/_shared/section-skeleton.md`
- `.github/prompts/general/run-all-goals/templates/_shared/skills-table-core.md`
- `.github/prompts/general/run-all-goals/templates/_shared/verification-checklist.md`
- `.github/prompts/general/run-all-goals/templates/_shared/best-practices.md`
- `.github/prompts/general/run-all-goals/references/prompt-workflow.md`
- `.github/prompts/general/run-all-goals/references/session-reporting.md`
- `.github/prompts/general/run-all-goals/references/batch-skill-injection.md`
- `.github/prompts/general/run-all-goals/run-all-goals.prompt.md` (the consolidated artifact â verified enhanced; 14,135 B; DRY; no fabricated content; authorization recorded; source `.txt` sizes verified from disk).
