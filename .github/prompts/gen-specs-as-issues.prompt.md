---
name: gen-specs-as-issues
title: 'Product Manager Assistant: Feature Identification and Specification'
description: This workflow guides you through a systematic approach to identify missing
  features, prioritize them, and create detailed specifications for implementation.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
- file
- terminal
scripts: []
skills: []
formatter: default
plan: null
tags:
- frontend
- ml
- prompts
- specification
- typescript
- workflow
- frontend
- ml
- prompts
- specification
- typescript
- workflow
trigger: /gen-specs-as-issues
dependencies: []
metadata:
  hermes: {}
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

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

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

## 1. Project Understanding Phase

- Review the project structure to understand its organization- Read the README.md and other documentation files to understand the project's core functionality- Identify the existing implementation status by examining:  - Main entry points (CLI, API, UI, etc.)  - Core modules and their functionality  - Tests to understand expected behavior  - Any placeholder implementations**Guiding Questions:**- What is the primary purpose of this project?- What user problems does it solve?- What patterns exist in the current implementation?- Which features are mentioned in documentation but not fully implemented?

## 2. Gap Analysis Phase

- Compare the documented capabilities ONLY against the actual implementation- Identify "placeholder" code that lacks real functionality- Look for features mentioned in documentation but missing robust implementation- Consider the user journey and identify broken or missing steps- Focus on core functionality first (not nice-to-have features)**Output Creation:**- Create a list of potential missing features (5-7 items)- For each feature, note:  - Current implementation status  - References in documentation  - Impact on user experience if missing

## 3. Prioritization Phase

> - Apply a score to each identified gap:
> **Scoring Matrix (1-5 scale):**
> **Full content:**

## 4. Specification Development Phase

> - For each prioritized feature, develop a detailed but practical specification:
> - Begin with the philosophical approach: simplicity over complexity
> **Full content:**

## 5. GitHub Issue Creation Phase

- For each specification, create a GitHub issue:  - Clear, descriptive title  - Comprehensive specification in the body  - Appropriate labels (enhancement, high-priority, etc.)  - Explicitly mention MVP philosophy where relevant**Issue Template Structure:**# [Feature Name]

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

- **Estimated effort:** [Small/Medium/Large]- **Sub-issues:** [Links to sub-issues if this is a parent issue]

## 5.5 Work Distribution Optimization

> - **Independence Analysis**
> - Review each specification to identify truly independent components
> **Full content:**

## 6. Final Review Phase

- Summarize all created specifications- Highlight implementation dependencies between features- Suggest a logical implementation order- Note any potential challenges or considerationsRemember throughout this process:- Favor simplicity over complexity- Start with minimal viable implementations that work- Focus on developer experience- Build a foundation that can be extended later- Consider the open-source community and contribution modelThis workflow embodiment of our approach should help maintain consistency in how features are specified and prioritized, ensuring that software projects evolve in a thoughtful, user-centered way.

## Template References

Detailed templates in `templates/gen-specs-as-issues/`:

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
