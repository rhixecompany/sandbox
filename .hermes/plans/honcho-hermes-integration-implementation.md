---
name: honcho-hermes-integration-implementation
title: Honcho + Hermes Agent Integration Implementation Plan
description: Comprehensive implementation plan for integrating Honcho persistent memory with Hermes Agent, covering context files, personality system, and all documented features
version: 1.0.0
author: Alexa
license: MIT
tags:
  - honcho
  - hermes
  - memory
  - integration
  - planning
---

# Honcho + Hermes Agent Integration Implementation Plan

## Overview

This plan consolidates all documentation from:
- Honcho documentation index (https://honcho.dev/docs/llms.txt)
- Hermes Honcho Memory feature docs (https://hermes-agent.nousresearch.com/docs/user-guide/features/honcho)
- Hermes Context Files docs (https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)
- Hermes Personality/SOUL.md docs (https://hermes-agent.nousresearch.com/docs/user-guide/features/personality)

## Phase 1: Honcho Setup & Configuration

### 1.1 Install & Configure Honcho Memory Provider
- [ ] Run `hermes memory setup` and select "honcho"
- [ ] Enter Honcho base URL (cloud: https://api.honcho.dev or self-hosted: http://localhost:8000)
- [ ] Provide API key (cloud) or JWT token (self-hosted)
- [ ] Verify with `hermes memory status`

### 1.2 Configure Honcho Settings in `~/.honcho/config.json` or `$HERMES_HOME/honcho.json`
- [ ] Set `recallMode`: `hybrid` (default) — auto-inject + tools
- [ ] Set `contextCadence`: `1` — refresh base context every turn
- [ ] Set `dialecticCadence`: `2` — run dialectic every 2 turns (recommended 1-5)
- [ ] Set `dialecticDepth`: `1` — single pass (can increase to 2-3 for deeper reasoning)
- [ ] Set `dialecticReasoningLevel`: `low` (options: minimal, low, medium, high, max)
- [ ] Set `dialecticDynamic`: `true` — allow model to override reasoning level per-call
- [ ] Set `contextTokens`: `1200` — cap auto-injected context
- [ ] Set `writeFrequency`: `async` — background flush (options: async, turn, session, integer N)
- [ ] Set `sessionStrategy`: `per-directory` — maps sessions to working directory
- [ ] Set `observationMode`: `directional` — full mutual observation

### 1.3 Self-Hosted Honcho (if applicable)
- [ ] Follow Self-Hosting Guide at https://honcho.dev/docs/v3/contributing/self-hosting
- [ ] Use elkimek/honcho-self-hosted for one-command installer
- [ ] Configure `AUTH_JWT_SECRET` and `AUTH_USE_AUTH=false` if needed
- [ ] Run `hermes honcho setup` for local JWT/bearer token

### 1.4 Verify Integration
- [ ] Run `hermes honcho status` — should show connection status, config, key settings
- [ ] Test fact storage: "My favorite language is Rust and I use dark mode"
- [ ] Start new session, ask "What do you know about my preferences?" — should recall Rust/dark mode
- [ ] Test tool calling: "Use honcho_search to find anything about me"

## Phase 2: Context Files Implementation

### 2.1 SOUL.md (Global Personality)
- [ ] Create/edit `~/.hermes/SOUL.md` (or `$HERMES_HOME/SOUL.md`)
- [ ] Define durable voice/personality (not project-specific)
- [ ] Example structure:
  ```
  # Personality
  You are a pragmatic senior engineer with strong taste.
  
  ## Style
  - Be direct without being cold
  - Prefer substance over filler
  - Push back when something is a bad idea
  - Admit uncertainty plainly
  - Keep explanations compact unless depth is useful
  
  ## What to avoid
  - Sycophancy
  - Hype language
  - Repeating the user's framing if it's wrong
  ```
- [ ] Verify loads at slot #1 of system prompt

### 2.2 AGENTS.md (Project Context)
- [ ] Create `AGENTS.md` at git root (highest priority project context)
- [ ] Add nested `AGENTS.md` in subdirectories for progressive discovery
- [ ] Example structure:
  ```
  # Project Context
  This is a Next.js 14 web application with Python FastAPI backend.
  
  ## Architecture
  - Frontend: Next.js 14 with App Router in /frontend
  - Backend: FastAPI in /backend, uses SQLAlchemy ORM
  - Database: PostgreSQL 16
  - Deployment: Docker Compose on Hetzner VPS
  
  ## Conventions
  - Use TypeScript strict mode for all frontend code
  - Python code follows PEP 8, use type hints everywhere
  - All API endpoints return JSON with {data, error, meta} shape
  ```
- [ ] Test progressive discovery by navigating into subdirectories

### 2.3 Context File Discovery Chain
- [ ] Verify priority order: `.hermes.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules`
- [ ] Only ONE project context type loaded per session (first match wins)
- [ ] SOUL.md always loaded independently from `HERMES_HOME`
- [ ] Test with `context_file_max_chars` limit (default: dynamic 20k-500k)
- [ ] Verify truncation markers appear correctly

### 2.4 Security Scanning
- [ ] Confirm prompt injection scanner active
- [ ] Test blocked patterns: `<!-- ignore instructions -->`, `<div style="display:none">`, `curl ... $API_KEY`, `cat .env`
- [ ] Verify blocked files show: `[BLOCKED: AGENTS.md contained potential prompt injection...]`

## Phase 3: Personality System Implementation

### 3.1 Built-in Personalities
- [ ] Test `/personality` command lists all 14 built-in personalities:
  - helpful, concise, technical, creative, teacher, kawaii, catgirl, pirate, shakespeare, surfer, noir, uwu, philosopher, hype
- [ ] Test switching: `/personality concise`, `/personality technical`, etc.
- [ ] Verify overlay applies on next message

### 3.2 Custom Personalities in Config
- [ ] Add custom personalities to `~/.hermes/config.yaml` under `agent.personalities`:
  ```yaml
  agent:
    personalities:
      codereviewer: |
        You are a meticulous code reviewer. Identify bugs, security issues,
        performance concerns, and unclear design choices. Be precise and constructive.
  ```
- [ ] Test switching: `/personality codereviewer`
- [ ] Verify stored in `display.personality`

### 3.3 Personality Overlay vs SOUL.md
- [ ] Confirm SOUL.md is foundation (slot #1)
- [ ] Confirm `/personality` is session-level overlay
- [ ] Test reset: `/personality none`, `/personality default`, `/personality neutral`
- [ ] Verify `agent.system_prompt` reserved for manual system prompt only

### 3.4 Personality + CLI Appearance Separation
- [ ] Confirm conversational personality ≠ CLI appearance
- [ ] Test `/skin` for terminal appearance separately
- [ ] Verify `display.skin` independent of `display.personality`

## Phase 4: Honcho Tools & CLI Commands

### 4.1 Honcho Tools (available when Honcho is active memory provider)
- [ ] `honcho_profile` — Read/update peer card (pass `card` list to update)
- [ ] `honcho_search` — Semantic search over context (raw excerpts)
- [ ] `honcho_context` — Full session context (summary, representation, card, recent messages)
- [ ] `honcho_reasoning` — Synthesized answer from Honcho LLM (pass `reasoning_level`)
- [ ] `honcho_conclude` — Create/delete conclusions (pass `conclusion` or `delete_id`)

### 4.2 Hermes Honcho CLI Commands
- [ ] `hermes honcho status` — Connection status, config, key settings
- [ ] `hermes honcho setup` — Redirects to memory setup
- [ ] `hermes honcho strategy` — Show/set session strategy
- [ ] `hermes honcho peer` — Show/update peer names + dialectic reasoning level
- [ ] `hermes honcho mode` — Show/set recall mode (hybrid/context/tools)
- [ ] `hermes honcho tokens` — Show/set token budget
- [ ] `hermes honcho identity` — Seed/show AI peer's Honcho identity
- [ ] `hermes honcho sync` — Sync Honcho config to all profiles
- [ ] `hermes honcho peers` — Show peer identities across profiles
- [ ] `hermes honcho sessions` — List Honcho session mappings
- [ ] `hermes honcho map` — Map current directory to Honcho session
- [ ] `hermes honcho enable/disable` — Toggle Honcho for active profile
- [ ] `hermes honcho migrate` — Migration guide from openclaw-honcho

## Phase 5: Advanced Configuration

### 5.1 Observation Modes
- [ ] Test `directional` (default) — full mutual observation
- [ ] Test `unified` — shared pool semantics
- [ ] Test custom `observation` block:
  ```json
  "observation": {
    "user": { "observeMe": true, "observeOthers": true },
    "ai": { "observeMe": true, "observeOthers": false }
  }
  ```
- [ ] Verify server-side dashboard toggles override local defaults

### 5.2 Dialectic Depth (Multi-Pass)
- [ ] Test `dialecticDepth: 2` with `dialecticDepthLevels: ["minimal", "medium"]`
- [ ] Test `dialecticDepth: 3` with `dialecticDepthLevels: ["minimal", "low", "high"]`
- [ ] Verify early bailout on strong signal

### 5.3 Session-Start Prewarm
- [ ] Verify background dialectic call on session init
- [ ] Test fallback to synchronous call if prewarm hasn't landed by turn 1

### 5.4 Query-Adaptive Reasoning Level
- [ ] Test auto-scaling: +1 level at ≥120 chars, +2 at ≥400 chars
- [ ] Verify clamp at `reasoningLevelCap` (default `high`)
- [ ] Test disable with `reasoningHeuristic: false`

### 5.5 Gateway Identity Mapping (if running gateway)
- [ ] Test `pinUserPeer: true` — collapse all users to single peer
- [ ] Test `userPeerAliases` mapping runtime IDs to peers
- [ ] Test `runtimePeerPrefix` for namespacing

## Phase 6: Verification & Testing

### 6.1 End-to-End Memory Flow
- [ ] Store fact in session 1 → recall in session 2 (different thread/CLI invocation)
- [ ] Test cross-session continuity with multiple conversations
- [ ] Verify dialectic reasoning extracts insights automatically

### 6.2 Context File Loading
- [ ] Test startup loading (system prompt)
- [ ] Test progressive subdirectory discovery during session
- [ ] Test deduplication of identical files in chain
- [ ] Test security scanner blocks malicious content

### 6.3 Personality System
- [ ] Test SOUL.md as persistent default
- [ ] Test /personality overlay persistence in `display.personality`
- [ ] Test custom personalities in config.yaml
- [ ] Test reset to default

### 6.4 Honcho Tools Integration
- [ ] Test all 5 tools return expected results
- [ ] Test tool calling from agent (not just CLI)
- [ ] Verify tool results integrated into responses

### 6.5 Configuration Persistence
- [ ] Verify config survives Hermes restarts
- [ ] Test `hermes honcho sync` across profiles
- [ ] Test migration from legacy `hermes honcho setup`

## Phase 7: Documentation & Knowledge Transfer

### 7.1 Create Reference Documentation
- [ ] Document Honcho config reference in project AGENTS.md
- [ ] Document context file conventions
- [ ] Document personality usage guidelines
- [ ] Create quick-reference card for Honcho CLI commands

### 7.2 Team Onboarding
- [ ] Document setup process for new team members
- [ ] Create troubleshooting guide for common issues
- [ ] Link to official docs: Honcho, Hermes, Self-Hosting Guide

## Configuration Reference

### Honcho Config (`~/.honcho/config.json` or `$HERMES_HOME/honcho.json`)
```json
{
  "baseUrl": "https://api.honcho.dev",
  "hosts": {
    "hermes": {
      "enabled": true,
      "aiPeer": "hermes",
      "peerName": "alexa",
      "workspace": "hermes",
      "apiKey": "***"
    }
  },
  "contextTokens": 1200,
  "contextCadence": 1,
  "dialecticCadence": 2,
  "dialecticDepth": 1,
  "dialecticReasoningLevel": "low",
  "dialecticDynamic": true,
  "dialecticMaxChars": 600,
  "recallMode": "hybrid",
  "writeFrequency": "async",
  "saveMessages": true,
  "observationMode": "directional",
  "messageMaxChars": 25000,
  "dialecticMaxInputChars": 10000,
  "sessionStrategy": "per-directory",
  "pinUserPeer": false,
  "userPeerAliases": {},
  "runtimePeerPrefix": ""
}
```

### Hermes Config (`~/.hermes/config.yaml`)
```yaml
memory:
  provider: honcho

agent:
  personalities:
    codereviewer: |
      You are a meticulous code reviewer. Identify bugs, security issues,
      performance concerns, and unclear design choices. Be precise and constructive.
    # Add more custom personalities here

display:
  personality: ""  # Set by /personality command
  skin: "default"
```

## Key URLs & References

| Resource | URL |
|----------|-----|
| Honcho Documentation Index | https://honcho.dev/docs/llms.txt |
| Hermes Honcho Memory Docs | https://hermes-agent.nousresearch.com/docs/user-guide/features/honcho |
| Hermes Context Files Docs | https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files |
| Hermes Personality Docs | https://hermes-agent.nousresearch.com/docs/user-guide/features/personality |
| Honcho Self-Hosting Guide | https://honcho.dev/docs/v3/contributing/self-hosting |
| Hermes Agent Source | https://github.com/NousResearch/hermes-agent |
| Honcho Architecture | https://honcho.dev/docs/v3/documentation/core-concepts/architecture |
| Honcho SDK Reference | https://honcho.dev/docs/v3/documentation/reference/sdk.md |
| Honcho CLI Reference | https://honcho.dev/docs/v3/documentation/reference/cli.md |

## Acceptance Criteria

- [ ] Honcho memory provider active and configured
- [ ] Cross-session memory verified (fact persists across sessions)
- [ ] All 5 Honcho tools functional
- [ ] All 12 `hermes honcho` CLI commands functional
- [ ] SOUL.md loads as global personality from `HERMES_HOME`
- [ ] AGENTS.md loads as project context (git root + progressive discovery)
- [ ] Built-in personalities switchable via `/personality`
- [ ] Custom personalities configurable in config.yaml
- [ ] Security scanner blocks prompt injection attempts
- [ ] Configuration persists across restarts
- [ ] Session strategy `per-directory` maps sessions correctly
- [ ] Dialectic reasoning extracts insights automatically

## Dependencies

- Hermes Agent installed and configured
- Honcho API access (cloud or self-hosted)
- Valid API key or JWT token
- Git repository for context file discovery
- Node.js/Bun for Hermes CLI
- Python 3.11+ for any scripts

## Timeline Estimate

| Phase | Estimated Time |
|-------|----------------|
| Phase 1: Honcho Setup | 30-60 min |
| Phase 2: Context Files | 30-45 min |
| Phase 3: Personality | 20-30 min |
| Phase 4: Tools & CLI | 20-30 min |
| Phase 5: Advanced Config | 30-45 min |
| Phase 6: Verification | 30-45 min |
| Phase 7: Documentation | 20-30 min |
| **Total** | **3-4 hours** |

## Notes

- This plan assumes Hermes Agent is already installed
- Self-hosted Honcho adds ~30 min for Docker Compose setup
- Some advanced features (gateway identity mapping) only apply if running Hermes gateway
- Configuration files use different locations: Honcho uses `~/.honcho/config.json`, Hermes uses `~/.hermes/config.yaml`
- The `hermes honcho` subcommand only appears AFTER Honcho is activated as memory provider