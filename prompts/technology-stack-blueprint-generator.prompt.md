---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Comprehensive Technology Stack Blueprint Generator
name: technology-stack-blueprint-generator
description: "Comprehensive technology stack blueprint generator that analyzes codebases to create detailed architectural documentation. Automatically detects technology stacks, programming languages, and implementation patterns across multiple platforms (.NET, Java, JavaScript, React, Python). Generates configurable blueprints with version information, licensing details, usage patterns, coding conventions, and visual diagrams. Provides implementation-ready templates and maintains architectural consistency for guided development."
tags:
  - architecture
  - configuration
  - csharp
  - documentation
  - dotnet
  - frontend
  - generator
  - java
  - javascript
  - ml
  - prompts
  - python
  - react
  - typescript
  - architecture
  - csharp
  - database
  - documentation
  - dotnet
  - drizzle
  - java
  - javascript
  - linux
  - python
  - react
---

## Goal

Comprehensive technology stack blueprint generator that analyzes codebases to create detailed architectural documentation. Automatically detects technology stacks, programming languages, and implementation patterns across multiple platforms (.NET, Java, JavaScript, React, Python). Generates configurable blueprints with version information, licensing details, usage patterns, coding conventions, and visual diagrams. Provides implementation-ready templates and maintains architectural consistency for guided development.

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

## Configuration Variables

${PROJECT_TYPE="Auto-detect|.NET|Java|JavaScript|React.js|React Native|Angular|Python|Other"} <!-- Primary technology -->
${DEPTH_LEVEL="Basic|Standard|Comprehensive|Implementation-Ready"} <!-- Analysis depth --> ${INCLUDE_VERSIONS=true|false} <!-- Include version information -->
${INCLUDE_LICENSES=true|false} <!-- Include license information --> ${INCLUDE_DIAGRAMS=true|false} <!-- Generate architecture diagrams -->
${INCLUDE_USAGE_PATTERNS=true|false} <!-- Include code usage patterns --> ${INCLUDE_CONVENTIONS=true|false} <!-- Document coding conventions -->
${OUTPUT_FORMAT="Markdown|JSON|YAML|HTML"} <!-- Select output format --> ${CATEGORIZATION="Technology Type|Layer|Purpose"} <!-- Organization method -->

## Generated Prompt

> "Analyze the codebase and generate a ${DEPTH_LEVEL} technology stack blueprint t
> ### 1. Technology Identification Phase

> **Full content:** `templates/technology-stack-blueprint-generator/generated_prompt.md`

## Template References

Detailed templates in `templates/technology-stack-blueprint-generator/`:
- `generated_prompt.md`
