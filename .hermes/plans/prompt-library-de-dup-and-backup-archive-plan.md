---
goal: prompt-library-de-dup-and-backup-archive (audit, merge, archive, artifacts)
version: 1.0.0
date_created: 2026-09-13
last_updated: 2026-09-13
owner: default (Alexa)
status: In progress
subgoal: audit .github/prompts ↔ .github/prompts_backup; triage exact/near/divergent; merge update + delete backup; produce spec, plan, prompt, script, skill
tags: [multi-file-change-protocol, audit, de-dup, archive, destructive]
---

# Plan — prompt-library-de-dup-and-backup-archive

Status badge: ![In progress](https://img.shields.io/badge/status-in%20progress-yellow)

## 1. Requirements & Constraints

- **REQ-001**: Audit .github/prompts ↔ .github/prompts_backup using filename + content verification.
- **REQ-002**: Triage categories: EXACT_DUP (same basename + same MD5) / DIVERGENT (same basename + different content) / ONLY_PROMPTS / ONLY_BACKUP.
- **REQ-003**: For EXACT_DUP → delete backup file (destructive, approval granted per clarification).
- **REQ-004**: For DIVERGENT → overwrite .github/prompts version with backup version (per user's "update .github/prompts with .github/prompts_backup" directive), then delete backup.
- **REQ-005**: For ONLY_BACKUP (no basename match in prompts) → migrate into .github/prompts (same basename kept), then delete backup; never lose unique backup content.
- **SEC-001**: Before destructive delete of .github/prompts_backup, verify each file action against audit JSON; never delete without logged reason.
- **CON-001**: Multi-file-change-protocol 14-skill stack loaded (plan loaded as substitute for missing `plan`).
- **GUD-001**: DRY enforcement; no duplicate artifacts; all artifacts cross-reference each other.

## 2. Implementation Phases (audit-first sequential; then parallel artifact creation)

### Phase 1 — Audit & Triage (COMPLETE — verified via execute_code)
- GOAL-P1: Build full audit (filename + MD5) of both directories.
- TASK-P1-1: Run audit script → `.hermes/specs/prompt-library-de-dup-audit.md` + `.json`.
- TASK-P1-2: Triage results saved (373 filename duplicates found across 1550 prompts / 676 backups; 29 exact + 21 divergent in first-50 sample).
- GATE-P1: Audit artifacts exist and contain filename-match list.

### Phase 2 — Merge / Refactor Prompts (destructive to backup; updates prompts)
- GOAL-P2: Apply triage rules file-by-file; delete .github/prompts_backup after migration.
- TASK-P2-1: For each EXACT_DUP in audit JSON → delete backup file; log action.
- TASK-P2-2: For each DIVERGENT → copy backup content over prompts file (overwrite); delete backup; log hash change.
- TASK-P2-3: For ONLY_BACKUP files (no basename match) → copy into .github/prompts with same basename; delete backup; log.
- TASK-P2-4: Leave .github/prompts files with only-in-prompts status untouched.
- GATE-P2: .github/prompts_backup directory removed or empty; audit log shows each action; no backup file remains unprocessed.

### Phase 3 — Artifact Creation (parallel subagent-capable phases)
- GOAL-P3-A: `.hermes/plans/prompt-library-de-dup-and-backup-archive-plan.md` (this file) — complete.
- GOAL-P3-B: `.hermes/specs/prompt-library-de-dup-and-backup-archive-spec.md` — spec document with architecture, acceptance criteria, file list.
- GOAL-P3-C: `.github/prompts/` updates — merged/refactored versions (already done by Phase 2 script actions).
- GOAL-P3-D: `scripts/prompt-library-de-dup-audit.sh` — portable audit script.
- GOAL-P3-E: `skills/prompt-library-de-dup-and-backup-archive/` — SKILL.md (new skill for future reuse).
- GOAL-P3-F: `.hermes/prompts/prompt-library-de-dup-and-backup-archive.prompt.md` — implementation prompt (execution commands) for this subgoal.
- GATE-P3: All artifacts present; cross-references verified; no placeholder text; SKILL.md ≤250 lines; script executable.

### Phase 4 — Final Gate & Verification
- GATE-FINAL: `.github/prompts_backup` deleted; all audit actions logged; artifacts verified; git status clean; user told to confirm.

## 3. Alternatives
- ALT-001: Skip audit → bulk delete backup. Rejected: violates verification-before-claim + could lose divergent content.
- ALT-002: Keep backup alongside prompts. Rejected: user's explicit instruction is delete backup after merging.

## 4. Dependencies
- DEP-001: Multi-file-change-protocol skill loaded (verified).
- DEP-002: .github/prompts and .github/prompts_backup exist (verified via terminal ls).
- DEP-003: Scripts dir (`scripts/`) available.

## 5. Files Affected
- FILE-001: `.github/prompts/*` (updated by Phase 2; some overwritten by backup content).
- FILE-002: `.github/prompts_backup/*` (deleted by Phase 2 after audit).
- FILE-003: `.hermes/plans/prompt-library-de-dup-and-backup-archive-plan.md` (this file).
- FILE-004: `.hermes/specs/prompt-library-de-dup-and-backup-archive-spec.md`.
- FILE-005: `.hermes/specs/prompt-library-de-dup-audit.md` + `.json`.
- FILE-006: `scripts/prompt-library-de-dup-audit.sh`.
- FILE-007: `skills/prompt-library-de-dup-and-backup-archive/SKILL.md`.
- FILE-008: `.hermes/prompts/prompt-library-de-dup-and-backup-archive.prompt.md`.

## 6. Testing / Verification Gates
- TEST-001: Audit artifacts exist (`os.path.isfile` verified).
- TEST-002: For every deleted backup file, audit JSON logs basename + action.
- TEST-003: `.github/prompts_backup` directory removed (`os.path.exists` = False after Phase 2).
- TEST-004: All new artifacts reference subgoal name and cross-reference each other.

## 7. Risks & Assumptions
- RISK-001: Divergent duplicates could overwrite newer prompt versions with older backup versions. Mitigation: user explicitly directed to use backup versions; log hash difference so rollback is possible via git.
- RISK-002: Large file count (676 backup files) → execution time. Mitigation: script runs sequentially; no subagent needed for destructive phase since audit-then-act is sequential.
- ASSUMPTION-001: User has approved destructive ops (confirmed in clarification turn 3: "all destructive operations approved").
