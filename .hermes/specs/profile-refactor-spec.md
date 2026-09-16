---
name: profile-refactor-spec
title: Profile Refactor Spec — Feature-Doc Synthesis
version: 1.0.0
---
# Implementation Spec
## Source
- Feature docs: docs/features/*.md (8 real .md files, stat-confirmed, frontmatter verified)
- Profile identity: ~/AppData/Local/hermes/profiles/*/ (15 profiles: SOUL.md/USER.md/MEMORY.md verified by cat, not synthetic 0-byte)
- Workspace identity reference: workspace root SOUL.md (25 lines) / USER.md (61 lines) / MEMORY.md (40 lines)
## Requirements
- Read feature docs; synthesize unified theme mapping (DRY, shared identity + profile customization at routing/model/provider only).
- Read profile identity files; backup originals (.orig in .hermes/plans/backups/profiles/).
- Generate enhanced profile identity copies (.hermes/plans/refactored/<profile>_*.md) incorporating feature concepts.
- Verify artifacts with real file-system checks (stat/diff/read); no synthetic data.
- Enforce DRY (single synthesis reference) + best practices (read→patch→verify; native equivalents for unavailable skills; honest blocker reporting).
## Acceptance Criteria
- [ ] Synthesis artifact present (.hermes/plans/profile-refactor-synthesis.md) with 8 feature concepts.
- [ ] Enhanced profile identity artifacts exist for default (verified); pattern documented for remaining 14 profiles.
- [ ] Backups verified (originals preserved; no destructive overwrite without verification).
- [ ] Bundle artifacts present: spec + prompt + skill + script + result + verification.
- [ ] No synthetic session IDs / fabricated capabilities / hidden errors.
- [ ] Scripts syntax verified (bash -n / python -m py_compile PASS); DRY (single FEATS/template reuse); clean.
