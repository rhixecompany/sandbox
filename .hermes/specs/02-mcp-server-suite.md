---
name: 02-mcp-server-suite
title: MCP Server Suite Setup
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

Install, configure, test, and verify all 14+ MCP servers are operational for Hermes Agent. Ensure MCP-first tool precedence is working and credentials are managed via vault_key_sync without hardcoded secrets.

## Requirements

### Functional
- [ ] All 14+ servers show as `enabled` in `hermes mcp list`
- [ ] `hermes mcp test <server>` passes for each server (github, filesystem, playwright, fetch, tavily, neon, docker, memory, honcho, ast-grep, code-sandbox, sentry, context7, sequential-thinking, smithery)
- [ ] Credentials configured via vault_key_sync (not hardcoded in config.yaml)
- [ ] MCP tools discoverable and preferred over native equivalents
- [ ] Context7 resolves library IDs correctly
- [ ] Sequential-thinking chain-of-thought works
- [ ] Neon MCP connects to remote https://mcp.neon.tech/mcp (Bearer auth)

### Non-Functional
- [ ] Test each server in < 10 seconds
- [ ] No hardcoded credentials in config.yaml
- [ ] Windows npx path: `C:\nvm4w\nodejs\npx.cmd` (bare `npx` fails in Python subprocess)

## Acceptance Criteria

| Check | Command | Expected |
|-------|---------|----------|
| List servers | `hermes mcp list` | 14+ enabled |
| Test github | `hermes mcp test github` | ✓ Connected, tools discovered |
| Test filesystem | `hermes mcp test filesystem` | ✓ Connected |
| Test playwright | `hermes mcp test playwright` | ✓ Connected |
| Test fetch | `hermes mcp test fetch` | ✓ Connected |
| Test tavily | `hermes mcp test tavily` | ✓ Connected |
| Test neon | `hermes mcp test neon` | ✓ Connected (remote) |
| Test docker | `hermes mcp test docker` | ✓ Connected |
| Test memory | `hermes mcp test memory` | ✓ Connected |
| Test honcho | `hermes mcp test honcho` | ✓ Connected |
| Test ast-grep | `hermes mcp test ast-grep` | ✓ Connected |
| Test code-sandbox | `hermes mcp test code-sandbox` | ✓ Connected |
| Test sentry | `hermes mcp test sentry` | ✓ Connected |
| Test context7 | `hermes mcp test context7` | ✓ Connected |
| Test sequential-thinking | `hermes mcp test sequential-thinking` | ✓ Connected |
| Test smithery | `hermes mcp test smithery` | ✓ Connected |
| Tools preferred | `hermes tools list \| grep mcp` | MCP tools listed |

## Non-Functional Requirements

Each MCP server must be tested within 10 seconds. No hardcoded credentials in config.yaml — all credentials managed via vault_key_sync.py. Windows-specific: bare `npx` fails in Python subprocess; use `C:\nvm4w\nodejs\npx.cmd`. Neon official MCP is REMOTE at https://mcp.neon.tech/mcp with Bearer token. Context7 uses HTTP endpoint https://mcp.context7.com/mcp with CONTEXT7_API_KEY.

## Verification

```bash
# Full test suite
cd ~/AppData/Local/hermes
for s in github filesystem playwright fetch tavily neon docker memory honcho ast-grep code-sandbox sentry context7 sequential-thinking smithery; do
  hermes mcp test $s 2>&1 | head -5
done
# Expected: All servers show connected

# Verify tools discovered
hermes tools list | grep -i mcp
# Expected: MCP tools listed

# Test MCP-first precedence: try a filesystem operation via MCP
# Should use MCP filesystem tools, not native terminal/read_file
```

## Linked Specs
- 02-mcp-server-suite.md

## Linked Plan
- ../skill-implementation-master-plan.md
- ../provider-workflow-master-plan.md
