# MCP Server Validation Report — SandBox

**Generated:** 2026-08-28 15:15:05

## Summary

- **Working**: 19 servers ✅
- **Broken**: 12 servers ❌
- **Disabled**: 0 servers ⊘
- **Total**: 31 servers

## Detailed Server Status

| # | Server | Type | Status | Message | Notes |
|---|--------|------|--------|---------|-------|
| 1 | `ast-grep` | local | ✅ working | Command available | |
| 2 | `code-sandbox` | local | ✅ working | Command available | |
| 3 | `context7` | remote | ❌ broken | HTTP Error 405 | |
| 4 | `django` | local | ✅ working | Command available | |
| 5 | `docs` | local | ✅ working | Command available | |
| 6 | `fetch` | local | ✅ working | Command available | |
| 7 | `filesystem` | local | ✅ working | Command available | |
| 8 | `github` | local | ✅ working | Command available | |
| 9 | `honcho` | remote | ❌ broken | HTTP Error 401 | |
| 10 | `mindstudio` | local | ✅ working | Command available | |
| 11 | `mcp-docker` | local | ✅ working | Command available | |
| 12 | `memory` | local | ✅ working | Command available | |
| 13 | `neon` | remote | ❌ broken | HTTP Error 401 | |
| 14 | `parallel-search` | remote | ❌ broken | HTTP Error 405 | |
| 15 | `parallel-task` | remote | ❌ broken | HTTP Error 404 | |
| 16 | `playwright` | local | ✅ working | Command available | |
| 17 | `postgres` | local | ✅ working | Command available | |
| 18 | `pytest` | local | ✅ working | Command available | |
| 19 | `python-quality` | local | ✅ working | Command available | |
| 20 | `sentry` | remote | ❌ broken | HTTP Error 401 | |
| 21 | `sequential-thinking` | local | ✅ working | Command available | |
| 22 | `smithery` | remote | ❌ broken | HTTP Error 405 | |
| 23 | `tavily` | remote | ❌ broken | HTTP Error 405 | |
| 24 | `tooling-config` | local | ✅ working | Command available | |
| 25 | `tooling-lint` | local | ✅ working | Command available | |
| 26 | `anthropic-resources` | remote | ❌ broken | HTTP Error 404 | |
| 27 | `time` | local | ✅ working | Command available | |
| 28 | `plaid` | remote | ❌ broken | Connection error: [Errno 11001] getaddrinfo failed | |
| 29 | `everart` | remote | ❌ broken | Connection error: [Errno 11001] getaddrinfo failed | |
| 30 | `evals` | local | ✅ working | Command available | |
| 31 | `stripe` | remote | ❌ broken | HTTP Error 404 | |

## Issues Found

**12 broken servers:**
- `context7`: HTTP Error 405
- `honcho`: HTTP Error 401
- `neon`: HTTP Error 401
- `parallel-search`: HTTP Error 405
- `parallel-task`: HTTP Error 404
- `sentry`: HTTP Error 401
- `smithery`: HTTP Error 405
- `tavily`: HTTP Error 405
- `anthropic-resources`: HTTP Error 404
- `plaid`: Connection error: [Errno 11001] getaddrinfo failed
- `everart`: Connection error: [Errno 11001] getaddrinfo failed
- `stripe`: HTTP Error 404

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
   - Review configuration for `context7`
   - Review configuration for `honcho`
   - Review configuration for `neon`
   - Review configuration for `parallel-search`
   - Review configuration for `parallel-task`
   - Review configuration for `sentry`
   - Review configuration for `smithery`
   - Review configuration for `tavily`
   - Review configuration for `anthropic-resources`
   - Review configuration for `plaid`
   - Review configuration for `everart`
   - Review configuration for `stripe`

3. **Sync Configuration**:
   - Ensure all agent configs (OpenCode, Copilot, Codex) are synchronized
   - Run sync script regularly

4. **Environment Setup**:
   - Verify all API keys are loaded correctly
   - Test remote MCP endpoints with `curl`
