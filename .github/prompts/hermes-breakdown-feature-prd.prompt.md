---
agent: "agent"
description: "Hermes-equivalent: create a Feature PRD from a feature idea or parent epic."
---

## Goal

Produce a feature PRD that is ready to hand off for implementation planning.

## Context

- Use when the user needs a structured `prd.md` for a single feature.
- Base the PRD on a parent epic or a clearly stated feature idea.
- Keep the content concrete and user-facing.
- Do not add implementation detail beyond what is needed for the PRD.

## Inputs

- Parent epic path or feature idea text

## Outputs

- `/docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md`

## Rules

1. Include the feature name and the epic reference.
2. Describe the problem, solution, and intended impact.
3. Write user stories in a clear, testable form.
4. Include functional and non-functional requirements.
5. Include acceptance criteria using checklist items or Given/When/Then.
6. List out-of-scope items and dependencies.

## Phases

### Phase 1: Understand the feature
**Goal:** capture the feature idea and the parent epic context.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Read the feature idea or parent epic | Input summary |
| 1.2 | Identify the intended user outcome | Goal statement |
| 1.3 | Record any missing context | Clarification notes |

#### Tasks
- Confirm what the feature should solve.
- Identify the intended users.
- Capture any constraints that affect scope.

### Phase 2: Draft the PRD
**Goal:** write a complete and structured `prd.md`.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Define the feature and epic linkage | Header section |
| 2.2 | Write the goal, stories, and requirements | PRD body |
| 2.3 | Add acceptance criteria and dependencies | Validation sections |

#### Tasks
- Keep user stories aligned with the feature intent.
- Make the acceptance criteria observable.
- Keep the writing concise and specific.

### Phase 3: Review and refine
**Goal:** ensure the PRD is complete and easy to use downstream.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Check for missing sections | Gap list |
| 3.2 | Tighten ambiguous language | Refined draft |
| 3.3 | Confirm the output path | File-ready draft |

#### Tasks
- Remove vague statements.
- Keep the PRD free of implementation details.
- Make sure dependencies are explicit.

### Phase 4: Verify
**Goal:** confirm the final PRD is usable for planning.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 4.1 | Re-read the final PRD | Verification notes |
| 4.2 | Check required sections | Section check |
| 4.3 | Confirm the target path | Output confirmation |

#### Tasks
- Verify the file path is correct.
- Verify the user stories and criteria are present.
- Report any missing data needed for a final rewrite.

## Actions Summary

1. Read the feature idea and epic context.
2. Draft the PRD structure and content.
3. Add stories, requirements, and acceptance criteria.
4. Verify completeness and file path.
