# audit-skills-judge-fix — Audit Issues Context

> Generated: 2026-06-20T02:00:00Z | Source: `audit-skills-judge-fix.prompt.md` + `audit-skills-judge-fix.prompt.txt`
> Audit batch: 2 files (1 .prompt.md, 1 .prompt.txt)

---

## Issues Summary

| Severity | Count | Category |
|----------|-------|----------|
| Medium | 1 | Prose in `skills:` frontmatter list (7 skills with descriptions) |
| Medium | 1 | .prompt.txt lacks frontmatter (not parseable as structured prompt) |
| Low | 1 | Hardcoded Windows paths in content (`C:\\Users\\...`) |
| Low | 1 | Emoji in technical doc (🔴) |
| Low | 4 | Table pipe-balance false positives (2-column tables flagged) |
| Low | 1 | Double frontmatter fence false positive (table separators counted) |

---

## Detailed Findings

### audit-skills-judge-fix.prompt.md

#### MEDIUM: Prose in skills: Frontmatter List
- **Location:** Frontmatter `skills:` array (lines 15-22)
- **Current:**
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
- **Expected:** Clean skill identifiers only (descriptions belong in `dependencies:` or docs)
- **Fix:** Change to:
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

#### LOW: Double Frontmatter Fence False Positive
- **Location:** First 60 lines
- **Count:** 4 `---` substrings (expected: 2)
- **Root Cause:** Audit script counts all `---` including table separator rows (`--- | ---`)
- **Actual:** Exactly 2 frontmatter fences (lines 1, 23) — correct
- **Action:** No file fix needed; audit pattern refinement needed

#### LOW: Table Pipe-Balance False Positives (4+ instances)
- **Location:** Skills Required table (rows 1-9), Category mapping table (rows 23-50), and others
- **Issue:** Regex flagged 2-column rows (skill + description / skill + category)
- **Reality:** These are valid 2-column tables
- **Action:** No fix needed for these; audit pattern needs refinement

#### LOW: Hardcoded Windows Paths
- **Location:** Multiple lines (39, 44, 215-219, 301-306, 389-402)
- **Paths:** `C:\Users\Alexa\AppData\Local\hermes\scripts\`, `C:\\Users\\Alexa\\AppData\\Local\\hermes\\skills\\`
- **Issue:** Platform-specific paths in cross-platform prompt
- **Fix:** Normalize to `~/AppData/Local/hermes/scripts/` or `$HERMES_HOME/scripts/`

#### LOW: Emoji in Technical Doc
- **Location:** Line 265 (score bands table)
- **Character:** 🔴 (red circle)
- **Issue:** Non-ASCII emoji in technical documentation
- **Fix:** Replace with text `[RED]` or `🔴` → `RED`

---

### audit-skills-judge-fix.prompt.txt

#### MEDIUM: Missing Frontmatter
- **Issue:** No YAML frontmatter - not parseable as structured Hermes prompt
- **Current format:** Inline skill triggers on line 1
- **Expected:** Full frontmatter with `trigger`, `description`, `tags`, `dependencies`, `skills`
- **Fix:** Convert to .prompt.md format (or add frontmatter if keeping .txt)
- **Recommendation:** Replace `.prompt.txt` with canonical `.prompt.md` (already exists)

#### LOW: Trigger Regex False Positives
- **Detection:** Found triggers `['using', 'user', 'plans', 'goal', 'local', 'local', 'plans', 'skill', 'local']`
- **Reality:** Partial matches from `/using-superpowers`, `/user-communication-preferences`, `/plans-and-specs`, `/goal`, `/local-skills`, `/skill-judge`
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
2. **Normalize Windows paths** (Low - cross-platform compatibility)
3. **Remove emoji** (Low - technical doc convention)
4. **Remove .prompt.txt duplicate** (Medium - prompt normalization)

---

## Verification Gates (Post-Fix)

- [ ] `yaml.safe_load` on frontmatter parses as single document
- [ ] Zero double-fence repeats in first 60 lines (actual frontmatter only)
- [ ] No dependency-style prose in `skills:` lists
- [ ] File uses `.prompt.md` extension
- [ ] Trigger matches filename stem convention
- [ ] Skills Required table matches frontmatter `skills:` exactly
- [ ] .prompt.txt either converted or removed (canonical .prompt.md kept)
- [ ] No hardcoded Windows paths (use `~/` or `$HERMES_HOME`)
- [ ] No emoji in technical tables