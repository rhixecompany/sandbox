---
name: readme-managed-agents
description: "Managed Agents — Python"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Python
     2|
     3|> **Bindings not shown here:** This README covers the most common managed-agents flows for Python. If you need a class, method, namespace, field, or behavior that isn't shown, WebFetch the Python SDK repo **or the relevant docs page** from `shared/live-sources.md` rather than guess. Do not extrapolate from cURL shapes or another language's SDK.
     4|
     5|> **Agents are persistent — create once, reference by ID.** Store the agent ID returned by `agents.create` and pass it to every subsequent `sessions.create`; do not call `agents.create` in the request path. The Anthropic CLI is one convenient way to create agents and environments from version-controlled YAML — its URL is in `shared/live-sources.md`. The examples below show in-code creation for completeness; in production the create call belongs in setup, not in the request path.
     6|
     7|## Installation
     8|
     9|```bash
    10|pip install anthropic
    11|```
    12|
    13|## Client Initialization
    14|
    15|```python
    16|import anthropic
    17|
    18|# Default (uses ANTHROPIC_API_KEY env var)
    19|client = anthropic.Anthropic()
    20|
    21|# Explicit API key
    22|client = anthropic.Anthropic(api_key="your-api-key")
    23|```
    24|
    25|---
    26|
    27|## Create an Environment
    28|
    29|```python
    30|environment = client.beta.environments.create(
    31|    name="my-dev-env",
    32|    config={
    33|        "type": "cloud",
    34|        "networking": {"type": "unrestricted"},
    35|    },
    36|)
    37|print(environment.id)  # env_...
    38|```
    39|
    40|---
    41|
    42|## Create an Agent (required first step)
    43|
    44|> ⚠️ **There is no inline agent config.** `model`/`system`/`tools` live on the agent object, not the session. Always start with `agents.create()` — the session only takes `agent={"type": "agent", "id": agent.id}`.
    45|
    46|### Minimal
    47|
    48|```python
    49|# 1. Create the agent (reusable, versioned)
    50|agent = client.beta.agents.create(
    51|    name="Coding Assistant",
    52|    model="claude-opus-4-7",
    53|    tools=[{"type": "agent_toolset_20260401", "default_config": {"enabled": True}}],
    54|)
    55|
    56|# 2. Start a session
    57|session = client.beta.sessions.create(
    58|    agent={"type": "agent", "id": agent.id, "version": agent.version},
    59|    environment_id=environment.id,
    60|)
    61|print(session.id, session.status)
    62|```
    63|
    64|### With system prompt and custom tools
    65|
    66|```python
    67|import os
    68|
    69|agent = client.beta.agents.create(
    70|    name="Code Reviewer",
    71|    model="claude-opus-4-7",
    72|    system="You are a senior code reviewer.",
    73|    tools=[
    74|        {"type": "agent_toolset_20260401"},
    75|        {
    76|            "type": "custom",
    77|            "name": "run_tests",
    78|            "description": "Run the test suite",
    79|            "input_schema": {
    80|                "type": "object",
    81|                "properties": {
    82|                    "test_path": {"type": "string", "description": "Path to test file"}
    83|                },
    84|                "required": ["test_path"],
    85|            },
    86|        },
    87|    ],
    88|)
    89|
    90|session = client.beta.sessions.create(
    91|    agent={"type": "agent", "id": agent.id, "version": agent.version},
    92|    environment_id=environment.id,
    93|    title="Code review session",
    94|    resources=[
    95|        {
    96|            "type": "github_repository",
    97|            "url": "https://github.com/owner/repo",
    98|            "mount_path": "/workspace/repo",
    99|            "authorization_token": os.environ["GITHUB_TOKEN"],
   100|            "branch": "main",
   101|        }
   102|    ],
   103|)
   104|```
   105|
   106|---
   107|
   108|## Send a User Message
   109|
   110|```python
   111|client.beta.sessions.events.send(
   112|    session_id=session.id,
   113|    events=[
   114|        {
   115|            "type": "user.message",
   116|            "content": [{"type": "text", "text": "Review the auth module"}],
   117|        }
   118|    ],
   119|)
   120|```
   121|
   122|> 💡 **Stream-first:** Open the stream _before_ (or concurrently with) sending the message. The stream only delivers events that occur after it opens — stream-after-send means early events arrive buffered in one batch. See [Steering Patterns](../../shared/managed-agents-events.md#steering-patterns).
   123|
   124|---
   125|
   126|## Stream Events (SSE)
   127|
   128|```python
   129|import json
   130|
   131|# Stream-first: open stream, then send while stream is live
   132|with client.beta.sessions.stream(
   133|    session_id=session.id,
   134|) as stream:
   135|    client.beta.sessions.events.send(
   136|        session_id=session.id,
   137|        events=[{"type": "user.message", "content": [{"type": "text", "text": "..."}]}],
   138|    )
   139|    for event in stream:
   140|        ...  # process events
   141|
   142|# Standalone stream iteration:
   143|with client.beta.sessions.stream(
   144|    session_id=session.id,
   145|) as stream:
   146|    for event in stream:
   147|        if event.type == "agent.message":
   148|            for block in event.content:
   149|                if block.type == "text":
   150|                    print(block.text, end="", flush=True)
   151|        elif event.type == "agent.custom_tool_use":
   152|            # Custom tool invocation — session is now idle
   153|            print(f"\nCustom tool call: {event.tool_name}")
   154|            print(f"Input: {json.dumps(event.input)}")
   155|            # Send result back (see below)
   156|        elif event.type == "session.status_idle":
   157|            print("\n--- Agent idle ---")
   158|        elif event.type == "session.status_terminated":
   159|            print("\n--- Session terminated ---")
   160|            break
   161|```
   162|
   163|---
   164|
   165|## Provide Custom Tool Result
   166|
   167|```python
   168|client.beta.sessions.events.send(
   169|    session_id=session.id,
   170|    events=[
   171|        {
   172|            "type": "user.custom_tool_result",
   173|            "custom_tool_use_id": "sevt_abc123",
   174|            "content": [{"type": "text", "text": "All 42 tests passed."}],
   175|        }
   176|    ],
   177|)
   178|```
   179|
   180|---
   181|
   182|## Poll Events
   183|
   184|```python
   185|events = client.beta.sessions.events.list(
   186|    session_id=session.id,
   187|)
   188|for event in events.data:
   189|    print(f"{event.type}: {event.id}")
   190|```
   191|
   192|> ⚠️ **Prefer the SDK over raw `requests`/`httpx`.** If you hand-roll a poll loop, don't assume `timeout=(5, 60)` or `httpx.Timeout(120)` caps total call duration — both are **per-chunk** read timeouts (reset on every byte), so a trickling response can block forever. For a hard wall-clock deadline, track `time.monotonic()` at the loop level and bail explicitly, or wrap with `asyncio.wait_for()`. See [Receiving Events](../../shared/managed-agents-events.md#receiving-events).
   193|
   194|---
   195|
   196|## Full Streaming Loop with Custom Tools
   197|
   198|```python
   199|import json
   200|
   201|
   202|def run_custom_tool(tool_name: str, tool_input: dict) -> str:
   203|    """Execute a custom tool and return the result."""
   204|    if tool_name == "run_tests":
   205|        # Your tool implementation here
   206|        return "All tests passed."
   207|    return f"Unknown tool: {tool_name}"
   208|
   209|
   210|def run_session(client, session_id: str):
   211|    """Stream events and handle custom tool calls."""
   212|    while True:
   213|        with client.beta.sessions.stream(
   214|            session_id=session_id,
   215|        ) as stream:
   216|            tool_calls = []
   217|            for event in stream:
   218|                if event.type == "agent.message":
   219|                    for block in event.content:
   220|                        if block.type == "text":
   221|                            print(block.text, end="", flush=True)
   222|                elif event.type == "agent.custom_tool_use":
   223|                    tool_calls.append(event)
   224|                elif event.type == "session.status_idle":
   225|                    break
   226|                elif event.type == "session.status_terminated":
   227|                    return
   228|
   229|        if not tool_calls:
   230|            break
   231|
   232|        # Process custom tool calls
   233|        results = []
   234|        for call in tool_calls:
   235|            result = run_custom_tool(call.tool_name, call.input)
   236|            results.append({
   237|                "type": "user.custom_tool_result",
   238|                "custom_tool_use_id": call.id,
   239|                "content": [{"type": "text", "text": result}],
   240|            })
   241|
   242|        client.beta.sessions.events.send(
   243|            session_id=session_id,
   244|            events=results,
   245|        )
   246|```
   247|
   248|---
   249|
   250|## Upload a File
   251|
   252|```python
   253|with open("data.csv", "rb") as f:
   254|    file = client.beta.files.upload(
   255|        file=f,
   256|    )
   257|
   258|# Use in a session
   259|session = client.beta.sessions.create(
   260|    agent={"type": "agent", "id": agent.id, "version": agent.version},
   261|    environment_id=environment.id,
   262|    resources=[{"type": "file", "file_id": file.id, "mount_path": "/workspace/data.csv"}],
   263|)
   264|```
   265|
   266|---
   267|
   268|## List and Download Session Files
   269|
   270|List files the agent wrote to `/mnt/session/outputs/` during a session, then download them.
   271|
   272|```python
   273|# List files associated with a session
   274|files = client.beta.files.list(
   275|    scope_id=session.id,
   276|    betas=["managed-agents-2026-04-01"],
   277|)
   278|for f in files.data:
   279|    print(f.filename, f.size_bytes)
   280|    # Download each file and save to disk
   281|    file_content = client.beta.files.download(f.id)
   282|    file_content.write_to_file(f.filename)
   283|```
   284|
   285|> 💡 There's a brief indexing lag (~1–3s) between `session.status_idle` and output files appearing in `files.list`. Retry once or twice if the list is empty.
   286|
   287|---
   288|
   289|## Session Management
   290|
   291|```python
   292|# Get session details
   293|session = client.beta.sessions.retrieve(session_id="sesn_011CZxAbc123Def456")
   294|print(session.status, session.usage)
   295|
   296|# List sessions
   297|sessions = client.beta.sessions.list()
   298|
   299|# Delete a session
   300|client.beta.sessions.delete(session_id="sesn_011CZxAbc123Def456")
   301|
   302|# Archive a session
   303|client.beta.sessions.archive(session_id="sesn_011CZxAbc123Def456")
   304|```
   305|
   306|---
   307|
   308|## MCP Server Integration
   309|
   310|```python
   311|# Agent declares MCP server (no auth here — auth goes in a vault)
   312|agent = client.beta.agents.create(
   313|    name="MCP Agent",
   314|    model="claude-opus-4-7",
   315|    mcp_servers=[
   316|        {"type": "url", "name": "my-tools", "url": "https://my-mcp-server.example.com/sse"},
   317|    ],
   318|    tools=[
   319|        {"type": "agent_toolset_20260401", "default_config": {"enabled": True}},
   320|        {"type": "mcp_toolset", "mcp_server_name": "my-tools"},
   321|    ],
   322|)
   323|
   324|# Session attaches vault(s) containing credentials for those MCP server URLs
   325|session = client.beta.sessions.create(
   326|    agent=agent.id,
   327|    environment_id=environment.id,
   328|    vault_ids=[vault.id],
   329|)
   330|```
   331|
   332|See `shared/managed-agents-tools.md` §Vaults for creating vaults and adding credentials.
   333|