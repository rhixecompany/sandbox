---
name: shared-managed-agents-tools
description: "Managed Agents — Tools & Skills"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Tools & Skills
     2|
     3|## Tools
     4|
     5|### Server tools vs client tools
     6|
     7|| Type | Who runs it | How it works |
     8|| --- | --- | --- |
     9|| **Prebuilt Claude Agent tools** (`agent_toolset_20260401`) | Anthropic, on the session's container | File ops, bash, web search, etc. Enable all at once or configure individually with `enabled: true/false`. |
    10|| **MCP tools** (`mcp_toolset`) | Anthropic, on the session's container | Capabilities exposed by connected MCP servers. Grant access per-server via the toolset. |
    11|| **Custom tools** | **You** — your application handles the call and returns results | Agent emits a `agent.custom_tool_use` event, session goes `idle`, you send back a `user.custom_tool_result` event. |
    12|
    13|**Recommendation:** Enable all prebuilt tools via `agent_toolset_20260401`, then disable individually as needed.
    14|
    15|**Versioning:** The toolset is a versioned, static resource. When underlying tools change, a new toolset version is created (hence `_20260401`) so you always know exactly what you're getting.
    16|
    17|### Agent Toolset
    18|
    19|The `agent_toolset_20260401` provides these built-in tools:
    20|
    21|| Tool | Description |
    22|| --- | --- |
    23|| `bash` | Execute bash commands in a shell session |
    24|| `read` | Read a file from the local filesystem, including text, images, PDFs, and Jupyter notebooks |
    25|| `write` | Write a file to the local filesystem |
    26|| `edit` | Perform string replacement in a file |
    27|| `glob` | Fast file pattern matching using glob patterns |
    28|| `grep` | Text search using regex patterns |
    29|| `web_fetch` | Fetch content from a URL |
    30|| `web_search` | Search the web for information |
    31|
    32|Enable the full toolset:
    33|
    34|```json
    35|{
    36|  "tools": [{ "type": "agent_toolset_20260401" }]
    37|}
    38|```
    39|
    40|### Per-Tool Configuration
    41|
    42|Override defaults for individual tools. This example enables everything except bash:
    43|
    44|```json
    45|{
    46|  "tools": [
    47|    {
    48|      "type": "agent_toolset_20260401",
    49|      "default_config": { "enabled": true },
    50|      "configs": [{ "name": "bash", "enabled": false }]
    51|    }
    52|  ]
    53|}
    54|```
    55|
    56|| Field | Required | Description |
    57|| --- | --- | --- |
    58|| `type` | ✅ | `"agent_toolset_20260401"` |
    59|| `default_config` | ❌ | Applied to all tools. `{ "enabled": bool, "permission_policy": {...} }` |
    60|| `configs` | ❌ | Per-tool overrides: `[{ "name": "...", "enabled": bool, "permission_policy": {...} }]` |
    61|
    62|### Permission Policies
    63|
    64|Control when server-executed tools (agent toolset + MCP) run automatically vs wait for approval. Does not apply to custom tools.
    65|
    66|| Policy | Behavior |
    67|| --- | --- |
    68|| `always_allow` | Tool executes automatically (default) |
    69|| `always_ask` | Session emits `session.status_idle` and pauses until you send a `tool_confirmation` event |
    70|
    71|```json
    72|{
    73|  "configs": [
    74|    { "name": "bash", "permission_policy": { "type": "always_ask" } }
    75|  ],
    76|  "default_config": {
    77|    "enabled": true,
    78|    "permission_policy": { "type": "always_allow" }
    79|  },
    80|  "type": "agent_toolset_20260401"
    81|}
    82|```
    83|
    84|**Responding to `always_ask`:** Send a `user.tool_confirmation` event with `tool_use_id` from the triggering `agent_tool_use`/`mcp_tool_use` event:
    85|
    86|```json
    87|{ "type": "tool_confirmation", "tool_use_id": "sevt_abc123", "result": "allow" }
    88|{ "type": "tool_confirmation", "tool_use_id": "sevt_def456", "result": "deny", "message": "Read .env.example instead" }
    89|```
    90|
    91|The optional `message` on a deny is delivered to the agent so it can adjust its approach.
    92|
    93|To enable only specific tools, flip the default off and opt-in per tool:
    94|
    95|```json
    96|{
    97|  "tools": [
    98|    {
    99|      "type": "agent_toolset_20260401",
   100|      "default_config": { "enabled": false },
   101|      "configs": [
   102|        { "name": "bash", "enabled": true },
   103|        { "name": "read", "enabled": true }
   104|      ]
   105|    }
   106|  ]
   107|}
   108|```
   109|
   110|### Custom Tools (Client-Side)
   111|
   112|Custom tools are executed by **your application**, not Anthropic. The flow:
   113|
   114|1. Agent decides to use the tool → session emits a `agent.custom_tool_use` event with inputs
   115|2. Session goes `idle` waiting for you
   116|3. Your application executes the tool
   117|4. You send back a `user.custom_tool_result` event with the output
   118|5. Session resumes `running`
   119|
   120|No permission policy needed — you're the one executing.
   121|
   122|```json
   123|{
   124|  "tools": [
   125|    {
   126|      "type": "custom",
   127|      "name": "get_weather",
   128|      "description": "Fetch current weather for a city.",
   129|      "input_schema": {
   130|        "type": "object",
   131|        "properties": {
   132|          "city": { "type": "string", "description": "City name" }
   133|        },
   134|        "required": ["city"]
   135|      }
   136|    }
   137|  ]
   138|}
   139|```
   140|
   141|### MCP Servers
   142|
   143|MCP (Model Context Protocol) servers expose standardized third-party capabilities (e.g. Asana, GitHub, Linear). **Configuration is split across agent and vault:**
   144|
   145|1. **Agent creation** declares which servers to connect to (`type`, `name`, `url` — no auth). The agent's `mcp_servers` array has no auth field.
   146|2. **Vault** stores the OAuth credentials. Attach via `vault_ids` on session create.
   147|
   148|This keeps secrets out of reusable agent definitions. Each vault credential is tied to one MCP server URL; Anthropic matches credentials to servers by URL.
   149|
   150|**Agent side — declare servers (no auth):**
   151|
   152|| Field | Required | Description |
   153|| --- | --- | --- |
   154|| `type` | ✅ | `"url"` |
   155|| `name` | ✅ | Unique name — referenced by `mcp_toolset.mcp_server_name` |
   156|| `url` | ✅ | The MCP server's endpoint URL (Streamable HTTP transport) |
   157|
   158|```json
   159|{
   160|  "mcp_servers": [
   161|    {
   162|      "type": "url",
   163|      "name": "linear",
   164|      "url": "https://mcp.linear.app/mcp"
   165|    }
   166|  ],
   167|  "tools": [{ "type": "mcp_toolset", "mcp_server_name": "linear" }]
   168|}
   169|```
   170|
   171|**Session side — attach vault:**
   172|
   173|```json
   174|{
   175|  "agent": "agent_abc123",
   176|  "environment_id": "env_abc123",
   177|  "vault_ids": ["vlt_abc123"]
   178|}
   179|```
   180|
   181|> 💡 **Per-tool enablement (empirical):** `mcp_toolset` has been observed accepting `default_config: {enabled: false}` + `configs: [{name, enabled: true}]` for an allowlist pattern. The API ref shows only the minimal `{type, mcp_server_name}` form.
   182|
   183|> ⚠️ **MCP auth tokens ≠ REST API tokens.** Hosted MCP servers (`mcp.notion.com`, `mcp.linear.app`, etc.) typically require **OAuth bearer tokens**, not the service's native API keys. A Notion `ntn_` integration token authenticates against Notion's REST API but will **not** work as a vault credential for the Notion MCP server. These are different auth systems.
   184|
   185|### Vaults — the MCP credential store
   186|
   187|**Vaults** store OAuth credentials (access token + refresh token) that Anthropic auto-refreshes on your behalf via standard OAuth 2.0 `refresh_token` grant. This is the only way to authenticate MCP servers in the launch SDK.
   188|
   189|#### Credentials and the sandbox
   190|
   191|Vaults store credentials; those credentials **never enter the sandbox**. This is a deliberate security boundary — code running in the sandbox (including anything the agent writes) cannot read or exfiltrate a vaulted credential, even under prompt injection. Instead, credentials are injected by Anthropic-side proxies **after** a request leaves the sandbox:
   192|
   193|- **MCP tool calls** are routed through an Anthropic-side proxy that fetches the credential from the vault and adds it to the outbound request.
   194|- **Git operations on attached GitHub repositories** (`git pull`, `git push`, GitHub REST calls) are routed through a git proxy that injects the `github_repository` resource's `authorization_token` the same way.
   195|
   196|**Not yet supported:** running other authenticated CLIs (e.g. `aws`, `gcloud`, `stripe`) directly inside the sandbox. There is currently no way to set container environment variables or expose vault credentials to arbitrary processes. If you need one of these today:
   197|
   198|- **Prefer an MCP server** for that service if one exists — it gets the same vault-backed injection.
   199|- **Otherwise, register a custom tool:** the agent emits `agent.custom_tool_use`, your orchestrator (which already holds the credential) executes the call and returns `user.custom_tool_result` over the same authenticated event stream. No public endpoint is exposed; the sandbox never sees the secret. See `shared/managed-agents-client-patterns.md` → Pattern 9.
   200|
   201|**Do not put API keys in the system prompt or user messages as a workaround** — they persist in the session's event history.
   202|
   203|> Formerly known internally as TATs (Tool/Tenant Access Tokens).
   204|
   205|**Flow:**
   206|
   207|1. Create a vault (`client.beta.vaults.create(...)`) — one per tenant/user, or one shared, depending on your model
   208|2. Add MCP credentials to it (`client.beta.vaults.credentials.create(...)`) — each credential is tied to one MCP server URL
   209|3. Reference the vault on session create via `vault_ids: ["vlt_..."]`
   210|4. Anthropic auto-refreshes tokens before they expire; the agent uses the current access token when calling MCP tools
   211|
   212|**Credential shape**:
   213|
   214|```json
   215|{
   216|  "auth": {
   217|    "type": "mcp_oauth",
   218|    "mcp_server_url": "https://mcp.notion.com/mcp",
   219|    "access_token": "<current access token>",
   220|    "expires_at": "2026-04-02T14:00:00Z",
   221|    "refresh": {
   222|      "refresh_token": "<refresh token>",
   223|      "client_id": "<your OAuth client_id>",
   224|      "token_endpoint": "https://api.notion.com/v1/oauth/token",
   225|      "token_endpoint_auth": { "type": "none" }
   226|    }
   227|  },
   228|  "display_name": "Notion (workspace-foo)"
   229|}
   230|```
   231|
   232|The `refresh` block is what enables auto-refresh — `token_endpoint` is where Anthropic posts the `refresh_token` grant. `token_endpoint_auth` is a discriminated union:
   233|
   234|| `type` | Shape | Use when |
   235|| --- | --- | --- |
   236|| `"none"` | `{type: "none"}` | Public OAuth client (no secret) |
   237|| `"client_secret_basic"` | `{type: "client_secret_basic", client_secret: "..."}` | Confidential client, secret via HTTP Basic auth |
   238|| `"client_secret_post"` | `{type: "client_secret_post", client_secret: "..."}` | Confidential client, secret in request body |
   239|
   240|Omit `refresh` entirely if you only have an access token with no refresh capability — it'll work until it expires, then the agent loses access.
   241|
   242|> 💡 **Getting an OAuth token.** How you obtain the initial access and refresh tokens depends on the MCP server — consult its documentation. Once you have them, store them in a vault credential using the shape above; Anthropic auto-refreshes via the `refresh.token_endpoint` from there.
   243|
   244|**Scoping:** Vaults are workspace-scoped. Anyone with developer+ role in the API workspace can create, read (metadata only — secrets are write-only), and attach vaults. `vault_ids` can be set at session **create** time but not via session update (the SDK docstring says "Not yet supported; requests setting this field are rejected").
   245|
   246|---
   247|
   248|## Skills
   249|
   250|Skills are reusable, filesystem-based resources that provide your agent with domain-specific expertise: workflows, context, and best practices that transform general-purpose agents into specialists. Unlike prompts (conversation-level instructions for one-off tasks), skills load on-demand and eliminate the need to repeatedly provide the same guidance across multiple conversations.
   251|
   252|Two types — both work the same way; the agent automatically uses them when relevant to the task at hand:
   253|
   254|| Type | What it is |
   255|| --- | --- |
   256|| **Pre-built Anthropic skills** | Common document tasks (PowerPoint, Excel, Word, PDF). Reference by name (e.g. `xlsx`). |
   257|| **Custom skills** | Skills you've created in your organization via the Skills API. Reference by `skill_id` + optional `version`. |
   258|
   259|**Max 20 skills per agent.** Agent creation uses `managed-agents-2026-04-01`; the separate Skills API (for managing custom skill definitions) uses `skills-2025-10-02`.
   260|
   261|### Enabling skills on a session
   262|
   263|Skills are attached to the **agent** definition via `agents.create()`:
   264|
   265|```ts
   266|const agent = await client.beta.agents.create({
   267|  name: "Financial Agent",
   268|  model: "claude-opus-4-7",
   269|  system: "You are a financial analysis agent.",
   270|  skills: [
   271|    { type: "anthropic", skill_id: "xlsx" },
   272|    { type: "custom", skill_id: "skill_abc123", version: "latest" }
   273|  ]
   274|});
   275|```
   276|
   277|Python:
   278|
   279|```python
   280|agent = client.beta.agents.create(
   281|    name="Financial Agent",
   282|    model="claude-opus-4-7",
   283|    system="You are a financial analysis agent.",
   284|    skills=[
   285|        {"type": "anthropic", "skill_id": "xlsx"},
   286|        {"type": "custom", "skill_id": "skill_abc123", "version": "latest"},
   287|    ]
   288|)
   289|```
   290|
   291|**Skill reference fields:**
   292|
   293|| Field | Anthropic skill | Custom skill |
   294|| --- | --- | --- |
   295|| `type` | `"anthropic"` | `"custom"` |
   296|| `skill_id` | Skill name (e.g. `"xlsx"`, `"docx"`, `"pptx"`, `"pdf"`) | Skill ID from Skills API (e.g. `"skill_abc123"`) |
   297|| `version` | — | `"latest"` or a specific version number |
   298|
   299|### Skills API
   300|
   301|| Operation      | Method   | Path                                 |
   302|| -------------- | -------- | ------------------------------------ |
   303|| Create Skill   | `POST`   | `/v1/skills`                         |
   304|| List Skills    | `GET`    | `/v1/skills`                         |
   305|| Get Skill      | `GET`    | `/v1/skills/{id}`                    |
   306|| Delete Skill   | `DELETE` | `/v1/skills/{id}`                    |
   307|| Create Version | `POST`   | `/v1/skills/{id}/versions`           |
   308|| List Versions  | `GET`    | `/v1/skills/{id}/versions`           |
   309|| Get Version    | `GET`    | `/v1/skills/{id}/versions/{version}` |
   310|| Delete Version | `DELETE` | `/v1/skills/{id}/versions/{version}` |
   311|