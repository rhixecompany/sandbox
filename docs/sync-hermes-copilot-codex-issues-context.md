# sync-hermes-copilot-codex — Audit Issues Context

> Generated: 2026-06-20T01:30:00Z | Source: `sync-hermes-copilot-codex.prompt.md` + `sync-hermes-copilot-codex.prompt.txt`
> Audit batch: 2 files (1 .prompt.md, 1 .prompt.txt)

---

## Issues Summary

| Severity | Count | Category |
|----------|-------|----------|
| Medium | 1 | Prose in `skills:` frontmatter list (YAML should be clean identifiers) |
| Medium | 1 | .prompt.txt lacks frontmatter (not parseable as structured prompt) |
| Low | 1 | Double frontmatter fence false positive (table separators counted) |
| Low | 4 | Table pipe-balance false positives (2-column Skills Required table) |

---

## Detailed Findings

### sync-hermes-copilot-codex.prompt.md

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

#### LOW: Double Frontmatter Fence False Positive
- **Location:** First 60 lines
- **Count:** 4 `---` fences (expected: 2)
- **Root Cause:** Audit script counts all `---` substrings including table separator rows (`--- | ---`)
- **Actual:** Exactly 2 frontmatter fences (lines 1, 15) — correct
- **Action:** No file fix needed; audit pattern refinement needed

#### LOW: Table Pipe-Balance False Positives (4 instances)
- **Location:** Skills Required table (rows 1-5)
- **Issue:** Regex flagged 2-column rows (skill + description)
- **Reality:** These are valid 2-column tables (Skill | Purpose)
- **Action:** No fix needed for these; audit pattern needs refinement

---

### sync-hermes-copilot-codex.prompt.txt

#### MEDIUM: Missing Frontmatter
- **Issue:** No YAML frontmatter - not parseable as structured Hermes prompt
- **Current format:** Inline skill triggers on line 1
- **Expected:** Full frontmatter with `trigger`, `description`, `tags`, `dependencies`, `skills`
- **Fix:** Convert to .prompt.md format (or add frontmatter if keeping .txt)

#### LOW: Trigger Regex False Positives
- **Detection:** Found triggers `['using', 'user', 'plans', 'goal', 'agents', 'instructions']`
- **Reality:** Partial matches from `/using-superpowers`, `/user-communication-preferences`, `/plans-and-specs`, `/goal`, and words in the goal text
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

1. **Clean skills: frontmatter list** (Medium - violates schema convention)
2. **Add frontmatter to .prompt.txt or convert** (Medium - prompt normalization)
3. **Audit script refinements** (Low - false positives only)

---

## Verification Gates (Post-Fix)

- [ ] `yaml.safe_load` on frontmatter parses as single document
- [ ] Zero double-fence repeats in first 60 lines (actual frontmatter only)
- [ ] No dependency-style prose in `skills:` lists
- [ ] File uses `.prompt.md` extension
- [ ] Trigger matches filename stem convention
- [ ] Skills Required table matches frontmatter `skills:` exactly
- [ ] .prompt.txt either converted or has frontmatter