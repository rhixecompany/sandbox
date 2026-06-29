# Phases

> Extracted from `hermes-breakdown-epic-arch.prompt.md`.

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
