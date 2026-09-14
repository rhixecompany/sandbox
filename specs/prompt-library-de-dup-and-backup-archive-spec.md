---
goal: prompt-library-de-dup-and-backup-archive subgoal implementation
version: 1.0.0
date: 2026-09-13
owner: default
status: In progress
dependencies: multi-file-change-protocol, user-communication-preferences, plans-and-specs, writing-clearly-and-concisely, subagent-driven-development
---

# Spec — prompt-library-de-dup-and-backup-archive

## Overview
Audit, triage (filename + content hash), merge/update, delete `.github/prompts_backup`, and produce full artifact bundle (plan, spec, script, skill, prompt).

## Acceptance Criteria
1. `.hermes/specs/prompt-library-de-dup-audit.md` exists with filename-match count, exact/near/divergent counts, only-prompts / only-backups lists.
2. `.github/prompts_backup/` removed; no file remains in it.
3. Every deleted backup file is logged in audit JSON (basename, action `DELETED_BACKUP` or `MIGRATED_THEN_DELETED`).
4. Every divergent file is overwritten in prompts (action `OVERWROTE_PROMPTS_WITH_BACKUP`) then deleted.
5. Every only-backup unique file copied into `.github/prompts/` (action `MIGRATED_TO_PROMPTS`) then deleted.
6. Artifacts: `.hermes/plans/*.md`, `.hermes/specs/*.md`, `scripts/*.sh`, `skills/*/SKILL.md`, `.hermes/prompts/*.prompt.md` all present and cross-referenced.

## Architecture
```
Audit (audit script) → Triage JSON → Action script (merge/delete) → Verification gate → Artifact generation
```
Sequential dependency: audit must complete before destructive phase.
Parallel phases (after audit): artifacts (plan/spec/prompt/script/skill) can be built in parallel, but since the user wants comprehensive artifacts, we'll create sequentially for verification.

## Triage Rules (implemented in script)
| Category | Filename match? | Content hash equal? | Action | Log entry |
|---|---|---|---|---|
| EXACT_DUP | Yes | Yes | Delete backup | `DELETED_BACKUP` |
| DIVERGENT | Yes | No | Overwrite prompts with backup content; delete backup | `OVERWROTE_PROMPTS_WITH_BACKUP` + `DELETED_BACKUP` |
| ONLY_PROMPTS | No (in prompts only) | N/A | Keep prompts; no action | `KEPT_PROMPTS_ONLY` |
| ONLY_BACKUP | No (in backup only) | N/A | Copy to prompts; delete backup | `MIGRATED_TO_PROMPTS` + `DELETED_BACKUP` |

## File List (Artfacts)
- `.hermes/plans/prompt-library-de-dup-and-backup-archive-plan.md`
- `.hermes/specs/prompt-library-de-dup-and-backup-archive-spec.md` (this file)
- `.hermes/specs/prompt-library-de-dup-audit.md`
- `.hermes/specs/prompt-library-de-dup-audit-data.json`
- `scripts/prompt-library-de-dup-audit.sh`
- `skills/prompt-library-de-dup-and-backup-archive/SKILL.md`
- `.hermes/prompts/prompt-library-de-dup-and-backup-archive.prompt.md`

## Verification (final gate)
- [ ] `.github/prompts_backup` not present (`os.path.exists` false)
- [ ] `.hermes/specs/prompt-library-de-dup-audit.md` readable
- [ ] Each artifact references subgoal name and cross-links to at least one other artifact.
- [ ] No placeholder text in SKILL.md or spec.
