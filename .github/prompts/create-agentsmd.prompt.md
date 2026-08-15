---
name: create-agentsmd
title: create agentsmd
description: Prompt for create-agentsmd
version: "1.0.0"
tags: [agents, automation, documentation, generation, tool]
trigger: create-agentsmd
metadata:
  hermes:
    profile: default
    priority: medium
    categories: []
  copilot:
    model_required: claude-opus
    context_length: medium
  opencode:
    enabled: true
    compatibility: compatible
  codex:
    enabled: false
    model_preferred: text-davinci-003

---
name: create-agentsmd
title: Create high‑quality AGENTS.md file
description: Prompt for generating an AGENTS.md file for a repository.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
- file
- terminal
scripts: []
skills: []
formatter: default
plan: null
tags:
- agents
- generator
- ml
- prompts
- specification
- typescript
- agents
- generator
- ml
- prompts
- specification
- typescript
trigger: /create-agentsmd
dependencies: []
metadata:
  hermes: {}
---

## Goal

Prompt for generating an AGENTS.md file for a repository.

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

## What is AGENTS.md?AGENTS.md is a Markdown file that serves as a "README for agents"

- a dedicated, predictable place to provide context and instructions to help AI coding agents work on your project. It complements README.md by containing detailed technical context that coding agents need but might clutter a human-focused README.

## Key Principles

- **Agent-focused**: Contains detailed technical instructions for automated tools- **Complements README.md**: Doesn't replace human documentation but adds agent-specific context- **Standardized location**: Placed at repository root (or subproject roots for monorepos)- **Open format**: Uses standard Markdown with flexible structure- **Ecosystem compatibility**: Works across 20+ different AI coding tools and agents

## File Structure and Content Guidelines

### 1. Required Setup

>
> - Create the file as `AGENTS.md` in the repository root
> **Full content:**

## Example Template

Use this as a starting template and customize based on the specific project:

```markdown
# AGENTS.md

## Project Overview
[Brief description of the project, its purpose, and key technologies]

## Setup Commands

- Install dependencies: `[package manager] install`- Start development server: `[command]`- Build for production: `[command]`

## Development Workflow

- [Development server startup instructions]- [Hot reload/watch mode information]- [Environment variable setup]

## Test

ing Instructions- Run all tests: `[command]`- Run unit tests: `[command]`- Run integration tests: `[command]`- Test coverage: `[command]`- [Specific testing patterns or requirements]

## Code Style

- [Language and framework conventions]- [Linting rules and commands]- [Formatting requirements]- [File organization patterns]

## Build and Deployment

- [Build process details]- [Output directories]- [Environment-specific builds]- [Deployment commands]

## Pull Request Guidelines

- Title format: [component] Brief description- Required checks: `[lint command]`, `[test command]`

- [Review requirements]

## Additional Notes

- [Any project-specific context]- [Common gotchas or troubleshooting tips]- [Performance considerations]
```

## Working Example from agents.md

Here's a real example from the agents.md website:

```markdown
# Sample AGENTS.md file

## Dev environment tips

- Use `pnpm dlx turbo run where <project_name

> ` to jump to a package instead of scanning with `ls`.- Run`pnpm install --filter <project_name>` to add the package to your workspace so Vite, ESLint, and TypeScript can see it.

- Use `pnpm create vite@latest <project_name

> -- --template react-ts` to spin up a new React + Vite package with TypeScript checks ready.

- Check the name field inside each package's package.json to confirm the right name—skip the top-level one.

## Test

ing instructions- Find the CI plan in the .github/workflows folder.

- Run `pnpm turbo run test --filter <project_name>` to run every check defined for that package.
- From the package root you can just call `pnpm test`. The commit should pass all tests before you merge.
- To focus on one step, add the Vitest pattern: `pnpm vitest run -t "<test name>"`.- Fix any test or type errors until the whole suite is green.
- After moving files or changing imports, run `pnpm lint --filter <project_name>` to be sure ESLint and TypeScript rules still pass.
- Add or update tests for the code you change, even if nobody asked.

## PR instructions

- Title format: [<project_name

> ] <Title>- Always run `pnpm lint` and `pnpm test` before committing.
```

## Implementation Steps

1. **Analyze the project structure** to understand:

- Programming languages and frameworks used   - Package managers and build tools   - Testing frameworks   - Project architecture (monorepo, single package, etc.)2. **Identify key workflows** by examining:   - package.json scripts   - Makefile or other build files   - CI/CD configuration files   - Documentation files3. **Create comprehensive sections** covering:   - All essential setup and development commands   - Testing strategies and commands   - Code style and conventions   - Build and deployment processes4. **Include specific, actionable commands** that agents can execute directly5. **Test the instructions** by ensuring all commands work as documented6. **Keep it focused** on what agents need to know, not general project information

## Best Practices

- **Be specific**: Include exact commands, not vague descriptions
- **Use code blocks**: Wrap commands in backticks for clarity
- **Include context**: Explain why certain steps are needed
- **Stay current**: Update as the project evolves
- **Test commands**: Ensure all listed commands actually work
- **Consider nested files**: For monorepos, create AGENTS.md files in subprojects as needed

## Monorepo Considerations

For large monorepos:

- Place a main AGENTS.md at the repository root- Create additional AGENTS.md files in subproject directories- The closest AGENTS.md file takes precedence for any given location- Include navigation tips between packages/projects

## Final Notes

- AGENTS.md works with 20+ AI coding tools including Cursor, Aider, Gemini CLI, and many others- The format is intentionally flexible - adapt it to your project's needs- Focus on actionable instructions that help agents understand and work with your codebase- This is living documentation - update it as your project evolvesWhen creating the AGENTS.md file, prioritize clarity, completeness, and actionability. The goal is to give any coding agent enough context to effectively contribute to the project without requiring additional human guidance.~~~

## Template References

Detailed templates in `templates/create-agentsmd/`:- `file_structure_and_content_gui.md`

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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.


## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section


## Related Prompts

Same-family prompts:

- [`create-architectural-decision-record.prompt.md`](create-architectural-decision-record.prompt.md)
- [`create-github-action-workflow-specification.prompt.md`](create-github-action-workflow-specification.prompt.md)
- [`create-github-issue-feature-from-specification.prompt.md`](create-github-issue-feature-from-specification.prompt.md)
- [`create-github-issues-feature-from-implementation-plan.prompt.md`](create-github-issues-feature-from-implementation-plan.prompt.md)
- [`create-github-issues-for-unmet-specification-requirements.prompt.md`](create-github-issues-for-unmet-specification-requirements.prompt.md)
- [`create-github-pull-request-from-specification.prompt.md`](create-github-pull-request-from-specification.prompt.md)
- [`create-implementation-plan.prompt.md`](create-implementation-plan.prompt.md)
- [`create-llms.prompt.md`](create-llms.prompt.md)
- [`create-oo-component-documentation.prompt.md`](create-oo-component-documentation.prompt.md)
- [`create-readme.prompt.md`](create-readme.prompt.md)
- [`create-specification.prompt.md`](create-specification.prompt.md)
- [`create-spring-boot-java-project.prompt.md`](create-spring-boot-java-project.prompt.md)
- [`create-spring-boot-kotlin-project.prompt.md`](create-spring-boot-kotlin-project.prompt.md)
- [`create-technical-spike.prompt.md`](create-technical-spike.prompt.md)
- [`create-tldr-page.prompt.md`](create-tldr-page.prompt.md)

