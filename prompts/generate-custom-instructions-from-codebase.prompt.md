---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Migration and Code Evolution Instructions Generator
name: generate-custom-instructions-from-codebase
description: "Migration and code evolution instructions generator for GitHub Copilot. Analyzes differences between two project versions (branches, commits, or releases) to create precise instructions allowing Copilot to maintain consistency during technology migrations, major refactoring, or framework version upgrades."
tags:
  - ai-assistant
  - generator
  - git
  - migration
  - ml
  - prompts
  - refactoring
  - specification
  - typescript
  - ai-assistant
  - ci-cd
  - documentation
  - github
  - migration
  - planning
  - refactoring
  - specification
metadata:
  hermes:
    related_skills: []
    tags:
    - generate-custom-instructions-from-codebase.prompt

trigger: generate-custom-instructions-from-codebase

---
metadata:
  hermes:
    related_skills: []
    tags:
    - generate-custom-instructions-from-codebase.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - generate-custom-instructions-from-codebase.prompt

## Goal

Migration and code evolution instructions generator for GitHub Copilot. Analyzes differences between two project versions (branches, commits, or releases) to create precise instructions allowing Copilot to maintain consistency during technology migrations, major refactoring, or framework version upgrades.

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

```
${MIGRATION_TYPE="Framework Version|Architecture Refactoring|Technology Migration|Dependencies Update|Pattern Changes"}
<!-- Type of migration or evolution -->

${SOURCE_REFERENCE="branch|commit|tag"}
<!-- Source reference point (before state) -->

${TARGET_REFERENCE="branch|commit|tag"}
<!-- Target reference point (after state) -->

${ANALYSIS_SCOPE="Entire project|Specific folder|Modified files only"}
<!-- Scope of analysis -->

${CHANGE_FOCUS="Breaking Changes|New Conventions|Obsolete Patterns|API Changes|Configuration"}
<!-- Main aspect of changes -->

${AUTOMATION_LEVEL="Conservative|Balanced|Aggressive"}
<!-- Level of automation for Copilot suggestions -->

${GENERATE_EXAMPLES="true|false"}
<!-- Include transformation examples -->

${VALIDATION_REQUIRED="true|false"}
<!-- Require validation before application -->
```

## Generated Prompt

> "Analyze code evolution between two project states to generate precise migration
> ### Phase 1: Comparative State Analysis

> **Full content:** `templates/generate-custom-instructions-from-codebase/generated_prompt.md`

## Migration Context
- **Type**: ${MIGRATION_TYPE}
- **From**: ${SOURCE_REFERENCE}
- **To**: ${TARGET_REFERENCE}
- **Date**: [GENERATION_DATE]
- **Scope**: ${ANALYSIS_SCOPE}

## Automatic Transformation Rules

> ### 1. Mandatory Transformations
> ${AUTOMATION_LEVEL != "Conservative" ?

> **Full content:** `templates/generate-custom-instructions-from-codebase/automatic_transformation_rules.md`

## File Type Specific Instructions

${GENERATE_EXAMPLES == "true" ?
  "### Configuration Files
   [CONFIG_TRANSFORMATION_EXAMPLES]

   ### Main Source Files
   [SOURCE_TRANSFORMATION_EXAMPLES]

   ### Test Files
   [TEST_TRANSFORMATION_EXAMPLES]" : ""}

## Validation and Security

### Automatic Control Points
- Verifications to perform after each transformation
- Tests to run to validate changes
- Performance metrics to monitor
- Compatibility checks to perform

### Manual Escalation
Situations requiring human intervention:
- [COMPLEX_CASES_LIST]
- [ARCHITECTURAL_DECISIONS]
- [BUSINESS_IMPACTS]

## Migration Monitoring

> - Percentage of code automatically migrated
> - Number of manual validations required

> **Full content:** `templates/generate-custom-instructions-from-codebase/migration_monitoring.md`

## Typical Use Cases

### Framework Version Migration

Perfect for documenting the transition from Angular 14 to Angular 17, React Class Components to Hooks, or .NET Framework to .NET Core. Automatically identifies breaking changes and generates corresponding transformation rules.

### Technology Stack Evolution

Essential when replacing a technology entirely: jQuery to React, REST to GraphQL, SQL to NoSQL. Creates a comprehensive migration guide with pattern mappings.

### Architecture Refactoring

Ideal for large refactorings like Monolith to Microservices, MVC to Clean Architecture, or Component to Composable architecture. Preserves architectural knowledge for future similar transformations.

### Design Pattern Modernization

Useful for adopting new patterns: Repository Pattern, Dependency Injection, Observer to Reactive Programming. Documents the rationale and implementation differences.

## Unique Benefits

### 🧠 **Artificial Intelligence Enhancement**

Unlike traditional migration documentation, these instructions "train" GitHub Copilot to reproduce your technology evolution decisions automatically during future code modifications.

### 🔄 **Knowledge Capitalization**

Transforms specific project experience into reusable rules, avoiding the loss of migration expertise and accelerating future similar transformations.

### 🎯 **Context-Aware Precision**

Instead of generic advice, generates instructions tailored to your specific codebase, with real before/after examples from your project evolution.

### ⚡ **Automated Consistency**

Ensures that new code additions automatically follow the new conventions, preventing architectural regression and maintaining code evolution coherence.


## Template References

Detailed templates in `templates/generate-custom-instructions-from-codebase/`:
- `automatic_transformation_rules.md`
- `generated_prompt.md`
- `migration_monitoring.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
