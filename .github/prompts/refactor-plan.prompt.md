---
agent: "agent"
tools: ["codebase", "terminalCommand"]
description: "Plan a multi-file refactor with proper sequencing and rollback steps"
---

## Goal

Plan a multi-file refactor with proper sequencing and rollback steps.

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
# Refactor Plan

Create a detailed plan for this refactoring task.

## Refactor Goal

{{refactor_description}}

## Instructions

1. Search the codebase to understand current state
2. Identify all affected files and their dependencies
3. Plan changes in a safe sequence (types first, then implementations, then tests)
4. Include verification steps between changes
5. Consider rollback if something fails

## Output Format

```markdown
## Refactor Plan: [title]

### Current State

[Brief description of how things work now]

### Target State

[Brief description of how things will work after]

### Affected Files

| File | Change Type          | Dependencies           |
| ---- | -------------------- | ---------------------- |
| path | modify/create/delete | blocks X, blocked by Y |

### Execution Plan

#### Phase 1: Types and Interfaces

- [ ] Step 1.1: [action] in `file.ts`
- [ ] Verify: [how to check it worked]

#### Phase 2: Implementation

- [ ] Step 2.1: [action] in `file.ts`
- [ ] Verify: [how to check]

#### Phase 3: Tests

- [ ] Step 3.1: Update tests in `file.test.ts`
- [ ] Verify: Run `npm test`

#### Phase 4: Cleanup

- [ ] Remove deprecated code
- [ ] Update documentation

### Rollback Plan

If something fails:

1. [Step to undo]
2. [Step to undo]

### Risks

- [Potential issue and mitigation]
```

Shall I proceed with Phase 1?
