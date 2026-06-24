---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Generate Standard OO Component Documentation
name: create-oo-component-documentation
agent: "agent"
description: "Create comprehensive, standardized documentation for object-oriented components following industry best practices and architectural documentation standards."
tools:
  [
    "changes",
    "search/codebase",
    "edit/editFiles",
    "extensions",
    "web/fetch",
    "githubRepo",
    "openSimpleBrowser",
    "problems",
    "runTasks",
    "search",
    "search/searchResults",
    "runCommands/terminalLastCommand",
    "runCommands/terminalSelection",
    "testFailure",
    "usages",
    "vscodeAPI"
  ]
---

## Goal

Create comprehensive, standardized documentation for object-oriented components following industry best practices and architectural documentation standards.

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

## Documentation Standards

- DOC-001: Follow C4 Model documentation levels (Context, Containers, Components, Code)
- DOC-002: Align with Arc42 software architecture documentation template
- DOC-003: Comply with IEEE 1016 Software Design Description standard
- DOC-004: Use Agile Documentation principles (just enough documentation that adds value)
- DOC-005: Target developers and maintainers as primary audience

## Analysis Instructions

- ANA-001: Determine path type (folder vs single file) and identify primary component
- ANA-002: Examine source code files for class structures and inheritance
- ANA-003: Identify design patterns and architectural decisions
- ANA-004: Document public APIs, interfaces, and dependencies
- ANA-005: Recognize creational/structural/behavioral patterns
- ANA-006: Document method parameters, return values, exceptions
- ANA-007: Assess performance, security, reliability, maintainability
- ANA-008: Infer integration patterns and data flow

## Language-Specific Optimizations

- LNG-001: **C#/.NET** - async/await, dependency injection, configuration, disposal
- LNG-002: **Java** - Spring framework, annotations, exception handling, packaging
- LNG-003: **TypeScript/JavaScript** - modules, async patterns, types, npm
- LNG-004: **Python** - packages, virtual environments, type hints, testing

## Error Handling

- ERR-001: Path doesn't exist - provide correct format guidance
- ERR-002: No source files found - suggest alternative locations
- ERR-003: Unclear structure - document findings and request clarification
- ERR-004: Non-standard patterns - document custom approaches
- ERR-005: Insufficient code - focus on available information, highlight gaps

## Output Format

Generate well-structured Markdown with clear heading hierarchy, code blocks, tables, bullet points, and proper formatting for readability and maintainability.

## File Location

The documentation should be saved in the `/docs/components/` directory and named according to the convention: `[component-name]-documentation.md`.

## Required Documentation Structure

The documentation file must follow the template below, ensuring that all sections are filled out appropriately. The front matter for the markdown should be structured correctly as per the example following:

````md
---
title: [Component Name] - Technical Documentation
component_path: `${input:ComponentPath}`
version: [Optional: e.g., 1.0, Date]
date_created: [YYYY-MM-DD]
last_updated: [Optional: YYYY-MM-DD]
owner: [Optional: Team/Individual responsible for this component]
tags: [Optional: List of relevant tags or categories, e.g., `component`,`service`,`tool`,`infrastructure`,`documentation`,`architecture` etc]
---

# [Component Name] Documentation

[A short concise introduction to the component and its purpose within the system.]

## 1. Component Overview

### Purpose/Responsibility

- OVR-001: State component's primary responsibility
- OVR-002: Define scope (included/excluded functionality)
- OVR-003: Describe system context and relationships

## 2. Architecture Section

> - ARC-001: Document design patterns used (Repository, Factory, Observer, etc.)
> - ARC-002: List internal and external dependencies with purposes

> **Full content:** `templates/create-oo-component-documentation/2_architecture_section.md`

## 3. Interface Documentation

- INT-001: Document all public interfaces and usage patterns
- INT-002: Create method/property reference table
- INT-003: Document events/callbacks/notification mechanisms

| Method/Property | Purpose | Parameters | Return Type | Usage Notes |
| --- | --- | --- | --- | --- |
| [Name] | [Purpose] | [Parameters] | [Type] | [Notes] |

## 4. Implementation Details

- IMP-001: Document main implementation classes and responsibilities
- IMP-002: Describe configuration requirements and initialization
- IMP-003: Document key algorithms and business logic
- IMP-004: Note performance characteristics and bottlenecks

## 5. Usage Examples

### Basic Usage

```csharp
// Basic usage example
var component = new ComponentName();
component.DoSomething();
```

### Advanced Usage

```csharp
// Advanced configuration patterns
var options = new ComponentOptions();
var component = ComponentFactory.Create(options);
await component.ProcessAsync(data);
```

- USE-001: Provide basic usage examples
- USE-002: Show advanced configuration patterns
- USE-003: Document best practices and recommended patterns

## 6. Quality Attributes

- QUA-001: Security (authentication, authorization, data protection)
- QUA-002: Performance (characteristics, scalability, resource usage)
- QUA-003: Reliability (error handling, fault tolerance, recovery)
- QUA-004: Maintainability (standards, testing, documentation)
- QUA-005: Extensibility (extension points, customization options)

## 7. Reference Information

- REF-001: List dependencies with versions and purposes
- REF-002: Complete configuration options reference
- REF-003: Testing guidelines and mock setup
- REF-004: Troubleshooting (common issues, error messages)
- REF-005: Related documentation links
- REF-006: Change history and migration notes

```

```


## Template References

Detailed templates in `templates/create-oo-component-documentation/`:
- `2_architecture_section.md`
