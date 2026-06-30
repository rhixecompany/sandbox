---
license: MIT
author: Hermes Agent
version: 1.0.0
name: refactor-method-complexity-reduce
title: Refactor Method Complexity Reduce
description: Refactor the method `${input:methodName}` to reduce cognitive complexity to `${input:complexityThreshold}` or below by extracting helper methods.
trigger: refactor-method-complexity-reduce
argument-hint: "methodName=..., complexityThreshold=15"
metadata:
  hermes:
    related_skills: []
    tags:
    - refactor-method-complexity-reduce.prompt

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
tags:
  - refactoring
  - complexity
  - cleanup
  - maintenance
  - code-review
dependencies: []
skills: []
toolsets:
  - search/changes
  - search/codebase
  - edit/editFiles
  - read/problems
  - execute/runTests

## Goal

Refactor the method `${input:methodName}` to reduce cognitive complexity to `${input:complexityThreshold}` or below by extracting helper methods.

## Context

Use when a method has grown too complex to read or maintain safely.

## Inputs

- The current workspace, repo, or document state
- The method path and refactoring constraints
- Any test or lint instructions needed to validate the change

## Outputs

- Refactored method with readable structure
- Updated helper methods and imports
- Tests or validation showing zero regressions
- Summary of complexity reduction

## Rules

- Follow the prompt literally and prefer evidence from the current workspace
- Keep the response structured, deterministic, and easy to act on
- Avoid changing unrelated files or adding unnecessary scope
- If something is unclear, state the assumption instead of guessing

## Workflow

1. Inspect the method and identify high-complexity branches
2. Extract helper methods to reduce nesting and branching
3. Re-run tests and confirm `failed=0`
4. Record the complexity delta and remaining hotspots

## Verification

- Complexity meets the target threshold
- All existing tests pass
- No unrelated behavior changed
- Output includes the test summary confirming zero failures
