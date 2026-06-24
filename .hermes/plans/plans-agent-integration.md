---
title: "Plans Agent Integration"
source: "docs/plans/agent-integration-plan.md"
---

# Agent Integration Plan: Qwen Code, OpenCode, Copilot CLI via ACPX

## Overview

Integrate three external AI coding agents (Qwen Code, OpenCode, GitHub Copilot CLI) into the Hermes ecosystem using ACPX (Agent Communication Protocol) for all coding tasks. Each agent needs:

1. Installation verification & authentication
2. ACPX configuration in Hermes config.yaml
3. Hermes skill creation for agent-specific workflows
4. MCP server registration (where applicable)
5. Plugin/hook configuration
6. Testing and verification

---

## Phase 1: Qwen Code Integration

### 1.1 Verify Installation & Auth
- [x] Qwen 0.17.0 installed (DONE)
- [ ] Auth: Qwen OAuth discontinued. Requires `qwen auth` reconfiguration
- [ ] Configure `~/.qwen/settings.json` with active API key
- [ ] Create `.qwen/settings.json` for SandBox project

### 1.2 ACPX Configuration
- [ ] Add ACP provider entry in Hermes config.yaml for Qwen Code
- [ ] Create `hermes-qwen` skill in Hermes skills directory
- [ ] Configure Qwen Code as ACP coding agent in Hermes

### 1.3 Hermes Integration
- [ ] Create/update `qwen-code` skill with ACPX integration pattern
- [ ] Add Qwen model references in Hermes config
- [ ] Configure Qwen as fallback/complementary agent

### 1.4 Testing
- [ ] Test `qwen -p "hello"` headless mode
- [ ] Test Hermes → Qwen ACP delegation
- [ ] Test basic coding task

---

## Phase 2: OpenCode Integration

### 2.1 Verify Installation & Auth
- [x] OpenCode 1.15.12 installed (DONE)
- [x] opencode.json configured (DONE)
- [ ] Verify provider auth (opencode auth list)
- [ ] Test basic `opencode run` command

### 2.2 ACPX Configuration
- [ ] Add OpenCode ACP provider in Hermes config.yaml
- [ ] Update `opencode` skill in Hermes with ACPX integration pattern
- [ ] Configure OpenCode agents (build/plan) mapping

### 2.3 Plugin & MCP Config
- [ ] Review and verify OpenCode plugins list
- [ ] Add OpenCode MCP servers for Hermes compatibility
- [ ] Create OpenCode hooks for ACPX callbacks

### 2.4 Testing
- [ ] Test `opencode run` smoke test
- [ ] Test Hermes → OpenCode delegation
- [ ] Test full coding workflow

---

## Phase 3: Copilot CLI Integration

### 3.1 Verify Installation & Auth
- [x] Copilot CLI 1.0.33 installed (DONE)
- [ ] Verify auth: `copilot` interactive login or GH_TOKEN
- [ ] Check Copilot subscription access

### 3.2 ACPX Configuration
- [x] Hermes already has `copilot-acp` provider (DONE in config.yaml)
- [ ] Update Copilot ACP configuration for direct `copilot` CLI use
- [ ] Create `copilot-cli` skill in Hermes

### 3.3 IDE & Tool Integration
- [ ] Configure Copilot CLI LSP settings if needed
- [ ] Wire Copilot CLI as coding agent in ACPX
- [ ] Create hooks for Copilot CLI output processing

### 3.4 Testing
- [ ] Test `copilot -p "list files"` non-interactive
- [ ] Test Hermes → Copilot CLI ACP delegation
- [ ] Test coding workflow

---

## Phase 4: Cross-Agent Configuration

### 4.1 Unified ACPX Config
- [ ] Create unified ACPX agent routing table
- [ ] Configure agent selection logic per task type
- [ ] Add agent routing documentation

### 4.2 Skill Updates
- [ ] Update all three skills with ACPX patterns
- [ ] Create dispatching skill for agent selection
- [ ] Add cross-reference documentation

### 4.3 MCP & Plugin Ecosystem
- [ ] Register common MCP servers across all agents
- [ ] Create shared hook patterns
- [ ] Document multi-agent workflow

---

## Phase 5: Final Verification

### 5.1 Integration Tests
- [ ] Each agent functional independently
- [ ] ACPX delegation working from Hermes
- [ ] Cross-agent context passing works
- [ ] All three agents can complete real coding tasks

### 5.2 Documentation & Commit
- [ ] Commit all config changes
- [ ] Update AGENTS.md with agent integration details
- [ ] Create SUMMARY.md with results
