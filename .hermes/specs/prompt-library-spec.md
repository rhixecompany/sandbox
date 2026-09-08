---
name: prompt-library-spec
title: "Prompt Library Specification"
description: "Structured prompt library with category/trigger organization and companion files"
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - prompt-library
  - prompt-management
  - structure
  - organization
---

# Prompt Library Specification

## Overview

Defines the complete structure for the prompt library at `/.github/prompts/` with category/trigger organization and mandatory companion files for each prompt.

## Requirements

### REQ-PL-001: Category Structure
- **Location**: `/.github/prompts/{category}/`
- **Categories** (13 total):
  1. `development` - Code creation, refactoring, debugging
  2. `planning` - Planning, specs, breakdown
  3. `creative` - Creative content, design, writing
  4. `testing` - Test creation, execution, validation
  5. `documentation` - Docs generation, maintenance
  6. `debugging` - Debugging, troubleshooting
  7. `security` - Security review, compliance
  8. `devops` - CI/CD, deployment, infrastructure
  9. `mcp` - MCP server management
  10. `research` - Research, analysis, synthesis
  11. `productivity` - Productivity, automation
  12. `github` - GitHub operations, PRs, issues
  13. `qa` - Quality assurance, auditing

### REQ-PL-002: Trigger Structure
- **Location**: `/.github/prompts/{category}/{trigger}/`
- **Trigger**: Specific action or event that invokes the prompt
- **Naming**: kebab-case, descriptive (e.g., `create-feature`, `fix-bug`, `write-test`)
- **Minimum**: 1 trigger per category

### REQ-PL-003: Prompt File Structure
- **Main File**: `{prompt-name}.prompt.md`
- **Companion Files** (10 required):
  1. `specs.md` - Links to .hermes/specs/ specification
  2. `plans.md` - Links to .hermes/plans/ implementation plan
  3. `goals.md` - High-level goals and success metrics
  4. `subgoals.md` - Decomposed sub-goals with owners
  5. `rules.md` - Business rules, constraints, invariants
  6. `phases.md` - Phase definitions with entry/exit criteria
  7. `steps.md` - Detailed step-by-step instructions
  8. `tasks.md` - Individual tasks with assignees
  9. `actions.md` - Specific actions/commands to execute
  10. `gates.md` - Verification gates with pass/fail criteria

### REQ-PL-004: Prompt Frontmatter
Required YAML frontmatter fields:
```yaml
---
name: {category}/{trigger}/{prompt-name}
title: "{Prompt Name}"
description: "Brief description"
version: 1.0.0
author: Hermes Agent
license: MIT
category: {category}
trigger: {trigger}
tags: [tag1, tag2]
skills_required: [skill1, skill2, ...]
tools_required: [tool1, tool2, ...]
companion_files:
  - specs.md
  - plans.md
  - goals.md
  - subgoals.md
  - rules.md
  - phases.md
  - steps.md
  - tasks.md
  - actions.md
  - gates.md
---
```

### REQ-PL-005: Cross-Reference Integrity
- Each prompt's `specs.md` must reference valid spec in `.hermes/specs/`
- Each prompt's `plans.md` must reference valid plan in `.hermes/plans/`
- `goals.md` → `subgoals.md` → `tasks.md` traceability chain
- `phases.md` → `steps.md` → `actions.md` execution chain
- `rules.md` constrains all other files
- `gates.md` validates all phases complete

## Acceptance Criteria

### AC-PL-001: Category Coverage
- [ ] All 13 categories exist as directories
- [ ] Each category has ≥1 trigger directory
- [ ] No empty categories

### AC-PL-002: Prompt Completeness
- [ ] Each prompt directory has 11 files (.prompt.md + 10 companions)
- [ ] All frontmatter fields present and valid
- [ ] No missing companion files

### AC-PL-003: Cross-Reference Validity
- [ ] All specs.md references resolve to existing spec files
- [ ] All plans.md references resolve to existing plan files
- [ ] No broken internal links

### AC-PL-004: Structural Consistency
- [ ] All prompts follow same file structure
- [ ] Naming conventions consistent
- [ ] No duplicate prompt names within category

## File Templates

### Template: specs.md
```markdown
# Specs for {Prompt Name}

## Linked Specification
- **Spec File**: `.hermes/specs/{spec-name}.md`
- **Spec Version**: 1.0.0
- **Requirements Covered**: [REQ-XXX, REQ-YYY]

## Requirements Traceability
| Requirement | Spec Section | Verification |
|-------------|--------------|--------------|
| REQ-XXX | Section X | Gate X |
```

