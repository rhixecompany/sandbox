---
name: hermes-complete-setup
title: "Hermes Agent Complete Setup & Configuration"
description: "Complete end-to-end workflow for installing, configuring, verifying, and integrating Hermes Agent across global environment and project scope with all 5 implementation phases."
author: Alexa
created: 2026-05-25
version: 1.0
triggers:
  - "configure Hermes"
  - "set up Hermes Agent"
  - "complete Hermes setup"
  - "integrate Hermes with project"
  - "verify Hermes configuration"
---

# Hermes Agent Complete Setup & Configuration

## When to Use

- When performing hermes complete setup operations or tasks
- When managing hermes complete setup infrastructure or configurations
- When automating or debugging hermes complete setup workflows
- **Triggers**: "set up devops/hermes-complete-setup", "configure hermes complete setup", "debug hermes complete setup issue"

## Workflow

### Phase 1: Setup

Verify prerequisites and ensure required dependencies are available.

### Phase 2: Execute

Perform the hermes complete setup operations following the instructions in this skill.

### Phase 3: Verify

Confirm the output meets expectations and address any issues.

### Phase 4: Document

Record any changes, configurations, or decisions made during execution.

## Overview

Complete end-to-end workflow for installing, configuring, verifying, and integrating Hermes Agent across global environment and project scope. Covers all 5 implementation phases: documentation, MCP setup, global config, project config, and verification.

**When to use**: 
- Initial Hermes Agent setup on a new machine or environment
- Migrating Hermes to a new project
- Complete reconfiguration after system changes
- Documenting Hermes configuration for a team

**Key outcome**: Hermes fully operational with 7+ MCP servers, 250+ tools, global config complete, comprehensive documentation in place, all systems verified.

---

## Prerequisites

- [ ] Hermes v0.14+ installed (check: `hermes --version`)
- [ ] Python 3.11+ with virtual environment active
- [ ] Terminal/bash access (bash/MSYS on Windows, native shell on Unix)
- [ ] Docker installed (optional, for docker-mcp server)
- [ ] API keys configured for at least one provider (OpenRouter, OpenAI, Google, xAI, etc.)
- [ ] Network access to MCP servers and API endpoints
- [ ] Working directory identified (where .hermes.md and docs/ will live)

---

## Phase 1: Documentation Research & Creation

### Step 1: Web Search for Latest Documentation

Search for the latest Hermes Agent documentation from official sources:

```bash
# Search 1: Official Hermes documentation
web_search "Hermes Agent latest documentation guide official"

# Search 2: MCP servers configuration & tools
web_search "Hermes MCP servers configuration tools management 2024 2025"

# Search 3: Skills and tools reference
web_search "Hermes skills tools reference cheatsheet"

# Search 4: MCP best practices & security
web_search "Model Context Protocol MCP servers setup best practices"
```

**Goal**: Identify 4+ authoritative sources covering Hermes features, MCP integration, security, and configuration options.

### Step 2: Extract & Organize Documentation

For each search result URL, extract content:

```bash
web_extract ["url1", "url2", "url3", "url4", "url5"]
```

**Output**: Markdown content from official Hermes, MCP, and Nous documentation.

### Step 3: Create Official Reference Guide

Create `docs/06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md` containing:
- Installation instructions (Windows, Linux, macOS)
- 50+ CLI commands documented
- Configuration options explained
- Model management (providers, fallbacks, selection)
- MCP integration and tool discovery
- Skills system (hub, installation, creation)
- Scheduling and automation
- Troubleshooting (50+ solutions)
- FAQ (25+ questions)

### Step 4: Create Security Best Practices Guide

Create `docs/07-MCP_SECURITY_BEST_PRACTICES.md` containing:
- MCP overview vs RAG comparison
- Threat model (client, server, network attacks)
- 18+ security best practices
- Input/output validation strategies
- Access control and tool scoping
- Credential management
- Network security (HTTPS, firewall, encryption)
- Monitoring and incident response

### Step 5: Create Project Setup Guide

Create `docs/HERMES_PROJECT_SETUP.md` containing:
- Quick start commands
- Project-level configuration (optional overrides)
- Available tools inventory
- Common workflows (6+ patterns)
- Skills system usage
- Memory and session management
- Scheduling jobs
- Troubleshooting (5+ common issues)
- Best practices
- Integration examples (Git, Docker, Browser)

### Step 6: Create Documentation Index

Create `docs/HERMES_DOCUMENTATION_INDEX.md` as the master reference:
- Quick start by audience (beginners, intermediate, advanced, admins)
- Document descriptions and links
- Configuration checklist
- Learning path progression
- FAQ section
- Support resources

---

## Phase 2: MCP Server Verification

### Step 1: List All MCP Servers

```bash
hermes mcp list
```

**Expected output**: 7-8 servers, status of each (enabled/disabled), tool counts.

### Step 2: Verify Each Server Type

Test by functionality:

