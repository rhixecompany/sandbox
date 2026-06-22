# Phases

> Extracted from `hermes-breakdown-feature-implementation.prompt.md`.

## Phases

### Phase 1: Analyze the PRD
**Goal:** extract the technical work implied by the feature.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Read the PRD and supporting notes | Requirements summary |
| 1.2 | Identify technical constraints | Constraint list |
| 1.3 | Capture dependencies and unknowns | Risk notes |

#### Tasks
- Map user requirements to engineering work.
- Identify missing technical details.
- Keep the analysis concise.

### Phase 2: Draft the implementation plan
**Goal:** produce the implementation-plan.md structure.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Write the goal and technical considerations | Opening sections |
| 2.2 | Add architecture, schema, and API sections | Core design sections |
| 2.3 | Add frontend, deployment, security, and performance notes | Delivery sections |

#### Tasks
- Make the architecture feature-specific.
- Include data model and migration strategy where needed.
- Keep the API section explicit and testable.

### Phase 3: Review and tighten
**Goal:** remove ambiguity and confirm completeness.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Check for missing required sections | Gap list |
| 3.2 | Tighten language and remove fluff | Refined draft |
| 3.3 | Verify the file path and naming | File-ready output |

#### Tasks
- Ensure deployment notes are present.
- Ensure security and performance notes are not skipped.
- Keep the plan readable and actionable.

### Phase 4: Verify
**Goal:** confirm the implementation plan is usable for execution.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 4.1 | Re-read the final plan | Verification notes |
| 4.2 | Confirm the required sections exist | Section check |
| 4.3 | Confirm the target path | Output confirmation |

#### Tasks
- Verify the plan content matches the PRD.
- Verify the file path is correct.
- Report missing inputs if the draft cannot be completed cleanly.
