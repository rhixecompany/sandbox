---
name: technology-stack-blueprint-generator
title: "Technology Stack Blueprint Generator"
description: "Use when analyzing codebases to create detailed technology stack documentation. Auto-detects technologies, versions, licensing, coding conventions, and usage patterns across multiple platforms."
version: 1.1.0
author: "Hermes Agent"
license: MIT
tags: [architecture, documentation, technology-stack, blueprint]
metadata:
  hermes:
    tags: [imported]
---
# Technology Stack Blueprint Generator

## Overview

Analyze a codebase and generate a comprehensive technology stack blueprint. The blueprint documents all technologies, frameworks, dependencies, versions, coding conventions, and usage patterns.

## When To Use

- Documenting the full technology stack of a project
- Onboarding developers who need to understand the toolchain
- Planning technology upgrades or migrations
- Creating a reference for consistent code generation
- Reviewing dependency licensing

## When NOT TO USE

- Documenting folder structure (use folder-structure-blueprint-generator)
- Documenting architecture patterns (use architecture-blueprint-generator)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `folder-structure-blueprint-generator` | Folder structure documentation |
| `architecture-blueprint-generator` | Architecture documentation |

## Workflow

### Phase 1: Identify Technologies

Scan the codebase for:
- Project files (package.json, .csproj, pom.xml, requirements.txt)
- Build configurations (webpack, vite, msbuild)
- CI/CD pipeline files (.github/workflows, azure-pipelines.yml)
- Docker and container configs
- IDE and tooling configs

### Phase 2: Analyze Dependencies

For each technology area, document:
- Core frameworks and their versions
- Key dependencies categorized by purpose
- Version constraints and compatibility notes
- License information for key dependencies

### Phase 3: Document Conventions

Extract and document:
- Naming conventions (files, classes, variables)
- Code organization patterns
- Error handling approaches
- Testing patterns
- Configuration management approach

### Phase 4: Generate Blueprint

Use the template at `templates/blueprint-template.md` to generate:
- Complete technology stack map
- Implementation patterns and conventions
- Usage examples for each major technology
- Technology relationship diagrams
- New code implementation templates

### Phase 5: Save Output

Save to `docs/Technology_Stack_Blueprint.md`

## Verification Checklist

- [ ] All technologies identified and versioned
- [ ] Dependencies categorized by purpose
- [ ] Coding conventions documented
- [ ] Usage examples extracted
- [ ] License information noted for key deps
- [ ] Blueprint saved to docs/ folder

## Pitfalls

- **Version staleness:** Versions in code may drift from docs — note the date
- **Over-documenting minor deps:** Focus on significant technologies
- **Missing dev tooling:** Don't forget linters, formatters, CI/CD tools
- **Ignoring deprecated tech:** Note technologies marked for replacement
