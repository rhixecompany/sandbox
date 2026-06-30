---
toolsets:
  - vscode/vscodeAPI
  - vscode/extensions
  - execute/testFailure
  - execute/runTask
  - execute/createAndRunTask
  - read/problems
  - read/readFile
  - read/terminalSelection
  - read/terminalLastCommand
  - read/getTaskOutput
  - agent
  - edit/editFiles
  - search
  - web
  - github/*
  - browser
  - vscode.mermaid-chat-features/renderMermaidDiagram
  - ms-azuretools.vscode-containers/containerToolsConfig
  - todo
license: MIT
author: Hermes Agent
version: 1.0.0
title: Create Implementation Plan
name: create-implementation-plan
description: "Create a new implementation plan file for new features, refactoring existing code or upgrading packages, design, architecture or infrastructure."
tags:
  - architecture
  - generator
  - ml
  - prompts
  - refactoring
  - specification
  - typescript
  - architecture
  - documentation
  - generator
  - linux
  - planning
  - refactoring
  - specification
metadata:
  hermes:
    related_skills: []
    tags:
    - create-implementation-plan.prompt

trigger: create-implementation-plan

---
metadata:
  hermes:
    related_skills: []
    tags:
    - create-implementation-plan.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - create-implementation-plan.prompt

## Goal

Create a new implementation plan file for new features, refactoring existing code or upgrading packages, design, architecture or infrastructure.

## Context

Use when you need to update or create a plan for the current workspace or task.

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

## Primary Directive

Your goal is to create a new implementation plan file for `${input:PlanPurpose}`. Your output must be machine-readable, deterministic, and structured for autonomous execution by other AI systems or humans.

## Execution Context

This prompt is designed for AI-to-AI communication and automated processing. All instructions must be interpreted literally and executed systematically without human interpretation or clarification.

## Core Requirements

- Generate implementation plans that are fully executable by AI agents or humans
- Use deterministic language with zero ambiguity
- Structure all content for automated parsing and execution
- Ensure complete self-containment with no external dependencies for understanding

## Plan Structure Requirements

Plans must consist of discrete, atomic phases containing executable tasks. Each phase must be independently processable by AI agents or humans without cross-phase dependencies unless explicitly declared.

## Phase Architecture

- Each phase must have measurable completion criteria
- Tasks within phases must be executable in parallel unless dependencies are specified
- All task descriptions must include specific file paths, function names, and exact implementation details
- No task should require human interpretation or decision-making

## AI-Optimized Implementation Standards

- Use explicit, unambiguous language with zero interpretation required
- Structure all content as machine-parseable formats (tables, lists, structured data)
- Include specific file paths, line numbers, and exact code references where applicable
- Define all variables, constants, and configuration values explicitly
- Provide complete context within each task description
- Use standardized prefixes for all identifiers (REQ-, TASK-, etc.)
- Include validation criteria that can be automatically verified

## Output File Specifications

- Save implementation plan files in `/plan/` directory
- Use naming convention: `[purpose]-[component]-[version].md`
- Purpose prefixes: `upgrade|refactor|feature|data|infrastructure|process|architecture|design`
- Example: `upgrade-system-command-4.md`, `feature-auth-module-1.md`
- File must be valid Markdown with proper front matter structure

## Mandatory Template Structure

All implementation plans must strictly adhere to the following template. Each section is required and must be populated with specific, actionable content. AI agents must validate template compliance before execution.

## Template Validation Rules

- All front matter fields must be present and properly formatted
- All section headers must match exactly (case-sensitive)
- All identifier prefixes must follow the specified format
- Tables must include all required columns
- No placeholder text may remain in the final output

## Status

> The status of the implementation plan must be clearly defined in the front matte
> goal: [Concise Title Describing the Package Implementation Plan's Goal]

> **Full content:** `templates/create-implementation-plan/status.md`

## 1. Requirements & Constraints

[Explicitly list all requirements & constraints that affect the plan and constrain how it is implemented. Use bullet points or tables for clarity.]

- **REQ-001**: Requirement 1
- **SEC-001**: Security Requirement 1
- **[3 LETTERS]-001**: Other Requirement 1
- **CON-001**: Constraint 1
- **GUD-001**: Guideline 1
- **PAT-001**: Pattern to follow 1

## 2. Implementation Steps

> ### Implementation Phase 1
> - GOAL-001: [Describe the goal of this phase, e.g., "Implement feature X", "Refa

> **Full content:** `templates/create-implementation-plan/2_implementation_steps.md`

## 3. Alternatives

[A bullet point list of any alternative approaches that were considered and why they were not chosen. This helps to provide context and rationale for the chosen approach.]

- **ALT-001**: Alternative approach 1
- **ALT-002**: Alternative approach 2

## 4. Dependencies

[List any dependencies that need to be addressed, such as libraries, frameworks, or other components that the plan relies on.]

- **DEP-001**: Dependency 1
- **DEP-002**: Dependency 2

## 5. Files

[List the files that will be affected by the feature or refactoring task.]

- **FILE-001**: Description of file 1
- **FILE-002**: Description of file 2

## 6. Testing

[List the tests that need to be implemented to verify the feature or refactoring task.]

- **TEST-001**: Description of test 1
- **TEST-002**: Description of test 2

## 7. Risks & Assumptions

[List any risks or assumptions related to the implementation of the plan.]

- **RISK-001**: Risk 1
- **ASSUMPTION-001**: Assumption 1

## 8. Related Specifications / Further Reading

[Link to related spec 1] [Link to relevant external documentation]
````


## Template References

Detailed templates in `templates/create-implementation-plan/`:


## Template References

Templates in `templates/create-implementation-plan/`:
- `1_requirements__constrain.md`
- `2_implementation_steps.md`
- `3_alternatives.md`
- `4_dependencies.md`
- `5_files.md`
- `6_testing.md`
- `7_risks__assumptions.md`
- `8_related_specifications_.md`
- `ai-optimized_implementati.md`
- `core_requirements.md`
- `inputs.md`
- `output_file_specification.md`
- `phase_architecture.md`
- `phases.md`
- `rules.md`
- `status.md`
- `template_validation_rules.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
