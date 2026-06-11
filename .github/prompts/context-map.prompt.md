---
trigger: /context-map
description: >-
  Build a dependency and reference map before making changes so implementation starts from the right files.
tags: [hermes, copilot, analysis, dependencies, planning]
dependencies:
  - skill:codemap
skills:
  - codemap — Codebase discovery and dependency mapping
---

# context-map

> Build a dependency-aware context map before implementation begins.

## Goal

Build a dependency and reference map before making changes so implementation starts from the right files.

## Context

- Use when the task needs a safe pre-change inventory
- Focus on direct dependencies, related tests, and nearby patterns
- Keep the map concrete and file-driven
- Do not proceed to implementation until the map is reviewed

## Inputs

- Task description
- Optional target area, feature, or bug report
- Optional constraints or known files

## Outputs

- A context map with files to modify, dependencies, tests, and reference patterns
- A short risk assessment
- Present the context map as a Markdown table with columns: File | Role (modify/dependency/test) | Notes
- Follow with a bulleted risk assessment of 3-5 items max

## Rules

1. If the task description is too vague to identify specific files, stop and ask the user to clarify the target area before proceeding to Phase 1
2. Search for the files directly related to the task
3. Identify imports, exports, and other dependencies
4. Identify the likely test files
5. If no related test files are found, explicitly state "No related tests identified" in the map and flag it as a risk item
6. Find 2-3 existing code examples in the codebase that demonstrate the same pattern (for example, same hook usage, same module export style) that the new change should follow
7. Call out breaking-change risks clearly
8. Stop after mapping; do not implement yet

## Skills Required

| Skill | Purpose |
| --- | --- |
| `codemap` | Codebase discovery and dependency mapping (loads symbol tables, dependency trees, and cross-file references) |

## Phases

### Phase 1: Discover the scope

**Goal:** find the files and relationships that matter.

#### Steps

| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Search for task-related files | File shortlist |
| 1.2 | Map direct dependencies | Dependency list |
| 1.3 | Identify related tests and patterns | Reference list |

#### Tasks
- Start from the target area
- Follow imports and exports
- Include tests that may change

### Phase 2: Build the context map

**Goal:** turn the findings into a usable planning artifact.

#### Steps

| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Organize files to modify | Modify list |
| 2.2 | Organize dependent files and tests | Dependency and test lists |
| 2.3 | Add reference patterns and risks | Context map |

#### Tasks
- Keep the table output concise
- Make the map easy to scan
- Highlight anything that may block the change

### Phase 3: Review the context map

**Goal:** confirm the map is complete enough to start work.

#### Steps

| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Check for missing files or dependencies | Gap list |
| 3.2 | Check for unclear risk items | Risk notes |
| 3.3 | Prepare the final map | Review-ready map |

#### Tasks
- Remove unnecessary detail
- Keep the map current and specific
- Make sure the affected tests are visible

### Phase 4: Verify and hand off

**Goal:** hand off a usable pre-implementation map.

#### Steps

| Step | Action | Output |
| --- | --- | --- |
| 4.1 | Summarize the scope | Summary |
| 4.2 | Present the map | Context map |
| 4.3 | State the main risks | Risk assessment |

#### Tasks
- Keep the handoff short
- Make the next step obvious
- Do not implement the change here

## Actions Summary

1. **Phase 1:** Discover the scope
2. **Phase 2:** Map dependencies, tests, and reference patterns
3. **Phase 3:** Record the risks and review completeness
4. **Phase 4:** Return the context map and stop
