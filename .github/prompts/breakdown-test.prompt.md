---
name: breakdown-test
title: Test Plan Breakdown
description: Produce comprehensive test strategies, task breakdowns, and quality validation plans aligned to ISTQB and ISO 25010 for GitHub projects.
trigger: /breakdown-test
version: 1.0.0
author: Hermes Agent
tags:
  - testing
  - planning
  - qa
  - istqb
  - iso-25010
  - github
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
---
## Table of Contents

## Goal

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
- [Quality Standards Framework](#quality-standards-framework)
  - [ISTQB Framework Application](#istqb-framework-application)
  - [ISO 25010 Quality Model](#iso-25010-quality-model)
- [Input Requirements](#input-requirements)
  - [Core Feature Documents](#core-feature-documents)
- [Output Format](#output-format)
- [GitHub Issue Templates for Testing](#github-issue-templates-for-testing)
  - [Test Strategy Issue Template](#test-strategy-issue-template)
- [Test Strategy Overview](#test-strategy-overview)
- [ISTQB Framework Application](#istqb-framework-application)
- [ISO 25010 Quality Characteristics**Priority Assessment:**](#iso-25010-quality-characteristics**priority-assessment:**)
- [Quality Gates](#quality-gates)
- [Labels](#labels)
- [Estimate](#estimate)
  - [Playwright Test Implementation Issue Template](#playwright-test-implementation-issue-template)
- [Test Implementation Scope](#test-implementation-scope)
- [ISTQB Test Case Design](#istqb-test-case-design)
- [Test Cases to Implement**Functional Tests:**](#test-cases-to-implement**functional-tests:**)
- [Playwright Implementation Tasks](#playwright-implementation-tasks)
- [Acceptance Criteria](#acceptance-criteria)
- [Labels](#labels)
- [Estimate](#estimate)
  - [Quality Assurance Issue Template](#quality-assurance-issue-template)
- [Quality Validation Scope](#quality-validation-scope)
- [ISO 25010 Quality Assessment**Quality Characteristics Validation:**](#iso-25010-quality-assessment**quality-characteristics-validation:**)
- [Quality Gate](#quality-gate)
- [Quality Metrics](#quality-metrics)
- [Labels](#labels)
- [Estimate](#estimate)
- [Success Metrics](#success-metrics)
  - [Test Coverage Metrics](#test-coverage-metrics)
  - [Quality Validation Metrics](#quality-validation-metrics)
  - [Process Efficiency Metrics](#process-efficiency-metrics)
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
- [Quality Standards Framework](#quality-standards-framework)
- [ISTQB Framework Application](#istqb-framework-application)
- [ISO 25010 Quality Model](#iso-25010-quality-model)
- [Input Requirements](#input-requirements)
- [Core Feature Documents](#core-feature-documents)
- [Output Format](#output-format)
- [GitHub Issue Templates for Testing](#github-issue-templates-for-testing)
- [Test Strategy Issue Template](#test-strategy-issue-template)
- [Test Strategy Overview](#test-strategy-overview)
- [ISTQB Framework Application](#istqb-framework-application)
- [ISO 25010 Quality Characteristics**Priority Assessment:**](#iso-25010-quality-characteristics**priority-assessment:**)
- [Quality Gates](#quality-gates)
- [Labels](#labels)
- [Estimate](#estimate)
- [Playwright Test Implementation Issue Template](#playwright-test-implementation-issue-template)
- [Test Implementation Scope](#test-implementation-scope)
- [ISTQB Test Case Design](#istqb-test-case-design)
- [Test Cases to Implement**Functional Tests:**](#test-cases-to-implement**functional-tests:**)
- [Playwright Implementation Tasks](#playwright-implementation-tasks)
- [Acceptance Criteria](#acceptance-criteria)
- [Labels](#labels)
- [Estimate](#estimate)
- [Quality Assurance Issue Template](#quality-assurance-issue-template)
- [Quality Validation Scope](#quality-validation-scope)
- [ISO 25010 Quality Assessment**Quality Characteristics Validation:**](#iso-25010-quality-assessment**quality-characteristics-validation:**)
- [Quality Gate](#quality-gate)
- [Quality Metrics](#quality-metrics)
- [Labels](#labels)
- [Estimate](#estimate)
- [Success Metrics](#success-metrics)
- [Test Coverage Metrics](#test-coverage-metrics)
- [Quality Validation Metrics](#quality-validation-metrics)
- [Process Efficiency Metrics](#process-efficiency-metrics)
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





Test Planning and Quality Assurance prompt that generates comprehensive test strategies, task breakdowns, and quality validation plans for GitHub projects.


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

## Quality Standards Framework

### ISTQB Framework Application

- **Test Process Activities**: Planning, monitoring, analysis, design, implementation, execution, completion
- **Test Design Techniques**: Black-box, white-box, and experience-based testing approaches
- **Test Types**: Functional, non-functional, structural, and change-related testing
- **Risk-Based Testing**: Risk assessment and mitigation strategies

### ISO 25010 Quality Model

- **Quality Characteristics**: Functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, portability
- **Quality Validation**: Measurement and assessment approaches for each characteristic
- **Quality Gates**: Entry and exit criteria for quality checkpoints

## Input Requirements

Before using this prompt, ensure you have:

### Core Feature Documents

1. **Feature PRD**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}.md`
2. **Technical Breakdown**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/technical-breakdown.md`
3. **Implementation Plan**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md`
4. **GitHub Project Plan**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/project-plan.md`

## Output Format

> Create comprehensive test planning documentation:>
>
> 1. **Test Strategy**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/test-s
> **Full content:**

## GitHub Issue Templates for Testing

### Test Strategy Issue Template

```markdown
# Test Strategy: {Feature Name}

## Test Strategy Overview

Summary of testing approach based on ISTQB and ISO 25010

## ISTQB Framework Application

**Test Design Techniques Used:**- [ ] Equivalence Partitioning- [ ] Boundary Value Analysis- [ ] Decision Table Testing- [ ] State Transition Testing- [ ] Experience-Based Testing**Test Types Coverage:**- [ ] Functional Testing- [ ] Non-Functional Testing- [ ] Structural Testing- [ ] Change-Related Testing (Regression)

## ISO 25010 Quality Characteristics**Priority Assessment:**

- [ ] Functional Suitability: {Critical/High/Medium/Low}- [ ] Performance Efficiency: {Critical/High/Medium/Low}- [ ] Compatibility: {Critical/High/Medium/Low}- [ ] Usability: {Critical/High/Medium/Low}- [ ] Reliability: {Critical/High/Medium/Low}- [ ] Security: {Critical/High/Medium/Low}- [ ] Maintainability: {Critical/High/Medium/Low}- [ ] Portability: {Critical/High/Medium/Low}

## Quality Gates

- [ ] Entry criteria defined
- [ ] Exit criteria established
- [ ] Quality thresholds documented

## Labels
- `test-strategy`, `istqb`, `iso25010`, `quality-gates`

## Estimate

{Strategic planning effort: 2-3 story points}
```

### Playwright Test Implementation Issue Template

```markdown
# Playwright Tests: {Story/Component Name}

## Test Implementation Scope

Specific user story or component being tested

## ISTQB Test Case Design
**Test Design Technique**: {Selected ISTQB technique} **Test Type**: {Functional/Non-Functional/Structural/Change-Related} {Selected ISTQB technique} **Test Type**: {Functional/Non-Functional/Structural/Change-Related}

## Test Cases to Implement**Functional Tests:**

- [ ] Happy path scenarios- [ ] Error handling validation- [ ] Boundary value testing- [ ] Input validation testing**Non-Functional Tests:**- [ ] Performance testing (response time < {threshold})- [ ] Accessibility testing (WCAG compliance)- [ ] Cross-browser compatibility- [ ] Mobile responsiveness

## Playwright Implementation Tasks

- [ ] Page Object Model development- [ ] Test fixture setup- [ ] Test data management- [ ] Test case implementation- [ ] Visual regression tests- [ ] CI/CD integration

## Acceptance Criteria

- [ ] All test cases pass
- [ ] Code coverage targets met (>80%)
- [ ] Performance thresholds validated
- [ ] Accessibility standards verified

## Labels
- `playwright`, `e2e-test`, `quality-validation`

## Estimate

{Test implementation effort: 2-5 story points}
```

### Quality Assurance Issue Template

```markdown
# Quality Assurance: {Feature Name}

## Quality Validation Scope

Overall quality validation for feature/epic

## ISO 25010 Quality Assessment**Quality Characteristics Validation:**

- [ ] Functional Suitability: Completeness, correctness, appropriateness- [ ] Performance Efficiency: Time behavior, resource utilization, capacity- [ ] Usability: Interface aesthetics, accessibility, learnability, operability- [ ] Security: Confidentiality, integrity, authentication, authorization- [ ] Reliability: Fault tolerance, recovery, availability- [ ] Compatibility: Browser, device, integration compatibility- [ ] Maintainability: Code quality, modularity, testability- [ ] Portability: Environment adaptability, installation procedures

## Quality Gate

s Validation**Entry Criteria:**- [ ] All implementation tasks completed- [ ] Unit tests passing- [ ] Code review approved**Exit Criteria:**- [ ] All test types completed with

> 95% pass rate- [ ] No critical/high severity defects- [ ] Performance benchmarks met- [ ] Security validation passed

## Quality Metrics

- [ ] Test coverage: {target}%- [ ] Defect density: <{threshold} defects/KLOC- [ ] Performance: Response time <{threshold}ms- [ ] Accessibility: WCAG {level} compliance- [ ] Security: Zero critical vulnerabilities

## Labels
- `quality-assurance`, `iso25010`, `quality-gates`

## Estimate

{Quality validation effort: 3-5 story points}
```

## Success Metrics

### Test Coverage Metrics

- **Code Coverage**: >80% line coverage, >90% branch coverage for critical paths
- **Functional Coverage**: 100% acceptance criteria validation
- **Risk Coverage**: 100% high-risk scenario testing
- **Quality Characteristics Coverage**: Validation for all applicable ISO 25010 characteristics

### Quality Validation Metrics

- **Defect Detection Rate**: >95% of defects found before production
- **Test Execution Efficiency**: >90% test automation coverage
- **Quality Gate Compliance**: 100% quality gates passed before release
- **Risk Mitigation**: 100% identified risks addressed with mitigation strategies

### Process Efficiency Metrics

- **Test Planning Time**: <2 hours to create comprehensive test strategy
- **Test Implementation Speed**: <1 day per story point of test development
- **Quality Feedback Time**: <2 hours from test completion to quality assessment
- **Documentation Completeness**: 100% test issues have complete template informationThis comprehensive test planning approach ensures thorough quality validation aligned with industry standards while maintaining efficient project management and clear accountability for all testing activities.````

## Template References

Detailed templates in `templates/breakdown-test/`:- `output_format.md`

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

Same-family prompts:

- [`breakdown-epic-arch.prompt.md`](breakdown-epic-arch.prompt.md)
- [`breakdown-epic-pm.prompt.md`](breakdown-epic-pm.prompt.md)
- [`breakdown-feature-implementation.prompt.md`](breakdown-feature-implementation.prompt.md)
- [`breakdown-feature-prd.prompt.md`](breakdown-feature-prd.prompt.md)
- [`breakdown-plan.prompt.md`](breakdown-plan.prompt.md)

