---
name: managed-agents-php
description: "Managed Agents — PHP"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — PHP
     2|
     3|> **Bindings not shown here:** This README covers the most common managed-agents flows for PHP. If you need a class, method, namespace, field, or behavior that isn't shown, WebFetch the PHP SDK repo **or the relevant docs page** from `shared/live-sources.md` rather than guess. Do not extrapolate from cURL shapes or another language's SDK.
     4|
     5|> **Agents are persistent — create once, reference by ID.** Store the agent ID returned by `$client->beta->agents->create` and pass it to every subsequent `->sessions->create`; do not call `agents->create` in the request path. The Anthropic CLI is one convenient way to create agents and environments from version-controlled YAML — its URL is in `shared/live-sources.md`. The examples below show in-code creation for completeness; in production the create call belongs in setup, not in the request path.
     6|
     7|## Installation
     8|
     9|```bash
    10|composer require "anthropic-ai/sdk"
    11|```
    12|
    13|## Client Initialization
    14|
    15|```php
    16|use Anthropic\Client;
    17|
    18|// Default (uses ANTHROPIC_API_KEY env var)
    19|$client = new Client();
    20|
    21|// Explicit API key
    22|$client = new Client(apiKey: 'your-api-key');
    23|```
    24|
    25|---
    26|
    27|## Create an Environment
    28|
    29|```php
    30|$environment = $client->beta->environments->create(
    31|    name: 'my-dev-env',
    32|    config: ['type' => 'cloud', 'networking' => ['type' => 'unrestricted']],
    33|);
    34|echo "Environment ID: {$environment->id}\n"; // env_...
    35|```
    36|
    37|---
    38|
    39|## Create an Agent (required first step)
    40|
    41|> ⚠️ **There is no inline agent config.** `model`/`system`/`tools` live on the agent object, not the session. Always start with `$client->beta->agents->create()` — the session takes either `agent: $agent->id` or the typed `BetaManagedAgentsAgentParams::with(type: 'agent', id: $agent->id, version: $agent->version)`.
    42|
    43|### Minimal
    44|
    45|```php
    46|use Anthropic\Beta\Agents\BetaManagedAgentsAgentToolset20260401Params;
    47|
    48|// 1. Create the agent (reusable, versioned)
    49|$agent = $client->beta->agents->create(
    50|    name: 'Coding Assistant',
    51|    model: 'claude-opus-4-7',
    52|    system: 'You are a helpful coding assistant.',
    53|    tools: [
    54|        BetaManagedAgentsAgentToolset20260401Params::with(
    55|            type: 'agent_toolset_20260401',
    56|        ),
    57|    ],
    58|);
    59|
    60|// 2. Start a session
    61|$session = $client->beta->sessions->create(
    62|    agent: ['type' => 'agent', 'id' => $agent->id, 'version' => $agent->version],
    63|    environmentID: $environment->id,
    64|    title: 'Quickstart session',
    65|);
    66|echo "Session ID: {$session->id}\n";
    67|```
    68|
    69|### Updating an Agent
    70|
    71|Updates create new versions; the agent object is immutable per version.
    72|
    73|```php
    74|$updatedAgent = $client->beta->agents->update(
    75|    $agent->id,
    76|    version: $agent->version,
    77|    system: 'You are a helpful coding agent. Always write tests.',
    78|);
    79|echo "New version: {$updatedAgent->version}\n";
    80|
    81|// List all versions
    82|foreach ($client->beta->agents->versions->list($agent->id)->pagingEachItem() as $version) {
    83|    echo "Version {$version->version}: {$version->updatedAt->format(DateTimeInterface::ATOM)}\n";
    84|}
    85|
    86|// Archive the agent
    87|$archived = $client->beta->agents->archive($agent->id);
    88|echo "Archived at: {$archived->archivedAt->format(DateTimeInterface::ATOM)}\n";
    89|```
    90|
    91|---
    92|
    93|## Send a User Message
    94|
    95|```php
    96|$client->beta->sessions->events->send(
    97|    $session->id,
    98|    events: [
    99|        [
   100|            'type' => 'user.message',
   101|            'content' => [['type' => 'text', 'text' => 'Review the auth module']],
   102|        ],
   103|    ],
   104|);
   105|```
   106|
   107|> 💡 **Stream-first:** Open the stream _before_ (or concurrently with) sending the message. The stream only delivers events that occur after it opens — stream-after-send means early events arrive buffered in one batch. See [Steering Patterns](../../shared/managed-agents-events.md#steering-patterns).
   108|
   109|---
   110|
   111|## Stream Events (SSE)
   112|
   113|> ℹ️ **Streaming transporter:** PHP's default buffered PSR-18 client never returns for the open-ended session event stream. Use a streaming Guzzle transporter for `streamStream()` calls — other calls keep the default client.
   114|
   115|```php
   116|$streamingClient = new GuzzleHttp\Client(['stream' => true]);
   117|
   118|// Open the stream first, then send the user message
   119|$stream = $client->beta->sessions->events->streamStream(
   120|    $session->id,
   121|    requestOptions: ['transporter' => $streamingClient],
   122|);
   123|$client->beta->sessions->events->send(
   124|    $session->id,
   125|    events: [
   126|        [
   127|            'type' => 'user.message',
   128|            'content' => [['type' => 'text', 'text' => 'Summarize the repo README']],
   129|        ],
   130|    ],
   131|);
   132|
   133|foreach ($stream as $event) {
   134|    match ($event->type) {
   135|        'agent.message' => array_walk(
   136|            $event->content,
   137|            static fn($block) => $block->type === 'text' ? print($block->text) : null,
   138|        ),
   139|        'agent.tool_use' => print("\n[Using tool: {$event->name}]\n"),
   140|        'session.error' => printf("\n[Error: %s]", $event->error?->message ?? 'unknown'),
   141|        default => null,
   142|    };
   143|    if ($event->type === 'session.status_idle' || $event->type === 'session.error') {
   144|        break;
   145|    }
   146|}
   147|$stream->close();
   148|```
   149|
   150|### Reconnecting and Tailing
   151|
   152|When reconnecting mid-session, list past events first to dedupe, then tail live events:
   153|
   154|```php
   155|$stream = $client->beta->sessions->events->streamStream(
   156|    $session->id,
   157|    requestOptions: ['transporter' => $streamingClient],
   158|);
   159|
   160|// Stream is open and buffering. List history before tailing live.
   161|$seenEventIds = [];
   162|foreach ($client->beta->sessions->events->list($session->id)->pagingEachItem() as $event) {
   163|    $seenEventIds[$event->id] = true;
   164|}
   165|
   166|// Tail live events, skipping anything already seen
   167|foreach ($stream as $event) {
   168|    if (isset($seenEventIds[$event->id])) {
   169|        continue;
   170|    }
   171|    $seenEventIds[$event->id] = true;
   172|    match ($event->type) {
   173|        'agent.message' => array_walk(
   174|            $event->content,
   175|            static fn($block) => $block->type === 'text' ? print($block->text) : null,
   176|        ),
   177|        default => null,
   178|    };
   179|    if ($event->type === 'session.status_idle') {
   180|        break;
   181|    }
   182|}
   183|$stream->close();
   184|```
   185|
   186|---
   187|
   188|## Provide Custom Tool Result
   189|
   190|> ℹ️ The PHP managed-agents bindings for `user.custom_tool_result` are not yet documented in this skill or in the apps source examples. Refer to `shared/managed-agents-events.md` for the wire format and the `anthropic-ai/sdk` PHP repository for the corresponding params.
   191|
   192|---
   193|
   194|## Poll Events
   195|
   196|```php
   197|foreach ($client->beta->sessions->events->list($session->id)->pagingEachItem() as $event) {
   198|    echo "{$event->type}: {$event->id}\n";
   199|}
   200|```
   201|
   202|---
   203|
   204|## Upload a File
   205|
   206|> ℹ️ **PHP file upload:** The PHP SDK's beta managed-agents file upload binding is not shown in the apps source examples; the canonical PHP example uses raw cURL against `POST /v1/files`. If your codebase prefers the SDK, WebFetch the `anthropic-ai/sdk` PHP repository for the latest binding before writing code.
   207|
   208|```php
   209|use Anthropic\Beta\Sessions\BetaManagedAgentsFileResourceParams;
   210|
   211|// Raw cURL upload (canonical example from the apps source)
   212|$csvPath = 'data.csv';
   213|$ch = curl_init('https://api.anthropic.com/v1/files');
   214|curl_setopt_array($ch, [
   215|    CURLOPT_RETURNTRANSFER => true,
   216|    CURLOPT_POST => true,
   217|    CURLOPT_HTTPHEADER => [
   218|        'x-api-key: ' . getenv('ANTHROPIC_API_KEY'),
   219|        'anthropic-version: 2023-06-01',
   220|        'anthropic-beta: files-api-2025-04-14',
   221|    ],
   222|    CURLOPT_POSTFIELDS => ['file' => new CURLFile($csvPath, 'text/csv', 'data.csv')],
   223|]);
   224|$file = json_decode(curl_exec($ch));
   225|echo "File ID: {$file->id}\n";
   226|
   227|// Mount in a session
   228|$session = $client->beta->sessions->create(
   229|    agent: $agent->id,
   230|    environmentID: $environment->id,
   231|    resources: [
   232|        BetaManagedAgentsFileResourceParams::with(
   233|            type: 'file',
   234|            fileID: $file->id,
   235|            mountPath: '/workspace/data.csv',
   236|        ),
   237|    ],
   238|);
   239|```
   240|
   241|### Add and Manage Resources on an Existing Session
   242|
   243|```php
   244|// Attach an additional file to an open session
   245|$resource = $client->beta->sessions->resources->add(
   246|    $session->id,
   247|    type: 'file',
   248|    fileID: $file->id,
   249|);
   250|echo "{$resource->id}\n"; // "sesrsc_01ABC..."
   251|
   252|// List resources on the session
   253|$listed = $client->beta->sessions->resources->list($session->id);
   254|foreach ($listed->data as $entry) {
   255|    echo "{$entry->id} {$entry->type}\n";
   256|}
   257|
   258|// Detach a resource
   259|$client->beta->sessions->resources->delete($resource->id, sessionID: $session->id);
   260|```
   261|
   262|---
   263|
   264|## List and Download Session Files
   265|
   266|> ℹ️ Listing and downloading files an agent wrote during a session is not yet documented for PHP in this skill or in the apps source examples. See `shared/managed-agents-events.md` and the `anthropic-ai/sdk` PHP repository for the file list/download bindings.
   267|
   268|---
   269|
   270|## Session Management
   271|
   272|```php
   273|// List environments
   274|$environments = $client->beta->environments->list();
   275|
   276|// Retrieve a specific environment
   277|$env = $client->beta->environments->retrieve($environment->id);
   278|
   279|// Archive an environment (read-only, existing sessions continue)
   280|$client->beta->environments->archive($environment->id);
   281|
   282|// Delete an environment (only if no sessions reference it)
   283|$client->beta->environments->delete($environment->id);
   284|
   285|// Delete a session
   286|$client->beta->sessions->delete($session->id);
   287|```
   288|
   289|---
   290|
   291|## MCP Server Integration
   292|
   293|```php
   294|use Anthropic\Beta\Agents\BetaManagedAgentsAgentToolset20260401Params;
   295|use Anthropic\Beta\Agents\BetaManagedAgentsMCPToolsetParams;
   296|use Anthropic\Beta\Agents\BetaManagedAgentsUrlmcpServerParams;
   297|use Anthropic\Beta\Sessions\BetaManagedAgentsAgentParams;
   298|
   299|// Agent declares MCP server (no auth here — auth goes in a vault)
   300|$agent = $client->beta->agents->create(
   301|    name: 'GitHub Assistant',
   302|    model: 'claude-opus-4-7',
   303|    mcpServers: [
   304|        BetaManagedAgentsUrlmcpServerParams::with(
   305|            type: 'url',
   306|            name: 'github',
   307|            url: 'https://api.githubcopilot.com/mcp/',
   308|        ),
   309|    ],
   310|    tools: [
   311|        BetaManagedAgentsAgentToolset20260401Params::with(type: 'agent_toolset_20260401'),
   312|        BetaManagedAgentsMCPToolsetParams::with(
   313|            type: 'mcp_toolset',
   314|            mcpServerName: 'github',
   315|        ),
   316|    ],
   317|);
   318|
   319|// Session attaches vault(s) containing credentials for those MCP server URLs
   320|$session = $client->beta->sessions->create(
   321|    agent: BetaManagedAgentsAgentParams::with(
   322|        type: 'agent',
   323|        id: $agent->id,
   324|        version: $agent->version,
   325|    ),
   326|    environmentID: $environment->id,
   327|    vaultIDs: [$vault->id],
   328|);
   329|```
   330|
   331|See `shared/managed-agents-tools.md` §Vaults for creating vaults and adding credentials.
   332|
   333|---
   334|
   335|## Vaults
   336|
   337|```php
   338|// Create a vault
   339|$vault = $client->beta->vaults->create(
   340|    displayName: 'Alice',
   341|    metadata: ['external_user_id' => 'usr_abc123'],
   342|);
   343|echo $vault->id . "\n"; // "vlt_01ABC..."
   344|
   345|// Add an OAuth credential
   346|$credential = $client->beta->vaults->credentials->create(
   347|    vaultID: $vault->id,
   348|    displayName: "Alice's Slack",
   349|    auth: [
   350|        'type' => 'mcp_oauth',
   351|        'mcp_server_url' => 'https://mcp.slack.com/mcp',
   352|        'access_token' => 'xoxp-...',
   353|        'expires_at' => '2026-04-15T00:00:00Z',
   354|        'refresh' => [
   355|            'token_endpoint' => 'https://slack.com/api/oauth.v2.access',
   356|            'client_id' => '1234567890.0987654321',
   357|            'scope' => 'channels:read chat:write',
   358|            'refresh_token' => 'xoxe-1-...',
   359|            'token_endpoint_auth' => [
   360|                'type' => 'client_secret_post',
   361|                'client_secret' => 'abc123...',
   362|            ],
   363|        ],
   364|    ],
   365|);
   366|
   367|// Rotate the credential (e.g., after a token refresh)
   368|$client->beta->vaults->credentials->update(
   369|    $credential->id,
   370|    vaultID: $vault->id,
   371|    auth: [
   372|        'type' => 'mcp_oauth',
   373|        'access_token' => 'xoxp-new-...',
   374|        'expires_at' => '2026-05-15T00:00:00Z',
   375|        'refresh' => ['refresh_token' => 'xoxe-1-new-...'],
   376|    ],
   377|);
   378|
   379|// Archive a vault
   380|$client->beta->vaults->archive($vault->id);
   381|```
   382|
   383|---
   384|
   385|## GitHub Repository Integration
   386|
   387|Mount a GitHub repository as a session resource (a vault holds the GitHub MCP credential):
   388|
   389|```php
   390|$session = $client->beta->sessions->create(
   391|    agent: $agent->id,
   392|    environmentID: $environment->id,
   393|    vaultIDs: [$vault->id],
   394|    resources: [
   395|        [
   396|            'type' => 'github_repository',
   397|            'url' => 'https://github.com/org/repo',
   398|            'mountPath' => '/workspace/repo',
   399|            'authorizationToken' => 'ghp_your_github_token',
   400|        ],
   401|    ],
   402|);
   403|```
   404|
   405|Multiple repositories on the same session:
   406|
   407|```php
   408|$resources = [
   409|    [
   410|        'type' => 'github_repository',
   411|        'url' => 'https://github.com/org/frontend',
   412|        'mountPath' => '/workspace/frontend',
   413|        'authorizationToken' => 'ghp_your_github_token',
   414|    ],
   415|    [
   416|        'type' => 'github_repository',
   417|        'url' => 'https://github.com/org/backend',
   418|        'mountPath' => '/workspace/backend',
   419|        'authorizationToken' => 'ghp_your_github_token',
   420|    ],
   421|];
   422|```
   423|
   424|Rotating a repository's authorization token:
   425|
   426|```php
   427|$listed = $client->beta->sessions->resources->list($session->id);
   428|$repoResourceId = $listed->data[0]->id;
   429|
   430|$client->beta->sessions->resources->update(
   431|    $repoResourceId,
   432|    sessionID: $session->id,
   433|    authorizationToken: 'ghp_your_new_github_token',
   434|);
   435|```
   436|