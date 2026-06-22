---
description: "This workflow guides you through a systematic approach to identify missing features, prioritize them, and create detailed specifications for implementation."
agent: "agent"
---

## Goal

This workflow guides you through a systematic approach to identify missing features, prioritize them, and create detailed specifications for implementation.

## Context

Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake
- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute
- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify
- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off
- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Legacy Prompt Details
# Product Manager Assistant: Feature Identification and Specification

This workflow guides you through a systematic approach to identify missing features, prioritize them, and create detailed specifications for implementation.

## 1. Project Understanding Phase

- Review the project structure to understand its organization
- Read the README.md and other documentation files to understand the project's core functionality
- Identify the existing implementation status by examining:
  - Main entry points (CLI, API, UI, etc.)
  - Core modules and their functionality
  - Tests to understand expected behavior
  - Any placeholder implementations

**Guiding Questions:**

- What is the primary purpose of this project?
- What user problems does it solve?
- What patterns exist in the current implementation?
- Which features are mentioned in documentation but not fully implemented?

## 2. Gap Analysis Phase

- Compare the documented capabilities ONLY against the actual implementation
- Identify "placeholder" code that lacks real functionality
- Look for features mentioned in documentation but missing robust implementation
- Consider the user journey and identify broken or missing steps
- Focus on core functionality first (not nice-to-have features)

**Output Creation:**

- Create a list of potential missing features (5-7 items)
- For each feature, note:
  - Current implementation status
  - References in documentation
  - Impact on user experience if missing

## 3. Prioritization Phase

> - Apply a score to each identified gap:
> **Scoring Matrix (1-5 scale):**

> **Full content:** `templates/gen-specs-as-issues/3_prioritization_phase.md`

## 4. Specification Development Phase

> - For each prioritized feature, develop a detailed but practical specification:
> - Begin with the philosophical approach: simplicity over complexity

> **Full content:** `templates/gen-specs-as-issues/4_specification_developme.md`

## 5. GitHub Issue Creation Phase

- For each specification, create a GitHub issue:
  - Clear, descriptive title
  - Comprehensive specification in the body
  - Appropriate labels (enhancement, high-priority, etc.)
  - Explicitly mention MVP philosophy where relevant

**Issue Template Structure:**

# [Feature Name]

## Overview

[Brief description of the feature and its purpose]

## Scope

[What's included and what's explicitly excluded]

## Technical Requirements

[Specific technical needs and constraints]

## Implementation Plan

[Step-by-step approach with simple code examples]

## Acceptance Criteria

[Clear list of requirements to consider the feature complete]

## Priority

[Justification for prioritization]

## Dependencies

- **Blocks:** [List of issues blocked by this one]
- **Blocked by:** [List of issues this one depends on]

## Implementation Size

- **Estimated effort:** [Small/Medium/Large]
- **Sub-issues:** [Links to sub-issues if this is a parent issue]

## 5.5 Work Distribution Optimization

> - **Independence Analysis**
> - Review each specification to identify truly independent components

> **Full content:** `templates/gen-specs-as-issues/55_work_distribution_opti.md`

## 6. Final Review Phase

- Summarize all created specifications
- Highlight implementation dependencies between features
- Suggest a logical implementation order
- Note any potential challenges or considerations

Remember throughout this process:

- Favor simplicity over complexity
- Start with minimal viable implementations that work
- Focus on developer experience
- Build a foundation that can be extended later
- Consider the open-source community and contribution model

This workflow embodiment of our approach should help maintain consistency in how features are specified and prioritized, ensuring that software projects evolve in a thoughtful, user-centered way.


## Template References

Detailed templates in `templates/gen-specs-as-issues/`:


## Template References

Templates in `templates/gen-specs-as-issues/`:
- `1_project_understanding_p.md`
- `2_gap_analysis_phase.md`
- `3_prioritization_phase.md`
- `4_specification_developme.md`
- `55_work_distribution_opti.md`
- `5_github_issue_creation_p.md`
- `6_final_review_phase.md`
- `inputs.md`
- `phases.md`
- `rules.md`
