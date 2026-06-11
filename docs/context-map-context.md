# Context-Map Prompt - Phase 1: Catalog & Audit Context

**File:** `.github/prompts/context-map.prompt.md`  
**Size:** 3,324 bytes | 128 lines  
**Analysis Date:** 2026-05-25  

## Document Structure Overview

### Part 1: YAML Frontmatter (Lines 1-10)
- Metadata: trigger, description, tags, dependencies, skills
- Purpose: Prompt configuration and discovery

### Part 2: Header & Overview (Lines 12-50)
- Title: `# context-map`
- Goal: Describe purpose of the prompt
- Context: Usage guidelines (4 bullet points)
- Inputs: What users provide (3 items)
- Outputs: What the prompt delivers (2 items)
- Rules: 6 numbered rules for execution
- Skills Required: 1 table with codemap skill

### Part 3: Main Content - Phases (Lines 53-121)
- **Phase 1: Discover the scope** (Lines 55-70)
  - Goal: Find files and relationships
  - 3 steps with step table (Lines 61-65)
  - 3 tasks (Lines 67-70)

- **Phase 2: Build the context map** (Lines 72-87)
  - Goal: Turn findings into planning artifact
  - 3 steps with step table (Lines 77-82)
  - 3 tasks (Lines 84-87)

- **Phase 3: Review the map** (Lines 89-104)
  - Goal: Confirm map completeness
  - 3 steps with step table (Lines 94-99)
  - 3 tasks (Lines 101-104)

- **Phase 4: Verify and hand off** (Lines 106-121)
  - Goal: Hand off usable map
  - 3 steps with step table (Lines 111-116)
  - 3 tasks (Lines 118-121)

### Part 4: Actions Summary (Lines 123-128)
- 4-point action list summarizing workflow

## Dependency & Reference Map

### External Dependencies
- **skill:codemap** - Referenced in YAML dependencies and Skills Required table
  - Purpose: Codebase discovery and dependency mapping

### Internal Cross-References

#### Forward References (Section introduces concept used later)
1. Line 7: Lists "skill:codemap" dependency
2. Line 51: Skills table explains codemap
3. Line 53: Header "Phases" introduces phases structure
4. Lines 55-121: Four phases detailed in sequence

#### Reverse References (Later sections reference earlier definitions)
1. Line 123-128: Actions Summary summarizes all phases
2. Phase descriptions repeat and build on Goal (Line 17-18)

#### Implicit Structure References
- YAML frontmatter dependencies → Skills Required table alignment
- Phase headers → Phase steps tables
- Phase tasks → Actions Summary

## Content Inventory

### Tables (5 total)
| # | Location | Name | Rows | Columns | Content |
|---|----------|------|------|---------|---------|
| 1 | Lines 49-51 | Skills Required | 1 | 2 | codemap skill |
| 2 | Lines 61-65 | Phase 1 Steps | 3 | 3 | Steps 1.1, 1.2, 1.3 |
| 3 | Lines 77-82 | Phase 2 Steps | 3 | 3 | Steps 2.1, 2.2, 2.3 |
| 4 | Lines 94-99 | Phase 3 Steps | 3 | 3 | Steps 3.1, 3.2, 3.3 |
| 5 | Lines 111-116 | Phase 4 Steps | 3 | 3 | Steps 4.1, 4.2, 4.3 |

### Lists
- **Bullet Lists:** 6 lists (Context, Inputs, Outputs, and task lists in each phase)
- **Numbered Lists:** 1 list (Rules section)
- **Total List Items:** 23

### Sections by Hierarchy
```
# context-map (title)
  ## Goal
  ## Context
  ## Inputs
  ## Outputs
  ## Rules
  ## Skills Required
  ## Phases
    ### Phase 1: Discover the scope
      #### Steps
      #### Tasks
    ### Phase 2: Build the context map
      #### Steps
      #### Tasks
    ### Phase 3: Review the map
      #### Steps
      #### Tasks
    ### Phase 4: Verify and hand off
      #### Steps
      #### Tasks
  ## Actions Summary
```

## Document Statistics

| Metric | Value |
|--------|-------|
| Total Lines | 128 |
| Total Sections | 8 major + 12 subsections |
| Heading Levels Used | 1-4 (# ## ### ####) |
| Blockquotes | 1 (Line 14) |
| Tables | 5 |
| Numbered Lists | 1 |
| Bullet Lists | 6 |
| Total List Items | 23 |
| External Dependencies | 1 (codemap skill) |
| Phase Steps | 12 (4 phases × 3 steps each) |
| Blank Lines | 35+ |

## Structure Quality Assessment

### Strengths
1. ✓ Clear phase-based workflow (4 phases)
2. ✓ Consistent step numbering (X.Y format)
3. ✓ Each phase has clear Goal, Steps, and Tasks
4. ✓ YAML metadata well-formed
5. ✓ All tables properly formatted with pipes and separators
6. ✓ Logical flow from discovery → mapping → review → handoff

### Format Validation
1. ✓ YAML frontmatter syntax correct (--- markers present)
2. ✓ Markdown headers proper (no skipped levels)
3. ✓ Table syntax valid (pipe delimiters, separator rows)
4. ✓ List markers consistent (hyphens for bullets, digits for numbered)
5. ✓ Blockquote syntax correct (> marker)

## Completeness Check

- [x] Goal clearly stated (Line 17-18)
- [x] Context provided (Lines 20-25)
- [x] Inputs specified (Lines 27-31)
- [x] Outputs described (Lines 33-36)
- [x] Rules documented (Lines 38-45)
- [x] Skills required listed (Lines 47-51)
- [x] Four phases fully detailed (Lines 53-121)
- [x] Each phase has steps and tasks
- [x] Actions summary provided (Lines 123-128)

## Consistency Verification

- Phase step numbering: Consistent (N.1, N.2, N.3 pattern)
- Table formatting: Consistent across all 5 tables
- Header hierarchy: Consistent (proper nesting)
- List markers: Consistent (- for bullets, numbers for numbered lists)
- Content organization: Consistent (Goal → Steps → Tasks pattern)
