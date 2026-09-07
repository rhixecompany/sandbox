---
name: 01-config-foundation-repair
title: Config & Foundation Repair
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

Fix YAML corruption in config.yaml and ensure all Hermes operations function correctly. Repair the config foundation so that all 14+ MCP servers load properly and profile persistence works.

## Requirements

### Functional
- [ ] Fix YAML syntax error at line 958 (and any others found during full parse)
- [ ] Ensure all `mcp_servers.*.args` are YAML lists, not JSON strings (pattern: `args: '["arg1","arg2"]'` → `args:\n  - "arg1"\n  - "arg2"`)
- [ ] `hermes config validate` exits 0 with no errors
- [ ] `hermes config get` works for all keys
- [ ] Profile_name persists in state.db sessions table (currently `None`)

### Non-Functional
- [ ] No backup files created (use git for rollback)
- [ ] Fix applied via python file I/O (not `patch`/`write_file` - security guard)
- [ ] Verification within 30 seconds of fix

## Acceptance Criteria

| Check | Command | Expected |
|-------|---------|----------|
| Config valid | `hermes config validate` | Exit 0, no YAML errors |
| MCP list | `hermes mcp list` | All 14+ servers shown, enabled |
| Profile persist | New session → check state.db | `profile_name` = "default" not `None` |
| No corruption backups | `ls config.yaml.corrupt.*` | No new corrupt files after fix |
| Config get works | `hermes config get model.provider` | Returns valid provider name |

## Non-Functional Requirements

Fix must be applied via Python file I/O directly (not patch/write_file tools) due to security guard. No backup files created in hermes config directory — git is used for rollback. Verification completes within 30 seconds of applying the fix. All changes tested before marking complete.

## Verification

```bash
# 1. Validate config
hermes config validate
# Expected: Exit 0, no YAML errors

# 2. List MCP servers
hermes mcp list
# Expected: All 14+ servers shown, enabled

# 3. Test each MCP server
for s in github filesystem playwright fetch tavily neon docker memory honcho ast-grep code-sandbox sentry context7 sequential-thinking smithery; do
  hermes mcp test $s
done
# Expected: Each server returns connected

# 4. Start new session, verify profile_name
# (Check state.db after new session starts)
# Expected: profile_name = "default" not None

# 5. Verify no new corrupt backups
ls ~/AppData/Local/hermes/config.yaml.corrupt.* 2>/dev/null || echo "No corrupt backups found"
```

## Linked Specs
- 01-config-foundation-repair.md

## Linked Plan
- ../skill-implementation-master-plan.md
- ../2026-08-15_hermes-profile-skills-enhancement-plan.md
