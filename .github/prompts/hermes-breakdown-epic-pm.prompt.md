---
agent: "agent"
description: "Hermes-equivalent: author a complete Epic PRD from a high-level epic idea or request."
---

## Goal

Produce a complete Epic PRD that is ready for downstream feature planning.

## Context

- Use when the user provides an epic idea, short brief, or high-level request.
- Keep the output measurable, concise, and aligned to business value.
- Ask a short clarifying list if the input is missing key details.
- Do not drift into implementation detail.

## Inputs

- Epic idea text or short brief
- Optional target metrics or constraints

## Outputs

- `/docs/ways-of-work/plan/{epic-name}/epic.md`

## Rules

1. Include problem, solution, and impact.
2. Define user personas and high-level journeys.
3. Include functional and non-functional business requirements.
4. Include success metrics and out-of-scope items.
5. Estimate business value in a clear, comparable way.
6. Ask for clarification when the epic is underspecified.

## Phases

### Phase 1: Understand the epic
**Goal:** capture the idea, audience, and business objective.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Read the epic idea or brief | Input summary |
| 1.2 | Identify users and goals | Persona summary |
| 1.3 | Note missing information | Clarification list |

#### Tasks
- Identify the epic boundary.
- Capture the intended business outcome.
- Record unresolved questions.

### Phase 2: Draft the Epic PRD
**Goal:** write a structured `epic.md`.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Write the goal and impact | Goal section |
| 2.2 | Add personas, journeys, and requirements | PRD body |
| 2.3 | Add metrics and out-of-scope sections | Validation sections |

#### Tasks
- Keep the language concrete.
- Make success criteria observable.
- Avoid implementation speculation.

### Phase 3: Review and refine
**Goal:** tighten wording and confirm completeness.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Check for missing sections | Gap list |
| 3.2 | Remove vague language | Refined draft |
| 3.3 | Confirm the output path | File-ready draft |

#### Tasks
- Keep the PRD readable and concise.
- Ensure all required sections exist.
- Ensure the epic is useful for feature planning.

### Phase 4: Verify
**Goal:** confirm the final epic PRD is usable.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 4.1 | Re-read the final PRD | Verification notes |
| 4.2 | Confirm the required sections exist | Section check |
| 4.3 | Confirm the target path | Output confirmation |

#### Tasks
- Verify the output path.
- Verify the business framing.
- Report missing inputs if the draft cannot be completed cleanly.

## Actions Summary

1. Read the epic brief.
2. Draft the Epic PRD structure and content.
3. Add journeys, requirements, metrics, and scope limits.
4. Verify completeness and file path.
