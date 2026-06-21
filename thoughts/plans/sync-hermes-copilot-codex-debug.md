# sync-hermes-copilot-codex — Debug Fix Plan

> Generated: 2026-06-20T01:30:00Z | Phase: 2 (Fix Planning)
> Source: `docs/sync-hermes-copilot-codex-issues-context.md`

---

## Fix Plan Overview

| Batch | Issue | Severity | File | Action |
|-------|-------|----------|------|--------|
| 1 | Prose in `skills:` frontmatter | Medium | `.prompt.md` | Clean to identifiers only |
| 1 | .prompt.txt missing frontmatter | Medium | `.prompt.txt` | Add frontmatter or convert to .md |
| 2 | Verify all fixes | - | Both | Re-run audit checks |

---

## Batch 1 (Proof-of-Concept) — 2 Issues

### Issue 1: Prose in skills: Frontmatter
- **File:** `sync-hermes-copilot-codex.prompt.md` lines 11-15
- **Root Cause:** Descriptions embedded in YAML list items
- **Fix:** Strip descriptions from `skills:` list; keep in `dependencies:` or docs
- **Before:**
  ```yaml
  skills:
    - using-superpowers — Establishes workflow foundation
    - user-communication-preferences — Loads user prefs for execution style
    - plans-and-specs — Creates implementation plan from goal
  ```
- **After:**
  ```yaml
  skills:
    - using-superpowers
    - user-communication-preferences
    - plans-and-specs
  ```
- **Verification:** Frontmatter `skills:` list contains only identifiers

### Issue 2: .prompt.txt Missing Frontmatter
- **File:** `sync-hermes-copilot-codex.prompt.txt`
- **Options:**
  A. Add frontmatter to .txt (making it parseable)
  B. Convert to .prompt.md (preferred - consistent with Hermes convention)
  C. Rename to `.prompt.md` and add frontmatter
- **Recommendation:** Option B - replace `.prompt.txt` with proper `.prompt.md` containing full frontmatter matching the main file structure
- **Detail:** The .txt is a minimal trigger-only version; the .md is the full structured prompt. Keep single canonical `.prompt.md` file.
- **Verification:** Single `.prompt.md` file with valid frontmatter

---

## Batch 2 — 1 Issue (Verification)

### Issue 3: Full Verification
- **Action:** Re-run all audit checks on the file
- **Gate criteria:**
  - [ ] Frontmatter parses as single YAML document
  - [ ] Zero actual frontmatter fences (2)
  - [ ] No prose in `skills:` lists
  - [ ] Skills Required table matches frontmatter exactly
  - [ ] Trigger matches filename stem
  - [ ] Single `.prompt.md` file (no .txt duplicate)

---

## Progress Log

| Batch | Status | Files Modified | Issues Resolved | Notes |
|-------|--------|----------------|-----------------|-------|
| 1 | Pending | - | 0/2 | Proof-of-concept batch |
| 2 | Pending | - | 0/1 | Verification |

---

## Rollback Plan

If any fix introduces regression:
1. `git checkout sync-hermes-copilot-codex.prompt.md`
2. `git checkout sync-hermes-copilot-codex.prompt.txt` (if exists)
3. Re-run audit to confirm original state