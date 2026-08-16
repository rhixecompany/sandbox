---
name: typescript-managed-agents
description: "Managed Agents — TypeScript"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — TypeScript
     2|
     3|> **Bindings not shown here:** This README covers the most common managed-agents flows for TypeScript. If you need a class, method, namespace, field, or behavior that isn't shown, WebFetch the TypeScript SDK repo **or the relevant docs page** from `shared/live-sources.md` rather than guess. Do not extrapolate from cURL shapes or another language's SDK.
     4|
     5|> **Agents are persistent — create once, reference by ID.** Store the agent ID returned by `agents.create` and pass it to every subsequent `sessions.create`; do not call `agents.create` in the request path. The Anthropic CLI is one convenient way to create agents and environments from version-controlled YAML — its URL is in `shared/live-sources.md`. The examples below show in-code creation for completeness; in production the create call belongs in setup, not in the request path.
     6|
     7|## Installation
     8|
     9|```bash
    10|npm install @anthropic-ai/sdk
    11|```
    12|
    13|## Client Initialization
    14|
    15|```typescript
    16|import Anthropic from "@anthropic-ai/sdk";
    17|
    18|// Default (uses ANTHROPIC_API_KEY env var)
    19|const client = new Anthropic();
    20|
    21|// Explicit API key
    22|const client = new Anthropic({ apiKey: "your-api-key" });
    23|```
    24|
    25|---
    26|
    27|## Create an Environment
    28|
    29|```typescript
    30|const environment = await client.beta.environments.create({
    31|  name: "my-dev-env",
    32|  config: {
    33|    type: "cloud",
    34|    networking: { type: "unrestricted" }
    35|  }
    36|});
    37|console.log(environment.id); // env_...
    38|```
    39|
    40|---
    41|
    42|## Create an Agent (required first step)
    43|
    44|> ⚠️ **There is no inline agent config.** `model`/`system`/`tools` live on the agent object, not the session. Always start with `agents.create()` — the session only takes `agent: { type: "agent", id: agent.id }`.
    45|
    46|### Minimal
    47|
    48|```typescript
    49|// 1. Create the agent (reusable, versioned)
    50|const agent = await client.beta.agents.create({
    51|  name: "Coding Assistant",
    52|  model: "claude-opus-4-7",
    53|  tools: [
    54|    {
    55|      type: "agent_toolset_20260401",
    56|      default_config: { enabled: true }
    57|    }
    58|  ]
    59|});
    60|
    61|// 2. Start a session
    62|const session = await client.beta.sessions.create({
    63|  agent: { type: "agent", id: agent.id, version: agent.version },
    64|  environment_id: environment.id
    65|});
    66|console.log(session.id, session.status);
    67|```
    68|
    69|### With system prompt and custom tools
    70|
    71|```typescript
    72|const agent = await client.beta.agents.create({
    73|  name: "Code Reviewer",
    74|  model: "claude-opus-4-7",
    75|  system: "You are a senior code reviewer.",
    76|  tools: [
    77|    {
    78|      type: "agent_toolset_20260401",
    79|      default_config: { enabled: true }
    80|    },
    81|    {
    82|      type: "custom",
    83|      name: "run_tests",
    84|      description: "Run the test suite",
    85|      input_schema: {
    86|        type: "object",
    87|        properties: {
    88|          test_path: {
    89|            type: "string",
    90|            description: "Path to test file"
    91|          }
    92|        },
    93|        required: ["test_path"]
    94|      }
    95|    }
    96|  ]
    97|});
    98|
    99|const session = await client.beta.sessions.create({
   100|  agent: { type: "agent", id: agent.id, version: agent.version },
   101|  environment_id: environment.id,
   102|  title: "Code review session",
   103|  resources: [
   104|    {
   105|      type: "github_repository",
   106|      url: "https://github.com/owner/repo",
   107|      mount_path: "/workspace/repo",
   108|      authorization_token: process.env.GITHUB_TOKEN,
   109|      branch: "main"
   110|    }
   111|  ]
   112|});
   113|```
   114|
   115|---
   116|
   117|## Send a User Message
   118|
   119|```typescript
   120|await client.beta.sessions.events.send(session.id, {
   121|  events: [
   122|    {
   123|      type: "user.message",
   124|      content: [{ type: "text", text: "Review the auth module" }]
   125|    }
   126|  ]
   127|});
   128|```
   129|
   130|> 💡 **Stream-first:** Open the stream _before_ (or concurrently with) sending the message. The stream only delivers events that occur after it opens — stream-after-send means early events arrive buffered in one batch. See [Steering Patterns](../../shared/managed-agents-events.md#steering-patterns).
   131|
   132|---
   133|
   134|## Stream Events (SSE)
   135|
   136|```typescript
   137|// Stream-first: open stream and send concurrently
   138|const [events] = await Promise.all([
   139|  collectStream(session.id),
   140|  client.beta.sessions.events.send(session.id, {
   141|    events: [
   142|      {
   143|        type: "user.message",
   144|        content: [{ type: "text", text: "..." }]
   145|      }
   146|    ]
   147|  })
   148|]);
   149|
   150|// Standalone stream iteration:
   151|const stream = await client.beta.sessions.stream(session.id);
   152|
   153|for await (const event of stream) {
   154|  switch (event.type) {
   155|    case "agent.message":
   156|      for (const block of event.content) {
   157|        if (block.type === "text") {
   158|          process.stdout.write(block.text);
   159|        }
   160|      }
   161|      break;
   162|    case "agent.custom_tool_use":
   163|      // Custom tool invocation — session is now idle
   164|      console.log(`\nCustom tool call: ${event.tool_name}`);
   165|      console.log(`Input: ${JSON.stringify(event.input)}`);
   166|      break;
   167|    case "session.status_idle":
   168|      console.log("\n--- Agent idle ---");
   169|      break;
   170|    case "session.status_terminated":
   171|      console.log("\n--- Session terminated ---");
   172|      break;
   173|  }
   174|}
   175|```
   176|
   177|---
   178|
   179|## Provide Custom Tool Result
   180|
   181|```typescript
   182|await client.beta.sessions.events.send(session.id, {
   183|  events: [
   184|    {
   185|      type: "user.custom_tool_result",
   186|      custom_tool_use_id: "sevt_abc123",
   187|      content: [{ type: "text", text: "All 42 tests passed." }]
   188|    }
   189|  ]
   190|});
   191|```
   192|
   193|---
   194|
   195|## Poll Events
   196|
   197|```typescript
   198|const events = await client.beta.sessions.events.list(session.id);
   199|for (const event of events.data) {
   200|  console.log(`${event.type}: ${event.id}`);
   201|}
   202|```
   203|
   204|---
   205|
   206|## Full Streaming Loop with Custom Tools
   207|
   208|```typescript
   209|function runCustomTool(toolName: string, toolInput: unknown): string {
   210|  if (toolName === "run_tests") {
   211|    // Your tool implementation here
   212|    return "All tests passed.";
   213|  }
   214|  return `Unknown tool: ${toolName}`;
   215|}
   216|
   217|async function runSession(client: Anthropic, sessionId: string) {
   218|  while (true) {
   219|    const stream = await client.beta.sessions.stream(sessionId);
   220|
   221|    const toolCalls: Array<{
   222|      custom_tool_use_id: string;
   223|      tool_name: string;
   224|      input: unknown;
   225|    }> = [];
   226|
   227|    for await (const event of stream) {
   228|      if (event.type === "agent.message") {
   229|        for (const block of event.content) {
   230|          if (block.type === "text") {
   231|            process.stdout.write(block.text);
   232|          }
   233|        }
   234|      } else if (event.type === "agent.custom_tool_use") {
   235|        toolCalls.push({
   236|          id: event.id,
   237|          tool_name: event.tool_name,
   238|          input: event.input
   239|        });
   240|      } else if (event.type === "session.status_idle") {
   241|        break;
   242|      } else if (event.type === "session.status_terminated") {
   243|        return;
   244|      }
   245|    }
   246|
   247|    if (toolCalls.length === 0) break;
   248|
   249|    // Process custom tool calls
   250|    const results = toolCalls.map(call => ({
   251|      type: "user.custom_tool_result" as const,
   252|      custom_tool_use_id: call.id,
   253|      content: [
   254|        {
   255|          type: "text" as const,
   256|          text: runCustomTool(call.tool_name, call.input)
   257|        }
   258|      ]
   259|    }));
   260|
   261|    await client.beta.sessions.events.send(sessionId, {
   262|      events: results
   263|    });
   264|  }
   265|}
   266|```
   267|
   268|---
   269|
   270|## Upload a File
   271|
   272|```typescript
   273|import fs from "fs";
   274|
   275|const file = await client.beta.files.upload({
   276|  file: fs.createReadStream("data.csv")
   277|});
   278|
   279|// Use in a session
   280|const session = await client.beta.sessions.create({
   281|  agent: { type: "agent", id: agent.id, version: agent.version },
   282|  environment_id: environment.id,
   283|  resources: [
   284|    {
   285|      type: "file",
   286|      file_id: file.id,
   287|      mount_path: "/workspace/data.csv"
   288|    }
   289|  ]
   290|});
   291|```
   292|
   293|---
   294|
   295|## List and Download Session Files
   296|
   297|List files the agent wrote to `/mnt/session/outputs/` during a session, then download them.
   298|
   299|```typescript
   300|import fs from "fs";
   301|
   302|// List files associated with a session
   303|const files = await client.beta.files.list({
   304|  scope_id: session.id,
   305|  betas: ["managed-agents-2026-04-01"]
   306|});
   307|for (const f of files.data) {
   308|  console.log(f.filename, f.size_bytes);
   309|
   310|  // Download and save to disk
   311|  const resp = await client.beta.files.download(f.id);
   312|  const buffer = Buffer.from(await resp.arrayBuffer());
   313|  fs.writeFileSync(f.filename, buffer);
   314|}
   315|```
   316|
   317|> 💡 There's a brief indexing lag (~1–3s) between `session.status_idle` and output files appearing in `files.list`. Retry once or twice if the list is empty.
   318|
   319|---
   320|
   321|## Session Management
   322|
   323|```typescript
   324|// Get session details
   325|const session = await client.beta.sessions.retrieve(
   326|  "sesn_011CZxAbc123Def456"
   327|);
   328|console.log(session.status, session.usage);
   329|
   330|// List sessions
   331|const sessions = await client.beta.sessions.list();
   332|
   333|// Delete a session
   334|await client.beta.sessions.delete("sesn_011CZxAbc123Def456");
   335|
   336|// Archive a session
   337|await client.beta.sessions.archive("sesn_011CZxAbc123Def456");
   338|```
   339|
   340|---
   341|
   342|## MCP Server Integration
   343|
   344|```typescript
   345|// Agent declares MCP server (no auth here — auth goes in a vault)
   346|const agent = await client.beta.agents.create({
   347|  name: "MCP Agent",
   348|  model: "claude-opus-4-7",
   349|  mcp_servers: [
   350|    {
   351|      type: "url",
   352|      name: "my-tools",
   353|      url: "https://my-mcp-server.example.com/sse"
   354|    }
   355|  ],
   356|  tools: [
   357|    {
   358|      type: "agent_toolset_20260401",
   359|      default_config: { enabled: true }
   360|    },
   361|    { type: "mcp_toolset", mcp_server_name: "my-tools" }
   362|  ]
   363|});
   364|
   365|// Session attaches vault(s) containing credentials for those MCP server URLs
   366|const session = await client.beta.sessions.create({
   367|  agent: agent.id,
   368|  environment_id: environment.id,
   369|  vault_ids: [vault.id]
   370|});
   371|```
   372|
   373|See `shared/managed-agents-tools.md` §Vaults for creating vaults and adding credentials.
   374|