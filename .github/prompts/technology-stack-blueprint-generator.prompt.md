---
name: technology-stack-blueprint-generator
title: Technology Stack Blueprint Generator
description: Generates comprehensive technology stack documentation for all projects in the workspace. Each project gets its own TECHNOLOGY_STACK.md in its root directory, plus a master Technology_Stack_Blueprint.md at the workspace root.
version: 2.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills:
  - technology-stack-blueprint-generator
formatter: default
plan: None
tags:
  - documentation
  - architecture
  - technology-stack
  - blueprint
  - multi-project
trigger: /technology-stack-blueprint-generator
dependencies: []
metadata:
  hermes: {}
---

# Technology Stack Blueprint Generator

## Goal

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
