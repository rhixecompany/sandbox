---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Comprehensive Project Architecture Blueprint Generator
name: architecture-blueprint-generator
description: "Comprehensive project architecture blueprint generator that analyzes codebases to create detailed architectural documentation. Automatically detects technology stacks and architectural patterns, generates visual diagrams, documents implementation patterns, and provides extensible blueprints for maintaining architectural consistency and guiding new development."
---

## Goal

Comprehensive project architecture blueprint generator that analyzes codebases to create detailed architectural documentation. Automatically detects technology stacks and architectural patterns, generates visual diagrams, documents implementation patterns, and provides extensible blueprints for maintaining architectural consistency and guiding new development.

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

## Configuration Variables

${PROJECT_TYPE="Auto-detect|.NET|Java|React|Angular|Python|Node.js|Flutter|Other"} <!-- Primary technology -->
${ARCHITECTURE_PATTERN="Auto-detect|Clean Architecture|Microservices|Layered|MVVM|MVC|Hexagonal|Event-Driven|Serverless|Monolithic|Other"} <!-- Primary architectural pattern --> ${DIAGRAM_TYPE="C4|UML|Flow|Component|None"} <!-- Architecture diagram type -->
${DETAIL_LEVEL="High-level|Detailed|Comprehensive|Implementation-Ready"} <!-- Level of detail to include --> ${INCLUDES_CODE_EXAMPLES=true|false} <!-- Include sample code to illustrate patterns -->
${INCLUDES_IMPLEMENTATION_PATTERNS=true|false} <!-- Include detailed implementation patterns --> ${INCLUDES_DECISION_RECORDS=true|false} <!-- Include architectural decision records -->
${FOCUS_ON_EXTENSIBILITY=true|false} <!-- Emphasize extension points and patterns -->

## Generated Prompt

> "Create a comprehensive 'Project_Architecture_Blueprint.md' document that thorou
> ### 1. Architecture Detection and Analysis

> **Full content:** `templates/architecture-blueprint-generator/generated_prompt.md`

## Template References

Detailed templates in `templates/architecture-blueprint-generator/`:
- `generated_prompt.md`
