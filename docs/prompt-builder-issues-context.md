# Prompt-Builder Issues Context (Phase 1 Findings)

## Total Issues Cataloged: 8

---

## CRITICAL ISSUES (2)

### Issue #1: Missing Reference Files
**Location:** Lines 129, 132  
**Severity:** CRITICAL  
**Type:** Broken References

**Details:**
- File references 6 prompt patterns for new users to learn from
- **Missing Files:**
  - `.github/prompts/dotnet-best-practices.prompt.md` (Line 129) — NOT FOUND
  - `.github/prompts/csharp-xunit.prompt.md` (Line 132) — NOT FOUND

**Verified Existing (4/6):**
- ✅ `playwright-generate-test.prompt.md` (Line 127) — EXISTS
- ✅ `create-github-action-workflow-specification.prompt.md` (Line 128) — EXISTS  
- ✅ `architecture-blueprint-generator.prompt.md` (Line 130) — EXISTS
- ✅ `create-implementation-plan.prompt.md` (Line 131) — EXISTS

**Impact:**
- Users following this prompt will encounter broken reference links
- Trust in documentation reduces
- Pattern learning blocked for those 2 reference types

**Recommended Fixes:**
1. **Option A:** Create the missing files (preferred if patterns needed)
2. **Option B:** Remove the missing references and note them as "planned"
3. **Option C:** Replace with existing equivalents

**Batch 1 Fix Strategy:** Remove the 2 missing references; mark as placeholder for future

---

### Issue #2: Unverified Skill Dependencies
**Location:** Lines 8-9, 11-12 (frontmatter); Lines 64-65 (skills table)  
**Severity:** CRITICAL  
**Type:** Dependency Validation

**Details:**
- Frontmatter declares dependency on 2 skills:
  - `skill:writing-plans`
  - `skill:prompt-engineering`
- No verification these skills exist or are accessible

**Problem:**
- Prompt will fail at runtime if skills aren't available
- No fallback or alternative provided
- Skill system integration unclear

**Impact:**
- Prompt execution will fail silently or with cryptic error
- User experience degraded
- System reliability questionable

**Recommended Fixes:**
1. Verify skill:writing-plans exists in codebase
2. Verify skill:prompt-engineering exists in codebase
3. If missing: document where skills should come from or provide inline alternatives
4. Add note: "Requires XYZ skill system" with version/dependency info

**Batch 1 Fix Strategy:** Document that skill verification needed (cannot fix without skill system access)

---

## MODERATE ISSUES (2)

### Issue #3: Discovery Questions Table Incomplete
**Location:** Lines 75-85 (Phase 1 Discovery table)  
**Severity:** MODERATE  
**Type:** Documentation Clarity

**Details:**
Current table format:
```
| Question | Area | Details |
| 1 | Prompt Identity & Purpose | Filename, one-sentence description, category |
| 2 | Persona Definition | Role, expertise level, domain knowledge, qualifications |
...etc (9 rows total)
```

**Problem:**
- "Question" column shows numbers (1-9) not actual questions
- Users don't see what questions will be asked
- Creates disconnect between "9 discovery questions" concept and actual implementation
- Table is more of a rubric/template than a question guide

**Impact:**
- Users expect to see questions; get only numbered categories instead
- Reduces usability as a reference
- Unclear what prompt will actually ask

**Recommended Fixes:**
1. Expand Question column to show actual question text (e.g., "What is the filename and primary purpose?")
2. OR: Rename column to "Question #" or "Topic" to clarify it's a category not a question
3. OR: Add a separate section "Actual Questions Asked" with full text

**Batch 1 Fix Strategy:** Rename "Question" column to "Topic #" for clarity; add note that actual questions shown during execution

---

### Issue #4: Tool Selection Guidance Missing
**Location:** Line 48  
**Severity:** MODERATE  
**Type:** Documentation Completeness

**Details:**
Line 48 mentions tool types in parentheses:
> Select appropriate tools (codebase, editFiles, search, runCommands, fetch, etc.)

**Problem:**
- Lists tool names but no selection criteria or guidance
- How does user/prompt choose which tools?
- No examples of tool usage for different task types
- "etc." suggests incomplete list

**Impact:**
- Users can't make informed tool selection
- May select wrong tools, leading to failed prompts
- Documentation feels incomplete

**Recommended Fixes:**
1. Create tool selection matrix: Task Type → Tools
2. Add examples: "For code analysis: use codebase + search"
3. Document tool purpose and constraints
4. Clarify what "etc." includes

**Batch 1 Fix Strategy:** Add brief tool selection guidelines inline; reference external guide if available

---

## LOW-PRIORITY ISSUES (4)

### Issue #5: Table Formatting Inconsistency
**Location:** Lines 54-58 (Modes), 62-65 (Skills), 75-85 (Questions)  
**Severity:** LOW  
**Type:** Style/Consistency

