---
name: prompt-library-de-dup-and-backup-archive
title: Prompt Library De-Dup and Backup Archive
version: 1.0.0
date: 2026-09-13
author: default (Alexa) / Hermes Agent
license: MIT
tags: [audit, de-dup, destructive, archive, prompts, multi-file-change-protocol]
related_skills:
  [
    multi-file-change-protocol,
    user-communication-preferences,
    plans-and-specs,
    writing-clearly-and-concisely,
    subagent-driven-development,
  ]
metadata:
  hermes:
    subgoal: prompt-library-de-dup-and-backup-archive
    artifacts: [plan, spec, script, prompt, audit-md, audit-json, action-log]
    destructive: true (deletes .github/prompts_backup after audit verification)
---

# Prompt Library De-Dup and Backup Archive

## When to Use

When the user asks to audit `.github/prompts` ↔ `.github/prompts_backup`, triage duplicates (filename + content), merge/update, delete backup, and produce full spec/plan/script/skill artifacts.

## Subgoal

`prompt-library-de-dup-and-backup-archive`: audit, merge, archive, artifacts.

## Protocol (audit-first sequential; then parallel artifacts if needed)

1. **Audit** — filename match + MD5 hash (`execute_code` script or `scripts/prompt-library-de-dup-audit.sh`).
2. **Triage** — EXACT_DUP / DIVERGENT / ONLY_PROMPTS / ONLY_BACKUP (see `.hermes/specs/`).
3. **Action** — destructive only after audit: delete/update files; log every action (`prompt-library-de-dup-action-log.md`).
4. **Verify gate** — `.github/prompts_backup` removed; audit logs exist; artifacts present.
5. **Artifacts** — `.hermes/plans/*.md`, `.hermes/specs/*.md`, `scripts/*.sh`, `.hermes/prompts/*.prompt.md`, `skills/*/SKILL.md`.

## Skill Stack (14)

Load in order: multi-file-change-protocol → using-superpowers → brainstorming → user-communication-preferences → mcp-sequential-thinking → mcp-filesystem → mcp-ast-grep → mcp-memory → plans-and-specs → create-implementation-plan → implementation-plan → executing-plans → writing-clearly-and-concisely → subagent-driven-development.

## Verification Checklist

- [ ] `.github/prompts_backup` not present (`not backup_exists`).
- [ ] `.hermes/specs/prompt-library-de-dup-audit.md` exists.
- [ ] `.hermes/plans/prompt-library-de-dup-and-backup-archive-plan.md` exists.
- [ ] `scripts/prompt-library-de-dup-audit.sh` executable.
- [ ] `.hermes/prompts/prompt-library-de-dup-and-backup-archive.prompt.md` exists.
- [ ] Every destructive action logged in `.hermes/specs/prompt-library-de-dup-action-log.md`.
- [ ] No placeholder text in artifacts; SKILL.md ≤250 lines; DRY cross-references enforced.

## Cross-References

- Plan: `.hermes/plans/prompt-library-de-dup-and-backup-archive-plan.md`
- Spec: `.hermes/specs/prompt-library-de-dup-and-backup-archive-spec.md`
- Script: `scripts/prompt-library-de-dup-audit.sh`
- Prompt: `.hermes/prompts/prompt-library-de-dup-and-backup-archive.prompt.md`
- Audit data: `.hermes/specs/prompt-library-de-dup-audit.md` + `.json`

## Pitfalls

- Never delete backup before audit completes (Phase 0 gate).
- Divergent duplicates must be logged with both `OVERWROTE_PROMPTS_WITH_BACKUP` and `DELETED_BACKUP`.
- Only-backup unique files must be migrated (`MIGRATED_TO_PROMPTS`) before deletion.
- Do not invent audit results; always derive from disk state (`os.path.exists`, `hashlib.md5`).
