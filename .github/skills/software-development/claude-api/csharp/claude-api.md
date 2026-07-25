---
name: claude-api-csharp
description: "Claude API — C# reference documentation"
version: 1.0.0
author: Alexa
---
     1|# Claude API — C#
     2|
     3|> **Note:** The C# SDK is the official Anthropic SDK for C#. Tool use is supported via the Messages API. A class-annotation-based tool runner is not available; use raw tool definitions with JSON schema. The SDK also supports Microsoft.Extensions.AI IChatClient integration with function invocation.
     4|
     5|## Installation
     6|
     7|```bash
     8|dotnet add package Anthropic
     9|```
    10|
    11|## Client Initialization
    12|
    13|```csharp
    14|using Anthropic;
    15|
    16|// Default (uses ANTHROPIC_API_KEY env var)
    17|AnthropicClient client = new();
    18|
    19|// Explicit API key (use environment variables — never hardcode keys)
    20|AnthropicClient client = new() {
    21|    ApiKey = Environment.GetEnvironmentVariable("ANTHROPIC_API_KEY")
    22|};
    23|```
    24|
    25|---
    26|
    27|## Basic Message Request
    28|
    29|```csharp
    30|using Anthropic.Models.Messages;
    31|
    32|var parameters = new MessageCreateParams
    33|{
    34|    Model = Model.ClaudeOpus4_6,
    35|    MaxTokens = 16000,
    36|    Messages = [new() { Role = Role.User, Content = "What is the capital of France?" }]
    37|};
    38|var response = await client.Messages.Create(parameters);
    39|
    40|// ContentBlock is a union wrapper. .Value unwraps to the variant object,
    41|// then OfType<T> filters to the type you want. Or use the TryPick* idiom
    42|// shown in the Thinking section below.
    43|foreach (var text in response.Content.Select(b => b.Value).OfType<TextBlock>())
    44|{
    45|    Console.WriteLine(text.Text);
    46|}
    47|```
    48|
    49|---
    50|
    51|## Streaming
    52|
    53|```csharp
    54|using Anthropic.Models.Messages;
    55|
    56|var parameters = new MessageCreateParams
    57|{
    58|    Model = Model.ClaudeOpus4_6,
    59|    MaxTokens = 64000,
    60|    Messages = [new() { Role = Role.User, Content = "Write a haiku" }]
    61|};
    62|
    63|await foreach (RawMessageStreamEvent streamEvent in client.Messages.CreateStreaming(parameters))
    64|{
    65|    if (streamEvent.TryPickContentBlockDelta(out var delta) &&
    66|        delta.Delta.TryPickText(out var text))
    67|    {
    68|        Console.Write(text.Text);
    69|    }
    70|}
    71|```
    72|
    73|**`RawMessageStreamEvent` TryPick methods** (naming drops the `Message`/`Raw` prefix): `TryPickStart`, `TryPickDelta`, `TryPickStop`, `TryPickContentBlockStart`, `TryPickContentBlockDelta`, `TryPickContentBlockStop`. There is no `TryPickMessageStop` — use `TryPickStop`.
    74|
    75|---
    76|
    77|## Thinking
    78|
    79|**Adaptive thinking is the recommended mode for Claude 4.6+ models.** Claude decides dynamically when and how much to think.
    80|
    81|```csharp
    82|using Anthropic.Models.Messages;
    83|
    84|var response = await client.Messages.Create(new MessageCreateParams
    85|{
    86|    Model = Model.ClaudeOpus4_6,
    87|    MaxTokens = 16000,
    88|    // ThinkingConfigParam? implicitly converts from the concrete variant classes —
    89|    // no wrapper needed.
    90|    Thinking = new ThinkingConfigAdaptive(),
    91|    Messages =
    92|    [
    93|        new() { Role = Role.User, Content = "Solve: 27 * 453" },
    94|    ],
    95|});
    96|
    97|// ThinkingBlock(s) precede TextBlock in Content. TryPick* narrows the union.
    98|foreach (var block in response.Content)
    99|{
   100|    if (block.TryPickThinking(out ThinkingBlock? t))
   101|    {
   102|        Console.WriteLine($"[thinking] {t.Thinking}");
   103|    }
   104|    else if (block.TryPickText(out TextBlock? text))
   105|    {
   106|        Console.WriteLine(text.Text);
   107|    }
   108|}
   109|```
   110|
   111|> **Deprecated:** `new ThinkingConfigEnabled { BudgetTokens = N }` (fixed-budget extended thinking) still works on Claude 4.6 but is deprecated. Use adaptive thinking above.
   112|
   113|Alternative to `TryPick*`: `.Select(b => b.Value).OfType<ThinkingBlock>()` (same LINQ pattern as the Basic Message example).
   114|
   115|---
   116|
   117|## Tool Use
   118|
   119|### Defining a tool
   120|
   121|`Tool` (NOT `ToolParam`) with an `InputSchema` record. `InputSchema.Type` is auto-set to `"object"` by the constructor — don't set it. `ToolUnion` has an implicit conversion from `Tool`, triggered by the collection expression `[...]`.
   122|
   123|```csharp
   124|using System.Text.Json;
   125|using Anthropic.Models.Messages;
   126|
   127|var parameters = new MessageCreateParams
   128|{
   129|    Model = Model.ClaudeSonnet4_6,
   130|    MaxTokens = 16000,
   131|    Tools = [
   132|        new Tool {
   133|            Name = "get_weather",
   134|            Description = "Get the current weather in a given location",
   135|            InputSchema = new() {
   136|                Properties = new Dictionary<string, JsonElement> {
   137|                    ["location"] = JsonSerializer.SerializeToElement(
   138|                        new { type = "string", description = "City name" }),
   139|                },
   140|                Required = ["location"],
   141|            },
   142|        },
   143|    ],
   144|    Messages = [new() { Role = Role.User, Content = "Weather in Paris?" }],
   145|};
   146|```
   147|
   148|Derived from `anthropic-sdk-csharp/src/Anthropic/Models/Messages/Tool.cs` and `ToolUnion.cs:799` (implicit conversion).
   149|
   150|See [shared tool use concepts](../shared/tool-use-concepts.md) for the loop pattern.
   151|
   152|### Converting response content to the follow-up assistant message
   153|
   154|When echoing Claude's response back in the assistant turn, **there is no `.ToParam()` helper** — manually reconstruct each `ContentBlock` variant as its `*Param` counterpart. Do NOT use `new ContentBlockParam(block.Json)`: it compiles and serializes, but `.Value` stays `null` so `TryPick*`/`Validate()` fail (degraded JSON pass-through, not the typed path).
   155|
   156|```csharp
   157|using Anthropic.Models.Messages;
   158|
   159|Message response = await client.Messages.Create(parameters);
   160|
   161|// No .ToParam() — reconstruct per variant. Implicit conversions from each
   162|// *Param type to ContentBlockParam mean no explicit wrapper.
   163|List<ContentBlockParam> assistantContent = [];
   164|List<ContentBlockParam> toolResults = [];
   165|foreach (ContentBlock block in response.Content)
   166|{
   167|    if (block.TryPickText(out TextBlock? text))
   168|    {
   169|        assistantContent.Add(new TextBlockParam { Text = text.Text });
   170|    }
   171|    else if (block.TryPickThinking(out ThinkingBlock? thinking))
   172|    {
   173|        // Signature MUST be preserved — the API rejects tampering
   174|        assistantContent.Add(new ThinkingBlockParam
   175|        {
   176|            Thinking = thinking.Thinking,
   177|            Signature = thinking.Signature,
   178|        });
   179|    }
   180|    else if (block.TryPickRedactedThinking(out RedactedThinkingBlock? redacted))
   181|    {
   182|        assistantContent.Add(new RedactedThinkingBlockParam { Data = redacted.Data });
   183|    }
   184|    else if (block.TryPickToolUse(out ToolUseBlock? toolUse))
   185|    {
   186|        // ToolUseBlock has required Caller; ToolUseBlockParam.Caller is optional — don't copy it
   187|        assistantContent.Add(new ToolUseBlockParam
   188|        {
   189|            ID = toolUse.ID,
   190|            Name = toolUse.Name,
   191|            Input = toolUse.Input,
   192|        });
   193|        // Execute the tool; collect ONE result per tool_use block — the API
   194|        // rejects the follow-up if any tool_use ID lacks a matching tool_result.
   195|        string result = ExecuteYourTool(toolUse.Name, toolUse.Input);
   196|        toolResults.Add(new ToolResultBlockParam
   197|        {
   198|            ToolUseID = toolUse.ID,
   199|            Content = result,
   200|        });
   201|    }
   202|}
   203|
   204|// Follow-up: prior messages + assistant echo + user tool_result(s)
   205|List<MessageParam> followUpMessages =
   206|[
   207|    .. parameters.Messages,
   208|    new() { Role = Role.Assistant, Content = assistantContent },
   209|    new() { Role = Role.User, Content = toolResults },
   210|];
   211|```
   212|
   213|`ToolResultBlockParam` has no tuple constructor — use the object initializer. `Content` is a string-or-list union; a plain `string` implicitly converts.
   214|
   215|---
   216|
   217|## Context Editing / Compaction (Beta)
   218|
   219|**Beta-namespace prefix is inconsistent** (source-verified against `src/Anthropic/Models/Beta/Messages/*.cs` @ 12.9.0). No prefix: `MessageCreateParams`, `MessageCountTokensParams`, `Role`. **Everything else has the `Beta` prefix**: `BetaMessageParam`, `BetaMessage`, `BetaContentBlock`, `BetaToolUseBlock`, all block param types. The unprefixed `Role` WILL collide with `Anthropic.Models.Messages.Role` if you import both namespaces (CS0104). Safest: import only Beta; if mixing, alias the beta `Role`:
   220|
   221|```csharp
   222|using Anthropic.Models.Beta.Messages;
   223|using NonBeta = Anthropic.Models.Messages;  // only if you also need non-beta types
   224|// Now: MessageCreateParams, BetaMessageParam, Role (beta's), NonBeta.Role (if needed)
   225|```
   226|
   227|`BetaMessage.Content` is `IReadOnlyList<BetaContentBlock>` — a 15-variant discriminated union. Narrow with `TryPick*`. **Response `BetaContentBlock` is NOT assignable to param `BetaContentBlockParam`** — there's no `.ToParam()` in C#. Round-trip by converting each block:
   228|
   229|```csharp
   230|using Anthropic.Models.Beta.Messages;
   231|
   232|var betaParams = new MessageCreateParams   // no Beta prefix — one of only 2 unprefixed
   233|{
   234|    Model = Model.ClaudeOpus4_6,
   235|    MaxTokens = 16000,
   236|    Betas = ["compact-2026-01-12"],
   237|    ContextManagement = new BetaContextManagementConfig
   238|    {
   239|        Edits = [new BetaCompact20260112Edit()],
   240|    },
   241|    Messages = messages,
   242|};
   243|BetaMessage resp = await client.Beta.Messages.Create(betaParams);
   244|
   245|foreach (BetaContentBlock block in resp.Content)
   246|{
   247|    if (block.TryPickCompaction(out BetaCompactionBlock? compaction))
   248|    {
   249|        // Content is nullable — compaction can fail server-side
   250|        Console.WriteLine($"compaction summary: {compaction.Content}");
   251|    }
   252|}
   253|
   254|// Context-edit metadata lives on a separate nullable field
   255|if (resp.ContextManagement is { } ctx)
   256|{
   257|    foreach (var edit in ctx.AppliedEdits)
   258|        Console.WriteLine($"cleared {edit.ClearedInputTokens} tokens");
   259|}
   260|
   261|// ROUND-TRIP: BetaMessageParam.Content is BetaMessageParamContent (a string|list
   262|// union). It implicit-converts from List<BetaContentBlockParam>, NOT from the
   263|// response's IReadOnlyList<BetaContentBlock>. Convert each block:
   264|List<BetaContentBlockParam> paramBlocks = [];
   265|foreach (var b in resp.Content)
   266|{
   267|    if (b.TryPickText(out var t)) paramBlocks.Add(new BetaTextBlockParam { Text = t.Text });
   268|    else if (b.TryPickCompaction(out var c)) paramBlocks.Add(new BetaCompactionBlockParam { Content = c.Content });
   269|    // ... other variants as needed
   270|}
   271|messages.Add(new BetaMessageParam { Role = Role.Assistant, Content = paramBlocks });
   272|```
   273|
   274|All 15 `BetaContentBlock.TryPick*` variants: `Text`, `Thinking`, `RedactedThinking`, `ToolUse`, `ServerToolUse`, `WebSearchToolResult`, `WebFetchToolResult`, `CodeExecutionToolResult`, `BashCodeExecutionToolResult`, `TextEditorCodeExecutionToolResult`, `ToolSearchToolResult`, `McpToolUse`, `McpToolResult`, `ContainerUpload`, `Compaction`.
   275|
   276|**`BetaToolUseBlock.Input` is `IReadOnlyDictionary<string, JsonElement>`** — index by key then call the `JsonElement` extractor:
   277|
   278|```csharp
   279|if (block.TryPickToolUse(out BetaToolUseBlock? tu))
   280|{
   281|    int a = tu.Input["a"].GetInt32();
   282|    string s = tu.Input["name"].GetString()!;
   283|}
   284|```
   285|
   286|---
   287|
   288|## Effort Parameter
   289|
   290|Effort is nested under `OutputConfig`, NOT a top-level property. `ApiEnum<string, Effort>` has an implicit conversion from the enum, so assign `Effort.High` directly.
   291|
   292|```csharp
   293|OutputConfig = new OutputConfig { Effort = Effort.High },
   294|```
   295|
   296|Values: `Effort.Low`, `Effort.Medium`, `Effort.High`, `Effort.Max`. Combine with `Thinking = new ThinkingConfigAdaptive()` for cost-quality control.
   297|
   298|---
   299|
   300|## Prompt Caching
   301|
   302|`System` takes `MessageCreateParamsSystem?` — a union of `string` or `List<TextBlockParam>`. There is no `SystemTextBlockParam`; use plain `TextBlockParam`. The implicit conversion needs the concrete `List<TextBlockParam>` type (array literals won't convert). For placement patterns and the silent-invalidator audit checklist, see `shared/prompt-caching.md`.
   303|
   304|```csharp
   305|System = new List<TextBlockParam> {
   306|    new() {
   307|        Text = longSystemPrompt,
   308|        CacheControl = new CacheControlEphemeral(),  // auto-sets Type = "ephemeral"
   309|    },
   310|},
   311|```
   312|
   313|Optional `Ttl` on `CacheControlEphemeral`: `new() { Ttl = Ttl.Ttl1h }` or `Ttl.Ttl5m`. `CacheControl` also exists on `Tool.CacheControl` and top-level `MessageCreateParams.CacheControl`.
   314|
   315|Verify hits via `response.Usage.CacheCreationInputTokens` / `response.Usage.CacheReadInputTokens`.
   316|
   317|---
   318|
   319|## Token Counting
   320|
   321|```csharp
   322|MessageTokensCount result = await client.Messages.CountTokens(new MessageCountTokensParams {
   323|    Model = Model.ClaudeOpus4_6,
   324|    Messages = [new() { Role = Role.User, Content = "Hello" }],
   325|});
   326|long tokens = result.InputTokens;
   327|```
   328|
   329|`MessageCountTokensParams.Tools` uses a different union type (`MessageCountTokensTool`) than `MessageCreateParams.Tools` (`ToolUnion`) — if you're passing tools, the compiler will tell you when it matters.
   330|
   331|---
   332|
   333|## Structured Output
   334|
   335|```csharp
   336|OutputConfig = new OutputConfig {
   337|    Format = new JsonOutputFormat {
   338|        Schema = new Dictionary<string, JsonElement> {
   339|            ["type"] = JsonSerializer.SerializeToElement("object"),
   340|            ["properties"] = JsonSerializer.SerializeToElement(
   341|                new { name = new { type = "string" } }),
   342|            ["required"] = JsonSerializer.SerializeToElement(new[] { "name" }),
   343|        },
   344|    },
   345|},
   346|```
   347|
   348|`JsonOutputFormat.Type` is auto-set to `"json_schema"` by the constructor. `Schema` is `required`.
   349|
   350|---
   351|
   352|## PDF / Document Input
   353|
   354|`DocumentBlockParam` takes a `DocumentBlockParamSource` union: `Base64PdfSource` / `UrlPdfSource` / `PlainTextSource` / `ContentBlockSource`. `Base64PdfSource` auto-sets `MediaType = "application/pdf"` and `Type = "base64"`.
   355|
   356|```csharp
   357|new MessageParam {
   358|    Role = Role.User,
   359|    Content = new List<ContentBlockParam> {
   360|        new DocumentBlockParam { Source = new Base64PdfSource { Data = base64String } },
   361|        new TextBlockParam { Text = "Summarize this PDF" },
   362|    },
   363|}
   364|```
   365|
   366|---
   367|
   368|## Server-Side Tools
   369|
   370|Web search, bash, text editor, and code execution are built-in server tools. Type names are version-suffixed; constructors auto-set `name`/`type`. All implicit-convert to `ToolUnion`.
   371|
   372|```csharp
   373|Tools = [
   374|    new WebSearchTool20260209(),
   375|    new ToolBash20250124(),
   376|    new ToolTextEditor20250728(),
   377|    new CodeExecutionTool20260120(),
   378|],
   379|```
   380|
   381|Also available: `WebFetchTool20260209`, `MemoryTool20250818`. `WebSearchTool20260209` optionals: `AllowedDomains`, `BlockedDomains`, `MaxUses`, `UserLocation`.
   382|
   383|---
   384|
   385|## Files API (Beta)
   386|
   387|Files live under `client.Beta.Files` (namespace `Anthropic.Models.Beta.Files`). `BinaryContent` implicit-converts from `Stream` and `byte[]`.
   388|
   389|```csharp
   390|using Anthropic.Models.Beta.Files;
   391|using Anthropic.Models.Beta.Messages;
   392|
   393|FileMetadata meta = await client.Beta.Files.Upload(
   394|    new FileUploadParams { File = File.OpenRead("doc.pdf") });
   395|
   396|// Referencing the uploaded file requires Beta message types:
   397|new BetaRequestDocumentBlock {
   398|    Source = new BetaFileDocumentSource { FileID = meta.ID },
   399|}
   400|```
   401|
   402|The non-beta `DocumentBlockParamSource` union has no file-ID variant — file references need `client.Beta.Messages.Create()`.
   403|