# audit-skills-judge-fix — Debug Fix Plan

> Generated: 2026-06-20T02:00:00Z | Phase: 2 (Fix Planning)
> Source: `docs/audit-skills-judge-fix-issues-context.md`

---

## Fix Plan Overview

| Batch | Issue | Severity | File | Action |
|-------|-------|----------|------|--------|
| 1 | Prose in `skills:` frontmatter | Medium | `.prompt.md` | Clean to identifiers only |
| 1 | Hardcoded Windows paths | Low | `.prompt.md` | Normalize to `~/AppData/Local/...` |
| 1 | Emoji in technical doc | Low | `.prompt.md` | Replace 🔴 with `[RED]` |
| 1 | .prompt.txt duplicate | Medium | `.prompt.txt` | Remove (canonical .prompt.md kept) |
| 2 | Verify all fixes | - | Both | Re-run audit checks |

---

## Batch 1 (Proof-of-Concept) — 4 Issues

### Issue 1: Prose in skills: Frontmatter
- **File:** `audit-skills-judge-fix.prompt.md` lines 15-22
- **Root Cause:** Descriptions embedded in YAML list items
- **Fix:** Strip descriptions from `skills:` list; keep in `dependencies:` or docs
- **Before:**
  ```yaml
  skills:
    - using-superpowers — Establishes workflow foundation
    - user-communication-preferences — Loads user prefs for execution style
    - plans-and-specs — Creates implementation plan from goal
    - skill-judge — Evaluates skill quality against criteria (v1.1.0)
    - hermes-skills — Skills discovery, install, management
    - skill-creator — Author in-repo SKILL.md
    - writing-skills — Write clear skill prose and structure
  ```
- **After:**
  ```yaml
  skills:
    - using-superpowers
    - user-communication-preferences
    - plans-and-specs
    - skill-judge
    - hermes-skills
    - skill-creator
    - writing-skills
  ```
- **Verification:** Frontmatter `skills:` list contains only identifiers

### Issue 2: Hardcoded Windows Paths
- **File:** `audit-skills-judge-fix.prompt.md` (multiple lines)
- **Root Cause:** Absolute Windows paths in content
- **Fix:** Replace all `C:\Users\Alexa\AppData\Local\hermes\` with `~/AppData/Local/hermes/` or `$HERMES_HOME/`
- **Specific replacements:**
  - `C:/Users/Alexa/AppData/Local/hermes/scripts/` → `~/AppData/Local/hermes/scripts/`
  - `C:\Users\Alexa\AppData\Local\hermes\skills\` → `~/AppData/Local/hermes/skills/`
- **Verification:** No `C:\Users\` or `C:/Users/` patterns in content

### Issue 3: Emoji in Technical Doc
- **File:** `audit-skills-judge-fix.prompt.md` line 265 (score bands table)
- **Root Cause:** 🔴 emoji in score band table
- **Fix:** Replace `🔴` with `[RED]` or `RED`
- **Verification:** No emoji characters in content

### Issue 4: .prompt.txt Duplicate
- **File:** `audit-skills-judge-fix.prompt.txt`
- **Action:** Remove file (canonical `.prompt.md` already exists with full frontmatter)
- **Verification:** Single `.prompt.md` file remains

---

## Batch 2 — 1 Issue (Verification)

### Issue 5: Full Verification
- **Action:** Re-run all audit checks on the file
- **Gate criteria:**
  - [ ] Frontmatter parses as single YAML document
  - [ ] Zero actual frontmatter fences (2)
  - [ ] No prose in `skills:` lists
  - [ ] Skills Required table matches frontmatter exactly
  - [ ] Trigger matches filename stem
  - [ ] No hardcoded Windows paths
  - [ ] No emoji in technical tables
  - [ ] Single `.prompt.md` file (no .txt duplicate)

---

## Progress Log

| Batch | Status | Files Modified | Issues Resolved | Notes |
|-------|--------|----------------|-----------------|-------|
| 1 | Pending | - | 0/4 | Proof-of-concept batch |
| 2 | Pending | - | 0/1 | Verification |

---

## Rollback Plan

If any fix introduces regression:
1. `git checkout audit-skills-judge-fix.prompt.md`
2. `git checkout audit-skills-judge-fix.prompt.txt` (if exists)
3. Re-run audit to confirm original state