---
name: hermes-operator-policies
title: "Hermes Operator Policies & Workspace Conventions"
description: "Operator-level policies and short how-to references for safe automation: backup policy, memory edits, deletion policy, validation scripts, cron jobs, and user preferences (PowerShell, overwrite vs backup)."
author: Alexa
created: 2026-05-26
version: 1.0
triggers:
  - "operator policies"
  - "memory policy"
  - "hermes policies"
---

# Hermes Operator Policies & Workspace Conventions

## Purpose

- Capture durable operator decisions and user preferences discovered during sessions so automation and skills behave predictably.

## When to use

- Any automation that edits local files under the Hermes home
- Creating or removing backups
- Scheduling cron jobs that act on local files
- Writing or patching skills that modify memory files

## Core policies

- **Backup policy (ENFORCED)**: NEVER create .bak, .backup, .old, or timestamped backup files when editing existing files. Update files directly via write_file() or patch(). Git is the backup system — use git branches or ask user before destructive changes. Exception: NONE. This rule applies to all Hermes automation, skills, and agent workflows. See SOUL.md for detailed enforcement rules and git-first workflow.
- Deletion policy: irreversible deletions require explicit user confirmation. When the user requests permanent deletion, perform it immediately only after confirming the user intent in-session (not via email/PR). Record the action in logs (append to .hermes_history).
- Trash behavior: when enabled, automation should move removed artifacts to C:\\Users\\Alexa\\AppData\\Local\\hermes\\trash first. Periodic cleanup is allowed only after explicit user request.
- Memory edits: USER.md and MEMORY.md are authoritative. When editing them, write in-place (no .bak) and ensure fields follow the canonical Key: Value form (Name:, OS:, Editor/IDE:, Shell preference:, Active model:). Run the validate_memories.py script after edits and include its output in the action report.
- Shell preference: prefer PowerShell equivalents for local user-facing commands on Windows. If a script runs in bash context, also provide a one-line PowerShell alternative in the report.
- Cron jobs: scripts scheduled under Hermes must live in C:\\\\Users\\\\Alexa\\\\AppData\\\\Local\\\\hermes\\\\scripts and be referenced by filename only (no `scripts/` prefix).
  ⚠ PITFALL: The `scripts/` prefix in the cronjob `script` field causes a double-prefix (`.../scripts/scripts/foo.py`) and a "Script not found" error. Use just `foo.py` — paths are resolved relative to `~/AppData/Local/hermes/scripts/`.
  ⚠ PITFALL: `deliver=origin` fails when no messaging platform is configured. Use `deliver=local` for silent local execution, or omit for auto-detection.
- Session management: `hermes sessions` commands manage the SQLite session DB. Pruning sessions does NOT automatically reclaim disk space — VACUUM is required. See `references/session-cleanup.md`.
- Skills hub installation: `hermes skills install <identifier> --yes` to skip interactive confirmation (required for batch/automated installs). Flow: fetch → quarantine → security scan → verdict → install. Official builtin skills still get scanned (DANGEROUS verdict common for skills handling tokens/credentials — expected, not a block). See `references/hub-skills-install.md` for full recipe and pitfall catalog.

## Files & scripts (pointers)
- Validation script: scripts/validate_memories.py — run after memory edits, return code must be recorded.
- Policy file: C:\\\\Users\\\\Alexa\\\\AppData\\\\Local\\\\hermes\\\\.hermes_policies
- Cron job: daily-validate-memories (cron_validate_memories.py)
- Reference: references/session-cleanup.md — session prune, delete, and DB VACUUM recipe

Operator checklist (pre-edit)
1. ~~Read .hermes_policies and honor backup.strategy~~ NEVER CREATE BACKUPS (git is version control)
2. Confirm user intent for destructive ops
3. Run validate_memories.py after memory edits
4. Append an entry to .hermes_history documenting the change
5. Use direct write_file() or patch() — no .bak/.backup/.old files ever

---

## References

- references/memory-policy.md — actionable recipe for agents and automation to follow when editing memories and backups.


## When to Use

- When performing hermes operator policies operations or tasks
- When managing hermes operator policies infrastructure or configurations
- When automating or debugging hermes operator policies workflows
- **Triggers**: "set up devops/hermes-operator-policies", "configure hermes operator policies", "debug hermes operator policies issue"

## Workflow

### Phase 1: Setup

Verify prerequisites and ensure required dependencies are available.

### Phase 2: Execute

Perform the hermes operator policies operations following the instructions in this skill.

### Phase 3: Verify

Confirm the output meets expectations and address any issues.

### Phase 4: Document

Record any changes, configurations, or decisions made during execution.

## Verification Checklist

- [ ] Prerequisites verified and available
- [ ] Hermes Operator Policies operations completed successfully
- [ ] Configuration or output verified against requirements
- [ ] No errors or warnings during execution
- [ ] Changes documented and committed if applicable

## Overview

Hermes Operator Policies is a skill for handling hermes operator policies tasks and automation workflows. Use this skill when you need to perform hermes operator policies operations efficiently.

