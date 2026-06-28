---
author: Hermes Agent
description: Use when analyzing and documenting the context boundaries, dependencies,
  and data flows between components in a complex system. Use during architecture review,
  onboarding to unfamiliar codebases, or debugging cross-component issues.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: context-map
tags:
- architecture
- documentation
- context-mapping
- onboarding
title: Context Map
version: 1.0.0

---
# Context Map

## Overview

Generate and maintain context maps that document the boundaries, dependencies, and data flows between components in a complex system. Context maps make implicit architecture explicit, enabling faster onboarding and safer changes.

## When to Use

- Onboarding to an unfamiliar codebase with multiple components
- Debugging issues that span component boundaries
- Documenting architecture decisions and their rationale
- Planning refactoring that affects multiple components
- Reviewing system architecture for coupling and cohesion issues

## When NOT to Use

- Simple single-file changes with no cross-component impact
- Performance profiling (use systematic-debugging instead)
- Initial project creation (use architecture-blueprint-generator instead)

## Workflow

### Phase 1: Discover Components

1. Identify all major components/modules in the system
2. Map entry points (APIs, CLIs, UI surfaces)
3. Catalog shared utilities, libraries, and services
4. Document external dependencies and integrations

```bash
# Find component boundaries
find src/ -name "*.ts" -o -name "*.py" | head -50
# Map imports/dependencies
grep -r "from.*import\|require(" src/ | head -30
```

### Phase 2: Map Relationships

For each component, document:
- **Provides:** What services/data does this component expose?
- **Requires:** What does this component depend on?
- **Boundary:** What are the clear interfaces between this and adjacent components?
- **Data flow:** What data crosses this boundary, in which direction?

### Phase 3: Document Context Boundaries

Create a context map document with:

| Component | Provides | Requires | Boundary Type |
|-----------|----------|----------|---------------|
| Auth Service | Token validation, user sessions | User DB | Synchronous API |
| API Gateway | Rate limiting, routing | All backend services | HTTP proxy |
| Cache Layer | Fast reads | Redis | In-memory KV |

**Boundary types:**
- **Synchronous API** — direct call/response
- **Event-driven** — pub/sub, message queue
- **Shared database** — direct data access (tight coupling)
- **File-based** — config files, shared storage

### Phase 4: Identify Risks

Flag these coupling patterns:
- **Circular dependencies** — A depends on B depends on A
- **God components** — Single component that everything depends on
- **Leaky abstractions** — Implementation details crossing boundaries
- **Shared mutable state** — Multiple components writing to same data

## Verification Checklist

- [ ] All major components identified and documented
- [ ] Dependencies mapped in both directions
- [ ] Boundary types classified
- [ ] Circular dependencies flagged
- [ ] Risk patterns identified
- [ ] Map stored in docs/context-map.md

## Skills Required

| Skill | Purpose |
|-------|---------|
| `codemap` | Generate component hierarchy |
| `architecture-blueprint-generator` | Full architecture documentation |
| `systematic-debugging` | Trace cross-component issues |

## Example Context Map

```
[User Browser] --HTTP--> [API Gateway] --gRPC--> [Auth Service]
                                             |
                                             +--gRPC--> [User Service] --SQL--> [User DB]
                                             |
                                             +--gRPC--> [Product Service] --SQL--> [Product DB]
                                             |
                                             +--Event--> [Notification Service]
```

## Pitfalls

- **Outdated maps:** Context maps rot quickly — update them when architecture changes
- **Too much detail:** Focus on component boundaries, not internal implementation
- **Missing implicit dependencies:** Some dependencies aren't in code (shared config, deployment order)
- **Ignoring data flow direction:** Unidirectional flows are easier to reason about than bidirectional
