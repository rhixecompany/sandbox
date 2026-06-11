---
agent: "agent"
description: "Hermes-equivalent: create a high-level Epic Architecture Specification from an Epic PRD."
---

## Goal

Turn an Epic PRD into a high-level architecture specification with layers, enablers, and technology guidance.

## Context

- Use when an epic already exists and needs architecture direction.
- Keep the plan high-level and architecture-focused.
- Use Mermaid diagrams for system layering and data flow.
- Do not write implementation code.

## Inputs

- Epic PRD path: `/docs/ways-of-work/plan/{epic-name}/epic.md`
- Optional architecture notes or constraints

## Outputs

- `/docs/ways-of-work/plan/{epic-name}/arch.md`

## Rules

1. Include an architecture overview.
2. Show User, Application, Service, Data, and Infrastructure layers.
3. List features and technical enablers.
4. Recommend a technology stack with short justification.
5. Include a value assessment and t-shirt estimate.
6. Prefer labeled Mermaid subgraphs for clarity.

## Phases

### Phase 1: Analyze the epic
**Goal:** extract the architectural implications of the epic.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Read the Epic PRD | Requirements summary |
| 1.2 | Identify architecture constraints | Constraint list |
| 1.3 | Record unknowns and trade-offs | Risk notes |

#### Tasks
- Map epic goals to system shape.
- Identify major integration points.
- Keep the analysis concise.

### Phase 2: Draft the architecture spec
**Goal:** write the `arch.md` structure.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Write the architecture overview | Overview section |
| 2.2 | Add the Mermaid diagram | Diagram section |
| 2.3 | Add enablers, stack, and estimation notes | Core sections |

#### Tasks
- Keep the diagram readable.
- Explain technology choices clearly.
- Include alternates when trade-offs matter.

### Phase 3: Review and refine
**Goal:** ensure the specification is complete and readable.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Check for missing sections | Gap list |
| 3.2 | Tighten wording | Refined draft |
| 3.3 | Confirm the output path | File-ready draft |

#### Tasks
- Avoid implementation detail.
- Keep the justification short and direct.
- Make the enabler list actionable.

### Phase 4: Verify
**Goal:** confirm the final architecture document is usable.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 4.1 | Re-read the final spec | Verification notes |
| 4.2 | Confirm required sections exist | Section check |
| 4.3 | Confirm the target path | Output confirmation |

#### Tasks
- Verify the diagram and stack guidance.
- Verify the file path is correct.
- Report missing inputs if needed.

## Actions Summary

1. Read the Epic PRD.
2. Draft the architecture overview and diagram.
3. Add enablers, stack guidance, and estimates.
4. Verify completeness and path correctness.
