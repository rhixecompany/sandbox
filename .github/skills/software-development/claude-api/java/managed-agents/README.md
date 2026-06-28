---
name: managed-agents-java
description: "Managed Agents — Java"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Java
     2|
     3|> **Bindings not shown here:** This README covers the most common managed-agents flows for Java. If you need a class, method, namespace, field, or behavior that isn't shown, WebFetch the Java SDK repo **or the relevant docs page** from `shared/live-sources.md` rather than guess. Do not extrapolate from cURL shapes or another language's SDK.
     4|
     5|> **Agents are persistent — create once, reference by ID.** Store the agent ID returned by `client.beta().agents().create` and pass it to every subsequent `client.beta().sessions().create`; do not call `agents().create` in the request path. The Anthropic CLI is one convenient way to create agents and environments from version-controlled YAML — its URL is in `shared/live-sources.md`. The examples below show in-code creation for completeness; in production the create call belongs in setup, not in the request path.
     6|
     7|## Installation
     8|
     9|```xml
    10|<dependency>
    11|    <groupId>com.anthropic</groupId>
    12|    <artifactId>anthropic-java</artifactId>
    13|</dependency>
    14|```
    15|
    16|## Client Initialization
    17|
    18|```java
    19|import com.anthropic.client.okhttp.AnthropicOkHttpClient;
    20|
    21|// Default (uses ANTHROPIC_API_KEY env var)
    22|var client = AnthropicOkHttpClient.fromEnv();
    23|```
    24|
    25|---
    26|
    27|## Create an Environment
    28|
    29|```java
    30|import com.anthropic.models.beta.environments.BetaCloudConfigParams;
    31|import com.anthropic.models.beta.environments.EnvironmentCreateParams;
    32|import com.anthropic.models.beta.environments.UnrestrictedNetwork;
    33|
    34|var environment = client.beta().environments().create(EnvironmentCreateParams.builder()
    35|    .name("my-dev-env")
    36|    .config(BetaCloudConfigParams.builder()
    37|        .networking(UnrestrictedNetwork.builder().build())
    38|        .build())
    39|    .build());
    40|System.out.println("Environment ID: " + environment.id()); // env_...
    41|```
    42|
    43|---
    44|
    45|## Create an Agent (required first step)
    46|
    47|> ⚠️ **There is no inline agent config.** Model, system, and tools live on the agent object, not the session. Always start with `client.beta().agents().create()` — the session takes either `.agent(agent.id())` or the typed `BetaManagedAgentsAgentParams.builder()...build()`.
    48|
    49|### Minimal
    50|
    51|```java
    52|import com.anthropic.models.beta.agents.AgentCreateParams;
    53|import com.anthropic.models.beta.agents.BetaManagedAgentsAgentToolset20260401Params;
    54|import com.anthropic.models.beta.sessions.BetaManagedAgentsAgentParams;
    55|import com.anthropic.models.beta.sessions.SessionCreateParams;
    56|
    57|// 1. Create the agent (reusable, versioned)
    58|var agent = client.beta().agents().create(AgentCreateParams.builder()
    59|    .name("Coding Assistant")
    60|    .model("claude-opus-4-7")
    61|    .system("You are a helpful coding assistant.")
    62|    .addTool(BetaManagedAgentsAgentToolset20260401Params.builder()
    63|        .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
    64|        .build())
    65|    .build());
    66|
    67|// 2. Start a session
    68|var session = client.beta().sessions().create(SessionCreateParams.builder()
    69|    .agent(BetaManagedAgentsAgentParams.builder()
    70|        .type(BetaManagedAgentsAgentParams.Type.AGENT)
    71|        .id(agent.id())
    72|        .version(agent.version())
    73|        .build())
    74|    .environmentId(environment.id())
    75|    .title("Quickstart session")
    76|    .build());
    77|System.out.println("Session ID: " + session.id());
    78|```
    79|
    80|### Updating an Agent
    81|
    82|Updates create new versions; the agent object is immutable per version.
    83|
    84|```java
    85|import com.anthropic.models.beta.agents.AgentUpdateParams;
    86|
    87|var updatedAgent = client.beta().agents().update(agent.id(), AgentUpdateParams.builder()
    88|    .version(agent.version())
    89|    .system("You are a helpful coding agent. Always write tests.")
    90|    .build());
    91|System.out.println("New version: " + updatedAgent.version());
    92|
    93|// List all versions
    94|for (var version : client.beta().agents().versions().list(agent.id()).autoPager()) {
    95|    System.out.println("Version " + version.version() + ": " + version.updatedAt());
    96|}
    97|
    98|// Archive the agent
    99|var archived = client.beta().agents().archive(agent.id());
   100|System.out.println("Archived at: " + archived.archivedAt().orElseThrow());
   101|```
   102|
   103|---
   104|
   105|## Send a User Message
   106|
   107|```java
   108|import com.anthropic.models.beta.sessions.events.BetaManagedAgentsUserMessageEventParams;
   109|import com.anthropic.models.beta.sessions.events.EventSendParams;
   110|
   111|client.beta().sessions().events().send(session.id(), EventSendParams.builder()
   112|    .addEvent(BetaManagedAgentsUserMessageEventParams.builder()
   113|        .type(BetaManagedAgentsUserMessageEventParams.Type.USER_MESSAGE)
   114|        .addTextContent("Review the auth module")
   115|        .build())
   116|    .build());
   117|```
   118|
   119|> 💡 **Stream-first:** Open the stream _before_ (or concurrently with) sending the message. The stream only delivers events that occur after it opens — stream-after-send means early events arrive buffered in one batch. See [Steering Patterns](../../shared/managed-agents-events.md#steering-patterns).
   120|
   121|---
   122|
   123|## Stream Events (SSE)
   124|
   125|```java
   126|import com.anthropic.models.beta.sessions.events.StreamEvents;
   127|
   128|// Open the stream first, then send the user message
   129|try (var stream = client.beta().sessions().events().streamStreaming(session.id())) {
   130|    client.beta().sessions().events().send(session.id(), EventSendParams.builder()
   131|        .addEvent(BetaManagedAgentsUserMessageEventParams.builder()
   132|            .type(BetaManagedAgentsUserMessageEventParams.Type.USER_MESSAGE)
   133|            .addTextContent("Summarize the repo README")
   134|            .build())
   135|        .build());
   136|
   137|    for (var event : (Iterable<StreamEvents>) stream.stream()::iterator) {
   138|        if (event.isAgentMessage()) {
   139|            event.asAgentMessage().content().forEach(block -> System.out.print(block.text()));
   140|        } else if (event.isAgentToolUse()) {
   141|            System.out.println("\n[Using tool: " + event.asAgentToolUse().name() + "]");
   142|        } else if (event.isSessionStatusIdle()) {
   143|            break;
   144|        } else if (event.isSessionError()) {
   145|            System.out.println("\n[Error]");
   146|            break;
   147|        }
   148|    }
   149|}
   150|```
   151|
   152|### Reconnecting and Tailing
   153|
   154|When reconnecting mid-session, list past events first to dedupe, then tail live events. The cross-variant `id` field is read from the raw `_json()` value:
   155|
   156|```java
   157|import com.anthropic.core.JsonValue;
   158|import java.util.HashSet;
   159|import java.util.Map;
   160|import java.util.Optional;
   161|
   162|try (var stream = client.beta().sessions().events().streamStreaming(session.id())) {
   163|    // Stream is open and buffering. List history before tailing live.
   164|    var seenEventIds = new HashSet<String>();
   165|    for (var past : client.beta().sessions().events().list(session.id()).autoPager()) {
   166|        Optional<Map<String, JsonValue>> obj = past._json().orElseThrow().asObject();
   167|        seenEventIds.add(obj.orElseThrow().get("id").asStringOrThrow());
   168|    }
   169|
   170|    // Tail live events, skipping anything already seen
   171|    for (var event : (Iterable<StreamEvents>) stream.stream()::iterator) {
   172|        Optional<Map<String, JsonValue>> obj = event._json().orElseThrow().asObject();
   173|        if (!seenEventIds.add(obj.orElseThrow().get("id").asStringOrThrow())) continue;
   174|        if (event.isAgentMessage()) {
   175|            event.asAgentMessage().content().forEach(block -> System.out.print(block.text()));
   176|        } else if (event.isSessionStatusIdle()) {
   177|            break;
   178|        }
   179|    }
   180|}
   181|```
   182|
   183|---
   184|
   185|## Provide Custom Tool Result
   186|
   187|> ℹ️ The Java managed-agents bindings for `user.custom_tool_result` are not yet documented in this skill or in the apps source examples. Refer to `shared/managed-agents-events.md` for the wire format and the `anthropic-java` repository for the corresponding params types.
   188|
   189|---
   190|
   191|## Poll Events
   192|
   193|```java
   194|for (var event : client.beta().sessions().events().list(session.id()).autoPager()) {
   195|    System.out.println(event.type() + ": " + event);
   196|}
   197|```
   198|
   199|---
   200|
   201|## Upload a File
   202|
   203|```java
   204|import com.anthropic.models.beta.files.FileUploadParams;
   205|import com.anthropic.models.beta.sessions.BetaManagedAgentsFileResourceParams;
   206|import java.nio.file.Path;
   207|
   208|var dataCsv = Path.of("data.csv");
   209|
   210|var file = client.beta().files().upload(FileUploadParams.builder()
   211|    .file(dataCsv)
   212|    .build());
   213|System.out.println("File ID: " + file.id());
   214|
   215|// Mount in a session
   216|var session = client.beta().sessions().create(SessionCreateParams.builder()
   217|    .agent(agent.id())
   218|    .environmentId(environment.id())
   219|    .addResource(BetaManagedAgentsFileResourceParams.builder()
   220|        .type(BetaManagedAgentsFileResourceParams.Type.FILE)
   221|        .fileId(file.id())
   222|        .mountPath("/workspace/data.csv")
   223|        .build())
   224|    .build());
   225|```
   226|
   227|### Add and Manage Resources on an Existing Session
   228|
   229|```java
   230|import com.anthropic.models.beta.sessions.resources.ResourceAddParams;
   231|import com.anthropic.models.beta.sessions.resources.ResourceDeleteParams;
   232|
   233|// Attach an additional file to an open session
   234|var resource = client.beta().sessions().resources().add(session.id(), ResourceAddParams.builder()
   235|    .betaManagedAgentsFileResourceParams(BetaManagedAgentsFileResourceParams.builder()
   236|        .type(BetaManagedAgentsFileResourceParams.Type.FILE)
   237|        .fileId(file.id())
   238|        .build())
   239|    .build());
   240|System.out.println(resource.id()); // "sesrsc_01ABC..."
   241|
   242|// List resources on the session — entries are a discriminated union
   243|var listed = client.beta().sessions().resources().list(session.id());
   244|for (var entry : listed.data()) {
   245|    if (entry.isFile()) {
   246|        var fileResource = entry.asFile();
   247|        System.out.println(fileResource.id() + " " + fileResource.type());
   248|    } else if (entry.isGitHubRepository()) {
   249|        var repoResource = entry.asGitHubRepository();
   250|        System.out.println(repoResource.id() + " " + repoResource.type());
   251|    }
   252|}
   253|
   254|// Detach a resource
   255|client.beta().sessions().resources().delete(resource.id(), ResourceDeleteParams.builder()
   256|    .sessionId(session.id())
   257|    .build());
   258|```
   259|
   260|---
   261|
   262|## List and Download Session Files
   263|
   264|> ℹ️ Listing and downloading files an agent wrote during a session is not yet documented for Java in this skill or in the apps source examples. See `shared/managed-agents-events.md` and the `anthropic-java` repository for the file list/download bindings.
   265|
   266|---
   267|
   268|## Session Management
   269|
   270|```java
   271|// List environments
   272|var environments = client.beta().environments().list();
   273|
   274|// Retrieve a specific environment
   275|var env = client.beta().environments().retrieve(environment.id());
   276|
   277|// Archive an environment (read-only, existing sessions continue)
   278|client.beta().environments().archive(environment.id());
   279|
   280|// Delete an environment (only if no sessions reference it)
   281|client.beta().environments().delete(environment.id());
   282|
   283|// Delete a session
   284|client.beta().sessions().delete(session.id());
   285|```
   286|
   287|---
   288|
   289|## MCP Server Integration
   290|
   291|```java
   292|import com.anthropic.models.beta.agents.BetaManagedAgentsMcpToolsetParams;
   293|import com.anthropic.models.beta.agents.BetaManagedAgentsUrlmcpServerParams;
   294|
   295|// Agent declares MCP server (no auth here — auth goes in a vault)
   296|var agent = client.beta().agents().create(AgentCreateParams.builder()
   297|    .name("GitHub Assistant")
   298|    .model("claude-opus-4-7")
   299|    .addMcpServer(BetaManagedAgentsUrlmcpServerParams.builder()
   300|        .type(BetaManagedAgentsUrlmcpServerParams.Type.URL)
   301|        .name("github")
   302|        .url("https://api.githubcopilot.com/mcp/")
   303|        .build())
   304|    .addTool(BetaManagedAgentsAgentToolset20260401Params.builder()
   305|        .type(BetaManagedAgentsAgentToolset20260401Params.Type.AGENT_TOOLSET_20260401)
   306|        .build())
   307|    .addTool(BetaManagedAgentsMcpToolsetParams.builder()
   308|        .type(BetaManagedAgentsMcpToolsetParams.Type.MCP_TOOLSET)
   309|        .mcpServerName("github")
   310|        .build())
   311|    .build());
   312|
   313|// Session attaches vault(s) containing credentials for those MCP server URLs
   314|var session = client.beta().sessions().create(SessionCreateParams.builder()
   315|    .agent(BetaManagedAgentsAgentParams.builder()
   316|        .type(BetaManagedAgentsAgentParams.Type.AGENT)
   317|        .id(agent.id())
   318|        .version(agent.version())
   319|        .build())
   320|    .environmentId(environment.id())
   321|    .addVaultId(vault.id())
   322|    .build());
   323|```
   324|
   325|See `shared/managed-agents-tools.md` §Vaults for creating vaults and adding credentials.
   326|
   327|---
   328|
   329|## Vaults
   330|
   331|```java
   332|import com.anthropic.core.JsonValue;
   333|import com.anthropic.models.beta.vaults.VaultCreateParams;
   334|import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsMcpOAuthCreateParams;
   335|import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsMcpOAuthRefreshParams;
   336|import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsMcpOAuthRefreshUpdateParams;
   337|import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsMcpOAuthUpdateParams;
   338|import com.anthropic.models.beta.vaults.credentials.CredentialCreateParams;
   339|import com.anthropic.models.beta.vaults.credentials.CredentialUpdateParams;
   340|import java.time.OffsetDateTime;
   341|
   342|// Create a vault
   343|var vault = client.beta().vaults().create(VaultCreateParams.builder()
   344|    .displayName("Alice")
   345|    .metadata(VaultCreateParams.Metadata.builder()
   346|        .putAdditionalProperty("external_user_id", JsonValue.from("usr_abc123"))
   347|        .build())
   348|    .build());
   349|System.out.println(vault.id()); // "vlt_01ABC..."
   350|
   351|// Add an OAuth credential
   352|var credential = client.beta().vaults().credentials().create(vault.id(),
   353|    CredentialCreateParams.builder()
   354|        .displayName("Alice's Slack")
   355|        .auth(BetaManagedAgentsMcpOAuthCreateParams.builder()
   356|            .type(BetaManagedAgentsMcpOAuthCreateParams.Type.MCP_OAUTH)
   357|            .mcpServerUrl("https://mcp.slack.com/mcp")
   358|            .accessToken("xoxp-...")
   359|            .expiresAt(OffsetDateTime.parse("2026-04-15T00:00:00Z"))
   360|            .refresh(BetaManagedAgentsMcpOAuthRefreshParams.builder()
   361|                .tokenEndpoint("https://slack.com/api/oauth.v2.access")
   362|                .clientId("1234567890.0987654321")
   363|                .scope("channels:read chat:write")
   364|                .refreshToken("xoxe-1-...")
   365|                .clientSecretPostTokenEndpointAuth("abc123...")
   366|                .build())
   367|            .build())
   368|        .build());
   369|
   370|// Rotate the credential (e.g., after a token refresh)
   371|client.beta().vaults().credentials().update(credential.id(),
   372|    CredentialUpdateParams.builder()
   373|        .vaultId(vault.id())
   374|        .auth(BetaManagedAgentsMcpOAuthUpdateParams.builder()
   375|            .type(BetaManagedAgentsMcpOAuthUpdateParams.Type.MCP_OAUTH)
   376|            .accessToken("xoxp-new-...")
   377|            .expiresAt(OffsetDateTime.parse("2026-05-15T00:00:00Z"))
   378|            .refresh(BetaManagedAgentsMcpOAuthRefreshUpdateParams.builder()
   379|                .refreshToken("xoxe-1-new-...")
   380|                .build())
   381|            .build())
   382|        .build());
   383|
   384|// Archive a vault
   385|client.beta().vaults().archive(vault.id());
   386|```
   387|
   388|---
   389|
   390|## GitHub Repository Integration
   391|
   392|Mount a GitHub repository as a session resource (a vault holds the GitHub MCP credential):
   393|
   394|```java
   395|import com.anthropic.models.beta.sessions.BetaManagedAgentsGitHubRepositoryResourceParams;
   396|
   397|var session = client.beta().sessions().create(SessionCreateParams.builder()
   398|    .agent(agent.id())
   399|    .environmentId(environment.id())
   400|    .addVaultId(vault.id())
   401|    .addResource(BetaManagedAgentsGitHubRepositoryResourceParams.builder()
   402|        .type(BetaManagedAgentsGitHubRepositoryResourceParams.Type.GITHUB_REPOSITORY)
   403|        .url("https://github.com/org/repo")
   404|        .mountPath("/workspace/repo")
   405|        .authorizationToken("ghp_your_github_token")
   406|        .build())
   407|    .build());
   408|```
   409|
   410|Multiple repositories on the same session:
   411|
   412|```java
   413|import java.util.List;
   414|
   415|var resources = List.of(
   416|    BetaManagedAgentsGitHubRepositoryResourceParams.builder()
   417|        .type(BetaManagedAgentsGitHubRepositoryResourceParams.Type.GITHUB_REPOSITORY)
   418|        .url("https://github.com/org/frontend")
   419|        .mountPath("/workspace/frontend")
   420|        .authorizationToken("ghp_your_github_token")
   421|        .build(),
   422|    BetaManagedAgentsGitHubRepositoryResourceParams.builder()
   423|        .type(BetaManagedAgentsGitHubRepositoryResourceParams.Type.GITHUB_REPOSITORY)
   424|        .url("https://github.com/org/backend")
   425|        .mountPath("/workspace/backend")
   426|        .authorizationToken("ghp_your_github_token")
   427|        .build());
   428|```
   429|
   430|Rotating a repository's authorization token:
   431|
   432|```java
   433|import com.anthropic.models.beta.sessions.resources.ResourceUpdateParams;
   434|
   435|var listed = client.beta().sessions().resources().list(session.id());
   436|var repoResourceId = listed.data().get(0).asGitHubRepository().id();
   437|
   438|client.beta().sessions().resources().update(repoResourceId, ResourceUpdateParams.builder()
   439|    .sessionId(session.id())
   440|    .authorizationToken("ghp_your_new_github_token")
   441|    .build());
   442|```
   443|