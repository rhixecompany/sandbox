# sample-prompt — Audit Issues Context

**Generated:** 2026-06-14
**Source File:** `./sample.prompt.md`
**Purpose:** sample-prompt
**Audit Mode:** Full enhance-markdown audit (fresh run)

---

## Issue Summary

| Severity | Count |
|----------|-------|
| High | 0 |
| Medium | 4 |
| Low | 3 |

---

## Issues Detail

### MEDIUM-001: Frontmatter missing optional but recommended fields
- **Location:** Lines 1-7 (frontmatter block)
- **Description:** Frontmatter has required fields (`name`, `title`, `description`, `trigger`, `tags`) but missing recommended fields per enhance-markdown verification checklist: `version`, `author`, `license`
- **Impact:** Inconsistent with skill specification which requires all fields
- **Fix:** Add `version: "1.0.0"`, `author: "Hermes Agent"`, `license: "MIT"` to frontmatter

### MEDIUM-002: Missing `metadata.hermes.related_skills` in frontmatter
- **Location:** Lines 1-7 (frontmatter block)
- **Description:** Frontmatter lacks `metadata.hermes.related_skills` array which should list all prerequisite skills (skill-creator, writing-skills, plans-and-specs)
- **Impact:** Skill discovery and cross-reference incomplete
- **Fix:** Add `metadata.hermes.related_skills: [skill-creator, writing-skills, plans-and-specs]`

### MEDIUM-003: Skills Required table not synchronized with frontmatter metadata
- **Location:** Lines 15-22 (Skills Required table) vs Lines 1-7 (frontmatter)
- **Description:** Skills table lists 3 skills but frontmatter has no `skills:` field or `metadata.hermes.related_skills`
- **Impact:** Two-source-of-truth drift risk
- **Fix:** Either add skills to frontmatter metadata or remove table (prefer adding to frontmatter)

### MEDIUM-004: No language tags on code blocks
- **Location:** Lines 58-65 (frontmatter example), Lines 73-78 (example output)
- **Description:** Code blocks use ```yaml and ``` but the second example block has no language tag
- **Impact:** Syntax highlighting and parsing consistency
- **Fix:** Add language tags to all code blocks

### LOW-001: Verification checklist item references filename extension
- **Location:** Line 52: "File is saved with `.prompt.md` extension"
- **Description:** Checklist item 6 references extension explicitly; could be generic
- **Impact:** Minor consistency
- **Fix:** Generalize to "File uses `.prompt.md` extension matching trigger"

### LOW-002: Trigger match checklist item could be more precise
- **Location:** Line 53: "Trigger matches filename stem (e.g., `trigger: /my-task` → `my-task.prompt.md`)"
- **Description:** Good example but could explicitly note current file's match
- **Impact:** Minor clarity
- **Fix:** Add parenthetical: "(current: `/sample-prompt` → `sample-prompt.md`)"

### LOW-003: Phase 3 "Format & Consistency" could be merged into Phase 2
- **Location:** Lines 38-44
- **Description:** Phase 3 has only 4 steps about formatting; Phase 2 "Structure" also covers structural formatting
- **Impact:** Phase granularity inconsistency
- **Fix:** Consider merging Phase 3 into Phase 2 or expanding Phase 3 with more substantive checks

---

## Frontmatter Parse Check

```
✅ YAML parses as single document
✅ No double-fence repeats in first 60 lines (only 2 fences: open/close)
✅ No dependency-style prose in `skills:` lists (no skills: field in frontmatter)
❌ Missing recommended fields: version, author, license
❌ Missing metadata.hermes.related_skills
```

---

## Structure Validation

| Check | Status | Notes |
|-------|--------|-------|
| H1 title present | ✅ | "# Sample Prompt Template" |
| H2 sections present | ✅ | Description, Skills Required, Workflow, Key Patterns, Example Output |
| H3 phases present | ✅ | Phase 1-4 with numbered steps |
| Skills Required table | ✅ | 3 skills listed |
| Verification checklist | ✅ | 7 items, all `- [ ]` format |
| No placeholder text | ✅ | No `[Add ... here]` found |
| Trigger matches filename | ✅ | `/sample-prompt` → `sample.prompt.md` |

---

## Recommendations

1. **Priority 1:** Add missing frontmatter fields (version, author, license, metadata.hermes.related_skills)
2. **Priority 2:** Add language tags to all code blocks
3. **Priority 3:** Synchronize Skills table with frontmatter metadata
4. **Priority 4:** Minor checklist wording improvements