---

name: create-github-action-workflow-specification

title: Create GitHub Actions Workflow Specification

description: 'Create a formal specification for an existing GitHub Actions CI/CD workflow, optimized for AI consumption and workflow maintenance.'

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - web

scripts: []

skills: []

formatter: default

plan: None

tags:

  - ci-cd

  - generator

  - git

  - ml

  - performance

  - prompts

  - specification

  - typescript

  - workflow

trigger: /create-github-action-workflow-specification

dependencies: []

metadata:

  hermes: {}

---

## Goal

Create a formal specification for an existing GitHub Actions CI/CD workflow, optimized for AI consumption and workflow maintenance.

## Workflow Overview

**Purpose**: [One sentence describing workflow's primary goal] **Trigger Events**: [List trigger conditions] **Target Environments**: [Environment scope]

## Execution Flow Diagram

```mermaid
graph TD    A[Trigger Event] --

> B[Job 1]    B --
> C[Job 2]    C --
> D[Job 3]    D --
> E[End]    B --
> F[Parallel Job]    F --
> D    style A fill:#e1f5fe    style E fill:#e8f5e8```````

## Jobs & Dependencies| Job Name | Purpose   | Dependencies    | Execution Context    || -------

- | --------- | --------------- | -------------------- || job-1    | [Purpose] | [Prerequisites] | [Runner/Environment] || job-2    | [Purpose] | job-1           | [Runner/Environment] |

## Requirements Matrix>

### Functional Requirements>

### Security Requirements

## Input

/Output Contracts

### Input

s

```

yaml# Environment VariablesENV_VAR_1: string # Purpose: [description]ENV_VAR_2: secret # Purpose: [description]# Repository Triggerspaths: [list of path filters]branches: [list of branch patterns]

```

## Output

s

```

yaml# Job Outputsjob_1_output: string # Description: [purpose]build_artifact: file # Description: [content type]

```

## Secrets & Variables| Type     | Name     | Purpose   | Scope      || -------

- | -------- | --------- | ---------- || Secret   | SECRET_1 | [Purpose] | Workflow   || Variable | VAR_1    | [Purpose] | Repository |

## Execution Constraints

### Runtime Constraints

- **Timeout**: [Maximum execution time]
- **Concurrency**: [Parallel execution limits]
- **Resource Limits**: [Memory/CPU constraints]

### Environmental Constraints

- **Runner Requirements**: [OS/hardware needs]
- **Network Access**: [External connectivity needs]
- **Permissions**: [Required access levels]

## Error Handling Strategy| Error Type         | Response   | Recovery Action  || -----------------

- | ---------- | ---------------- || Build Failure      | [Response] | [Recovery steps] || Test Failure       | [Response] | [Recovery steps] || Deployment Failure | [Response] | [Recovery steps] |

## Quality Gate

s

### Gate Definitions| Gate          | Criteria     | Bypass Conditions || ------------

- | ------------ | ----------------- || Code Quality  | [Standards]  | [When allowed]    || Security Scan | [Thresholds] | [When allowed]    || Test Coverage | [Percentage] | [When allowed]    |

## Monitoring & Observability

### Key Metrics

- **Success Rate**: [Target percentage]
- **Execution Time**: [Target duration]
- **Resource Usage**: [Monitoring approach]

### Alerting| Condition   | Severity | Notification Target || ----------

- | -------- | ------------------- || [Condition] | [Level]  | [Who/Where]         |

## Integration Points

### External Systems| System   | Integration Type | Data Exchange | SLA Requirements || -------

- | ---------------- | ------------- | ---------------- || [System] | [Type]           | [Data format] | [Requirements]   |

### Dependent Workflows| Workflow   | Relationship | Trigger Mechanism || ---------

- | ------------ | ----------------- || [Workflow] | [Type]       | [How triggered]   |

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

### Scenario Matrix| Scenario    | Expected Behavior | Validation Method || ----------

- | ----------------- | ----------------- || [Edge case] | [Behavior]        | [How to verify]   |

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

### Version History| Version | Date   | Changes               | Author   || ------

- | ------ | --------------------- | -------- || 1.0     | [Date] | Initial specification | [Author] |

## Related Specifications

- [Link to related workflow specs]- [Link to infrastructure specs]- [Link to deployment specs]````

## Analysis Instructions

When analyzing the workflow file:1. **Extract Core Purpose**: Identify the primary business objective2. **Map Job Flow**: Create dependency graph showing execution order3. **Identify Contracts**: Document inputs, outputs, and interfaces4. **Capture Constraints**: Extract timeouts, permissions, and limits5. **Define Quality Gates**: Identify validation and approval points6. **Document Error Paths**: Map failure scenarios and recovery7. **Abstract Implementation**: Focus on behavior, not syntax

## Mermaid Diagram Guidelines

> - **Sequential**: `A --
> B --
> C`
> - **Parallel**: `A --
> B & A --
> C; B --
> D & C --
> D`
> **Full content:**

## Token Optimization Strategies

1. **Use Tables**: Dense information in structured format2. **Abbreviate Consistently**: Define once, use throughout3. **Bullet Points**: Avoid prose paragraphs4. **Code Blocks**: Structured data over narrative5. **Cross-Reference**: Link instead of repeat informationFocus on creating a specification that serves as both documentation and a template for workflow updates.
```

## Template References

Detailed templates in `templates/create-github-action-workflow-specification/`:

## Template References

Templates in `templates/create-github-action-workflow-specification/`:- `ai-optimized_requirements.md`- `analysis_instructions.md`- `change_management.md`- `compliance__governance.md`- `edge_cases__exceptions.md`- `error_handling_strategy.md`- `execution_constraints.md`- `execution_flow_diagram.md`- `inputoutput_contracts.md`- `inputs.md`- `integration_points.md`- `jobs__dependencies.md`- `legacy_prompt_details.md`- `mermaid_diagram_guideline.md`- `monitoring__observability.md`- `outputs.md`- `phases.md`- `quality_gates.md`- `related_specifications.md`- `requirements_matrix.md`- `rules.md`- `secrets__variables.md`- `specification_template.md`- `token_optimization_strate.md`- `validation_criteria.md`

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

## Context

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State clearly when something fails.

## Phases

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

- Return final artifact or findings clearly.
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
