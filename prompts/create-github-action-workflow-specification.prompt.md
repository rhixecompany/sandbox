---
toolsets:
  - changes
  - search/codebase
  - edit/editFiles
  - extensions
  - web/fetch
  - findTestFiles
  - githubRepo
  - new
  - openSimpleBrowser
  - problems
  - runCommands
  - runInTerminal2
  - runNotebooks
  - runTasks
  - runTests
  - search
  - search/searchResults
  - runCommands/terminalLastCommand
  - runCommands/terminalSelection
  - testFailure
  - usages
  - vscodeAPI
  - microsoft.docs.mcp
  - github
  - Microsoft Docs
license: MIT
author: Hermes Agent
version: 1.0.0
title: Create GitHub Actions Workflow Specification
name: create-github-action-workflow-specification
description: "Create a formal specification for an existing GitHub Actions CI/CD workflow, optimized for AI consumption and workflow maintenance."
tags: []
---

## Goal

Create a formal specification for an existing GitHub Actions CI/CD workflow, optimized for AI consumption and workflow maintenance.

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

## AI-Optimized Requirements

- **Token Efficiency**: Use concise language without sacrificing clarity
- **Structured Data**: Leverage tables, lists, and diagrams for dense information
- **Semantic Clarity**: Use precise terminology consistently throughout
- **Implementation Abstraction**: Avoid specific syntax, commands, or tool versions
- **Maintainability**: Design for easy updates as workflow evolves

## Specification Template

Save as: `/spec/spec-process-cicd-[workflow-name].md`

````md
---
title: CI/CD Workflow Specification - [Workflow Name]
version: 1.0
date_created: [YYYY-MM-DD]
last_updated: [YYYY-MM-DD]
owner: DevOps Team
tags:
  [process, cicd, github-actions, automation, [domain-specific-tags]]
---

## Workflow Overview

