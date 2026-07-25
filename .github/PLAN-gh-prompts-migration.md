# .github Prompts Migration & Canonicalization Plan

**Status:** In Progress | **Owner:** Alexa | **Created:** 2026-07-23
**Profile:** `exec-assistant`
**Scope:** `.github/` prompt library, legacy Hermes prompts, cross-references, duplicates

---

## Goal

Make `.github/` the single source of truth for all prompt-family assets, migrate any remaining Hermes legacy prompts, fix path/folder issues, dedupe exact bodies, and verify the result on disk.

## Existing Plans Reviewed

| Plan | Role | Status |
| ------ | ------ | -------- |
| `.hermes/plans/2026-06-30-execution-plan-for-prompt-and-plan-normalization.md` | Meta-normalization template | Stale/duplicate frontmatter |
| `projects/Bash/PLAN.md` | Bash toolkit roadmap | Active, separate scope |
| `projects/Bash/SPECS.md` | Bash toolkit specs | Active, separate scope |

## Verified Current State

| Source | Count | Notes |
| -------- | ------- | ------- |
| `.github/prompts/` | 1133 files | Canonical; agents, instructions, archived |
| `%LOCALAPPDATA%\hermes\prompts` | 211 `.prompt.md` | Legacy; not yet migrated |
| Exact duplicates in `.github/prompts` | 0 | By body hash |
| Exact duplicates in legacy prompts | 0 | By file hash |

## Phases

### Phase 1: Audit & Gap Analysis

- [ ] Enumerate legacy `%LOCALAPPDATA%\hermes\.github/prompts/*.prompt.md`
- [ ] Compare against `.github/prompts/` by normalized body hash
- [ ] Identify path/folder issues in `.github/` files
- [ ] Classify each legacy prompt: migrate / archive / delete

### Phase 2: Migration & Dedupe

- [ ] Migrate missing legacy prompts to `.github/prompts/`
- [ ] Consolidate any exact-duplicate bodies; keep one canonical copy
- [ ] Remove orphaned/duplicate references
- [ ] Update `index.md` and `copilot-instructions.md` counts

### Phase 3: Path/Folder Fixes

- [ ] Fix stale paths in `.github/workflows/*.yml`
- [ ] Fix stale paths in `.github/instructions/*.md`
- [ ] Fix stale paths in `.github/*.md`
- [ ] Verify no `Bash/` → `projects/Bash/` and similar stale refs remain

### Phase 4: Enhance & Upgrade

- [ ] Standardize frontmatter across prompt-family files
- [ ] Add missing navigation/index links
- [ ] Validate YAML/JSON in config-like prompts
- [ ] Run lint/format pass on markdown assets

### Phase 5: Verification

- [ ] Re-run exact-duplicate scan post-migration
- [ ] Verify all referenced paths exist
- [ ] Confirm counts in docs match filesystem
- [ ] Git status clean; no stray backup artifacts

## Constraints

- No `.bak`/`.backup`/`.old` files; use git for rollback
- Prefer targeted `patch`/`write_file` over bulk scripts for structured files
- Re-verify after each phase
- Report blockers explicitly; no fabricated outputs

## Success Criteria

- [ ] All legacy Hermes prompts either migrated or intentionally archived
- [ ] Zero exact-duplicate prompt/instruction bodies
- [ ] All path references in `.github/` resolve correctly
- [ ] `index.md` and `copilot-instructions.md` reflect actual counts
- [ ] All verification checks pass on disk
