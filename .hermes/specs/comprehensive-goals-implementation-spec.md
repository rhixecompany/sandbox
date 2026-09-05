---
name: comprehensive-goals-implementation-spec
title: Comprehensive Goals Implementation Specification
description: "Define requirements for Hermes Agent configuration, debugging, sync, cleanup, and release across SandBox and Hermes root."
version: 2.1.0
author: Alexa
license: MIT
tags: [hermes, config, debugging, sync, cleanup, docker, git, mcp, hooks, plugins, agents]
status: approved
owner: Alexa
plan: .hermes/plans/comprehensive-goals-implementation-plan.md
---

# Comprehensive Goals Implementation Specification

## Goal
Implement all user-requested goals for Hermes Agent configuration, systematic debugging, environment synchronization, file management, cleanup, MCP server health, session management, health checks, and rate limit handling across the SandBox repository and Hermes root installation.

## Project Overview
- **Project**: Hermes Agent Configuration & Debugging
- **Repository**: rhixecompany/sandbox (C:/Users/Alexa/Desktop/SandBox)
- **Hermes Root**: C:/Users/Alexa/AppData/Local/hermes
- **Profile**: default
- **Model**: nemotron-3-ultra-free (opencode-zen)

## Requirements

### Functional Requirements

#### FR1: Quick Commands System
- All scripts in SandBox/scripts and Hermes/scripts must have valid quick_commands in config.yaml
- Quick commands must be testable via `hermes_quick_commands.py audit`
- Commands must pass smoke test (execute without errors) - **< 60 seconds for 265 scripts**
- Registry must pass verification (no issues) - **0 issues**

#### FR2: Environment Synchronization
- All .env files in SandBox and Hermes root must be inventoried - **20 in SandBox, 57 in Hermes**
- All config.yaml files in Hermes profiles must be inventoried - **14 profiles + 1 root + 1 snapshot**
- Changes to root config.yaml must propagate to profile configs - **sync verification passes with 0 diffs**
- Changes to .env files must be tracked - **variable names only, no values**

#### FR3: Systematic Debugging
- All Hermes desktop issues must be identified and fixed - **hermes doctor: 0 issues**
- All plugin issues must be identified and fixed - **hermes plugins list: clean**
- All hook issues must be identified and fixed - **hermes hooks list: clean**
- All script issues must be identified and fixed - **scripts-judge: ≥ 98**
- All agent issues must be identified and fixed - **agent provider matrix: all verified**

#### FR4: Git Operations
- All changes must be committed with conventional commit messages - **type: description format**
- Changes must be pushed to clean-development, development, and production branches - **3 branches**
- Push must succeed on all branches - **3/3 success**

#### FR5: File Management
- All files in both repositories must be listed with purpose - **100% coverage**
- Duplicate files must be identified and consolidated - **0 duplicates**
- Unused files must be deleted - **0 unused**
- File inventory must be documented - **inventory.json created**

#### FR6: Cleanup Operations
- Unused Docker images, containers, volumes, builds must be removed - **docker system df: clean**
- Unused models must be removed - **0 unused models**
- Unused MCP toolkit components must be removed - **0 unused**
- Unused AI agent configurations must be removed - **0 unused**

#### FR7: MCP Server Health
- All 17+ MCP servers must pass `hermes mcp test` - **17/17 pass**
- Failed servers (VSCode, OpenCode, Hermes, Copilot, Codex) must be fixed - **5/5 fixed**
- MCP configurations must be synced across profiles - **14/14 synced**
- Skills must exist for all MCP servers - **17/17 skills**

#### FR8: Session Management
- Session startup must load 5 mandatory skills - **5/5 loaded**
- Session end must generate SESSION_REPORT.md - **generated on end**
- Context files must be valid - **validated on startup**
- System prompts must be correct - **verified on load**

#### FR9: Health Checks
- `hermes doctor` must pass with 0 issues - **0 issues**
- `hermes doctor --fix` must resolve all auto-fixable issues - **applied**
- `hermes security audit` must pass - **clean**
- `hermes status` must show healthy state - **healthy**
- `hermes insights` must run without errors - **no errors**
- All log commands must run without errors - **no errors**
- `bun run check` must pass - **pass**

#### FR10: Rate Limit Handling
- Rate limit errors must be bypassed for all providers - **all providers bypassed**
- Plugins/hooks/scripts/skills must implement bypass strategies - **implemented**
- Fallback chain must work: openrouter → nous → opencode-zen - **verified**

### Non-Functional Requirements

#### NFR1: Performance
- Quick command generation: < 30 seconds
- Smoke test for 265 scripts: < 60 seconds
- Environment sync: < 10 seconds
- Docker cleanup: < 5 minutes

#### NFR2: Reliability
- All operations must be idempotent
- Rollback must be possible for all changes
- No data loss during cleanup

#### NFR3: Maintainability
- All scripts must have quick_commands
- All skills must follow SKILL.md format
- All plans must follow .hermes/plans/ format
- Documentation must be updated with changes

#### NFR4: Security
- No secrets in output or config.yaml
- .env files must not be committed
- Credential pool strategies must be maintained

## Technical Specifications

