---
name: verification-checklist
category: templates/_shared
version: 2.0.0
license: MIT
author: derived from run-all-goals.prompt.md verification block + tree.prompt.txt (primary source) + prompt-management verification checklist + skill-judge scoring rules
description: Shared verification checklist format. Applied to every phase output. tree.prompt.txt is PRIMARY source.
---

# Verification Checklist — Shared Template

> Sources: verified from `.github/prompts/general/run-all-goals/run-all-goals.prompt.md` + **`tree.prompt.txt`** (PRIMARY source) + `prompt-management` skill verification checklist + `skill-judge` scoring rules (0-100 scale; 99+ target). No fabricated criteria.

## Mandatory Checks (Every Artifact)

Apply in order. Halt on first failure; do not proceed to next phase until gate passes.

### Tree-Primary Source Verification

- [ ] **tree.prompt.txt** verified as PRIMARY source (read from disk; file size confirmed).
- [ ] All goals/subgoals derive from tree.prompt.txt directives (not synthesized).
- [ ] No fabricated content; all goals/subgoals backed by tree.prompt.txt lines.
- [ ] tree.prompt.txt referenced in prompt frontmatter, plan, and all artifacts.

### Tree Cleanup Verification (tree.prompt.txt Goals 1-3)

- [ ] **Phase 1 Cleanup:** .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts folders deleted/verified.
- [ ] **Phase 2 Cleanup:** *.json (except package.json, pyrightconfig.json), *-report.md, *.log, *.txt (skip *.prompt.txt) cleaned/verified.
- [ ] **Phase 3 Config:** .editorconfig, .git-blame-ignore-revs, .gitattributes, .gitignore, .gitmodules, .markdownlint-cli2.jsonc, .markdownlint.jsonc, .pre-commit-config.yaml, .prettierignore, .prettierrc.json, *.toml, *.yaml updated/verified.
- [ ] **Phase 4 Config:** requirements.txt, tsconfig.json, package.json, pyrightconfig.json updated/verified.

### mjs->mts Conversion Verification (tree.prompt.txt Goal 5)

- [ ] All *.mjs files converted to *.mts files.
- [ ] No .mjs files remain without .mts counterparts.
- [ ] Conversion verified via `find . -name '*.mjs'` or equivalent.

### Source Integrity

- [ ] All source files read directly from disk (not synthesized from memory).
- [ ] File sizes verified (`ls -l` or `read_file` byte count reported).
- [ ] Missing source files documented explicitly (e.g., `test-run.prompt.txt`: 0 matches — NOT fabricated).
- [ ] No placeholder markers (`FIXME:`, `TODO:`, `PLACEHOLDER`, `[SKILL_PRUNED]`) present in output.

### Structure Integrity

- [ ] YAML frontmatter loads with `yaml.safe_load` (no duplicate fields, no broken fences).
- [ ] `name:` matches folder/file name; `trigger:` equals `/<name>`.
- [ ] `dependencies:` and `skills:` both present; prefix conventions (`skill:` / `tool:` / `prompt:`) verified.
- [ ] `tags:` non-empty (derived from filename/content; not empty `tags: []` from conversion artifacts).
- [ ] `references:` resolves to existing files (verified by `search_files` or `read_file` before claim).
- [ ] `templates/_shared/` references resolve (verified: `rules-core.md`, `deps-core.md`, `section-skeleton.md`, `skills-table-core.md` exist at build time).

### Content Integrity

- [ ] No duplicated rules text (DRY: references `rules-core.md`, not inline duplication).
- [ ] Subgoals AâH mapped to real session work (verified from `goal-using-superpowers-brainstormin.txt` lines 1â14; not synthesized).
- [ ] Phase gate table present with verified requirements and status column.
- [ ] Metric values backed by verified terminal/git/file/session output (not estimated).
- [ ] Agent identity block present; model/provider/workspace verified in live config (`hermes profile list`, `.hermes.md` state).

### Security / Safety

- [ ] No `.env` contents, tokens, or credentials embedded in prompt body or scripts.
- [ ] `${ENV_VAR}` placeholders only where secrets required.
- [ ] Destructive operations (`doctor --fix`, `git push`, archive, model `--yolo`) have authorization record in plan/artifact.
- [ ] Recoverable backup references verified (`.env.pre-delete`, `.hermes/history`, `.git` state).
- [ ] No backup files created (SOUL.md Rule 6 / user preference); git rollback relied upon exclusively.

### Execution Verification (Real Tool Output â Not Fabricated)

- [ ] Each phase executed via `terminal` (not simulated); output captured in result.
- [ ] `git status` / `git log` verified before/after destructive phases.
- [ ] `hermes doctor`, `hermes status`, `hermes auth list`, `hermes config show` outputs recorded (Phase E / F).
- [ ] Session IDs (Phase F) captured from actual `hermes chat` output (not estimated).
- [ ] `verify_run_all_goals.py` (or equivalent) run; output recorded (`PASS` / `FAIL` with line numbers).
- [ ] `ruff format+check --fix` or equivalent syntax validation executed (per hooks preference).

## Score Scale (From Skill-Judge / Audit Patterns â Verified Reference)

| Score | Meaning | Action |
|---|---|---|
| 99â100 | Excellent â passes all gates | Proceed; claim complete |
| 95â98 | Near-pass â minor issues | Fix and re-verify (do not claim complete) |
| <95 | Fail â major structural/content/safety issues | Halt; fix root cause; do not retry same failing path (SOUL.md Fallback Trigger) |

If 2 consecutive verification passes report the same HIGH issue: stop batch automation (per `prompt-management` pitfall rules); switch to per-file `read_file` + targeted `patch` or manual repair.
