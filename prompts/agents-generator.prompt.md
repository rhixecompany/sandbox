---
license: MIT
author: Hermes Agent
version: 1.0.0
title: Agents Generator
name: agents-generator
description: "Technology-agnostic blueprint generator for creating comprehensive AGENTS.md files that guide GitHub Copilot to produce code consistent with project standards, architecture patterns, and exact technology versions by analyzing existing codebase patterns and avoiding assumptions."
tags:
  - agents
  - ai-assistant
  - architecture
  - data
  - debugging
  - frontend
  - generator
  - git
  - ml
  - prompts
  - specification
  - testing
  - typescript
  - workflow
  - agents
  - ai-assistant
  - architecture
  - ci-cd
  - debugging
  - documentation
  - github
  - linux
  - markdown
  - orchestration
  - planning
  - specification
  - workflow
metadata:
  hermes:
    related_skills: []
    tags:
    - agents-generator.prompt

trigger: agents-generator

---
metadata:
  hermes:
    related_skills: []
    tags:
    - agents-generator.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - agents-generator.prompt

Analyze this codebase to generate or update `AGENTS.md` for guiding AI coding agents.

Focus on discovering the essential knowledge that would help an AI agents be immediately productive in this codebase. Consider aspects like:

- The `big picture` architecture that requires reading multiple files to understand - major components, service boundaries, data flows, and the `why` behind structural decisions
- Critical developer workflows (builds, tests, debugging) especially commands that aren't obvious from file inspection alone
- Project-specific conventions and patterns that differ from common practices
- Integration points, external dependencies, and cross-component communication patterns
- Always use powershell commands and pnpm

Source existing AI conventions from `**/{.github/copilot-instructions.md,AGENT.md,AGENTS.md,CLAUDE.md,.cursorrules,.windsurfrules,.clinerules,.cursor/rules/**,.windsurf/rules/**,.clinerules/**,README.md}` (do one glob search).

Guidelines (read more at https://aka.ms/vscode-instructions-docs):

- If `AGENTS.md` exists, merge intelligently - preserve valuable content while updating outdated sections
- Write concise, actionable instructions (~500-1000 lines) using markdown structure
- Include specific examples from the codebase when describing patterns
- Avoid generic advice (`write tests`, `handle errors`) - focus on THIS project's specific approaches
- Document only discoverable patterns, not aspirational practices
- Reference key files/directories that exemplify important patterns
- when you are debugging a single file always execute pnpm lint `<file>` instead of the entire project.
- always read the documentation and comments before making changes.
- always check `src/scripts/*.ts`, `./*.ps1`, `./*.sh`, package.json for helpful scripts.
- always follow the coding standards and best practices outlined in the project's documentation.

Update `AGENTS.md` for the user, then ask for feedback on any unclear or incomplete sections to iterate.

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
