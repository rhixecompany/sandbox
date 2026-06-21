# test-providers-models — Audit Issues Context

> Generated: 2026-06-20T00:00:00Z | Source: `test-providers-models.prompt.md` + `test-providers-models.prompt.txt`
> Audit batch: 2 files (1 .prompt.md, 1 .prompt.txt)

---

## Issues Summary

| Severity | Count | Category |
|----------|-------|----------|
| High | 1 | Double frontmatter fences (4 in first 60 lines) |
| High | 1 | Referenced script missing (`test_models.py`) |
| Medium | 3 | Prose in `skills:` frontmatter list (YAML should be clean identifiers) |
| Medium | 1 | Skills table mismatch with frontmatter (table includes model names) |
| Medium | 1 | .prompt.txt lacks frontmatter (not parseable as structured prompt) |
| Low | 5 | Table pipe-balance warnings (Skills Required table has 2-col rows) |
| Low | 1 | Hardcoded Windows path in content |

---

## Detailed Findings

### test-providers-models.prompt.md

#### HIGH: Double Frontmatter Fences
- **Location:** First 60 lines
- **Count:** 4 `---` fences (expected: 2)
- **Cause:** Likely nested frontmatter or copy-paste artifact
- **Fix:** Ensure exactly 2 fences (open/close) around single YAML document

#### HIGH: Referenced Script Missing
- **Location:** Line 128
- **Reference:** `C:\Users\Alexa\AppData\Local\hermes\scripts\test_models.py`
- **Status:** File does not exist
- **Fix:** Either create the script or update reference to indicate it's planned/not yet created

#### MEDIUM: Prose in skills: Frontmatter List
- **Location:** Frontmatter `skills:` array (lines 11-15)
- **Current:**
  ```yaml
  skills:
    - using-superpowers — Establishes workflow foundation
    - user-communication-preferences — Loads user prefs for execution style
    - plans-and-specs — Creates implementation plan from goal
  ```
- **Expected:** Clean skill identifiers only (descriptions belong in `dependencies:` or docs)
- **Fix:** Change to:
  ```yaml
  skills:
    - using-superpowers
    - user-communication-preferences
    - plans-and-specs
  ```

#### MEDIUM: Skills Required Table Mismatch
- **Location:** Lines 38-43 (Markdown table)
- **Table includes:** 3 skills + 7 model names (from free models table)
- **Frontmatter has:** 3 skills only
- **Cause:** Regex picked up model names from Phase 2 free models table
- **Fix:** Ensure Skills Required table only lists actual required skills

#### LOW: Table Pipe-Balance Warnings (5 instances)
- **Location:** Skills Required table rows 1-5
- **Issue:** Regex detection flagged 2-column rows (skill + description)
- **Reality:** These are valid 2-column tables (Skill | Purpose)
- **Note:** False positive from audit script - 2-column tables are valid
- **Action:** No fix needed for these; audit pattern needs refinement

#### LOW: Hardcoded Windows Path
- **Location:** Line 128
- **Path:** `C:\Users\Alexa\AppData\Local\hermes\scripts\test_models.py`
- **Issue:** Platform-specific path in cross-platform prompt
- **Fix:** Use `~/AppData/Local/hermes/scripts/test_models.py` or `$HERMES_HOME/scripts/test_models.py`

---

### test-providers-models.prompt.txt

#### MEDIUM: Missing Frontmatter
- **Issue:** No YAML frontmatter - not parseable as structured Hermes prompt
- **Current format:** Inline skill triggers on line 1
- **Expected:** Full frontmatter with `trigger`, `description`, `tags`, `dependencies`, `skills`
- **Fix:** Convert to .prompt.md format (or add frontmatter if keeping .txt)

#### LOW: Trigger Regex False Positives
- **Detection:** Found triggers `['using', 'user', 'plans', 'goal', 'Logic']`
- **Reality:** These are partial matches from `/using-superpowers`, `/user-communication-preferences`, `/plans-and-specs`, `/goal`, and `Logic` in "Reasoning/Logic"
- **Action:** No fix needed - detection pattern limitation

---

## Audit Patterns Applied

| Pattern | Reference |
|---------|-----------|
| Double frontmatter fence detection | `references/audit-detection-edge-cases.md` |
| Skills prose in YAML | `references/prompt-file-debugging-patterns.md` (Bug #2) |
| Pipe-balance false positives | `references/audit-detection-edge-cases.md` |
| Heading hierarchy validation | `references/heading-hierarchy-validation.md` |
| Cross-file symmetry | `references/doc-symmetry-validation.md` |

---

## Fix Priority Order

1. **Fix double frontmatter fences** (High - blocks YAML parsing reliability)
2. **Clean skills: frontmatter list** (Medium - violates schema convention)
3. **Fix Skills Required table** (Medium - documentation accuracy)
4. **Add frontmatter to .prompt.txt or convert** (Medium - prompt normalization)
5. **Resolve missing script reference** (High - but requires script creation)
6. **Normalize Windows path** (Low - cross-platform compatibility)

---

## Verification Gates (Post-Fix)

- [ ] `yaml.safe_load` on frontmatter parses as single document
- [ ] Zero double-fence repeats in first 60 lines
- [ ] No dependency-style prose in `skills:` lists
- [ ] File uses `.prompt.md` extension
- [ ] Trigger matches filename stem convention
- [ ] Skills Required table matches frontmatter `skills:` exactly
- [ ] Referenced script exists or reference updated with status