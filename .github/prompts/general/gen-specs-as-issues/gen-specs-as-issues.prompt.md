---
name: gen-specs-as-issues
title: Generate Specs as Issues
description: Identifies missing features, prioritizes them, and creates detailed implementation specifications as GitHub issues.
trigger: /gen-specs-as-issues
category: general
version: 1.0.0
author: Hermes Agent
date: 2026-08-25
tags: 
metadata: 
hermes: 
profile: code-architect
priority: medium
copilot: 
model_required: sonnet
opencode: 
enabled: true
codex: 
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
license: MIT
---

## Table of Contents

## Goal
Identifies missing features, prioritizes them, and creates detailed implementation specifications as GitHub issues.

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
- [1. Project Understanding Phase](#1-project-understanding-phase)
- [2. Gap Analysis Phase](#2-gap-analysis-phase)
- [3. Prioritization Phase](#3-prioritization-phase)
- [4. Specification Development Phase](#4-specification-development-phase)
- [5. GitHub Issue Creation Phase](#5-github-issue-creation-phase)
- [Overview](#overview)
- [Scope](#scope)
- [Technical Requirements](#technical-requirements)
- [Implementation Plan](#implementation-plan)
- [Acceptance Criteria](#acceptance-criteria)
- [Priority](#priority)
- [Dependencies](#dependencies)
- [Implementation Size](#implementation-size)
- [5.5 Work Distribution Optimization](#55-work-distribution-optimization)
- [6. Final Review Phase](#6-final-review-phase)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)



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
- [1. Project Understanding Phase](#1-project-understanding-phase)
- [2. Gap Analysis Phase](#2-gap-analysis-phase)
- [3. Prioritization Phase](#3-prioritization-phase)
- [4. Specification Development Phase](#4-specification-development-phase)
- [5. GitHub Issue Creation Phase](#5-github-issue-creation-phase)
- [Overview](#overview)
- [Scope](#scope)
- [Technical Requirements](#technical-requirements)
- [Implementation Plan](#implementation-plan)
- [Acceptance Criteria](#acceptance-criteria)
- [Priority](#priority)
- [Dependencies](#dependencies)
- [Implementation Size](#implementation-size)
- [5.5 Work Distribution Optimization](#55-work-distribution-optimization)
- [6. Final Review Phase](#6-final-review-phase)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)





This workflow guides you through a systematic approach to identify missing features, prioritize them, and create detailed specifications for implementation.


Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

> Core rules: [`templates/rules-core.md`](templates/rules-core.md)

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

## 1. Project Understanding Phase

- Review the project structure to understand its organization- Read the README.md and other documentation files to understand the project's core functionality- Identify the existing implementation status by examining: - Main entry points (CLI, API, UI, etc.) - Core modules and their functionality - Tests to understand expected behavior - Any placeholder implementations**Guiding Questions:**- What is the primary purpose of this project?- What user problems does it solve?- What patterns exist in the current implementation?- Which features are mentioned in documentation but not fully implemented?

## 2. Gap Analysis Phase

- Compare the documented capabilities ONLY against the actual implementation- Identify "placeholder" code that lacks real functionality- Look for features mentioned in documentation but missing strong implementation- Consider the user journey and identify broken or missing steps- Focus on core functionality first (not nice-to-have features)**Output Creation:**- Create a list of potential missing features (5-7 items)- For each feature, note: - Current implementation status - References in documentation - Impact on user experience if missing

## 3. Prioritization Phase

> - Apply a score to each identified gap:
> **Scoring Matrix (1-5 scale):**
> **Full content:**

## 4. Specification Development Phase

> - For each prioritized feature, develop a detailed but practical specification:
> - Begin with the philosophical approach: simplicity over complexity
> **Full content:**

## 5. GitHub Issue Creation Phase

- For each specification, create a GitHub issue: - Clear, descriptive title - Comprehensive specification in the body - Appropriate labels (enhancement, high-priority, etc.) - Explicitly mention MVP philosophy where relevant**Issue Template Structure:**# [Feature Name]

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

Detailed templates in `templates/`:

## Personas

See [`templates/personas.md`](templates/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/personality.md`](templates/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Best Practices

See [`templates/best-practices.md`](templates/best-practices.md) for cross-cutting best practices.

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

See [`templates/skills-table-core.md`](templates/skills-table-core.md) for shared skills table.

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

## Workflow

<content>

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section
```
# Prompt template
Execute the workflow defined in this file.
```
