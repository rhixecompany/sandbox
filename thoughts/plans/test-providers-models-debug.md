# test-providers-models — Debug Fix Plan

> Generated: 2026-06-20T00:00:00Z | Phase: 2 (Fix Planning)
> Source: `docs/test-providers-models-issues-context.md`

---

## Fix Plan Overview

| Batch | Issue | Severity | File | Action |
|-------|-------|----------|------|--------|
| 1 | Double frontmatter fences | High | `.prompt.md` | Remove extra `---` fences, keep exactly 2 |
| 1 | Prose in `skills:` frontmatter | Medium | `.prompt.md` | Clean to identifiers only |
| 1 | Skills Required table mismatch | Medium | `.prompt.md` | Align table with frontmatter skills |
| 1 | Hardcoded Windows path | Low | `.prompt.md` | Normalize to `~/AppData/Local/...` |
| 2 | Missing frontmatter in .txt | Medium | `.prompt.txt` | Add frontmatter or convert to .md |
| 2 | Referenced script missing | High | `.prompt.md` | Create script or update reference |
| 2 | Verify all fixes | - | Both | Re-run audit checks |

---

## Batch 1 (Proof-of-Concept) — 4 Issues

### Issue 1: Double Frontmatter Fences
- **File:** `test-providers-models.prompt.md`
- **Root Cause:** 4 `---` fences in first 60 lines (lines 1, 15, and likely 2 more from nested content)
- **Fix:** Ensure exactly 2 fences surrounding single YAML document
- **Verification:** `yaml.safe_load` parses cleanly; fence count = 2 in first 60 lines

### Issue 2: Prose in skills: Frontmatter
- **File:** `test-providers-models.prompt.md` lines 11-15
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

### Issue 3: Skills Required Table Mismatch
- **File:** `test-providers-models.prompt.md` lines 38-43
- **Root Cause:** Table includes model names from Phase 2 free models table
- **Fix:** Replace table with only the 3 actual required skills
- **Expected table:**
  ```markdown
  | Skill | Purpose |
  | --- | --- |
  | `using-superpowers` | Establishes workflow foundation |
  | `user-communication-preferences` | Loads user prefs for execution style |
  | `plans-and-specs` | Creates implementation plan from goal |
  ```

### Issue 4: Hardcoded Windows Path
- **File:** `test-providers-models.prompt.md` line 128
- **Fix:** Change `C:\Users\Alexa\AppData\Local\hermes\scripts\test_models.py` → `~/AppData/Local/hermes/scripts/test_models.py`

---

## Batch 2 — 3 Issues

### Issue 5: .prompt.txt Missing Frontmatter
- **File:** `test-providers-models.prompt.txt`
- **Options:**
  A. Add frontmatter to .txt (making it parseable)
  B. Convert to .prompt.md (preferred - consistent with Hermes convention)
  C. Rename to `.prompt.md` and add frontmatter
- **Recommendation:** Option B - convert to full `.prompt.md` with frontmatter matching the main file
- **Note:** The .txt is a minimal trigger version; the .md is the full structured prompt

### Issue 6: Referenced Script Missing
- **File:** `test-providers-models.prompt.md` line 128
- **Reference:** `~/AppData/Local/hermes/scripts/test_models.py`
- **Options:**
  A. Create the test harness script
  B. Update reference to note "planned/not yet created"
  C. Remove reference if not needed
- **Recommendation:** Option A - create minimal test harness (supports the prompt's purpose)
- **Script requirements:**
  - Fetch model catalog from `https://hermes-agent.nousresearch.com/docs/api/model-catalog.json`
  - Filter free models
  - Run 3-task benchmark (reasoning, tool calling, knowledge)
  - Log results with performance metrics

### Issue 7: Full Verification
- **Action:** Re-run all audit checks on both files
- **Gate criteria:**
  - [ ] Frontmatter parses as single YAML document
  - [ ] Zero double-fence repeats in first 60 lines
  - [ ] No prose in `skills:` lists
  - [ ] Skills Required table matches frontmatter exactly
  - [ ] Trigger matches filename stem
  - [ ] Referenced script exists or reference updated
  - [ ] .prompt.txt either converted or has frontmatter

---

## Progress Log

| Batch | Status | Files Modified | Issues Resolved | Notes |
|-------|--------|----------------|-----------------|-------|
| 1 | Pending | - | 0/4 | Proof-of-concept batch |
| 2 | Pending | - | 0/3 | Remaining fixes |
| Verify | Pending | - | 0/7 | Independent verification |

---

## Rollback Plan

If any fix introduces regression:
1. `git checkout test-providers-models.prompt.md`
2. `git checkout test-providers-models.prompt.txt`
3. Re-run audit to confirm original state