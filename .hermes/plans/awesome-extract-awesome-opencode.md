---
title: Awesome Extract Awesome Opencode
description: Plan for Awesome Extract Awesome Opencode
date: 2026-09-07
author: Alexa
status: in_progress
profile: default
model: inclusionai/ling-3.0-flash
---


## Goal

**Awesome Extract Awesome Opencode**

Complete all phases and pass verification gates.

# Hermes-Compatible Extract: awesome-opencode

**Source**: https://github.com/awesome-opencode/awesome-opencode

**Description**: A curated list of plugins, themes, agents, and resources for Opencode

**Totals**: ~44 plugins identified (readable from README)

**Hermes Compatible**: PARTIAL — Opencode uses a different plugin system (plugin.json/extensions) than Hermes. However, many plugins follow similar patterns and some items (skills, MCP servers) may be portable.

**Format**: Opencode plugins (plugin.json), SKILL.md (for skills), .toml (for agents)

**Install Method**: Via Opencode's plugin system (`opencode plugin install`), git clone, or npm

---

## Plugins

- **@bluelovers/opencode-arise** (plugin, awesome-opencode/awesome-opencode) — Lightweight orchestrator harness for OpenCode
- **aerovato/opencode-quotes-plugin** (plugin, awesome-opencode/awesome-opencode) — Inspirational quotes instead of tips
- **gotgenes/opencode-agent-identity** (plugin, awesome-opencode/awesome-opencode) — Agent self-identity and per-message attribution
- **joshuadavidthomas/opencode-agent-memory** (plugin, awesome-opencode/awesome-opencode) — Letta-inspired persistent memory
- **joshuadavidthomas/opencode-agent-skills** (plugin, awesome-opencode/awesome-opencode) — Dynamic skills loader
- **NoeFabris/opencode-antigravity-auth** (plugin, awesome-opencode/awesome-opencode) — Google Antigravity models auth
- **theblazehen/opencode-antigravity-multi-auth** (plugin, awesome-opencode/awesome-opencode) — Multiple Google accounts auth
- **pawelma/opencode-autotitle** (plugin, awesome-opencode/awesome-opencode) — AI-powered automatic session naming
- **zenobi-us/opencode-background** (plugin, awesome-opencode/awesome-opencode) — Background process management
- **kdcokenny/opencode-background-agents** (plugin, awesome-opencode/awesome-opencode) — Claude Code-style background agents
- **opencode-beads** (plugin, awesome-opencode/awesome-opencode) — Beads issue tracker integration
- **ZanzyTHEbar/brhp** (plugin, awesome-opencode/awesome-opencode) — Persistent planning state
- **kenryu42/claude-code-safety-net** (plugin, awesome-opencode/awesome-opencode) — Safety net catching destructive commands
- **JasonLandbridge/opencode-ccs-sync** (plugin, awesome-opencode/awesome-opencode) — Claude Code Switch to OpenCode sync
- **shihyuho/opencode-command-inject** (plugin, awesome-opencode/awesome-opencode) — Auto-inject project commands
- **IgorWarzocha/Opencode-Context-Analysis-Plugin** (plugin, awesome-opencode/awesome-opencode) — Token usage analysis
- **xberg-io/plugins** (plugin, awesome-opencode/awesome-opencode) — Crawlberg, HTML to Markdown, liter-llm
- **CrewBeeLab/CrewBee** (plugin, awesome-opencode/awesome-opencode) — Task-specific Agent Teams
- **athal7/opencode-devcontainers** (plugin, awesome-opencode/awesome-opencode) — Multi-branch devcontainers
- **simonwjackson/opencode-direnv** (plugin, awesome-opencode/awesome-opencode) — Load direnv variables
- **dodopayments/dodo-agent-plugin** (plugin, awesome-opencode/awesome-opencode) — Payments, subscriptions, billing
- **Tarquinen/opencode-dynamic-context-pruning** (plugin, awesome-opencode/awesome-opencode) — Optimize token usage
- **ejentum/ejentum-mcp** (plugin, awesome-opencode/awesome-opencode) — MCP server with reasoning, code, memory tools
- **boxpositron/envsitter-guard** (plugin, awesome-opencode/awesome-opencode) — Prevent .env leaks
- **DVNghiem/FlowDeck** (plugin, awesome-opencode/awesome-opencode) — Multi-agent workflow orchestration
- **forloop-cc/forloop-opencode-plugin-planner** (plugin, awesome-opencode/awesome-opencode) — Autopilot development planner
- **smartfrog/opencode-froggy** (plugin, awesome-opencode/awesome-opencode) — Hooks and specialized agents
- **jenslys/opencode-gemini-auth** (plugin, awesome-opencode/awesome-opencode) — Google account auth
- **amestsantim/opencode-github-release** (plugin, awesome-opencode/awesome-opencode) — Automated GitHub releases
- **IgorWarzocha/Opencode-Google-AI-Search-Plugin** (plugin, awesome-opencode/awesome-opencode) — Query Google AI Mode
- **hffmnnj/opencode-goopspec** (plugin, awesome-opencode/awesome-opencode) — Spec-driven development workflow
- **yuji-hatakeyama/opencode-gpt-imagegen** (plugin, awesome-opencode/awesome-opencode) — gpt-image-2 in OpenCode
- **joshuadavidthomas/opencode-handoff** (plugin, awesome-opencode/awesome-opencode) — Session handoff prompts
- **smc2315/harness-memory** (plugin, awesome-opencode/awesome-opencode) — Persistent project memory
- **HiAi-gg/hiai-opencode** (plugin, awesome-opencode/awesome-opencode) — 12-agent model with bundled skills
- **plastic-labs/opencode-honcho** (plugin, awesome-opencode/awesome-opencode) — AI-native long-term memory
- **Kibi stack** (plugin, awesome-opencode/awesome-opencode) — Repo-local branch-scoped knowledge
- **JungHoonGhae/opencode-kilo-auth** (plugin, awesome-opencode/awesome-opencode) — Kilo Gateway provider
- **Lemma** (plugin, awesome-opencode/awesome-opencode) — Persistent memory layer via MCP
- **cortexkit/opencode-magic-context** (plugin, awesome-opencode/awesome-opencode) — Lossless context management
- **Ranroids-Dojo/ManageSkills** (plugin, awesome-opencode/awesome-opencode) — Wizard-driven skills management
- **vtemian/micode** (plugin, awesome-opencode/awesome-opencode) — Brainstorm-Plan-Implement workflow
- **ramarivera/opencode-model-announcer** (plugin, awesome-opencode/awesome-opencode) — Model self-awareness
- **Jedrick/opencode-morph-fast-apply** (plugin, awesome-opencode/awesome-opencode) — 10,500+ tokens/sec code editing

