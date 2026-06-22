# Phases

> Extracted from `hermes-breakdown-test.prompt.md`.

## Phases

### Phase 1: Read the feature artifacts
**Goal:** understand the feature and the likely QA surface.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Read the feature PRD and supporting docs | QA brief |
| 1.2 | Identify the riskiest behaviors | Risk summary |
| 1.3 | Note missing inputs or assumptions | Gap list |

#### Tasks
- Identify the core user flows.
- Call out areas with high failure impact.
- Capture any missing context early.

### Phase 2: Draft the test strategy and checklist
**Goal:** produce the QA documents.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 2.1 | Write the test scope and quality model mapping | Strategy draft |
| 2.2 | Add the test issue checklist | Checklist draft |
| 2.3 | Add the QA plan and execution notes | QA plan draft |

#### Tasks
- Keep the strategy specific to the feature.
- Tie tests to risk and quality characteristics.
- Make the checklist actionable.

### Phase 3: Review and refine
**Goal:** tighten the QA package before finalizing it.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 3.1 | Check for missing test categories | Coverage gap list |
| 3.2 | Simplify wording and reduce overlap | Refined draft |
| 3.3 | Confirm file names and output paths | File-ready output |

#### Tasks
- Ensure the issue checklist is concrete.
- Ensure the QA plan can drive execution.
- Keep the wording concise.

### Phase 4: Verify
**Goal:** confirm the package is complete and usable.

#### Steps
| Step | Action | Output |
| --- | --- | --- |
| 4.1 | Re-read the final artifacts | Verification notes |
| 4.2 | Confirm the required sections are present | Section check |
| 4.3 | Confirm the target paths | Output confirmation |

#### Tasks
- Verify the strategy includes risk and technique mapping.
- Verify the checklist contains issue-ready items.
- Report missing source material if the QA package cannot be completed.
