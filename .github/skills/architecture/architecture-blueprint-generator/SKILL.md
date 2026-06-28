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

### Phase 2: Analyze Components

For each major component:
1. Document purpose and responsibility
2. Map internal structure (classes, modules)
3. Identify interaction patterns (APIs, events, shared DB)
4. Note extension points and plugin mechanisms

### Phase 3: Document Cross-Cutting Concerns

Analyze how the architecture handles:
- Authentication & authorization
- Error handling & resilience
- Logging & monitoring
- Validation
- Configuration management

### Phase 4: Generate Blueprint

Use the template at `templates/blueprint-template.md` to generate:
- Architectural overview with diagrams
- Core component documentation
- Layer and dependency map
- Data architecture
- Implementation patterns
- Extension and evolution guide

### Phase 5: Save Output

Save to `docs/Project_Architecture_Blueprint.md`

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
