---
name: agents-system-prompt-context-fix
title: Agents System Prompt Context Fix
description: Repair malformed frontmatter, missing fields, and stale context references in `.github/agents/` and `.github/instructions/` artifacts.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets: - file - terminal
scripts: []
skills: - using-superpowers - user-communication-preferences - plans-and-specs - executing-plans - verification-before-completion - subagent-driven-development
formatter: default
dependencies: - skill:using-superpowers - skill:user-communication-preferences - skill:plans-and-specs - skill:executing-plans - skill:verification-before-completion - skill:subagent-driven-development
tags: - audit - fix - prompts - repairs
trigger: /agents-system-prompt-context-fix
metadata:
  related_skills: [using-superpowers, user-communication-preferences, plans-and-specs, executing-plans, verification-before-completion, subagent-driven-development]
---

# Agents System Prompt Context Fix

## Phase 2 Overview

1. Inspect `.github/agents/` and `.github/instructions/` for malformed frontmatter, missing fields, and stale context references.
2. Repair frontmatter-only issues; do not alter agent behavior beyond prompt/spec correctness.
3. Ensure context/spec references point to existing files in this repo.
4. Verify each repaired artifact can be parsed as valid markdown/YAML frontmatter.

**Skip condition:** If no `.agent.md` or `.instructions.md` repair targets exist, mark phase complete with evidence.