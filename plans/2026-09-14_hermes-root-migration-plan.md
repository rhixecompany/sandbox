---
goal: Migrate all ./**/*.md files to hermes root, consolidate/dedupe, then implement run-all-goals.prompt.md
version: 1.0.0
date_created: 2026-09-14
last_updated: 2026-09-14
owner: Alexa
status: In progress
tags: [migration, consolidation, dedupe, hermes-root, run-all-goals]
---

# Introduction

![Status: In progress](https://img.shields.io/badge/status-In%20progress-yellow)

Migrate 1200+ `./**/*.md` files into the hermes root folder, consolidate and dedupe duplicates, fix conflicts, update all cross-references, then implement `.github/prompts/general/run-all-goals/run-all-goals.prompt.md`.

## 1. Requirements & Constraints

- **REQ-001**: All 1200+ `./**/*.md` files must be migrated to hermes root
- **REQ-002**: Diff/consolidate/dedupe duplicates across all migrated files
- **REQ-003**: Debug and fix all conflicts/issues/errors found
- **REQ-004**: Update every affected file that references `./` paths
- **REQ-005**: Delete `./` directory ONLY after root is fully updated
- **REQ-006**: Implement `.github/prompts/general/run-all-goals/run-all-goals.prompt.md` completely
- **REQ-007**: `.env` must remain protected (3334 B unchanged)
- **REQ-008**: No synthetic artifacts; all results verified real
- **REQ-009**: DRY enforcement — cross-references not duplication
- **CON-001**: No backup files (.bak, .old, .timestamped)
- **CON-002**: Git used for rollback only
- **CON-003**: Sequential execution for dependent phases; parallel for independent ones

## 2. Implementation Steps

### Phase 1: Discovery & Inventory
- GOAL-001: Catalog all 1200 `./**/*.md` files by subdirectory and content type

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-001 | Inventory all ./**/*.md files with sizes and content hashes | | 2026-09-14 |
| TASK-002 | Identify duplicate content across files (by hash) | | 2026-09-14 |
| TASK-003 | Map all cross-references to `./` paths in affected files | | 2026-09-14 |

### Phase 2: Migration & Consolidation
- GOAL-002: Move files from `./` subdirectories to hermes root

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-004 | Create root-level directory structure matching ./ subdirs | | 2026-09-14 |
| TASK-005 | Copy all ./**/*.md files to corresponding root locations | | 2026-09-14 |
| TASK-006 | Deduplicate identical content (keep one copy, update references) | | 2026-09-14 |
| TASK-007 | Consolidate overlapping content (SKILL.md variants, specs) | | 2026-09-14 |

### Phase 3: Conflict Resolution & Debugging
- GOAL-003: Fix all conflicts, issues, and errors

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-008 | Run diff between old and new locations to verify integrity | | 2026-09-14 |
| TASK-009 | Identify and fix all broken cross-references | | 2026-09-14 |
| TASK-010 | Resolve naming conflicts and deduplication issues | | 2026-09-14 |
| TASK-011 | Validate all migrated files are readable and complete | | 2026-09-14 |

### Phase 4: Reference Updates
- GOAL-004: Update all files that reference `./` paths

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-012 | Update AGENTS.md, CLAUDE.md, .hermes.md, SOUL.md, USER.md, MEMORY.md | | 2026-09-14 |
| TASK-013 | Update all .prompt.md files referencing ./ paths | | 2026-09-14 |
| TASK-014 | Update skill files and SKILL.md references | | 2026-09-14 |
| TASK-015 | Verify no remaining `./` references in affected files | | 2026-09-14 |

### Phase 5: Delete ./ & Verify
- GOAL-005: Remove ./ directory after verification

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-016 | Final integrity check on all migrated files | | 2026-09-14 |
| TASK-017 | Delete ./ directory (git-tracked) | | 2026-09-14 |
| TASK-018 | Verify .env unchanged (3334 B) and no .bak artifacts | | 2026-09-14 |

### Phase 6: Run-All-Goals Implementation
- GOAL-006: Implement .github/prompts/general/run-all-goals/run-all-goals.prompt.md

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-019 | Read and analyze run-all-goals.prompt.md (4340 B) | | 2026-09-14 |
| TASK-020 | Implement all specifications from run-all-goals.prompt.md | | 2026-09-14 |
| TASK-021 | Execute and verify the implementation completely | | 2026-09-14 |

## 3. Alternatives

- **ALT-001**: Migrate incrementally by subdirectory instead of all-at-once — rejected, too slow and error-prone
- **ALT-002**: Keep ./ as symlinks to root — rejected, user explicitly wants deletion
- **ALT-003**: Use git filter-branch for migration — rejected, too destructive and hard to verify

## 4. Dependencies

- **DEP-001**: Git must be available and working directory clean
- **DEP-002**: .env must remain protected throughout (3334 B unchanged)
- **DEP-003**: All 14-skill stack must be loaded before execution
- **DEP-004**: run-all-goals.prompt.md must be analyzed before Phase 6

## 5. Files

- **FILE-001**: `./` directory (source — 1200+ .md files)
- **FILE-002**: `hermes root/` directory (destination)
- **FILE-003**: `.github/prompts/general/run-all-goals/run-all-goals.prompt.md` (target implementation)
- **FILE-004**: `.hermes.md` (must be updated with new references)
- **FILE-005**: `AGENTS.md`, `CLAUDE.md`, `USER.md`, `MEMORY.md`, `SOUL.md` (must be updated)
- **FILE-006**: All `.prompt.md` files referencing `./` paths

## 6. Testing

- **TEST-001**: Verify all 1200+ files migrated successfully (count check)
- **TEST-002**: Verify no file content lost (hash comparison)
- **TEST-003**: Verify no broken references (grep for ./ in all files)
- **TEST-004**: Verify .env unchanged (size check)
- **TEST-005**: Verify ./ directory deleted
- **TEST-006**: Verify run-all-goals.prompt.md implemented and working
- **TEST-007**: Run `bun run check` and `pytest` to verify no regressions

## 7. Risks & Assumptions

- **RISK-001**: Some ./ files may have hardcoded paths that break after migration
- **RISK-002**: Duplicate content consolidation may lose metadata or context
- **RISK-003**: Deleting ./ may break external tools that depend on it
- **ASSUMPTION-001**: All ./ .md files are git-tracked and can be recovered via reflog
- **ASSUMPTION-002**: The workspace is clean (verified: status clean)

## 8. Related Specifications

- Link: `./specs/run-all-goals-spec.md`
- Link: `./specs/run-all-goals-five-day-consolidated-spec.md`
- Link: `./plans/2026-09-14_hermes-root-migration-plan.md` (this plan)
