---
name: sync-hermes-copilot-codex
title: Sync Hermes Copilot Codex
project_path: C:\Users\Alexa\Desktop\SandBox
description: Inventory repository instruction/agent assets; identify root templates and derived assets; sync corrective diffs from root to derived assets; run verification; do not overwrite intentionally customized copies unless explicitly authorized.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets: - file - terminal - browser - skills
scripts: []
skills: - using-superpowers - user-communication-preferences - plans-and-specs - executing-plans - verification-before-completion - subagent-driven-development
formatter: default
plan: |
  ### Phase 1: Asset Inventory
  - List repository asset directories:
    - `.github/instructions/*.instructions.md`
    - `.github/agents/*.agent.md`
  - For each, capture: file path, size, frontmatter fields, last modified
  - Store inventory data in `docs/inventory/assets-inventory.json`

  ### Phase 2: Root Template Analysis
  - Identify root templates (non-derived):
    - By examining naming patterns: base templates vs. versioned copies
    - Check if derived assets reference root templates via frontmatter
    - Determine which assets need syncing: those not customized

  ### Phase 3: Diff Generation & Apply
  - For non-customized assets:
    - Generate unified diff between root and derived asset
    - If diff exists and changes are corrective (not breaking), apply to derived asset
  - Log applied diffs in `docs/audit/sync-application-log.json`

  ### Phase 4: Verification & Reporting
  - After sync, re-run inventory to verify consistency
  - Generate report: `docs/sync/sync-summary.md`
  - Include: assets inventoried, syncs applied, assets left unchanged

  ### Phase 5: Safety Validation
  - Ensure no intentional customizations were overwritten
  - For any overwritten files, move to backup: `assets/<name>.backup.<timestamp>`
  - Log all backup actions in sync log

dependencies: - skill:using-superpowers - skill:user-communication-preferences - skill:plans-and-specs - skill:executing-plans - skill:verification-before-completion - skill:subagent-driven-development
tags: - inventory - sync - safe-sync - prompts
trigger: /sync-hermes-copilot-codex
metadata:
  related_skills: [using-superpowers, user-communication-preferences, plans-and-specs, executing-plans, verification-before-completion, subagent-driven-development]
  workspace_path: C:\Users\Alexa\Desktop\SandBox
  inventory_output_dir: C:\Users\Alexa\Desktop\SandBox\docs\inventory
  audit_log_dir: C:\Users\Alexa\Desktop\SandBox\docs\audit
  sync_log_dir: C:\Users\Alexa\Desktop\SandBox\docs\sync
---

# Sync Hermes Copilot Codex

## Overview

Synchronize derived instruction/agent assets (`.github/instructions/*.instructions.md` and `.github/agents/*.agent.md`) with their root templates to maintain consistency while respecting intentional customizations.

## Phase 1: Asset Inventory

1. **List asset directories**
   - Execute: `ls -la .github/instructions/` → capture files with `*.instructions.md`
   - Execute: `ls -la .github/agents/` → capture files with `*.agent.md`

2. **Collect metadata**
   - For each asset, extract: filename, size, frontmatter sections, last modified timestamp
   - Write structured inventory: `docs/inventory/assets-inventory.json`

3. **Classify assets**
   - **Root templates**: Non-derived, base implementations
   - **Derived assets**: Copy/references to root templates
   - **Custom assets**: Deliberate modifications marked as such

## Phase 2: Root Template Analysis

1. **Identify root templates**
   - Determine which files are source templates (e.g., `design-patterns.agent.md` vs. `design-patterns-v2.agent.md`)
   - Analyze frontmatter for template references: `template: design-patterns.agent.md`

2. **Determine sync candidates**
   - Assets without customization markers
   - Those with clear root template references
   - Assets matching root naming but with minor version suffixes

## Phase 3: Diff Generation & Apply

1. **Generate diffs for candidates**
   - For each candidate derived asset, generate diff against root template
   - Use diff tool: `diff -u root.md derived.md` → analysis

2. **Apply corrective diffs**
   - If root → derived has only formatting/legal/copyright updates, apply to derived
   - Log applied diffs in `docs/audit/sync-application-log.json` with action details

3. **Handle intentional customizations**
   - If diff indicates substantive changes or customizations, skip syncing
   - Move the derived file to backup: `assets/<name>.backup.<timestamp>`

## Phase 4: Verification & Reporting

1. **Re-inventory after sync**
   - Run Phase 1 steps again to confirm inventory consistency
   - Generate `docs/sync/sync-summary.md` with stats: total assets, syncs applied, assets unchanged

2. **Generate quality report**
   - Document any custom assets that were preserved
   - List assets that remain divergent after sync (intentional content)

## Phase 5: Safety Validation

1. **Custom backup preservation**
   - For assets that were NOT synced (intentional customizations), ensure backups exist
   - Verify backups: `assets/<name>.backup.<timestamp>` maintained

2. **Log completeness**
   - For each operation, record: operation type, source file, target file, outcome (applied/skipped/backup)
   - Include timestamps and reasoning for each decision

## Exit Condition

Sync completes when:

- All inventory assets documented and classified
- All corrective diffs applied successfully
- Customizations preserved with proper backups
- Verification report generated and audit logs finalized
- Sync summary shows all assets in expected states

## Notes

- Use `diff` tool for comparing asset contents
- Assume incremental changes; bulk regeneration not required
- Prioritize safety: never overwrite intentional customizations
- Detailed logging required for audit and reproducibility
- Use `docs/` directory structure for all outputs (inventory, audit, sync)
