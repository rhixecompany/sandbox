---
trigger: /update-implementation-plan
description: >-
  Create or update an implementation plan with new or updated requirements for features, refactoring, package upgrades, design, or infrastructure.
tags: [hermes, copilot, planning, implementation]
dependencies:
  - skill:writing-plans
  - skill:plans-and-specs
  - command:/context-map
skills:
  - writing-plans — Author structured implementation plans
  - plans-and-specs — Plan and spec management
---

# update-implementation-plan

> Create or update an implementation plan file with new or updated requirements for features, refactoring, package upgrades, design, architecture, or infrastructure.

## Goal

Systematically create or update structured implementation plans with proper version control and status tracking. This ensures all requirements, dependencies, and implementation steps are documented and discoverable for team coordination and project tracking.

## Context

Use when you need to create or update an implementation plan for the current workspace or task. The output implementation plan follows a standard section template with status badges.

## Inputs

The following inputs are gathered to create or update an implementation plan:

- **Workspace State**: The current contents of `<workspace_root>`, including existing files, directory structure, and any plan files in the `plan/` directory. Discovered via Phase 1 file system scan.
- **User Request**: The specific request, diff, spec, or features provided by the user initiating the command. Passed as command arguments or context.
- **Plan Variables**: Any explicit prompt variables, paths, or constraints named in the original instructions (e.g., `<purpose>`, `<component>`, `<version>`). Extracted from user input.
- **Existing Plan File**: If updating an existing plan, the current content at `<workspace_root>/plan/<purpose>-<component>-<version>.md`. Loaded during Phase 1 assessment.

## Template Variables

Template variables used in this prompt follow this convention:

| Variable | Scope | Example |
| --- | --- | --- |
| `<workspace_root>` | Absolute path to project root | `C:\Users\Alexa\Desktop\Sandbox` |
| `<purpose>` | Slug derived from task/feature name | `feature-auth-refactor` |
| `<component>` | Target component or module | `database` |
| `<version>` | Plan version (typically `v1`, `v2`) | `v1` |

**Composite Example:**
When combined in the output path template, these variables produce a concrete file path:
```
<workspace_root>/plan/<purpose>-<component>-<version>.md
C:\Users\Alexa\Desktop\Sandbox\plan\feature-auth-refactor-database-v1.md
```

## Outputs

- A complete implementation plan at `<workspace_root>/plan/<purpose>-<component>-<version>.md`
- A concise verification note when the task benefits from one

## Rules

1. Use only evidence from the current workspace and the user request
2. Change only the implementation plan sections directly affected by new requirements
3. If the target file does not exist, create it at `<workspace_root>/plan/<purpose>-<component>-<version>.md` using status `Planned`
4. Use these section names: `Introduction`, `Requirements & Constraints`, `Implementation Steps`, `Alternatives`, `Dependencies`, `Files`, `Testing`, `Risks & Assumptions`, `Related Specifications / Further Reading`
5. Use the status badge template: `https://img.shields.io/badge/status-<url_encoded_status>-<color>`

### Naming Constraints for Template Variables

When creating plan file names, follow these conventions:

- **`<purpose>`**: Use lowercase hyphen-separated slugs (e.g., `feature-auth-refactor`, `bugfix-memory-leak`). Max 30 characters.
- **`<component>`**: Use lowercase hyphen-separated module/component names (e.g., `database`, `ui-components`, `auth-service`). Max 20 characters.
- **`<version>`**: Use semantic version format (e.g., `v1`, `v2`, `v1-draft`). Max 10 characters.
- **Avoid:** Spaces, special characters (!@#$%), and uppercase letters in variable values.
- **Result:** Final file names will be filesystem-safe with only alphanumeric characters and hyphens.

### Status Mapping

|| Status | shields.io color |
|| --- | --- |
|| Completed | brightgreen |
|| In progress | yellow |
|| Planned | blue |
|| Deprecated | red |
|| On Hold | orange |

### Status Usage Guidance

- **Planned** (blue): Use for newly created plans before implementation begins. Initial status for all new implementation plans.
- **In progress** (yellow): Use when implementation has begun. Update status when first implementation step is started.
- **Completed** (brightgreen): Use when all implementation steps are finished and verified. Plan is ready for reference/archive.
- **On Hold** (orange): Use when implementation is temporarily paused due to blockers, resource constraints, or priority changes.
- **Deprecated** (red): Use when plan is no longer relevant due to scope change, cancellation, or superseding by newer plan.

## Skills Required

The skills listed below in the "Skills Required" section mirror the YAML front-matter `skills` declaration and indicate which Hermes skills must be available for this prompt to execute successfully. The Hermes agent will verify skill availability before running this prompt.

| Skill | Purpose |
| --- | --- |
| `context-map` | Pre-change map of plan-related files and dependencies |
| `writing-plans` | Author structured implementation plans |
| `plans-and-specs` | Plan and spec namespace management |

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

## Actions Summary

1. Read the request and workspace state
2. Determine create vs. update mode
3. Write or update the implementation plan with standard sections
4. Apply the correct status badge
5. Verify all sections are present and accurate
