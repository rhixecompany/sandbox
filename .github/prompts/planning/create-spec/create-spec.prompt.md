---
name: planning/create-spec/create-spec
title: "Create Feature"
description: "Create a new feature with full implementation including tests, docs, and verification"
version: 1.0.0
author: Hermes Agent
license: MIT
category: planning
trigger: create-spec
tags: [feature, implementation, tdd]
skills_required: [test-driven-development, executing-plans, subagent-driven-development]
tools_required: [terminal, write_file, patch, search_files]
companion_files:
  - specs.md
  - plans.md
  - goals.md
  - subgoals.md
  - rules.md
  - phases.md
  - steps.md
  - tasks.md
  - actions.md
  - gates.md
---

# Create Feature

## Overview

Systematic feature creation workflow using TDD with subagent-driven development for parallel execution.

## When to Use

Building new features from requirements; creating components, services, or modules

## When NOT to Use

Bug fixes (use fix-bug); refactoring (use refactor-code); simple config changes

## Workflow

### Phase 1: Preparation
1. Read requirements from spec
2. Create implementation plan
3. Set up test structure
4. Define acceptance criteria

### Phase 2: Execution
1. Write failing tests (TDD)
2. Implement minimal code
3. Run tests to pass
4. Refactor with tests green

### Phase 3: Verification
1. Run full test suite
2. Verify against spec
3. Code quality review
4. Integration testing

### Phase 4: Completion
1. Update documentation
2. Commit changes
3. Create PR
4. Verify CI passes

## Verification Checklist

- [ ] All tests passing
- [ ] Spec requirements met
- [ ] Code quality approved
- [ ] Documentation updated
- [ ] CI/CD green

## Best Practices

Follow TDD strictly; use subagents for parallel tasks; keep commits atomic

## Pitfalls

Skipping tests; scope creep; not verifying integration; large unreviewed commits
