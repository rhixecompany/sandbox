---
toolsets:
  - vscode
  - execute
  - read
  - agent
  - edit
  - search
  - web
  - github/*
  - browser
  - vscode.mermaid-chat-features/renderMermaidDiagram
  - github.vscode-pull-request-github/issue_fetch
  - github.vscode-pull-request-github/labels_fetch
  - github.vscode-pull-request-github/notification_fetch
  - github.vscode-pull-request-github/doSearch
  - github.vscode-pull-request-github/activePullRequest
  - github.vscode-pull-request-github/pullRequestStatusChecks
  - github.vscode-pull-request-github/openPullRequest
  - todo
license: MIT
author: Hermes Agent
version: 1.0.0
title: Refactor Mardown Files
name: refactor-mardown-files
description: "Refactor and update Banking documentation files (`AGENTS.md` and `.github/copilot-instructions.md`) to maximize clarity, actionability, and AI agent productivity, following project conventions and Diátaxis principles."
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
  - agents
  - ai-assistant
  - ci-cd
  - documentation
  - github
  - markdown
  - nextjs
  - planning
  - refactoring
  - specification
  - typescript
metadata:
  hermes:
    related_skills: []
    tags:
    - refactor-mardown-files.prompt

trigger: refactor-mardown-files

---
metadata:
  hermes:
    related_skills: []
    tags:
    - refactor-mardown-files.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - refactor-mardown-files.prompt

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

## 1. Task Specification

Analyze, refactor, and update the `AGENTS.md`,`.cursorrules` and `.github/copilot-instructions.md` files in the Banking repository. Ensure all instructions are clear, actionable, and aligned with current project conventions, Diátaxis documentation principles, and markdown best practices. Remove outdated or redundant content, and structure the documentation for maximum utility by both humans and AI agents.

## 2. Context & Variable Requirements

- Project: Banking (Next.js 16, TypeScript, Drizzle ORM, PostgreSQL, NextAuth, shadcn/UI, Tailwind CSS v4)
- Documentation files: `AGENTS.md`,`.cursorrules`, `.github/copilot-instructions.md`,`docs/*.md`,`*.md`
- Reference files: `README.md`, blueprints, `.github/instructions/documentation.instructions.md`, and other instruction files
- All referenced commands, file paths, and code samples must exist and be up-to-date
- Diátaxis documentation structure and Banking-specific standards must be followed

## 3. Detailed Instructions & Standards

> 1. **Analyze the Target Documentation:**
> - Read the full content of `AGENTS.md`,`.cursorrules` and `.github/copilot-instr

> **Full content:** `templates/refactor-mardown-files/3_detailed_instructions__stand.md`

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
- Markdown linting and formatting tools (e.g., `markdownlint`).
- Codebase search tools to resolve file paths, section headings, and code samples.
- Date and metadata insertion for “Last Updated” sections.
- Diátaxis and documentation skills, referencing `.github/instructions/documentation.instructions.md`.
- AI agent capabilities for chunked processing, persona-driven prompting, and anti-rate-limiting.
- Optional: Use “documentation-writer” and “refactor” skills if available.

## 6. Technical Configuration

- Use GPT-4.1 or higher.
- Operate in “Documentation Refactorer” persona with Diátaxis expertise.
- Chunk large files for processing; checkpoint after each section.
- Back up original files before overwriting.
- Run `markdownlint`, `npm run validate` for validation.
- Load and apply `.github/instructions/documentation.instructions.md` and other relevant instructions.
- Output must be valid markdown, ready for direct commit.

## 7. Quality & Validation Criteria

- All instructions must be clear, concise, and actionable.
- All references must be accurate and up-to-date.
- Output must pass markdown linting and render correctly.
- All required sections must be present and fully populated.
- Run `npm run validate` to ensure no regressions.
- Adhere to Banking documentation standards and Diátaxis principles.
- Include “Last Updated” and, if needed, “Migration Notes” sections.
- Output must be peer-reviewed and approved before commit.


## Template References

Detailed templates in `templates/refactor-mardown-files/`:
- `3_detailed_instructions__stand.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
