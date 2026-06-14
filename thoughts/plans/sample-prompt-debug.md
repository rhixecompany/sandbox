# sample-prompt — Fix Plan (Debug)

**Purpose:** sample-prompt
**Generated:** 2026-06-14
**Source Issues:** `docs/sample-prompt-issues-context.md`
**Target File:** `./sample.prompt.md`

---

## Fix Plan Overview

| Batch | Issues | Files | Status |
|-------|--------|-------|--------|
| 1 (PoC) | MEDIUM-001, MEDIUM-002, MEDIUM-003, MEDIUM-004, LOW-001, LOW-002, LOW-003 | sample.prompt.md (7 issues) | 🔄 Ready |

**Batch Size:** 7 issues (matches enhance-markdown batch size)
**Proof-of-Concept Gate:** Batch 1 must pass verification before completion (single batch)

---

## Batch 1 Fixes (Proof-of-Concept — All Issues)

### MEDIUM-001: Frontmatter missing recommended fields (version, author, license)
- **Location:** Lines 1-7 (frontmatter block)
- **Fix:** Add `version: "1.0.0"`, `author: "Hermes Agent"`, `license: "MIT"` to frontmatter
- **Action:** `patch` — insert three fields before closing `---`

### MEDIUM-002: Missing `metadata.hermes.related_skills` in frontmatter
- **Location:** Lines 1-7 (frontmatter block)
- **Fix:** Add `metadata.hermes.related_skills: [skill-creator, writing-skills, plans-and-specs]`
- **Action:** `patch` — insert metadata block before closing `---`

### MEDIUM-003: Skills Required table not synchronized with frontmatter metadata
- **Location:** Lines 15-22 (Skills Required table) vs Lines 1-7 (frontmatter)
- **Fix:** The fix for MEDIUM-002 adds related_skills to frontmatter, synchronizing the two sources
- **Action:** Covered by MEDIUM-002 fix; no separate patch needed

### MEDIUM-004: No language tags on code blocks
- **Location:** Lines 58-65 (frontmatter example), Lines 73-78 (example output)
- **Fix:** 
  - Line 58: ```yaml → ```yaml (already correct)
  - Line 73: ``` → ```markdown (add language tag)
- **Action:** `patch` — replace bare ``` with ```markdown on line 73

### LOW-001: Verification checklist item references filename extension
- **Location:** Line 52
- **Fix:** Change "File is saved with `.prompt.md` extension" → "File uses `.prompt.md` extension matching trigger"
- **Action:** `patch` — replace line 52

### LOW-002: Trigger match checklist item could be more precise
- **Location:** Line 53
- **Fix:** Change "Trigger matches filename stem (e.g., `trigger: /my-task` → `my-task.prompt.md`)" → "Trigger matches filename stem (e.g., `trigger: /my-task` → `my-task.prompt.md`) (current: `/sample-prompt` → `sample-prompt.md`)"
- **Action:** `patch` — replace line 53

### LOW-003: Phase 3 "Format & Consistency" could be merged into Phase 2
- **Location:** Lines 38-44
- **Fix:** Merge Phase 3 steps into Phase 2 "Structure" as sub-steps; renumber Phase 4→3 (Verification)
- **Action:** `patch` — restructure phases section

---

## Execution Strategy

**Tool:** `patch` (targeted find-and-replace)
**Order:** Apply frontmatter fixes first (MEDIUM-001, MEDIUM-002), then code block fix, then checklist fixes, then phase restructure
**Verification:** Re-read file, check frontmatter parses, check markdown renders, verify all 7 issues resolved

---

## Plugin System Registration

Plan registered under namespace: `sample-prompt-debug`
Specs registered for: fix application, verification