---
name: shared-managed-agents-core
description: "Managed Agents — Core Concepts"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Core Concepts
     2|
     3|## Architecture
     4|
     5|Managed Agents is built around four core concepts:
     6|
     7|| Concept | Endpoint | What it is |
     8|| --- | --- | --- |
     9|| **Agent** | `/v1/agents` | A persisted, versioned object defining the agent's capabilities and persona: model, system prompt, tools, MCP servers, skills. **Must be created before starting a session.** See the Agents section below. |
    10|| **Session** | `/v1/sessions` | A stateful interaction with an agent. References a pre-created agent by ID + an environment + initial instructions. Produces an event stream. |
    11|| **Environment** | `/v1/environments` | A template defining the configuration for container provisioning. |
    12|| **Container** | N/A | An isolated compute instance where the agent's **tools** execute (bash, file ops, code). The agent loop does not run here — it runs on Anthropic's orchestration layer and acts on the container via tool calls. |
    13|
    14|```
    15|                       ┌─────────────────────────────────────┐
    16|                       │  Anthropic orchestration layer      │
    17|Agent (config) ───────▶│  (agent loop: Claude + tool calls)  │
    18|                       └──────────────┬──────────────────────┘
    19|                                      │ tool calls
    20|                                      ▼
    21|Environment (template) ──▶ Container (tool execution workspace)
    22|                                 │
    23|                         Session ─┤
    24|                                 ├── Resources (files, repos, memory stores — attached at startup)
    25|                                 ├── Vault IDs (MCP credential references)
    26|                                 └── Conversation (event stream in/out)
    27|```
    28|
    29|> **Agent creation is a prerequisite.** Sessions reference a pre-created agent by ID — `model`/`system`/`tools` live on the agent object, never on the session. Every flow starts with `POST /v1/agents`.
    30|
    31|---
    32|
    33|## Session Lifecycle
    34|
    35|```
    36|rescheduling → running ↔ idle → terminated
    37|```
    38|
    39|| Status | Description |
    40|| --- | --- |
    41|| `idle` | Agent has finished the current task, and is awaiting input. It's either waiting for input to continue working via a `user.message` or blocked awaiting a `user.custom_tool_result` or `user.tool_confirmation`. The `stop_reason` attached contains more information about why the Agent has stopped working. |
    42|| `running` | Session has starting running, and the Agent is actively doing work. |
    43|| `rescheduling` | Session is (re)scheduling after a retryable error has occurred, ready to be picked up by the orchestration system. |
    44|| `terminated` | Session has terminated, entering an irreversible and unusable state. |
    45|
    46|- Events can be sent when the session is `running` or `idle`. Messages are queued and processed in order.
    47|- The agent transitions `idle → running` when it receives a new event, then back to `idle` when done.
    48|- Errors surface as `session.error` events in the stream, not as a status value.
    49|
    50|### Built-in session features
    51|
    52|- **Context compaction** — if you approach max context, the API automatically condenses session history to keep the interaction going
    53|- **Prompt caching** — historical repeated tokens are cached, reducing processing time and cost
    54|- **Extended thinking** — on by default, returned as `agent.thinking` events
    55|
    56|### Session operations
    57|
    58|| Operation | Notes |
    59|| --- | --- |
    60|| List / fetch | Paginated list or single resource by ID |
    61|| Update | Only `title` is updatable |
    62|| Archive | Session becomes **read-only**. Not reversible. |
    63|| Delete | Permanently deletes session, event history, container, and checkpoints. |
    64|
    65|---
    66|
    67|## Sessions
    68|
    69|A session is a running agent instance inside an environment.
    70|
    71|### Session Object
    72|
    73|Key fields returned by the API:
    74|
    75|| Field | Type | Description |
    76|| --- | --- | --- |
    77|| `type` | string | Always `"session"` |
    78|| `id` | string | Unique session ID |
    79|| `title` | string | Human-readable title |
    80|| `status` | string | `idle`, `running`, `rescheduling`, `terminated` |
    81|| `created_at` | string | ISO 8601 timestamp |
    82|| `updated_at` | string | ISO 8601 timestamp |
    83|| `archived_at` | string | ISO 8601 timestamp (nullable) |
    84|| `environment_id` | string | Environment ID |
    85|| `agent` | object | Agent configuration |
    86|| `resources` | array | Attached files, repos, and memory stores |
    87|| `metadata` | object | User-provided key-value pairs (max 8 keys) |
    88|| `usage` | object | Token usage statistics |
    89|
    90|### Creating a session
    91|
    92|**A session is meaningless without an agent.** Sessions reference a pre-created agent by ID. Create the agent first via `agents.create()`, then reference it:
    93|
    94|```ts
    95|// 1. Create the agent (reusable, versioned)
    96|const agent = await client.beta.agents.create({
    97|  name: "Coding Assistant",
    98|  model: "claude-opus-4-7",
    99|  system: "You are a helpful coding agent.",
   100|  tools: [{ type: "agent_toolset_20260401" }]
   101|});
   102|
   103|// 2. Start a session that references it
   104|const session = await client.beta.sessions.create({
   105|  agent: agent.id, // string shorthand → latest version. Or: { type: "agent", id: agent.id, version: agent.version }
   106|  environment_id: environmentId,
   107|  title: "Hello World Session"
   108|});
   109|```
   110|
   111|**Session creation parameters:**
   112|
   113|| Field | Type | Required | Description |
   114|| --- | --- | --- | --- |
   115|| `agent` | string or object | **Yes** | String shorthand `"agent_abc123"` (latest version) or `{type: "agent", id, version}` |
   116|| `environment_id` | string | **Yes** | Environment ID |
   117|| `title` | string | No | Human-readable name (appears in logs/dashboards) |
   118|| `resources` | array | No | Files, GitHub repos, or memory stores, attached to the container at startup. Memory stores are session-create-only (not addable via `resources.add()`). |
   119|| `vault_ids` | array | No | Vault IDs (`vlt_*`) — MCP credentials with auto-refresh. See `shared/managed-agents-tools.md` → Vaults. |
   120|| `metadata` | object | No | User-provided key-value pairs |
   121|
   122|**Agent configuration fields** (passed to `agents.create()`, not `sessions.create()`):
   123|
   124|| Field | Type | Required | Description |
   125|| --- | --- | --- | --- |
   126|| `name` | string | **Yes** | Human-readable name (1-256 chars) |
   127|| `model` | string or object | **Yes** | Claude model ID (bare string, or `{id, speed}` object). All Claude 4.5+ models supported. |
   128|| `system` | string | No | System prompt — defines the agent's behavior (up to 100K chars) |
   129|| `tools` | array | No | Encompasses three kinds: (1) pre-built Claude Agent tools (`agent_toolset_20260401`), (2) MCP tools (`mcp_toolset`), and (3) custom client-side tools. Max 128. |
   130|| `mcp_servers` | array | No | MCP server connections — standardized third-party capabilities (e.g. GitHub, Asana). Max 20, unique names. See `shared/managed-agents-tools.md` → MCP Servers. |
   131|| `skills` | array | No | Customized "best-practices" context with progressive disclosure. Max 20. See `shared/managed-agents-tools.md` → Skills. |
   132|| `description` | string | No | Description of the agent (up to 2048 chars) |
   133|| `multiagent` | object | No | `{type: "coordinator", agents: [...]}` — roster this agent may delegate to. See `shared/managed-agents-multiagent.md`. |
   134|| `metadata` | object | No | Arbitrary key-value pairs (max 16, keys ≤64 chars, values ≤512 chars) |
   135|
   136|---
   137|
   138|## Agents
   139|
   140|**This is where every Managed Agents flow begins.** The agent object is a persisted, versioned configuration — you create it once, then reference it by ID every time you start a session. No agent → no session.
   141|
   142|### Agent Object
   143|
   144|The API is **flat** — `model`, `system`, `tools` etc. are top-level fields, not wrapped in an `agent:{}` sub-object.
   145|
   146|| Field | Type | Required | Description |
   147|| --- | --- | --- | --- |
   148|| `name` | string | Yes | Human-readable name |
   149|| `model` | string | Yes | Claude model ID |
   150|| `system` | string | No | System prompt |
   151|| `tools` | array | No | Agent toolset / MCP toolset / custom tools |
   152|| `mcp_servers` | array | No | MCP server connections |
   153|| `skills` | array | No | Skill references (max 20) |
   154|| `description` | string | No | Description of the agent |
   155|| `multiagent` | object | No | Coordinator roster — see `shared/managed-agents-multiagent.md` |
   156|| `metadata` | object | No | Arbitrary key-value pairs |
   157|
   158|### Lifecycle: create once, run many, update in place
   159|
   160|The agent is a **persistent resource**, not a per-run parameter. The intended pattern:
   161|
   162|```
   163|┌─ setup (once) ─────────┐     ┌─ runtime (every invocation) ─┐
   164|│ agents.create()        │     │ sessions.create(             │
   165|│   → store agent_id     │ ──→ │   agent={type:..., id: ID}   │
   166|│     in config/env/db   │     │ )                            │
   167|└────────────────────────┘     └──────────────────────────────┘
   168|```
   169|
   170|**Anti-pattern:** calling `agents.create()` at the top of every script run. This accumulates orphaned agent objects, pays create latency on every invocation, and defeats the versioning model. If you see `agents.create()` in a function that's called per-request or per-cron-tick, that's wrong — hoist it to one-time setup and persist the ID.
   171|
   172|### Versioning
   173|
   174|Each `POST /v1/agents/{id}` (update) creates a new immutable version (numeric timestamp, e.g. `1772585501101368014`). The agent's history is append-only — you can't edit a past version.
   175|
   176|**Why version:**
   177|
   178|- **Reproducibility** — pin a session to a known-good config: `{type: "agent", id, version: 3}`
   179|- **Safe iteration** — update the agent without breaking sessions already running on the old version
   180|- **Rollback** — if a new system prompt regresses, pin new sessions back to the prior version while you debug
   181|
   182|**`version` is optional.** Omit it (or use the string shorthand `agent="agent_abc123"`) to get the latest version at session-creation time. Pass it explicitly (`{type: "agent", id, version: N}`) to pin for reproducibility.
   183|
   184|**Getting the version to pin:** `agents.create()` and `agents.update()` both return `version` in the response. Store it alongside `agent_id`. To fetch the current latest for an existing agent: `GET /v1/agents/{id}` → `.version`.
   185|
   186|**When to update vs create new:** Update (`POST /v1/agents/{id}`) when it's conceptually the same agent with tweaked behavior (better prompt, extra tool). Create a new agent when it's a different persona/purpose. Rule of thumb: if you'd give it the same `name`, update.
   187|
   188|### Agent Endpoints
   189|
   190|| Operation | Method | Path                      |
   191|| --------- | ------ | ------------------------- |
   192|| Create    | `POST` | `/v1/agents`              |
   193|| List      | `GET`  | `/v1/agents`              |
   194|| Get       | `GET`  | `/v1/agents/{id}`         |
   195|| Update    | `POST` | `/v1/agents/{id}`         |
   196|| Archive   | `POST` | `/v1/agents/{id}/archive` |
   197|
   198|> ⚠️ **Archive is permanent.** Archiving makes the agent read-only: existing sessions continue to run, but **new sessions cannot reference it**, and there is no unarchive. Since agents have no `delete`, this is the terminal lifecycle state. Never archive a production agent as routine cleanup — confirm with the user first.
   199|
   200|### Using an Agent in a Session
   201|
   202|Reference the agent by string ID (latest version) or by object with an explicit version:
   203|
   204|```python
   205|# String shorthand — uses the agent's latest version
   206|session = client.beta.sessions.create(
   207|    agent=agent.id,
   208|    environment_id=environment_id,
   209|)
   210|
   211|# Or pin to a specific version (int)
   212|session = client.beta.sessions.create(
   213|    agent={"type": "agent", "id": agent.id, "version": agent.version},
   214|    environment_id=environment_id,
   215|)
   216|```
   217|