---
title: "Hermes Configuration Spec"
source: "docs/hermes-configuration-spec.md"
---

# Hermes Agent Complete Configuration Specification

**Created**: May 25, 2026  
**Version**: 1.0  
**Status**: ACTIVE  
**Linked Plan**: hermes-configuration-plan.md

---

## Overview

Complete specification for Hermes Agent configuration across global and project scopes, including all 7 MCP servers, tool discovery, verification procedures, and production-ready deployment.

---

## 1. Documentation Specification

### Requirement D1.1: Official Reference Documentation
**Spec ID**: D1.1  
**Status**: ✅ COMPLETE

- **What**: Unified Hermes Agent reference guide covering installation, CLI, skills, MCP, and troubleshooting
- **File**: `06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md`
- **Source**: hermes-agent.nousresearch.com official docs
- **Content**:
  - Quick overview (5 min)
  - Installation & setup (all platforms)
  - 50+ CLI commands reference
  - Skills system (4 registries, 660+ skills)
  - MCP integration guide
  - Configuration reference
  - Troubleshooting (8 common issues)

**Acceptance Criteria**:
- [ ] All CLI commands documented
- [ ] All configuration keys listed
- [ ] Code examples working
- [ ] Cross-references functional
- [ ] Version pinned to v0.10.0

### Requirement D1.2: Security Best Practices
**Spec ID**: D1.2  
**Status**: ✅ COMPLETE

- **What**: MCP & Hermes security hardening guide
- **File**: `07-MCP_SECURITY_BEST_PRACTICES.md`
- **Source**: MCP official spec + security docs
- **Content**:
  - Confused Deputy problem
  - SSRF (Server-Side Request Forgery)
  - Session hijacking
  - Local compromise
  - Scope minimization
  - Production deployment checklist

**Acceptance Criteria**:
- [ ] All 5 attack vectors documented
- [ ] Mitigations provided for each
- [ ] Code examples included
- [ ] Production checklist complete

---

## 2. MCP Configuration Specification

### Requirement M2.1: MCP Server Discovery
**Spec ID**: M2.1  
**Status**: 🟡 IN PROGRESS

- **What**: Discover all 7 MCP servers via Docker gateway
- **Method**: `docker mcp gateway run --profile adminbot`
- **Servers Expected** (7 total):
  1. **filesystem** - File operations
  2. **docker** - Container management
  3. **playwright** - Browser automation
  4. **context7** - Documentation lookup
  5. **gh_grep** - GitHub code search
  6. **sequential-thinking** - Reasoning/analysis
  7. **next-devtools** - Next.js development

**Output Specification**:
```
Server: <name>
  Status: <connected|disconnected>
  Tools: <count>
  Transport: <stdio|http>
```

**Acceptance Criteria**:
- [ ] All 7 servers discoverable
- [ ] Tool counts accurate (250+ total)
- [ ] Connection status verified
- [ ] No authentication errors

### Requirement M2.2: MCP Server Configuration
**Spec ID**: M2.2  
**Status**: ⏳ PENDING

- **What**: Configure all 7 servers in ~/.hermes/config.yaml
- **Format**: YAML with bun package manager
- **Location**: `~/.hermes/config.yaml` under `mcp_servers` section

**Configuration Template**:
```yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/path"]
    enabled: true
    timeout: 30
    tools:
      include: []  # or exclude: []
      
  docker:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-docker"]
    enabled: true
    
  # ... additional servers
```

**Acceptance Criteria**:
- [ ] All 7 servers configured
- [ ] YAML syntax valid
- [ ] No secrets hardcoded
- [ ] Timeouts set appropriately

### Requirement M2.3: Tool Registration & Naming
**Spec ID**: M2.3  
**Status**: ⏳ PENDING

- **What**: Verify tool naming and registration
- **Convention**: `mcp_<server>_<tool_name>`
- **Examples**:
  - `mcp_filesystem_read_file`
  - `mcp_github_create_issue`
  - `mcp_docker_list_containers`

**Verification Command**:
```bash
hermes tools list | grep mcp_
# Expected: 250+ tools listed with mcp_ prefix
```

**Acceptance Criteria**:
- [ ] Tool naming follows convention
- [ ] No naming collisions
- [ ] All tools registered
- [ ] Hermes tools list shows 250+

---

## 3. Global Configuration Specification

### Requirement G3.1: Provider Setup
**Spec ID**: G3.1  
**Status**: ⏳ PENDING

- **What**: Configure default LLM provider and model
- **File**: `~/.hermes/config.yaml`

**Configuration**:
```yaml
default_model: "claude-3-5-sonnet-20241022"
default_provider: "anthropic"

providers:
  anthropic:
    api_key: "${ANTHROPIC_API_KEY}"
```

**Acceptance Criteria**:
- [ ] Model configured
- [ ] Provider set
- [ ] API key in .env (not hardcoded)
- [ ] `hermes model` shows configured provider

### Requirement G3.2: Environment Variables
**Spec ID**: G3.2  
**Status**: ⏳ PENDING

