---
author: Hermes Agent
description: Use when creating complex HTML artifacts with React, Tailwind CSS, shadcn/ui
  — multi-component interfaces, state management, routing.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: web-artifacts-builder
tags:
- web
- react
- tailwind
- artifacts
- shadcn
title: Web Artifacts Builder
version: 1.0.0

---
# Web Artifacts Builder

## Overview

Create complex HTML artifacts using React, Tailwind CSS, and shadcn/ui.

## When to Use

- Building interactive multi-component HTML artifacts
- Creating dashboards or tooling surfaces outside a full app pipeline
- Rapidly producing standalone frontend artifacts

## When NOT to Use

- Static one-page documents
- Simple text or table exports

## Skills Required

| Skill | Purpose |
|-------|---------|
| `frontend-design` | Layout and visual structure guidance |
| `shadcn` | Reusable UI components |

## Workflow

### Phase 1: Define Scope

1. Identify target audience and primary actions.
2. Confirm routing and state requirements.
3. Check whether the artifact needs shadcn components.

### Phase 2: Structure the Artifact

1. Select a base structure and component hierarchy.
2. Define route structure if needed.
3. Plan data and interaction needs.

### Phase 3: Implement

1. Create main entry and routing.
2. Build component set with Tailwind and shadcn/ui.
3. Wire state management.

### Phase 4: Verify and Deliver

1. Review generated artifact behavior.
2. Confirm UI consistency.
3. Deliver final file or bundle.

## Verification Checklist

- [ ] Artifact purpose and pages identified
- [ ] Routing and state requirements defined
- [ ] Components built and integrated
- [ ] Tailwind classes applied consistently
- [ ] Final artifact reviewed and delivered

## Pitfalls

- Overcomplicating state for simple artifacts
- Adding unnecessary routing when a single-page artifact is sufficient
- Skipping component responsibility review before final revision

## Recently Absorbed Skills
- `create-web-form` (2026-06-25) — Web form creation with accessible HTML/CSS/JS
