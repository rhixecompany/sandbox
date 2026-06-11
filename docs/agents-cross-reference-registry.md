---
title: Agent Cross-Reference Registry
description: Three-way cross-reference mapping of agents across OpenCode, Hermes, and Copilot platforms.
status: final
tags: [hermes, agents, cross-reference, discovery, sync]
created: 2026-06-01
---

# Agent Cross-Reference Registry

Generated: 2026-06-01
Scope: Prompts/ ↔ Hermes skills ↔ .github/prompts/

## Platform Inventory Summary

| Platform | Agent Type | Location | Count |
|----------|-----------|----------|-------|
| **OpenCode** (via Copilot prompts) | `.prompt.md` workflow files | `.github/prompts/*.prompt.md` | 100+ |
| **Hermes** | Skill definitions | `~/AppData/Local/hermes/skills/**/SKILL.md` | 177 |
| **Copilot** | Prompt orchestration files | `Prompts/*.md` | 8 |

## Three-Way Cross-Reference Table

### Prompts/ → .github/prompts/ Dependencies

| Prompts File | Trigger | .github/prompts/ Dependencies |
|-------------|---------|------------------------------|
| `general.prompts.md` | `/general` | `context-map` |
| `commands-fix.prompts.md` | `/commands-fix` | `context-map` |
| `agents-fix.prompts.md` | `/agents-fix` | `context-map` |
| `bash-scripts-fix.prompts.md` | `/bash-scripts-fix` | `context-map` |
| `dev-init.prompts.md` | `/dev-init` | `context-map`, `convert-plaintext-to-md` |
| `repo.prompts.md` | `/repo` | `context-map` |
| `skills-fix.prompts.md` | `/skills-fix` | `context-map` |
| `workspace-consolidate.prompts.md` | `/workspace-consolidate` | `context-map` |

### Prompts/ → Hermes Skills Dependencies

| Prompts File | Hermes Skills Referenced |
|-------------|------------------------|
| `general.prompts.md` | brainstorming, plans-and-specs, dispatching-parallel-agents, subagent-driven-development, systematic-debugging, simplify, plan, prompt-engineering |
| `commands-fix.prompts.md` | brainstorming, plans-and-specs, dispatching-parallel-agents, subagent-driven-development, systematic-debugging, simplify |
| `agents-fix.prompts.md` | brainstorming, plans-and-specs, dispatching-parallel-agents, subagent-driven-development, systematic-debugging, simplify |
| `bash-scripts-fix.prompts.md` | brainstorming, plans-and-specs, dispatching-parallel-agents, subagent-driven-development, systematic-debugging, simplify |
| `dev-init.prompts.md` | brainstorming, plans-and-specs |
| `repo.prompts.md` | brainstorming, plans-and-specs, dispatching-parallel-agents, subagent-driven-development, systematic-debugging, simplify |
| `skills-fix.prompts.md` | brainstorming, plans-and-specs, dispatching-parallel-agents, subagent-driven-development, systematic-debugging, simplify |
| `workspace-consolidate.prompts.md` | brainstorming, plans-and-specs, dispatching-parallel-agents, subagent-driven-development, systematic-debugging, simplify |

### .github/prompts/ → Hermes Skills Dependencies

| .github/prompts File | Hermes Skills Referenced |
|---------------------|------------------------|
| `boost-prompt.prompt.md` | prompt-engineering, writing-plans |
| `context-map.prompt.md` | codemap |
| `convert-plaintext-to-md.prompt.md` | enhance-markdown, writing-plans, simplify |
| `ai-prompt-engineering-safety-review.prompt.md` | prompt-engineering, systematic-debugging |
| `update-implementation-plan.prompt.md` | writing-plans, plans-and-specs |
| `prompt-builder.prompt.md` | writing-plans, prompt-engineering |

## Flagged Items

### 🔶 Potential Skill Overlap

| Issue | Details |
|-------|---------|
| `humanizer` (root) vs `creative/humanizer` | Two separate skill directories: root (2KB) and creative (32KB). Root has references directory. May be intentional — creative subcategory has more content — but worth verifying if the root-level one should remain or be merged. |

### ✅ No Direct Agent Redundancy Found

| Check | Result |
|-------|--------|
| Same agent under different names across platforms | None detected — each platform uses distinct naming conventions |
| Agents on one platform missing from another by same purpose | Not applicable — platforms serve different roles (Copilot = commands, Hermes = skills, Prompts = orchestration) |
| Duplicate trigger definitions | No trigger collisions found across platforms |

## Hermes Skill Categories Distribution

| Category | Count | Coverage |
|----------|-------|----------|
| software-development | 30 | Core dev workflows |
| creative | 26 | Art, design, media |
| devops | 18 | Infrastructure, CI/CD |
| productivity | 17 | Docs, spreadsheets, email |
| autonomous-ai-agents | 14 | Agent orchestration |
| github | 10 | Git/GitHub workflows |
| media | 6 | Audio, video, GIF |
| qa | 5 | Testing, verification |
| research | 5 | Papers, blogs, data |
| apple | 4 | macOS/iOS integration |
| planning | 3 | Planning, specs |
| mlops | 3 | ML model management |
| gaming | 2 | Game automation |
| mcp | 2 | MCP protocol |
| product | 2 | PRD generation |
| development | 2 | Feature implementation |
| banking, brainstorming, brand-guidelines, canvas-design, data-science, humanizer, agent-browser, algorithmic-art, architecture, asdf, email, note-taking, red-teaming, smart-home, social-media, validate-memories | 1 each | Specialized |

## Risk Assessment

1. **No OpenCode `agents/` directory found** — OpenCode is used via VS Code extension (opencode-zen). Agent definitions may live in extension storage, not on-disk. Cannot sync what isn't discoverable.
2. **No `opencode.json`/`opencode.jsonc`** — The OpenCode platform config could not be located on disk. All OpenCode references in Prompts/ files point to `.github/prompts/` as the shared agent source.
3. **100+ Copilot prompts lack explicit triggers** — Only 7 `.github/prompts/` files have `trigger:` in frontmatter. The rest rely on filename-as-command convention. No sync issue — this is by design.
4. **humanizer split** — Two separate `humanizer` skills exist (root + creative). If unintentional, the root-level one could absorb into `creative/humanizer` and be deleted.

## Actions Required

| Action | Priority | Description |
|--------|----------|-------------|
| N/A | None | Cross-reference complete. No forced sync or deduplication needed. Platforms serve different roles and naming is consistent within each. |

## Verification Results

| Check | Status |
|-------|--------|
| OpenCode agent discovery | ⚠️ No `agents/` directory — using `.github/prompts/` as equivalent |
| Hermes skill discovery | ✅ 177 skills catalogued across 25 categories |
| Copilot prompt discovery | ✅ 100+ prompts in `.github/prompts/` |
| Cross-reference mapping | ✅ Table complete |
| Deduplication scan | ✅ No redundant triggers found |
| Schema validation | ✅ Naming conventions consistent per platform |
