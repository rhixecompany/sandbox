# Phase 1: Issues Context - update-implementation-plan.prompt.md

## Issues Identified

### ISSUE #1: Duplicate Content in Goal Section
**Severity:** MEDIUM
**Type:** Redundancy / Inconsistency
**Location:** Lines 18-20
**Description:**
The Goal section (lines 18-20) contains nearly identical content to the main description in the quote block (lines 16). This creates redundancy.

**Current Content:**
```markdown
> Create or update an implementation plan file with new or updated requirements for features, refactoring, package upgrades, design, or infrastructure.
...
## Goal
Create or update an implementation plan file with new or updated requirements for new features, refactoring existing code, upgrading packages, or modifying design, architecture, or infrastructure.
```

**Issue:** The two statements are 95% identical with only minor wording variations. Additionally, the Goal statement is more verbose than needed and doesn't add substantial new information beyond the quote block.

**Fix Needed:** Consolidate these or make the Goal more distinct and action-oriented.

---

### ISSUE #2: Inconsistent Status Colors in Table
**Severity:** LOW
**Type:** Documentation / Convention Consistency
**Location:** Lines 57-65 (Status Mapping table)
**Description:**
The status mapping table shows 5 statuses, but the Rules section (line 53) only mentions one status: "Planned". The other statuses in the table are not referenced in the Rules or explained in context.

**Current Content:**
```markdown
|| Status | shields.io color |
|| Completed | brightgreen |
|| In progress | yellow |
|| Planned | blue |
|| Deprecated | red |
|| On Hold | orange |
```

**Issue:** Rules state "create it at ... using status `Planned`" but 5 different statuses are defined without guidance on when to use others.

**Fix Needed:** Clarify in Rules when to use each status (especially In progress, Completed, Deprecated, On Hold).

---

### ISSUE #3: Skills Section References Non-Existent Definitions
**Severity:** MEDIUM
**Type:** Clarity / Documentation Gap
**Location:** Lines 67-72
**Description:**
The "Skills Required" section lists 2 skills with purposes, but the front matter lists the same skills with identical descriptions. This creates confusion about the difference between the declaration and the requirement.

**Current Content (Front Matter):**
```yaml
skills:
  - writing-plans — Author structured implementation plans
  - plans-and-specs — Plan and spec management
```

**Current Content (Body):**
```markdown
| Skill | Purpose |
| `writing-plans` | Author structured implementation plans |
| `plans-and-specs` | Plan and spec management |
```

**Issue:** The "Skills Required" section duplicates YAML front matter information. It's unclear if this is intentional documentation or an error. If these skills should be automatically installed/referenced, the table adds no value.

**Fix Needed:** Either remove the duplicate table or clarify the distinction between front-matter skills and body-section "Skills Required".

---

### ISSUE #4: Phase 3 Verification Steps Incomplete
**Severity:** MEDIUM
**Type:** Incomplete Instructions
**Location:** Lines 94-101
**Description:**
Phase 3 is labeled "Verify" but the steps are vague and lack actionable guidance.

**Current Content:**
```markdown
### Phase 3: Verify

**Goal:** Confirm the plan is complete, accurate, and usable.

**Steps:**
1. Verify all required sections are present
2. Confirm the status badge matches the current state
3. Ensure no section contradicts workspace evidence
```

**Issue:** 
- Step 1: "all required sections" - which sections? (There are 9 mentioned, but how enforced?)
- Step 2: "status badge matches current state" - how to determine "current state"? Who determines it?
- Step 3: "contradicts workspace evidence" - too vague. What constitutes contradiction?

**Fix Needed:** Provide concrete verification checklist with specific criteria.

---

### ISSUE #5: Missing Example in Template Variables
**Severity:** LOW
**Type:** Documentation Gap
**Location:** Lines 33-42
**Description:**
The Template Variables table provides one example for `<workspace_root>` (Windows path), but no examples for `<purpose>`, `<component>`, or `<version>` variable interpolation in the context of the actual output path.

**Current Content:**
```markdown
| Variable | Scope | Example |
| `<workspace_root>` | Absolute path to project root | `C:\Users\Alexa\Desktop\Sandbox` |
| `<purpose>` | Slug derived from task/feature name | `feature-auth-refactor` |
| `<component>` | Target component or module | `database` |
| `<version>` | Plan version (typically `v1`, `v2`) | `v1` |
```

**Issue:** While individual variable examples exist, there's no composite example showing how they combine into the final path, e.g.:
```
C:\Users\Alexa\Desktop\Sandbox\plan\feature-auth-refactor-database-v1.md
```

**Fix Needed:** Add a composite example showing the full output path with variable substitution.

---

### ISSUE #6: Vague Input Description
**Severity:** LOW
**Type:** Clarity
**Location:** Lines 26-31
**Description:**
The "Inputs" section uses bullet points but lacks clarity about what each input means or how it's provided.

