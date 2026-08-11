---
name: refactor-mardown-files
title: Refactor Mardown Files
description: 'Refactor and update Banking documentation files (`AGENTS.md` and `.github/copilot-instructions.md`) to maximize clarity, actionability, and AI agent productivity, following project conventions and Diátaxis principles.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - web
  - browser
  - todo
scripts: []
skills: []
formatter: default
plan: 'None'
dependencies: []
tags:
  - agents
  - ai-assistant
  - documentation
  - git
  - ml
  - nextjs
  - prompts
  - refactoring
  - specification
  - typescript
trigger: /refactor-mardown-files
metadata:
  hermes: {}
---

## Goal

Refactor and update Banking documentation files (`AGENTS.md` and `.github/copilot-instructions.md`) to maximize clarity, actionability, and AI agent productivity, following project conventions and Diátaxis principles.

## Context

Use when you need to next.js expert for the current workspace or task.

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

## 1. Task Specification

Analyze, refactor, and update the `AGENTS.md`,`.cursorrules` and `.github/copilot-instructions.md` files in the Banking repository. Ensure all instructions are clear, actionable, and aligned with current project conventions, Diátaxis documentation principles, and markdown best practices. Remove outdated or redundant content, and structure the documentation for maximum utility by both humans and AI agents.

## 2. Context & Variable Requirements

- Project: Banking (Next.js 16, TypeScript, Drizzle ORM, PostgreSQL, NextAuth, shadcn/UI, Tailwind CSS v4)- Documentation files: `AGENTS.md`,`.cursorrules`, `.github/copilot-instructions.md`,`docs/*.md`,`*.md`- Reference files: `README.md`, blueprints, `.github/instructions/documentation.instructions.md`, and other instruction files- All referenced commands, file paths, and code samples must exist and be up-to-date- Diátaxis documentation structure and Banking-specific standards must be followed

## 3. Detailed Instructions & Standards

> 1. **Analyze the Target Documentation:**>
>
> - Read the full content of `AGENTS.md`,`.cursorrules` and `.github/copilot-instr
> **Full content:**

## 4. Output Requirements

- Produce fully rewritten versions of `AGENTS.md`,`.cursorrules` and `.github/copilot-instructions.md`, ready for direct commit.
- Use clear, hierarchical headings, bullet points, callout blocks, and code blocks.
- All instructions must be actionable, concise, and unambiguous.
- Add a “Last Updated” section with the current date and summary of major changes.
- Output must pass markdown linting and render correctly in GitHub and VS Code preview.
- All code samples must be syntactically correct and match the current codebase.
- All links and references must resolve to real files or sections.
- Deliver three markdown files: `AGENTS.md`,`.cursorrules` and `.github/copilot-instructions.md`.

## 5. Tool & Capability Requirements

- File system access to read/write `AGENTS.md`, `.cursorrules`, `.github/copilot-instructions.md`, and reference files.
- Markdown linting and formatting tools (e.g., `markdownlint`).- Codebase search tools to resolve file paths, section headings, and code samples.
- Date and metadata insertion for “Last Updated” sections.
- Diátaxis and documentation skills, referencing `.github/instructions/documentation.instructions.md`.- AI agent capabilities for chunked processing, persona-driven prompting, and anti-rate-limiting.
- Optional: Use “documentation-writer” and “refactor” skills if available.

## 6. Technical Configuration

- Use GPT-4.1 or higher.
- Operate in “Documentation Refactorer” persona with Diátaxis expertise.
- Chunk large files for processing; checkpoint after each section.
- Back up original files before overwriting.
- Run `markdownlint`, `bun run validate` for validation.
- Load and apply `.github/instructions/documentation.instructions.md` and other relevant instructions.
- Output must be valid markdown, ready for direct commit.

## 7. Quality & Validation Criteria

- All instructions must be clear, concise, and actionable.
- All references must be accurate and up-to-date.
- Output must pass markdown linting and render correctly.
- All required sections must be present and fully populated.
- Run `bun run validate` to ensure no regressions.
- Adhere to Banking documentation standards and Diátaxis principles.
- Include “Last Updated” and, if needed, “Migration Notes” sections.
- Output must be peer-reviewed and approved before commit.

## Template References

Detailed templates in `templates/refactor-mardown-files/`:- `3_detailed_instructions__stand.md`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
|| ------- | ----------- ||
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
|| --- | ------ | ----------- ||
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
|| ------- | --------- ||
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
