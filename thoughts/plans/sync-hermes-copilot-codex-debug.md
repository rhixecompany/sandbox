# sync-hermes-copilot-codex — Debug Fix Plan

> Generated: 2026-06-21T10:00:00Z | Phase: 2 (Fix Planning)
> Source: `docs/sync-hermes-copilot-codex-issues-context.md`
> Status: Fresh re-run

---

## Fix Plan Overview

| Batch | ID | Issue | Severity | File | Action |
|-------|----|-------|----------|------|--------|
| 1 | F1 | Stale `.prompt.txt` reference (line 45) | Medium | `.prompt.md` | Update to note TXT was consolidated |
| 1 | F2 | Missing frontmatter fields | Low | `.prompt.md` | Add `name`, `title`, `version` |
| 1 | F3 | Missing `metadata.hermes` | Low | `.prompt.md` | Add metadata block with related_skills |
| 1 | F4 | Missing verification checklist | Low | `.prompt.md` | Add checklist section at end |
| 1 | F5 | Inconsistent tags style | Info | `.prompt.md` | Convert flow seq to block-style list |
| 1 | F6 | `dependencies`/`skills` redundancy | Info | `.prompt.md` | Add YAML comment clarifying dual format |
| 2 | G1 | Full verification | — | Both | Re-run audit + YAML parse checks |

---

## Batch 1 (Proof-of-Concept) — 6 Issues

### F1: Stale `.prompt.txt` Reference

- **File:** `sync-hermes-copilot-codex.prompt.md` line 45
- **Root Cause:** `.prompt.txt` was removed in prior audit as redundant
- **Fix:** Replace `**Source reference:** \`./sync-hermes-copilot-codex.prompt.txt\`` with consolidated reference
- **After:**
  ```
  - **Source:** `sync-hermes-copilot-codex.prompt.md` (canonical; legacy `.txt` consolidated)
  ```
- **Verification:** No remaining `.prompt.txt` reference in file

### F2: Missing Frontmatter Fields

- **File:** `sync-hermes-copilot-codex.prompt.md` frontmatter
- **Root Cause:** Fields omitted; `.prompt.md` convention includes `name`, `title`, `version`
- **Fix:** Add after `trigger:`:
  ```yaml
  name: sync-hermes-copilot-codex
  title: Sync Hermes Copilot Codex
  version: 1.0.0
  ```
- **Verification:** `name`, `title`, `version` present in YAML

### F3: Missing metadata.hermes

- **File:** `sync-hermes-copilot-codex.prompt.md` frontmatter
- **Root Cause:** No metadata block
- **Fix:** Add after `skills:` (before closing `---`):
  ```yaml
  metadata:
    hermes:
      related_skills:
        - using-superpowers
        - user-communication-preferences
        - plans-and-specs
  ```
- **Verification:** `metadata.hermes.related_skills` present and matches skills list

### F4: Missing Verification Checklist

- **File:** End of `sync-hermes-copilot-codex.prompt.md`
- **Root Cause:** No self-checking section
- **Fix:** Add after `## Actions Summary`:
  ```markdown
  ## Verification Checklist

  - [ ] All instructions scanned and personalities created
  - [ ] All agents scanned and profiles created
  - [ ] Hermes root identified
  - [ ] Copilot root identified
  - [ ] Codex root identified
  - [ ] Skills synced bidirectionally
  - [ ] Plugins synced bidirectionally
  - [ ] Hooks synced bidirectionally
  - [ ] Plan and specs verified complete
  ```
- **Verification:** Section present with 9 checkboxes

### F5: Inconsistent YAML tags Style

- **File:** `sync-hermes-copilot-codex.prompt.md` frontmatter lines 8-17
- **Root Cause:** Flow sequence `[...]` in block context
- **Fix:** Convert to block-style:
  ```yaml
  tags:
    - hermes
    - copilot
    - opencode
    - sync
    - skills
    - plugins
    - hooks
    - personalities
    - profiles
  ```
- **Verification:** Frontmatter parses; tags loaded as list of 9 items

### F6: dependencies/skills Redundancy Note

- **File:** `sync-hermes-copilot-codex.prompt.md` frontmatter
- **Root Cause:** `dependencies:` (Copilot format with `skill:` prefix) duplicates `skills:` (Hermes format)
- **Fix:** Add YAML comment line before `dependencies:` explaining the dual format
- **Verification:** Comment present in frontmatter

---

## Batch 2 — 1 Issue (Verification)

### G1: Full Verification

- **Action:** Re-run all audit checks on the modified file
- **Gate criteria:**
  - [ ] Frontmatter parses as single YAML document
  - [ ] 2 fences in first 60 lines (no double-fence issue)
  - [ ] No prose in `skills:` lists
  - [ ] Required fields present: `name`, `title`, `version`
  - [ ] `metadata.hermes.related_skills` matches Skills Required table
  - [ ] Trigger matches filename stem
  - [ ] All tables balanced
  - [ ] Verification checklist section present
  - [ ] No stale `.prompt.txt` reference

---

## Progress Log

| Batch | Status | Files Modified | Issues Resolved | Notes |
|-------|--------|----------------|-----------------|-------|
| 1 | Pending | — | 0/6 | All 6 issues in single batch |
| 2 | Pending | — | 0/1 | Full verification pass |

---

## Rollback Plan

If any fix introduces regression:
1. `git checkout sync-hermes-copilot-codex.prompt.md`
2. Re-run audit to confirm original state
3. Cherry-pick fixes one at a time
