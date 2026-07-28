---
name: readme-blueprint-generator
title: README Generator Prompt
description: 'Intelligent README.md generation prompt that analyzes project documentation structure and creates comprehensive repository documentation. Scans .github/copilot directory files and copilot-instructions.md to extract project information, technology stack, architecture, development workflow, coding standards, and testing approaches while generating well-structured markdown documentation with proper formatting, cross-references, and developer-focused content.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills: []
formatter: default
plan: None
tags:
  - ai-assistant
  - architecture
  - documentation
  - generator
  - git
  - linting
  - markdown
  - prompts
  - testing
  - workflow
trigger: /readme-blueprint-generator
dependencies: []
metadata:
  hermes: {}
---
## GoalIntelligent README.md generation prompt that analyzes project documentation structure and creates comprehensive repository documentation. Scans .github/copilot directory files and copilot-instructions.md to extract project information, technology stack, architecture, development workflow, coding standards, and testing approaches while generating well-structured markdown documentation with proper formatting, cross-references, and developer-focused content.

## ContextUse when you need to work on the current workspace or task.

## Inputs- The current workspace, repo, or document state.- The specific request, diff, spec, or files provided by the user.- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs- A complete result that matches the prompt's purpose.- A concise verification note when the task benefits from one.

## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)- Follow the prompt literally and prefer evidence from the current workspace.- Keep the response structured, deterministic, and easy to act on.- Avoid changing unrelated files or adding unnecessary scope.- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake- Read the request and identify the exact scope.- Locate the relevant files, diffs, or references.

### Phase 2: Execute- Perform the requested work with the smallest safe change set.- Keep the steps explicit and reproducible.

### Phase 3: Verify- Check the result against the goal, rules, and inputs.- Confirm the output is usable and complete.

### Phase 4: Hand off- Return the final artifact or findings clearly.- Stop once the requested result is delivered.

## Project Name and Description- Extract the project name and primary purpose from the documentation- Include a concise description of what the project does

## Technology Stack- List the primary technologies, languages, and frameworks used- Include version information when available- Source this information primarily from the Technology_Stack file

## Project Architecture- Provide a high-level overview of the architecture- Consider including a simple diagram if described in the documentation- Source from the Architecture file

## Getting Started- Include installation instructions based on the technology stack- Add setup and configuration steps- Include any prerequisites

## Project Structure- Brief overview of the folder organization- Source from Project_Folder_Structure file

## Key Features- List main functionality and features of the project- Extract from various documentation files

## Development Workflow- Summarize the development process- Include information about branching strategy if available- Source from Workflow_Analysis file

## Coding Standards- Summarize key coding standards and conventions- Source from the Coding_Standards file

## Testing- Explain testing approach and tools- Source from Unit_Tests file

## Contributing- Guidelines for contributing to the project- Reference any code exemplars for guidance- Source from Code_Exemplars and copilot-instructions

## License- Include license information if availableFormat the README with proper Markdown, including:- Clear headings and subheadings- Code blocks where appropriate- Lists for better readability- Links to other documentation files- Badges for build status, version, etc. if information is availableKeep the README concise yet informative, focusing on what new developers or users would need to know about the project.

## Template ReferencesTemplates in `templates/readme-blueprint-generator/`:- `legacy_prompt_details.md`- `phases.md`

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

Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.


## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Read existing code before writing new code.
- Match project conventions and style.
- Add tests for new functionality.

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
|---|------|-----------|
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |


## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Goal

Intelligent README.md generation prompt that analyzes project documentation structure and creates comprehensive repository documentation. Scans .github/copilot directory files and copilot-instructions.md to extract project information, technology stack, architecture, development workflow, coding standards, and testing approaches while generating well-structured markdown documentation with proper formatting, cross-references, and developer-focused content.


## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.


## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
|-------|---------|
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


