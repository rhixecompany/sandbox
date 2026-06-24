---
title: "Hermes Configuration Plan"
source: "docs/hermes-configuration-plan.md"
---

# Hermes Agent Complete Configuration Plan

**Created**: May 25, 2026  
**Project**: SandBox Hermes Full Configuration  
**Status**: ACTIVE  
**Owner**: Alexa

---

## Executive Summary

Complete configuration of Hermes Agent across global and project scope, integrating all 7 MCP servers, verifying tool discovery, and establishing production-ready setup with comprehensive documentation.

---

## Phases

### Phase 1: Documentation & Knowledge Base (COMPLETE)
- [x] Web search for latest Hermes documentation
- [x] Extract official reference materials
- [x] Create unified documentation (06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md)
- [x] Create security best practices (07-MCP_SECURITY_BEST_PRACTICES.md)

### Phase 2: MCP Server Setup & Migration
- [ ] Inspect Docker MCP servers via `docker mcp gateway run --profile adminbot`
- [ ] List discovered MCP servers and tools
- [ ] Migrate each server configuration to bun package manager
- [ ] Update ~/.hermes/config.yaml with all 7 servers
- [ ] Verify tool discovery for each server

### Phase 3: Global Hermes Configuration
- [ ] Run `hermes doctor` to validate environment
- [ ] Configure default LLM provider and model
- [ ] Set up environment variables (.env)
- [ ] Configure skills registry (4 official registries)
- [ ] Set up memory configuration
- [ ] Configure gateway (optional, for messaging)

### Phase 4: Project-Level Configuration
- [ ] Create project-specific config (.hermes/config.yaml)
- [ ] Configure project-scoped skills
- [ ] Set up project MCP servers
- [ ] Configure .cursorrules and AGENTS.md integration
- [ ] Link documentation to project context

### Phase 5: Verification & Validation
- [ ] Run `hermes mcp list` - verify all servers
- [ ] Test tool discovery - `hermes tools list`
- [ ] Run `hermes doctor` - full diagnostics
- [ ] Test basic chat functionality
- [ ] Verify skills installation
- [ ] Validate configuration syntax

### Phase 6: Documentation & Handoff
- [ ] Create HERMES_CONFIGURATION_GUIDE.md (global setup)
- [ ] Create HERMES_PROJECT_SETUP.md (project-specific)
- [ ] Link plans and specs in .hermes.md
- [ ] Archive executed plan
- [ ] Document lessons learned

---

## Detailed Tasks

### Phase 2: MCP Server Setup & Migration

#### Task 2.1: Inspect Docker MCP Gateway
```bash
# Command to execute
docker mcp gateway run --profile adminbot

# Expected Output
# - List of available MCP servers
# - Tool count per server
# - Connection status
# - Configuration details
```

**Success Criteria**:
- Gateway starts without errors
- All MCP servers listed
- Tool counts displayed
- No authentication errors

#### Task 2.2: Migrate MCP Server Configurations
- For each discovered MCP server:
  1. Extract current configuration
  2. Migrate to bun-compatible format
  3. Test connection
  4. Verify tool discovery

**Servers to Configure** (7 total):
1. filesystem
2. docker
3. playwright
4. context7
5. gh_grep
6. sequential-thinking
7. next-devtools

#### Task 2.3: Update ~/.hermes/config.yaml

Add to `mcp_servers` section:
```yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user"]
  # ... additional servers
```

### Phase 3: Global Configuration

#### Task 3.1: Initial Diagnostics
```bash
hermes doctor
```

**Check for**:
- Python 3.11+ installed
- Node.js v22+ installed
- Dependencies available
- API keys configured
- Network connectivity

#### Task 3.2: Configure Provider

```bash
hermes setup
# OR
hermes config set default_model "claude-3-5-sonnet-20241022"
hermes config set default_provider "anthropic"
```

#### Task 3.3: Set Environment Variables