**Details:**
- All 3 tables follow same pipe format but spacing/alignment varies slightly
- Modes table: 3 columns, 4 rows
- Skills table: 2 columns, 3 rows  
- Questions table: 3 columns, 10 rows
- Some tables have header underlines, some don't (markdown renders same either way)

**Impact:**
- Minor readability issue
- No functional impact
- Lint tools would flag inconsistency

**Recommended Fixes:**
1. Normalize all tables to same format
2. Ensure consistent spacing and alignment
3. Use markdown linter to validate

**Batch 1 Fix Strategy:** Skip or defer (low priority)

---

### Issue #6: Phase 3 (Verify) Lacks Detail
**Location:** Lines 101-109  
**Severity:** LOW  
**Type:** Documentation Completeness

**Details:**
- Phase 1 (Discovery): 9 detailed questions
- Phase 2 (Generate): 8 detailed steps
- Phase 3 (Verify): Only 4 generic steps
- Verify phase feels rushed compared to others

**Current Verify Steps:**
1. Verify all required sections present
2. Check against pattern references
3. Confirm token-efficient and well-structured
4. Present final file path

**Problem:**
- Step 4 ("Present final file path") is trivial, not verification
- No testing/validation steps mentioned
- No error handling covered

**Impact:**
- Users may not verify prompts are actually functional
- No quality gate at end of workflow
- Incomplete picture of workflow

**Recommended Fixes:**
1. Add step: "Test prompt with sample input"
2. Add step: "Validate all tool references exist"
3. Add step: "Review for ambiguous language"
4. Rename step 4 or integrate into closing summary

**Batch 1 Fix Strategy:** Expand Phase 3 with 2-3 additional validation steps

---

### Issue #7: Context Rules Hard to Find
**Location:** Lines 27-30  
**Severity:** LOW  
**Type:** Information Architecture

**Details:**
- "Critical rules (must appear within the first 15% of execution)" mentioned in Context section
- But rules are scattered across file:
  - Lines 27-30: "Critical rules" (3 rules)
  - Lines 43-50: "Rules" section (6 rules)
- Unclear what applies when

**Problem:**
- 9 total rules across 2 sections
- "Critical" designation only for 3; what about other 6?
- Execution order and precedence unclear

**Impact:**
- Users may miss critical rules
- Confusion about rule hierarchy
- Reduces guidance effectiveness

**Recommended Fixes:**
1. Consolidate to single Rules section with priority markers
2. Mark critical rules with ⚠️ icon or **CRITICAL** label
3. Clarify execution phase for each rule

**Batch 1 Fix Strategy:** Add priority markers to all rules (defer consolidation)

---

### Issue #8: Best Practices List Not Sourced
**Location:** Lines 113-122  
**Severity:** LOW  
**Type:** Documentation Attribution

**Details:**
- "Based on analysis of existing prompts, ensure the generated prompt includes:"
- Lists 8 best practices with checkmarks
- No source attribution or examples cited

**Problem:**
- Claims based on "analysis of existing prompts" but doesn't show which ones
- Could be user's opinion not backed by data
- No way to verify or learn from examples

**Impact:**
- Credibility reduced
- Users can't learn from examples
- Makes it sound like opinion rather than established practice

**Recommended Fixes:**
1. Add example reference prompts for each practice
2. Show which existing prompts exemplify each practice
3. Or: Move to general best practices section with explicit sourcing

**Batch 1 Fix Strategy:** Add brief examples inline (e.g., "Clear Structure: see architecture-blueprint-generator.prompt.md")

---

## Summary Table

| Issue # | Title | Severity | Type | Lines | Fixable in Batch 1 |
|---------|-------|----------|------|-------|-------------------|
| #1 | Missing Reference Files | CRITICAL | Refs | 129, 132 | ✅ YES (remove refs) |
| #2 | Unverified Skills | CRITICAL | Deps | 8-9, 11-12, 64-65 | ⚠️ PARTIAL (document) |
| #3 | Discovery Questions Table | MODERATE | Doc | 75-85 | ✅ YES (rename) |
| #4 | Tool Selection Guidance | MODERATE | Doc | 48 | ✅ YES (add guide) |
| #5 | Table Formatting | LOW | Style | 54-85 | ⏭️ DEFER |
| #6 | Phase 3 Detail | LOW | Doc | 101-109 | ✅ YES (expand) |
| #7 | Rules Organization | LOW | Info Arch | 27-30, 43-50 | ⏭️ DEFER |
| #8 | Best Practices Sourcing | LOW | Attribution | 113-122 | ✅ YES (add refs) |

**Batch 1 Fixable Issues: 5 of 8**
- Remove 2 missing file references
- Document skill verification need
- Rename discovery table column  
- Add tool selection guidance
- Expand Phase 3 validation steps
- Add best practices example references

**Total Defects to Fix: 8**  
**Priority Fixes (CRITICAL/MODERATE): 4**  
**Cosmetic/Deferred: 4**