- **What**: Secure credential management
- **File**: `~/.hermes/.env` (not tracked in git)
- **Permissions**: `chmod 600`

**Required Variables**:
```bash
ANTHROPIC_API_KEY=sk-ant-...
# Additional provider keys as needed
```

**Acceptance Criteria**:
- [ ] .env file created
- [ ] Permissions set to 600
- [ ] No credentials in config.yaml
- [ ] All providers can authenticate

### Requirement G3.3: Skills Registry Setup
**Spec ID**: G3.3  
**Status**: ⏳ PENDING

- **What**: Enable all 4 official skill registries
- **Registries**:
  1. nous/core - Core capabilities
  2. nous/dev - Development tools (660+ total)
  3. community/skills - Community contributions
  4. partner/skills - Partner integrations

**Configuration**:
```bash
hermes skills list              # View installed
hermes skills add nous/dev/code-review
```

**Acceptance Criteria**:
- [ ] All 4 registries accessible
- [ ] At least 10 skills installed
- [ ] Skills cache operational
- [ ] Skill discovery working

### Requirement G3.4: Gateway Configuration (Optional)
**Spec ID**: G3.4  
**Status**: ⏳ PENDING (Optional)

- **What**: Set up messaging platform integration
- **Platforms**: Telegram, Discord, Slack, WhatsApp, Signal
- **File**: `~/.hermes/config.yaml` under `gateway` section

**Basic Configuration**:
```yaml
gateway:
  host: "0.0.0.0"
  port: 8000
  enable_messaging: true
```

**Acceptance Criteria**:
- [ ] Gateway configuration valid
- [ ] Port available
- [ ] TLS configured (production)
- [ ] `hermes gateway start` functional

---

## 4. Project Configuration Specification

### Requirement P4.1: Project-Level Config
**Spec ID**: P4.1  
**Status**: ⏳ PENDING

- **What**: Project-specific Hermes configuration
- **Location**: `.hermes/config.yaml` (relative to project)
- **Scope**: Overrides global settings for this project

**Content**:
```yaml
# Project-specific overrides
default_model: "claude-3-5-sonnet-20241022"

# Project MCP servers
mcp_servers:
  # Add project-specific servers here

# Project skills
bundled_skills:
  - name: "custom-project-skill"
    enabled: true
```

**Acceptance Criteria**:
- [ ] Config file created
- [ ] Valid YAML syntax
- [ ] Overrides working
- [ ] MCP servers accessible

### Requirement P4.2: Project Skills Integration
**Spec ID**: P4.2  
**Status**: ⏳ PENDING

- **What**: Project-local skills directory
- **Location**: `./skills/` (relative to project)
- **Format**: SKILL.md files

**Acceptance Criteria**:
- [ ] Skills directory created
- [ ] Project skills loadable
- [ ] Global skills still available
- [ ] Slash commands working

### Requirement P4.3: Documentation Integration
**Spec ID**: P4.3  
**Status**: ⏳ PENDING

- **What**: Link documentation to project context
- **File**: `.hermes.md` update

**Link to Add**:
```markdown
## Documentation (Updated)

- 06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md - Official reference
- 07-MCP_SECURITY_BEST_PRACTICES.md - Security guide
- HERMES_CONFIGURATION_GUIDE.md - Global setup (to create)
- HERMES_PROJECT_SETUP.md - Project setup (to create)
- hermes-configuration-plan.md - Implementation plan
- hermes-configuration-spec.md - This specification
```

**Acceptance Criteria**:
- [ ] All docs linked
- [ ] Cross-references working
- [ ] No broken links
- [ ] Version information current

---

## 5. Verification Specification

### Requirement V5.1: MCP Server Verification
**Spec ID**: V5.1  
**Status**: ⏳ PENDING

- **Command**: `hermes mcp list`
- **Expected Output**: All 7 servers listed with status

```
MCP Servers (7):
  ✓ filesystem
  ✓ docker
  ✓ playwright
  ✓ context7
  ✓ gh_grep
  ✓ sequential-thinking
  ✓ next-devtools

Total Tools: 250+
```

**Acceptance Criteria**:
- [ ] All 7 servers listed
- [ ] All connected (✓)
- [ ] Tool count ≥ 250
- [ ] No error messages

### Requirement V5.2: Tool Discovery Verification
**Spec ID**: V5.2  
**Status**: ⏳ PENDING

- **Command**: `hermes tools list | grep mcp_`
- **Expected**: 250+ tools with mcp_ prefix

**Sample Output**:
```
mcp_filesystem_read_file
mcp_filesystem_write_file
mcp_filesystem_list_directory
mcp_docker_list_containers
mcp_docker_run_container
... (250+ total)
```

**Acceptance Criteria**:
- [ ] All MCP tools discoverable
- [ ] Naming convention followed
- [ ] No naming collisions
- [ ] Tool count accurate

### Requirement V5.3: Hermes Doctor Verification
**Spec ID**: V5.3  
**Status**: ⏳ PENDING

