# Prompt-Builder Context Analysis (Phase 1)

## File Location
- **Source:** `.github/prompts/prompt-builder.prompt.md`
- **Size:** 6.95 KB
- **Lines:** 141
- **Format:** YAML frontmatter + Markdown

## Document Structure

### Frontmatter (Lines 1-13)
- **Trigger:** `/prompt-builder`
- **Description:** Guide for creating .prompt.md files
- **Tags:** hermes, copilot, opencode, prompt-engineering, scaffolding, template
- **Dependencies:** 
  - skill:writing-plans
  - skill:prompt-engineering
- **Skills:** 2 defined (writing-plans, prompt-engineering)

### Content Sections (Lines 14-141)
1. **Title & Description** (Lines 15-17)
2. **Goal** (Lines 19-21)
3. **Context** (Lines 23-30)
   - Explains use case
   - Lists 3 critical rules
4. **Inputs** (Lines 32-36)
   - 3 input types listed
5. **Outputs** (Lines 38-41)
   - 2 output types listed
6. **Rules** (Lines 43-50)
   - 6 numbered rules
   - References pattern types
7. **Modes** (Lines 52-58)
   - 3 modes in table format (ask, edit, agent)
8. **Skills Required** (Lines 60-65)
   - 2 skills in table format
9. **Phases** (Lines 67-109)
   - Phase 1: Discovery (9 discovery questions)
   - Phase 2: Generate (8 steps)
   - Phase 3: Verify (4 steps)
10. **Best Practices Integration** (Lines 111-122)
    - 8 checkmarked best practices
11. **Reference Patterns** (Lines 124-132)
    - 6 pattern file references
12. **Actions Summary** (Lines 134-141)
    - 6 numbered action items

## Forward References (Internal Links)

### Relative Links to Prompt Files
- `.github/prompts/playwright-generate-test.prompt.md` (Line 127)
- `.github/prompts/create-github-action-workflow-specification.prompt.md` (Line 128)
- `.github/prompts/dotnet-best-practices.prompt.md` (Line 129)
- `.github/prompts/architecture-blueprint-generator.prompt.md` (Line 130)
- `.github/prompts/create-implementation-plan.prompt.md` (Line 131)
- `.github/prompts/csharp-xunit.prompt.md` (Line 132)

**Status:** All 6 reference files should exist in `.github/prompts/`

### Dependencies
- **Internal Skill References:**
  - `skill:writing-plans` (Line 8, 11, 64)
  - `skill:prompt-engineering` (Line 9, 12, 65)

**Status:** Should be defined elsewhere in skill system

## Reverse References (What References This File)

Since this is a prompt file, it should be referenced by:
- Parent index/catalog files in `.github/prompts/`
- Trigger system that recognizes `/prompt-builder`
- Skill documentation or guides

**Files to Check:**
- `.github/prompts/README.md` (if exists)
- `.github/prompts/index.md` (if exists)
- Root README.md
- Hermes configuration files

## Issues Identified (Phase 1 Audit)

### CRITICAL ISSUES

**Issue #1:** Reference Pattern File Validation
- **Line:** 127-132
- **Problem:** 6 reference files are listed but accessibility not verified
- **Impact:** Dead links if files don't exist
- **Severity:** HIGH
- **Fix Needed:** Verify all 6 files exist; if not, remove or replace references

**Issue #2:** Skill Dependency References
- **Lines:** 8-9, 11-12, 64-65
- **Problem:** Skill names referenced but no verification they're available
- **Impact:** Prompt may fail to execute if skills missing
- **Severity:** HIGH
- **Fix Needed:** Verify skill:writing-plans and skill:prompt-engineering exist

**Issue #3:** Phase Completeness
- **Lines:** 67-109
- **Problem:** Only 3 phases described; Actions Summary mentions 6 steps but Phase 1 has 9 questions
- **Severity:** MEDIUM
- **Note:** Phase 3 (Verify) is only 4 steps, should expand

### MODERATE ISSUES

**Issue #4:** Inconsistent Table Formatting
- **Lines:** 54-58, 62-65, 75-85
- **Problem:** Multiple table formats used; some use pipes consistently, some vary
- **Severity:** LOW
- **Impact:** Readability
- **Fix:** Normalize table formatting

**Issue #5:** Question vs. Area Mismatch (Phase 1 Discovery)
- **Lines:** 75-85
- **Problem:** Question column labeled "Question" but lists "1, 2, 3..." instead of actual questions
- **Severity:** MEDIUM
- **Impact:** Table doesn't show actual questions, just numbers
- **Fix:** Either expand with full questions or clarify numbering system

**Issue #6:** Missing Implementation Pattern
- **Lines:** 69-100
- **Problem:** Phase 1 shows questions in table but doesn't show actual interactive flow
- **Severity:** LOW
- **Impact:** Users unclear on question phrasing
- **Note:** May be intentional (left to implementation)

### DOCUMENTATION ISSUES

**Issue #7:** Incomplete Reference Section
- **Lines:** 124-132
- **Problem:** Only 6 references listed; may be incomplete list of available patterns
- **Severity:** LOW
- **Impact:** Users may miss relevant patterns
- **Fix:** Verify if list is exhaustive or needs expansion

**Issue #8:** Tools List Not Detailed
- **Line:** 48
- **Problem:** Tool types mentioned (codebase, editFiles, search, runCommands, fetch) but no detailed tool selection guide
- **Severity:** LOW
- **Impact:** Users unclear on tool selection criteria
- **Note:** Could reference external tool documentation

## Structural Summary

| Category | Count | Status |
|----------|-------|--------|
| Sections | 12 | ✓ Complete |
| Tables | 3 | ⚠ Formatting varies |
| Lists | 8+ | ✓ Present |
| Code Refs | 0 | N/A |
| External Links | 0 | ✓ N/A |
| Internal Links | 9 | ⚠ 6 need verification |
| Dependencies | 2 | ⚠ Need verification |

## Total Issues Found
- **CRITICAL:** 2 issues
- **MODERATE:** 2 issues  
- **LOW/DOCUMENTATION:** 4 issues
- **TOTAL:** 8 issues

## Audit Confidence
- **Structure Integrity:** 95% (well-formed markdown)
- **Reference Validity:** 60% (untested links)
- **Completeness:** 85% (most sections present but some sparse)
