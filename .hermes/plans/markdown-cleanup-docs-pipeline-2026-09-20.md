# Plan: Markdown Cleanup and Docs Pipeline Feature

**Feature**: A markdown cleanup and docs pipeline feature.
**What it does**: Cleans up empty subfolders and trims whitespace in markdown files at repo root, docs/, .github/; creates docs/document.md and docs/project-docs/.
**Who it's for**: Workspace maintainers and agents that rely on clean docs.

## Pipeline (sequential)

1. LOAD — verify 14-stack access (scope, multi-file-crud-protocol loaded; others checked)
2. MEMORY — context saved (markdown cleanup feature, 2026-09-20)
3. PLAN — this file
4. VERIFY — clarifications complete (new feature; cleanup = delete empty dirs + trim .md whitespace; docs targets = docs/document.md + docs/project-docs/)
5. EXECUTE — sequential phases:
   - Phase A: /scope (new feature scope file)
   - Phase B: /architect (spec for feature)
   - Phase C: /audit (work audit of .md files)
   - Phase D: /develop (build docs artifacts)
   - Phase E: Cleanup (delete empty subfolders, trim whitespace)
   - Phase F: Verify gates

## Gates

- [ ] Scope file exists at docs/scope/ with feature table
- [ ] Architect spec exists
- [ ] Audit report exists (counts of .md files, empty dirs)
- [ ] docs/document.md exists and non-empty
- [ ] docs/project-docs/ exists with content
- [ ] Cleanup completed: no empty subfolders remain in root/docs/.github; whitespace trimmed in .md files (verified with `find` + `grep` or `python`)
- [ ] No .env secrets exposed; .env untouched
- [ ] Integrity verified

## Evidence (real, not fabricated)

- File counts from `ls` and `find` commands
- Exit codes from `find`/`grep` verification commands
- No synthetic session IDs, capabilities, rankings, or artifacts