File: `~/.hermes/.env`
```bash
ANTHROPIC_API_KEY=sk-ant-...
GITHUB_TOKEN=ghp_...
# Additional provider keys as needed
```

#### Task 3.4: Skills Registry

```bash
hermes skills list              # View installed
hermes skills cache clean       # Clear cache if needed
hermes skills add nous/core/code-review
```

### Phase 4: Project Configuration

#### Task 4.1: Project Config
File: `C:\Users\Alexa\Desktop\SandBox\.hermes\config.yaml`

```yaml
# Project-specific overrides
default_model: "claude-3-5-sonnet-20241022"
mcp_servers:
  # Project MCP servers
skills:
  - name: "custom-skill"
    enabled: true
```

#### Task 4.2: Link Documentation
Update `.hermes.md` to reference:
- 06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md
- 07-MCP_SECURITY_BEST_PRACTICES.md
- HERMES_CONFIGURATION_GUIDE.md
- HERMES_PROJECT_SETUP.md

### Phase 5: Verification

#### Task 5.1: MCP Server Verification
```bash
hermes mcp list
# Expected: All 7 servers listed with tool counts
```

#### Task 5.2: Tool Discovery
```bash
hermes tools list
# Expected: 250+ tools available
```

#### Task 5.3: Full Diagnostics
```bash
hermes doctor
# Expected: All checks passing
```

#### Task 5.4: Chat Test
```bash
hermes chat -q "List the files in current directory"
# Expected: Tool execution, successful response
```

---

## Acceptance Criteria

✅ **All phases complete when**:

1. **Documentation**:
   - All 4 documentation files created
   - Cross-references working
   - Security best practices documented

2. **MCP Configuration**:
   - All 7 servers configured
   - Tool discovery working for each
   - No connection errors

3. **Global Setup**:
   - `hermes doctor` passes all checks
   - Default model configured
   - Environment variables set

4. **Project Setup**:
   - Project config created
   - Skills available
   - MCP servers accessible

5. **Verification**:
   - `hermes mcp list` shows 7 servers
   - `hermes tools list` shows 250+ tools
   - Chat works end-to-end
   - `hermes doctor` shows "All systems operational"

---

## Dependencies & Prerequisites

- Hermes Agent v0.10.0+
- Python 3.11+
- Node.js v22+
- Docker (for MCP gateway inspection)
- bun package manager
- Git
- API keys for LLM providers

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| MCP server connection timeout | Configure `connect_timeout` in config.yaml |
| Tool naming conflicts | Use MCP prefix convention (mcp_<server>_<tool>) |
| Secret exposure | Keep .env file in gitignore, chmod 600 |
| Configuration syntax errors | Run `hermes config show` to validate |
| Missing dependencies | Run `hermes doctor` before starting |

---

## Success Metrics

- [ ] 7/7 MCP servers operational
- [ ] 250+ tools discoverable
- [ ] 0 configuration errors
- [ ] 100% hermes doctor checks passing
- [ ] Chat endpoint functioning
- [ ] Skills system operational

---

## Timeline

| Phase | Duration | Status |
|-------|----------|--------|
| Phase 1: Documentation | Complete | ✅ DONE |
| Phase 2: MCP Setup | 30 min | 🟡 IN PROGRESS |
| Phase 3: Global Config | 20 min | ⏳ PENDING |
| Phase 4: Project Config | 15 min | ⏳ PENDING |
| Phase 5: Verification | 20 min | ⏳ PENDING |
| Phase 6: Handoff | 15 min | ⏳ PENDING |

**Total Estimated Time**: ~2 hours

---

## Document References

- Plan: hermes-configuration-plan.md (this file)
- Spec: hermes-configuration-spec.md
- Docs: 06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md
- Security: 07-MCP_SECURITY_BEST_PRACTICES.md

---

**Plan Version**: 1.0  
**Last Updated**: May 25, 2026  
**Created By**: Alexa
