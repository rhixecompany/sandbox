# Phase 2: Fix Issues Context - update-implementation-plan.prompt.md

## Batch 1 Fixes Applied

**Date:** 2026-05-25
**Status:** COMPLETED
**Issues Fixed:** 2/10

### Summary of Changes

#### Fix #1: Goal Section Replacement
**Issue:** Duplicate content between quote block and Goal section
**Type:** Content replacement
**Lines Changed:** 18-20

**Before:**
```markdown
## Goal

Create or update an implementation plan file with new or updated requirements for new features, refactoring existing code, upgrading packages, or modifying design, architecture, or infrastructure.
```

**After:**
```markdown
## Goal

Systematically create or update structured implementation plans with proper version control and status tracking. This ensures all requirements, dependencies, and implementation steps are documented and discoverable for team coordination and project tracking.
```

**Impact:**
- Removed redundancy with quote block
- Made Goal more action-oriented and value-focused
- Clarified the WHY behind the process
- Added context about team coordination benefits

---

#### Fix #2: Terminology Standardization
**Issue:** Inconsistent use of "plan" vs "implementation plan"
**Type:** Terminology normalization
**Total Occurrences Changed:** 5 locations

**Changes Made:**

| Line | Before | After | Justification |
|------|--------|-------|---------------|
| 24 | "use when you need to create or update a plan" | "use when you need to create or update an implementation plan" | Consistency with title |
| 24 | "The output plan follows" | "The output implementation plan follows" | Specificity |
| 52 | "Change only the plan sections" | "Change only the implementation plan sections" | Specificity |
| 90 | "Create or update plan sections" | "Create or update implementation plan sections" | Consistency |
| 91 | "Keep the plan aligned" | "Keep the implementation plan aligned" | Consistency |
| 108 | "Write or update the plan with" | "Write or update the implementation plan with" | Consistency |

**Impact:**
- All references now consistently use "implementation plan"
- Reduced ambiguity about what type of plan is being discussed
- Improved document searchability and consistency

---

## Verification of Batch 1 Changes

### Change Validation Checklist
- [x] Goal section now contains distinct, action-oriented content
- [x] Goal section is not redundant with quote block
- [x] All instances of "plan" standardized to "implementation plan" (where appropriate)
- [x] Terminology changes don't alter functionality or intent
- [x] Markdown formatting remains valid
- [x] Document still reads naturally after changes
- [x] No accidental content loss

### Issues Remaining (8/10)

| Issue | Severity | Status | Notes |
|-------|----------|--------|-------|
| #2: Status color guidance | MEDIUM | Pending Batch 2 | Requires phase guidance documentation |
| #3: Skills table duplication | MEDIUM | Pending Batch 2 | Needs consolidation strategy |
| #4: Phase 3 incomplete steps | MEDIUM | Pending Batch 2 | Needs concrete verification checklist |
| #5: Missing composite example | LOW | Pending Batch 3 | Add full path example |
| #6: Vague input description | LOW | Pending Batch 3 | Clarify input gathering mechanism |
| #7: Phase 1 scope definition | MEDIUM | Pending Batch 2 | Needs explicit scope criteria |
| #9: Missing error handling | LOW | Pending Batch 4 | Requires design decision |
| #10: No naming constraints | LOW | Pending Batch 3 | Specify variable constraints |

---

## Batch 2 Planning

**Target Issues:** #2, #3, #4, #7 (4 issues)

### Batch 2.1: Status Usage Guidance
**Issue #2** - The Status Mapping table lists 5 statuses but provides no guidance on when to use each.

**Proposed Fix:**
Add guidance text after the Status Mapping table explaining when to use each status.

**New Content to Add:**
```markdown
### Status Usage Guidance

- **Planned** (blue): Use for newly created plans before implementation begins. Initial status for all new implementation plans.
- **In progress** (yellow): Use when implementation has begun. Update status when first implementation step is started.
- **Completed** (brightgreen): Use when all implementation steps are finished and verified. Plan is ready for reference/archive.
- **On Hold** (orange): Use when implementation is temporarily paused due to blockers, resource constraints, or priority changes.
- **Deprecated** (red): Use when plan is no longer relevant due to scope change, cancellation, or superseding by newer plan.
```

---

### Batch 2.2: Phase 1 Scope Definition
**Issue #7** - Phase 1 instructions don't define what constitutes "scope" or "relevant files".

**Proposed Fix:**
Expand Phase 1 with explicit scope definition criteria.

**New Content to Add:**
```markdown
**Scope Definition Criteria:**
- **Scope** = the set of features, components, or changes described in the user request
- **Relevant Files** = any source files, configuration files, or documentation files directly affected by the scope
- **Determine Relevance** by examining: file imports, class dependencies, configuration references, and documentation cross-references
```

---

### Batch 2.3: Phase 3 Verification Checklist
**Issue #4** - Phase 3 verification steps are vague and not actionable.

**Proposed Fix:**
Replace vague steps with concrete, testable verification items.

**New Content:**
```markdown
### Phase 3: Verify

**Goal:** Confirm the implementation plan is complete, accurate, and usable.

**Verification Checklist:**
1. ✓ All 9 required sections are present: Introduction, Requirements & Constraints, Implementation Steps, Alternatives, Dependencies, Files, Testing, Risks & Assumptions, Related Specifications / Further Reading
2. ✓ Status badge is present in Introduction and matches the plan's current state
3. ✓ All template variables in the plan are properly substituted (no `<variable>` placeholders remain)
4. ✓ Each Requirements item has corresponding Implementation Steps
5. ✓ Dependencies section lists all external requirements (skills, services, data)
6. ✓ Files section accurately lists affected source files with brief descriptions
7. ✓ Risks section identifies potential blockers with mitigation strategies
8. ✓ No section contradicts workspace evidence or prior sections
9. ✓ All links, references, and cross-references are valid (no broken links)
```

---

### Batch 2.4: Skills Documentation
**Issue #3** - Skills table duplicates front-matter information without clear purpose.

**Proposed Fix:**
Add explanatory text clarifying the relationship between front-matter skills and body-section skills.

**New Content to Add (before Skills Required table):**
```markdown
The skills listed below in the "Skills Required" section mirror the YAML front-matter `skills` declaration and indicate which Hermes skills must be available for this prompt to execute successfully. The Hermes agent will verify skill availability before running this prompt.
```

---

## Files Modified

- **Source:** `.github/prompts/update-implementation-plan.prompt.md`
  - 6 lines modified
  - Total changes: 5 terminology updates + 1 goal section replacement
  - File size: ~4.0 KB (unchanged)
  - Status: Ready for Batch 2 fixes

---

## Next Steps (Batch 2)

1. Apply all 4 fixes (Status guidance, Phase 1 criteria, Phase 3 checklist, Skills documentation)
2. Validate markdown formatting
3. Cross-reference changes with Phase 1 audit findings
4. Proceed to Phase 3 for any remaining fixes

---

## Metrics

- **Issues Fixed (Batch 1):** 2/10 (20%)
- **Issues Fixed (Total):** 2/10
- **Lines Modified:** 6 lines
- **Severity Reduction:** Eliminated 1 MEDIUM issue (redundancy), improved 1 MEDIUM issue (terminology)
- **Documentation Created:** 3 files (context, issues, debug plan)
- **Time Estimate for Batch 2:** ~15-20 minutes
