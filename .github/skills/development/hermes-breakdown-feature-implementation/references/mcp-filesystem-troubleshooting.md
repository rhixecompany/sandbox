# MCP Filesystem Troubleshooting

Short diagnostics and reproducible steps to collect evidence when MCP filesystem write/create operations fail.

1. Confirm allowed directories
   - Run: hermes mcp list OR use `mcp_filesystem_list_allowed_directories()` to check which root paths are permitted. Copy the value into the log.

2. Check agent health
   - hermes status
   - hermes doctor

3. Inspect logs
   - tail -n 200 ~/.hermes/logs/agent.log
   - tail -n 200 ~/.hermes/mcp-stderr.log (if present)
   - cat ~/.hermes/gateway_state.json

4. Retry strategy
   - Create parent directories stepwise. Example:
     1) create docs
     2) create docs/ways-of-work
     3) create docs/ways-of-work/plan
     4) create docs/ways-of-work/plan/<feature>
   - Add 3 attempts with backoff: sleep 2s, 5s, 10s

5. When in doubt
   - Ask the user to create the top-level parent directory locally; this often bypasses permission / nested creation issues.

