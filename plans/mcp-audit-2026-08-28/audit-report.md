# MCP Audit Report — 2026-09-08T03:13:32

**Registry:** `.mcp\registry.json`

## Summary

| Status | Count |
|--------|-------|
| ✓ PASS | 26 |
| ⚠ WARN | 1 |
| ✗ FAIL | 0 |
| ⊘ SKIP | 10 |
| **Total** | **37** |

## Server Status

| # | Server | Type | Status | Details |
|---|--------|------|--------|---------|
| 1 | `anthropic-resources` | http | SKIP | ⊘ disabled in registry |
| 2 | `ast-grep` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: @notprolands/ast-grep-mcp |
| 3 | `atlassian` | sse | PASS | ✓ https://mcp.atlassian.com/v1/sse: HTTP 401 (reachable) |
| 4 | `cloudinary` | http | PASS | ✓ https://asset-management.mcp.cloudinary.com/mcp: HTTP 405 (reachable) |
| 5 | `code-sandbox` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: node-code-sandbox-mcp |
| 6 | `context7` | http | PASS | ✓ https://mcp.context7.com/mcp: HTTP 405 (reachable) |
| 7 | `django` | stdio | SKIP | ⊘ disabled in registry |
| 8 | `docs` | stdio | SKIP | ⊘ disabled in registry |
| 9 | `evals` | stdio | SKIP | ⊘ disabled in registry |
| 10 | `everart` | http | SKIP | ⊘ disabled in registry |
| 11 | `fetch` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: mcp-server-fetch-typescript |
| 12 | `filesystem` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: @modelcontextprotocol/server-filesystem<br>· args[2]: C:/Users/Alexa<br>· args[3]: C:/Users/Alexa/AppData/Local/hermes<br>✓ args[4]: workspace placeholder (OK) |
| 13 | `github` | stdio | WARN | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: @modelcontextprotocol/server-github<br>⚠ env.GITHUB_PERSONAL_ACCESS_TOKEN: unresolved placeholder ${env:GITHUB_TOKEN} |
| 14 | `honcho` | http | PASS | ✓ https://mcp.honcho.dev/: HTTP 401 (reachable) |
| 15 | `mcp-docker` | stdio | PASS | ✓ command on PATH: docker -> C:\Program Files\Docker\Docker\resources\bin\docker.EXE<br>· args[0]: mcp<br>· args[1]: gateway<br>· args[2]: run<br>· args[3]: --profile<br>· args[4]: adminbot |
| 16 | `memory` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: @modelcontextprotocol/server-memory |
| 17 | `mindstudio` | stdio | PASS | ✓ command path exists: C:\Users\Alexa\.mindstudio\bin\mindstudio.exe<br>· args[0]: mcp |
| 18 | `neon` | http | PASS | ✓ https://mcp.neon.tech/mcp: HTTP 401 (reachable) |
| 19 | `parallel-search` | http | PASS | ✓ https://search.parallel.ai/mcp: HTTP 405 (reachable) |
| 20 | `parallel-task` | http | PASS | ✓ https://task-mcp.parallel.ai/mcp: HTTP 405 (reachable) |
| 21 | `paypal` | http | PASS | ✓ https://mcp.paypal.com/sse: HTTP 401 (reachable) |
| 22 | `plaid` | http | SKIP | ⊘ disabled in registry |
| 23 | `playwright` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: @playwright/mcp@0.0.78 |
| 24 | `postgres` | stdio | SKIP | ⊘ disabled in registry |
| 25 | `pytest` | stdio | SKIP | ⊘ disabled in registry |
| 26 | `python-quality` | stdio | PASS | ✓ command path exists: C:\Users\Alexa\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe<br>✓ args[0]: C:\Users\Alexa\AppData\Local\hermes\scripts\python_quality_mcp_server.py |
| 27 | `sentry` | http | PASS | ✓ https://mcp.sentry.dev/mcp: HTTP 401 (reachable) |
| 28 | `sequential-thinking` | stdio | PASS | ✓ command: bunx (resolved at runtime)<br>· args[0]: -y<br>· args[1]: @modelcontextprotocol/server-sequential-thinking |
| 29 | `smithery` | http | PASS | ✓ https://mcp.smithery.ai/alexanderrhixe30: HTTP 405 (reachable) |
| 30 | `stripe` | http | SKIP | ⊘ disabled in registry |
| 31 | `supabase` | http | PASS | ✓ https://mcp.supabase.com/mcp: HTTP 401 (reachable) |
| 32 | `tavily` | http | PASS | ✓ https://mcp.tavily.com/mcp/?tavilyApiKey=tvly-dev-3qid56-RU7ijydkVpR89PP5CFm9lg5: HTTP 405 (reachable) |
| 33 | `time` | stdio | SKIP | ⊘ disabled in registry |
| 34 | `tooling-config` | stdio | PASS | ✓ command path exists: C:\Users\Alexa\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe<br>✓ args[0]: C:\Users\Alexa\AppData\Local\hermes\scripts\tooling_config_mcp_server.py |
| 35 | `tooling-lint` | stdio | PASS | ✓ command path exists: C:\Users\Alexa\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe<br>✓ args[0]: C:\Users\Alexa\AppData\Local\hermes\scripts\tooling_lint_mcp_server.py |
| 36 | `twilio-docs` | http | PASS | ✓ https://mcp.twilio.com/docs: HTTP 405 (reachable) |
| 37 | `vercel` | http | PASS | ✓ https://mcp.vercel.com: HTTP 401 (reachable) |
