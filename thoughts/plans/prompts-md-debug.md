# prompts-md — Fix Plan

Created: 2026-06-12
Target scope: `Prompts/*.md` (9 files)
Source issues: `docs/prompts-md-issues-context.md`

## Goal

Repair prompt files with the smallest safe change set: normalize bad skill/dependency formatting, fix incomplete sections, and correct frontmatter copy errors. Do not rewrite content strategy or split `workspace-consolidate.prompts.md`.

## Batch Assignments

- Batch 1: agents-fix, bash-scripts-fix, dev-init, general, prompts-fix
- Batch 2: repo-management, repo, skills-fix, workspace-consolidate

## Plan Items

1. Replace malformed `skills:` bullets with plain skill names across Batch 1.
2. Fix truncated skill section in `prompts-fix.prompts.md`.
3. Remove the empty `## Phase 3` heading in `dev-init.prompts.md`.
4. Expand or normalize the "three ecosystems" wording in `agents-fix.prompts.md`.
5. Resolve the stale in-body plan archive reference in `bash-scripts-fix.prompts.md` or mark it conditional.
6. Add missing section headings to `general.prompts.md` for tooling parity.
7. Correct frontmatter copy duplication in `prompts-fix.prompts.md` ("prompt prompts").

## Progress Log

- 2026-06-12: Plan created; Batch 1 application started.

## Status

In progress.