```bash
# Filesystem operations
hermes chat -q "List files in current directory using mcp_filesystem"

# Docker operations (if docker-mcp enabled)
hermes chat -q "List running containers"

# Browser automation (if playwright enabled)
hermes chat -q "Navigate to example.com and take screenshot"

# Sequential thinking (reasoning)
hermes chat -q "Solve this step-by-step: 3x + 5 = 20"

# Tool discovery
hermes tools list | grep mcp_
```

### Step 3: Confirm Tool Discovery

```bash
hermes tools list
```

**Expected**: 
- 250+ tools total
- All 7+ MCP servers represented
- Tool naming: `mcp_<server>_<function>`
- All tools marked as enabled/available

### Step 4: Document Tool Inventory

Create `docs/HERMES_CONFIGURATION_STATUS.md` with:
- MCP servers table (enabled/disabled, tool count, status)
- Built-in toolsets inventory (21 available, count enabled)
- Tool registry statistics
- Model configuration
- Performance baseline

---

## Phase 3: Global Configuration Setup

### Step 1: Verify Configuration File

```bash
hermes config show
cat ~/.hermes/config.yaml
```

**Check for**:
- `default_model` set (default: big-pickle, opencode-zen)
- `mcp_servers` section (8 servers configured)
- `fallback_providers` list (minimum 2)
- `terminal` settings (backend: bash, timeout: 300s)
- `context_compression` enabled (75% threshold)
- `memory` configuration present

### Step 2: Test Chat Functionality

```bash
hermes chat -q "List available tools and MCP servers"
```

**Verify**:
- Agent initializes successfully (~0.5s)
- Tool discovery works (<1s)
- Response generated successfully
- No errors or timeouts

### Step 3: Run Health Check

```bash
hermes doctor
```

**All checks must pass**:
- ✓ No security advisories
- ✓ Python environment correct
- ✓ Required packages installed
- ✓ Configuration files valid
- ✓ API connectivity working (27+ checks)
- ✓ Tool availability (19+/24 enabled)
- ✓ Skills Hub ready

### Step 4: Verify API Connectivity

The `hermes doctor` command runs 27 connectivity checks in parallel. All should pass:
- OpenRouter API responding
- OpenCode Zen API responding
- Google Gemini responding
- All other configured providers available

### Step 5: Test Model Fallback Chain

```bash
hermes chat --model "gpt-4o" -q "What is your model?"
```

If primary model unavailable, fallback should activate automatically.

---

## Phase 4: Project Integration

### Step 1: Update Project Configuration File

Edit `.hermes.md` in project root:

```markdown
# Key Directories

docs/
├── HERMES_DOCUMENTATION_INDEX.md         # START HERE
├── HERMES_CONFIGURATION_STATUS.md        # System health
├── HERMES_PROJECT_SETUP.md               # Usage guide
├── 06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md  # CLI reference
├── 07-MCP_SECURITY_BEST_PRACTICES.md     # Security
├── hermes-configuration-plan.md          # Roadmap
├── hermes-configuration-spec.md          # Specs
└── HERMES_COMPLETE_VERIFICATION.md       # Verification
```

### Step 2: Create Project-Level Config (Optional)

If project needs specific MCP servers or tool overrides, create `.hermes/config.yaml`:

```yaml
# Project-specific Hermes configuration
# Overrides ~/.hermes/config.yaml

mcp_servers:
  # Add project-specific servers here
  # Global servers still available

# Project working directory (optional)
terminal:
  cwd: "C:/Users/Alexa/Desktop/SandBox"
```

### Step 3: Link Documentation in Project

Update project README to link:
- `.hermes.md` — project Hermes config
- `docs/HERMES_DOCUMENTATION_INDEX.md` — complete reference
- `docs/HERMES_PROJECT_SETUP.md` — usage guide

---

## Phase 5: Verification & Documentation

### Step 1: Run Complete Verification

```bash
# System health
hermes doctor

# MCP status
hermes mcp list

# Tool discovery
hermes tools list

# Test chat
hermes chat -q "What tools are available?"
```

### Step 2: Create Completion Report

Document:
- All 7+ MCP servers enabled ✓
- 250+ tools available ✓
- Chat functionality working ✓
- hermes doctor all passing ✓
- Security: 0 advisories ✓
- API connectivity: all checks passed ✓

### Step 3: Archive Documentation

Create final verification report:
- `docs/HERMES_COMPLETE_VERIFICATION.md` — test results
- `docs/COMPLETION_REPORT.md` — final report with statistics
- `HERMES_SETUP_COMPLETE.txt` — quick reference summary

---

## Pitfalls & Solutions

### Pitfall 1: MCP Server Connectivity Issues

**Symptom**: `hermes mcp list` shows servers as disabled or errors on connection.

**Solution**:
```bash
# Restart MCP servers
hermes mcp restart

# Check if specific server is responding
hermes chat -q "Test filesystem server: list files"

# View MCP logs
hermes logs | grep mcp
```

### Pitfall 2: API Keys Not Configured

