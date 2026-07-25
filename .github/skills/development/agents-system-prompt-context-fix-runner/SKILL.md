---
name: agents-system-prompt-context-fix-runner
title: "Agents System Prompt Context Fix Runner"
description: "Execute the agents-system-prompt-context-fix prompt workflow - generates architecture blueprints, folder structure blueprints, tech stack blueprints for all projects, then audits and fixes VS Code configs."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [architecture, documentation, vscode, automation, audit]
metadata:
  hermes:
    related_skills:
    - architecture-blueprint-generator
    - folder-structure-blueprint-generator
    - technology-stack-blueprint-generator
    - vscode-workspace-configurator
    - vscode-config-audit
    tags:
    - architecture
    - documentation
    - vscode
    - automation
    - audit
---

# Agents System Prompt Context Fix Runner

This skill orchestrates the full execution of the agents-system-prompt-context-fix prompt workflow.

## Phase 1: Generate Agent Context Files

### Step 1.1: Run architecture-blueprint-generator
Analyzes codebase architecture and generates comprehensive blueprints.

### Step 1.2: Run folder-structure-blueprint-generator
Documents folder structures with naming conventions and patterns.

### Step 1.3: Run technology-stack-blueprint-generator
Documents technology stacks, dependencies, and conventions.

## Phase 2: Audit VS Code Configuration

### Step 2.1: List all JSON files in .vscode directories
### Step 2.2-2.6: Triage, Audit, Debug, Enhance, Verify

## Phase 3: Verify & Implement

### Step 3.1: Verify plan and specs
### Step 3.2: Implement verified plan

## Lessons from recent runs

- When sweeping `.vscode` JSON files across a mixed workspace, exclude generated/vendor trees first: `node_modules`, `.git`, `.next`, `dist`, `build`, `coverage`, `out`, `.venv`, `venv`, and `__pycache__`.
- Keep syntax validation separate from formatter-policy warnings. Fail on invalid JSON or missing required files; warn on formatter mismatches unless the task explicitly requires strict enforcement.
- In large workspaces, namespace generated per-project docs by relative path under `docs/Project_Architecture/` to avoid collisions between root-level and nested projects.
- See `references/vscode-audit-lessons.md` for the verified commands and the exact audit workaround.

## Execution

Run via: hermes skill run agents-system-prompt-context-fix-runner