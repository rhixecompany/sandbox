# MCP Audit Report — 2026-09-05T03:24:54

**Registry:** `.mcp\registry.json`

## Summary

| Status | Count |
|--------|-------|
| ✓ PASS | 28 |
| ⚠ WARN | 4 |
| ✗ FAIL | 0 |
| ⊘ SKIP | 0 |
| **Total** | **32** |

## Server Status

| # | Server | Type | Status | Details |
|---|--------|------|--------|---------|
| 1 | `anthropic-resources` | http | PASS | ✓ https://resources.anthropic.com/mcp: HTTP 404 (reachable) |
| 2 | `ast-grep` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: @notprolands/ast-grep-mcp |
| 3 | `atlassian` | sse | PASS | ✓ https://mcp.atlassian.com/v1/sse: HTTP 401 (reachable) |
| 4 | `code-sandbox` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: node-code-sandbox-mcp |
| 5 | `context7` | http | PASS | ✓ https://mcp.context7.com/mcp: HTTP 405 (reachable) |
| 6 | `django` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: django-mcp |
| 7 | `docs` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: docs-mcp<br>· args[2]: docs/ |
| 8 | `evals` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: @modelcontextprotocol/server-evals |
| 9 | `everart` | http | WARN | ⚠ https://mcp.everart.ai/mcp: unreachable (URLError) |
| 10 | `fetch` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: mcp-server-fetch-typescript |
| 11 | `filesystem` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: @modelcontextprotocol/server-filesystem<br>· args[2]: C:/Users/Alexa<br>· args[3]: C:/Users/Alexa/AppData/Local/hermes<br>✓ args[4]: workspace placeholder (OK) |
| 12 | `github` | stdio | WARN | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: @modelcontextprotocol/server-github<br>⚠ env.GITHUB_PERSONAL_ACCESS_TOKEN: unresolved placeholder ${env:GITHUB_TOKEN} |
| 13 | `honcho` | http | PASS | ✓ https://mcp.honcho.dev/: HTTP 401 (reachable) |
| 14 | `mcp-docker` | stdio | PASS | ✓ command on PATH: docker -> C:\Program Files\Docker\Docker\resources\bin\docker.EXE<br>· args[0]: mcp<br>· args[1]: gateway<br>· args[2]: run<br>· args[3]: --profile<br>· args[4]: adminbot |
| 15 | `memory` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: @modelcontextprotocol/server-memory |
| 16 | `mindstudio` | stdio | PASS | ✓ command path exists: C:\Users\Alexa\.mindstudio\bin\mindstudio.exe<br>· args[0]: mcp |
| 17 | `neon` | http | PASS | ✓ https://mcp.neon.tech/mcp: HTTP 401 (reachable) |
| 18 | `parallel-search` | http | PASS | ✓ https://search.parallel.ai/mcp: HTTP 405 (reachable) |
| 19 | `parallel-task` | http | PASS | ✓ https://task-mcp.parallel.ai/mcp: HTTP 405 (reachable) |
| 20 | `plaid` | http | WARN | ⚠ https://mcp.plaid.com/mcp: unreachable (URLError) |
| 21 | `playwright` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: @playwright/mcp@0.0.78 |
| 22 | `postgres` | stdio | WARN | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: postgres-mcp<br>⚠ env.DATABASE_URL: unresolved placeholder ${env:DATABASE_URL} |
| 23 | `pytest` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: pytest-mcp |
| 24 | `python-quality` | stdio | PASS | ✓ command path exists: C:\Users\Alexa\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe<br>✓ args[0]: C:\Users\Alexa\AppData\Local\hermes\scripts\python_quality_mcp_server.py |
| 25 | `sentry` | http | PASS | ✓ https://mcp.sentry.dev/mcp: HTTP 401 (reachable) |
| 26 | `sequential-thinking` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: @modelcontextprotocol/server-sequential-thinking |
| 27 | `smithery` | http | PASS | ✓ https://mcp.smithery.ai/alexanderrhixe30: HTTP 405 (reachable) |
| 28 | `stripe` | http | PASS | ✓ https://mcp.stripe.com/mcp: HTTP 404 (reachable) |
| 29 | `tavily` | http | PASS | ✓ https://mcp.tavily.com/mcp/?tavilyApiKey=tvly-dev-3qid56-RU7ijydkVpR89PP5CFm9lg5: HTTP 405 (reachable) |
| 30 | `time` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: @modelcontextprotocol/server-time |
| 31 | `tooling-config` | stdio | PASS | ✓ command path exists: C:\Users\Alexa\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe<br>✓ args[0]: C:\Users\Alexa\AppData\Local\hermes\scripts\tooling_config_mcp_server.py |
| 32 | `tooling-lint` | stdio | PASS | ✓ command path exists: C:\Users\Alexa\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe<br>✓ args[0]: C:\Users\Alexa\AppData\Local\hermes\scripts\tooling_lint_mcp_server.py |
