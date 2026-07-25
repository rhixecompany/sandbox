---
author: Alexa
description: Use when working with Mcp Cli.
license: MIT
metadata:
  hermes:
    tags:
    - tools
name: mcp-cli
tags:
- tools
title: Mcp Cli
version: 1.0.0

---

# Mcp Cli

## Goal
Provide comprehensive guidance for Mcp Cli workflows.

## Subgoals
1. **Preparation** — Understand prerequisites and setup
2. **Execution** — Follow structured workflow with error handling
3. **Verification** — Confirm output meets requirements

## Personas
| Persona | When to Use |
|---------|-------------|
| **Developer** | Technical implementation and coding tasks |
| **Admin** | System operations and maintenance |
| **User** | Day-to-day operations and usage |

## Personality & Tone
- **Tone**: Professional, concise
- **Style**: Step-by-step instructions with examples
- **Avoid**: Unclear prerequisites, missing error handling
- **Encourage**: Verification checkpoints, resumability

## Profile Selection
| Task Type | Recommended Profile |
|-----------|---------------------|
| General purpose | `default` |
| Code changes | `code-architect` |
| System operations | `adminbot` |

## Skills Required
| Skill | Purpose |
|-------|---------|
| `hermes-agent` | Core Hermes functionality |
| `skill-judge` | Evaluate skill quality |

## When to Use
When working with Mcp Cli in Hermes workflows.

## When NOT to Use
When this skill is not relevant to your task.

## Workflow

### Phase 1: Preparation
- Understand the context and requirements
- Verify prerequisites are met

### Phase 2: Execution
- Follow step-by-step instructions
- Handle errors gracefully

### Phase 3: Verification
- Confirm output meets requirements
- Document results

## Pitfalls
- **Thin content**: This skill may lack concrete examples. Add code examples and real-world use cases.
- **Missing error handling**: Always include error handling patterns in workflow phases.
- **No resumability**: Add entry/exit checks at each phase for long-running workflows.

## Verification Checklist
- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

