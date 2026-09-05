---
name: plugins-hooks-audit
description: Audit Hermes plugin + hook event coverage. Run when checking which plugins are enabled, which hook events have shell scripts wired, and which events exist in code but have no hook.
trigger: /plugins-hooks-audit
category: general
version: 1.0.0
author: Hermes Agent
license: MIT
tags: 
metadata: 
hermes: 
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
title: Plugins + Hooks Audit
---

# Plugin + Hook Audit

Run a comprehensive audit of Hermes Agent's plugin and hook coverage.

## Steps

1. **Run the audit script**:
   ```bash
   python scripts/plugins_hooks_audit.py --out .hermes/plans/plugins-hooks-audit-$(date +%Y-%m-%d)
   ```

2. **Review the report** at `.hermes/plans/plugins-hooks-audit-YYYY-MM-DD/report.md`:
   - Plugin count + which have plugin.yaml
   - Possible events (from Hermes source) vs shell hooks registered (in config.yaml)
   - Missing event coverage (events that exist in code but have no shell hook)

3. **Cross-validate**:
   ```bash
   hermes plugins list --plain | wc -l
   hermes hooks list | grep -E "^\s*\[" | wc -l
   ```
   These should match the report counts.

4. **For each missing event**, decide:
   - Is it a real dispatcher in code? (grep source for `emit("event_name")`)
   - If yes and needed: add to `~/AppData/Local/hermes/config.yaml` hooks block
   - If false positive: update regex in `scripts/plugins_hooks_audit.py`

5. **Verify**:
   ```bash
   hermes hooks list    # shows all registered events with their commands
   hermes hooks doctor  # checks allowlist health
   ```

## Key Distinction

Hermes has TWO hook systems:
- **Shell hooks** — external scripts in `config.yaml`. Currently 6 events supported.
- **Plugin hooks** — Python callbacks in plugin code. ~8 events.

The audit reports both. Missing plugin-internal events are informational, not bugs.

## Output

- `report.json` — machine-readable audit data
- `report.md` — human-readable tables and lists

## Verification

## Goal
Audit Hermes plugin + hook event coverage. Run when checking which plugins are enabled, which hook events have shell scripts wired, and which events exist in code but have no hook.

## Context

## Workflow

<content>

<content>

<content>

- [ ] Script exits 0
- [ ] Report files exist
- [ ] Counts match `hermes plugins list` and `hermes hooks list`
- [ ] No unexpected missing events

See `~/AppData/Local/hermes/skills/devops/plugins-hooks-audit/SKILL.md` for the full skill.
```
# Prompt template
Execute the workflow defined in this file.
```
