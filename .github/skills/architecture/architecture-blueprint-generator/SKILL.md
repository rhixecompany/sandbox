---
name: architecture-blueprint-generator
title: "Architecture Blueprint Generator"
description: "Use when analyzing codebases to create detailed architectural documentation. Auto-detects technology stacks and architectural patterns, generates visual diagrams, documents implementation patterns, and provides extensible blueprints."
version: 1.1.0
author: "Hermes Agent"
license: MIT
tags: [architecture, documentation, blueprint, design-patterns]
metadata:
  hermes:
    tags: [imported]
---
# Architecture Blueprint Generator

## Overview

Analyze a codebase's architecture and generate a comprehensive blueprint document. The blueprint includes architectural pattern detection, component analysis, data flow documentation, cross-cutting concerns, and implementation templates.

## When to Use

- Documenting architecture for an existing codebase
- Onboarding architects or senior developers to a project
- Planning refactoring that spans multiple components
- Creating architectural decision records (ADRs)
- Reviewing architecture for consistency and best practices

## When NOT TO USE

- Documenting folder structure only (use folder-structure-blueprint-generator)
- Documenting technology stack (use technology-stack-blueprint-generator)
- Small single-component projects

## Skills Required

| Skill | Purpose |
|-------|---------|
| `context-map` | Map component boundaries and data flows |
| `folder-structure-blueprint-generator` | Folder structure documentation |
| `technology-stack-blueprint-generator` | Technology stack documentation |

## Workflow

### Phase 1: Detect Architecture Pattern

Analyze the codebase for architectural patterns:
- Clean Architecture (use cases, entities, adapters)
- Microservices (multiple deployable services)
- Layered (presentation → business → data)
- MVVM/MVC (UI patterns)
- Hexagonal (ports and adapters)
- Event-Driven (event sourcing, CQRS)

### Phase 2: Gather Context

Before deep code analysis, check for existing context files that provide ready-made architecture information:

1. **Check `AGENTS.md` first** — these files often contain pre-digested architecture, tech stack, conventions, and commands. Use them as the primary source, then verify against actual code.
2. Check `README.md` for project overview and setup.
3. Check `docs/` for existing architecture documentation.
4. Only then deep-dive into source code for patterns that context files don't cover.

### Phase 3: Analyze Components

For each major component:
1. Document purpose and responsibility
2. Map internal structure (classes, modules)
3. Identify interaction patterns (APIs, events, shared DB)
4. Note extension points and plugin mechanisms

### Phase 4: Document Cross-Cutting Concerns

Analyze how the architecture handles:
- Authentication & authorization
- Error handling & resilience
- Logging & monitoring
- Validation
- Configuration management

### Phase 5: Generate Blueprint

Use the template at `templates/blueprint-template.md` to generate:
- Architectural overview with diagrams
- Core component documentation
- Layer and dependency map
- Data architecture
- Implementation patterns
- Extension and evolution guide

### Phase 6: Save Output

Save to `docs/Project_Architecture_Blueprint.md`

### Phase 7: Generate Per-Subproject Documentation (Multi-Repo Workspaces)

When the workspace contains multiple subprojects (monorepo), generate individual context files for each:

1. Identify all subproject directories (skip `.git`, `node_modules`, `venv`)
2. For each subproject, create three files under `docs/Project_Architecture/`:
   - `{subproject-name}_architecture.md` — Architecture overview
   - `{subproject-name}_folders.md` — Key directory structure
   - `{subproject-name}_techstack.md` — Technology stack table

**Critical: File naming must match the directory name exactly.** Use the precise directory name (hyphens, underscores, case) — do NOT normalize to underscores or any other convention. A subproject in `projects/cookiecutter-django-tailwind/` must produce `cookiecutter-django-tailwind_architecture.md`, not `cookiecutter_django_tailwind_architecture.md`. Mismatched naming creates duplicate files that confuse agents and humans.

For tech-stack and folder-structure docs, use the companion skills (`technology-stack-blueprint-generator`, `folder-structure-blueprint-generator`) — but apply the same naming rule there too.

## Verification Checklist

- [ ] Architectural pattern correctly identified
- [ ] All major components documented
- [ ] Cross-cutting concerns analyzed
- [ ] Diagrams generated (C4, UML, or flow)
- [ ] Implementation patterns documented
- [ ] Blueprint saved to docs/ folder

## Pitfalls

- **Theory vs. reality:** Document what the code actually does, not what the pattern理论上 should look like
- **Over-diagramming:** One clear diagram beats three confusing ones
- **Missing evolution section:** Architecture changes — document how to extend it
- **Ignoring violations:** Note where the code deviates from the stated pattern
