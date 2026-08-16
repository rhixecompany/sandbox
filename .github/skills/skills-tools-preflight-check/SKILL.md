---
name: skills-tools-preflight-check
description: Preflight verification of skills and tools availability before execution. Check that all required skills exist, tools are accessible, and dependencies are satisfied before starting a workflow.
category: qa
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
metadata:
  hermes:
    tags: []
---
# Skills & Tools Preflight Check

Preflight verification of skills and tools availability before execution.


## When to Use

- When you need to automate or structure workflows for `skills-tools-preflight-check`.
- When executing multi-step tasks that benefit from phased orchestration.
- When you need deterministic, verifiable tool execution.

## Overview

Automated reasoning and workflow tool for `skills-tools-preflight-check`. Execute multi-step tasks with deterministic quality controls and structured outputs.

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

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for "Skills Tools Preflight Check".

### Phase 2: Execution

Run the primary "Skills Tools Preflight Check" operations according to the defined requirements.

### Phase 3: Verification

Verify output, handle any errors, and confirm results meet expectations.

### Phase 4: Completion

Document results, clean up resources, and finalize any deliverables.

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