## Notes

Opencode's plugin ecosystem uses its own extension format. While not natively Hermes-compatible (Hermes uses SKILL.md and plugin.yaml), several items like MCP servers, skills, and agent definitions could potentially be adapted. The `agentskills.io` ecosystem items listed here are cross-platform and may work with Hermes.

**Key cross-compatible items**: opencode-agent-skills (dynamic skills loader), opencode-agent-memory (Letta-inspired), opencode-agent-identity, and any agentskills.io-standard items.

## Phase 1

- **Gate**: All tasks in this phase complete and verified.


## Phase 2

- **Gate**: All tasks in this phase complete and verified.


## Phase 3

- **Gate**: All tasks in this phase complete and verified.


## Linked Specs
- .hermes/specs/master-spec.md

## Risks

| Risk | Likelihood | Impact |
|------|-----------|--------|
| Scope creep | Medium | Medium |
| Dependencies change | Low | High |
| Timeline slippage | Medium | Medium |


## Files to Create/Modify

- Plan file itself (updated)

## Verification

- All phase gates pass
- All tasks completed with dependencies satisfied
- Spec coupling verified via ## Linked Specs
- .hermes/specs/master-spec.md

## Status

- [ ] Phase 1 complete
- [ ] Phase 2 complete
- [ ] Phase 3 complete
- [ ] Verification passed


## Linked Plan

- [../specs/master-spec.md](../specs/master-spec.md) — Master Spec
