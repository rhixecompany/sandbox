---
name: agents-system-prompt-context-fix
...
title: Agents System Prompt Context Fix
...
description: 'Audit and repair GitHub Copilot/Hermes agent and instruction markdown: fix malformed
  frontmatter, missing fields, stale references, cross-repo path drift, and verification
  state across .github instructions/agents and related docs.'
version: 1.0.0
...
license: MIT
...
author: Hermes Agent
...
toolsets: - file
- terminal
scripts: []
skills: - using-superpowers
- user-communication-preferences
- executing-plans
- verification-before-completion
formatter: default
...
plan: ''
dependencies: - skill:using-superpowers
- skill:user-communication-preferences
- skill:executing-plans
- skill:verification-before-completion
tags: - agents
- copilot
- instructions
- prompts
- audit
- fix
trigger: /agents-system-prompt-context-fix
...
---

# Agents System Prompt Context Fix

> Repair prompt/spec correctness only. Do not alter agent behavior beyond correcting instruction/context references.

## Context

- **Workspace root:** `C:\Users\Alexa\Desktop\SandBox`
- **Real assets:**
  - `.github/instructions/*.instructions.md`
  - `.github/agents/*.agent.md`
- **Reference skill:** `agents-system-prompt-context-fix-runner` at `~/AppData/Local/hermes/skills/development/agents-system-prompt-context-fix-runner/SKILL.md`

## Rules

1. Work read-only until a concrete repair target is identified.
2. Do not overwrite intentionally customized copies.
3. Verify repaired artifacts parse as valid markdown/YAML frontmatter.
4. Update `docs/orchestrator-verification.md` evidence table after this phase.

## Phase 1: Inventory

1. List instruction files: `.github/instructions/*.instructions.md`
2. List agent files: `.github/agents/*.agent.md`
3. Capture counts:
   - instructions total
   - agents total
4. Identify obvious parse risks:
   - missing frontmatter fences
   - missing `applyTo` or mismatched YAML
   - broken links to non-existent files

**Verification:** counts recorded; repair candidates listed; no blind rewrites.

---

## Phase 2: Repair Frontmatter & Context References

1. Repair YAML-only issues; do not change prompt body semantics.
2. Fix stale file references to paths that no longer exist in this repo.
3. Normalize instruction/agent cross-refs to repo paths that actually exist.
4. Avoid changing fields like `model`, `tools`, or behavior unless the source material explicitly contradicts execution.

**Verification:** representative sample of repaired files parses; no broken `[text](...)` refs remain on samples.

---

## Phase 3: Finalize Documentation

1. Write `docs/agents-system-prompt-context-fix-report.md` with:
   - totals audited
   - repaired count
   - skipped intentionally-customized copies
   - parser verification method
2. Update `docs/orchestrator-progress.md` Phase 2 section.

**Verification:** report exists; verification artifact updated; no malformed YAML in sampled output.
