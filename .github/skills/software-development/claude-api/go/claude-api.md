---
name: claude-api-go
description: "Claude API — Go reference documentation"
version: 1.0.0
author: Alexa
---
     1|# Claude API — Go
     2|
     3|> **Note:** The Go SDK supports the Claude API and beta tool use with `BetaToolRunner`. Agent SDK is not yet available for Go.
     4|
     5|## Installation
     6|
     7|```bash
     8|go get github.com/anthropics/anthropic-sdk-go
     9|```
    10|
    11|## Client Initialization
    12|
    13|```go
    14|import (
    15|    "github.com/anthropics/anthropic-sdk-go"
    16|    "github.com/anthropics/anthropic-sdk-go/option"
    17|)
    18|
    19|// Default (uses ANTHROPIC_API_KEY env var)
    20|client := anthropic.NewClient()
    21|
    22|// Explicit API key
    23|client := anthropic.NewClient(
    24|    option.WithAPIKey("your-api-key"),
    25|)
    26|```
    27|
    28|---
    29|
    30|## Basic Message Request
    31|
    32|```go
    33|response, err := client.Messages.New(context.Background(), anthropic.MessageNewParams{
    34|    Model:     anthropic.ModelClaudeOpus4_6,
    35|    MaxTokens: 16000,
    36|    Messages: []anthropic.MessageParam{
    37|        anthropic.NewUserMessage(anthropic.NewTextBlock("What is the capital of France?")),
    38|    },
    39|})
    40|if err != nil {
    41|    log.Fatal(err)
    42|}
    43|for _, block := range response.Content {
    44|    switch variant := block.AsAny().(type) {
    45|    case anthropic.TextBlock:
    46|        fmt.Println(variant.Text)
    47|    }
    48|}
    49|```
    50|
    51|---
    52|
    53|## Streaming
    54|
    55|```go
    56|stream := client.Messages.NewStreaming(context.Background(), anthropic.MessageNewParams{
    57|    Model:     anthropic.ModelClaudeOpus4_6,
    58|    MaxTokens: 64000,
    59|    Messages: []anthropic.MessageParam{
    60|        anthropic.NewUserMessage(anthropic.NewTextBlock("Write a haiku")),
    61|    },
    62|})
    63|
    64|for stream.Next() {
    65|    event := stream.Current()
    66|    switch eventVariant := event.AsAny().(type) {
    67|    case anthropic.ContentBlockDeltaEvent:
    68|        switch deltaVariant := eventVariant.Delta.AsAny().(type) {
    69|        case anthropic.TextDelta:
    70|            fmt.Print(deltaVariant.Text)
    71|        }
    72|    }
    73|}
    74|if err := stream.Err(); err != nil {
    75|    log.Fatal(err)
    76|}
    77|```
    78|
    79|**Accumulating the final message** (there is no `GetFinalMessage()` on the stream):
    80|
    81|```go
    82|stream := client.Messages.NewStreaming(ctx, params)
    83|message := anthropic.Message{}
    84|for stream.Next() {
    85|    message.Accumulate(stream.Current())
    86|}
    87|if err := stream.Err(); err != nil { log.Fatal(err) }
    88|// message.Content now has the complete response
    89|```
    90|
    91|---
    92|
    93|## Tool Use
    94|
    95|### Tool Runner (Beta — Recommended)
    96|
    97|**Beta:** The Go SDK provides `BetaToolRunner` for automatic tool use loops via the `toolrunner` package.
    98|
    99|```go
   100|import (
   101|    "context"
   102|    "fmt"
   103|    "log"
   104|
   105|    "github.com/anthropics/anthropic-sdk-go"
   106|    "github.com/anthropics/anthropic-sdk-go/toolrunner"
   107|)
   108|
   109|// Define tool input with jsonschema tags for automatic schema generation
   110|type GetWeatherInput struct {
   111|    City string `json:"city" jsonschema:"required,description=The city name"`
   112|}
   113|
   114|// Create a tool with automatic schema generation from struct tags
   115|weatherTool, err := toolrunner.NewBetaToolFromJSONSchema(
   116|    "get_weather",
   117|    "Get current weather for a city",
   118|    func(ctx context.Context, input GetWeatherInput) (anthropic.BetaToolResultBlockParamContentUnion, error) {
   119|        return anthropic.BetaToolResultBlockParamContentUnion{
   120|            OfText: &anthropic.BetaTextBlockParam{
   121|                Text: fmt.Sprintf("The weather in %s is sunny, 72°F", input.City),
   122|            },
   123|        }, nil
   124|    },
   125|)
   126|if err != nil {
   127|    log.Fatal(err)
   128|}
   129|
   130|// Create a tool runner that handles the conversation loop automatically
   131|runner := client.Beta.Messages.NewToolRunner(
   132|    []anthropic.BetaTool{weatherTool},
   133|    anthropic.BetaToolRunnerParams{
   134|        BetaMessageNewParams: anthropic.BetaMessageNewParams{
   135|            Model:     anthropic.ModelClaudeOpus4_6,
   136|            MaxTokens: 16000,
   137|            Messages: []anthropic.BetaMessageParam{
   138|                anthropic.NewBetaUserMessage(anthropic.NewBetaTextBlock("What's the weather in Paris?")),
   139|            },
   140|        },
   141|        MaxIterations: 5,
   142|    },
   143|)
   144|
   145|// Run until Claude produces a final response
   146|message, err := runner.RunToCompletion(context.Background())
   147|if err != nil {
   148|    log.Fatal(err)
   149|}
   150|
   151|// RunToCompletion returns *BetaMessage; content is []BetaContentBlockUnion.
   152|// Narrow via AsAny() switch — note the Beta-namespace types (BetaTextBlock,
   153|// not TextBlock):
   154|for _, block := range message.Content {
   155|    switch block := block.AsAny().(type) {
   156|    case anthropic.BetaTextBlock:
   157|        fmt.Println(block.Text)
   158|    }
   159|}
   160|```
   161|
   162|**Key features of the Go tool runner:**
   163|
   164|- Automatic schema generation from Go structs via `jsonschema` tags
   165|- `RunToCompletion()` for simple one-shot usage
   166|- `All()` iterator for processing each message in the conversation
   167|- `NextMessage()` for step-by-step iteration
   168|- Streaming variant via `NewToolRunnerStreaming()` with `AllStreaming()`
   169|
   170|### Manual Loop
   171|
   172|For fine-grained control over the agentic loop, define tools with `ToolParam`, check `StopReason`, execute tools yourself, and feed `tool_result` blocks back. This is the pattern when you need to intercept, validate, or log tool calls.
   173|
   174|Derived from `anthropic-sdk-go/examples/tools/main.go`.
   175|
   176|```go
   177|package main
   178|
   179|import (
   180|    "context"
   181|    "encoding/json"
   182|    "fmt"
   183|    "log"
   184|
   185|    "github.com/anthropics/anthropic-sdk-go"
   186|)
   187|
   188|func main() {
   189|    client := anthropic.NewClient()
   190|
   191|    // 1. Define tools. ToolParam.InputSchema uses a map, no struct tags needed.
   192|    addTool := anthropic.ToolParam{
   193|        Name:        "add",
   194|        Description: anthropic.String("Add two integers"),
   195|        InputSchema: anthropic.ToolInputSchemaParam{
   196|            Properties: map[string]any{
   197|                "a": map[string]any{"type": "integer"},
   198|                "b": map[string]any{"type": "integer"},
   199|            },
   200|        },
   201|    }
   202|    // ToolParam must be wrapped in ToolUnionParam for the Tools slice
   203|    tools := []anthropic.ToolUnionParam{{OfTool: &addTool}}
   204|
   205|    messages := []anthropic.MessageParam{
   206|        anthropic.NewUserMessage(anthropic.NewTextBlock("What is 2 + 3?")),
   207|    }
   208|
   209|    for {
   210|        resp, err := client.Messages.New(context.Background(), anthropic.MessageNewParams{
   211|            Model:     anthropic.ModelClaudeSonnet4_6,
   212|            MaxTokens: 16000,
   213|            Messages:  messages,
   214|            Tools:     tools,
   215|        })
   216|        if err != nil {
   217|            log.Fatal(err)
   218|        }
   219|
   220|        // 2. Append the assistant response to history BEFORE processing tool calls.
   221|        //    resp.ToParam() converts Message → MessageParam in one call.
   222|        messages = append(messages, resp.ToParam())
   223|
   224|        // 3. Walk content blocks. ContentBlockUnion is a flattened struct;
   225|        //    use block.AsAny().(type) to switch on the actual variant.
   226|        toolResults := []anthropic.ContentBlockParamUnion{}
   227|        for _, block := range resp.Content {
   228|            switch variant := block.AsAny().(type) {
   229|            case anthropic.TextBlock:
   230|                fmt.Println(variant.Text)
   231|            case anthropic.ToolUseBlock:
   232|                // 4. Parse the tool input. Use variant.JSON.Input.Raw() to get the
   233|                //    raw JSON — block.Input is json.RawMessage, not the parsed value.
   234|                var in struct {
   235|                    A int `json:"a"`
   236|                    B int `json:"b"`
   237|                }
   238|                if err := json.Unmarshal([]byte(variant.JSON.Input.Raw()), &in); err != nil {
   239|                    log.Fatal(err)
   240|                }
   241|                result := fmt.Sprintf("%d", in.A+in.B)
   242|                // 5. NewToolResultBlock(toolUseID, content, isError) builds the
   243|                //    ContentBlockParamUnion for you. block.ID is the tool_use_id.
   244|                toolResults = append(toolResults,
   245|                    anthropic.NewToolResultBlock(block.ID, result, false))
   246|            }
   247|        }
   248|
   249|        // 6. Exit when Claude stops asking for tools
   250|        if resp.StopReason != anthropic.StopReasonToolUse {
   251|            break
   252|        }
   253|
   254|        // 7. Tool results go in a user message (variadic: all results in one turn)
   255|        messages = append(messages, anthropic.NewUserMessage(toolResults...))
   256|    }
   257|}
   258|```
   259|
   260|**Key API surface:**
   261|
   262|| Symbol | Purpose |
   263|| --- | --- |
   264|| `resp.ToParam()` | Convert `Message` response → `MessageParam` for history |
   265|| `block.AsAny().(type)` | Type-switch on `ContentBlockUnion` variants |
   266|| `variant.JSON.Input.Raw()` | Raw JSON string of tool input (for `json.Unmarshal`) |
   267|| `anthropic.NewToolResultBlock(id, content, isError)` | Build `tool_result` block |
   268|| `anthropic.NewUserMessage(blocks...)` | Wrap tool results as a user turn |
   269|| `anthropic.StopReasonToolUse` | `StopReason` constant to check loop termination |
   270|| `anthropic.ToolUnionParam{OfTool: &t}` | Wrap `ToolParam` in the union for `Tools:` |
   271|
   272|---
   273|
   274|## Thinking
   275|
   276|Enable Claude's internal reasoning by setting `Thinking` in `MessageNewParams`. The response will contain `ThinkingBlock` content before the final `TextBlock`.
   277|
   278|**Adaptive thinking is the recommended mode for Claude 4.6+ models.** Claude decides dynamically when and how much to think. Combine with the `effort` parameter for cost-quality control.
   279|
   280|Derived from `anthropic-sdk-go/message.go` (`ThinkingConfigParamUnion`, `NewThinkingConfigAdaptiveParam`).
   281|
   282|```go
   283|// There is no ThinkingConfigParamOfAdaptive helper — construct the union
   284|// struct-literal directly and take the address of the variant.
   285|adaptive := anthropic.NewThinkingConfigAdaptiveParam()
   286|params := anthropic.MessageNewParams{
   287|    Model:     anthropic.ModelClaudeSonnet4_6,
   288|    MaxTokens: 16000,
   289|    Thinking:  anthropic.ThinkingConfigParamUnion{OfAdaptive: &adaptive},
   290|    Messages: []anthropic.MessageParam{
   291|        anthropic.NewUserMessage(anthropic.NewTextBlock("How many r's in strawberry?")),
   292|    },
   293|}
   294|
   295|resp, err := client.Messages.New(context.Background(), params)
   296|if err != nil {
   297|    log.Fatal(err)
   298|}
   299|
   300|// ThinkingBlock(s) precede TextBlock in content
   301|for _, block := range resp.Content {
   302|    switch b := block.AsAny().(type) {
   303|    case anthropic.ThinkingBlock:
   304|        fmt.Println("[thinking]", b.Thinking)
   305|    case anthropic.TextBlock:
   306|        fmt.Println(b.Text)
   307|    }
   308|}
   309|```
   310|
   311|> **Deprecated:** `ThinkingConfigParamOfEnabled(budgetTokens)` (fixed-budget extended thinking) still works on Claude 4.6 but is deprecated. Use adaptive thinking above.
   312|
   313|To disable: `anthropic.ThinkingConfigParamUnion{OfDisabled: &anthropic.ThinkingConfigDisabledParam{}}`.
   314|
   315|---
   316|
   317|## Prompt Caching
   318|
   319|`System` is `[]TextBlockParam`; set `CacheControl` on the last block to cache tools + system together. For placement patterns and the silent-invalidator audit checklist, see `shared/prompt-caching.md`.
   320|
   321|```go
   322|System: []anthropic.TextBlockParam{{
   323|    Text:         longSystemPrompt,
   324|    CacheControl: anthropic.NewCacheControlEphemeralParam(), // default 5m TTL
   325|}},
   326|```
   327|
   328|For 1-hour TTL: `anthropic.CacheControlEphemeralParam{TTL: anthropic.CacheControlEphemeralTTLTTL1h}`. There's also a top-level `CacheControl` on `MessageNewParams` that auto-places on the last cacheable block.
   329|
   330|Verify hits via `resp.Usage.CacheCreationInputTokens` / `resp.Usage.CacheReadInputTokens`.
   331|
   332|---
   333|
   334|## Server-Side Tools
   335|
   336|Version-suffixed struct names with `Param` suffix. `Name`/`Type` are `constant.*` types — zero value marshals correctly, so `{}` works. Wrap in `ToolUnionParam` with the matching `Of*` field.
   337|
   338|```go
   339|Tools: []anthropic.ToolUnionParam{
   340|    {OfWebSearchTool20260209: &anthropic.WebSearchTool20260209Param{}},
   341|    {OfBashTool20250124: &anthropic.ToolBash20250124Param{}},
   342|    {OfTextEditor20250728: &anthropic.ToolTextEditor20250728Param{}},
   343|    {OfCodeExecutionTool20260120: &anthropic.CodeExecutionTool20260120Param{}},
   344|},
   345|```
   346|
   347|Also available: `WebFetchTool20260209Param`, `MemoryTool20250818Param`, `ToolSearchToolBm25_20251119Param`, `ToolSearchToolRegex20251119Param`.
   348|
   349|---
   350|
   351|## PDF / Document Input
   352|
   353|`NewDocumentBlock` generic helper accepts any source type. `MediaType`/`Type` are auto-set.
   354|
   355|```go
   356|b64 := base64.StdEncoding.EncodeToString(pdfBytes)
   357|
   358|msg := anthropic.NewUserMessage(
   359|    anthropic.NewDocumentBlock(anthropic.Base64PDFSourceParam{Data: b64}),
   360|    anthropic.NewTextBlock("Summarize this document"),
   361|)
   362|```
   363|
   364|Other sources: `URLPDFSourceParam{URL: "https://..."}`, `PlainTextSourceParam{Data: "..."}`.
   365|
   366|---
   367|
   368|## Files API (Beta)
   369|
   370|Under `client.Beta.Files`. Method is **`Upload`** (NOT `New`/`Create`), params struct is `BetaFileUploadParams`. The `File` field takes an `io.Reader`; use `anthropic.File()` to attach a filename + content-type for the multipart encoding.
   371|
   372|```go
   373|f, _ := os.Open("./upload_me.txt")
   374|defer f.Close()
   375|
   376|meta, err := client.Beta.Files.Upload(ctx, anthropic.BetaFileUploadParams{
   377|    File:  anthropic.File(f, "upload_me.txt", "text/plain"),
   378|    Betas: []anthropic.AnthropicBeta{anthropic.AnthropicBetaFilesAPI2025_04_14},
   379|})
   380|// meta.ID is the file_id to reference in subsequent message requests
   381|```
   382|
   383|Other `Beta.Files` methods: `List`, `Delete`, `Download`, `GetMetadata`.
   384|
   385|---
   386|
   387|## Context Editing / Compaction (Beta)
   388|
   389|Use `Beta.Messages.New` with `ContextManagement` on `BetaMessageNewParams`. There is no `NewBetaAssistantMessage` — use `.ToParam()` for the round-trip.
   390|
   391|```go
   392|params := anthropic.BetaMessageNewParams{
   393|    Model:     anthropic.ModelClaudeOpus4_6,  // also supported: ModelClaudeSonnet4_6
   394|    MaxTokens: 16000,
   395|    Betas:     []anthropic.AnthropicBeta{"compact-2026-01-12"},
   396|    ContextManagement: anthropic.BetaContextManagementConfigParam{
   397|        Edits: []anthropic.BetaContextManagementConfigEditUnionParam{
   398|            {OfCompact20260112: &anthropic.BetaCompact20260112EditParam{}},
   399|        },
   400|    },
   401|    Messages: []anthropic.BetaMessageParam{ /* ... */ },
   402|}
   403|
   404|resp, err := client.Beta.Messages.New(ctx, params)
   405|if err != nil {
   406|    log.Fatal(err)
   407|}
   408|
   409|// Round-trip: append response to history via .ToParam()
   410|params.Messages = append(params.Messages, resp.ToParam())
   411|
   412|// Read compaction blocks from the response
   413|for _, block := range resp.Content {
   414|    if c, ok := block.AsAny().(anthropic.BetaCompactionBlock); ok {
   415|        fmt.Println("compaction summary:", c.Content)
   416|    }
   417|}
   418|```
   419|
   420|Other edit types: `BetaClearToolUses20250919EditParam`, `BetaClearThinking20251015EditParam`.
   421|