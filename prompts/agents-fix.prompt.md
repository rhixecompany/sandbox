---
license: MIT
author: Hermes Agent
version: 1.0.0
name: agents-fix
title: Agents Sync and Deduplication
trigger: agents-fix
description: Sync and deduplicate agent definitions across Hermes and Copilot with dependency mapping and schema validation.
tags:
  - agents
  - ai-assistant
  - configuration
  - fix
  - ml
  - prompts
  - typescript
  - workflow
  - hermes
  - copilot
  - agents
  - sync
metadata:
  hermes:
    related_skills: []
    tags:
    - agents-fix.prompt

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
dependencies:
    - prompt:context-map.prompt.md
    - prompt:update-implementation-plan.prompt.md
    - skill:brainstorming
    - skill:plans-and-specs
    - skill:dispatching-parallel-agents
    - skill:subagent-driven-development
    - skill:systematic-debugging
    - skill:simplify
    - skill:acpx-executor
    - skill:copilot-cli-quickstart
    - tool:terminal
    - tool:search_files
skills:
    - introspection-only-general
    - no-git-delete
    - no-net-fetch
    - skills-tools-preflight-check
    - brainstorming
    - plans-and-specs
    - dispatching-parallel-agents
    - subagent-driven-development
    - systematic-debugging
    - simplify
    - acpx-executor
    - copilot-cli-quickstart

## Goal

Sync agent definitions across Hermes and Copilot without losing schema fidelity or registration details.

## Context

Use this prompt when agent definitions, agent-style prompts, or platform registrations drift across the three ecosystems. The workflow is discovery first, then mapping, then sync, then verification.

## Inputs

- The agent files and registrations in each platform
- Workspace context and platform configuration
- Optional user constraints, platform targets, or migration rules

## Outputs

- A cross-reference table for equivalent agents
- A sync plan with deduplication notes
- Updated files or config entries
- A verification report showing what changed

## Rules

> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)
> Domain-specific additions below.

- Detect the file format before modifying anything
- Preserve registrations unless the user explicitly requests a rename or removal
- Keep the response structured and deterministic

## Phases

### Phase 1: Discovery

Discover agent files across Hermes, and Copilot. Record names, triggers, descriptions, and registration state.

### Phase 2: Cross-reference mapping

Build a mapping table that links equivalent agents across platforms and highlights gaps.

### Phase 3: Sync and deduplicate

Apply the minimal set of changes needed to align the agent definitions.

### Phase 4: Verification

Verify that each platform still matches its expected schema and that no agents were lost.

## Steps

1. Inventory each platform's agent definitions or prompt manifests
2. Match equivalent agents by name, trigger, and behavior
3. Resolve conflicts with explicit portable rules
4. Write deduplicated definitions back to each platform
5. Run verification and report drift or mismatches
