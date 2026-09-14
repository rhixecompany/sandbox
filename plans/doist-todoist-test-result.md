=== SP-B: Doist/Todoist-AI MCP Server Test ===
Command: hermes mcp test doist/todoist-ai
Timestamp: 2026-09-14T09:56:10+01:00
Mon, Sep 14, 2026  9:56:10 AM
---

  Testing 'doist/todoist-ai'...
  Transport: HTTP → https://ai.todoist.net/mcp
  Auth: none
  ✗ Connection failed (20625ms): MCP server 'doist/todoist-ai': both Streamable HTTP and SSE transports failed (Streamable HTTP: Server returned an error response; SSE: Client error '401 Unauthorized' for url 'https://ai.todoist.net/mcp'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401). Check the URL points at an MCP endpoint, or pin `transport: sse` if the server is SSE-only.
Exit code: 0
Note: Real result — if server error, it's an external/auth blocker, not hidden.
=== Checking env for Todoist auth ===
/c/Users/Alexa/AppData/Local/hermes/config.yaml:  doist/todoist-ai:
/c/Users/Alexa/AppData/Local/hermes/config.yaml:    url: https://ai.todoist.net/mcp
.vscode/mcp.json:		"doist/todoist-ai": {
.vscode/mcp.json:			"url": "https://ai.todoist.net/mcp",
