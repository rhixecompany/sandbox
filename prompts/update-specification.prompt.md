---
toolsets:
  - changes
  - search/codebase
  - edit/editFiles
  - extensions
  - web/fetch
  - githubRepo
  - openSimpleBrowser
  - problems
  - runTasks
  - search
  - search/searchResults
  - runCommands/terminalLastCommand
  - runCommands/terminalSelection
  - testFailure
  - usages
  - vscodeAPI
license: MIT
author: Hermes Agent
version: 1.0.0
title: Update Specification
name: update-specification
description: "Update an existing specification file for the solution, optimized for Generative AI consumption based on new requirements or updates to any existing code."
tags:
  - frontend
  - maintenance
  - ml
  - performance
  - prompts
  - specification
  - typescript
  - documentation
  - performance
  - planning
  - specification
metadata:
  hermes:
    related_skills: []
    tags:
    - update-specification.prompt

trigger: update-specification

---
metadata:
  hermes:
    related_skills: []
    tags:
    - update-specification.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - update-specification.prompt

## Goal

Update an existing specification file for the solution, optimized for Generative AI consumption based on new requirements or updates to any existing code.

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
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


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

## Best Practices for AI-Ready Specifications

> - Use precise, explicit, and unambiguous language.
> - Clearly distinguish between requirements, constraints, and recommendations.

> **Full content:** `templates/update-specification/best_practices_for_ai-rea.md`

## 1. Purpose & Scope

[Provide a clear, concise description of the specification's purpose and the scope of its application. State the intended audience and any assumptions.]

## 2. Definitions

[List and define all acronyms, abbreviations, and domain-specific terms used in this specification.]

## 3. Requirements, Constraints & Guidelines

[Explicitly list all requirements, constraints, rules, and guidelines. Use bullet points or tables for clarity.]

- **REQ-001**: Requirement 1
- **SEC-001**: Security Requirement 1
- **[3 LETTERS]-001**: Other Requirement 1
- **CON-001**: Constraint 1
- **GUD-001**: Guideline 1
- **PAT-001**: Pattern to follow 1

## 4. Interfaces & Data Contracts

[Describe the interfaces, APIs, data contracts, or integration points. Use tables or code blocks for schemas and examples.]

## 5. Acceptance Criteria

[Define clear, testable acceptance criteria for each requirement using Given-When-Then format where appropriate.]

- **AC-001**: Given [context], When [action], Then [expected outcome]
- **AC-002**: The system shall [specific behavior] when [condition]
- **AC-003**: [Additional acceptance criteria as needed]

## 6. Test Automation Strategy

[Define the testing approach, frameworks, and automation requirements.]

- **Test Levels**: Unit, Integration, End-to-End
- **Frameworks**: MSTest, FluentAssertions, Moq (for .NET applications)
- **Test Data Management**: [approach for test data creation and cleanup]
- **CI/CD Integration**: [automated testing in GitHub Actions pipelines]
- **Coverage Requirements**: [minimum code coverage thresholds]
- **Performance Testing**: [approach for load and performance testing]

## 7. Rationale & Context

[Explain the reasoning behind the requirements, constraints, and guidelines. Provide context for design decisions.]

## 8. Dependencies & External Integrations

> [Define the external systems, services, and architectural dependencies required 
> - **EXT-001**: [External system name] - [Purpose and integration type]

> **Full content:** `templates/update-specification/8_dependencies__external_.md`

## 9. Examples & Edge Cases

```code
// Code snippet or data example demonstrating the correct application of the guidelines, including edge cases
```
````

## 10. Validation Criteria

[List the criteria or tests that must be satisfied for compliance with this specification.]

## 11. Related Specifications / Further Reading

[Link to related spec 1] [Link to relevant external documentation]

```

```


## Template References

Detailed templates in `templates/update-specification/`:


## Template References

Templates in `templates/update-specification/`:
- `11_related_specifications.md`
- `3_requirements_constraint.md`
- `5_acceptance_criteria.md`
- `6_test_automation_strateg.md`
- `8_dependencies__external_.md`
- `9_examples__edge_cases.md`
- `best_practices_for_ai-rea.md`
- `inputs.md`
- `legacy_prompt_details.md`
- `phases.md`
- `rules.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