### Template: plans.md
```markdown
# Plans for {Prompt Name}

## Linked Plan
- **Plan File**: `.hermes/plans/{plan-name}.md`
- **Plan Version**: 1.0.0
- **Phases**: [Preparation, Execution, Verification, Completion]

## Plan Traceability
| Phase | Plan Section | Status |
|-------|--------------|--------|
| Preparation | Phase 1 | Pending |
```

### Template: goals.md
```markdown
# Goals for {Prompt Name}

## Primary Goal
{One sentence describing the primary outcome}

## Success Metrics
- Metric 1: {measurable target}
- Metric 2: {measurable target}

## Secondary Goals
- Goal 1: {description}
- Goal 2: {description}
```

### Template: subgoals.md
```markdown
# Subgoals for {Prompt Name}

| Subgoal | Owner | Dependencies | Status |
|---------|-------|--------------|--------|
| SG-1: {description} | {role} | - | Pending |
| SG-2: {description} | {role} | SG-1 | Pending |
```

### Template: rules.md
```markdown
# Rules for {Prompt Name}

## Invariants
- Rule 1: {immutable constraint}
- Rule 2: {immutable constraint}

## Constraints
- Constraint 1: {conditional limit}
- Constraint 2: {conditional limit}

## Business Rules
- Rule 1: {domain-specific rule}
```

### Template: phases.md
```markdown
# Phases for {Prompt Name}

## Phase 1: Preparation
- **Entry Criteria**: {conditions}
- **Exit Criteria**: {conditions}
- **Duration**: {estimate}

## Phase 2: Execution
- **Entry Criteria**: {conditions}
- **Exit Criteria**: {conditions}
- **Duration**: {estimate}

## Phase 3: Verification
- **Entry Criteria**: {conditions}
- **Exit Criteria**: {conditions}
- **Duration**: {estimate}

## Phase 4: Completion
- **Entry Criteria**: {conditions}
- **Exit Criteria**: {conditions}
- **Duration**: {estimate}
```

### Template: steps.md
```markdown
# Steps for {Prompt Name}

## Phase 1: Preparation
### Step 1.1: {name}
- **Action**: {description}
- **Tool**: {tool name}
- **Output**: {expected output}

## Phase 2: Execution
### Step 2.1: {name}
- **Action**: {description}
- **Tool**: {tool name}
- **Output**: {expected output}
```

### Template: tasks.md
```markdown
# Tasks for {Prompt Name}

| Task ID | Description | Phase | Assignee | Status | Dependencies |
|---------|-------------|-------|----------|--------|--------------|
| T-1 | {description} | Preparation | {role} | Pending | - |
| T-2 | {description} | Execution | {role} | Pending | T-1 |
```

### Template: actions.md
```markdown
# Actions for {Prompt Name}

## Task T-1: {description}
### Action 1.1
```bash
{command}
```
- **Expected Output**: {description}
- **Verification**: {check}

## Task T-2: {description}
### Action 2.1
```bash
{command}
```
```

### Template: gates.md
```markdown
# Gates for {Prompt Name}

## Gate 1: Preparation Complete
- **Criteria**: All Phase 1 tasks verified
- **Check**: {verification command}
- **Pass Condition**: {condition}
- **Fail Action**: {remediation}

## Gate 2: Execution Complete
- **Criteria**: All Phase 2 tasks verified
- **Check**: {verification command}
- **Pass Condition**: {condition}
- **Fail Action**: {remediation}

## Gate 3: Verification Complete
- **Criteria**: All gates pass
- **Check**: {verification command}
- **Pass Condition**: All ACs met
- **Fail Action**: Re-execute failed phases

## Gate 4: Completion Verified
- **Criteria**: All artifacts created, validated
- **Check**: {final validation command}
- **Pass Condition**: Zero errors, all ACs met
- **Fail Action**: Full rollback
```

## Verification Gates

### Gate 1: Structure Validation
- All 13 categories exist
- Each category has ≥1 trigger
- Each trigger has 11 files

### Gate 2: Content Validation
- All frontmatter valid YAML
- All required fields present
- Cross-references resolve

### Gate 3: Template Compliance
- All companion files follow templates
- No placeholder text
- Consistent formatting

## Dependencies
- .hermes/specs/ specifications exist
- .hermes/plans/ plans exist
- Multi-file protocol (≥3 files) followed

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Missing companion files | High | High | Automated validation script |
| Broken cross-references | Medium | High | Verification gate checks |
| Inconsistent templates | Medium | Medium | Template enforcement in skill |