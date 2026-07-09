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
title: Update Oo Component Documentation
name: update-oo-component-documentation
description: "Update existing object-oriented component documentation following industry best practices and architectural documentation standards."
tags:
  - architecture
  - documentation
  - maintenance
  - ml
  - prompts
  - specification
  - typescript
  - architecture
  - documentation
  - linux
  - planning
  - specification
---

## Goal

Update existing object-oriented component documentation following industry best practices and architectural documentation standards.

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

## 1. Component Overview

### Purpose/Responsibility

- OVR-001: Update component's primary responsibility
- OVR-002: Refresh scope (included/excluded functionality)
- OVR-003: Update system context and relationships

## 2. Architecture Section

- ARC-001: Update design patterns used (Repository, Factory, Observer, etc.)
- ARC-002: Refresh internal and external dependencies with current purposes
- ARC-003: Update component interactions and relationships
- ARC-004: Update visual diagrams (UML class, sequence, component)
- ARC-005: Refresh mermaid diagram showing current component structure, relationships, and dependencies

### Component Structure and Dependencies Diagram

Update the mermaid diagram to show current:

- **Component structure** - Current classes, interfaces, and their relationships
- **Internal dependencies** - How components currently interact within the system
- **External dependencies** - Current external libraries, services, databases, APIs
- **Data flow** - Current direction of dependencies and interactions
- **Inheritance/composition** - Current class hierarchies and composition relationships

```mermaid
[Update diagram to reflect current architecture]
```
````

## 3. Interface Documentation

- INT-001: Update all public interfaces and current usage patterns
- INT-002: Refresh method/property reference table with current API
- INT-003: Update events/callbacks/notification mechanisms

| Method/Property | Purpose | Parameters | Return Type | Usage Notes |
| --- | --- | --- | --- | --- |
| [Update table with current API] |  |  |  |  |

## 4. Implementation Details

- IMP-001: Update main implementation classes and current responsibilities
- IMP-002: Refresh configuration requirements and initialization patterns
- IMP-003: Update key algorithms and business logic
- IMP-004: Update performance characteristics and bottlenecks

## 5. Usage Examples

### Basic Usage

```csharp
// Update basic usage example to current API
```

### Advanced Usage

```csharp
// Update advanced configuration patterns to current implementation
```

- USE-001: Update basic usage examples
- USE-002: Refresh advanced configuration patterns
- USE-003: Update best practices and recommended patterns

## 6. Quality Attributes

- QUA-001: Update security (authentication, authorization, data protection)
- QUA-002: Refresh performance (characteristics, scalability, resource usage)
- QUA-003: Update reliability (error handling, fault tolerance, recovery)
- QUA-004: Refresh maintainability (standards, testing, documentation)
- QUA-005: Update extensibility (extension points, customization options)

## 7. Reference Information

- REF-001: Update dependencies with current versions and purposes
- REF-002: Refresh configuration options reference
- REF-003: Update testing guidelines and mock setup
- REF-004: Refresh troubleshooting (common issues, error messages)
- REF-005: Update related documentation links
- REF-006: Add change history and migration notes for this update

```

```


## Template References

Detailed templates in `templates/update-oo-component-documentation/`:
- `legacy_prompt_details.md`
