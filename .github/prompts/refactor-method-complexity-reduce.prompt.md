---
name: refactor-method-complexity-reduce
title: Refactor Method Complexity Reduce
description: Refactor a given method to reduce its cognitive complexity to a target threshold or below by extracting focused helper methods, with mandatory test verification.
trigger: /refactor-method-complexity-reduce
version: 1.0.0
author: Hermes Agent
tags: [refactor, code-quality, complexity, testing, javascript, typescript]
metadata: 
hermes: 
profile: code-architect
priority: medium
copilot: 
model_required: sonnet
opencode: 
enabled: true
codex: 
date: 2026-08-25
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
license: MIT
---

## Table of Contents

## Goal
Refactor a given method to reduce its cognitive complexity to a target threshold or below by extracting focused helper methods, with mandatory test verification.

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand off](#phase-4:-hand-off)
- [Objective](#objective)
- [Instructions](#instructions)
- [Implementation Approach](#implementation-approach)
- [Result](#result)
- [Test](#test)
- [Confirmation Checklist](#confirmation-checklist)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand off](#phase-4:-hand-off)
- [Objective](#objective)
- [Instructions](#instructions)
- [Implementation Approach](#implementation-approach)
- [Result](#result)
- [Test](#test)
- [Confirmation Checklist](#confirmation-checklist)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





Refactor given method `${input:methodName}` to reduce its cognitive complexity to `${input:complexityThreshold}` or below, by extracting helper methods.


Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.


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

- Return the final artifact or findings .
- Stop once the requested result is delivered.

## Objective

Refactor the method to reduce its cyclomatic complexity while preserving behavior.

input:methodName}`, to reduce its cognitive complexity to`${input:complexityThreshold}` or below, by extracting logic into focused helper methods.

## Instructions

> 1. **Analyze the current method** to identify sources of cognitive complexity:>
>
> - Nested conditional statements

## Implementation Approach

- Extract helper methods before refactoring the main flow- Test incrementally to ensure no regressions- Use meaningful names that describe the extracted responsibility- Keep extracted methods close to where they're used- Consider making repeated code patterns into generic methods

## Result

The refactored method should:

- Have cognitive complexity reduced to the target threshold of `${input:complexityThreshold}` or below- Be more readable and maintainable- Have clear separation of concerns- Be easier to test and debug- Retain all original functionality

## Test

ing and Validation**CRITICAL: After completing the refactoring, you MUST:**1. **Run all existing tests** related to the refactored method and its surrounding functionality2. **MANDATORY: Explicitly verify test results show "failed=0"** - **NEVER assume tests passed** - always examine the actual test output - Search for the summary line containing pass/fail counts (e.g., "passed=X failed=Y") - **If the summary shows any number other than "failed=0", tests have FAILED** - If test output is in a file, read the entire file to locate and verify the failure count - Running tests is NOT the same as verifying tests passed - **Do not proceed** until you have explicitly confirmed zero failures3. **If any tests fail (failed > 0):** - State how many tests failed - Analyze each failure to understand what functionality was broken - Common causes: null handling, empty collection checks, condition logic errors - Identify the root cause in the refactored code - Correct the refactored code to restore the original behavior - Re-run tests and verify "failed=0" in the output - Repeat until all tests pass (failed=0)4. **Verify compilation** - Ensure there are no compilation errors5. **Check cognitive complexity** - Confirm the metric is at or below the target threshold of `${input:complexityThreshold}`

## Confirmation Checklist

- [ ] Code compiles without errors- [ ] **Test results explicitly state "failed=0"** (verified by reading the output)- [ ] All test failures analyzed and corrected (if any occurred)- [ ] Cognitive complexity is at or below the target threshold of `${input:complexityThreshold}`- [ ] All original functionality is preserved- [ ] Code follows project conventions and standards

## Template References

Detailed templates in `templates/refactor-method-complexity-reduce/`:- `instructions.md`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section

## Related Prompts

## Workflow

<content>

Same-family prompts:

- [`refactor-code.prompt.md`](refactor-code.prompt.md)
- [`refactor-mardown-files.prompt.md`](refactor-mardown-files.prompt.md)
- [`refactor-plan.prompt.md`](refactor-plan.prompt.md)
```
# Prompt template
Execute the workflow defined in this file.
```
