# SPEC: MCP Server Suite Setup

**Workstream:** 02-mcp-server-suite
**Priority:** P1 - Enabler
**Dependencies:** 01-config-foundation-repair (config must be valid)
**Profile:** adminbot

---

## Problem Statement

14+ MCP servers need to be installed, configured, tested, and verified. Currently some may not be enabled or may have credential issues. MCP-first tool precedence requires all servers operational.

## Required MCP Servers (14+)

| Server | Purpose | Credentials Needed |
|--------|---------|-------------------|
| github | Repository management, issues, PRs | GitHub token |
| filesystem | File read/write/edit | None (local) |
| playwright | Browser automation | None |
| fetch | Web content extraction | None |
| tavily | Web search | Tavily API key |
| neon | Database operations | Neon API key |
| docker | Container management | Docker socket |
| memory | Knowledge graph | None |
| honcho | Cross-session memory | Honcho API key |
| ast-grep | AST-based code search | None |
| code-sandbox | Isolated code execution | None |
| sentry | Error tracking | Sentry DSN |
| context7 | Library docs resolution | Context7 API key |
| sequential-thinking | Structured reasoning | None |
| smithery | Toolbox search/management | None |

## Requirements

### Functional
- [ ] All 14+ servers show as `enabled` in `hermes mcp list`
- [ ] `hermes mcp test <server>` passes for each server
- [ ] Credentials configured via vault_key_sync (not hardcoded)
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

## Implementation Approach

```bash
# 1. Ensure config valid (prerequisite)
hermes config validate

# 2. List current state
hermes mcp list

# 3. For each missing/disabled server:
hermes mcp add <server> --config '{"key": "value"}'

# 4. Sync vault keys for credentialed servers
python3 ~/AppData/Local/hermes/scripts/vault_key_sync.py --live-test --write

# 5. Test all
for server in github filesystem playwright fetch tavily neon docker memory honcho ast-grep code-sandbox sentry context7 sequential-thinking smithery; do
  echo "Testing $server..."
  hermes mcp test $server
done
```

## Credential Management

- **vault_key_sync.py**: Live-tests keys from `~/Desktop/Github/*.txt`, writes working keys to hermes + repo `.env`
- **env_sync.py**: Legacy sync (deprecated)
- **validate_services.py**: Live validation of all configured services
- **Preferred**: MCP gateways (e.g., `https://mcp.neon.tech/mcp` with Bearer token)
- **Accept headers**: `application/json, text/event-stream`

## Verification Steps

```bash
# Full test suite
cd ~/AppData/Local/hermes
for s in github filesystem playwright fetch tavily neon docker memory honcho ast-grep code-sandbox sentry context7 sequential-thinking smithery; do
  hermes mcp test $s 2>&1 | head -5
done

# Verify tools discovered
hermes tools list | grep -i mcp

# Test MCP-first precedence: try a filesystem operation via MCP
# Should use MCP filesystem tools, not native terminal/read_file
```

## Risks

- **Neon official MCP is REMOTE** at https://mcp.neon.tech/mcp (not local npm package)
- **Windows npx quirk**: bare `npx` fails in Python subprocess → use `C:\nvm4w\nodejs\npx.cmd`
- **Context7**: HTTP endpoint `https://mcp.context7.com/mcp` with `CONTEXT7_API_KEY`
- **Tavily**: Requires API key from tavily.com
- **Rate limits**: Some free tiers have limits; configure fallbacks

## References

- MEMORY.md: "Neon official MCP is REMOTE at https://mcp.neon.tech/mcp (Bearer); npm @neondatabase/mcp-server-neon deprecated"
- MEMORY.md: "Windows: bare `npx` fails in Python subprocess (WinError 2) — use C:\nvm4w\nodejs\npx.cmd"
- MEMORY.md: "context7: HTTP https://mcp.context7.com/mcp with CONTEXT7_API_KEY. Provides resolve-library-id + query-docs. Verified 2026-08-19."
- `~/AppData/Local/hermes/scripts/vault_key_sync.py`
- `~/AppData/Local/hermes/scripts/validate_services.py`