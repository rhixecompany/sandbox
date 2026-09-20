---
title: Goal 3 — Skills Dedupe + Judge ≥90 + Debug Ascending-Modified
status: "in_progress"
created: 2026-09-11
applies_to: ~/AppData/Local/hermes/skills/
trigger_threshold: >6 file changes → load multi-file-change-protocol (this plan)
---

# Goal 3 — Skills Dedup + Judge + Debug

## Decision Lock (from clarifications)

| Decision       | Value                                                                           |
| -------------- | ------------------------------------------------------------------------------- |
| Pipeline scope | FULL end-to-end (list → dedupe → judge ≥90 → debug ascending-modified)          |
| Judge method   | Existing `skill-judge` skill via Hermes CLI / `batch-skill-judge` (development) |
| Batch size     | ≤5 skills per turn                                                              |
| Order          | ascending by `hermes skills list-modified`                                      |

## Discovery (current state)

| Metric                                         | Value                              |
| ---------------------------------------------- | ---------------------------------- |
| Total installed skills (`hermes skills list`)  | **~1,120** (1,123 rows − 3 header) |
| User-modified bundled skills (`list-modified`) | **32**                             |
| `skill-judge` skill                            | local, enabled                     |
| `batch-skill-judge` skill                      | development category, enabled      |
| Existing `dedupe-skills` skill                 | patched this session               |

## Phase 1 — Capture Initial State

```bash
hermes skills list > initial-skills.txt
wc -l initial-skills.txt  # record baseline
```

**Gate 1.1:** `initial-skills.txt` exists with line count.

## Phase 2 — Identify Duplicates

Parse `initial-skills.txt`:

1. Extract `Name` column (truncated names with `…` need expansion via `hermes skills inspect <name>`)
2. Normalize: strip `-v2`, `-1`, `_final`, `(copy)`, `(2)`, `[old]`
3. Group by normalized name
4. For each group of ≥2, choose winner by:
   - Newest `metadata.modified` (use `hermes skills inspect`)
   - Largest body (≥10 lines, real content, no `[SKILL_PRUNED]`)
   - Intact linked files (references/, templates/, scripts/)
5. Skip USER-OWNED skills (per MEMORY.md: `profile-directive-sync`, `convert-plaintext-to-md`, `enhance-markdown`)

**Gate 2.1:** Duplicate groups logged to `./scratch/dup-groups.json`.
**Gate 2.2:** USER-OWNED skills excluded from deletion list.

## Phase 3 — Delete Duplicates

```bash
hermes skills uninstall <loser-name>
```

Rules:

- Preserve category version over root duplicate (e.g. keep `devops/hermes-setup`, delete root `hermes-setup`)
- Preserve skills.sh (community) version over copy if both present (community is upstream)
- If `[SKILL_PRUNED]` is in EVERY dup → restore from bundle before delete

**Gate 3.1:** Losers deleted; winners remain.
**Gate 3.2:** Log each delete to `./scratch/dedup-actions.log`.

## Phase 4 — Log Updated State

```bash
hermes skills list > updated-skills.txt
wc -l updated-skills.txt
diff initial-skills.txt updated-skills.txt > skills-dedup-diff.txt
```

**Gate 4.1:** `updated-skills.txt` count < `initial-skills.txt` count.
**Gate 4.2:** `skills-dedup-diff.txt` non-empty (proves deletions happened).

## Phase 5 — Judge (≥90 target)

Use `batch-skill-judge` (development category) — already known to work per MEMORY.md:

```bash
cd ~/AppData/Local/hermes/scripts
MSYS_NO_PATHCONV=1 ./batch_skill_judge.py --threshold 90
```

Per MEMORY.md: `--threshold 100` is max-verify; we'll use `--threshold 90` per user request.

**Gate 5.1:** Batch judge runs to completion without errors.
**Gate 5.2:** Output log at `./scratch/skill-judge.log` shows pass/fail counts.

## Phase 6 — Debug/fix ascending-modified (≤5 skills/turn)

For each of the 32 user-modified skills (from `hermes skills list-modified`), in ascending order:

```bash
# Per turn (5 skills):
for skill in $(hermes skills list-modified | head -5); do
  hermes skills diff "$skill"   # see what user changed
  # fix any warnings/errors flagged in judge log
done
```

Apply fixes via `patch` (no full rewrites unless ≥30% body change).

**Gate 6.1:** All 32 user-modified skills reviewed.
**Gate 6.2:** Final `hermes skills audit` clean.

## Risks & Mitigations

| Risk                                                                      | Mitigation                                                             |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Accidentally delete USER-OWNED skill                                      | Cross-check against MEMORY.md USER-OWNED list before every delete      |
| Skill body has [SKILL_PRUNED]                                             | Skip delete; run `hermes skills reset` to restore from bundle first    |
| 1,120 skills = many false-positive dups (similar names, different scopes) | Inspect before delete; only delete when normalized names match exactly |
| Judge threshold unreachable for thin skills                               | Patch body to ≥10 lines with real workflow content                     |
| Race with other sessions                                                  | Re-run `hermes skills list` immediately before each batch of deletes   |

## Out of Scope

- Goal 4 (free-model benchmark)
- Goal 5 (profile cleanup)

## Completion Signal

"`updated-skills.txt` < `initial-skills.txt`, all 32 modified skills reviewed, `hermes skills audit` clean, `batch-skill-judge.py --threshold 90` ≥90% pass."

## Estimated Effort

| Phase                 | Skills touched         | Turns                |
| --------------------- | ---------------------- | -------------------- |
| 1 (capture)           | 0                      | 1                    |
| 2 (identify dups)     | 0 (analysis only)      | 1-2                  |
| 3 (delete dups)       | TBD (~50-200 expected) | 1-3                  |
| 4 (log updated)       | 0                      | 1                    |
| 5 (judge batch)       | all remaining          | 1 (script run)       |
| 6 (debug 32 modified) | 32                     | 7 (5/turn, last = 2) |

Total: ~12-15 turns.
