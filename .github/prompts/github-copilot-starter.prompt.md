---

name: github-copilot-starter

title: React Development Guidelines

description: Set up complete GitHub Copilot configuration for a new project based on technology stack.

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - file

  - terminal

  - web

scripts: []

skills: []

formatter: default

plan: None

dependencies: []

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

trigger: /github-copilot-starter

metadata:

  hermes: {}

---

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

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

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

Ask the user for the following information if not provided:1. **Primary Language/Framework**: (e.g., JavaScript/React, Python/Django, Java/Spring Boot, etc.)2. **Project Type**: (e.g., web app, API, mobile app, desktop app, library, etc.)3. **Additional Technologies**: (e.g., database, cloud provider, testing frameworks, etc.)4. **Team Size**: (solo, small team, enterprise)5. **Development Style**: (strict standards, flexible, specific patterns)

## Configuration Files to Create

> Based on the provided stack, create the following files in the appropriate direc>>

### 1. `.github/copilot-instructions.md`

> **Full content:**

## Content Guidelines

For each file, follow these principles:**MANDATORY FIRST STEP**: Always use the fetch tool to research existing patterns before creating any content:1. **Fetch from awesome-copilot collections**: <<https://github.com/github/awesome-copilot/blob/main/docs/README.collections.md>

> 1. **Fetch specific instruction files**: <https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/[relevant-file].instructions.md>3. **Check for existing patterns** that match the technology stack**Primary Approach**: Reference and adapt existing instructions from awesome-copilot repository:- **Use existing content** when available - don't reinvent the wheel- **Adapt proven patterns** to the specific project context- **Combine multiple examples** if the stack requires it- **ALWAYS add attribution comments** when using awesome-copilot content**Attribution Format**: When using content from awesome-copilot, add this comment at the top of the file:```markdown<!-- Based on/Inspired by: https://github.com/github/awesome-copilot/blob/main/instructions/[filename].instructions.md -->```**Examples:**```markdown

## <!-

- Based on: <https://github.com/github/awesome-copilot/blob/main/instructions/react.instructions.md> --

> applyTo: "**/\*.jsx,**/\*.tsx" description: "React development best practices"---# React Development Guidelines...``````markdown<!-- Inspired by: https://github.com/github/awesome-copilot/blob/main/instructions/java.instructions.md -->

## <!-

- and: <https://github.com/github/awesome-copilot/blob/main/instructions/spring-boot.instructions.md> --

>
> applyTo: "\*_/_.java" description: "Java Spring Boot development standards"
>
> # Java Spring Boot Guidelines
>
> **Full content:**

## File Structure StandardsEnsure all files follow these conventions:```project-root/├── .github/│   ├── copilot-instructions.md│   ├── instructions/│   │   ├── [language].instructions.md│   │   ├── testing.instructions.md│   │   ├── documentation.instructions.md│   │   ├── security.instructions.md│   │   ├── performance.instructions.md│   │   └── code-review.instructions.md│   ├── prompts/│   │   ├── setup-component.prompt.md│   │   ├── write-tests.prompt.md│   │   ├── code-review.prompt.md│   │   ├── refactor-code.prompt.md│   │   ├── generate-docs.prompt.md│   │   └── debug-issue.prompt.md│   ├── agents/│   │   ├── architect.agent.md│   │   ├── reviewer.agent.md│   │   └── debugger.agent.md│   └── workflows/│       └── copilot-setup-steps.yml```

## YAML Frontmatter TemplateUse this frontmatter structure for all files:**Instructions (.instructions.md):**```yaml---applyTo: "**/*.ts,**/*.tsx"---# Project coding standards for TypeScript and ReactApply the [general coding guidelines](./general-coding.instructions.md) to all code.

## TypeScript Guidelines

- Use TypeScript for all new code- Follow functional programming principles where possible- Use interfaces for data structures and type definitions- Prefer immutable data (const, readonly)- Use optional chaining (?.) and nullish coalescing (??) operators

## React Guidelines

> - Use functional components with hooks
> - Follow the React hooks rules (no conditional hooks)
> **Full content:**

## Execution Steps

1. **Analyze the provided technology stack**2. **Create the directory structure**3. **Generate main copilot-instructions.md with project-wide standards**4. **Create language-specific instruction files using awesome-copilot references**5. **Generate reusable prompts for common development tasks**6. **Set up specialized chat modes for different development scenarios**7. **Create the GitHub Actions workflow for Coding Agent** (`copilot-setup-steps.yml`)8. **Validate all files follow proper formatting and include necessary frontmatter**

## Post-Setup Instructions

After creating all files, provide the user with:1. **VS Code setup instructions** - How to enable and configure the files2. **Usage examples** - How to use each prompt and chat mode3. **Customization tips** - How to modify files for their specific needs4. **Testing recommendations** - How to verify the setup works correctly

## Quality Checklist

Before completing, verify:

- [ ] All files have proper YAML frontmatter- [ ] Language-specific best practices are included- [ ] Files reference each other appropriately using Markdown links- [ ] Prompts include relevant tools and variables- [ ] Instructions are comprehensive but not overwhelming- [ ] Security and performance considerations are addressed- [ ] Testing guidelines are included- [ ] Documentation standards are clear- [ ] Code review standards are defined

## Workflow Template Structure

> The `copilot-setup-steps.yml` workflow MUST follow this exact format and KEEP IT
> name: "Copilot Setup Steps"
> **Full content:**

## Template References

Detailed templates in `templates/github-copilot-starter/`:- `--_and_httpsgithubcomgithubawe.md`- `configuration_files_to_create.md`- `react_guidelines.md`- `workflow_template_structure.md`

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

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
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