### Quick Commands Architecture
```
config.yaml
  └── quick_commands: {key: {type: "exec"|"alias", command: "...", target?: "..."}}
```

Generated commands format:
```bash
python "C:/Users/Alexa/AppData/Local/hermes/scripts/hermes_quick_commands.py" --scripts-dir "<scripts_dir>" audit -s "<script_name>"
```

### Environment Sync Architecture
```
Sync Script → 
  1. Inventory .env files (both locations)
  2. Inventory config.yaml files (all profiles)
  3. Compare and sync
  4. Validate sync
```

### Debugging Workflow
```
For each component:
  1. Run diagnostic command
  2. Parse output for issues
  3. Apply systematic-debugging (4 phases)
  4. Verify fix
  5. Document in plan
```

### MCP Server Testing
```
For each MCP server:
  1. hermes mcp test <server>
  2. If fail: debug with systematic-debugging
  3. Fix configuration
  4. Re-test
  5. Create skill if missing
```

### Judge Skills Quality Gates
Each judge skill must score ≥ 99:
- scripts-judge: Script quality
- plans-judge: Plan quality  
- prompts-judge: Prompt quality
- hooks-judge: Hook quality
- plugins-judge: Plugin quality
- specs-judge: Spec quality
- skills-judge: Skill quality

## Acceptance Criteria

### AC1: Quick Commands
- [ ] 265 scripts have quick_commands
- [ ] All 272 commands pass smoke test
- [ ] Registry verification passes (0 issues)

### AC2: Environment Sync
- [ ] All .env files inventoried (20 in SandBox, 2 in Hermes)
- [ ] All config.yaml files inventoried (14 profiles + 1 root + 1 snapshot)
- [ ] Sync script created and tested

### AC3: Debugging
- [ ] hermes doctor: 0 issues
- [ ] hermes doctor --fix: all auto-fixes applied
- [ ] hermes security audit: clean
- [ ] All logs: no errors

### AC4: Git
- [ ] All changes committed
- [ ] Push to clean-development: success
- [ ] Push to development: success
- [ ] Push to production: success

### AC5: File Management
- [ ] Complete file inventory for both locations
- [ ] 0 duplicate files
- [ ] File purpose document created

### AC6: Cleanup
- [ ] Docker: 0 unused images/containers/volumes
- [ ] Models: 0 unused models
- [ ] MCP toolkit: 0 unused components
- [ ] AI agents: 0 unused configs

### AC7: MCP Servers
- [ ] All 17+ MCP servers pass test
- [ ] All failed servers fixed
- [ ] Skills created for all servers

### AC8: Session
- [ ] 5-skill startup protocol works
- [ ] SESSION_REPORT.md generated on end
- [ ] Context files valid

### AC9: Health Checks
- [ ] All health commands pass
- [ ] bun run check passes

### AC10: Rate Limits
- [ ] Bypass works for all providers
- [ ] Fallback chain verified

### AC11: Quality Gates
- [ ] All 7 judge skills score ≥ 99

## File Structure

### Input Files
- SandBox/scripts/* (47 scripts)
- Hermes/scripts/* (220 scripts)
- SandBox/.env + project .env files
- Hermes/.env + .env.pre-delete
- Hermes/config.yaml + 13 profile config.yaml

### Output Files
- Updated Hermes/config.yaml (quick_commands)
- .hermes/plans/comprehensive-goals-implementation-plan.md (this file)
- .hermes/specs/comprehensive-goals-implementation-spec.md (this file)
- Sync script: scripts/sync_env_config.py
- Cleanup script: scripts/cleanup_agents_docker.py
- Debug reports: .hermes/plans/debug-reports/
- Judge reports: .hermes/plans/judge-reports/

### Modified Files
- Hermes/config.yaml
- Hermes/scripts/hermes_quick_commands.py (if needed)
- Profile config.yaml files (synced)
- Various script fixes

## Testing Strategy

### Unit Tests
- hermes_quick_commands.py: inventory, generate, audit, verify-registry, smoke
- sync_env_config.py: inventory, compare, sync, validate
- cleanup_agents_docker.py: dry-run, execute, verify

### Integration Tests
- Full quick_commands lifecycle
- Environment sync across profiles
- MCP server test suite
- Session start/end cycle
- Git push to all branches

### End-to-End Tests
- Complete plan execution
- All judge skills pass
- No regressions

## Deployment
- All changes in SandBox repo
- Config changes in Hermes root
- Profile configs synced
- Documentation updated

## Rollback Plan
1. Git revert last commit
2. Restore config.yaml from backup
3. Restore .env files from backup
4. Re-run sync if needed

## Verification
- Run specs-judge with threshold 98 on all specs in .hermes/specs/
- Run plans-judge with threshold 98 on all plans in .hermes/plans/
- Run prompts-judge with threshold 98 on all prompts in .github/prompts/
- All judge skills must score ≥ 98
- Verify all acceptance criteria are met with evidence
- Run hermes doctor and confirm 0 issues
- Run hermes security audit and confirm clean
- Verify all MCP servers pass hermes mcp test
- Confirm git push succeeds on all three branches

## Linked Plan
../plans/comprehensive-goals-implementation-plan.md