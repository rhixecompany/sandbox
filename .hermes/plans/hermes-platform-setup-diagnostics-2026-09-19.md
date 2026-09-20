---
goal: Hermes Platform Setup & Diagnostics — Full Platform Configuration, Plugin/Hook/MCP Enablement, Diagnostics, Git Operations, and Filesystem Cleanup
version: 1.0.0
date_created: 2026-09-19
owner: default
status: in_progress
tags: [feature, infrastructure, process, architecture, design]
---

# Introduction

![Status: in_progress](https://img.shields.io/badge/status-in_progress-yellow)

Comprehensive plan to configure, diagnose, repair, and verify the Hermes Agent platform across all agents (Hermes, Copilot, Codex, OpenCode, Vscode). Covers config enhancement, memory consolidation, plugin/hook/MCP enablement, diagnostics, git operations, scripts quick_commands, .env sync, and filesystem triage/dedupe.

## 1. Requirements & Constraints

- **REQ-001**: Diff and enhance `$HERMES_HOME/config.yaml` without conflicts; verify with `hermes config` CLI
- **REQ-010**: Consolidate SOUL.md/USER.md/MEMORY.md from repo root into `$HERMES_HOME/`; delete originals
- **REQ-020**: Create writing-{spec|plan|prompt} skills with proper folder structure and content
- **REQ-030**: Update `/multi-file-change-protocol` skill with cross-references to all related skills
- **REQ-040**: Run full Hermes diagnostics suite (doctor, security audit, status, insights, logs)
- **REQ-050**: Enable, debug, fix, verify all Hermes plugins and hooks
- **REQ-060**: Configure, debug, fix, enable all MCP servers across all agents
- **REQ-070**: Debug, fix, sync Vscode/OpenCode/Hermes/Copilot/Codex MCP servers
- **REQ-080**: Git add/commit/push across repo and subrepos on clean-development, development, production
- **REQ-090**: Ensure all scripts have valid quick_commands in config.yaml
- **REQ-100**: Triage, dedupe, consolidate files in repo and Hermes root

- **CON-001**: Destructive operations approved (user confirmed)
- **CON-002**: Use DRY principles — no duplicate identity rules across files
- **CON-003**: Use MCP servers/tools to increase speed and accuracy
- **CON-004**: Subagent delegation for implementation (parallel where possible)

## 2. Implementation Steps

### Implementation Phase 1: Config & Memory Consolidation

- **GOAL-001**: Enhance config.yaml and consolidate memory files

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-001 | Diff `$HERMES_HOME/config.yaml` against backups; identify changes needed | | |
| TASK-002 | Enhance config.yaml: add quick_commands for all scripts, sync settings | | |
| TASK-003 | Verify config.yaml with `hermes config show` and `hermes config` CLI | | |
| TASK-004 | Locate all SOUL.md, USER.md, MEMORY.md in repo root and Hermes home | | |
| TASK-005 | Merge ./SOUL.md into $HERMES_HOME/SOUL.md; delete ./SOUL.md | | |
| TASK-006 | Merge ./USER.md and ./MEMORY.md into $HERMES_HOME/memories/; delete originals | | |
| TASK-007 | Merge $HERMES_HOME/USER.md and $HERMES_HOME/MEMORY.md into memories/; delete originals | | |

### Implementation Phase 2: Skills Creation

- **GOAL-002**: Create writing-{spec|plan|prompt} skills

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-010 | Create writing-spec skill: $HERMES_HOME/specs/<spec-filename>/ with SPEC.md, scripts/, verification/ | | |
| TASK-011 | Create writing-plan skill: $HERMES_HOME/plans/<spec-filename>/ with rules, steps, goal, phases, tasks, gates | | |
| TASK-012 | Create writing-prompt skill: .github/prompts/<category>/<trigger>/ with prompt.md, templates/, scripts/, verification/ | | |
| TASK-013 | Verify all three skills have valid content and folder structure | | |

### Implementation Phase 3: Multi-File Protocol Update

- **GOAL-003**: Update multi-file-change-protocol skill

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-020 | Read current multi-file-change-protocol SKILL.md | | |
| TASK-021 | Add cross-references to: using-superpowers, brainstorming, user-communication-preferences, mcp-sequential-thinking, mcp-filesystem, mcp-ast-grep, mcp-memory, writing-clearly-and-concisely, subagent-driven-development, systematic-debugging, plan, plan-mode, plans-and-specs, implementation-{skill|specs|plans|prompts}, update-implementation-{skill|specs|plans|prompts}, create-implementation-{skill|specs|plans|prompts}, executing-{specs|plans|prompts}, {skill|specs|plans|prompts}-judge, writing-{spec|plan|prompt} | | |
| TASK-022 | Verify updated skill loads correctly via skill_view | | |

### Implementation Phase 4: Diagnostics & Repair

- **GOAL-004**: Run full Hermes diagnostics and fix all issues

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-030 | Execute `hermes doctor` in background; capture output | | |
| TASK-031 | Execute `hermes doctor --fix` in background; capture output | | |
| TASK-032 | Execute `hermes security audit` in background; capture output | | |
| TASK-033 | Execute `hermes status` and `hermes insights` in background; capture output | | |
| TASK-034 | Execute `hermes logs list` in background; capture output | | |
| TASK-035 | Execute `hermes logs errors`, `hermes logs desktop`, `hermes logs gateway`, `hermes logs gui`, `hermes logs agent` in background; capture output | | |
| TASK-036 | Execute `bun run check` in SandBox repo; capture output | | |
| TASK-037 | Use `/systematic-debugging` to triage all diagnostic output; identify bugs, issues, warnings, errors | | |
| TASK-038 | Debug, fix, verify all identified issues | | |
| TASK-039 | Re-run diagnostics to confirm fixes (gate: hermes doctor exit 0, bun run check exit 0) | | |

### Implementation Phase 5: Plugins & Hooks

- **GOAL-005**: Enable, debug, fix, verify all plugins and hooks

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-040 | List all Hermes plugins at $HERMES_HOME/plugins/ | | |
| TASK-041 | For each plugin: enable, debug, fix, test, verify | | |
| TASK-042 | List all Hermes hooks at $HERMES_HOME/hooks/ | | |
| TASK-043 | For each hook: enable, debug, fix, test, verify; ensure every possible event is handled | | |
| TASK-044 | Update, enhance, debug, fix, verify each plugin and hook | | |
| TASK-045 | List all desktop-plugins; enable, debug, fix, verify | | |

### Implementation Phase 6: MCP Servers

- **GOAL-006**: Configure, debug, fix, enable all MCP servers

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-050 | Read `.github/mcp.json` — list all configured MCP servers | | |
| TASK-051 | Check Copilot, Codex, Hermes configs for MCP servers | | |
| TASK-052 | For each MCP server: configure, debug, fix, test, enable | | |
| TASK-053 | Ensure all MCP servers work with Hermes, Copilot, Codex, OpenCode | | |
| TASK-054 | Create skills for any Hermes MCP servers without skills | | |
| TASK-055 | Create plugins/hooks/scripts/skills to bypass rate-limit errors | | |

### Implementation Phase 7: Vscode/OpenCode/MCP Sync

- **GOAL-007**: Debug, fix, sync all agent MCP servers

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-060 | Debug, fix all failed Vscode MCP servers | | |
| TASK-061 | Debug, fix all failed OpenCode MCP servers | | |
| TASK-062 | Ensure Hermes, Copilot, Codex MCP servers synced and working | | |
| TASK-063 | Sync hooks, skills, scripts, .env, prompts, plugins, config.yaml from Hermes root into repo | | |
| TASK-064 | Sync Hermes default profile configs with each Hermes profile | | |

### Implementation Phase 8: Git Operations

- **GOAL-008**: Git add/commit/push across all branches and subrepos

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-070 | `git add -A` on repo and all subrepos | | |
| TASK-071 | `git commit -m "platform setup: config, plugins, hooks, MCP, diagnostics"` | | |
| TASK-072 | `git push -u origin clean-development` in background without timeout | | |
| TASK-073 | `/systematic-debugging` — fix blockers, retry until push succeeds | | |
| TASK-074 | `git push -u origin development` in background without timeout | | |
| TASK-075 | `git push -u origin production` in background without timeout | | |
| TASK-076 | Verify all pushes succeeded on repo and all subrepos | | |

### Implementation Phase 9: Scripts & Quick Commands

- **GOAL-009**: Ensure all scripts have valid quick_commands

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-080 | List all scripts at $HERMES_HOME/scripts/ | | |
| TASK-081 | For each script: verify it has a quick_command in config.yaml | | |
| TASK-082 | Add missing quick_commands to config.yaml | | |
| TASK-083 | Test each quick_command via `hermes <command>` | | |
| TASK-084 | Update scripts-judge skill to validate quick_commands | | |

### Implementation Phase 10: Filesystem Cleanup

- **GOAL-010**: Triage, dedupe, consolidate files

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-090 | List all files in repo and Hermes root; provide summary of purpose | | |
| TASK-091 | Identify duplicates between repo and Hermes root | | |
| TASK-092 | Deduplicate, consolidate, delete duplicate files | | |
| TASK-093 | Suggest cleanup plan for Docker images, builds, containers, volumes, models, MCP toolkit | | |
| TASK-094 | Create cleanup spec, plan, scripts for Docker cleanup (if approved) | | |

## 3. Alternatives

- **ALT-001**: Run all diagnostics sequentially in one session instead of subagent delegation — simpler but slower
- **ALT-002**: Skip plugins/hooks phase and focus only on MCP servers — narrower scope
- **ALT-003**: Defer git operations to end of all other work — avoids premature commits

## 4. Dependencies

- **DEP-001**: Hermes CLI must be functional (hermes doctor should pass first)
- **DEP-002**: Git credentials must be configured for push operations
- **DEP-003**: Subagent availability for parallel work (if using subagent delegation)
- **DEP-004**: Network access for hermes doctor, security audit, logs, insights

## 5. Files

- **FILE-001**: `$HERMES_HOME/config.yaml` — primary config (enhanced)
- **FILE-002**: `$HERMES_HOME/SOUL.md` — consolidated soul file
- **FILE-003**: `$HERMES_HOME/memories/USER.md` — consolidated user file
- **FILE-004**: `$HERMES_HOME/memories/MEMORY.md` — consolidated memory file
- **FILE-005**: `$HERMES_HOME/specs/hermes-platform-setup-diagnostics/SPEC.md` — this spec
- **FILE-006**: `.hermes/plans/hermes-platform-setup-diagnostics-2026-09-19.md` — this plan
- **FILE-007**: `.github/mcp.json` — MCP server configuration
- **FILE-008**: `$HERMES_HOME/scripts/*.py` / `$HERMES_HOME/scripts/*.sh` — scripts with quick_commands
- **FILE-009**: `$HERMES_HOME/plugins/` — plugin directory
- **FILE-010**: `$HERMES_HOME/hooks/` — hook directory

## 6. Testing

- **TEST-001**: `hermes doctor` exits 0
- **TEST-002**: `hermes security audit` exits 0 or acceptable findings
- **TEST-003**: `bun run check` exits 0 in SandBox
- **TEST-004**: `hermes mcp list` shows all servers enabled
- **TEST-005**: `hermes plugins list` shows all plugins enabled
- **TEST-006**: `hermes hooks list` shows all hooks enabled
- **TEST-007**: All quick_commands test successfully via `hermes <command>`
- **TEST-008**: Git push succeeds on clean-development, development, production

## 7. Risks & Assumptions

- **RISK-001**: Some plugins/hooks may be incompatible with current Hermes version — may require updates or removal
- **RISK-002**: MCP server configuration may conflict between agents — may need per-agent config variants
- **RISK-003**: Git push may fail due to authentication or network issues — may need manual intervention
- **RISK-004**: Some diagnostic commands may hang or timeout — use background execution with timeout
- **ASSUMPTION-001**: User has approved all destructive operations (confirmed)
- **ASSUMPTION-002**: Hermes home path is `C:\Users\Alexa\AppData\Local\hermes`
- **ASSUMPTION-003**: SandBox repo path is `C:\Users\Alexa\Desktop\SandBox`
- **ASSUMPTION-004**: Subagent delegation is available for parallel work

## 8. Linked Scope and Design

- **Scope**: `../docs/scope/scope.md` — defines WHAT this plan builds (Hermes platform setup & diagnostics)
- **Design**: `../DESIGN.md` — defines visual tokens if this plan produces UI (N/A for this plan)

## 9. Related Specifications / Further Reading

- **Spec**: `$HERMES_HOME/specs/hermes-platform-setup-diagnostics/SPEC.md`
- **Provider/Model Testing**: Separate spec + plan (not in this plan's scope)
- **Skills Library Enhancement**: Separate spec + plan (not in this plan's scope)

---

## Verification Checklist

- [ ] SPEC.md exists at `$HERMES_HOME/specs/hermes-platform-setup-diagnostics/SPEC.md`
- [ ] All 10 phases defined with tasks, dependencies, and acceptance criteria
- [ ] All REQ-XXX requirements have corresponding TASK-XXX or TEST-XXX
- [ ] Diagnostic commands identified with background execution and logging
- [ ] Gate conditions defined for each phase (hermes doctor exit 0, bun run check exit 0, etc.)
- [ ] Subagent delegation plan documented (if using subagents)
- [ ] Scope and design files referenced
- [ ] All file paths are absolute or relative to known roots
- [ ] No secrets or .env contents in plan
