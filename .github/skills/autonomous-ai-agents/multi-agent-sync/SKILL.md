---
name: multi-agent-sync
title: Multi-Agent Platform Sync
description: "Sync skills, plugins, hooks, personalities, and profiles across Hermes, Copilot, and Codex/OpenCode agents in a shared workspace. Inventory, map, sync, and verify cross-platform parity at scale."
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  [sync, multi-agent, hermes, copilot, codex, profiles, personalities, workspace]
metadata:
  hermes:
    related_skills:
      - hermes-profiles
      - hermes-skills
      - hermes-hooks
      - profile-maintenance
      - plans-and-specs
      - enhance-markdown
---

## Goal

Synchronize skills, plugins, hooks, personalities, and profiles across multiple AI agent platforms (Hermes, GitHub Copilot, Codex/OpenCode) sharing the same workspace. Produces cross-platform parity with verified deliverables.

## When to Use

- Adding a new AI agent platform to an existing workspace
- Re-syncing after adding/removing skills, hooks, or profiles
- Creating Hermes profiles from Copilot agent definitions
- Normalizing instruction files across platforms
- Workspace audit and consolidation across agent ecosystems

## Architecture

```
Agent Platform Inventory:
  Hermes  →  ~/AppData/Local/hermes/    (skills/, plugins/, hooks/, profiles/)
  Copilot →  .github/                   (instructions/, agents/, hooks/)
  Codex   →  ~/.codex/ or ~/.opencode/  (skills/, agents/, config.toml)

Sync Flow:  Inventory → Map → Sync → Verify
```

## Critical Rules

1. **Sequential phases** — Complete each phase before starting the next
2. **Bidirectional sync** — Assets flow in both directions where format-compatible
3. **Scale-aware grouping** — Group large instruction/agent sets by category; do NOT create 1:1 profiles for 170+ items
4. **Completeness** — Do not stop until verification passes

## Phase 1: Inventory

### 1.1 Scan All Agent Root Directories

| Platform | Check | Expected |
|----------|-------|----------|
| Hermes | `~/AppData/Local/hermes/skills/` | SKILL.md files in category dirs |
| Copilot | `.github/instructions/*.instructions.md` | Instruction markdown files |
| Copilot | `.github/agents/*.agent.md` | Agent definition files |
| Codex | `~/.codex/agents/*.toml` | Agent config TOML files |
| Codex | `~/.codex/skills/` | Skill definitions (often sparse) |

### 1.2 Map Instructions → Personalities

For instruction files (Copilot), create Hermes personality entries in the active profile's `config.yaml` under `agent.personalities:`.

**Scale rule:** With 100+ instruction files, group by functional category rather than creating one personality per file:

```yaml
personalities:
  azure-devops: >-
    Expert in Azure DevOps, Bicep, Terraform, Azure Functions...
  web-frontend: >-
    Expert in React, Next.js, TypeScript, Tailwind CSS...
  # — group by tech stack, not by individual file
```

### 1.3 Map Agents → Profiles

For each agent definition file (Copilot `.agent.md`), create a Hermes profile directory at `~/AppData/Local/hermes/profiles/<name>/`.

**Scale rule:** Create profiles for priority/commonly-used agents first (hermes, arch, planner, debugger, reviewer, spec, etc.) rather than all 170+. Document the full inventory in a reference file.

Minimum profile structure:
```
profiles/<name>/
├── config.yaml    # Minimal agent config
└── SOUL.md        # References the source agent file
```

### 1.4 Personality Entries vs Profile Directories

| Concept | Hermes Mechanism | When to Create |
|---------|-----------------|----------------|
| Personality | `config.yaml > agent.personalities.<name>` | From instruction files (grouped) |
| Profile | `profiles/<name>/` directory | From agent definitions (selective) |

## Phase 2: Root Identification

Confirm all platform root directories exist:

| Step | Action | Output |
|------|--------|--------|
| 2.1 | Check Hermes root | `~/AppData/Local/hermes/` |
| 2.2 | Check Copilot root | `.github/` in workspace |
| 2.3 | Check Codex root | `~/.codex/` or `.opencode/` |

Report MISSING if any root is absent; phased sync is still possible for present platforms.

## Phase 3: Asset Sync

### 3.1 Hook Sync

Hook shell scripts (`hook.sh`) are **directly portable** between Hermes and `.github/hooks/` because both use bash/posix-compatible scripts.

```bash
for hook in session-logger session-auto-commit governance-audit; do
  cp -r ~/AppData/Local/hermes/hooks/$hook/* .github/hooks/$hook/
done
```

### 3.2 Skill Sync

Skills are **NOT directly format-compatible** between platforms:
- Hermes uses `SKILL.md` (YAML frontmatter + markdown body)
- Codex uses `skill.json` / TOML-based definitions
- Copilot uses instruction files (`.instructions.md`)

**Strategy:** Copy Hermes skill categories into a namespace directory under the target platform's skills location (e.g., `~/.codex/skills/hermes-auto/`). Document format difference; actual format conversion is platform-specific.

### 3.3 Plugin Sync

- Only Hermes has a meaningful plugin system (plugins in `~/AppData/Local/hermes/plugins/`)
- Codex may have `~/.codex/plugins/` but this is often a cache directory, not loadable plugins
- Skip if only Hermes has plugins; log as informational

### 3.4 Cross-Reference Document

Write a cross-system asset inventory (see `references/cross-platform-inventory.md`) showing:
```
| Asset | Hermes | Copilot | Codex |
|-------|--------|---------|-------|
| Skills | 83 | 186 instructions | 1 |
| Profiles | 23 | 174 agents | 144 agents |
| Plugins | 4 | — | — |
| Hooks | 2 | 3 stubs | — |
```

## Phase 4: Verify & Implement

### Gates

- [ ] All present platform roots identified
- [ ] Instructions → personalities created (grouped if >50)
- [ ] Agents → profiles created (priority-first strategy)
- [ ] Hooks synced to all platforms that support them
- [ ] Skills synced to target platform namespace
- [ ] Cross-platform inventory document written
- [ ] Verification report produced with zero failures

### Verification Script Pattern

Use `execute_code` with Python to run deterministic checks:
```python
# Check each gate programmatically
results = {"passed": [], "warnings": [], "failed": []}
# ... run checks ...
print(f"PASS: {len(passed)} WARN: {len(warnings)} FAIL: {len(failed)}")
```

## Pitfalls

- **1:1 profile creation at scale**: Creating 170+ profiles for 170+ agents is excessive and clutters the profile directory. Group by category and prioritize.
- **Format incompatibility**: Hermes skills (SKILL.md) ≠ Codex skills (JSON/TOML). Don't claim format compatibility where none exists. Copy into a clearly-namespaced directory.
- **Personality ≠ Profile**: These are different Hermes concepts. Personalities are config.yaml entries for behavior overrides; profiles are full directories with config + SOUL.md. Map instructions → personalities, agents → profiles.
- **Codex plugin hole**: `~/.codex/plugins/cache` is not a plugin system — it's a cache directory. Don't attempt to sync Hermes plugins there.
- **Hermes config.yaml size**: Adding 12+ personality entries to a large config (800+ lines) is fine, but use `patch` or `write_file` — direct terminal sed can corrupt YAML.
- **Incomplete inventory**: Always `ls` the actual directories rather than trusting stale context. Directory contents change.
