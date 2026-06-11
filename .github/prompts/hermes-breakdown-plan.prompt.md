---
agent: "agent"
description: "Hermes-equivalent: generate a GitHub project plan from PRD, technical breakdown, implementation plan, and test strategy artifacts."
---

## Goal

Generate a project plan that turns feature and epic inputs into an execution-ready planning package.

## Context

- Use when the user needs a Project Plan plus issue-creation support.
- Prefer concise, actionable language.
- Keep the plan aligned with the provided PRD, technical breakdown, implementation plan, and test strategy.
- Do not invent scope that is not supported by the source artifacts.

## Inputs

- Epic PRD path: `/docs/ways-of-work/plan/{epic-name}/epic.md`
- Feature PRD path: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md`
- Optional: `technical-breakdown.md`, `implementation-plan.md`, `test-strategy.md`

## Outputs

- Project Plan markdown at `/docs/ways-of-work/plan/{epic-name}/{feature-name}/project-plan.md`
- Issue Creation Checklist at `/docs/ways-of-work/plan/{epic-name}/{feature-name}/issues-checklist.md`
- GitHub issue templates for Epic, Feature, Story, Enabler, and Test work items
- A minimal GitHub Actions snippet for issue creation

## Rules

1. Use the provided artifacts as the only source of scope.
2. Keep outputs concise and directly usable.
3. Use Mermaid diagrams for hierarchy and dependency views.
4. Include practical issue templates, not generic prose.
5. Create backup copies before overwriting existing outputs.
6. Split large outputs into companion files if a single file would exceed the size limit.

## Phases

### Phase 1: Parse the source artifacts
**Goal:** identify the epic, feature, and supporting planning inputs.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Read the available planning inputs | Source summary |
| 1.2 | Identify the scope boundary and dependencies | Scope map |
| 1.3 | Capture the target output paths | Output plan |

#### Tasks
- Confirm which artifacts are available.
- Extract the main work items.
- Record any missing input that blocks planning.

### Phase 2: Build the project plan
**Goal:** produce the project-plan.md structure.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Draft the project overview | Overview section |
| 2.2 | Build the Work Item Hierarchy diagram | Mermaid hierarchy |
| 2.3 | Add issue breakdown, prioritization, and estimation guidance | Planning sections |

#### Tasks
- Keep the hierarchy traceable to the source inputs.
- Include a clear Epic → Feature → Story/Enabler → Test breakdown.
- Make the issue templates ready for automated creation.

### Phase 3: Create the checklist and automation snippet
**Goal:** produce the issue checklist and a minimal automation example.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Draft the pre-creation checklist | Checklist |
| 3.2 | Draft per-level checklists | Level checklists |
| 3.3 | Add the GitHub Actions snippet | Automation sample |

#### Tasks
- Keep the checklist practical and short.
- Make the automation snippet minimal and understandable.
- Ensure the snippet maps to the same issue taxonomy used in the plan.

### Phase 4: Verify the outputs
**Goal:** ensure the files contain the required sections and paths.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 4.1 | Verify file paths | Path check |
| 4.2 | Verify required sections exist | Content check |
| 4.3 | Confirm backups were created before overwrite | Safety check |

#### Tasks
- Confirm all required outputs were written.
- Re-read the generated files.
- Report any missing section or path clearly.

## Actions Summary

1. Read the source planning artifacts.
2. Derive the project scope and hierarchy.
3. Write the project plan and issue checklist.
4. Add the minimal automation snippet.
5. Verify the outputs and backup state.
