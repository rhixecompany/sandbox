---
title: Command Cross-Reference — Copilot, Hermes, OpenCode
description: Maps all command definitions across three platforms with trigger names, locations, and purpose.
tags: [commands, copilot, hermes, opencode, cross-reference]
---

# Command Cross-Reference

## Overview

Comprehensive inventory of all command definitions across Copilot, Hermes, and OpenCode platforms used in this workspace.

Commands are defined as prompt files with `trigger:` fields — they act as slash commands that can be invoked in AI chat sessions.

---

## Platform Inventory

### Copilot — `.github/prompts/` (8 commands)

| Trigger | File | Purpose |
|---------|------|---------|
| `/ai-prompt-engineering-safety-review` | `.github/prompts/ai-prompt-engineering-safety-review.prompt.md` | Security/safety review for AI prompts |
| `/boost-prompt` | `.github/prompts/boost-prompt.prompt.md` | Optimize prompts for AI response quality |
| `/context-map` | `.github/prompts/context-map.prompt.md` | Create/maintain project context map |
| `/convert-plaintext-to-md` | `.github/prompts/convert-plaintext-to-md.prompt.md` | Convert plaintext → markdown documentation |
| `/generator-orchestrator` | `.github/prompts/generator-orchestrator.prompt.md` | Orchestrate blueprint generators |
| `/prompt-builder` | `.github/prompts/prompt-builder.prompt.md` | Build prompts from templates |
| `/skills-debug-prompt` | `.github/prompts/skills-debug-prompt.prompt.md` | Execute skills debug fix plan |
| `/update-implementation-plan` | `.github/prompts/update-implementation-plan.prompt.md` | Update plan with current progress |

**Format:** `.prompt.md` with YAML frontmatter (trigger, description, tags, dependencies, skills).
**Location:** Project-specific (`SandBox/.github/prompts/`)

### Hermes / Prompt Library — `Prompts/` (8 commands)

| Trigger | File | Purpose |
|---------|------|---------|
| `/agents-fix` | `Prompts/agents-fix.prompts.md` | Sync agent definitions across 3 platforms |
| `/bash-scripts-fix` | `Prompts/bash-scripts-fix.prompts.md` | Modernize and consolidate scripts |
| `/commands-fix` | `Prompts/commands-fix.prompts.md` | Sync command definitions across 3 platforms |
| `/dev-init` | `Prompts/dev-init.prompts.md` | Plan and implement prompt library standardization |
| `/general` | `Prompts/general.prompts.md` | General development workflow |
| `/repo` | `Prompts/repo.prompts.md` | Consolidate projects into rhixecompany-comics |
| `/skills-fix` | `Prompts/skills-fix.prompts.md` | Audit, debug, enhance Hermes skills |
| `/workspace-consolidate` | `Prompts/workspace-consolidate.prompts.md` | Consolidate scripts, patches, docs |

**Format:** `.prompts.md` with YAML frontmatter (trigger, description, tags) + skills list + phases.
**Location:** Project-specific (`SandBox/Prompts/`)

### OpenCode — Config & Rules (1 custom + 22 instruction files)

| Command | Location | Type |
|---------|----------|------|
| `mystatus` | `~/.config/opencode/opencode.json` | Custom (description + template) |
| 22 instruction files | `~/.config/opencode/rules/*.md` | Session-start instructions |
| 18 plugins | `~/.config/opencode/opencode.json` → `plugin` array | Plugin-provided commands |

**Instruction files loaded on session start:**
- building.md, code-review.md, commit-messages.md, context7.md, custom-instructions.md
- debugging.md, documentation.md, github-automation.md, github-session-limits.md, memory-bank.md
- nextjs-tailwind.md, performance.md, planning.md, playwright-typescript.md, process-workflows.md
- security.md, sequential-thinking.md, system-control.md, task-implementation.md, tasksync.md
- testing.md, typescript.md

**Format:** JSON config (`"command"` section) + `.md` instruction files with YAML frontmatter.
**Location:** Global (`~/.config/opencode/`)

---

## Cross-Reference Matrix

### Overlap Between Platforms

| Function | Copilot (.github/prompts/) | Hermes (Prompts/) | OpenCode |
|----------|---------------------------|-------------------|----------|
| Plaintext→MD conversion | `/convert-plaintext-to-md` | — | — |
| Skills debugging | `/skills-debug-prompt` | `/skills-fix` | — |
| Prompt enhancement | `/boost-prompt` | — | — |
| Context mapping | `/context-map` | — | — |
| Prompt building | `/prompt-builder` | — | — |
| Implementation plans | `/update-implementation-plan` | — | — |
| Safety review | `/ai-prompt-engineering-safety-review` | — | — |
| Generator orchestration | `/generator-orchestrator` | — | — |
| Agent sync | — | `/agents-fix` | — |
| Script consolidation | — | `/bash-scripts-fix` | — |
| Command sync | — | `/commands-fix` | — |
| Dev init | — | `/dev-init` | — |
| General dev | — | `/general` | — |
| Repo consolidation | — | `/repo` | — |
| Workspace consolidation | — | `/workspace-consolidate` | — |
| Usage monitoring | — | — | `mystatus` |

### Key Observations

1. **Zero overlap** — No single command exists on more than one platform. Each platform has its own exclusive set.
2. **Copilot = prompt engineering tools** — All 8 commands focus on prompt creation, review, and enhancement.
3. **Hermes/Prompts = workspace automation** — All 8 commands focus on sync, consolidation, and fixes.
4. **OpenCode = custom + infrastructure** — Single custom command plus 22 rules files and 18 plugins.
5. **Different naming conventions** — Copilot uses descriptive names (`ai-prompt-engineering-safety-review`), Hermes uses short names (`agents-fix`), OpenCode uses single-word plugin names.

### Coverage Gaps

| Area | Missing On |
|------|-----------|
| Usage / cost monitoring | Copilot, Hermes |
| Workspace automation | Copilot, OpenCode |
| Prompt engineering | Hermes, OpenCode |
| Code quality / safety review | Hermes, OpenCode |
| Agent management | Copilot, OpenCode |
| Documentation generation | Copilot (partial), Hermes, OpenCode |

---

## Recommendations

1. **Add cross-references in copilot-instructions.md** — Already done in agents-fix agent table. Add command reference too below it.
2. **Keep platform-native formats** — `.prompt.md` vs `.prompts.md` distinction is intentional (Copilot vs Hermes/OpenCode conventions).
3. **Document commands in AGENTS.md** — Add a section listing available commands and their locations.
4. **Consider merging overlapping functionality** — `/skills-fix` (Hermes) and `/skills-debug-prompt` (Copilot) serve similar purposes. Merge into one where possible.

---

## File Locations

```
# Copilot prompt commands (triggers via /command)
.github/prompts/*.prompt.md

# Hermes/prompt library commands (triggers via /command)
Prompts/*.prompts.md

# OpenCode custom commands
~/.config/opencode/opencode.json  → "command" section
~/.config/opencode/rules/*.md      → session-start instruction files

# AGENTS.md (command documentation reference)
AGENTS.md
```
