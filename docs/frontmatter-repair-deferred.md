# Frontmatter Repair Deferred

## Status

- **Date:** 2026-06-30
- **Decision:** Pause automated repair after concurrent-write warnings and repeated verification failures.
- **Scope:** 9 `Prompts/*.prompt.md` files with HIGH frontmatter issues.

## Blocked Files

1. Prompts/apple-appstore-reviewer.prompt.md
2. Prompts/create-github-action-workflow-specification.prompt.md
3. Prompts/database.prompt.md
4. Prompts/dev-init.prompt.md
5. Prompts/features.prompt.md
6. Prompts/general.prompt.md
7. Prompts/pl.md
8. Prompts/repo.prompt.md
9. Prompts/workspace-consolidate.prompt.md

## Last Verified Issue

- `docs/audit_results.json` still reports 9 HIGH issues across these files.

## Recovery Guidance

- Repair must be done manually with an exclusive file lock or in a session with no concurrent writers.
- Use strict YAML frontmatter: single `---` open, valid YAML block, closing `---`, then content.
- After repair, rerun `python3 scripts/audit_prompts.py` and confirm HIGH count drops to 0 before resuming `/execute-all-prompts`.

## Session Handoff

- Resume `/prompts/execute-all-prompts.prompt.md` only after these 9 files are verified clean.
- Do not rerun automated frontmatter fixers on this set without exclusive access.
