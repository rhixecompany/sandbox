---
name: Initial
title: ComicWise Project Initialization
description: Complete project setup guide for ComicWise — Next.js 16 application with pnpm, covering installation, configuration, and development workflow.
version: 1.0.0
author: Hermes Agent
date: '2026-08-25'
tags:
  - setup
  - nextjs
  - comicwise
  - pnpm
  - onboarding
  - documentation
  - frontend
  - configuration
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
---


# Table of Contents

- [Goal](#goal)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
  - [Domain Rules](#domain-rules)
  - [Standing Rules](#standing-rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand Off](#phase-4:-hand-off)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)


## Table of Contents

- [Goal](#goal)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
- [Domain Rules](#domain-rules)
- [Standing Rules](#standing-rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand Off](#phase-4:-hand-off)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)




## Goal

Complete project setup guide for ComicWise — Next.js 16 application with pnpm, covering installation, configuration, and development workflow.

Read And understand @/**/*.ts, @/**/*.tsx, @/**/*.mjs, @/**/*.json , @/**/*.mts, @/**/*.json @/**/*.md, @/**/*.txt, @/**/*.yml, @/**/*.ps1, @/**/*.sh, @/**/*/Dockerfile, @/src, @scripts and the overall structure of the project.After fully understanding the project the package manager is pnpm and the system is windows, Request all permissions needed to complete all tasks.Confirm if I have the necessary permissions to complete all tasks.Complete all tasks the bests way.Tasks:1 - Create, Optimize and Validate all comprehensive configurations listed below if exists copy file to end with .backup and Create, Optimize and Validate an enhanced version of the following files:- @.vscode/mcp.json- @.vscode/extensions.json- @.vscode/launch.json- @.vscode/tasks.json- @.vscode/settings.json2 - Create, Optimize and Validate if exists copy file to end with .backup and Create, Optimize and Validate an enhanced version of @.env.local and @appConfig.ts file to ensure all environment variables are properly set and configured for development and production environments update all usage of this file across the project.3 - Create, Create, Optimize and Validate if exists copy file to end with .backup and Create, Optimize and Validate an enhanced version of @src/database/seed/**/*.ts to be dynamic allowing the creation of data from @users.json @chapters*.json @comics*.json, create and use all needed helpers at @src/database/seed/**/*.ts to ensure the inserted data is being created or updated if it exists and ensure all images are not redownloaded checking if they are already saved and downloaded with @src/services/imageService.ts and saved at @public/uploads use best practices if not saved download the images use do not repeat yourself practices and zod validation with all fields from @users.json @chapters*.json @comics*.json update all usages across the project reference @src/database/seed/seeders/universalSeeder.ts as example.After completing all the tasks above, perform the following additional tasks to further enhance the project:1 - Create, Optimize and Validate if exists copy file to end with .backup and Create, Optimize and Validate an enhanced version of all scripts at @/scripts to ensure they are efficient, well-documented, and follow best practices for maintainability and scalability update all usages across the project.2 - Create and Run once created and validated a script to Analyze the project for performance bottlenecks, security vulnerabilities, and code quality issues generate a report with findings and suggestions for improvements.3 - Create and Run once created and validated a script to Generate comprehensive documentation for the project including setup instructions, usage guidelines, and API references ensure the documentation is clear, concise, and easy to navigate.4 - Create and Run once created and validated a script to Set up automated testing for the project including unit tests, integration tests, and end-to-end tests ensure tests are well-structured and provide adequate coverage for critical components.5 - Create and Run once created and validated a scripts to Perform a cleanup of the project which prevent duplicates, deleting unused or duplecate files, functions, Delete all files that ends with .backup, Delete all unused Components,Scripts that are not being used.6 - Uninstall all unused packages from @package.json.7 - Create, Optimize and Validate a complete @.github/workflows/*.yml files for ci, automating the testing, building, and deployment of the project.8 - Create, Optimize and Validate a complete @prompts/Setup.prompt.md if exists update the file with all the content,tasks, todos, recommendations from @.md, @.txt, @.ts, @.tsx, @.mjs, @.json , @.mts, @.json @.yml @.ps1 @.sh @Dockerfile files as Github copilot cli Prompts for a complete setup of this project and scaffolding all necessary files, components, pages and codes setup handler for long running functions.9 - Create, Optimize and Validate a complete README.md for the project that includes setup instructions, usage guidelines, contribution instructions, and any other relevant information.10 - Fix all linting errors

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

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State when something fails.

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

- Return final artifact or findings .
- Stop once the requested result is delivered.

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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section