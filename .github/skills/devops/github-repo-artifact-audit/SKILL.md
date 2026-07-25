---
name: github-repo-artifact-audit
description: >
  Audit repo-side GitHub artifacts under .github/ for drift, stale paths, hook/plugin wrappers,
  workflow assumptions, approvals/archive state, and safe-vs-destructive edit triage.
  Use when asked to review .github scripts, workflows, instructions, hooks, plugins,
  approvals, archive state, or stale references in a monorepo/workspace.
tags:
  - github
  - audit
  - hooks
  - plugins
  - workflows
  - drift
title: GitHub Repo Artifact Audit
version: 1.0.0
---

# GitHub Repo Artifact Audit

Class-level skill for auditing root-level .github repo artifacts and producing actionable triage.

## When to Use

- The user asks to audit .github scripts, workflows, instructions, hooks, plugins,
  approvals, archive state, or stale paths.
- You need to distinguish repo-side wrappers/docs from live Hermes or runtime artifacts.
- You need safe-vs-destructive change gating for .github/ edits.

## When NOT to Use

- Local Hermes hook-tree only audits; use hermes-hooks.
- Monorepo instruction precedence audits without workflow concerns; use customization-audit.

## Workflow

### 1. Enumerate repo-side artifacts

Scan:
- .github/scripts/ — shell, Python, or PowerShell wrappers and auditors
- .github/workflows/*.yml and *.md
- .github/copilot-instructions.md and any root .github/*.md
- .github/agents/, .github/instructions/, .github/prompts/, .github/skills/
- .github/approvals/, .github/archive/, .github/archived/, and similar state directories

### 2. Classify hook and plugin references

For each reference, identify its target:
- Repo-local path under .github/...
- Local Hermes runtime path under LOCALAPPDATA/hermes/hooks or LOCALAPPDATA/hermes/plugins
- External assumption such as plugins/**, .github/plugin/plugin.json, or materialization scripts

### 3. Detect stale paths and assumptions

Common stale-pattern checklist:
- .github/hooks referenced when live hooks are under LOCALAPPDATA/hermes/hooks
- plugins/** globs or plugin materialization refs when no plugins/ tree exists in the repo
- Workflows that forbid .github/** contribution changes in PR paths
- Counts in copilot-instructions.md that diverge from filesystem counts
- Paths in instructions that reference sibling project names incorrectly

### 4. Determine archive and approval state

Check for:
- Presence or absence of .github/approvals/, .github/archive/, .github/archived/
- .disabled workflow naming conventions in subprojects as a proxy for stale artifacts
- Any explicit archive or approval policy references in root docs

### 5. Classify change risk

- Low risk: documentation counts, descriptions, or adding canonical assets under existing .github/ directories
- High risk: removing plugin materialization logic, bulk deletion or rename of scripts or workflows,
  or introducing new .github/* directory semantics

### 6. Surface approval requirements

- Edit copilot-instructions.md: repo PR review
- Add or modify .github/scripts/* auditors or wrappers: repo PR review
- Edit .github/workflows/*.yml affecting plugin or materialization gates: repo PR plus owner confirmation
- New .github/* directory semantics: owner sign-off

## Output Shape

Return a concise report containing:
1. Inventory tables by artifact type
2. Stale-path findings with exact files and issues
3. Safe vs destructive change guidance
4. Approval requirements per change type

Store session-specific detail under references/ when the audit is non-trivial.

## Pitfalls

- Do not assume every .github/workflows/*.yml describes live repo state; some describe external or plugin pipelines.
- Do not treat subproject .disabled workflows as repo-root .github/archive/ equivalents without explicit naming.
- Do not conflate local Hermes runtime audits with repo-side audits; use the right skill for each layer.
- Do not edit protected or manually-authored skills from another tool layer; record lessons in this class-level skill instead.
