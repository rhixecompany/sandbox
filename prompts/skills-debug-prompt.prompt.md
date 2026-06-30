---
license: MIT
author: Hermes Agent
version: 1.0.0
name: skills-debug-prompt
title: Skills Debug and Remediation Execution
trigger: skills-debug
description: >
  Execute the skills remediation plan from docs/plan/skills-debug-plan.md.
  Fix F-grade skills first (boilerplate, missing frontmatter), then C-grade
  (unclosed fences, duplicate headings), then verify.
tags:
  - ai-assistant
  - audit
  - data
  - debugging
  - fix
  - prompts
  - skills
  - typescript
  - hermes
  - skills
  - remediation
  - fix
metadata:
  hermes:
    related_skills: []
    tags:
    - skills-debug-prompt.prompt

---
metadata:
  hermes:
    related_skills: []
    tags:
    - skills-debug-prompt.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - skills-debug-prompt.prompt

## Goal

Apply fixes to all F-grade and C-grade skills identified in the audit.
Target: F=0, C≤5 after completion.

## Context

- **Skills root:** `$HOME/AppData/Local/hermes/skills/` (resolves to `C:\Users\Alexa\AppData\Local\hermes\skills\`)
- **Audit results:** `docs/skills-audit-results.json`
- **Remediation plan:** `docs/plan/skills-debug-plan.md`
- **Master index:** `docs/skills-debug-context.md`

## Execution Steps

> ### Step 1: Fix F3/F3b Boilerplate (29 skills)
> For each F3/F3b skill, read the file and fix the `## Goal` section:

> **Full content:** `templates/skills-debug-prompt/execution_steps.md`

## Tools

- `read_file(path)` — Read skill before fixing
- `patch(path, old_string, new_string)` — Apply targeted fix
- `write_file(path, content)` — Full rewrite if needed
- `execute_code(code)` — Re-run audit verification


## Template References

Templates in `templates/skills-debug-prompt/`:
- `execution_steps.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
