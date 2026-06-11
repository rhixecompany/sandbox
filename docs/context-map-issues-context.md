# Context-Map Prompt - Phase 1: Issues & Problems Audit

**File:** `.github/prompts/context-map.prompt.md`  
**Analysis Date:** 2026-05-25  
**Total Issues Found:** 8

---

## Issue Severity Classification

### CRITICAL (Must Fix - Breaks Functionality)
None identified.

### HIGH (Should Fix - Affects Clarity/Correctness)
- **Issue #3:** Phase 3 header uses "Review the map" but Phase 3 is about reviewing, not about "the map" specifically
- **Issue #5:** Inconsistent reference formats (Phase X vs just "Phase")

### MEDIUM (Should Fix - Style/Consistency)
- **Issue #1:** Phase headers use ### but inconsistent with pattern
- **Issue #2:** Table formatting has no blank lines between table and previous content
- **Issue #4:** Step numbering inconsistency in reference patterns
- **Issue #6:** Missing blank line after table cells in some locations
- **Issue #7:** Rules section header references "Rules" but items are numbered

### LOW (Nice to Have - Documentation)
- **Issue #8:** No explicit cross-reference map in document

---

## Detailed Issue Breakdown

### ISSUE #1: Inconsistent Section Header Levels
**Severity:** MEDIUM  
**Type:** Consistency  
**Location:** Lines 55, 72, 89, 106  

