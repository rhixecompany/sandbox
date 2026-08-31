---
name: create-technical-spike
title: Create Technical Spike
description: Define a time-boxed technical spike with research questions, investigation plan, and deliverables.
trigger: /create-technical-spike
version: 1.0.0
author: Hermes Agent
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
Define a time-boxed technical spike with research questions, investigation plan, and deliverables.

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Prerequisites](#prerequisites)
- [Pitfalls](#pitfalls)
- [Summary](#summary)
- [Research Question(s)](#research-questions)
- [Investigation Plan](#investigation-plan)
  - [Research Tasks](#research-tasks)
  - [Success Criteria](#success-criteria)
- [Technical Context](#technical-context)
- [Research Findings](#research-findings)
  - [Investigation Results](#investigation-results)
  - [Prototype/Testing Notes](#prototype/testing-notes)
  - [External Resources](#external-resources)
- [Decision](#decision)
  - [Recommendation](#recommendation)
  - [Rationale](#rationale)
  - [Implementation Notes](#implementation-notes)
  - [Follow-up Actions](#follow-up-actions)
- [Status History](#status-history)
- [Categories for Technical Spikes](#categories-for-technical-spikes)
- [File Naming Conventions](#file-naming-conventions)
- [Best Practices for AI Agents](#best-practices-for-ai-agents)
- [Research Strategy](#research-strategy)
  - [Phase 1: Information Gathering](#phase-1:-information-gathering)
  - [Phase 2: Validation & Testing](#phase-2:-validation-&-testing)
  - [Phase 3: Decision & Documentation](#phase-3:-decision-&-documentation)
- [Tools Usage](#tools-usage)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
  - [Domain Rules](#domain-rules)
  - [Standing Rules](#standing-rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand Off](#phase-4:-hand-off)
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
- [Prerequisites](#prerequisites)
- [Pitfalls](#pitfalls)
- [Summary](#summary)
- [Research Question(s)](#research-questions)
- [Investigation Plan](#investigation-plan)
- [Research Tasks](#research-tasks)
- [Success Criteria](#success-criteria)
- [Technical Context](#technical-context)
- [Research Findings](#research-findings)
- [Investigation Results](#investigation-results)
- [Prototype/Testing Notes](#prototype/testing-notes)
- [External Resources](#external-resources)
- [Decision](#decision)
- [Recommendation](#recommendation)
- [Rationale](#rationale)
- [Implementation Notes](#implementation-notes)
- [Follow-up Actions](#follow-up-actions)
- [Status History](#status-history)
- [Categories for Technical Spikes](#categories-for-technical-spikes)
- [File Naming Conventions](#file-naming-conventions)
- [Best Practices for AI Agents](#best-practices-for-ai-agents)
- [Research Strategy](#research-strategy)
- [Phase 1: Information Gathering](#phase-1:-information-gathering)
- [Phase 2: Validation & Testing](#phase-2:-validation-&-testing)
- [Phase 3: Decision & Documentation](#phase-3:-decision-&-documentation)
- [Tools Usage](#tools-usage)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
- [Domain Rules](#domain-rules)
- [Standing Rules](#standing-rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand Off](#phase-4:-hand-off)
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





Write time-boxed technical spike documents that research a single design question and produce a recommendation with evidence.

## Prerequisites

- A codebase or system context to investigate
- Access to relevant documentation, APIs, and dependencies
- A clear timebox and decision deadline

title: "${input:SpikeTitle}"category: "${input:Category|Technical}"status: "🔴 Not Started"priority: "${input:Priority|High}"timebox: "${input:Timebox|1 week}"created: [YYYY-MM-DD]updated: [YYYY-MM-DD]owner: "${input:Owner}"---
# ${input:SpikeTitle}

## Summary

**Spike Objective:** [Clear, specific question or decision that needs resolution]**Why This Matters:** [Impact on development/architecture decisions]**Timebox:** [How much time allocated to this spike]**Decision Deadline:** [When this must be resolved to avoid blocking development]

## Research Question(s)

**Primary Question:** [Main technical question that needs answering]**Secondary Questions:**

- [Related question 1]- [Related question 2]- [Related question 3]

## Investigation Plan

### Research Tasks

- [ ] [Specific research task 1]
- [ ] [Specific research task 2]
- [ ] [Specific research task 3]
- [ ] [Create proof of concept/prototype]
- [ ] [Document findings and recommendations]

### Success Criteria

**This spike is complete when:**

- [ ] [Specific criteria 1]
- [ ] [Specific criteria 2]
- [ ] [Clear recommendation documented]
- [ ] [Proof of concept completed (if applicable)]

## Technical Context

**Related Components:** [List system components affected by this decision]**Dependencies:** [What other spikes or decisions depend on resolving this]**Constraints:** [Known limitations or requirements that affect the solution]

## Research Findings

### Investigation Results

[Document research findings, test results, and evidence gathered]

### Prototype/Testing Notes

[Results from any prototypes, spikes, or technical experiments]

### External Resources

- [Link to relevant documentation]
- [Link to API references]
- [Link to community discussions]
- [Link to examples/tutorials]

## Decision

### Recommendation

[Clear recommendation based on research findings]

### Rationale

[Why this approach was chosen over alternatives]

### Implementation Notes

[Key considerations for implementation]

### Follow-up Actions

- [ ] [Action item 1]
- [ ] [Action item 2]
- [ ] [Update architecture documents]
- [ ] [Create implementation tasks]

## Status History

| Date | Status | Notes || -----

- | -------------- | ------------------------ || [Date] | 🔴 Not Started | Spike created and scoped || [Date] | 🟡 In Progress | Research commenced || [Date] | 🟢 Complete | [Resolution summary] |---_Last updated: [Date] by [Name]_```

## Categories for Technical Spikes

> - Third-party API capabilities and limitations
> - Integration patterns and authentication
> **Full content:**

## File Naming Conventions

Use descriptive, kebab-case names that indicate the category and specific unknown.

## Best Practices for AI Agents

1. **One Question Per Spike:** Each document focuses on a single technical decision or research question

## Research Strategy

### Phase 1: Information Gathering

1. **Search existing documentation** using search/fetch tools
2. **Analyze codebase** for existing patterns and constraints
3. **Research external resources** (APIs, libraries, examples)

### Phase 2: Validation & Testing

1. **Create focused prototypes** to test specific hypotheses
2. **Run targeted experiments** to validate assumptions
3. **Document test results** with supporting evidence

### Phase 3: Decision & Documentation

1. **Synthesize findings** into clear recommendations
2. **Document implementation guidance** for development team
3. **Create follow-up tasks** for implementation

## Tools Usage

- **search/searchResults:** Research existing solutions and documentation- **fetch/githubRepo:** Analyze external APIs, libraries, and examples- **codebase:** Understand existing system constraints and patterns- **runTasks:** Execute prototypes and validation tests- **editFiles:** Update research progress and findings- **vscodeAPI:** Test VS Code extension capabilities and limitationsFocus on time-boxed research that resolves critical technical decisions and unblocks development progress.

## Template References

Detailed templates in `templates/create-technical-spike/`:- `categories_for_technical_spike.md`

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


Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Read existing code before writing new code.
- Match project conventions and style.
- Add tests for new functionality.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State when something fails.


### Phase 1: Intake

- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute

- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify

- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off

- Return final artifact or findings .
- Stop once the requested result is delivered.

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

- [`create-agentsmd.prompt.md`](create-agentsmd.prompt.md)
- [`create-architectural-decision-record.prompt.md`](create-architectural-decision-record.prompt.md)
- [`create-github-action-workflow-specification.prompt.md`](create-github-action-workflow-specification.prompt.md)
- [`create-github-issue-feature-from-specification.prompt.md`](create-github-issue-feature-from-specification.prompt.md)
- [`create-github-issues-feature-from-implementation-plan.prompt.md`](create-github-issues-feature-from-implementation-plan.prompt.md)
- [`create-github-issues-for-unmet-specification-requirements.prompt.md`](create-github-issues-for-unmet-specification-requirements.prompt.md)
- [`create-github-pull-request-from-specification.prompt.md`](create-github-pull-request-from-specification.prompt.md)
- [`create-implementation-plan.prompt.md`](create-implementation-plan.prompt.md)
- [`create-llms.prompt.md`](create-llms.prompt.md)
- [`create-oo-component-documentation.prompt.md`](create-oo-component-documentation.prompt.md)
- [`create-readme.prompt.md`](create-readme.prompt.md)
- [`create-specification.prompt.md`](create-specification.prompt.md)
- [`create-spring-boot-java-project.prompt.md`](create-spring-boot-java-project.prompt.md)
- [`create-spring-boot-kotlin-project.prompt.md`](create-spring-boot-kotlin-project.prompt.md)
- [`create-tldr-page.prompt.md`](create-tldr-page.prompt.md)
```
# Prompt template
Execute the workflow defined in this file.
```
