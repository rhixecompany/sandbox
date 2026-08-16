---
name: shared-managed-agents-api-reference
description: "Managed Agents — Endpoint Reference"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Endpoint Reference
     2|
     3|All endpoints require `x-api-key` and `anthropic-version: 2023-06-01` headers. Managed Agents endpoints additionally require the `anthropic-beta` header.
     4|
     5|## Beta Headers
     6|
     7|```
     8|anthropic-beta: managed-agents-2026-04-01
     9|```
    10|
    11|The SDK adds this header automatically for all `client.beta.{agents,environments,sessions,vaults,memory_stores}.*` calls. Skills endpoints use `skills-2025-10-02`; Files endpoints use `files-api-2025-04-14`.
    12|
    13|---
    14|
    15|## SDK Method Reference
    16|
    17|All resources are under the `beta` namespace. Python and TypeScript share identical method names.
    18|
    19|| Resource | Python / TypeScript (`client.beta.*`) | Go (`client.Beta.*`) |
    20|| --- | --- | --- |
    21|| Agents | `agents.create` / `retrieve` / `update` / `list` / `archive` | `Agents.New` / `Get` / `Update` / `List` / `Archive` |
    22|| Agent Versions | `agents.versions.list` | `Agents.Versions.List` |
    23|| Environments | `environments.create` / `retrieve` / `update` / `list` / `delete` / `archive` | `Environments.New` / `Get` / `Update` / `List` / `Delete` / `Archive` |
    24|| Sessions | `sessions.create` / `retrieve` / `update` / `list` / `delete` / `archive` | `Sessions.New` / `Get` / `Update` / `List` / `Delete` / `Archive` |
    25|| Session Events | `sessions.events.list` / `send` / `stream` | `Sessions.Events.List` / `Send` / `StreamEvents` |
    26|| Session Threads | `sessions.threads.list` / `retrieve` / `archive`; `sessions.threads.events.list` / `stream` | `Sessions.Threads.List` / `Get` / `Archive`; `Sessions.Threads.Events.List` / `StreamEvents` |
    27|| Session Resources | `sessions.resources.add` / `retrieve` / `update` / `list` / `delete` | `Sessions.Resources.Add` / `Get` / `Update` / `List` / `Delete` |
    28|| Vaults | `vaults.create` / `retrieve` / `update` / `list` / `delete` / `archive` | `Vaults.New` / `Get` / `Update` / `List` / `Delete` / `Archive` |
    29|| Credentials | `vaults.credentials.create` / `retrieve` / `update` / `list` / `delete` / `archive` / `mcp_oauth_validate` | `Vaults.Credentials.New` / `Get` / `Update` / `List` / `Delete` / `Archive` / `McpOauthValidate` |
    30|| Memory Stores | `memory_stores.create` / `retrieve` / `update` / `list` / `delete` / `archive` | `MemoryStores.New` / `Get` / `Update` / `List` / `Delete` / `Archive` |
    31|| Memories | `memory_stores.memories.create` / `retrieve` / `update` / `list` / `delete` | `MemoryStores.Memories.New` / `Get` / `Update` / `List` / `Delete` |
    32|| Memory Versions | `memory_stores.memory_versions.list` / `retrieve` / `redact` | `MemoryStores.MemoryVersions.List` / `Get` / `Redact` |
    33|
    34|**Naming quirks to watch for:**
    35|
    36|- Agents and Session Threads have **no delete** — only `archive`. Archive is **permanent**: the agent becomes read-only, new sessions cannot reference it, and there is no unarchive. Confirm with the user before archiving a production agent. Environments, Sessions, Vaults, Credentials, and Memory Stores have both `delete` and `archive`; Session Resources, Files, Skills, and Memories are `delete`-only; Memory Versions have neither — only `redact`.
    37|- Session resources use `add` (not `create`).
    38|- Go's event stream is `StreamEvents` (not `Stream`).
    39|
    40|**Agent shorthand:** `agent` on session create accepts either a bare string (`agent="agent_abc123"` — uses latest version) or the full reference object (`{type: "agent", id: "agent_abc123", version: 123}`).
    41|
    42|**Model shorthand:** `model` on agent create accepts either a bare string (`model="claude-opus-4-7"` — uses `standard` speed) or the full config object (`{type: "model_config", id: "claude-opus-4-6", speed: "fast"}`). Note: `speed: "fast"` is only supported on Opus 4.6.
    43|
    44|---
    45|
    46|## Agents
    47|
    48|**Step one of every flow.** Sessions require a pre-created agent — there is no inline agent config under `managed-agents-2026-04-01`.
    49|
    50|| Method | Path | Operation | Description |
    51|| --- | --- | --- | --- |
    52|| `GET` | `/v1/agents` | ListAgents | List agents |
    53|| `POST` | `/v1/agents` | CreateAgent | Create a saved agent configuration |
    54|| `GET` | `/v1/agents/{agent_id}` | GetAgent | Get agent details |
    55|| `POST` | `/v1/agents/{agent_id}` | UpdateAgent | Update agent configuration |
    56|| `POST` | `/v1/agents/{agent_id}/archive` | ArchiveAgent | Archive an agent. Makes it **read-only**; existing sessions continue, new sessions cannot reference it. No unarchive — this is the terminal state. |
    57|| `GET` | `/v1/agents/{agent_id}/versions` | ListAgentVersions | List agent versions |
    58|
    59|## Sessions
    60|
    61|| Method | Path | Operation | Description |
    62|| --- | --- | --- | --- |
    63|| `GET` | `/v1/sessions` | ListSessions | List sessions (paginated) |
    64|| `POST` | `/v1/sessions` | CreateSession | Create a new session |
    65|| `GET` | `/v1/sessions/{session_id}` | GetSession | Get session details |
    66|| `POST` | `/v1/sessions/{session_id}` | UpdateSession | Update session metadata/title |
    67|| `DELETE` | `/v1/sessions/{session_id}` | DeleteSession | Delete a session |
    68|| `POST` | `/v1/sessions/{session_id}/archive` | ArchiveSession | Archive a session |
    69|
    70|## Events
    71|
    72|| Method | Path | Operation | Description |
    73|| --- | --- | --- | --- |
    74|| `GET` | `/v1/sessions/{session_id}/events` | ListEvents | List events (polling, paginated) |
    75|| `POST` | `/v1/sessions/{session_id}/events` | SendEvents | Send events (user message, tool result) |
    76|| `GET` | `/v1/sessions/{session_id}/events/stream` | StreamEvents | Stream events via SSE |
    77|
    78|## Session Threads
    79|
    80|Per-subagent event streams in multiagent sessions. See `shared/managed-agents-multiagent.md`.
    81|
    82|| Method | Path | Operation | Description |
    83|| --- | --- | --- | --- |
    84|| `GET` | `/v1/sessions/{session_id}/threads` | ListThreads | List threads (paginated) |
    85|| `GET` | `/v1/sessions/{session_id}/threads/{thread_id}` | GetThread | Retrieve one thread (carries `agent` snapshot, `status`, `parent_thread_id`, `stats`, `usage`) |
    86|| `POST` | `/v1/sessions/{session_id}/threads/{thread_id}/archive` | ArchiveThread | Archive a thread |
    87|| `GET` | `/v1/sessions/{session_id}/threads/{thread_id}/events` | ListThreadEvents | List past events for one thread (paginated) |
    88|| `GET` | `/v1/sessions/{session_id}/threads/{thread_id}/stream` | StreamThreadEvents | Stream one thread via SSE (SDK: `threads.events.stream`) |
    89|
    90|## Session Resources
    91|
    92|| Method | Path | Operation | Description |
    93|| --- | --- | --- | --- |
    94|| `GET` | `/v1/sessions/{session_id}/resources` | ListResources | List resources attached to session |
    95|| `POST` | `/v1/sessions/{session_id}/resources` | AddResource | Attach `file` or `github_repository` resource (SDK method: `add`, not `create`). `memory_store` resources attach at session-create time only. |
    96|| `GET` | `/v1/sessions/{session_id}/resources/{resource_id}` | GetResource | Get a single resource |
    97|| `POST` | `/v1/sessions/{session_id}/resources/{resource_id}` | UpdateResource | Update resource |
    98|| `DELETE` | `/v1/sessions/{session_id}/resources/{resource_id}` | DeleteResource | Remove resource from session |
    99|
   100|## Environments
   101|
   102|| Method | Path | Operation | Description |
   103|| --- | --- | --- | --- |
   104|| `POST` | `/v1/environments` | CreateEnvironment | Create environment |
   105|| `GET` | `/v1/environments` | ListEnvironments | List environments |
   106|| `GET` | `/v1/environments/{environment_id}` | GetEnvironment | Get environment details |
   107|| `POST` | `/v1/environments/{environment_id}` | UpdateEnvironment | Update environment |
   108|| `DELETE` | `/v1/environments/{environment_id}` | DeleteEnvironment | Delete environment. Returns 204. |
   109|| `POST` | `/v1/environments/{environment_id}/archive` | ArchiveEnvironment | Archive environment. Makes it **read-only**; existing sessions continue, new sessions cannot reference it. No unarchive — this is the terminal state. |
   110|
   111|## Vaults
   112|
   113|Vaults store MCP credentials that Anthropic manages on your behalf — OAuth credentials with auto-refresh, or static bearer tokens. Attach to sessions via `vault_ids`. See `managed-agents-tools.md` §Vaults for the conceptual guide and credential shapes.
   114|
   115|| Method | Path | Operation | Description |
   116|| --- | --- | --- | --- |
   117|| `POST` | `/v1/vaults` | CreateVault | Create a vault |
   118|| `GET` | `/v1/vaults` | ListVaults | List vaults |
   119|| `GET` | `/v1/vaults/{vault_id}` | GetVault | Get vault details |
   120|| `POST` | `/v1/vaults/{vault_id}` | UpdateVault | Update vault |
   121|| `DELETE` | `/v1/vaults/{vault_id}` | DeleteVault | Delete vault |
   122|| `POST` | `/v1/vaults/{vault_id}/archive` | ArchiveVault | Archive vault |
   123|
   124|## Credentials
   125|
   126|Credentials are individual secrets stored inside a vault.
   127|
   128|| Method | Path | Operation | Description |
   129|| --- | --- | --- | --- |
   130|| `POST` | `/v1/vaults/{vault_id}/credentials` | CreateCredential | Create a credential |
   131|| `GET` | `/v1/vaults/{vault_id}/credentials` | ListCredentials | List credentials in vault |
   132|| `GET` | `/v1/vaults/{vault_id}/credentials/{credential_id}` | GetCredential | Get credential metadata |
   133|| `POST` | `/v1/vaults/{vault_id}/credentials/{credential_id}` | UpdateCredential | Update credential |
   134|| `DELETE` | `/v1/vaults/{vault_id}/credentials/{credential_id}` | DeleteCredential | Delete credential |
   135|| `POST` | `/v1/vaults/{vault_id}/credentials/{credential_id}/archive` | ArchiveCredential | Archive credential |
   136|| `POST` | `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate` | McpOauthValidate | Validate an MCP OAuth credential |
   137|
   138|## Memory Stores
   139|
   140|Workspace-scoped persistent memory that survives across sessions. Attach to a session via a `{"type": "memory_store", "memory_store_id": ...}` entry in `resources[]` (session-create time only). See `shared/managed-agents-memory.md` for the conceptual guide, the FUSE-mount agent interface, preconditions, and versioning.
   141|
   142|| Method | Path | Operation | Description |
   143|| --- | --- | --- | --- |
   144|| `POST` | `/v1/memory_stores` | CreateMemoryStore | Create a store (`name`, `description`, `metadata`) |
   145|| `GET` | `/v1/memory_stores` | ListMemoryStores | List stores (`include_archived`, `created_at_{gte,lte}`) |
   146|| `GET` | `/v1/memory_stores/{memory_store_id}` | GetMemoryStore | Get store details |
   147|| `POST` | `/v1/memory_stores/{memory_store_id}` | UpdateMemoryStore | Update store |
   148|| `DELETE` | `/v1/memory_stores/{memory_store_id}` | DeleteMemoryStore | Delete store |
   149|| `POST` | `/v1/memory_stores/{memory_store_id}/archive` | ArchiveMemoryStore | Archive store. Makes it **read-only**; existing sessions continue, new sessions cannot reference it. No unarchive. |
   150|
   151|## Memories
   152|
   153|Individual text documents inside a store (≤ 100KB each). `create` creates at a `path` and returns `409` (`memory_path_conflict_error`, with `conflicting_memory_id`) if the path is occupied; `update` mutates by `mem_...` ID (rename and/or content). Only `update` accepts a `precondition` (`{"type": "content_sha256", "content_sha256": ...}`) — on mismatch returns `409` (`memory_precondition_failed_error`). List endpoints accept `view: "basic"|"full"` (controls whether `content` is populated; `retrieve` defaults to `full`).
   154|
   155|| Method | Path | Operation | Description |
   156|| --- | --- | --- | --- |
   157|| `GET` | `/v1/memory_stores/{memory_store_id}/memories` | ListMemories | Returns `Memory \| MemoryPrefix`; filter by `path_prefix`, `depth`, `order_by`/`order` |
   158|| `POST` | `/v1/memory_stores/{memory_store_id}/memories` | CreateMemory | Create at `path` (SDK: `memories.create`); `409 memory_path_conflict_error` if occupied |
   159|| `GET` | `/v1/memory_stores/{memory_store_id}/memories/{memory_id}` | GetMemory | Read one memory (defaults to `view="full"`) |
   160|| `PATCH` | `/v1/memory_stores/{memory_store_id}/memories/{memory_id}` | UpdateMemory | Change `content`, `path`, or both by ID; optional `precondition` |
   161|| `DELETE` | `/v1/memory_stores/{memory_store_id}/memories/{memory_id}` | DeleteMemory | Delete (optional `expected_content_sha256`) |
   162|
   163|## Memory Versions
   164|
   165|Immutable per-mutation snapshots (`memver_...`) — the audit and rollback surface. `operation` ∈ `created` / `modified` / `deleted`.
   166|
   167|| Method | Path | Operation | Description |
   168|| --- | --- | --- | --- |
   169|| `GET` | `/v1/memory_stores/{memory_store_id}/memory_versions` | ListMemoryVersions | Newest-first; filter by `memory_id`, `operation`, `session_id`, `api_key_id`, `created_at_{gte,lte}` |
   170|| `GET` | `/v1/memory_stores/{memory_store_id}/memory_versions/{version_id}` | GetMemoryVersion | List fields + full `content` |
   171|| `POST` | `/v1/memory_stores/{memory_store_id}/memory_versions/{version_id}/redact` | RedactMemoryVersion | Clear `content`/`content_sha256`/`content_size_bytes`/`path`; preserve actor + timestamps |
   172|
   173|## Files
   174|
   175|| Method | Path | Operation | Description |
   176|| --- | --- | --- | --- |
   177|| `POST` | `/v1/files` | UploadFile | Upload a file |
   178|| `GET` | `/v1/files` | ListFiles | List files |
   179|| `GET` | `/v1/files/{file_id}` | GetFile | Get file metadata (SDK method: `retrieve_metadata`) |
   180|| `GET` | `/v1/files/{file_id}/content` | DownloadFile | Download file content |
   181|| `DELETE` | `/v1/files/{file_id}` | DeleteFile | Delete a file |
   182|
   183|## Skills
   184|
   185|| Method | Path | Operation | Description |
   186|| --- | --- | --- | --- |
   187|| `POST` | `/v1/skills` | CreateSkill | Create a skill |
   188|| `GET` | `/v1/skills` | ListSkills | List skills |
   189|| `GET` | `/v1/skills/{skill_id}` | GetSkill | Get skill details |
   190|| `DELETE` | `/v1/skills/{skill_id}` | DeleteSkill | Delete a skill |
   191|| `POST` | `/v1/skills/{skill_id}/versions` | CreateVersion | Create skill version |
   192|| `GET` | `/v1/skills/{skill_id}/versions` | ListVersions | List skill versions |
   193|| `GET` | `/v1/skills/{skill_id}/versions/{version}` | GetVersion | Get skill version |
   194|| `DELETE` | `/v1/skills/{skill_id}/versions/{version}` | DeleteVersion | Delete skill version |
   195|
   196|---
   197|
   198|## Request/Response Schema Quick Reference
   199|
   200|### CreateAgent Request Body
   201|
   202|**Always start here.** `model`, `system`, `tools`, `mcp_servers`, `skills` are top-level fields on this object — they do NOT go on the session.
   203|
   204|```json
   205|{
   206|  "description": "string (optional, up to 2048 chars)",
   207|  "mcp_servers": [
   208|    {
   209|      "type": "url",
   210|      "name": "github",
   211|      "url": "https://api.githubcopilot.com/mcp/"
   212|    }
   213|  ],
   214|  "metadata": {
   215|    "key": "value (max 16 pairs, keys ≤64 chars, values ≤512 chars)"
   216|  },
   217|  "model": "claude-opus-4-7 (required — bare string, or {id, speed} object)",
   218|  "multiagent": {
   219|    "type": "coordinator",
   220|    "agents": [
   221|      "agent_abc123",
   222|      { "type": "agent", "id": "agent_def456", "version": 4 },
   223|      { "type": "self" }
   224|    ]
   225|  },
   226|  "name": "string (required, 1-256 chars)",
   227|  "skills": [
   228|    { "type": "anthropic", "skill_id": "xlsx" },
   229|    { "type": "custom", "skill_id": "skill_abc123", "version": "1" }
   230|  ],
   231|  "system": "string (optional, up to 100,000 chars)",
   232|  "tools": [{ "type": "agent_toolset_20260401" }]
   233|}
   234|```
   235|
   236|> Limits: `tools` max 128, `skills` max 20, `mcp_servers` max 20 (unique names). `multiagent.agents` 1–20 entries (string ID | `{type:"agent",id,version?}` | `{type:"self"}`) — see `shared/managed-agents-multiagent.md`.
   237|
   238|### CreateSession Request Body
   239|
   240|```json
   241|{
   242|  "agent": "agent_abc123 (required — string shorthand for latest version, or {type: \"agent\", id, version} object)",
   243|  "environment_id": "env_abc123 (required)",
   244|  "metadata": {
   245|    "key": "value"
   246|  },
   247|  "resources": [
   248|    {
   249|      "type": "github_repository",
   250|      "url": "https://github.com/owner/repo (required)",
   251|      "authorization_token": "ghp_... (required)",
   252|      "mount_path": "/workspace/repo (optional — defaults to /workspace/<repo-name>)",
   253|      "checkout": { "type": "branch", "name": "main" }
   254|    }
   255|  ],
   256|  "title": "string (optional)",
   257|  "vault_ids": [
   258|    "vlt_abc123 (optional — MCP credentials with auto-refresh)"
   259|  ]
   260|}
   261|```
   262|
   263|> The `agent` field accepts only a string ID or `{type: "agent", id, version}` — `model`/`system`/`tools` live on the agent, not here.
   264|>
   265|> **`checkout`** accepts `{type: "branch", name: "..."}` or `{type: "commit", sha: "..."}`. Omit for the repo's default branch.
   266|
   267|### CreateEnvironment Request Body
   268|
   269|```json
   270|{
   271|  "config": {
   272|    "type": "cloud",
   273|    "networking": {
   274|      "type": "unrestricted | limited (union — see SDK types)"
   275|    },
   276|    "packages": {}
   277|  },
   278|  "description": "string (optional)",
   279|  "metadata": { "key": "value" },
   280|  "name": "string (required)"
   281|}
   282|```
   283|
   284|### SendEvents Request Body
   285|
   286|```json
   287|{
   288|  "events": [
   289|    {
   290|      "type": "user.message",
   291|      "content": [
   292|        {
   293|          "type": "text",
   294|          "text": "Hello"
   295|        }
   296|      ]
   297|    }
   298|  ]
   299|}
   300|```
   301|
   302|### Define Outcome Event
   303|
   304|```json
   305|{
   306|  "description": "Build a DCF model for Costco in .xlsx",
   307|  "max_iterations": 5,
   308|  "rubric": { "type": "file", "file_id": "file_01..." },
   309|  "type": "user.define_outcome"
   310|}
   311|```
   312|
   313|> `rubric` is required: `{type: "text", content}` or `{type: "file", file_id}`. `max_iterations` default 3, max 20. Echoed back with `outcome_id` + `processed_at`. See `shared/managed-agents-outcomes.md`.
   314|
   315|### Tool Result Event
   316|
   317|```json
   318|{
   319|  "content": [{ "type": "text", "text": "Result data" }],
   320|  "custom_tool_use_id": "sevt_abc123",
   321|  "is_error": false,
   322|  "type": "user.custom_tool_result"
   323|}
   324|```
   325|
   326|---
   327|
   328|## Error Handling
   329|
   330|Managed Agents endpoints use the standard Anthropic API error format. Errors are returned with an HTTP status code and a JSON body containing `type`, `error`, and `request_id`:
   331|
   332|```json
   333|{
   334|  "error": {
   335|    "type": "invalid_request_error",
   336|    "message": "Description of what went wrong"
   337|  },
   338|  "request_id": "req_011CRv1W3XQ8XpFikNYG7RnE",
   339|  "type": "error"
   340|}
   341|```
   342|
   343|Include the `request_id` when reporting issues to Anthropic — it lets us trace the request end-to-end. The inner `error.type` is one of the following:
   344|
   345|| Status | Error type | Description |
   346|| --- | --- | --- |
   347|| 400 | `invalid_request_error` | The request was malformed or missing required parameters |
   348|| 401 | `authentication_error` | Invalid or missing API key |
   349|| 403 | `permission_error` | The API key doesn't have permission for this operation |
   350|| 404 | `not_found_error` | The requested resource doesn't exist |
   351|| 409 | `invalid_request_error` | The request conflicts with the resource's current state (e.g., sending to an archived session) |
   352|| 413 | `request_too_large` | The request body exceeds the maximum allowed size |
   353|| 429 | `rate_limit_error` | Too many requests — check rate limit headers for retry timing |
   354|| 500 | `api_error` | An internal server error occurred |
   355|| 529 | `overloaded_error` | The service is temporarily overloaded — retry with backoff |
   356|
   357|Note that `409 Conflict` carries `error.type: "invalid_request_error"` (there is no separate `conflict_error` type); inspect both the HTTP status and the `message` to distinguish conflicts from other invalid requests.
   358|
   359|---
   360|
   361|## Rate Limits
   362|
   363|Managed Agents endpoints have per-organization request-per-minute (RPM) limits, separate from your [Messages API token limits](https://platform.claude.com/docs/en/api/rate-limits). Model inference inside a session still draws from your organization's standard ITPM/OTPM limits.
   364|
   365|| Endpoint group | Scope | RPM | Max concurrent |
   366|| --- | --- | --- | --- |
   367|| Create operations (Agents, Sessions, Vaults) | organization | 60 | — |
   368|| All other operations (Agents, Sessions, Vaults) | organization | 600 | — |
   369|| All operations (Environments) | organization | 60 | 5 |
   370|
   371|Files and Skills endpoints use the standard tier-based [rate limits](https://platform.claude.com/docs/en/api/rate-limits).
   372|
   373|When a limit is exceeded the API returns `429` with a `rate_limit_error` (see [Error Handling](#error-handling) for the response envelope) and a `retry-after` header indicating how many seconds to wait before retrying. The Anthropic SDK reads this header and retries automatically.
   374|