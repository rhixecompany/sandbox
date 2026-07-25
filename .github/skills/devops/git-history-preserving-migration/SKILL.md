---
author: Alexa
description: Procedures, templates, and scripts for migrating projects between local
  directories while preserving git history and providing safe rollback.
license: MIT
name: git-history-preserving-migration
tags:
- imported
title: Git History Preserving Migration
version: 1.0.0

---
# Git-history-preserving-migration

## Purpose

- Provide a repeatable, safe, Windows-friendly workflow for migrating projects (single repos or folders) from one local path to another while preserving git history when present.
- Capture pitfalls and proven fixes from recent real-world runs: robust manifest parsing, quoting/escaping when generating files, backup-before-destructive-change, and a PowerShell-first execution path for Windows environments.

## When to use

- Migrating many projects between local directories or consolidating multiple repositories into a single target layout.
- Needing to preserve git history when moving repositories.
- Running unattended per-project operations but pausing on conflicts or failures.

## Key principles (user preferences embedded)
- Preserve git history by default when the source contains a .git directory.
- On Windows, prefer PowerShell Copy-Item (or Move-Item on explicit request) for file operations when the user has requested that instead of invoking git clone; provide the exact PowerShell commands as templates.
- Always create a backup (zip / Compress-Archive) of the target before any destructive change.
- Proceed project-by-project and pause only on unresolvable conflicts (git merge conflicts, git clone failure, permission errors).
- Create non-destructive per-project decision files for human review before executing destructive steps.

High-level workflow
1. Discovery: read a machine-readable manifest or parse a triage markdown file. Prefer explicit JSON/YAML manifests, but if parsing markdown, use robust regexes and fallbacks.
2. Decision: for each project, produce a decision file containing: action (create/copy/clone/overwrite/skip), source path, target path, rationale, and planned commands (explicit PowerShell commands on Windows).
3. Review: present decisions for approval (index file and per-project files). Do not change files yet.
4. Execution (after approval): for each project in order:
   a. Backup target (if present): Compress-Archive or create zip via a reproducible script.
   b. If action = create and source has .git:
      - Option A (preserve history, default): run `git clone <src> <tgt>` when the user prefers git clone.
      - Option B (Windows-preferred copy): run `Copy-Item -Path '<src>' -Destination '<tgt>' -Recurse -Force` (non-destructive) and then `git init` + graft commit metadata only if history preservation isn't possible.
   c. If action = overwrite: remove target (Remove-Item) then re-run the create step.
   d. If source is non-git: copy tree then git init & initial commit (policy-based).
   e. Run verification steps (git log top entries, run linters/tests if configured) and write verification artifacts.
   f. If conflict or error occurs, stop and record logs for human decision.

Pitfalls & fixes (learned from session)
- read_file usage: tool returns a dict; always check for the 'content' key before indexing. If missing, re-read with a larger limit or fail gracefully with an explanatory decision file.
- Manifest parsing: avoid a single strict json.loads on an extracted markdown block. Use heuristics: search for a fenced ```json block, trim surrounding text, and if json.loads fails with Extra data, try a tolerant parser or split the block by balanced braces/brackets. Provide a fallback to parse a comma-separated line of project names.
- Markdown output quoting: when programmatically writing decision/markdown files, do not embed unescaped triple backticks or unbalanced quotes inside Python f-strings. Use write_file with plain triple-quoted strings or templates; escape user content.
- Regex fragility: Windows paths with backslashes require careful regex patterns; prefer matching inside quotes and use non-greedy groups.
- PowerShell vs git: Respect explicit user preference to use PowerShell Copy/Move on Windows; store recommended commands in templates.
- Commit-script generation pitfalls: When generating commit scripts programmatically, avoid placing raw backslashes inside Python f-strings; this caused a live SyntaxError ("f-string expression part cannot include a backslash") in an early run. Use raw strings, pre-computed replacements (e.g. path.replace('/', '\\')), or build strings with concatenation so backslashes are not part of the evaluated expression. Output both PowerShell and Bash variants and validate them before execution.
- Safe batch size: During automated mass edits we used a conservative batch size of 7 files. Record batch-size as a recommended default for large automated edits to keep each commit reviewable and to reduce blast radius.
- Non-destructive defaults: Scripts should create backups under docs/skills-backups/ (or a configurable backups/ path) before modifying files. Always write a human-readable decision file and per-file .bak before making in-place edits.
- Commit approval policy: The toolchain should generate commit scripts for review; do NOT run git commit or push without explicit human approval. Include an option in scripts to run in dry-run mode and a separate run mode that commits — default to dry-run unless the user explicitly requests commit-and-commit.
- Post-edit verification: After automated edits, run validators and produce docs/skills-merge-verify.md containing per-file verification entries (what was changed, backup path, verification checks performed). Keep the verification artifacts alongside backups.



Verification & rollback
- Each executed step must produce:
  - A backup ZIP path (absolute) recorded in the decision file and migration log.
  - A verification file that contains the top-level git log (if any) and a pass/fail for smoke tests (if present).
- Rollback is simply: uncompress the backup zip to restore the target; provide the exact PowerShell command in the verification file for convenience.

Files provided by this skill
- references/decision-template.md — canonical per-project decision template (editable).
- references/parsing-and-quoting-pitfalls.md — concise notes about parsing and quoting pitfalls encountered and how to avoid them.
- references/5-phase-repo-migration-pattern.md — comprehensive 5-phase workflow for multi-repository consolidation with patch application, documentation-first orchestration, and zero data loss verification (validated 2026-05-27).
- references/patch-classification-and-debugging.md — systematic git patch classification (pre-applied, applied, missing-target, obsolete) with commit SHA verification workflow.
- scripts/powershell-backup-and-copy.ps1 — a reusable PowerShell script that creates backups and copies/moves content safely.

Usage examples
- Non-destructive: run discovery -> generate decision files -> review index -> execute approved decisions.
- Dry-run: generate commands and write them into decision files without running them.

Maintenance
- Add new references when you encounter additional environment-specific quirks.
- Patch the script if Compress-Archive semantics change on future Windows versions.

## Workflow

### Phase 1: Setup

Verify prerequisites and ensure required dependencies are available.

### Phase 2: Execute

Perform the git history preserving migration operations following the instructions in this skill.

### Phase 3: Verify

Confirm the output meets expectations and address any issues.

### Phase 4: Document

Record any changes, configurations, or decisions made during execution.


## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist

- [ ] Prerequisites verified and available
- [ ] Git History Preserving Migration operations completed successfully
- [ ] Configuration or output verified against requirements
- [ ] No errors or warnings during execution
- [ ] Changes documented and committed if applicable

## Overview

Git History Preserving Migration is a skill for handling git history preserving migration tasks and automation workflows. Use this skill when you need to perform git history preserving migration operations efficiently.
```