- **Command**: `hermes doctor`
- **Expected**: All 12 checks passing

**Checks**:
1. ✓ Python 3.11+ installed
2. ✓ Node.js v22+ installed
3. ✓ ripgrep installed
4. ✓ Dependencies resolved
5. ✓ Config file valid
6. ✓ API keys configured
7. ✓ Network connectivity
8. ✓ MCP servers accessible
9. ✓ Skills registry reachable
10. ✓ Gateway operational (if enabled)
11. ✓ No deprecated settings
12. ✓ Version current

**Acceptance Criteria**:
- [ ] All 12 checks passing
- [ ] No warnings
- [ ] No errors
- [ ] Output: "All systems operational"

### Requirement V5.4: Chat Functionality Test
**Spec ID**: V5.4  
**Status**: ⏳ PENDING

- **Command**: `hermes chat -q "List files in current directory"`
- **Expected**: Tool execution, working response

**Test Case**:
```bash
hermes chat -q "What tools are available via MCP?"
# Expected: Agent lists MCP tools successfully
```

**Acceptance Criteria**:
- [ ] Chat starts without error
- [ ] Tools callable
- [ ] Response received
- [ ] No timeout errors
- [ ] Execution time < 30 seconds

---

## 6. Quality & Security Requirements

### Requirement Q6.1: Configuration Security
**Spec ID**: Q6.1  
**Status**: ⏳ PENDING

- **Secret Management**:
  - [ ] No secrets in config.yaml
  - [ ] All secrets in ~/.hermes/.env
  - [ ] .env in gitignore
  - [ ] File permissions: `chmod 600`

- **API Key Security**:
  - [ ] Keys use environment variable syntax
  - [ ] Keys rotatable
  - [ ] No keys in git history
  - [ ] Keys masked in logs

**Acceptance Criteria**:
- [ ] Zero hardcoded secrets
- [ ] Proper permission model
- [ ] Audit trail enabled
- [ ] Key rotation procedure documented

### Requirement Q6.2: MCP Server Security
**Spec ID**: Q6.2  
**Status**: ⏳ PENDING

- **Scope Minimization**:
  - [ ] Each server has whitelisted tools
  - [ ] No overly broad permissions
  - [ ] Dangerous tools excluded
  - [ ] Per-server filtering applied

- **Network Security**:
  - [ ] HTTPS for remote servers
  - [ ] Certificate validation
  - [ ] No HTTP connections
  - [ ] Firewall rules applied

**Acceptance Criteria**:
- [ ] Security checklist complete
- [ ] All best practices followed
- [ ] No vulnerabilities identified
- [ ] Production deployment ready

---

## 7. Acceptance & Sign-Off

### Phase Completion Checklist

- [ ] **Documentation Phase**: All docs created and verified
- [ ] **MCP Setup Phase**: All 7 servers configured and tested
- [ ] **Global Configuration**: Provider, env vars, skills set up
- [ ] **Project Configuration**: Project-level config created
- [ ] **Verification Phase**: All tests passing, 0 errors
- [ ] **Security Review**: Best practices implemented

### Final Verification

**When all phases complete**:

```bash
# 1. Verify servers
hermes mcp list                    # ✓ All 7 servers
hermes tools list | wc -l          # ✓ 250+ tools

# 2. Verify configuration
hermes doctor                      # ✓ All checks pass
hermes config show                 # ✓ Valid syntax

# 3. Verify chat
hermes chat -q "Test"              # ✓ Works end-to-end

# 4. Verify security
grep -r "sk-ant" docs/             # ✓ No secrets found
ls -la ~/.hermes/                  # ✓ Proper permissions
```

**Success Criteria**:
- [ ] `hermes mcp list` shows 7/7 servers
- [ ] `hermes doctor` shows all checks passing
- [ ] Chat endpoint functional
- [ ] No configuration errors
- [ ] Security requirements met

---

## 8. Success Metrics

| Metric | Target | Status |
|--------|--------|--------|
| MCP Servers Operational | 7/7 | ⏳ |
| Tools Discoverable | 250+ | ⏳ |
| Configuration Errors | 0 | ⏳ |
| hermes doctor Checks | 12/12 passing | ⏳ |
| Chat Functionality | 100% working | ⏳ |
| Security Compliance | 100% | ⏳ |
| Documentation Complete | 4/4 files | ✅ |

---

## Document Cross-References

| Document | Purpose | Link |
|----------|---------|------|
| Official Reference | Hermes complete reference | `06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md` |
| Security Guide | MCP & Hermes security | `07-MCP_SECURITY_BEST_PRACTICES.md` |
| Implementation Plan | Phase-based execution | `hermes-configuration-plan.md` |
| This Spec | Requirements definition | `hermes-configuration-spec.md` |

---

**Specification Version**: 1.0  
**Created**: May 25, 2026  
**Status**: ACTIVE  
**Author**: Alexa  
**Linked To Plan**: hermes-configuration-plan.md
