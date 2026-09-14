---
name: "tool-gateway-bundle"
title: "Feature Bundle Skill — Nous Tool Gateway"
version: 1.0.0
author: Hermes Agent
description: "Implements the feature documented at docs/features/tool-gateway.md by generating plan/spec/prompt/skill/script/result artifacts."
---

# Skill: tool-gateway-bundle

## Purpose

Translate the feature documentation (tool-gateway.md, 223 lines) into executable artifacts following the multi-file-change-protocol.

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
- .hermes/plans/feature-docs-implementation-plan.md
