---
toolsets: []
license: MIT
author: Hermes Agent
version: 1.0.0
title: React Development Guidelines
name: github-copilot-starter
  - edit
  - githubRepo
  - changes
  - problems
  - search
  - runCommands
  - web/fetch
description: "Set up complete GitHub Copilot configuration for a new project based on technology stack"
tags:
  - ai-assistant
  - configuration
  - frontend
  - git
  - ml
  - prompts
  - react
  - specification
  - typescript
  - ai-assistant
  - ci-cd
  - documentation
  - github
  - linux
  - planning
  - react
  - specification
metadata:
  hermes:
    related_skills: []
    tags:
    - github-copilot-starter.prompt

trigger: github-copilot-starter

---
metadata:
  hermes:
    related_skills: []
    tags:
    - github-copilot-starter.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - github-copilot-starter.prompt

## Goal

Set up complete GitHub Copilot configuration for a new project based on technology stack.

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

## Project Information Required

Ask the user for the following information if not provided:

1. **Primary Language/Framework**: (e.g., JavaScript/React, Python/Django, Java/Spring Boot, etc.)
2. **Project Type**: (e.g., web app, API, mobile app, desktop app, library, etc.)
3. **Additional Technologies**: (e.g., database, cloud provider, testing frameworks, etc.)
4. **Team Size**: (solo, small team, enterprise)
5. **Development Style**: (strict standards, flexible, specific patterns)

## Configuration Files to Create

> Based on the provided stack, create the following files in the appropriate direc
> ### 1. `.github/copilot-instructions.md`

> **Full content:** `templates/github-copilot-starter/configuration_files_to_create.md`

## Content Guidelines

For each file, follow these principles:

**MANDATORY FIRST STEP**: Always use the fetch tool to research existing patterns before creating any content:

1. **Fetch from awesome-copilot collections**: https://github.com/github/awesome-copilot/blob/main/docs/README.collections.md
2. **Fetch specific instruction files**: https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/[relevant-file].instructions.md
3. **Check for existing patterns** that match the technology stack

**Primary Approach**: Reference and adapt existing instructions from awesome-copilot repository:

- **Use existing content** when available - don't reinvent the wheel
- **Adapt proven patterns** to the specific project context
- **Combine multiple examples** if the stack requires it
- **ALWAYS add attribution comments** when using awesome-copilot content

**Attribution Format**: When using content from awesome-copilot, add this comment at the top of the file:

```markdown
<!-- Based on/Inspired by: https://github.com/github/awesome-copilot/blob/main/instructions/[filename].instructions.md -->
```

**Examples:**

```markdown
## <!-- Based on: https://github.com/github/awesome-copilot/blob/main/instructions/react.instructions.md -->

applyTo: "**/\*.jsx,**/\*.tsx" description: "React development best practices"

---

# React Development Guidelines

...
```

```markdown
<!-- Inspired by: https://github.com/github/awesome-copilot/blob/main/instructions/java.instructions.md -->

## <!-- and: https://github.com/github/awesome-copilot/blob/main/instructions/spring-boot.instructions.md -->

> applyTo: "\*_/_.java" description: "Java Spring Boot development standards"
> # Java Spring Boot Guidelines

> **Full content:** `templates/github-copilot-starter/--_and_httpsgithubcomgithubawe.md`

## File Structure Standards

Ensure all files follow these conventions:

```
project-root/
├── .github/
│   ├── copilot-instructions.md
│   ├── instructions/
│   │   ├── [language].instructions.md
│   │   ├── testing.instructions.md
│   │   ├── documentation.instructions.md
│   │   ├── security.instructions.md
│   │   ├── performance.instructions.md
│   │   └── code-review.instructions.md
│   ├── prompts/
│   │   ├── setup-component.prompt.md
│   │   ├── write-tests.prompt.md
│   │   ├── code-review.prompt.md
│   │   ├── refactor-code.prompt.md
│   │   ├── generate-docs.prompt.md
│   │   └── debug-issue.prompt.md
│   ├── agents/
│   │   ├── architect.agent.md
│   │   ├── reviewer.agent.md
│   │   └── debugger.agent.md
│   └── workflows/
│       └── copilot-setup-steps.yml
```

## YAML Frontmatter Template

Use this frontmatter structure for all files:

**Instructions (.instructions.md):**

```yaml
---
applyTo: "**/*.ts,**/*.tsx"
---
# Project coding standards for TypeScript and React

Apply the [general coding guidelines](./general-coding.instructions.md) to all code.

## TypeScript Guidelines
- Use TypeScript for all new code
- Follow functional programming principles where possible
- Use interfaces for data structures and type definitions
- Prefer immutable data (const, readonly)
- Use optional chaining (?.) and nullish coalescing (??) operators

## React Guidelines

> - Use functional components with hooks
> - Follow the React hooks rules (no conditional hooks)

> **Full content:** `templates/github-copilot-starter/react_guidelines.md`

## Execution Steps

1. **Analyze the provided technology stack**
2. **Create the directory structure**
3. **Generate main copilot-instructions.md with project-wide standards**
4. **Create language-specific instruction files using awesome-copilot references**
5. **Generate reusable prompts for common development tasks**
6. **Set up specialized chat modes for different development scenarios**
7. **Create the GitHub Actions workflow for Coding Agent** (`copilot-setup-steps.yml`)
8. **Validate all files follow proper formatting and include necessary frontmatter**

## Post-Setup Instructions

After creating all files, provide the user with:

1. **VS Code setup instructions** - How to enable and configure the files
2. **Usage examples** - How to use each prompt and chat mode
3. **Customization tips** - How to modify files for their specific needs
4. **Testing recommendations** - How to verify the setup works correctly

## Quality Checklist

Before completing, verify:

- [ ] All files have proper YAML frontmatter
- [ ] Language-specific best practices are included
- [ ] Files reference each other appropriately using Markdown links
- [ ] Prompts include relevant tools and variables
- [ ] Instructions are comprehensive but not overwhelming
- [ ] Security and performance considerations are addressed
- [ ] Testing guidelines are included
- [ ] Documentation standards are clear
- [ ] Code review standards are defined

## Workflow Template Structure

> The `copilot-setup-steps.yml` workflow MUST follow this exact format and KEEP IT
> name: "Copilot Setup Steps"

> **Full content:** `templates/github-copilot-starter/workflow_template_structure.md`

## Template References

Detailed templates in `templates/github-copilot-starter/`:
- `--_and_httpsgithubcomgithubawe.md`
- `configuration_files_to_create.md`
- `react_guidelines.md`
- `workflow_template_structure.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
