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
