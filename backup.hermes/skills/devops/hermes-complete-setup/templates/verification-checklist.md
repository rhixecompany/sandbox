# Hermes Complete Setup Verification Checklist

Use this checklist to track progress through all 5 phases of Hermes Agent configuration.

## PHASE 1: Documentation Research & Creation

- [ ] Web search completed (4+ sources identified)
- [ ] Official Hermes documentation extracted
- [ ] MCP configuration sources extracted
- [ ] Security best practices researched
- [ ] `06-HERMES_AGENT_OFFICIAL_REFERENCE_2026.md` created (installation, CLI commands, config, MCP, skills, troubleshooting, FAQ)
- [ ] `07-MCP_SECURITY_BEST_PRACTICES.md` created (MCP overview, threat model, best practices, credential management)
- [ ] `HERMES_PROJECT_SETUP.md` created (quick start, config, tools, workflows, troubleshooting)
- [ ] `HERMES_DOCUMENTATION_INDEX.md` created (master reference, learning path, FAQ)

**Status**: _____ / 8 complete

## PHASE 2: MCP Server Verification

- [ ] Run `hermes mcp list` — all 7-8 servers listed
- [ ] Verify each server status (enabled/disabled)
- [ ] Test filesystem operations: `hermes chat -q "List files in current directory"`
- [ ] Test docker operations (if enabled): `hermes chat -q "List running containers"`
- [ ] Test browser automation (if enabled): screenshot test
- [ ] Test sequential thinking (reasoning): step-by-step problem solve
- [ ] Run `hermes tools list` — verify 250+ tools
- [ ] Confirm tool naming pattern: `mcp_<server>_<function>`
- [ ] Create `HERMES_CONFIGURATION_STATUS.md` with tool inventory

**Status**: _____ / 9 complete

## PHASE 3: Global Configuration Setup

- [ ] Run `hermes config show` — review all settings
- [ ] Verify `default_model` configured (should be big-pickle or preferred model)
- [ ] Check `mcp_servers` section (8 servers configured)
- [ ] Verify `fallback_providers` list (minimum 2 providers)
- [ ] Confirm `terminal` settings (backend: bash, timeout: 300s)
- [ ] Check `context_compression` enabled (75% threshold)
- [ ] Verify `memory` configuration present
- [ ] Test chat: `hermes chat -q "List available tools and MCP servers"`
- [ ] Run `hermes doctor` — ALL CHECKS MUST PASS
- [ ] Verify no security advisories
- [ ] Confirm API connectivity (27+ checks)
- [ ] Verify tool availability (19+/24 enabled)
- [ ] Test model fallback: `hermes chat --model "gpt-4o" -q "What is your model?"`

**Status**: _____ / 13 complete

## PHASE 4: Project Integration

- [ ] Update `.hermes.md` with documentation links
- [ ] Link all 8+ documentation files in Key Directories section
- [ ] Create project-level `.hermes/config.yaml` (if project-specific overrides needed)
- [ ] Configure project working directory in `.hermes/config.yaml`
- [ ] Update project README with links to Hermes docs
- [ ] Link `HERMES_DOCUMENTATION_INDEX.md` as quick reference
- [ ] Link `HERMES_PROJECT_SETUP.md` for project-specific workflows

**Status**: _____ / 7 complete

## PHASE 5: Verification & Documentation

- [ ] Run final `hermes doctor` — ALL SYSTEMS PASSING
- [ ] Run `hermes mcp list` — confirm 7/8 servers enabled
- [ ] Run `hermes tools list` — confirm 250+ tools available
- [ ] Test chat: `hermes chat -q "What tools are available?"`
- [ ] Create `HERMES_COMPLETE_VERIFICATION.md` with all test results
- [ ] Create `COMPLETION_REPORT.md` with final statistics
- [ ] Create `HERMES_SETUP_COMPLETE.txt` quick reference
- [ ] Verify security: 0 advisories
- [ ] Verify API connectivity: all checks passed
- [ ] All documentation files in `docs/` directory
- [ ] `.hermes.md` updated and linked

**Status**: _____ / 11 complete

---

## Summary

| Phase | Name | Status | Items | Complete |
|-------|------|--------|-------|----------|
| 1 | Documentation Research & Creation | ⚪ | 8 | / 8 |
| 2 | MCP Server Verification | ⚪ | 9 | / 9 |
| 3 | Global Configuration Setup | ⚪ | 13 | / 13 |
| 4 | Project Integration | ⚪ | 7 | / 7 |
| 5 | Verification & Documentation | ⚪ | 11 | / 11 |
| **TOTAL** | **Complete Setup** | ⚪ | **48** | **/ 48** |

---

## Quick Status Commands

Copy these commands to verify status at any point:

```bash
# System health
hermes doctor

# MCP servers
hermes mcp list

# All tools
hermes tools list

# Test chat
hermes chat -q "What tools are available?"

# Configuration
hermes config show

# Verify API connectivity
hermes chat -q "Test all configured APIs"
```

---

**Created**: May 25, 2026  
**Version**: 1.0  
**Author**: Alexa