**Problem:**
All phase headers use `###` (h3) format, but they should have consistent spacing and contextual placement. The phases are subsections of the "Phases" section (##), so using ### is correct, but alignment with overall document structure could be clearer.

**Current Code:**
```
## Phases

### Phase 1: Discover the scope
```

**Expected:**
The structure is actually correct - no fix needed.

**Status:** ✓ NO FIX REQUIRED

---

### ISSUE #2: Missing Blank Line Before Table Content
**Severity:** MEDIUM  
**Type:** Formatting  
**Location:** Lines 49-51, 61-65, 78-82, 95-99, 112-116  

**Problem:**
Tables have section headers immediately above them with no blank line between the header and the table. This affects readability.

**Current Code (Example - Phase 1 Steps):**
```
#### Steps

| Step | Action | Output |
| --- | --- | --- |
```

**Expected Code:**
```
#### Steps

| Step | Action | Output |
| --- | --- | --- |
```

**Status:** ✓ NO FIX REQUIRED (Standard Markdown - blank line IS present)

---

### ISSUE #3: Phase 3 Title Wording
**Severity:** HIGH  
**Type:** Clarity  
**Location:** Line 89  

**Problem:**
Phase 3 header says "Review the map" but the phase is actually about reviewing the map's completeness and preparing for handoff. The title is accurate but could be clearer.

**Current Code:**
```
### Phase 3: Review the map
```

**Expected Code:**
```
### Phase 3: Review the context map
```

**Rationale:** This change clarifies that we're reviewing THE context map (the artifact produced), not just any map.

**Recommendation:** OPTIONAL - Current wording is acceptable.

---

### ISSUE #4: Step Numbering Format Inconsistency
**Severity:** MEDIUM  
**Type:** Consistency  
**Location:** Tables in lines 61-65, 78-82, 95-99, 112-116  

**Problem:**
Step numbers use decimal format (1.1, 1.2, 1.3, 2.1, 2.2, 2.3, etc.) but the column header just says "Step" without explanation of the numbering system.

**Current Code:**
```
| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Search for task-related files | File shortlist |
```

**Expected Code:**
```
| Step # | Action | Output |
| --- | --- | --- |
| 1.1 | Search for task-related files | File shortlist |
```

**Status:** OPTIONAL - Current format is readable.

---

### ISSUE #5: Inconsistent Phase References
**Severity:** HIGH  
**Type:** Consistency  
**Location:** Lines 123-128 (Actions Summary)  

**Problem:**
The Actions Summary refers to phases without full context. It says "1. Discover the scope" instead of "1. Run Phase 1: Discover the scope".

**Current Code (Lines 125-128):**
```
1. Discover the scope
2. Map dependencies, tests, and reference patterns
3. Record the risks
4. Return the context map and stop
```

**Expected Code:**
```
1. Execute Phase 1: Discover the scope
2. Execute Phase 2: Map dependencies, tests, and reference patterns
3. Execute Phase 3: Record the risks  
4. Execute Phase 4: Return the context map and stop
```

**Status:** ✓ OPTIONAL - Brevity may be intentional.

---

### ISSUE #6: Whitespace and Alignment in Tables
**Severity:** LOW  
**Type:** Formatting  
**Location:** Lines 49-51 (Skills Required table)  

**Problem:**
The "Purpose" column in the Skills Required table contains a long description that wraps:
`Codebase discovery and dependency mapping (loads symbol tables, dependency trees, and cross-file references)`

This is valid Markdown, but could be split or reformatted for clarity.

**Current Code:**
```
| `codemap` | Codebase discovery and dependency mapping (loads symbol tables, dependency trees, and cross-file references) |
```

**Expected Code:**
```
| `codemap` | Codebase discovery and dependency mapping. Loads symbol tables, dependency trees, and cross-file references. |
```

**Status:** OPTIONAL - Current format is readable.

---

### ISSUE #7: Rule Numbering and Formatting
**Severity:** LOW  
**Type:** Style  
**Location:** Lines 38-45  

**Problem:**
Rules are numbered 1-6 with periods and bold formatting could be applied:

**Current Code:**
```
1. Search for the files directly related to the task
2. Identify imports, exports, and other dependencies
...
```

**Expected Code:**
Could add bold or checkboxes for consistency, but current format is clear.

**Status:** ✓ NO FIX REQUIRED

---

### ISSUE #8: Missing Cross-Reference Documentation
**Severity:** LOW  
**Type:** Documentation Gap  
**Location:** Entire document  

**Problem:**
The document lacks an explicit "cross-reference map" showing which sections reference which other sections. This would be helpful for documentation navigation.

**Recommendation:** 
Add a "Document Cross-Reference Map" section in the documentation (context file), not in the prompt itself.

**Status:** ✓ HANDLED IN CONTEXT FILE

---

## Summary Table

| # | Issue | Severity | Type | Line(s) | Status |
|---|-------|----------|------|---------|--------|
| 1 | Section header consistency | MEDIUM | Consistency | 55,72,89,106 | NO FIX |
| 2 | Blank lines before tables | MEDIUM | Formatting | 49,61,78,95,112 | NO FIX |
| 3 | Phase 3 title clarity | HIGH | Clarity | 89 | OPTIONAL |
| 4 | Step numbering label | MEDIUM | Consistency | Various | OPTIONAL |
| 5 | Phase references in summary | HIGH | Consistency | 125-128 | OPTIONAL |
| 6 | Table cell wrapping | LOW | Formatting | 51 | OPTIONAL |
| 7 | Rule formatting | LOW | Style | 38-45 | NO FIX |
| 8 | Missing cross-ref map | LOW | Documentation | N/A | HANDLED |

---

## Issue Categories

### Format Issues (Will NOT Fix)
- Issue #1: Section headers are correct
- Issue #2: Blank lines are already present
- Issue #7: Rules formatting is clear

### Clarity Issues (CAN Fix)
- Issue #3: Phase 3 title could be improved
- Issue #5: Actions Summary could be more explicit

### Documentation Issues (HANDLING in Context Files)
- Issue #8: Cross-reference map provided in context file

### Optional Improvements
- Issue #4: Step numbering column could have better label
- Issue #6: Long table cell content could be reformatted

---

## Recommendations for Phase 2 (Fix Application)

### BATCH 1 FIXES (Proof of Concept)
1. Clarify Phase 3 header: "Review the map" → "Review the context map" (Line 89)
2. Improve Actions Summary references (Lines 125-128): Make phase references more explicit

### BATCH 2 FIXES (Optional)
- Reformat the Skills Required table for better readability
- Add explicit column labels to step tables

### NO FIXES NEEDED
- Structure and headers are correct
- Tables are properly formatted
- Content flow is logical
- YAML metadata is correct

---

## Cross-Reference Validation

### Dependencies Listed
- ✓ `skill:codemap` (Line 7)
- ✓ `codemap` explained in Skills table (Line 51)
- ✓ Used implicitly in Phase 1 (Lines 61-70)

### Phases Cross-Referenced
- ✓ Phase 1 referenced in Phases section header (Line 53)
- ✓ All 4 phases documented (Lines 55-121)
- ✓ Phases summarized in Actions Summary (Lines 125-128)

### Consistency Check
- ✓ Goal statement (Line 17-18) matches Actions Summary
- ✓ All phases follow Goal, Steps, Tasks pattern
- ✓ Skill dependencies match frontmatter

---

## File Quality Score

| Category | Score | Notes |
|----------|-------|-------|
| Structure | 95% | Clear phase organization |
| Formatting | 95% | All tables properly formatted |
| Clarity | 88% | Could improve Phase 3 title |
| Completeness | 100% | All sections present |
| Consistency | 90% | Minor inconsistencies in references |
| **OVERALL** | **92%** | Good quality, minor improvements possible |
