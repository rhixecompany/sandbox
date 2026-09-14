---
name: readme-managed-agents
description: "Managed Agents — Ruby"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Ruby
     2|
     3|> **Bindings not shown here:** This README covers the most common managed-agents flows for Ruby. If you need a class, method, namespace, field, or behavior that isn't shown, WebFetch the Ruby SDK repo **or the relevant docs page** from `shared/live-sources.md` rather than guess. Do not extrapolate from cURL shapes or another language's SDK.
     4|
     5|> **Agents are persistent — create once, reference by ID.** Store the agent ID returned by `client.beta.agents.create` and pass it to every subsequent `client.beta.sessions.create`; do not call `agents.create` in the request path. The Anthropic CLI is one convenient way to create agents and environments from version-controlled YAML — its URL is in `shared/live-sources.md`. The examples below show in-code creation for completeness; in production the create call belongs in setup, not in the request path.
     6|
     7|## Installation
     8|
     9|```bash
    10|gem install anthropic
    11|```
    12|
    13|## Client Initialization
    14|
    15|```ruby
    16|require "anthropic"
    17|
    18|# Default (uses ANTHROPIC_API_KEY env var)
    19|client = Anthropic::Client.new
    20|
    21|# Explicit API key
    22|client = Anthropic::Client.new(api_key: "your-api-key")
    23|```
    24|
    25|> ⚠️ **Trailing underscores:** The Ruby SDK uses `system_:` and `send_(` (trailing underscore) to avoid shadowing `Kernel#system` and `Kernel#send`. Use these forms throughout managed-agents code.
    26|
    27|---
    28|
    29|## Create an Environment
    30|
    31|```ruby
    32|environment = client.beta.environments.create(
    33|  name: "my-dev-env",
    34|  config: {
    35|    type: "cloud",
    36|    networking: {type: "unrestricted"}
    37|  }
    38|)
    39|puts "Environment ID: #{environment.id}" # env_...
    40|```
    41|
    42|---
    43|
    44|## Create an Agent (required first step)
    45|
    46|> ⚠️ **There is no inline agent config.** `model`/`system_`/`tools` live on the agent object, not the session. Always start with `client.beta.agents.create()` — the session takes either `agent: agent.id` or the typed hash form `agent: {type: "agent", id: agent.id, version: agent.version}`.
    47|
    48|### Minimal
    49|
    50|```ruby
    51|# 1. Create the agent (reusable, versioned)
    52|agent = client.beta.agents.create(
    53|  name: "Coding Assistant",
    54|  model: :"claude-opus-4-7",
    55|  system_: "You are a helpful coding assistant.",
    56|  tools: [{type: "agent_toolset_20260401"}]
    57|)
    58|
    59|# 2. Start a session
    60|session = client.beta.sessions.create(
    61|  agent: {type: "agent", id: agent.id, version: agent.version},
    62|  environment_id: environment.id,
    63|  title: "Quickstart session"
    64|)
    65|puts "Session ID: #{session.id}"
    66|```
    67|
    68|### Updating an Agent
    69|
    70|Updates create new versions; the agent object is immutable per version.
    71|
    72|```ruby
    73|updated_agent = client.beta.agents.update(
    74|  agent.id,
    75|  version: agent.version,
    76|  system_: "You are a helpful coding agent. Always write tests."
    77|)
    78|puts "New version: #{updated_agent.version}"
    79|
    80|# List all versions
    81|client.beta.agents.versions.list(agent.id).auto_paging_each do |version|
    82|  puts "Version #{version.version}: #{version.updated_at.iso8601}"
    83|end
    84|
    85|# Archive the agent
    86|archived = client.beta.agents.archive(agent.id)
    87|puts "Archived at: #{archived.archived_at.iso8601}"
    88|```
    89|
    90|---
    91|
    92|## Send a User Message
    93|
    94|```ruby
    95|client.beta.sessions.events.send_(
    96|  session.id,
    97|  events: [{
    98|    type: "user.message",
    99|    content: [{type: "text", text: "Review the auth module"}]
   100|  }]
   101|)
   102|```
   103|
   104|> 💡 **Stream-first:** Open the stream _before_ (or concurrently with) sending the message. The stream only delivers events that occur after it opens — stream-after-send means early events arrive buffered in one batch. See [Steering Patterns](../../shared/managed-agents-events.md#steering-patterns).
   105|
   106|---
   107|
   108|## Stream Events (SSE)
   109|
   110|```ruby
   111|# Open the stream first, then send the user message
   112|stream = client.beta.sessions.events.stream_events(session.id)
   113|
   114|client.beta.sessions.events.send_(
   115|  session.id,
   116|  events: [{
   117|    type: "user.message",
   118|    content: [{type: "text", text: "Summarize the repo README"}]
   119|  }]
   120|)
   121|
   122|stream.each do |event|
   123|  case event.type
   124|  in :"agent.message"
   125|    event.content.each { |block| print block.text }
   126|  in :"agent.tool_use"
   127|    puts "\n[Using tool: #{event.name}]"
   128|  in :"session.status_idle"
   129|    break
   130|  in :"session.error"
   131|    puts "\n[Error: #{event.error&.message || "unknown"}]"
   132|    break
   133|  else
   134|    # ignore other event types
   135|  end
   136|end
   137|```
   138|
   139|> ℹ️ Event `.type` is a Symbol (compare with `:"agent.message"`, not `"agent.message"`).
   140|
   141|### Reconnecting and Tailing
   142|
   143|When reconnecting mid-session, list past events first to dedupe, then tail live events:
   144|
   145|```ruby
   146|require "set"
   147|
   148|stream = client.beta.sessions.events.stream_events(session.id)
   149|
   150|# Stream is open and buffering. List history before tailing live.
   151|seen_event_ids = Set.new
   152|client.beta.sessions.events.list(session.id).auto_paging_each { |past| seen_event_ids << past.id }
   153|
   154|# Tail live events, skipping anything already seen
   155|stream.each do |event|
   156|  next if seen_event_ids.include?(event.id)
   157|  seen_event_ids << event.id
   158|  case event.type
   159|  in :"agent.message"
   160|    event.content.each { |block| print block.text }
   161|  in :"session.status_idle"
   162|    break
   163|  else
   164|    # ignore other event types
   165|  end
   166|end
   167|```
   168|
   169|---
   170|
   171|## Provide Custom Tool Result
   172|
   173|> ℹ️ The Ruby managed-agents bindings for `user.custom_tool_result` are not yet documented in this skill or in the apps source examples. Refer to `shared/managed-agents-events.md` for the wire format and the `anthropic` Ruby gem repository for the corresponding params.
   174|
   175|---
   176|
   177|## Poll Events
   178|
   179|```ruby
   180|client.beta.sessions.events.list(session.id).auto_paging_each do |event|
   181|  puts "#{event.type}: #{event.id}"
   182|end
   183|```
   184|
   185|---
   186|
   187|## Upload a File
   188|
   189|```ruby
   190|require "pathname"
   191|
   192|file = client.beta.files.upload(file: Pathname("data.csv"))
   193|puts "File ID: #{file.id}"
   194|
   195|# Mount in a session
   196|session = client.beta.sessions.create(
   197|  agent: agent.id,
   198|  environment_id: environment.id,
   199|  resources: [
   200|    {
   201|      type: "file",
   202|      file_id: file.id,
   203|      mount_path: "/workspace/data.csv"
   204|    }
   205|  ]
   206|)
   207|```
   208|
   209|### Add and Manage Resources on an Existing Session
   210|
   211|```ruby
   212|# Attach an additional file to an open session
   213|resource = client.beta.sessions.resources.add(
   214|  session.id,
   215|  type: "file",
   216|  file_id: file.id
   217|)
   218|puts resource.id # "sesrsc_01ABC..."
   219|
   220|# List resources on the session
   221|listed = client.beta.sessions.resources.list(session.id)
   222|listed.data.each { |entry| puts "#{entry.id} #{entry.type}" }
   223|
   224|# Detach a resource
   225|client.beta.sessions.resources.delete(resource.id, session_id: session.id)
   226|```
   227|
   228|---
   229|
   230|## List and Download Session Files
   231|
   232|> ℹ️ Listing and downloading files an agent wrote during a session is not yet documented for Ruby in this skill or in the apps source examples. See `shared/managed-agents-events.md` and the `anthropic` Ruby gem repository for the file list/download bindings.
   233|
   234|---
   235|
   236|## Session Management
   237|
   238|```ruby
   239|# List environments
   240|environments = client.beta.environments.list
   241|
   242|# Retrieve a specific environment
   243|env = client.beta.environments.retrieve(environment.id)
   244|
   245|# Archive an environment (read-only, existing sessions continue)
   246|client.beta.environments.archive(environment.id)
   247|
   248|# Delete an environment (only if no sessions reference it)
   249|client.beta.environments.delete(environment.id)
   250|
   251|# Delete a session
   252|client.beta.sessions.delete(session.id)
   253|```
   254|
   255|---
   256|
   257|## MCP Server Integration
   258|
   259|```ruby
   260|# Agent declares MCP server (no auth here — auth goes in a vault)
   261|agent = client.beta.agents.create(
   262|  name: "GitHub Assistant",
   263|  model: :"claude-opus-4-7",
   264|  mcp_servers: [
   265|    {
   266|      type: "url",
   267|      name: "github",
   268|      url: "https://api.githubcopilot.com/mcp/"
   269|    }
   270|  ],
   271|  tools: [
   272|    {type: "agent_toolset_20260401"},
   273|    {type: "mcp_toolset", mcp_server_name: "github"}
   274|  ]
   275|)
   276|
   277|# Session attaches vault(s) containing credentials for those MCP server URLs
   278|session = client.beta.sessions.create(
   279|  agent: {type: "agent", id: agent.id, version: agent.version},
   280|  environment_id: environment.id,
   281|  vault_ids: [vault.id]
   282|)
   283|```
   284|
   285|See `shared/managed-agents-tools.md` §Vaults for creating vaults and adding credentials.
   286|
   287|---
   288|
   289|## Vaults
   290|
   291|```ruby
   292|# Create a vault
   293|vault = client.beta.vaults.create(
   294|  display_name: "Alice",
   295|  metadata: {external_user_id: "usr_abc123"}
   296|)
   297|puts vault.id # "vlt_01ABC..."
   298|
   299|# Add an OAuth credential
   300|credential = client.beta.vaults.credentials.create(
   301|  vault.id,
   302|  display_name: "Alice's Slack",
   303|  auth: {
   304|    type: "mcp_oauth",
   305|    mcp_server_url: "https://mcp.slack.com/mcp",
   306|    access_token: "xoxp-...",
   307|    expires_at: "2026-04-15T00:00:00Z",
   308|    refresh: {
   309|      token_endpoint: "https://slack.com/api/oauth.v2.access",
   310|      client_id: "1234567890.0987654321",
   311|      scope: "channels:read chat:write",
   312|      refresh_token: "xoxe-1-...",
   313|      token_endpoint_auth: {
   314|        type: "client_secret_post",
   315|        client_secret: "abc123..."
   316|      }
   317|    }
   318|  }
   319|)
   320|
   321|# Rotate the credential (e.g., after a token refresh)
   322|client.beta.vaults.credentials.update(
   323|  credential.id,
   324|  vault_id: vault.id,
   325|  auth: {
   326|    type: "mcp_oauth",
   327|    access_token: "xoxp-new-...",
   328|    expires_at: "2026-05-15T00:00:00Z",
   329|    refresh: {refresh_token: "xoxe-1-new-..."}
   330|  }
   331|)
   332|
   333|# Archive a vault
   334|client.beta.vaults.archive(vault.id)
   335|```
   336|
   337|---
   338|
   339|## GitHub Repository Integration
   340|
   341|Mount a GitHub repository as a session resource (a vault holds the GitHub MCP credential):
   342|
   343|```ruby
   344|session = client.beta.sessions.create(
   345|  agent: agent.id,
   346|  environment_id: environment.id,
   347|  vault_ids: [vault.id],
   348|  resources: [
   349|    {
   350|      type: "github_repository",
   351|      url: "https://github.com/org/repo",
   352|      mount_path: "/workspace/repo",
   353|      authorization_token: "ghp_your_github_token"
   354|    }
   355|  ]
   356|)
   357|```
   358|
   359|Multiple repositories on the same session:
   360|
   361|```ruby
   362|resources = [
   363|  {
   364|    type: "github_repository",
   365|    url: "https://github.com/org/frontend",
   366|    mount_path: "/workspace/frontend",
   367|    authorization_token: "ghp_your_github_token"
   368|  },
   369|  {
   370|    type: "github_repository",
   371|    url: "https://github.com/org/backend",
   372|    mount_path: "/workspace/backend",
   373|    authorization_token: "ghp_your_github_token"
   374|  }
   375|]
   376|```
   377|
   378|Rotating a repository's authorization token:
   379|
   380|```ruby
   381|listed = client.beta.sessions.resources.list(session.id)
   382|repo_resource_id = listed.data.first.id
   383|
   384|client.beta.sessions.resources.update(
   385|  repo_resource_id,
   386|  session_id: session.id,
   387|  authorization_token: "ghp_your_new_github_token"
   388|)
   389|```
   390|