**Purpose**: [One sentence describing workflow's primary goal] **Trigger Events**: [List trigger conditions] **Target Environments**: [Environment scope]

## Execution Flow Diagram

```mermaid
graph TD
    A[Trigger Event] --> B[Job 1]
    B --> C[Job 2]
    C --> D[Job 3]
    D --> E[End]

    B --> F[Parallel Job]
    F --> D

    style A fill:#e1f5fe
    style E fill:#e8f5e8
```
````

## Jobs & Dependencies

| Job Name | Purpose   | Dependencies    | Execution Context    |
| -------- | --------- | --------------- | -------------------- |
| job-1    | [Purpose] | [Prerequisites] | [Runner/Environment] |
| job-2    | [Purpose] | job-1           | [Runner/Environment] |

## Requirements Matrix

> ### Functional Requirements
> ### Security Requirements

> **Full content:** `templates/create-github-action-workflow-specification/requirements_matrix.md`

## Input/Output Contracts

### Inputs

```yaml
# Environment Variables
ENV_VAR_1: string # Purpose: [description]
ENV_VAR_2: secret # Purpose: [description]

# Repository Triggers
paths: [list of path filters]
branches: [list of branch patterns]
```

## Outputs

```yaml
# Job Outputs
job_1_output: string # Description: [purpose]
build_artifact: file # Description: [content type]
```

## Secrets & Variables

| Type     | Name     | Purpose   | Scope      |
| -------- | -------- | --------- | ---------- |
| Secret   | SECRET_1 | [Purpose] | Workflow   |
| Variable | VAR_1    | [Purpose] | Repository |

## Execution Constraints

### Runtime Constraints

- **Timeout**: [Maximum execution time]
- **Concurrency**: [Parallel execution limits]
- **Resource Limits**: [Memory/CPU constraints]

### Environmental Constraints

- **Runner Requirements**: [OS/hardware needs]
- **Network Access**: [External connectivity needs]
- **Permissions**: [Required access levels]

## Error Handling Strategy

| Error Type         | Response   | Recovery Action  |
| ------------------ | ---------- | ---------------- |
| Build Failure      | [Response] | [Recovery steps] |
| Test Failure       | [Response] | [Recovery steps] |
| Deployment Failure | [Response] | [Recovery steps] |

## Quality Gates

### Gate Definitions

| Gate          | Criteria     | Bypass Conditions |
| ------------- | ------------ | ----------------- |
| Code Quality  | [Standards]  | [When allowed]    |
| Security Scan | [Thresholds] | [When allowed]    |
| Test Coverage | [Percentage] | [When allowed]    |

## Monitoring & Observability

### Key Metrics

- **Success Rate**: [Target percentage]
- **Execution Time**: [Target duration]
- **Resource Usage**: [Monitoring approach]

### Alerting

| Condition   | Severity | Notification Target |
| ----------- | -------- | ------------------- |
| [Condition] | [Level]  | [Who/Where]         |

## Integration Points

### External Systems

| System   | Integration Type | Data Exchange | SLA Requirements |
| -------- | ---------------- | ------------- | ---------------- |
| [System] | [Type]           | [Data format] | [Requirements]   |

### Dependent Workflows

| Workflow   | Relationship | Trigger Mechanism |
| ---------- | ------------ | ----------------- |
| [Workflow] | [Type]       | [How triggered]   |

## Compliance & Governance

### Audit Requirements

- **Execution Logs**: [Retention policy]
- **Approval Gates**: [Required approvals]
- **Change Control**: [Update process]

### Security Controls

- **Access Control**: [Permission model]
- **Secret Management**: [Rotation policy]
- **Vulnerability Scanning**: [Scan frequency]

## Edge Cases & Exceptions

### Scenario Matrix

| Scenario    | Expected Behavior | Validation Method |
| ----------- | ----------------- | ----------------- |
| [Edge case] | [Behavior]        | [How to verify]   |

## Validation Criteria

### Workflow Validation

- **VLD-001**: [Validation rule]
- **VLD-002**: [Validation rule]

### Performance Benchmarks

- **PERF-001**: [Benchmark criteria]
- **PERF-002**: [Benchmark criteria]

## Change Management

### Update Process

1. **Specification Update**: Modify this document first
2. **Review & Approval**: [Approval process]
3. **Implementation**: Apply changes to workflow
4. **Testing**: [Validation approach]
5. **Deployment**: [Release process]

### Version History

| Version | Date   | Changes               | Author   |
| ------- | ------ | --------------------- | -------- |
| 1.0     | [Date] | Initial specification | [Author] |

## Related Specifications

- [Link to related workflow specs]
- [Link to infrastructure specs]
- [Link to deployment specs]

````

## Analysis Instructions

When analyzing the workflow file:

1. **Extract Core Purpose**: Identify the primary business objective
2. **Map Job Flow**: Create dependency graph showing execution order
3. **Identify Contracts**: Document inputs, outputs, and interfaces
4. **Capture Constraints**: Extract timeouts, permissions, and limits
5. **Define Quality Gates**: Identify validation and approval points
6. **Document Error Paths**: Map failure scenarios and recovery
7. **Abstract Implementation**: Focus on behavior, not syntax

## Mermaid Diagram Guidelines

> - **Sequential**: `A --> B --> C`
> - **Parallel**: `A --> B & A --> C; B --> D & C --> D`

> **Full content:** `templates/create-github-action-workflow-specification/mermaid_diagram_guideline.md`

## Token Optimization Strategies

1. **Use Tables**: Dense information in structured format
2. **Abbreviate Consistently**: Define once, use throughout
3. **Bullet Points**: Avoid prose paragraphs
4. **Code Blocks**: Structured data over narrative
5. **Cross-Reference**: Link instead of repeat information

Focus on creating a specification that serves as both documentation and a template for workflow updates.
```


## Template References

Detailed templates in `templates/create-github-action-workflow-specification/`:


## Template References

Templates in `templates/create-github-action-workflow-specification/`:
- `ai-optimized_requirements.md`
- `analysis_instructions.md`
- `change_management.md`
- `compliance__governance.md`
- `edge_cases__exceptions.md`
- `error_handling_strategy.md`
- `execution_constraints.md`
- `execution_flow_diagram.md`
- `inputoutput_contracts.md`
- `inputs.md`
- `integration_points.md`
- `jobs__dependencies.md`
- `legacy_prompt_details.md`
- `mermaid_diagram_guideline.md`
- `monitoring__observability.md`
- `outputs.md`
- `phases.md`
- `quality_gates.md`
- `related_specifications.md`
- `requirements_matrix.md`
- `rules.md`
- `secrets__variables.md`
- `specification_template.md`
- `token_optimization_strate.md`
- `validation_criteria.md`