**Current Content:**
```markdown
## Inputs

- The current workspace, repo, or document state
- The specific request, diff, spec, or files provided by the user
- Any prompt variables, paths, or constraints named in the original instructions
- Existing plan file (if updating)
```

**Issue:** "The current workspace, repo, or document state" is too vague. How is this discovered? Is it automatic? Manual?

**Fix Needed:** Clarify the mechanism for gathering each input (e.g., "discovered via Phase 1 file scanning" or "provided by user as command argument").

---

### ISSUE #7: Phase 1 Instructions Lack Scope Definition
**Severity:** MEDIUM
**Type:** Incomplete Instructions
**Location:** Lines 76-83
**Description:**
Phase 1 (Assess) doesn't define how to determine "scope" or what constitutes "relevant files".

**Current Content:**
```markdown
### Phase 1: Assess

**Goal:** Read the current workspace state and determine whether to create or update a plan.

**Steps:**
1. Read the request and identify the exact scope
2. Check if a plan file already exists at `<workspace_root>/plan/`
3. Locate the relevant files, diffs, or references
```

**Issue:**
- Step 1: "identify the exact scope" - what does this mean? Scope of the plan? The request? The affected files?
- Step 3: "relevant files" - relevant to what? How to determine relevance?

**Fix Needed:** Provide explicit criteria for scope definition and relevance assessment.

---

### ISSUE #8: Inconsistent Terminology
**Severity:** LOW
**Type:** Terminology / Consistency
**Location:** Multiple lines
**Description:**
The prompt uses "plan file" and "implementation plan file" interchangeably without clear distinction.

**Occurrences:**
- Line 20: "implementation plan file"
- Line 23: "plan"
- Line 46: "implementation plan"
- Line 53: "plan file"
- Line 90: "plan sections"

**Issue:** Inconsistent terminology may confuse readers about what exactly is being created/updated.

**Fix Needed:** Standardize on a single term (recommend "implementation plan" or "plan file").

---

### ISSUE #9: Missing Error Handling Guidance
**Severity:** LOW
**Type:** Documentation Gap
**Location:** Entire document
**Description:**
The prompt provides instructions for the happy path (create or update a plan) but doesn't address error scenarios or edge cases.

**Examples of Missing Guidance:**
- What if `<workspace_root>/plan/` directory doesn't exist?
- What if a plan file exists but is malformed?
- What if required skills (`writing-plans`, `plans-and-specs`) are not available?
- What if shields.io service is unavailable?

**Fix Needed:** Add "Error Handling" or "Edge Cases" section with guidance.

---

### ISSUE #10: Output Path Template Not Validated
**Severity:** LOW
**Type:** Documentation Gap
**Location:** Line 46
**Description:**
The output path template uses `<purpose>`, `<component>`, and `<version>` variables without specifying naming constraints.

**Current Content:**
```markdown
A complete implementation plan at `<workspace_root>/plan/<purpose>-<component>-<version>.md`
```

**Issue:** No guidance on:
- Are these slugs? Should spaces be converted to hyphens?
- What characters are allowed/disallowed?
- What's the maximum length?
- Case sensitivity?

**Fix Needed:** Specify naming conventions for each variable.

---

## Summary Statistics

- **Total Issues Found:** 10
- **Critical Severity:** 0
- **Medium Severity:** 5 (Issues #1, #2, #3, #4, #7)
- **Low Severity:** 5 (Issues #5, #6, #8, #9, #10)

## Categorization

### Redundancy Issues (1)
- Issue #1: Duplicate Goal content

### Clarity/Documentation Gaps (6)
- Issue #3: Skills table duplication
- Issue #4: Vague Phase 3 steps
- Issue #5: Missing composite example
- Issue #6: Vague input descriptions
- Issue #7: Unclear scope definition in Phase 1
- Issue #9: Missing error handling

### Consistency Issues (2)
- Issue #2: Status color guidance incomplete
- Issue #8: Inconsistent terminology

### Validation Issues (1)
- Issue #10: No naming constraints for variables

## Recommended Fix Priority

1. **High Impact, Low Effort:**
   - Issue #1 (Redundancy) - Remove duplicate Goal
   - Issue #8 (Terminology) - Standardize naming
   
2. **High Impact, Medium Effort:**
   - Issue #2 (Status guidance) - Clarify when to use each status
   - Issue #3 (Skills duplication) - Consolidate or clarify
   - Issue #7 (Phase 1 clarity) - Add explicit criteria
   
3. **Medium Impact, Medium Effort:**
   - Issue #4 (Phase 3 verification) - Create concrete checklist
   - Issue #6 (Input clarity) - Detail input gathering mechanism
   
4. **Lower Impact, Low Effort:**
   - Issue #5 (Composite example) - Add full path example
   - Issue #9 (Error handling) - Document edge cases
   - Issue #10 (Naming constraints) - Specify conventions
