---
name: technology-stack-blueprint-generator
title: Technology Stack Blueprint Generator
description: Generate per-project technology stack documentation plus a workspace-level master blueprint covering languages, frameworks, runtimes, dependencies, conventions, and CI/CD.
trigger: /technology-stack-blueprint-generator
version: 1.0.0
author: Hermes Agent
tags:
  - documentation
  - architecture
  - blueprint
  - analysis
  - tooling
  - workspace
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
toolsets:
  - file
  - terminal
skills:
  - skill:using-superpowers
dependencies: []
formatter: markdown
license: MIT
---
## Table of Contents

## Goal

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Core Requirements](#core-requirements)
  - [Output Locations](#output-locations)
  - [Documentation Depth](#documentation-depth)
  - [Master Blueprint Must Include](#master-blueprint-must-include)
- [Workflow](#workflow)
  - [Phase 1: Discovery](#phase-1:-discovery)
  - [Phase 2: Analysis (Per Project)](#phase-2:-analysis-per-project)
  - [Phase 3: Generation (Per Project)](#phase-3:-generation-per-project)
  - [Phase 4: Master Blueprint Generation](#phase-4:-master-blueprint-generation)
- [Rules (from shared-rules-core)](#rules-from-shared-rules-core)
- [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
- [Success Criteria](#success-criteria)
- [Subgoals](#subgoals)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Dependencies](#dependencies)
- [Hooks](#hooks)
- [Scripts](#scripts)



- [Goal](#goal)
- [Core Requirements](#core-requirements)
- [Output Locations](#output-locations)
- [Documentation Depth](#documentation-depth)
- [Master Blueprint Must Include](#master-blueprint-must-include)
- [Workflow](#workflow)
- [Phase 1: Discovery](#phase-1:-discovery)
- [Phase 2: Analysis (Per Project)](#phase-2:-analysis-per-project)
- [Phase 3: Generation (Per Project)](#phase-3:-generation-per-project)
- [Phase 4: Master Blueprint Generation](#phase-4:-master-blueprint-generation)
- [Rules (from shared-rules-core)](#rules-from-shared-rules-core)
- [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
- [Success Criteria](#success-criteria)
- [Subgoals](#subgoals)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Dependencies](#dependencies)
- [Hooks](#hooks)
- [Scripts](#scripts)





Generate comprehensive technology stack documentation for every project in the workspace, placing each project's documentation directly inside its own directory (not in a centralized docs/ folder), plus a master workspace-level blueprint.

## Core Requirements

### Output Locations

1. **Per-Project**: `projects/<project-name>/TECHNOLOGY_STACK.md` — each project gets its own file in its root
2. **Workspace Root**: `Technology_Stack_Blueprint.md` — master cross-project blueprint

### Documentation Depth

Each TECHNOLOGY_STACK.md must include:

- Technology stack overview table (Language, Framework, Runtime, Package Manager, Database, Key Dependencies)
- Version information for all major dependencies (from package.json, requirements.txt, pyproject.toml, Cargo.toml, go.mod, pom.xml, build.gradle.kts, composer.json, Package.swift, *.csproj)
- Dependency analysis (production vs dev, outdated flags if detectable)
- Coding conventions specific to the project (from .editorconfig, eslint.config.mjs, .ruff.toml, pyrightconfig.json, etc.)
- Architecture patterns detected (monorepo, dual-stack, microservices, monolith)
- Build/test/lint commands
- Environment variables required (from .env.example if present)
- CI/CD pipeline references (from .github/workflows/)

### Master Blueprint Must Include

- Workspace-wide technology inventory (all languages, runtimes, package managers detected)
- Cross-project dependency map
- Shared tooling configurations
- Architectural decisions and conventions
- Deprecation/consolidation targets

## Workflow

### Phase 1: Discovery

1. Scan workspace for all project directories containing build manifests
2. Identify project types by manifest files:
- `package.json` → Node.js/TypeScript/Bun
- `requirements.txt` / `pyproject.toml` / `Pipfile` → Python
- `Cargo.toml` → Rust
- `go.mod` → Go
- `pom.xml` → Java/Maven
- `build.gradle.kts` / `settings.gradle.kts` → Kotlin/Gradle
- `composer.json` → PHP
- `Package.swift` → Swift
- `*.csproj` → C#/.NET
- `Gemfile` → Ruby
3. Build project inventory with paths

### Phase 2: Analysis (Per Project)

For each discovered project:

1. Read all manifest/config files
2. Parse dependencies and versions
3. Detect frameworks from dependency names
4. Read tooling configs (.editorconfig, eslint, ruff, pyright, etc.)
5. Read CI/CD workflows if present
6. Detect architecture patterns (check for backend/frontend split, dual-stack, etc.)

### Phase 3: Generation (Per Project)

Write `projects/<project-name>/TECHNOLOGY_STACK.md` with:

- Project header (path, generated date, status)
- Technology stack table
- Detailed dependency sections
- Coding conventions
- Commands reference
- Environment variables
- Architecture notes

### Phase 4: Master Blueprint Generation

Write `Technology_Stack_Blueprint.md` at workspace root with:

- Cross-project technology matrix
- Shared tooling summary
- Dependency version alignment analysis
- Architectural patterns across projects
- Consolidation recommendations

## Rules (from shared-rules-core)

1. **Map before touch** — Scan and inventory all projects first
2. **No backup files** — Use git for rollback
3. **Verify after each pass** — Check each generated file exists and has content
4. **One project at a time** — Process each project independently
5. **Explicit mappings** — Use actual config file content, not guesses
6. **Preserve intent** — Don't rename projects or change structure
7. **Idempotent** — Safe to re-run; overwrites existing TECHNOLOGY_STACK.md files
8. **File-backed evidence** — Every version claim must trace to a source file

## Anti-Patterns to Avoid

- ❌ Writing to `docs/Project_Architecture/` or any centralized folder
- ❌ Skipping projects without manifests (document as "No manifest detected")
- ❌ Inventing versions not found in source files
- ❌ Merging all projects into one giant file
- ❌ Omitting projects because they use unfamiliar tech stacks

## Success Criteria

- [ ] Every project directory with a manifest has a TECHNOLOGY_STACK.md
- [ ] Master Technology_Stack_Blueprint.md exists at workspace root
- [ ] All version numbers trace to actual config files
- [ ] No credentials/secrets in any output
- [ ] Files are valid Markdown with proper formatting

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

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


Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.

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

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `test-driven-development` | TDD workflow enforcement |
| `code-review` | Code quality assurance |
| `systematic-debugging` | Debugging and root cause analysis |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `code-sandbox` | Isolated code execution and testing |
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

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section