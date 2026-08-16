# Writing Plans — Body Reference

This reference preserves the detailed guidance from `writing-plans/SKILL.md` and is the canonical source for expanded content.

## Core Principle

A good plan makes implementation obvious. If someone has to guess, the plan is incomplete.

## Bite-Sized Task Granularity

Each task = 2-5 minutes of focused work. Every step is one action:
- "Write the failing test"
- "Run it to make sure it fails"
- "Implement the minimal code to make the test pass"
- "Run the tests and make sure they pass"
- "Commit"

If a task needs 50 lines across 5 files, break it into smaller tasks.

## Plan Document Structure

### Required Header

```
# [Feature Name] Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** [One sentence]

**Architecture:** [2-3 sentences]

**Tech Stack:** [Key technologies/libraries]

---
```

### Required Task Block

````markdown
### Task N: [Descriptive Name]

**Objective:** What this task accomplishes (one sentence)

**Files:**
- Create: `exact/path/to/new_file.py`
- Modify: `exact/path/to/existing.py:45-67`
- Test: `tests/path/to/test_file.py`

**Step 1:** [Action]
**Step 2:** [Action]
**Step 3:** [Action]
**Step 4:** [Action]
**Step 5:** [Action]
````

## Writing Process

1. Read requirements, design docs, acceptance criteria, constraints, prerequisite artifacts, and the plan-format contract in `implementation-plan-contract.md`.
2. Check prerequisites and create any missing discovery artifacts before finalizing the plan.
3. Explore the codebase with `search_files` and `read_file`.
4. Choose architecture, file organization, dependencies, and testing strategy.
5. Write tasks in implementation order: setup, core functionality, edge cases, integration, cleanup/documentation.
6. Add exact file paths, copy-pasteable code, exact commands, expected output, and verification steps.
7. Review against completeness, size, exactness, and TDD/DRY/YAGNI.
8. Save plan under `docs/plans/YYYY-MM-DD-feature-name.md`, then commit with `docs: add implementation plan for [feature]`.

## Execution Handoff

After saving the plan, offer execution via `subagent-driven-development` with fresh `delegate_task` per task, two-stage review, and approval gates.

## Principles

- DRY: avoid duplication; prefer extract/reuse.
- YAGNI: avoid speculative flexibility.
- TDD: include failing test, run, implement, run pass.
- Frequent commits: after each task.

## Common Mistakes

- Vague tasks: "Add authentication" → "Create User model with email and password_hash fields"
- Incomplete code: provide whole function context, not just "add validation"
- Missing verification: "Run `pytest tests/test_auth.py -v`, expected: 3 passed"
- Missing file paths: prefer exact paths

## Cross-Platform Considerations

Use `$HOME` and `%USERPROFILE%` environment variables. Respect per-project conventions in AGENTS.md, CLAUDE.md, and README.md.
