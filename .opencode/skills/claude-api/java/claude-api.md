---
name: claude-api-java
description: "Claude API — Java reference documentation"
version: 1.0.0
author: Alexa
---
     1|# Claude API — Java
     2|
     3|> **Note:** The Java SDK supports the Claude API and beta tool use with annotated classes. Agent SDK is not yet available for Java.
     4|
     5|## Installation
     6|
     7|Maven:
     8|
     9|```xml
    10|<dependency>
    11|    <groupId>com.anthropic</groupId>
    12|    <artifactId>anthropic-java</artifactId>
    13|    <version>2.17.0</version>
    14|</dependency>
    15|```
    16|
    17|Gradle:
    18|
    19|```groovy
    20|implementation("com.anthropic:anthropic-java:2.17.0")
    21|```
    22|
    23|## Client Initialization
    24|
    25|```java
    26|import com.anthropic.client.AnthropicClient;
    27|import com.anthropic.client.okhttp.AnthropicOkHttpClient;
    28|
    29|// Default (reads ANTHROPIC_API_KEY from environment)
    30|AnthropicClient client = AnthropicOkHttpClient.fromEnv();
    31|
    32|// Explicit API key
    33|AnthropicClient client = AnthropicOkHttpClient.builder()
    34|    .apiKey("your-api-key")
    35|    .build();
    36|```
    37|
    38|---
    39|
    40|## Basic Message Request
    41|
    42|```java
    43|import com.anthropic.models.messages.MessageCreateParams;
    44|import com.anthropic.models.messages.Message;
    45|import com.anthropic.models.messages.Model;
    46|
    47|MessageCreateParams params = MessageCreateParams.builder()
    48|    .model(Model.CLAUDE_OPUS_4_6)
    49|    .maxTokens(16000L)
    50|    .addUserMessage("What is the capital of France?")
    51|    .build();
    52|
    53|Message response = client.messages().create(params);
    54|response.content().stream()
    55|    .flatMap(block -> block.text().stream())
    56|    .forEach(textBlock -> System.out.println(textBlock.text()));
    57|```
    58|
    59|---
    60|
    61|## Streaming
    62|
    63|```java
    64|import com.anthropic.core.http.StreamResponse;
    65|import com.anthropic.models.messages.RawMessageStreamEvent;
    66|
    67|MessageCreateParams params = MessageCreateParams.builder()
    68|    .model(Model.CLAUDE_OPUS_4_6)
    69|    .maxTokens(64000L)
    70|    .addUserMessage("Write a haiku")
    71|    .build();
    72|
    73|try (StreamResponse<RawMessageStreamEvent> streamResponse = client.messages().createStreaming(params)) {
    74|    streamResponse.stream()
    75|        .flatMap(event -> event.contentBlockDelta().stream())
    76|        .flatMap(deltaEvent -> deltaEvent.delta().text().stream())
    77|        .forEach(textDelta -> System.out.print(textDelta.text()));
    78|}
    79|```
    80|
    81|---
    82|
    83|## Thinking
    84|
    85|**Adaptive thinking is the recommended mode for Claude 4.6+ models.** Claude decides dynamically when and how much to think. The builder has a direct `.thinking(ThinkingConfigAdaptive)` overload — no manual union wrapping.
    86|
    87|```java
    88|import com.anthropic.models.messages.ContentBlock;
    89|import com.anthropic.models.messages.MessageCreateParams;
    90|import com.anthropic.models.messages.Model;
    91|import com.anthropic.models.messages.ThinkingConfigAdaptive;
    92|
    93|MessageCreateParams params = MessageCreateParams.builder()
    94|    .model(Model.CLAUDE_SONNET_4_6)
    95|    .maxTokens(16000L)
    96|    .thinking(ThinkingConfigAdaptive.builder().build())
    97|    .addUserMessage("Solve this step by step: 27 * 453")
    98|    .build();
    99|
   100|for (ContentBlock block : client.messages().create(params).content()) {
   101|    block.thinking().ifPresent(t -> System.out.println("[thinking] " + t.thinking()));
   102|    block.text().ifPresent(t -> System.out.println(t.text()));
   103|}
   104|```
   105|
   106|> **Deprecated:** `ThinkingConfigEnabled.builder().budgetTokens(N)` (and the `.enabledThinking(N)` shortcut) still works on Claude 4.6 but is deprecated. Use adaptive thinking above.
   107|
   108|`ContentBlock` narrowing: `.thinking()` / `.text()` return `Optional<T>` — use `.ifPresent(...)` or `.stream().flatMap(...)`. Alternative: `isThinking()` / `asThinking()` boolean+unwrap pairs (throws on wrong variant).
   109|
   110|---
   111|
   112|## Tool Use (Beta)
   113|
   114|The Java SDK supports beta tool use with annotated classes. Tool classes implement `Supplier<String>` for automatic execution via `BetaToolRunner`.
   115|
   116|### Tool Runner (automatic loop)
   117|
   118|```java
   119|import com.anthropic.models.beta.messages.MessageCreateParams;
   120|import com.anthropic.models.beta.messages.BetaMessage;
   121|import com.anthropic.helpers.BetaToolRunner;
   122|import com.fasterxml.jackson.annotation.JsonClassDescription;
   123|import com.fasterxml.jackson.annotation.JsonPropertyDescription;
   124|import java.util.function.Supplier;
   125|
   126|@JsonClassDescription("Get the weather in a given location")
   127|static class GetWeather implements Supplier<String> {
   128|    @JsonPropertyDescription("The city and state, e.g. San Francisco, CA")
   129|    public String location;
   130|
   131|    @Override
   132|    public String get() {
   133|        return "The weather in " + location + " is sunny and 72°F";
   134|    }
   135|}
   136|
   137|BetaToolRunner toolRunner = client.beta().messages().toolRunner(
   138|    MessageCreateParams.builder()
   139|        .model("claude-opus-4-7")
   140|        .maxTokens(16000L)
   141|        .putAdditionalHeader("anthropic-beta", "structured-outputs-2025-11-13")
   142|        .addTool(GetWeather.class)
   143|        .addUserMessage("What's the weather in San Francisco?")
   144|        .build());
   145|
   146|for (BetaMessage message : toolRunner) {
   147|    System.out.println(message);
   148|}
   149|```
   150|
   151|### Memory Tool
   152|
   153|The Java SDK provides `BetaMemoryToolHandler` for implementing the memory tool backend. You supply a handler that manages file storage, and the `BetaToolRunner` handles memory tool calls automatically.
   154|
   155|```java
   156|import com.anthropic.helpers.BetaMemoryToolHandler;
   157|import com.anthropic.helpers.BetaToolRunner;
   158|import com.anthropic.models.beta.messages.BetaMemoryTool20250818;
   159|import com.anthropic.models.beta.messages.BetaMessage;
   160|import com.anthropic.models.beta.messages.MessageCreateParams;
   161|import com.anthropic.models.beta.messages.ToolRunnerCreateParams;
   162|
   163|// Implement BetaMemoryToolHandler with your storage backend (e.g., filesystem)
   164|BetaMemoryToolHandler memoryHandler = new FileSystemMemoryToolHandler(sandboxRoot);
   165|
   166|MessageCreateParams createParams = MessageCreateParams.builder()
   167|    .model("claude-opus-4-7")
   168|    .maxTokens(4096L)
   169|    .addTool(BetaMemoryTool20250818.builder().build())
   170|    .addUserMessage("Remember that my favorite color is blue")
   171|    .build();
   172|
   173|BetaToolRunner toolRunner = client.beta().messages().toolRunner(
   174|    ToolRunnerCreateParams.builder()
   175|        .betaMemoryToolHandler(memoryHandler)
   176|        .initialMessageParams(createParams)
   177|        .build());
   178|
   179|for (BetaMessage message : toolRunner) {
   180|    System.out.println(message);
   181|}
   182|```
   183|
   184|See the [shared memory tool concepts](../shared/tool-use-concepts.md) for more details on the memory tool.
   185|
   186|### Non-Beta Tool Declaration (manual JSON schema)
   187|
   188|`Tool.InputSchema.Properties` is a freeform `Map<String, JsonValue>` wrapper — build property schemas via `putAdditionalProperty`. `type: "object"` is the default. The builder has a direct `.addTool(Tool)` overload that wraps in `ToolUnion` automatically.
   189|
   190|```java
   191|import com.anthropic.core.JsonValue;
   192|import com.anthropic.models.messages.Tool;
   193|
   194|Tool tool = Tool.builder()
   195|    .name("get_weather")
   196|    .description("Get the current weather in a given location")
   197|    .inputSchema(Tool.InputSchema.builder()
   198|        .properties(Tool.InputSchema.Properties.builder()
   199|            .putAdditionalProperty("location", JsonValue.from(Map.of("type", "string")))
   200|            .build())
   201|        .required(List.of("location"))
   202|        .build())
   203|    .build();
   204|
   205|MessageCreateParams params = MessageCreateParams.builder()
   206|    .model(Model.CLAUDE_SONNET_4_6)
   207|    .maxTokens(16000L)
   208|    .addTool(tool)
   209|    .addUserMessage("Weather in Paris?")
   210|    .build();
   211|```
   212|
   213|For manual tool loops, handle `tool_use` blocks in the response, send `tool_result` back, loop until `stop_reason` is `"end_turn"`. See [shared tool use concepts](../shared/tool-use-concepts.md).
   214|
   215|### Building `MessageParam` with Content Blocks (Tool Result Round-Trip)
   216|
   217|`MessageParam.Content` is an inner union class (string | list). Use the builder's `.contentOfBlockParams(List<ContentBlockParam>)` alias — there is NO separate `MessageParamContent` class with a static `ofBlockParams`:
   218|
   219|```java
   220|import com.anthropic.models.messages.MessageParam;
   221|import com.anthropic.models.messages.ContentBlockParam;
   222|import com.anthropic.models.messages.ToolResultBlockParam;
   223|
   224|List<ContentBlockParam> results = List.of(
   225|    ContentBlockParam.ofToolResult(ToolResultBlockParam.builder()
   226|        .toolUseId(toolUseBlock.id())
   227|        .content(yourResultString)
   228|        .build())
   229|);
   230|
   231|MessageParam toolResultMsg = MessageParam.builder()
   232|    .role(MessageParam.Role.USER)
   233|    .contentOfBlockParams(results)   // builder alias for Content.ofBlockParams(...)
   234|    .build();
   235|```
   236|
   237|---
   238|
   239|## Effort Parameter
   240|
   241|Effort is nested inside `OutputConfig` — there is NO `.effort()` directly on `MessageCreateParams.Builder`.
   242|
   243|```java
   244|import com.anthropic.models.messages.OutputConfig;
   245|
   246|.outputConfig(OutputConfig.builder()
   247|    .effort(OutputConfig.Effort.HIGH)  // or LOW, MEDIUM, MAX
   248|    .build())
   249|```
   250|
   251|Combine with `Thinking = ThinkingConfigAdaptive` for cost-quality control.
   252|
   253|---
   254|
   255|## Prompt Caching
   256|
   257|System message as a list of `TextBlockParam` with `CacheControlEphemeral`. Use `.systemOfTextBlockParams(...)` — the plain `.system(String)` overload can't carry cache control. For placement patterns and the silent-invalidator audit checklist, see `shared/prompt-caching.md`.
   258|
   259|```java
   260|import com.anthropic.models.messages.TextBlockParam;
   261|import com.anthropic.models.messages.CacheControlEphemeral;
   262|
   263|.systemOfTextBlockParams(List.of(
   264|    TextBlockParam.builder()
   265|        .text(longSystemPrompt)
   266|        .cacheControl(CacheControlEphemeral.builder()
   267|            .ttl(CacheControlEphemeral.Ttl.TTL_1H)  // optional; also TTL_5M
   268|            .build())
   269|        .build()))
   270|```
   271|
   272|There's also a top-level `.cacheControl(CacheControlEphemeral)` on `MessageCreateParams.Builder` and on `Tool.builder()`.
   273|
   274|Verify hits via `response.usage().cacheCreationInputTokens()` / `response.usage().cacheReadInputTokens()`.
   275|
   276|---
   277|
   278|## Token Counting
   279|
   280|```java
   281|import com.anthropic.models.messages.MessageCountTokensParams;
   282|
   283|long tokens = client.messages().countTokens(
   284|    MessageCountTokensParams.builder()
   285|        .model(Model.CLAUDE_SONNET_4_6)
   286|        .addUserMessage("Hello")
   287|        .build()
   288|).inputTokens();
   289|```
   290|
   291|---
   292|
   293|## Structured Output
   294|
   295|The class-based overload auto-derives the JSON schema from your POJO and gives you a typed `.text()` return — no manual schema, no manual parsing.
   296|
   297|```java
   298|import com.anthropic.models.messages.StructuredMessageCreateParams;
   299|
   300|record Book(String title, String author) {}
   301|record BookList(List<Book> books) {}
   302|
   303|StructuredMessageCreateParams<BookList> params = MessageCreateParams.builder()
   304|    .model(Model.CLAUDE_SONNET_4_6)
   305|    .maxTokens(16000L)
   306|    .outputConfig(BookList.class)  // returns a typed builder
   307|    .addUserMessage("List 3 classic novels")
   308|    .build();
   309|
   310|client.messages().create(params).content().stream()
   311|    .flatMap(cb -> cb.text().stream())
   312|    .forEach(typed -> {
   313|        // typed.text() returns BookList, not String
   314|        for (Book b : typed.text().books()) System.out.println(b.title());
   315|    });
   316|```
   317|
   318|Supports Jackson annotations: `@JsonPropertyDescription`, `@JsonIgnore`, `@ArraySchema(minItems=...)`. Manual schema path: `OutputConfig.builder().format(JsonOutputFormat.builder().schema(...).build())`.
   319|
   320|---
   321|
   322|## PDF / Document Input
   323|
   324|`DocumentBlockParam` builder has source shortcuts. Wrap in `ContentBlockParam.ofDocument()` and pass via `.addUserMessageOfBlockParams()`.
   325|
   326|```java
   327|import com.anthropic.models.messages.DocumentBlockParam;
   328|import com.anthropic.models.messages.ContentBlockParam;
   329|import com.anthropic.models.messages.TextBlockParam;
   330|
   331|DocumentBlockParam doc = DocumentBlockParam.builder()
   332|    .base64Source(base64String)  // or .urlSource("https://...") or .textSource("...")
   333|    .title("My Document")        // optional
   334|    .build();
   335|
   336|.addUserMessageOfBlockParams(List.of(
   337|    ContentBlockParam.ofDocument(doc),
   338|    ContentBlockParam.ofText(TextBlockParam.builder().text("Summarize this").build())))
   339|```
   340|
   341|---
   342|
   343|## Server-Side Tools
   344|
   345|Version-suffixed types; `name`/`type` auto-set by builder. Direct `.addTool()` overloads exist for every type — no manual `ToolUnion` wrapping.
   346|
   347|```java
   348|import com.anthropic.models.messages.WebSearchTool20260209;
   349|import com.anthropic.models.messages.ToolBash20250124;
   350|import com.anthropic.models.messages.ToolTextEditor20250728;
   351|import com.anthropic.models.messages.CodeExecutionTool20260120;
   352|
   353|.addTool(WebSearchTool20260209.builder()
   354|    .maxUses(5L)                              // optional
   355|    .allowedDomains(List.of("example.com"))   // optional
   356|    .build())
   357|.addTool(ToolBash20250124.builder().build())
   358|.addTool(ToolTextEditor20250728.builder().build())
   359|.addTool(CodeExecutionTool20260120.builder().build())
   360|```
   361|
   362|Also available: `WebFetchTool20260209`, `MemoryTool20250818`, `ToolSearchToolBm25_20251119`.
   363|
   364|### Beta namespace (MCP, compaction)
   365|
   366|For beta-only features use `com.anthropic.models.beta.messages.*` — class names have a `Beta` prefix AND live in the beta package. The beta `MessageCreateParams.Builder` has direct `.addTool(BetaToolBash20250124)` overloads AND `.addMcpServer()`:
   367|
   368|```java
   369|import com.anthropic.models.beta.messages.MessageCreateParams;
   370|import com.anthropic.models.beta.messages.BetaToolBash20250124;
   371|import com.anthropic.models.beta.messages.BetaCodeExecutionTool20260120;
   372|import com.anthropic.models.beta.messages.BetaRequestMcpServerUrlDefinition;
   373|
   374|MessageCreateParams params = MessageCreateParams.builder()
   375|    .model(Model.CLAUDE_OPUS_4_6)
   376|    .maxTokens(16000L)
   377|    .addBeta("mcp-client-2025-11-20")
   378|    .addTool(BetaToolBash20250124.builder().build())
   379|    .addTool(BetaCodeExecutionTool20260120.builder().build())
   380|    .addMcpServer(BetaRequestMcpServerUrlDefinition.builder()
   381|        .name("my-server")
   382|        .url("https://example.com/mcp")
   383|        .build())
   384|    .addUserMessage("...")
   385|    .build();
   386|
   387|client.beta().messages().create(params);
   388|```
   389|
   390|`BetaTool*` types are NOT interchangeable with non-beta `Tool*` — pick one namespace per request.
   391|
   392|**Reading server-tool blocks in the response:** `ServerToolUseBlock` has `.id()`, `.name()` (enum), and `._input()` returning raw `JsonValue` — there is NO typed `.input()`. For code execution results, unwrap two levels:
   393|
   394|```java
   395|for (ContentBlock block : response.content()) {
   396|    block.serverToolUse().ifPresent(stu -> {
   397|        System.out.println("tool: " + stu.name() + " input: " + stu._input());
   398|    });
   399|    block.codeExecutionToolResult().ifPresent(r -> {
   400|        r.content().resultBlock().ifPresent(result -> {
   401|            System.out.println("stdout: " + result.stdout());
   402|            System.out.println("stderr: " + result.stderr());
   403|            System.out.println("exit: " + result.returnCode());
   404|        });
   405|    });
   406|}
   407|```
   408|
   409|---
   410|
   411|## Files API (Beta)
   412|
   413|Under `client.beta().files()`. File references in messages need the beta message types (non-beta `DocumentBlockParam.Source` has no file-ID variant).
   414|
   415|```java
   416|import com.anthropic.models.beta.files.FileUploadParams;
   417|import com.anthropic.models.beta.files.FileMetadata;
   418|import com.anthropic.models.beta.messages.BetaRequestDocumentBlock;
   419|import java.nio.file.Paths;
   420|
   421|FileMetadata meta = client.beta().files().upload(
   422|    FileUploadParams.builder()
   423|        .file(Paths.get("/path/to/doc.pdf"))  // or .file(InputStream) or .file(byte[])
   424|        .build());
   425|
   426|// Reference in a beta message:
   427|BetaRequestDocumentBlock doc = BetaRequestDocumentBlock.builder()
   428|    .fileSource(meta.id())
   429|    .build();
   430|```
   431|
   432|Other methods: `.list()`, `.delete(String fileId)`, `.download(String fileId)`, `.retrieveMetadata(String fileId)`.
   433|