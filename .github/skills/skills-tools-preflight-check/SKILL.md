---
name: skills-tools-preflight-check
description: Preflight verification of skills and tools availability before execution. Check that all required skills exist, tools are accessible, and dependencies are satisfied before starting a workflow.
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - preflight
  - verification
  - skills
  - tools
  - safety
title: "Skills Tools Preflight Check"
---
# Skills & Tools Preflight Check

Preflight verification of skills and tools availability before execution.

## Checks

1. **Skills exist** — All referenced skills are available in the skill library
2. **Tools accessible** — Required tools are in the enabled toolset
3. **Dependencies met** — Script dependencies and packages are installed
4. **Permissions OK** — Required file/network permissions are granted

## When to use

- Before starting multi-step workflows
- Before running prompts that reference multiple skills
- As CI gate for prompt validation
- When onboarding new prompts to the library

## Verification

| Check | Pass | Fail |
|-------|------|------|
| All skills exist | ✓ | ✗ |
| Tools accessible | ✓ | ✗ |
| Dependencies met | ✓ | ✗ |
| Permissions OK | ✓ | ✗ |

## Usage

```bash
# Run preflight check for a prompt
skills-tools-preflight-check <prompt-name>

# Run preflight for all prompts in directory
skills-tools-preflight-check --all
```

## Skills Required

| Skill | Purpose |
|-------|---------|
| `hermes-agent` | Core Hermes functionality |
| `skill-judge` | Evaluate skill quality |

## Pitfalls

- **Thin content**: Add concrete code examples and real-world use cases where applicable.
- **Missing error handling**: Include error-handling patterns in workflow phases.
- **No resumability**: Add entry/exit checks at each phase for long-running workflows.

## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has >=3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md under 250 lines
- [ ] No placeholder text
