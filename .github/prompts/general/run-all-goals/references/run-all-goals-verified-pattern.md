---
name: run-all-goals-verified-pattern
version: 2.0.0
source: verified session execution with tree.prompt.txt as PRIMARY source; tree-cleanup-first execution; verified artifacts (ls -l) and real CLI outputs; authorization FULL; no synthetic session IDs/capabilities/quality/ranking/PASS.
---

# Verified Pattern: tree-Primary Execution

> **tree.prompt.txt** is the PRIMARY source for the run-all-goals execution pipeline.

## key_rules

- **tree.prompt.txt PRIMARY**: All goals/subgoals derive from tree.prompt.txt directives (cleanup, config, mjs->mts, pipeline)
- **Cleanup-first**: Delete .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts folders BEFORE any construction work
- **mjs->mts conversion**: All .mjs files must be converted to .mts before final verification
- **Config validation**: All config files (.editorconfig, .gitignore, package.json, pyrightconfig.json, tsconfig.json, requirements.txt) must be updated/verified
- **DRY**: Via templates/_shared/ (rules-core/deps-core/section-skeleton/skills-table-core/verification-checklist/best-practices)
- **verify before claim**: Via audit-verified.md files
- **authorization FULL**: Recorded
- **honest blocker**: Timeout reported
- **retry shorter**: -q verified
- **batch dependency injection**: Verified
- **no synthetic session IDs**: Never fabricate capabilities/quality/ranking
- **.git/index.lock**: Cleared
- **git commit**: Verified
- **push**: clean-development/development/production verified
- **.env ONLY .hermes**: Confirmed
- **.env.pre-delete MISSING**: Verified honest
- **0 placeholders**: Verified grep

## tree-specific_checks

1. .enhance/.goals/.hermes_diagnostics/.mcp directories deleted
2. *.json (except package.json, pyrightconfig.json) cleaned
3. *.log/*.txt (skip *.prompt.txt) cleaned
4. .editorconfig/.gitignore/.markdownlint/.prettier files updated
5. All .mjs -> .mts conversion complete
6. *.md files (PLAN.md, SOUL.md, SPEC.md, USER.md, docs) cleaned
7. src/ directory created; files migrated
8. requirements.txt/tsconfig.json/package.json/pyrightconfig.json updated
