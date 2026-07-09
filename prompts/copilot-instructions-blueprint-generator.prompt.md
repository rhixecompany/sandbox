---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Copilot Instructions Blueprint Generator
name: copilot-instructions-blueprint-generator
description: "Technology-agnostic blueprint generator for creating comprehensive copilot-instructions.md files that guide GitHub Copilot to produce code consistent with project standards, architecture patterns, and exact technology versions by analyzing existing codebase patterns and avoiding assumptions."
tags:
  - ai-assistant
  - architecture
  - frontend
  - generator
  - git
  - prompts
  - specification
  - typescript
  - ai-assistant
  - architecture
  - ci-cd
  - documentation
  - github
  - linux
  - markdown
  - planning
  - specification
---

## Goal

Technology-agnostic blueprint generator for creating comprehensive copilot-instructions.md files that guide GitHub Copilot to produce code consistent with project standards, architecture patterns, and exact technology versions by analyzing existing codebase patterns and avoiding assumptions.

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

${PROJECT_TYPE="Auto-detect|.NET|Java|JavaScript|TypeScript|React|Angular|Python|Multiple|Other"} <!-- Primary technology -->
${ARCHITECTURE_STYLE="Layered|Microservices|Monolithic|Domain-Driven|Event-Driven|Serverless|Mixed"} <!-- Architectural approach --> ${CODE_QUALITY_FOCUS="Maintainability|Performance|Security|Accessibility|Testability|All"} <!-- Quality priorities -->
${DOCUMENTATION_LEVEL="Minimal|Standard|Comprehensive"} <!-- Documentation requirements --> ${TESTING_REQUIREMENTS="Unit|Integration|E2E|TDD|BDD|All"} <!-- Testing approach -->
${VERSIONING="Semantic|CalVer|Custom"} <!-- Versioning approach -->

## Generated Prompt

"Generate a comprehensive copilot-instructions.md file that will guide GitHub Copilot to produce code consistent with our project's standards, architecture, and technology versions. The instructions must be strictly based on actual code patterns in our codebase and avoid making any assumptions. Follow this approach:

### 1. Core Instruction Structure

```markdown
# GitHub Copilot Instructions

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our ${ARCHITECTURE_STYLE} architectural style and established boundaries
5. **Code Quality**: Prioritize ${CODE_QUALITY_FOCUS == "All" ? "maintainability, performance, security, accessibility, and testability" : CODE_QUALITY_FOCUS} in all generated code

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - Examine project files, configuration files, and package managers
   - Look for language-specific version indicators (e.g., <LangVersion> in .NET projects)
   - Never use language features beyond the detected version

2. **Framework Versions**: Identify the exact versions of all frameworks
   - Check package.json, .csproj, pom.xml, requirements.txt, etc.
   - Respect version constraints when generating code
   - Never suggest features not available in the detected framework versions

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - Generate code compatible with these specific versions
   - Never use APIs or features not available in the detected versions

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines
- **tech-stack.md**: Technology versions and framework details
- **coding-standards.md**: Code style and formatting standards
- **folder-structure.md**: Project organization guidelines
- **exemplars.md**: Exemplary code patterns to follow

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar files to the one being modified or created
2. Analyze patterns for:
   - Naming conventions
   - Code organization
   - Error handling
   - Logging approaches
   - Documentation style
   - Testing patterns
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files or files with higher test coverage
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

> ${CODE_QUALITY_FOCUS.includes("Maintainability") || CODE_QUALITY_FOCUS == "All" 
> - Write self-documenting code with clear naming

> **Full content:** `templates/copilot-instructions-blueprint-generator/code_quality_standards.md`

## Documentation Requirements

${DOCUMENTATION_LEVEL == "Minimal" ? `- Match the level and style of comments found in existing code

- Document according to patterns observed in the codebase
- Follow existing patterns for documenting non-obvious behavior
- Use the same format for parameter descriptions as existing code` : ""}

${DOCUMENTATION_LEVEL == "Standard" ? `- Follow the exact documentation format found in the codebase

- Match the XML/JSDoc style and completeness of existing comments
- Document parameters, returns, and exceptions in the same style
- Follow existing patterns for usage examples
- Match class-level documentation style and content` : ""}

${DOCUMENTATION_LEVEL == "Comprehensive" ? `- Follow the most detailed documentation patterns found in the codebase

- Match the style and completeness of the best-documented code
- Document exactly as the most thoroughly documented files do
- Follow existing patterns for linking documentation
- Match the level of detail in explanations of design decisions` : ""}

## Testing Approach

> ${TESTING_REQUIREMENTS.includes("Unit") || TESTING_REQUIREMENTS == "All" ? `### 
> - Match the exact structure and style of existing unit tests

> **Full content:** `templates/copilot-instructions-blueprint-generator/testing_approach.md`

## Technology-Specific Guidelines

> ${PROJECT_TYPE == ".NET" || PROJECT_TYPE == "Auto-detect" || PROJECT_TYPE == "Mu
> - Detect and strictly adhere to the specific .NET version in use

> **Full content:** `templates/copilot-instructions-blueprint-generator/technology-specific_guidelines.md`

## Version Control Guidelines

${VERSIONING == "Semantic" ? `- Follow Semantic Versioning patterns as applied in the codebase

- Match existing patterns for documenting breaking changes
- Follow the same approach for deprecation notices` : ""}

${VERSIONING == "CalVer" ? `- Follow Calendar Versioning patterns as applied in the codebase

- Match existing patterns for documenting changes
- Follow the same approach for highlighting significant changes` : ""}

${VERSIONING == "Custom" ? `- Match the exact versioning pattern observed in the codebase

- Follow the same changelog format used in existing documentation
- Apply the same tagging conventions used in the project` : ""}

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Follow the same approach to testing as seen in the codebase
- Match logging patterns from existing code
- Use the same approach to configuration as seen in the codebase

## Project-Specific Guidance

> - Scan the codebase thoroughly before generating any code
> - Respect existing architectural boundaries without exception

> **Full content:** `templates/copilot-instructions-blueprint-generator/project-specific_guidance.md`

## Expected Output

A comprehensive copilot-instructions.md file that will guide GitHub Copilot to produce code that is perfectly compatible with your existing technology versions and follows your established patterns and architecture.


## Template References

Detailed templates in `templates/copilot-instructions-blueprint-generator/`:
- `code_quality_standards.md`
- `project-specific_guidance.md`
- `technology-specific_guidelines.md`
- `testing_approach.md`
