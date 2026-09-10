---
name: shared-managed-agents-environments
description: "Managed Agents — Environments & Resources"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Environments & Resources
     2|
     3|## Environments
     4|
     5|Creating a session requires an `environment_id`. Environments are **reusable configuration templates** for spinning up containers in Anthropic's infrastructure — you might create different environments for different use cases (e.g. data visualization vs web development, with different package sets). Anthropic handles scaling, container lifecycle, and work orchestration.
     6|
     7|**Environment names must be unique.** Creating an environment with an existing name returns 409.
     8|
     9|### Networking
    10|
    11|| Network Policy | Description |
    12|| --- | --- |
    13|| `unrestricted` | Full egress (except legal blocklist) |
    14|| `package_managers_and_custom` | Package managers + custom `allowed_hosts` |
    15|
    16|```json
    17|{
    18|  "networking": {
    19|    "type": "package_managers_and_custom",
    20|    "allowed_hosts": ["api.example.com"]
    21|  }
    22|}
    23|```
    24|
    25|**MCP caveat:** If using restricted networking, make sure `allowed_hosts` includes your MCP server domains. Otherwise the container can't reach them and tools silently fail.
    26|
    27|### Creating an environment
    28|
    29|The SDK adds `managed-agents-2026-04-01` automatically. TypeScript:
    30|
    31|```ts
    32|const env = await client.beta.environments.create({
    33|  name: "my_env",
    34|  config: {
    35|    type: "cloud",
    36|    networking: { type: "unrestricted" }
    37|  }
    38|});
    39|```
    40|
    41|### Environment CRUD
    42|
    43|| Operation | Method | Path | Notes |
    44|| --- | --- | --- | --- |
    45|| Create | `POST` | `/v1/environments` |  |
    46|| List | `GET` | `/v1/environments` | Paginated (`limit`, `after_id`, `before_id`) |
    47|| Get | `GET` | `/v1/environments/{id}` |  |
    48|| Update | `POST` | `/v1/environments/{id}` | Changes apply only to **new** containers; existing sessions keep their original config |
    49|| Delete | `DELETE` | `/v1/environments/{id}` | Returns 204. |
    50|| Archive | `POST` | `/v1/environments/{id}/archive` | Makes it **read-only**; existing sessions continue, new sessions cannot reference it. No unarchive — terminal state. |
    51|
    52|---
    53|
    54|## Resources
    55|
    56|Attach files, GitHub repositories, and memory stores to a session. **Session creation blocks until all resources are mounted** — the container won't go `running` until every file and repo is in place. Max **999 file resources** per session. Multiple GitHub repositories per session are supported. For `type: "memory_store"` resources (persistent cross-session memory — max 8 per session), see `shared/managed-agents-memory.md`.
    57|
    58|### File Uploads (input — host → agent)
    59|
    60|Upload a file first via the Files API, then reference by `file_id` + `mount_path`:
    61|
    62|```ts
    63|// 1. Upload
    64|const file = await client.beta.files.upload({
    65|  file: fs.createReadStream("data.csv")
    66|});
    67|
    68|// 2. Attach as a session resource
    69|const session = await client.beta.sessions.create({
    70|  agent: agent.id,
    71|  environment_id: envId,
    72|  resources: [
    73|    {
    74|      type: "file",
    75|      file_id: file.id,
    76|      mount_path: "/workspace/data.csv"
    77|    }
    78|  ]
    79|});
    80|```
    81|
    82|**`mount_path` is required** and must be absolute. Parent directories are created automatically. Agent working directory defaults to `/workspace`. Files are mounted read-only — the agent writes modified versions to new paths.
    83|
    84|### Session outputs (output — agent → host)
    85|
    86|The agent can write files to `/mnt/session/outputs/` during a session. These are automatically captured by the Files API and can be listed and downloaded afterwards:
    87|
    88|```ts
    89|// After the turn completes, list output files scoped to this session:
    90|for await (const f of client.beta.files.list({
    91|  scope_id: session.id,
    92|  betas: ["managed-agents-2026-04-01"]
    93|})) {
    94|  console.log(f.filename, f.size_bytes);
    95|  const resp = await client.beta.files.download(f.id);
    96|  const text = await resp.text();
    97|}
    98|```
    99|
   100|**Requirements:**
   101|
   102|- The `write` tool (or `bash`) must be enabled for the agent to create output files.
   103|- Session-scoped `files.list` / `files.download` captures outputs written to `/mnt/session/outputs/`.
   104|- The filter parameter is **`scope_id`** (REST query param `?scope_id=<session_id>`). The SDK's files resource auto-adds only the `files-api-2025-04-14` header, so pass `betas: ["managed-agents-2026-04-01"]` explicitly (or both headers on raw HTTP) — without it the API may reject `scope_id` as an unknown field. Requires `@anthropic-ai/sdk` ≥ 0.88.0 / `anthropic` (Python) ≥ 0.92.0 — older versions don't type `scope_id`. The `ant` CLI does **not** expose this flag yet; use the SDK or curl.
   105|- Pass the session ID returned by `sessions.create()` verbatim (e.g. `sesn_011CZx...`) — the API validates the prefix.
   106|- There's a brief indexing lag (~1–3s) between `session.status_idle` and output files appearing in `files.list`. Retry once or twice if empty.
   107|
   108|> **Fallback when `scope_id` filtering is unavailable** (older SDK, or endpoint returns an error): send a follow-up `user.message` asking the agent to `read` each file under `/mnt/session/outputs/` and return the contents. The agent streams the file bodies back as `agent.message` text. This works for text files only and costs output tokens — use it to unblock, not as the primary path.
   109|
   110|This gives you a bidirectional file bridge: upload reference data in, download agent artifacts out.
   111|
   112|### GitHub Repositories
   113|
   114|Clones a GitHub repository into the session container during initialization, before the agent begins execution. The agent can read, edit, commit, and push via `bash` (`git`). Multiple repositories per session are supported — add one `resources` entry per repo. Repositories are cached, so future sessions that use the same repository start faster.
   115|
   116|Repositories are attached for the lifetime of the session — to change which repositories are mounted, create a new session. You **can** rotate a repository's `authorization_token` on a running session via `client.beta.sessions.resources.update(resource_id, {session_id, authorization_token})`; the resource `id` is returned at session creation and by `resources.list()`.
   117|
   118|**Fields:**
   119|
   120|| Field | Required | Notes |
   121|| --- | --- | --- |
   122|| `type` | ✅ | `"github_repository"` |
   123|| `url` | ✅ | The GitHub repository URL |
   124|| `authorization_token` | ✅ | GitHub Personal Access Token with repository access. **Never echoed in API responses.** |
   125|| `mount_path` | ❌ | Path where the repository will be cloned. Defaults to `/workspace/<repo-name>`. |
   126|| `checkout` | ❌ | `{type: "branch", name: "..."}` or `{type: "commit", sha: "..."}`. Defaults to the repo's default branch. |
   127|
   128|**Token permission levels** (fine-grained PATs):
   129|
   130|- `Contents: Read` — clone only
   131|- `Contents: Read and write` — push changes and create pull requests
   132|
   133|**How auth works:** `authorization_token` is never placed inside the container. `git pull` / `git push` and GitHub REST calls against the attached repository are routed through an Anthropic-side git proxy that injects the token after the request leaves the sandbox. Code running in the container — including anything the agent writes — cannot read or exfiltrate it.
   134|
   135|> ‼️ **To generate pull requests** you also need GitHub **MCP server** access — the `github_repository` resource gives filesystem + git access only. See `shared/managed-agents-tools.md` → MCP Servers. The PR workflow is: edit files in the mounted repo → push branch via `bash` (authenticated via the git proxy using `authorization_token`) → create PR via the MCP `create_pull_request` tool (authenticated via the vault).
   136|
   137|**TypeScript:**
   138|
   139|```ts
   140|// 1. Create the agent — declare GitHub MCP (no auth here)
   141|const agent = await client.beta.agents.create({
   142|  name: "GitHub Agent",
   143|  model: "claude-opus-4-7",
   144|  mcp_servers: [
   145|    {
   146|      type: "url",
   147|      name: "github",
   148|      url: "https://api.githubcopilot.com/mcp/"
   149|    }
   150|  ],
   151|  tools: [
   152|    {
   153|      type: "agent_toolset_20260401",
   154|      default_config: { enabled: true }
   155|    },
   156|    { type: "mcp_toolset", mcp_server_name: "github" }
   157|  ]
   158|});
   159|
   160|// 2. Start a session — attach vault for MCP auth + mount the repo
   161|const session = await client.beta.sessions.create({
   162|  agent: agent.id,
   163|  environment_id: envId,
   164|  vault_ids: [vaultId], // vault contains the GitHub MCP OAuth credential
   165|  resources: [
   166|    {
   167|      type: "github_repository",
   168|      url: "https://github.com/owner/repo",
   169|      authorization_token: process.env.GITHUB_TOKEN, // repo clone token (≠ MCP auth)
   170|      checkout: { type: "branch", name: "main" }
   171|    }
   172|  ]
   173|});
   174|```
   175|
   176|**Python:**
   177|
   178|```python
   179|import os
   180|
   181|agent = client.beta.agents.create(
   182|    name="GitHub Agent",
   183|    model="claude-opus-4-7",
   184|    mcp_servers=[{
   185|        "type": "url",
   186|        "name": "github",
   187|        "url": "https://api.githubcopilot.com/mcp/",
   188|    }],
   189|    tools=[
   190|        {"type": "agent_toolset_20260401", "default_config": {"enabled": True}},
   191|        {"type": "mcp_toolset", "mcp_server_name": "github"},
   192|    ],
   193|)
   194|
   195|session = client.beta.sessions.create(
   196|    agent=agent.id,
   197|    environment_id=env_id,
   198|    vault_ids=[vault_id],  # vault contains the GitHub MCP OAuth credential
   199|    resources=[{
   200|        "type": "github_repository",
   201|        "url": "https://github.com/owner/repo",
   202|        "authorization_token": os.environ["GITHUB_TOKEN"],  # repo clone token (≠ MCP auth)
   203|        "checkout": {"type": "branch", "name": "main"},
   204|    }],
   205|)
   206|```
   207|
   208|---
   209|
   210|## Files API
   211|
   212|Upload and manage files for use as session resources, and download files the agent wrote to `/mnt/session/outputs/`.
   213|
   214|| Operation | Method | Path | SDK |
   215|| --- | --- | --- | --- |
   216|| Upload | `POST` | `/v1/files` | `client.beta.files.upload({ file })` |
   217|| List | `GET` | `/v1/files?scope_id=...` | `client.beta.files.list({ scope_id, betas: ["managed-agents-2026-04-01"] })` |
   218|| Get Metadata | `GET` | `/v1/files/{id}` | `client.beta.files.retrieveMetadata(id)` |
   219|| Download | `GET` | `/v1/files/{id}/content` | `client.beta.files.download(id)` → `Response` |
   220|| Delete | `DELETE` | `/v1/files/{id}` | `client.beta.files.delete(id)` |
   221|
   222|The `scope_id` filter on List scopes the results to files written to `/mnt/session/outputs/` by that session. Without the filter, you get all files uploaded to your account.
   223|