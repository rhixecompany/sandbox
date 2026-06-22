# Phases

> Extracted from `update-implementation-plan.prompt.md`.

## Phases

### Phase 1: Assess

**Goal:** Read the current workspace state and determine whether to create or update an implementation plan.

**Steps:**
1. Read the request and identify the exact scope
2. Check if an implementation plan file already exists at `<workspace_root>/plan/`
3. Locate the relevant files, diffs, or references
4. Run `/context-map` for the implementation-plan scope before writing updates

**Scope Definition Criteria:**
- **Scope** = the set of features, components, or changes described in the user request
- **Relevant Files** = any source files, configuration files, or documentation files directly affected by the scope
- **Determine Relevance** by examining: file imports, class dependencies, configuration references, and documentation cross-references

### Phase 2: Write or Update

**Goal:** Produce the implementation plan with the correct section structure.

**Steps:**
1. Create or update implementation plan sections: Introduction, Requirements & Constraints, Implementation Steps, Alternatives, Dependencies, Files, Testing, Risks & Assumptions, Related Specifications
2. Add or update the status badge in the Introduction
3. Keep the implementation plan aligned with evidence from the workspace

### Phase 3: Verify

**Goal:** Confirm the implementation plan is complete, accurate, and usable.

**Verification Checklist:**
1. ✓ All 9 required sections are present: Introduction, Requirements & Constraints, Implementation Steps, Alternatives, Dependencies, Files, Testing, Risks & Assumptions, Related Specifications / Further Reading
2. ✓ Status badge is present in Introduction and matches the plan's current state
3. ✓ All template variables in the plan are properly substituted (no `<variable>` placeholders remain)
4. ✓ Each requirement item has corresponding implementation steps
5. ✓ Dependencies section lists all external requirements (skills, services, data)
6. ✓ Files section accurately lists affected source files with brief descriptions
7. ✓ Risks section identifies potential blockers with mitigation strategies
8. ✓ No section contradicts workspace evidence or prior sections
9. ✓ All links, references, and cross-references are valid (no broken links)
