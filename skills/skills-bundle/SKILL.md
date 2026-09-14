---
name: "skills-bundle"
title: "Feature Bundle Skill — Skills System"
version: 1.0.0
author: Hermes Agent
description: "Implements the feature documented at docs/features/skills.md by generating plan/spec/prompt/skill/script/result artifacts."
---

# Skill: skills-bundle

## Purpose

Translate the feature documentation (skills.md, 1063 lines) into executable artifacts following the multi-file-change-protocol.

## Workflow

1. Load source (verified downloaded with real content).
2. Generate 5-artifact bundle (plan, spec, prompt, skill, script).
3. Execute script ().
4. Verify exists.

## Rules

- Never invent URLs or session IDs.
- Always verify file counts and sizes before claiming download success.
- Use sequential gate verification after parallel bundle generation.
- Report unavailable skills honestly (plan / mcp-ast-grep / mcp-filesystem / mcp-memory unavailable in default profile — use native equivalents).

## Cross-References

- multi-file-change-protocol (loaded)
- subagent-driven-development (load for parallel execution)
- using-superpowers / brainstorming / user-communication-preferences
- ./plans/feature-docs-implementation-plan.md
