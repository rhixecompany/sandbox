---
author: Alexa
description: Use when working with Prompt Engineering.
license: MIT
metadata:
  hermes:
    tags:
    - tools
name: prompt-engineering
tags:
- tools
title: Prompt Engineering
version: 1.1.0

---

# Prompt Engineering

## Goal
Provide comprehensive guidance for Prompt Engineering workflows.

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
When working with Prompt Engineering in Hermes workflows.

## When NOT to Use
When this skill is not relevant to your task.


## Usage

```bash
# Example usage
prompt engineering [options]
```

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


### Phase 4: Add Onboarding Q&A to an Existing Prompt

Apply when a complex orchestrator prompt has no lightweight entry points for simple user questions.

**Steps:**
1. Identify target prompt files (e.g. `repo.*.prompt.md`)
2. Read all matching files to understand their structure and scope
3. Search for any existing handling of the target questions
4. Plan which questions fit in which prompt (question classification table in `references/onboarding-qa-pattern.md`)
5. Add a `## Quick <Topic> Onboarding` section with Q&A blocks
6. Each Q&A block: **question header** → **Phase:** label → numbered steps → **Actions:** code block
7. For cross-cutting questions, add the primary version in the most natural prompt and cross-reference from others
8. Verify with grep that every question string appears in the expected files

**Pattern reference:** `references/onboarding-qa-pattern.md`

### Phase 5: Final Review

Confirm all changes complete and produce summary report.

- Use `--dry-run` to preview changes before applying
- Use `--help` to see all available options

## Pitfalls
- **Thin content**: This skill may lack concrete examples. Add code examples and real-world use cases.
- **Missing error handling**: Always include error handling patterns in workflow phases.
- **No resumability**: Add entry/exit checks at each phase for long-running workflows.
- **Onboarding Q&A bloating the prompt**: Keep each Q&A to ≤15 lines, whole section ≤80 lines. If the onboarding section would exceed 80 lines, split to a separate lightweight prompt instead.
- **Orphaned Q&A with stale commands**: Every command in **Actions:** MUST work at runtime. Grep for backticked shell commands and verify them before committing. A `du` flag that doesn't exist on the target OS is worse than no command at all.
- **Read_file pipe-prefix confusion**: `read_file` renders output as `LINE_NUM|CONTENT`. The `|` is a display separator, NOT file content. When copying text from read_file into a `patch` call, the pipe and line number must be stripped. Same for `grep -n` output where `LINE_NUM:CONTENT` includes a colon prefix. This caused a real bug where `---` became `|---` in a section separator (see `references/onboarding-qa-pattern.md` Post-Edit Validation Checklist for detection commands).

## Verification Checklist
- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