**Symptom**: `hermes doctor` shows "API key or custom endpoint missing" or "API unreachable".

**Solution**:
```bash
# Check configured providers
hermes config show | grep -A5 "providers:"

# Set API key for a provider
export OPENROUTER_API_KEY=*** 

# Or configure in ~/.hermes/.env
echo "OPENROUTER_API_KEY=***" >> ~/.hermes/.env
```

### Pitfall 3: Context Window Overflow

**Symptom**: "Message too long" errors during chat.

**Solution**:
```bash
# Enable context compression
hermes config set agent.context_compression true

# Or increase threshold
hermes config set compression.threshold 80
```

### Pitfall 4: Timeout on Slow Networks

**Symptom**: "Connection timeout" or "Gateway timeout" errors.

**Solution**:
```bash
# Increase gateway timeout
hermes config set agent.gateway_timeout 5000  # 5 seconds

# Increase terminal timeout
hermes config set terminal.timeout 600  # 10 minutes
```

### Pitfall 5: Windows Path Issues

**Symptom**: File not found errors even though file exists.

**Solution**: Use POSIX paths in bash context:
```bash
# ❌ Wrong (Windows path)
hermes chat -q "Read C:\Users\Alexa\file.txt"

# ✅ Correct (POSIX path)
hermes chat -q "Read /c/Users/Alexa/file.txt"
```

### Pitfall 6: Docker MCP Gateway Disabled on Windows

**Symptom**: `docker-gateway` shows as disabled; docker-mcp gateway commands don't work.

**Status**: Expected on Windows (WSL2 limitation).

**Solution**:
- Use standard docker-mcp server for container operations (7/8 enabled is correct)
- Or migrate to WSL2 Linux environment if admin features needed

### Pitfall 7: Incomplete Documentation

**Symptom**: Missing documentation files or incomplete configuration guide.

**Solution**: Re-run Phase 1 completely:
1. Search for latest Hermes documentation
2. Extract all sources
3. Create all 8+ documentation files
4. Create documentation index
5. Link in project .hermes.md

---

## Verification Checklist

Use this checklist to confirm complete setup:

```
PHASE 1: Documentation
  [ ] Web search completed (4+ sources)
  [ ] Documentation extracted
  [ ] 06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md created
  [ ] 07-MCP_SECURITY_BEST_PRACTICES.md created
  [ ] HERMES_PROJECT_SETUP.md created
  [ ] HERMES_DOCUMENTATION_INDEX.md created

PHASE 2: MCP Verification
  [ ] All 7+ MCP servers listed
  [ ] hermes mcp list shows correct status
  [ ] Tool discovery working (<1s)
  [ ] 250+ tools available
  [ ] Each server type tested

PHASE 3: Global Configuration
  [ ] ~/.hermes/config.yaml valid
  [ ] Model configured (big-pickle or preferred)
  [ ] Fallback chain set up (2+ providers)
  [ ] Terminal backend configured (bash)
  [ ] Chat functionality tested
  [ ] hermes doctor all passing
  [ ] API connectivity verified (27+ checks)

PHASE 4: Project Integration
  [ ] .hermes.md updated with documentation links
  [ ] Project config created (if needed)
  [ ] Documentation linked in project
  [ ] Quick reference created

PHASE 5: Verification
  [ ] All MCP servers enabled (7/8 is correct)
  [ ] 250+ tools discoverable
  [ ] Chat working end-to-end
  [ ] hermes doctor: ALL SYSTEMS PASSING
  [ ] Security: 0 advisories
  [ ] API: all connectivity checks passed
  [ ] Completion report created
```

---

## Quick Commands

```bash
# Verify status
hermes doctor                    # Full health check
hermes mcp list                  # MCP servers
hermes tools list                # All tools
hermes config show               # Configuration

# Chat
hermes chat                      # Interactive
hermes chat -q "question"        # One-shot
hermes -z "question"             # Final answer only

# Configuration
hermes config set KEY VALUE      # Change setting
hermes config edit               # Full editor

# Skills & Memory
hermes skills list               # View skills
/session_search "topic"          # Search sessions
/memory                          # Access memory
```

---

## Related Documentation

- **[HERMES_DOCUMENTATION_INDEX.md](../HERMES_DOCUMENTATION_INDEX.md)** — Complete reference index
- **[HERMES_PROJECT_SETUP.md](../HERMES_PROJECT_SETUP.md)** — Project usage guide
- **[06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md](../06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md)** — CLI reference
- **[07-MCP_SECURITY_BEST_PRACTICES.md](../07-MCP_SECURITY_BEST_PRACTICES.md)** — Security guide

---

## Support

For help:
- `hermes help` — General help
- `hermes doctor` — Diagnose issues
- `hermes dump` — Setup summary for support
- Check: `docs/HERMES_DOCUMENTATION_INDEX.md`

---

**Skill Version**: 1.0  
**Last Updated**: May 25, 2026  
**Status**: Production Ready  
**Author**: Alexa

