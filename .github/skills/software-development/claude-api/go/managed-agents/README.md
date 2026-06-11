---
name: managed-agents-managed-agents
description: "Reference: managed-agents-managed-agents"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Go
     2|
     3|> **Bindings not shown here:** This README covers the most common managed-agents flows for Go. If you need a class, method, namespace, field, or behavior that isn't shown, WebFetch the Go SDK repo **or the relevant docs page** from `shared/live-sources.md` rather than guess. Do not extrapolate from cURL shapes or another language's SDK.
     4|
     5|> **Agents are persistent — create once, reference by ID.** Store the agent ID returned by `agents.New` and pass it to every subsequent `sessions.New`; do not call `agents.New` in the request path. The Anthropic CLI is one convenient way to create agents and environments from version-controlled YAML — its URL is in `shared/live-sources.md`. The examples below show in-code creation for completeness; in production the create call belongs in setup, not in the request path.
     6|
     7|## Installation
     8|
     9|```bash
    10|go get github.com/anthropics/anthropic-sdk-go
    11|```
    12|
    13|## Client Initialization
    14|
    15|```go
    16|import (
    17|    "context"
    18|
    19|    "github.com/anthropics/anthropic-sdk-go"
    20|    "github.com/anthropics/anthropic-sdk-go/option"
    21|)
    22|
    23|// Default (uses ANTHROPIC_API_KEY env var)
    24|client := anthropic.NewClient()
    25|
    26|// Explicit API key
    27|client := anthropic.NewClient(
    28|    option.WithAPIKey("your-api-key"),
    29|)
    30|
    31|ctx := context.Background()
    32|```
    33|
    34|---
    35|
    36|## Create an Environment
    37|
    38|```go
    39|environment, err := client.Beta.Environments.New(ctx, anthropic.BetaEnvironmentNewParams{
    40|    Name: "my-dev-env",
    41|    Config: anthropic.BetaCloudConfigParams{
    42|        Networking: anthropic.BetaCloudConfigParamsNetworkingUnion{
    43|            OfUnrestricted: &anthropic.UnrestrictedNetworkParam{},
    44|        },
    45|    },
    46|})
    47|if err != nil {
    48|    panic(err)
    49|}
    50|fmt.Println(environment.ID) // env_...
    51|```
    52|
    53|---
    54|
    55|## Create an Agent (required first step)
    56|
    57|> ⚠️ **There is no inline agent config.** `Model`/`System`/`Tools` live on the agent object, not the session. Always start with `Beta.Agents.New()` — the session only takes `Agent: anthropic.BetaSessionNewParamsAgentUnion{OfString: anthropic.String(agent.ID)}` (or the typed `OfBetaManagedAgentsAgents` variant when you need a specific version).
    58|
    59|### Minimal
    60|
    61|```go
    62|// 1. Create the agent (reusable, versioned)
    63|agent, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
    64|    Name: "Coding Assistant",
    65|    Model: anthropic.BetaManagedAgentsModelConfigParams{
    66|        ID:   "claude-opus-4-7",
    67|        Type: anthropic.BetaManagedAgentsModelConfigParamsTypeModelConfig,
    68|    },
    69|    System: anthropic.String("You are a helpful coding assistant."),
    70|    Tools: []anthropic.BetaAgentNewParamsToolUnion{{
    71|        OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
    72|            Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
    73|        },
    74|    }},
    75|})
    76|if err != nil {
    77|    panic(err)
    78|}
    79|
    80|// 2. Start a session
    81|session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
    82|    Agent: anthropic.BetaSessionNewParamsAgentUnion{
    83|        OfBetaManagedAgentsAgents: &anthropic.BetaManagedAgentsAgentParams{
    84|            Type:    anthropic.BetaManagedAgentsAgentParamsTypeAgent,
    85|            ID:      agent.ID,
    86|            Version: anthropic.Int(agent.Version),
    87|        },
    88|    },
    89|    EnvironmentID: environment.ID,
    90|    Title:         anthropic.String("Quickstart session"),
    91|})
    92|if err != nil {
    93|    panic(err)
    94|}
    95|fmt.Printf("Session ID: %s, status: %s\n", session.ID, session.Status)
    96|```
    97|
    98|### Updating an Agent
    99|
   100|Updates create new versions; the agent object is immutable per version.
   101|
   102|```go
   103|updatedAgent, err := client.Beta.Agents.Update(ctx, agent.ID, anthropic.BetaAgentUpdateParams{
   104|    Version: agent.Version,
   105|    System:  anthropic.String("You are a helpful coding agent. Always write tests."),
   106|})
   107|if err != nil {
   108|    panic(err)
   109|}
   110|fmt.Printf("New version: %d\n", updatedAgent.Version)
   111|
   112|// List all versions
   113|iter := client.Beta.Agents.Versions.ListAutoPaging(ctx, agent.ID, anthropic.BetaAgentVersionListParams{})
   114|for iter.Next() {
   115|    version := iter.Current()
   116|    fmt.Printf("Version %d: %s\n", version.Version, version.UpdatedAt.Format(time.RFC3339))
   117|}
   118|if err := iter.Err(); err != nil {
   119|    panic(err)
   120|}
   121|
   122|// Archive the agent
   123|_, err = client.Beta.Agents.Archive(ctx, agent.ID, anthropic.BetaAgentArchiveParams{})
   124|if err != nil {
   125|    panic(err)
   126|}
   127|```
   128|
   129|---
   130|
   131|## Send a User Message
   132|
   133|```go
   134|_, err = client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
   135|    Events: []anthropic.SendEventsParamsUnion{{
   136|        OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
   137|            Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
   138|            Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{{
   139|                OfText: &anthropic.BetaManagedAgentsTextBlockParam{
   140|                    Type: anthropic.BetaManagedAgentsTextBlockTypeText,
   141|                    Text: "Review the auth module",
   142|                },
   143|            }},
   144|        },
   145|    }},
   146|})
   147|if err != nil {
   148|    panic(err)
   149|}
   150|```
   151|
   152|> 💡 **Stream-first:** Open the stream _before_ (or concurrently with) sending the message. The stream only delivers events that occur after it opens — stream-after-send means early events arrive buffered in one batch. See [Steering Patterns](../../shared/managed-agents-events.md#steering-patterns).
   153|
   154|---
   155|
   156|## Stream Events (SSE)
   157|
   158|```go
   159|// Open the stream first, then send the user message
   160|stream := client.Beta.Sessions.Events.StreamEvents(ctx, session.ID, anthropic.BetaSessionEventStreamParams{})
   161|defer stream.Close()
   162|
   163|if _, err := client.Beta.Sessions.Events.Send(ctx, session.ID, anthropic.BetaSessionEventSendParams{
   164|    Events: []anthropic.SendEventsParamsUnion{{
   165|        OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
   166|            Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
   167|            Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{{
   168|                OfText: &anthropic.BetaManagedAgentsTextBlockParam{
   169|                    Type: anthropic.BetaManagedAgentsTextBlockTypeText,
   170|                    Text: "Summarize the repo README",
   171|                },
   172|            }},
   173|        },
   174|    }},
   175|}); err != nil {
   176|    panic(err)
   177|}
   178|
   179|events:
   180|for stream.Next() {
   181|    switch event := stream.Current().AsAny().(type) {
   182|    case anthropic.BetaManagedAgentsAgentMessageEvent:
   183|        for _, block := range event.Content {
   184|            fmt.Print(block.Text)
   185|        }
   186|    case anthropic.BetaManagedAgentsAgentToolUseEvent:
   187|        fmt.Printf("\n[Using tool: %s]\n", event.Name)
   188|    case anthropic.BetaManagedAgentsSessionStatusIdleEvent:
   189|        break events
   190|    case anthropic.BetaManagedAgentsSessionErrorEvent:
   191|        fmt.Printf("\n[Error: %s]\n", event.Error.Message)
   192|        break events
   193|    }
   194|}
   195|if err := stream.Err(); err != nil {
   196|    panic(err)
   197|}
   198|```
   199|
   200|### Reconnecting and Tailing
   201|
   202|When reconnecting mid-session, list past events first to dedupe, then tail live events:
   203|
   204|```go
   205|stream := client.Beta.Sessions.Events.StreamEvents(ctx, session.ID, anthropic.BetaSessionEventStreamParams{})
   206|defer stream.Close()
   207|
   208|// Stream is open and buffering. List history before tailing live.
   209|seenEventIDs := map[string]struct{}{}
   210|history := client.Beta.Sessions.Events.ListAutoPaging(ctx, session.ID, anthropic.BetaSessionEventListParams{})
   211|for history.Next() {
   212|    seenEventIDs[history.Current().ID] = struct{}{}
   213|}
   214|if err := history.Err(); err != nil {
   215|    panic(err)
   216|}
   217|
   218|// Tail live events, skipping anything already seen
   219|tail:
   220|for stream.Next() {
   221|    event := stream.Current()
   222|    if _, seen := seenEventIDs[event.ID]; seen {
   223|        continue
   224|    }
   225|    seenEventIDs[event.ID] = struct{}{}
   226|    switch event := event.AsAny().(type) {
   227|    case anthropic.BetaManagedAgentsAgentMessageEvent:
   228|        for _, block := range event.Content {
   229|            fmt.Print(block.Text)
   230|        }
   231|    case anthropic.BetaManagedAgentsSessionStatusIdleEvent:
   232|        break tail
   233|    }
   234|}
   235|if err := stream.Err(); err != nil {
   236|    panic(err)
   237|}
   238|```
   239|
   240|---
   241|
   242|## Provide Custom Tool Result
   243|
   244|> ℹ️ The Go managed-agents bindings for `user.custom_tool_result` are not yet documented in this skill or in the apps source examples. Refer to `shared/managed-agents-events.md` for the wire format and the `github.com/anthropics/anthropic-sdk-go` repository for the corresponding Go params types.
   245|
   246|---
   247|
   248|## Poll Events
   249|
   250|```go
   251|// Auto-paginating iterator
   252|iter := client.Beta.Sessions.Events.ListAutoPaging(ctx, session.ID, anthropic.BetaSessionEventListParams{})
   253|for iter.Next() {
   254|    event := iter.Current()
   255|    fmt.Printf("%s: %s\n", event.Type, event.ID)
   256|}
   257|if err := iter.Err(); err != nil {
   258|    panic(err)
   259|}
   260|```
   261|
   262|---
   263|
   264|## Upload a File
   265|
   266|```go
   267|csvFile, err := os.Open("data.csv")
   268|if err != nil {
   269|    panic(err)
   270|}
   271|defer csvFile.Close()
   272|
   273|file, err := client.Beta.Files.Upload(ctx, anthropic.BetaFileUploadParams{
   274|    File: csvFile,
   275|})
   276|if err != nil {
   277|    panic(err)
   278|}
   279|fmt.Printf("File ID: %s\n", file.ID)
   280|
   281|// Mount in a session
   282|session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
   283|    Agent: anthropic.BetaSessionNewParamsAgentUnion{
   284|        OfString: anthropic.String(agent.ID),
   285|    },
   286|    EnvironmentID: environment.ID,
   287|    Resources: []anthropic.BetaSessionNewParamsResourceUnion{{
   288|        OfFile: &anthropic.BetaManagedAgentsFileResourceParams{
   289|            Type:      anthropic.BetaManagedAgentsFileResourceParamsTypeFile,
   290|            FileID:    file.ID,
   291|            MountPath: anthropic.String("/workspace/data.csv"),
   292|        },
   293|    }},
   294|})
   295|if err != nil {
   296|    panic(err)
   297|}
   298|```
   299|
   300|### Add and Manage Resources on an Existing Session
   301|
   302|```go
   303|// Attach an additional file to an open session
   304|resource, err := client.Beta.Sessions.Resources.Add(ctx, session.ID, anthropic.BetaSessionResourceAddParams{
   305|    BetaManagedAgentsFileResourceParams: anthropic.BetaManagedAgentsFileResourceParams{
   306|        Type:   anthropic.BetaManagedAgentsFileResourceParamsTypeFile,
   307|        FileID: file.ID,
   308|    },
   309|})
   310|if err != nil {
   311|    panic(err)
   312|}
   313|fmt.Println(resource.ID) // "sesrsc_01ABC..."
   314|
   315|// List resources on the session
   316|listed, err := client.Beta.Sessions.Resources.List(ctx, session.ID, anthropic.BetaSessionResourceListParams{})
   317|if err != nil {
   318|    panic(err)
   319|}
   320|for _, entry := range listed.Data {
   321|    fmt.Println(entry.ID, entry.Type)
   322|}
   323|
   324|// Detach a resource
   325|if _, err := client.Beta.Sessions.Resources.Delete(ctx, resource.ID, anthropic.BetaSessionResourceDeleteParams{
   326|    SessionID: session.ID,
   327|}); err != nil {
   328|    panic(err)
   329|}
   330|```
   331|
   332|---
   333|
   334|## List and Download Session Files
   335|
   336|> ℹ️ Listing and downloading files an agent wrote during a session is not yet documented for Go in this skill or in the apps source examples. See `shared/managed-agents-events.md` and the `github.com/anthropics/anthropic-sdk-go` repository for the `Beta.Files.List` and `Beta.Files.Download` Go params types.
   337|
   338|---
   339|
   340|## Session Management
   341|
   342|```go
   343|// List environments
   344|environments, err := client.Beta.Environments.List(ctx, anthropic.BetaEnvironmentListParams{})
   345|if err != nil {
   346|    panic(err)
   347|}
   348|
   349|// Retrieve a specific environment
   350|env, err := client.Beta.Environments.Get(ctx, environment.ID, anthropic.BetaEnvironmentGetParams{})
   351|if err != nil {
   352|    panic(err)
   353|}
   354|
   355|// Archive an environment (read-only, existing sessions continue)
   356|_, err = client.Beta.Environments.Archive(ctx, environment.ID, anthropic.BetaEnvironmentArchiveParams{})
   357|if err != nil {
   358|    panic(err)
   359|}
   360|
   361|// Delete an environment (only if no sessions reference it)
   362|_, err = client.Beta.Environments.Delete(ctx, environment.ID, anthropic.BetaEnvironmentDeleteParams{})
   363|if err != nil {
   364|    panic(err)
   365|}
   366|
   367|// Delete a session
   368|_, err = client.Beta.Sessions.Delete(ctx, session.ID, anthropic.BetaSessionDeleteParams{})
   369|if err != nil {
   370|    panic(err)
   371|}
   372|```
   373|
   374|---
   375|
   376|## MCP Server Integration
   377|
   378|```go
   379|// Agent declares MCP server (no auth here — auth goes in a vault)
   380|agent, err := client.Beta.Agents.New(ctx, anthropic.BetaAgentNewParams{
   381|    Name: "GitHub Assistant",
   382|    Model: anthropic.BetaManagedAgentsModelConfigParams{
   383|        ID:   "claude-opus-4-7",
   384|        Type: anthropic.BetaManagedAgentsModelConfigParamsTypeModelConfig,
   385|    },
   386|    MCPServers: []anthropic.BetaManagedAgentsUrlmcpServerParams{{
   387|        Type: anthropic.BetaManagedAgentsUrlmcpServerParamsTypeURL,
   388|        Name: "github",
   389|        URL:  "https://api.githubcopilot.com/mcp/",
   390|    }},
   391|    Tools: []anthropic.BetaAgentNewParamsToolUnion{
   392|        {
   393|            OfAgentToolset20260401: &anthropic.BetaManagedAgentsAgentToolset20260401Params{
   394|                Type: anthropic.BetaManagedAgentsAgentToolset20260401ParamsTypeAgentToolset20260401,
   395|            },
   396|        },
   397|        {
   398|            OfMCPToolset: &anthropic.BetaManagedAgentsMCPToolsetParams{
   399|                Type:          anthropic.BetaManagedAgentsMCPToolsetParamsTypeMCPToolset,
   400|                MCPServerName: "github",
   401|            },
   402|        },
   403|    },
   404|})
   405|if err != nil {
   406|    panic(err)
   407|}
   408|
   409|// Session attaches vault(s) containing credentials for those MCP server URLs
   410|session, err := client.Beta.Sessions.New(ctx, anthropic.BetaSessionNewParams{
   411|    Agent: anthropic.BetaSessionNewParamsAgentUnion{
   412|        OfBetaManagedAgentsAgents: &anthropic.BetaManagedAgentsAgentParams{
   413|            Type:    anthropic.BetaManagedAgentsAgentParamsTypeAgent,
   414|            ID:      agent.ID,
   415|            Version: anthropic.Int(agent.Version),
   416|        },
   417|    },
   418|    EnvironmentID: environment.ID,
   419|    VaultIDs:      []string{vault.ID},
   420|})
   421|if err != nil {
   422|    panic(err)
   423|}
   424|```
   425|
   426|See `shared/managed-agents-tools.md` §Vaults for creating vaults and adding credentials.
   427|
   428|---
   429|
   430|## Vaults
   431|
   432|```go
   433|// Create a vault
   434|vault, err := client.Beta.Vaults.New(ctx, anthropic.BetaVaultNewParams{
   435|    DisplayName: "Alice",
   436|    Metadata:    map[string]string{"external_user_id": "usr_abc123"},
   437|})
   438|if err != nil {
   439|    panic(err)
   440|}
   441|
   442|// Add an OAuth credential
   443|credential, err := client.Beta.Vaults.Credentials.New(ctx, vault.ID, anthropic.BetaVaultCredentialNewParams{
   444|    DisplayName: anthropic.String("Alice's Slack"),
   445|    Auth: anthropic.BetaVaultCredentialNewParamsAuthUnion{
   446|        OfMCPOAuth: &anthropic.BetaManagedAgentsMCPOAuthCreateParams{
   447|            Type:         anthropic.BetaManagedAgentsMCPOAuthCreateParamsTypeMCPOAuth,
   448|            MCPServerURL: "https://mcp.slack.com/mcp",
   449|            AccessToken:  "xoxp-...",
   450|            ExpiresAt:    anthropic.Time(time.Date(2026, time.April, 15, 0, 0, 0, 0, time.UTC)),
   451|            Refresh: anthropic.BetaManagedAgentsMCPOAuthRefreshParams{
   452|                TokenEndpoint: "https://slack.com/api/oauth.v2.access",
   453|                ClientID:      "1234567890.0987654321",
   454|                Scope:         anthropic.String("channels:read chat:write"),
   455|                RefreshToken:  "xoxe-1-...",
   456|                TokenEndpointAuth: anthropic.BetaManagedAgentsMCPOAuthRefreshParamsTokenEndpointAuthUnion{
   457|                    OfClientSecretPost: &anthropic.BetaManagedAgentsTokenEndpointAuthPostParam{
   458|                        Type:         anthropic.BetaManagedAgentsTokenEndpointAuthPostParamTypeClientSecretPost,
   459|                        ClientSecret: "abc123...",
   460|                    },
   461|                },
   462|            },
   463|        },
   464|    },
   465|})
   466|if err != nil {
   467|    panic(err)
   468|}
   469|
   470|// Rotate the credential (e.g., after a token refresh)
   471|_, err = client.Beta.Vaults.Credentials.Update(ctx, credential.ID, anthropic.BetaVaultCredentialUpdateParams{
   472|    VaultID: vault.ID,
   473|    Auth: anthropic.BetaVaultCredentialUpdateParamsAuthUnion{
   474|        OfMCPOAuth: &anthropic.BetaManagedAgentsMCPOAuthUpdateParams{
   475|            Type:        anthropic.BetaManagedAgentsMCPOAuthUpdateParamsTypeMCPOAuth,
   476|            AccessToken: anthropic.String("xoxp-new-..."),
   477|            ExpiresAt:   anthropic.Time(time.Date(2026, time.May, 15, 0, 0, 0, 0, time.UTC)),
   478|            Refresh: anthropic.BetaManagedAgentsMCPOAuthRefreshUpdateParams{
   479|                RefreshToken: anthropic.String("xoxe-1-new-..."),
   480|            },
   481|        },
   482|    },
   483|})
   484|if err != nil {
   485|    panic(err)
   486|}
   487|
   488|// Archive a vault
   489|_, err = client.Beta.Vaults.Archive(ctx, vault.ID, anthropic.BetaVaultArchiveParams{})
   490|if err != nil {
   491|    panic(err)
   492|}
   493|```
   494|
   495|---
   496|
   497|## GitHub Repository Integration
   498|
   499|Mount a GitHub repository as a session resource (a vault holds the GitHub MCP credential):
   500|
   501|