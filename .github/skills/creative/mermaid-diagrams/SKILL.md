---
author: Hermes Agent
description: Use when creating software diagrams — class diagrams, sequence diagrams,
  flowcharts, ERDs, C4 architecture diagrams — using Mermaid syntax.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: mermaid-diagrams
tags:
- diagrams
- mermaid
- architecture
- documentation
- visualization
title: Mermaid Diagrams
version: 1.0.0

---
# Mermaid Diagrams

## Overview

Comprehensive guide for creating software diagrams using Mermaid syntax. Includes class diagrams, sequence diagrams, flowcharts, ERDs, C4 architecture diagrams, state diagrams, and more.

## When to Use

- Creating software architecture diagrams
- Visualizing system design
- Documenting database schemas
- Showing application flows
- Creating flowcharts or algorithms
- Modeling domain objects
- Documenting API interactions

## When NOT to Use

- Simple text descriptions
- Real-time collaboration
- Complex 3D visualizations
- Non-technical diagrams

## Skills Required

| Skill | Purpose |
|-------|---------|
| `project-docs` | Integrate diagrams into project documentation |
| `frontend-design` | Layout and visual hierarchy for rendered diagrams |

## Workflow

### Phase 1: Identify Diagram Type

- Determine what to visualize
- Choose appropriate diagram type
- Plan diagram structure

### Phase 2: Design Diagram

- Sketch layout and relationships
- Identify key components
- Plan connections and flows

### Phase 3: Create Mermaid Diagram

- Write Mermaid syntax
- Add labels and descriptions
- Verify syntax correctness

### Phase 4: Refine & Document

- Review diagram clarity
- Adjust layout if needed
- Add to documentation
- Maintain as code evolves

## Tools & References

- **Mermaid**: https://mermaid.js.org
- **Diagram Types**: Class, sequence, flowchart, ERD, C4, state, git graph

## Best Practices

- Keep diagrams simple and focused
- Use consistent naming
- Label all relationships
- Update diagrams with code changes
- Version control diagrams
- Use appropriate diagram type
- Test diagram rendering

## Verification Checklist

- [ ] Diagram type selected and appropriate for the use case
- [ ] Mermaid syntax validates without errors
- [ ] All components and relationships labeled
- [ ] Diagram renders correctly in target viewer
- [ ] Documentation updated with diagram reference
- [ ] Diagram version-controlled alongside code

## Pitfalls

- Overly complex diagrams become unmaintainable; split into multiple views
- Forgetting to update diagrams when code drifts reduces trust
- Mermaid syntax varies slightly across versions; test in target renderer
- Large sequence diagrams can become unreadable; use `alt`/`opt` blocks to simplify
