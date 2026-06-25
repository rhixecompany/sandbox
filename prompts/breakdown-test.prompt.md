---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Test Planning & Quality Assurance Prompt
name: breakdown-test
description: "Test Planning and Quality Assurance prompt that generates comprehensive test strategies, task breakdowns, and quality validation plans for GitHub projects."
---

## Goal

Test Planning and Quality Assurance prompt that generates comprehensive test strategies, task breakdowns, and quality validation plans for GitHub projects.

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

## Goal

Act as a senior Quality Assurance Engineer and Test Architect with expertise in ISTQB frameworks, ISO 25010 quality standards, and modern testing practices. Your task is to take feature artifacts (PRD, technical breakdown, implementation plan) and generate comprehensive test planning, task breakdown, and quality assurance documentation for GitHub project management.

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

> Create comprehensive test planning documentation:
> 1. **Test Strategy**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/test-s

> **Full content:** `templates/breakdown-test/output_format.md`

## GitHub Issue Templates for Testing

### Test Strategy Issue Template

```markdown
# Test Strategy: {Feature Name}

## Test Strategy Overview

{Summary of testing approach based on ISTQB and ISO 25010}

## ISTQB Framework Application

**Test Design Techniques Used:**

- [ ] Equivalence Partitioning
- [ ] Boundary Value Analysis
- [ ] Decision Table Testing
- [ ] State Transition Testing
- [ ] Experience-Based Testing

**Test Types Coverage:**

- [ ] Functional Testing
- [ ] Non-Functional Testing
- [ ] Structural Testing
- [ ] Change-Related Testing (Regression)

## ISO 25010 Quality Characteristics

**Priority Assessment:**

- [ ] Functional Suitability: {Critical/High/Medium/Low}
- [ ] Performance Efficiency: {Critical/High/Medium/Low}
- [ ] Compatibility: {Critical/High/Medium/Low}
- [ ] Usability: {Critical/High/Medium/Low}
- [ ] Reliability: {Critical/High/Medium/Low}
- [ ] Security: {Critical/High/Medium/Low}
- [ ] Maintainability: {Critical/High/Medium/Low}
- [ ] Portability: {Critical/High/Medium/Low}

## Quality Gates

- [ ] Entry criteria defined
- [ ] Exit criteria established
- [ ] Quality thresholds documented

## Labels

`test-strategy`, `istqb`, `iso25010`, `quality-gates`

## Estimate

{Strategic planning effort: 2-3 story points}
```

### Playwright Test Implementation Issue Template

```markdown
# Playwright Tests: {Story/Component Name}

## Test Implementation Scope

{Specific user story or component being tested}

## ISTQB Test Case Design

**Test Design Technique**: {Selected ISTQB technique} **Test Type**: {Functional/Non-Functional/Structural/Change-Related}

## Test Cases to Implement

**Functional Tests:**

- [ ] Happy path scenarios
- [ ] Error handling validation
- [ ] Boundary value testing
- [ ] Input validation testing

**Non-Functional Tests:**

- [ ] Performance testing (response time < {threshold})
- [ ] Accessibility testing (WCAG compliance)
- [ ] Cross-browser compatibility
- [ ] Mobile responsiveness

## Playwright Implementation Tasks

- [ ] Page Object Model development
- [ ] Test fixture setup
- [ ] Test data management
- [ ] Test case implementation
- [ ] Visual regression tests
- [ ] CI/CD integration

## Acceptance Criteria

- [ ] All test cases pass
- [ ] Code coverage targets met (>80%)
- [ ] Performance thresholds validated
- [ ] Accessibility standards verified

## Labels

`playwright`, `e2e-test`, `quality-validation`

## Estimate

{Test implementation effort: 2-5 story points}
```

### Quality Assurance Issue Template

```markdown
# Quality Assurance: {Feature Name}

## Quality Validation Scope

{Overall quality validation for feature/epic}

## ISO 25010 Quality Assessment

**Quality Characteristics Validation:**

- [ ] Functional Suitability: Completeness, correctness, appropriateness
- [ ] Performance Efficiency: Time behavior, resource utilization, capacity
- [ ] Usability: Interface aesthetics, accessibility, learnability, operability
- [ ] Security: Confidentiality, integrity, authentication, authorization
- [ ] Reliability: Fault tolerance, recovery, availability
- [ ] Compatibility: Browser, device, integration compatibility
- [ ] Maintainability: Code quality, modularity, testability
- [ ] Portability: Environment adaptability, installation procedures

## Quality Gates Validation

**Entry Criteria:**

- [ ] All implementation tasks completed
- [ ] Unit tests passing
- [ ] Code review approved

**Exit Criteria:**

- [ ] All test types completed with >95% pass rate
- [ ] No critical/high severity defects
- [ ] Performance benchmarks met
- [ ] Security validation passed

## Quality Metrics

- [ ] Test coverage: {target}%
- [ ] Defect density: <{threshold} defects/KLOC
- [ ] Performance: Response time <{threshold}ms
- [ ] Accessibility: WCAG {level} compliance
- [ ] Security: Zero critical vulnerabilities

## Labels

`quality-assurance`, `iso25010`, `quality-gates`

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
- **Documentation Completeness**: 100% test issues have complete template information

This comprehensive test planning approach ensures thorough quality validation aligned with industry standards while maintaining efficient project management and clear accountability for all testing activities.

````


## Template References

Detailed templates in `templates/breakdown-test/`:
- `output_format.md`
