# Prompts/Templates Consolidation Master Plan

> **Scope:** canonicalize the prompt library under `prompts/`, migrate the root `templates/` tree into `prompts/templates/`, deduplicate/normalize conflicting template files, and validate prompt references, skills, scripts, and toolset declarations.
>
> **Supersedes for this scope:**
>
> - `.hermes/plans/2026-06-30_171919-prompt-orchestration-comprehensive-plan.md`
> - `.hermes/plans/2026-06-30-execution-plan-for-prompt-and-plan-normalization.md`
> - `.hermes/plans/2026-06-30_enhance-markdown-full-pass.md`
> - `.hermes/plans/2026-06-30_171919-sandbox-aggressive-cleanup-plan.md`
>
> **Current inventory snapshot (2026-07-10):**
>
> - `templates/` (root): 25 files
> - `prompts/templates/`: 27 files
> - shared relative paths: 23
> - identical relative paths: 17
> - differing relative paths: 6
> - root-only files: 2
> - prompts-only files: 4
> - prompt files with template references: 199
> - `../templates/` link targets found in prompt files: 170 occurrences
>
> **User approval:** destructive cleanup approved in-chat.

## Goal

Make `prompts/` the single source of truth for prompt assets.

## Non-Goals

- Do not touch unrelated project folders outside prompt/template/validation assets.
- Do not rewrite unrelated user work in the current dirty tree.
- Do not delete any asset before the migrated replacement exists and references are verified.

## Phase 0: Baseline Snapshot

**Objective:** capture the current state before migration.

**Tasks**

- [x] Record `git status --short` and note unrelated modified files.
- [x] Inventory root `templates/` vs `prompts/templates/`.
- [x] Inventory prompt files that reference `../templates/`.
- [x] Identify filename conflicts, Unicode-hyphen variants, and stub placeholders.

**Acceptance**

- Baseline counts are documented.
- Canonical source/target decision is explicit.

## Phase 1: Canonicalize `prompts/templates/`

**Objective:** promote the prompt-side template tree to the canonical location.

**Tasks**

- [x] Copy/overwrite prompt-side stubs with the full content from the root `templates/` tree.
- [x] Normalize the `test-providers-models` phase filenames to ASCII canonical names.
- [x] Ensure `prompts/templates/test-providers-models/` matches the full root content.
- [x] Update `prompts/test-providers-models.prompt.md` to reference canonical filenames.

**Acceptance**

- `prompts/templates/` contains the full template bodies.
- No stub placeholders remain in the migrated template family.
- Canonical names are consistent across prompt and template files.

## Phase 2: Migrate References

**Objective:** make every prompt reference resolve inside `prompts/`.

**Tasks**

- [x] Replace `../templates/` link targets with `templates/`.
- [x] Normalize visible path labels where they still mention the root `templates/` tree.
- [x] Search for any remaining `../templates/` references across `prompts/*.prompt.md`.
- [x] Verify all `templates/...` references resolve to `prompts/templates/...`.

**Acceptance**

- No prompt file points to the root `templates/` tree.
- All template references resolve from the prompt directory.

## Phase 3: Retire Root `templates/`

**Objective:** remove the duplicate root tree after reference migration is complete.

**Tasks**

- [x] Verify root `templates/` is no longer referenced.
- [x] Delete or archive the root `templates/` tree with git-tracked removal.
- [x] Confirm only `prompts/templates/` remains as the template source.
- [x] Clean up any empty directories left behind.

**Acceptance**

- Root `templates/` is gone or reduced to zero relevant files.
- No duplicate template tree remains.

## Phase 4: Enhance Prompt Files

**Objective:** tighten prompt structure and remove conflicting or stale instructions.

**Tasks**

- [x] Normalize frontmatter fields and tags.
- [x] Remove duplicate/conflicting sections in prompt bodies.
- [x] Standardize shared rule references and section ordering.
- [x] Keep prompt intent intact while trimming boilerplate.

**Acceptance**

- Prompt files are consistent, concise, and self-contained.
- Shared references are DRY and correct.

## Phase 5: Validate Prompts, Skills, Scripts, and Toolsets

**Objective:** ensure all referenced assets resolve and are structurally valid.

**Tasks**

- [x] Run prompt frontmatter validation.
- [x] Verify `skill:` / `prompt:` references resolve.
- [x] Inventory referenced scripts and toolsets from prompts.
- [x] Flag any broken or missing skill/script/tool references for repair.

**Acceptance**

- Validation passes with no unresolved prompt dependencies.
- Any required skill/script/toolset references are either present or explicitly documented as intentionally absent.

## Phase 6: Final Verification

**Objective:** prove the tree is clean and the migration is complete.

**Tasks**

- [x] Re-run `git status --short` and compare against baseline.
- [x] Search for `../templates/` and root `templates/` references.
- [x] Confirm the prompt/template families load from `prompts/` only.
- [x] Document the final result in a report artifact.

**Acceptance**

- Zero broken template references.
- Zero duplicate template trees.
- Validation artifacts and final status are documented.

## Risks & Mitigations

| Risk                              | Mitigation                                                                          |
| --------------------------------- | ----------------------------------------------------------------------------------- |
| Existing dirty worktree           | Only touch prompt/template assets required by this scope; preserve unrelated edits. |
| Mixed filename variants           | Normalize filenames before deleting old copies.                                     |
| Broken references after migration | Search/verify after every batch; do not delete root files first.                    |
| Large batch edits drift           | Work in small batches and re-validate after each batch.                             |
| Windows/MSYS path confusion       | Use paths relative to repo root and verify with searches, not assumptions.          |

## Deliverables

1. Prompts/Templates Consolidation Master Plan
	1. Goal
	2. Non-Goals
	3. Phase 0: Baseline Snapshot
	4. Phase 1: Canonicalize `prompts/templates/`
	5. Phase 2: Migrate References
	6. Phase 3: Retire Root `templates/`
	7. Phase 4: Enhance Prompt Files
	8. Phase 5: Validate Prompts, Skills, Scripts, and Toolsets
	9. Phase 6: Final Verification
	10. Risks \& Mitigations
	11. Deliverables
