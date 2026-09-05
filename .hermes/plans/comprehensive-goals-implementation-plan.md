# Comprehensive Goals Implementation Plan

## Overview
This plan addresses all goals from the user request, organized into phases with dependencies, timelines, and verification gates.

## Goals Summary

1. **Config & Quick Commands** - Ensure all scripts have valid quick_commands in config.yaml, sync .env/config.yaml files
2. **Systematic Debugging** - Fix all Hermes desktop, plugins, hooks, scripts, agents issues
3. **Git Operations** - Commit and push to clean-development, development, production branches
4. **File Triage & Deduplication** - List, triage, dedupe files across repo and Hermes root
5. **Cleanup Plan** - Clean up unused AI agents, Docker images, containers, volumes, models, MCP toolkit
6. **MCP Server Debugging** - Fix all failed VSCode, OpenCode, Hermes, Copilot, Codex MCP servers
7. **Session Startup/End Debugging** - Fix all session skills, context files, system prompts
8. **Doctor & Health Checks** - Run hermes doctor, security audit, status, insights, logs, bun run check
9. **MCP Skills** - Create skills for Hermes MCP servers without skills
10. **Rate Limit Bypass** - Implement plugins/hooks/scripts/skills to bypass rate limits

---

## Phase 1: Config & Quick Commands (COMPLETED)
**Status**: ✅ Complete
**Duration**: Completed
**Tasks**:
- [x] Generated unified quick_commands for both script directories (265 scripts)
- [x] Updated config.yaml with 272 quick_commands (265 generated + 7 preserved)
- [x] Verified all commands pass smoke test
- [x] Verified registry has no issues

---

## Phase 2: Environment Sync (.env & config.yaml)
**Status**: 🔄 In Progress
**Duration**: 30 minutes
**Tasks**:
- [ ] Inventory all .env files in SandBox and Hermes root
- [ ] Inventory all config.yaml files in Hermes profiles
- [ ] Create sync script to keep them consistent
- [ ] Validate sync works

### .env Files Found:
**SandBox**:
- /c/Users/Alexa/Desktop/SandBox/.env
- /c/Users/Alexa/Desktop/SandBox/projects/Banking/.env
- /c/Users/Alexa/Desktop/SandBox/projects/Banking/.env.example
- /c/Users/Alexa/Desktop/SandBox/projects/Banking/.env.local
- /c/Users/Alexa/Desktop/SandBox/projects/Banking/.envs/local/.env
- /c/Users/Alexa/Desktop/SandBox/projects/Banking/.envs/local/.env.local
- /c/Users/Alexa/Desktop/SandBox/projects/Banking/.envs/production/.env
- /c/Users/Alexa/Desktop/SandBox/projects/comicwise/.env.example
- /c/Users/Alexa/Desktop/SandBox/projects/comicwise/.env.local
- /c/Users/Alexa/Desktop/SandBox/projects/comicwise/.env.local.example
- /c/Users/Alexa/Desktop/SandBox/projects/comicwise/.env.test
- /c/Users/Alexa/Desktop/SandBox/projects/Django-Scrapy-Selenium/.env.example
- /c/Users/Alexa/Desktop/SandBox/projects/ecom/.env.example
- /c/Users/Alexa/Desktop/SandBox/projects/rhixecompany-comics/.env.example
- /c/Users/Alexa/Desktop/SandBox/projects/rhixecompany-comics/backend/.env.example
- /c/Users/Alexa/Desktop/SandBox/projects/rhixecompany-comics/frontend/.env.local
- /c/Users/Alexa/Desktop/SandBox/projects/selenium_webdriver/.env.example
- /c/Users/Alexa/Desktop/SandBox/projects/university-libary-jsm/.env.example
- /c/Users/Alexa/Desktop/SandBox/projects/xamehi/.env.example
- /c/Users/Alexa/Desktop/SandBox/projects/xamehi.tv/.env.example

**Hermes Root**:
- /c/Users/Alexa/AppData/Local/hermes/.env
- /c/Users/Alexa/AppData/Local/hermes/.env.pre-delete

