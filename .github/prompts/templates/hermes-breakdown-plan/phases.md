# Phases

> Extracted from `hermes-breakdown-plan.prompt.md`.

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
