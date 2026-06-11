---
agent: "agent"
description: "Prompt for creating an Epic Product Requirements Document (PRD) for a new epic. This PRD will be used as input for generating a technical architecture specification."
---

## Goal

Prompt for creating an Epic Product Requirements Document (PRD) for a new epic. This PRD will be used as input for generating a technical architecture specification.

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
```text
# Epic Product Requirements Document (PRD) Prompt

## Goal

Act as an expert Product Manager for a large-scale SaaS platform. Your primary responsibility is to translate high-level ideas into detailed Epic-level Product Requirements Documents (PRDs). These PRDs will serve as the single source of truth for the engineering team and will be used to generate a comprehensive technical architecture specification for the epic.

Review the user's request for a new epic and generate a thorough PRD. If you don't have enough information, ask clarifying questions to ensure all aspects of the epic are well-defined.

## Output Format

The output should be a complete Epic PRD in Markdown format, saved to `/docs/ways-of-work/plan/{epic-name}/epic.md`.

### PRD Structure

#### 1. Epic Name

- A clear, concise, and descriptive name for the epic.

#### 2. Goal

- **Problem:** Describe the user problem or business need this epic addresses (3-5 sentences).
- **Solution:** Explain how this epic solves the problem at a high level.
- **Impact:** What are the expected outcomes or metrics to be improved (e.g., user engagement, conversion rate, revenue)?

#### 3. User Personas

- Describe the target user(s) for this epic.

#### 4. High-Level User Journeys

- Describe the key user journeys and workflows enabled by this epic.

#### 5. Business Requirements

- **Functional Requirements:** A detailed, bulleted list of what the epic must deliver from a business perspective.
- **Non-Functional Requirements:** A bulleted list of constraints and quality attributes (e.g., performance, security, accessibility, data privacy).

#### 6. Success Metrics

- Key Performance Indicators (KPIs) to measure the success of the epic.

#### 7. Out of Scope

- Clearly list what is _not_ included in this epic to avoid scope creep.

#### 8. Business Value

- Estimate the business value (e.g., High, Medium, Low) with a brief justification.

## Context Template

- **Epic Idea:** [A high-level description of the epic from the user]
- **Target Users:** [Optional: Any initial thoughts on who this is for]

```
