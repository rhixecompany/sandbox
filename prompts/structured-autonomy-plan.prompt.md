---
license: MIT
author: Hermes Agent
version: 1.0.0
name: "sa-plan"
title: "Sa Plan"
description: "Structured Autonomy Planning Prompt"
trigger: /sa-plan
tags: []
  - hermes
---

## Goal

Structured Autonomy Planning Prompt.

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

## Step 1: Research and Gather Context

MANDATORY: Run #tool:runSubagent tool instructing the agent to work autonomously following <research_guide> to gather context. Return all findings.

DO NOT do any other tool calls after #tool:runSubagent returns!

If #tool:runSubagent is unavailable, execute <research_guide> via tools yourself.

## Step 2: Determine Commits

Analyze the user's request and break it down into commits:

- For **SIMPLE** features, consolidate into 1 commit with all changes.
- For **COMPLEX** features, break into multiple commits, each representing a testable step toward the final goal.

## Step 3: Plan Generation

1. Generate draft plan using <output_template> with `[NEEDS CLARIFICATION]` markers where the user's input is needed.
2. Save the plan to "plans/{feature-name}/plan.md"
3. Ask clarifying questions for any `[NEEDS CLARIFICATION]` sections
4. MANDATORY: Pause for feedback
5. If feedback received, revise plan and go back to Step 1 for any research needed

</workflow>

<output_template> **File:** `plans/{feature-name}/plan.md`

```markdown
# {Feature Name}

**Branch:** `{kebab-case-branch-name}` **Description:** {One sentence describing what gets accomplished}

## Goal

{1-2 sentences describing the feature and why it matters}

## Implementation Steps

> ### Step 1: {Step Name} [SIMPLE features have only this step]
> **Files:** {List affected files: Service/HotKeyManager.cs, Models/PresetSize.cs,

> **Full content:** `templates/structured-autonomy-plan/implementation_steps.md`

## Template References

Templates in `templates/structured-autonomy-plan/`:
- `implementation_steps.md`
- `phases.md`
- `step_3_plan_generation.md`
