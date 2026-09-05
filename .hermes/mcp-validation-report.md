# MCP Server Validation Report — SandBox

**Generated:** 2026-09-05 00:37:06

## Summary

- **Working**: 16 servers ✅
- **Broken**: 13 servers ❌
- **Disabled**: 3 servers ⊘
- **Total**: 32 servers

## Detailed Server Status

| # | Server | Type | Status | Message | Notes |
|---|--------|------|--------|---------|-------|
| 1 | `anthropic-resources` | remote | ❌ broken | HTTP Error 404 | |
| 2 | `ast-grep` | local | ✅ working | Command available | |
| 3 | `atlassian` | remote | ⊘ disabled | Server is disabled | |
| 4 | `code-sandbox` | local | ✅ working | Command available | |
| 5 | `context7` | remote | ❌ broken | HTTP Error 405 | |
| 6 | `django` | local | ✅ working | Command available | |
| 7 | `docs` | local | ⊘ disabled | Server is disabled | |
| 8 | `evals` | local | ✅ working | Command available | |
| 9 | `everart` | remote | ❌ broken | Connection error: [Errno 11001] getaddrinfo failed | |
| 10 | `fetch` | local | ✅ working | Command available | |
| 11 | `filesystem` | local | ✅ working | Command available | |
| 12 | `github` | local | ✅ working | Command available | |
| 13 | `honcho` | remote | ❌ broken | HTTP Error 401 | |
| 14 | `mcp-docker` | local | ❌ broken | Command timeout | |
| 15 | `memory` | local | ✅ working | Command available | |
| 16 | `mindstudio` | local | ✅ working | Command available | |
| 17 | `neon` | remote | ❌ broken | HTTP Error 401 | |
| 18 | `parallel-search` | remote | ❌ broken | HTTP Error 405 | |
| 19 | `parallel-task` | remote | ❌ broken | HTTP Error 404 | |
| 20 | `plaid` | remote | ❌ broken | Connection error: [Errno 11001] getaddrinfo failed | |
| 21 | `playwright` | local | ✅ working | Command available | |
| 22 | `postgres` | local | ⊘ disabled | Server is disabled | |
| 23 | `pytest` | local | ✅ working | Command available | |
| 24 | `python-quality` | local | ✅ working | Command available | |
| 25 | `sentry` | remote | ❌ broken | HTTP Error 401 | |
| 26 | `sequential-thinking` | local | ✅ working | Command available | |
| 27 | `smithery` | remote | ❌ broken | HTTP Error 405 | |
| 28 | `stripe` | remote | ❌ broken | HTTP Error 404 | |
| 29 | `tavily` | remote | ❌ broken | HTTP Error 405 | |
| 30 | `time` | local | ✅ working | Command available | |
| 31 | `tooling-config` | local | ✅ working | Command available | |
| 32 | `tooling-lint` | local | ✅ working | Command available | |

## Issues Found

**13 broken servers:**
- `anthropic-resources`: HTTP Error 404
- `context7`: HTTP Error 405
- `everart`: Connection error: [Errno 11001] getaddrinfo failed
- `honcho`: HTTP Error 401
- `mcp-docker`: Command timeout
- `neon`: HTTP Error 401
- `parallel-search`: HTTP Error 405
- `parallel-task`: HTTP Error 404
- `plaid`: Connection error: [Errno 11001] getaddrinfo failed
- `sentry`: HTTP Error 401
- `smithery`: HTTP Error 405
- `stripe`: HTTP Error 404
- `tavily`: HTTP Error 405

## Environment Variables Status

| Variable | Status | Value Preview |
|----------|--------|----------------|
| `GITHUB_TOKEN` | ❌ | NOT SET |
| `TAVILY_API_KEY` | ✅ | tvly-dev-3qid56-RU7i... |
| `DATABASE_URL` | ❌ | NOT SET |
| `OPENCODE_ZEN_API_KEY` | ✅ | sk-HpBeCoY7syJu2eyM5... |

## Configuration Files Status

- ✅ `opencode.json`: C:\Users\Alexa\Desktop\SandBox\opencode.json
- ✅ `.copilot/mcp.json`: C:\Users\Alexa\Desktop\SandBox\.copilot\mcp.json
- ✅ `.codex/mcp.json`: C:\Users\Alexa\Desktop\SandBox\.codex\mcp.json
- ✅ `Hermes config.yaml`: C:\Users\Alexa\AppData\Local\hermes\config.yaml

## Recommended Next Steps

1. **Add Missing MCP Servers**:
   - Stripe MCP for comicwise project
   - Plaid MCP for Banking project
   - Additional AI/LLM integrations

2. **Fix Broken Servers**:
   - Review configuration for `anthropic-resources`
   - Review configuration for `context7`
   - Review configuration for `everart`
   - Review configuration for `honcho`
   - Review configuration for `mcp-docker`
   - Review configuration for `neon`
   - Review configuration for `parallel-search`
   - Review configuration for `parallel-task`
   - Review configuration for `plaid`
   - Review configuration for `sentry`
   - Review configuration for `smithery`
   - Review configuration for `stripe`
   - Review configuration for `tavily`

3. **Sync Configuration**:
   - Ensure all agent configs (OpenCode, Copilot, Codex) are synchronized
   - Run sync script regularly

4. **Environment Setup**:
   - Verify all API keys are loaded correctly
   - Test remote MCP endpoints with `curl`
