---
agent: "agent"
description: "Hermes-equivalent: generate a test strategy, issue checklist, and QA plan from feature artifacts."
---

## Goal

Produce a QA package that turns feature artifacts into a clear test strategy and issue checklist.

## Context

- Use when feature planning needs QA structure and test coverage guidance.
- Prefer concrete, implementation-aware but not implementation-bound test planning.
- Keep the output useful for QA, engineering, and issue triage.
- Align the strategy with the available feature artifacts.

## Inputs

- Feature PRD path
- `technical-breakdown.md`
- `implementation-plan.md` (recommended)

## Outputs

- `/docs/ways-of-work/plan/{epic}/{feature}/test-strategy.md`
- `/docs/ways-of-work/plan/{epic}/{feature}/test-issues-checklist.md`
- `/docs/ways-of-work/plan/{epic}/{feature}/qa-plan.md`

## Rules

1. Include test scope and quality-risk mapping.
2. Use ISTQB-style technique selection where helpful.
3. Map the feature to ISO25010 quality characteristics.
4. Include environment, data, and CI/CD considerations.
5. Provide concrete issue templates for unit, integration, e2e, performance, and security coverage.
6. Include labeling and prioritization guidance.

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

## Actions Summary

1. Read the feature artifacts.
2. Draft the test strategy, checklist, and QA plan.
3. Add risk mapping and coverage guidance.
4. Verify completeness and path correctness.
