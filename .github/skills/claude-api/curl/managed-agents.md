---
name: managed-agents-curl
description: "Reference: managed-agents-curl"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — cURL / Raw HTTP
     2|
     3|Use these examples when the user needs raw HTTP requests or is working without an SDK.
     4|
     5|## Setup
     6|
     7|```bash
     8|export ANTHROPIC_API_KEY="your-api-key"
     9|
    10|# Common headers
    11|HEADERS=(
    12|  -H "Content-Type: application/json"
    13|  -H "x-api-key: $ANTHROPIC_API_KEY"
    14|  -H "anthropic-version: 2023-06-01"
    15|  -H "anthropic-beta: managed-agents-2026-04-01"
    16|)
    17|```
    18|
    19|---
    20|
    21|## Create an Environment
    22|
    23|```bash
    24|curl -X POST https://api.anthropic.com/v1/environments \
    25|  "${HEADERS[@]}" \
    26|  -d '{
    27|    "name": "my-dev-env",
    28|    "config": {
    29|      "type": "cloud",
    30|      "networking": { "type": "unrestricted" }
    31|    }
    32|  }'
    33|```
    34|
    35|### With restricted networking
    36|
    37|```bash
    38|curl -X POST https://api.anthropic.com/v1/environments \
    39|  "${HEADERS[@]}" \
    40|  -d '{
    41|    "name": "restricted-env",
    42|    "config": {
    43|      "type": "cloud",
    44|      "networking": {
    45|        "type": "package_managers_and_custom",
    46|        "allowed_hosts": ["api.example.com"]
    47|      }
    48|    }
    49|  }'
    50|```
    51|
    52|---
    53|
    54|## Create an Agent (required first step)
    55|
    56|> ⚠️ **There is no inline agent config.** Under `managed-agents-2026-04-01`, `model`/`system`/`tools` are top-level fields on `POST /v1/agents`, not on the session. Always create the agent first — the session only takes `"agent": {"type": "agent", "id": "..."}`.
    57|
    58|### Minimal
    59|
    60|```bash
    61|# 1. Create the agent
    62|curl -X POST https://api.anthropic.com/v1/agents \
    63|  "${HEADERS[@]}" \
    64|  -d '{
    65|    "name": "Coding Assistant",
    66|    "model": "claude-opus-4-7",
    67|    "tools": [{ "type": "agent_toolset_20260401" }]
    68|  }'
    69|# → { "id": "agent_abc123", ... }
    70|
    71|# 2. Start a session
    72|curl -X POST https://api.anthropic.com/v1/sessions \
    73|  "${HEADERS[@]}" \
    74|  -d '{
    75|    "agent": { "type": "agent", "id": "agent_abc123", "version": "1772585501101368014" },
    76|    "environment_id": "env_abc123"
    77|  }'
    78|```
    79|
    80|### With system prompt, custom tools, and GitHub repo
    81|
    82|```bash
    83|# 1. Create the agent
    84|curl -X POST https://api.anthropic.com/v1/agents \
    85|  "${HEADERS[@]}" \
    86|  -d '{
    87|    "name": "Code Reviewer",
    88|    "model": "claude-opus-4-7",
    89|    "system": "You are a senior code reviewer. Be thorough and constructive.",
    90|    "tools": [
    91|      { "type": "agent_toolset_20260401" },
    92|      {
    93|        "type": "custom",
    94|        "name": "run_linter",
    95|        "description": "Run the project linter on a file",
    96|        "input_schema": {
    97|          "type": "object",
    98|          "properties": {
    99|            "file_path": { "type": "string", "description": "Path to lint" }
   100|          },
   101|          "required": ["file_path"]
   102|        }
   103|      }
   104|    ]
   105|  }'
   106|
   107|# 2. Start a session with the repo mounted
   108|curl -X POST https://api.anthropic.com/v1/sessions \
   109|  "${HEADERS[@]}" \
   110|  -d '{
   111|    "agent": { "type": "agent", "id": "agent_abc123", "version": "1772585501101368014" },
   112|    "environment_id": "env_abc123",
   113|    "title": "Code review session",
   114|    "resources": [
   115|      {
   116|        "type": "github_repository",
   117|        "url": "https://github.com/owner/repo",
   118|        "mount_path": "/workspace/repo",
   119|        "authorization_token": "ghp_...",
   120|        "branch": "feature-branch"
   121|      }
   122|    ]
   123|  }'
   124|```
   125|
   126|---
   127|
   128|## Send a User Message
   129|
   130|```bash
   131|curl -X POST https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
   132|  "${HEADERS[@]}" \
   133|  -d '{
   134|    "events": [
   135|      {
   136|        "type": "user.message",
   137|        "content": [{ "type": "text", "text": "Review the auth module for security issues" }]
   138|      }
   139|    ]
   140|  }'
   141|```
   142|
   143|---
   144|
   145|## Stream Events (SSE)
   146|
   147|```bash
   148|curl -N https://api.anthropic.com/v1/sessions/$SESSION_ID/events/stream \
   149|  "${HEADERS[@]}"
   150|```
   151|
   152|Response format:
   153|
   154|```
   155|event: session.status_running
   156|data: {"type":"session.status_running","id":"sevt_...","processed_at":"..."}
   157|
   158|event: agent.message
   159|data: {"type":"agent.message","id":"sevt_...","content":[{"type":"text","text":"I'll review..."}],"processed_at":"..."}
   160|
   161|event: session.status_idle
   162|data: {"type":"session.status_idle","id":"sevt_...","processed_at":"..."}
   163|```
   164|
   165|---
   166|
   167|## Poll Events
   168|
   169|```bash
   170|# Get all events
   171|curl https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
   172|  "${HEADERS[@]}"
   173|
   174|# Paginated — get next page of events
   175|curl "https://api.anthropic.com/v1/sessions/$SESSION_ID/events?page=page_abc123" \
   176|  "${HEADERS[@]}"
   177|```
   178|
   179|---
   180|
   181|## Provide Custom Tool Result
   182|
   183|When the agent calls a custom tool, send the result back:
   184|
   185|```bash
   186|curl -X POST https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
   187|  "${HEADERS[@]}" \
   188|  -d '{
   189|    "events": [
   190|      {
   191|        "type": "user.custom_tool_result",
   192|        "custom_tool_use_id": "sevt_abc123",
   193|        "content": [{ "type": "text", "text": "No linting errors found." }]
   194|      }
   195|    ]
   196|  }'
   197|```
   198|
   199|---
   200|
   201|## Interrupt a Running Session
   202|
   203|```bash
   204|curl -X POST https://api.anthropic.com/v1/sessions/$SESSION_ID/events \
   205|  "${HEADERS[@]}" \
   206|  -d '{
   207|    "events": [
   208|      {
   209|        "type": "interrupt"
   210|      }
   211|    ]
   212|  }'
   213|```
   214|
   215|---
   216|
   217|## Get Session Details
   218|
   219|```bash
   220|curl https://api.anthropic.com/v1/sessions/$SESSION_ID \
   221|  "${HEADERS[@]}"
   222|```
   223|
   224|---
   225|
   226|## List Sessions
   227|
   228|```bash
   229|curl https://api.anthropic.com/v1/sessions \
   230|  "${HEADERS[@]}"
   231|```
   232|
   233|---
   234|
   235|## Delete a Session
   236|
   237|```bash
   238|curl -X DELETE https://api.anthropic.com/v1/sessions/$SESSION_ID \
   239|  "${HEADERS[@]}"
   240|```
   241|
   242|---
   243|
   244|## Upload a File
   245|
   246|```bash
   247|curl -X POST https://api.anthropic.com/v1/files \
   248|  -H "x-api-key: $ANTHROPIC_API_KEY" \
   249|  -H "anthropic-version: 2023-06-01" \
   250|  -H "anthropic-beta: files-api-2025-04-14" \
   251|  -F "file=@path/to/file.txt"
   252|```
   253|
   254|---
   255|
   256|## List and Download Session Files
   257|
   258|List files the agent wrote to `/mnt/session/outputs/` during a session, then download them.
   259|
   260|```bash
   261|# List files associated with a session
   262|curl "https://api.anthropic.com/v1/files?scope_id=$SESSION_ID" \
   263|  -H "x-api-key: $ANTHROPIC_API_KEY" \
   264|  -H "anthropic-version: 2023-06-01" \
   265|  -H "anthropic-beta: files-api-2025-04-14,managed-agents-2026-04-01"
   266|
   267|# Download a specific file
   268|curl "https://api.anthropic.com/v1/files/$FILE_ID/content" \
   269|  -H "x-api-key: $ANTHROPIC_API_KEY" \
   270|  -H "anthropic-version: 2023-06-01" \
   271|  -H "anthropic-beta: files-api-2025-04-14,managed-agents-2026-04-01" \
   272|  -o downloaded_file.txt
   273|```
   274|
   275|---
   276|
   277|## List Agents
   278|
   279|```bash
   280|curl https://api.anthropic.com/v1/agents \
   281|  "${HEADERS[@]}"
   282|```
   283|
   284|---
   285|
   286|## MCP Server Integration
   287|
   288|```bash
   289|# 1. Agent declares MCP server (no auth here — auth goes in a vault)
   290|curl -X POST https://api.anthropic.com/v1/agents \
   291|  "${HEADERS[@]}" \
   292|  -d '{
   293|    "name": "MCP Agent",
   294|    "model": "claude-opus-4-7",
   295|    "mcp_servers": [
   296|      { "type": "url", "name": "my-tools", "url": "https://my-mcp-server.example.com/sse" }
   297|    ],
   298|    "tools": [
   299|      { "type": "agent_toolset_20260401" },
   300|      { "type": "mcp_toolset", "mcp_server_name": "my-tools" }
   301|    ]
   302|  }'
   303|
   304|# 2. Session attaches vault containing credentials for that MCP server URL
   305|curl -X POST https://api.anthropic.com/v1/sessions \
   306|  "${HEADERS[@]}" \
   307|  -d '{
   308|    "agent": "agent_abc123",
   309|    "environment_id": "env_abc123",
   310|    "vault_ids": ["vlt_abc123"]
   311|  }'
   312|```
   313|
   314|See `shared/managed-agents-tools.md` §Vaults for creating vaults and adding credentials.
   315|
   316|---
   317|
   318|## Tool Configuration
   319|
   320|```bash
   321|curl -X POST https://api.anthropic.com/v1/agents \
   322|  "${HEADERS[@]}" \
   323|  -d '{
   324|    "name": "Restricted Agent",
   325|    "model": "claude-opus-4-7",
   326|    "tools": [
   327|      {
   328|        "type": "agent_toolset_20260401",
   329|        "default_config": { "enabled": true },
   330|        "configs": [
   331|          { "name": "bash", "enabled": false }
   332|        ]
   333|      }
   334|    ]
   335|  }'
   336|```
   337|