---
name: brainstorming
title: Brainstorming
description: "Use when you need structured idea generation and divergent ideation under constraints. Use before creating features, building components, adding functionality, or modifying behavior."
version: 1.2.0
author: Alexa
license: MIT
tags: [imported]
metadata:
  hermes:
    tags: [imported]
---
# Brainstorming

## Goal
Explore user intent, requirements, and design through structured divergent thinking before any creative work. Produce a documented decision with rationale, trade-offs, and implementation plan.

## Subgoals
1. **Understand** — Clarify problem, user, desired outcome, and constraints
2. **Explore** — Generate multiple approaches with pros/cons
3. **Evaluate** — Compare options against requirements; get feedback
4. **Plan** — Break down into tasks with dependencies and estimates

## Personas
| Persona | When to Use |
|---------|-------------|
| **Product Manager** | Defining features, prioritizing requirements |
| **Developer** | Exploring implementation approaches |
| **Designer** | Exploring UI/UX directions |
| **Architect** | Evaluating system-level trade-offs |

## Personality & Tone
- **Tone**: Open, curious, non-judgmental
- **Style**: Generate quantity first, then filter for quality
- **Avoid**: Premature convergence on a single idea, dismissing impractical concepts
- **Encourage**: "Yes, and..." thinking, building on others' ideas

## Profile Selection
| Task Type | Recommended Profile |
|-----------|---------------------|
| Feature ideation | `creative-director` |
| Technical approach | `code-architect` |
| Research/synthesis | `research-analyst` |
| Planning/coordination | `exec-assistant` |
| General purpose | `default` |

## When to Use
- Creating new features
- Building components
- Adding functionality
- Modifying existing behavior
- Making design decisions
- Starting any creative work

**Triggers**: "Build X", "Create feature Y", "Add component Z", "Design this", "How should we approach", "What's the best way to"

## When NOT to Use
- For code review (use `requesting-code-review` instead)
- For debugging (use `systematic-debugging` instead)
- For implementation (use `test-driven-development` instead)
- When requirements are already fully defined and approved

## Skills Required
| Skill | Purpose |
|-------|---------|
| `plans-and-specs` | Document the plan after brainstorming |
| `test-driven-development` | Implement using TDD after deciding approach |
| `frontend-design` | Design UI/UX if brainstorming interface |
| `mermaid-diagrams` | Visualize architecture options |
| `writing-plans` | Document the implementation plan |

## Workflow

### Phase 1: Understand Intent
- What problem are we solving?
- Who is the user?
- What's the desired outcome?
- What constraints exist?

### Phase 2: Explore Options
- Generate multiple approaches (aim for 3+)
- List pros and cons for each
- Consider trade-offs
- Identify risks
- **Techniques**: See `references/ideation-techniques.md` for SCAMPER, brainwriting, mind mapping

### Phase 3: Evaluate & Decide
- Compare options against requirements
- Get stakeholder feedback
- Document decision rationale
- Identify next steps
- **Framework**: See `references/ideation-techniques.md` for feasibility matrix

### Phase 4: Plan Implementation
- Break down into tasks
- Identify dependencies
- Estimate effort
- Create implementation plan
- **Template**: See `references/ideation-techniques.md` for decision documentation template

## Pitfalls
- **Premature convergence**: Don't settle on the first idea. Generate at least 3 options before evaluating.
- **No stakeholder input**: Always involve relevant stakeholders before deciding.
- **Missing documentation**: Record WHY you chose an approach, not just WHAT.
- **Skipping validation**: Test assumptions with users or prototypes before committing.
- **Over-polishing**: Brainstorming is about exploration, not perfection. Keep ideas rough.

## Best Practices
- **Involve stakeholders**: Get input early
- **Document decisions**: Record why you chose this approach
- **Consider alternatives**: Don't settle on first idea
- **Validate assumptions**: Test with users if possible
- **Plan before coding**: Brainstorm before implementation

## Verification Checklist
- [ ] Problem and user are clearly defined
- [ ] Multiple approaches were considered and documented (≥3)
- [ ] Decision rationale is recorded with pros/cons
- [ ] Implementation plan is created with task breakdown
- [ ] Stakeholders have been consulted on the direction
- [ ] At least 3 options were generated before evaluating