### config.yaml Files Found:
- /c/Users/Alexa/AppData/Local/hermes/config.yaml (main)
- /c/Users/Alexa/AppData/Local/hermes/profiles/*/config.yaml (13 profiles)

---

## Phase 3: Systematic Debugging - Hermes Desktop/Plugins/Hooks/Scripts/Agents
**Status**: ⏳ Pending
**Duration**: 2-3 hours
**Dependencies**: Phase 2 complete
**Tasks**:
- [ ] Run `hermes doctor` and capture all issues
- [ ] Run `hermes doctor --fix` 
- [ ] Run `hermes security audit`
- [ ] Run `hermes status`
- [ ] Run `hermes insights`
- [ ] Run all log checks (list, errors, desktop, gateway, gui, agent)
- [ ] Run `bun run check`
- [ ] Fix all identified issues systematically

### Sub-agents for parallel debugging:
1. **Desktop Debugging** - Inspect Hermes TUI DOM/CSS via CDP
2. **Plugin Debugging** - Audit plugins list, check disabled/enabled
3. **Hook Debugging** - Check hook allowlist, fix hook config pitfalls
4. **Script Debugging** - Validate all scripts with quick_commands
5. **Agent Debugging** - Check agent provider matrix

---

## Phase 4: Git Operations
**Status**: ⏳ Pending
**Duration**: 15 minutes
**Dependencies**: Phase 3 complete (all fixes committed)
**Tasks**:
- [ ] `git add -A`
- [ ] `git commit -m "chore: comprehensive fixes and enhancements"`
- [ ] `git push -u origin clean-development development production`
- [ ] Verify push succeeds on all branches
- [ ] Retry if any failures

---

## Phase 5: File Triage & Deduplication
**Status**: ⏳ Pending
**Duration**: 45 minutes
**Dependencies**: Phase 2 complete
**Tasks**:
- [ ] List all files in SandBox repo with purpose
- [ ] List all files in Hermes root with purpose
- [ ] Identify duplicates across both locations
- [ ] Consolidate duplicate files
- [ ] Delete truly unused files
- [ ] Document file purposes in summary

---

## Phase 6: Cleanup Plan - AI Agents & Docker
**Status**: ⏳ Pending
**Duration**: 30 minutes
**Dependencies**: Phase 5 complete
**Tasks**:
- [ ] Create cleanup script for unused Docker images, builds, containers, volumes
- [ ] Create cleanup script for unused models
- [ ] Create cleanup script for unused MCP toolkit
- [ ] Create cleanup script for unused AI agents (VSCode, OpenCode, Copilot, Codex)
- [ ] Execute cleanup with verification
- [ ] Document what was cleaned

---

## Phase 7: MCP Server Debugging
**Status**: ⏳ Pending
**Duration**: 1 hour
**Dependencies**: Phase 2 complete
**Tasks**:
- [ ] Test all MCP servers with `hermes mcp test <server>`
- [ ] Fix failed VSCode MCP servers
- [ ] Fix failed OpenCode MCP servers
- [ ] Fix failed Hermes MCP servers
- [ ] Fix failed Copilot MCP servers
- [ ] Fix failed Codex MCP servers
- [ ] Sync all MCP configurations
- [ ] Create skills for MCP servers without skills

### MCP Servers to Test:
- github, filesystem, playwright, fetch, tavily, neon, docker, memory, honcho, ast-grep, code-sandbox, sentry, mindstudio, python-quality, context7, sequential-thinking, smithery, parallel-*

---

## Phase 8: Session Startup/End Debugging
**Status**: ⏳ Pending
**Duration**: 45 minutes
**Dependencies**: Phase 2 complete
**Tasks**:
- [ ] Debug session start skills
- [ ] Debug session end skills
- [ ] Fix context files
- [ ] Fix system prompts
- [ ] Verify 5-skill session startup protocol

---

## Phase 9: Doctor & Health Checks
**Status**: ⏳ Pending
**Duration**: 30 minutes
**Dependencies**: Phase 7, 8 complete
**Tasks**:
- [ ] Run `hermes doctor && hermes doctor --fix`
- [ ] Run `hermes security audit`
- [ ] Run `hermes status`
- [ ] Run `hermes insights`
- [ ] Run all log commands
- [ ] Run `bun run check`
- [ ] Fix any remaining issues

---

## Phase 10: MCP Skills Creation
**Status**: ⏳ Pending
**Duration**: 1 hour
**Dependencies**: Phase 7 complete
**Tasks**:
- [ ] List all MCP servers without skills
- [ ] Create skills for each
- [ ] Test skills work correctly
- [ ] Register skills

---

## Phase 11: Rate Limit Bypass
**Status**: ⏳ Pending
**Duration**: 45 minutes
**Dependencies**: Phase 2 complete
**Tasks**:
- [ ] Implement rate-limit-bypass.py enhancements
- [ ] Create plugins/hooks for rate limiting
- [ ] Test with all providers
- [ ] Document bypass strategies

---

## Phase 12: Final Verification & Documentation
**Status**: ⏳ Pending
**Duration**: 30 minutes
**Dependencies**: All phases complete
**Tasks**:
- [ ] Run all judge skills (scripts-judge, plans-judge, prompts-judge, hooks-judge, plugins-judge, specs-judge, skills-judge)
- [ ] Raise all scores to 99+
- [ ] Create final summary report
- [ ] Update SESSION_REPORT.md
- [ ] Commit final changes

---

## Timeline Summary

| Phase | Duration | Start | End |
|-------|----------|-------|-----|
| 1. Config & Quick Commands | 30 min | ✅ Done | ✅ Done |
| 2. Environment Sync | 30 min | Now | +30 min |
| 3. Systematic Debugging | 3 hours | +30 min | +3.5 hours |
| 4. Git Operations | 15 min | +3.5 hours | +3.75 hours |
| 5. File Triage | 45 min | +30 min | +1.15 hours |
| 6. Cleanup Plan | 30 min | +1.15 hours | +1.65 hours |
| 7. MCP Server Debugging | 1 hour | +1.65 hours | +2.65 hours |
| 8. Session Debugging | 45 min | +2.65 hours | +3.4 hours |
| 9. Doctor & Health | 30 min | +3.4 hours | +3.9 hours |
| 10. MCP Skills | 1 hour | +3.9 hours | +4.9 hours |
| 11. Rate Limit Bypass | 45 min | +4.9 hours | +5.65 hours |
| 12. Final Verification | 30 min | +5.65 hours | +6 hours |

**Total Estimated Time**: ~6 hours

---

## Resource Allocation

### Parallel Execution Opportunities:
- Phase 3 sub-tasks (Desktop, Plugin, Hook, Script, Agent debugging) can run in parallel via subagents
- Phase 5 (File triage) can run in parallel with Phase 3
- Phase 7 (MCP servers) can run in parallel with Phase 8
- Phase 9 can start once Phase 7 and 8 complete

### Tools Required:
- `hermes_quick_commands.py` - for script validation
- `hermes doctor`, `hermes mcp test`, `hermes hooks list` - for diagnostics
- `git` - for version control
- `bun` - for TypeScript/JavaScript checks
- `docker` - for container cleanup
- Custom scripts for sync and cleanup

### Sub-agent Delegation:
Each major debugging task (Phase 3, 7, 8, 9) should be delegated to subagents with `delegate_task` for parallel execution.

---

## Verification Gates

Each phase must pass these gates before proceeding:
1. **Config Gates**: All quick_commands verified, config.yaml valid
2. **Sync Gates**: All .env files synced, all config.yaml consistent
3. **Debug Gates**: `hermes doctor` returns clean, no errors in logs
4. **Git Gates**: All commits pushed successfully to all branches
5. **Dedupe Gates**: No duplicate files, all files documented
6. **Cleanup Gates**: Docker clean, no unused models/agents
7. **MCP Gates**: All MCP servers test pass, all have skills
8. **Session Gates**: Session start/end works, 5 skills loaded
9. **Health Gates**: All doctor/security/status/insights/logs clean
10. **Judge Gates**: All judge skills score 99+

---

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Breaking changes in config.yaml | High | Backup before changes, test in isolation |
| Git push conflicts | Medium | Pull before push, resolve conflicts |
| Docker cleanup removes needed images | Medium | Dry-run first, confirm before delete |
| MCP server config corruption | High | Test each server individually |
| Rate limit bypass fails | Low | Multiple fallback strategies |
| Session startup fails | High | Verify 5-skill protocol works |

---

## Success Criteria

✅ All quick_commands valid and tested
✅ All .env and config.yaml synced
✅ `hermes doctor` clean (0 issues)
✅ `hermes security audit` clean
✅ All git pushes successful
✅ No duplicate files
✅ Docker clean (no unused images/containers/volumes)
✅ All MCP servers working with skills
✅ Session startup works (5 skills loaded)
✅ All judge skills score 99+
✅ Rate limiting bypassed for all providers