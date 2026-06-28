---
toolsets: []
license: MIT
author: Hermes Agent
version: 1.0.0
name: "refactor-method-complexity-reduce"
title: "Refactor Method Complexity Reduce"
description: "Refactor given method `${input:methodName}` to reduce its cognitive complexity to `${input:complexityThreshold}` or below, by extracting helper methods."
trigger: /refactor-method-complexity-reduce
argument-hint: "methodName=..., complexityThreshold=15"
tags:
  - hermes
  - refactoring
toolsets:
  - search/changes
  - search/codebase
  - edit/editFiles
  - read/problems
  - execute/runTests
---

## Goal

Refactor given method `${input:methodName}` to reduce its cognitive complexity to `${input:complexityThreshold}` or below, by extracting helper methods.

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

## Objective

Refactor the method `${input:methodName}`, to reduce its cognitive complexity to `${input:complexityThreshold}` or below, by extracting logic into focused helper methods.

## Instructions

> 1. **Analyze the current method** to identify sources of cognitive complexity:
> - Nested conditional statements

> **Full content:** `templates/refactor-method-complexity-reduce/instructions.md`

## Implementation Approach

- Extract helper methods before refactoring the main flow
- Test incrementally to ensure no regressions
- Use meaningful names that describe the extracted responsibility
- Keep extracted methods close to where they're used
- Consider making repeated code patterns into generic methods

## Result

The refactored method should:

- Have cognitive complexity reduced to the target threshold of `${input:complexityThreshold}` or below
- Be more readable and maintainable
- Have clear separation of concerns
- Be easier to test and debug
- Retain all original functionality

## Testing and Validation

**CRITICAL: After completing the refactoring, you MUST:**

1. **Run all existing tests** related to the refactored method and its surrounding functionality
2. **MANDATORY: Explicitly verify test results show "failed=0"**
   - **NEVER assume tests passed** - always examine the actual test output
   - Search for the summary line containing pass/fail counts (e.g., "passed=X failed=Y")
   - **If the summary shows any number other than "failed=0", tests have FAILED**
   - If test output is in a file, read the entire file to locate and verify the failure count
   - Running tests is NOT the same as verifying tests passed
   - **Do not proceed** until you have explicitly confirmed zero failures
3. **If any tests fail (failed > 0):**
   - State clearly how many tests failed
   - Analyze each failure to understand what functionality was broken
   - Common causes: null handling, empty collection checks, condition logic errors
   - Identify the root cause in the refactored code
   - Correct the refactored code to restore the original behavior
   - Re-run tests and verify "failed=0" in the output
   - Repeat until all tests pass (failed=0)
4. **Verify compilation** - Ensure there are no compilation errors
5. **Check cognitive complexity** - Confirm the metric is at or below the target threshold of `${input:complexityThreshold}`

## Confirmation Checklist

- [ ] Code compiles without errors
- [ ] **Test results explicitly state "failed=0"** (verified by reading the output)
- [ ] All test failures analyzed and corrected (if any occurred)
- [ ] Cognitive complexity is at or below the target threshold of `${input:complexityThreshold}`
- [ ] All original functionality is preserved
- [ ] Code follows project conventions and standards


## Template References

Detailed templates in `templates/refactor-method-complexity-reduce/`:
- `instructions.md`
