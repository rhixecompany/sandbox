---
name: typescript-claude-api
description: "Claude API — TypeScript"
version: 1.0.0
author: Alexa
---
     1|# Claude API — TypeScript
     2|
     3|## Installation
     4|
     5|```bash
     6|npm install @anthropic-ai/sdk
     7|```
     8|
     9|## Client Initialization
    10|
    11|```typescript
    12|import Anthropic from "@anthropic-ai/sdk";
    13|
    14|// Default (uses ANTHROPIC_API_KEY env var)
    15|const client = new Anthropic();
    16|
    17|// Explicit API key
    18|const client = new Anthropic({ apiKey: "your-api-key" });
    19|```
    20|
    21|---
    22|
    23|## Basic Message Request
    24|
    25|```typescript
    26|const response = await client.messages.create({
    27|  model: "claude-opus-4-7",
    28|  max_tokens: 16000,
    29|  messages: [
    30|    { role: "user", content: "What is the capital of France?" }
    31|  ]
    32|});
    33|// response.content is ContentBlock[] — a discriminated union. Narrow by .type
    34|// before accessing .text (TypeScript will error on content[0].text without this).
    35|for (const block of response.content) {
    36|  if (block.type === "text") {
    37|    console.log(block.text);
    38|  }
    39|}
    40|```
    41|
    42|---
    43|
    44|## System Prompts
    45|
    46|```typescript
    47|const response = await client.messages.create({
    48|  model: "claude-opus-4-7",
    49|  max_tokens: 16000,
    50|  system:
    51|    "You are a helpful coding assistant. Always provide examples in Python.",
    52|  messages: [{ role: "user", content: "How do I read a JSON file?" }]
    53|});
    54|```
    55|
    56|---
    57|
    58|## Vision (Images)
    59|
    60|### URL
    61|
    62|```typescript
    63|const response = await client.messages.create({
    64|  model: "claude-opus-4-7",
    65|  max_tokens: 16000,
    66|  messages: [
    67|    {
    68|      role: "user",
    69|      content: [
    70|        {
    71|          type: "image",
    72|          source: {
    73|            type: "url",
    74|            url: "https://example.com/image.png"
    75|          }
    76|        },
    77|        { type: "text", text: "Describe this image" }
    78|      ]
    79|    }
    80|  ]
    81|});
    82|```
    83|
    84|### Base64
    85|
    86|```typescript
    87|import fs from "fs";
    88|
    89|const imageData = fs.readFileSync("image.png").toString("base64");
    90|
    91|const response = await client.messages.create({
    92|  model: "claude-opus-4-7",
    93|  max_tokens: 16000,
    94|  messages: [
    95|    {
    96|      role: "user",
    97|      content: [
    98|        {
    99|          type: "image",
   100|          source: {
   101|            type: "base64",
   102|            media_type: "image/png",
   103|            data: imageData
   104|          }
   105|        },
   106|        { type: "text", text: "What's in this image?" }
   107|      ]
   108|    }
   109|  ]
   110|});
   111|```
   112|
   113|---
   114|
   115|## Prompt Caching
   116|
   117|**Caching is a prefix match** — any byte change anywhere in the prefix invalidates everything after it. For placement patterns, architectural guidance (frozen system prompt, deterministic tool order, where to put volatile content), and the silent-invalidator audit checklist, read `shared/prompt-caching.md`.
   118|
   119|### Automatic Caching (Recommended)
   120|
   121|Use top-level `cache_control` to automatically cache the last cacheable block in the request:
   122|
   123|```typescript
   124|const response = await client.messages.create({
   125|  model: "claude-opus-4-7",
   126|  max_tokens: 16000,
   127|  cache_control: { type: "ephemeral" }, // auto-caches the last cacheable block
   128|  system: "You are an expert on this large document...",
   129|  messages: [{ role: "user", content: "Summarize the key points" }]
   130|});
   131|```
   132|
   133|### Manual Cache Control
   134|
   135|For fine-grained control, add `cache_control` to specific content blocks:
   136|
   137|```typescript
   138|const response = await client.messages.create({
   139|  model: "claude-opus-4-7",
   140|  max_tokens: 16000,
   141|  system: [
   142|    {
   143|      type: "text",
   144|      text: "You are an expert on this large document...",
   145|      cache_control: { type: "ephemeral" } // default TTL is 5 minutes
   146|    }
   147|  ],
   148|  messages: [{ role: "user", content: "Summarize the key points" }]
   149|});
   150|
   151|// With explicit TTL (time-to-live)
   152|const response2 = await client.messages.create({
   153|  model: "claude-opus-4-7",
   154|  max_tokens: 16000,
   155|  system: [
   156|    {
   157|      type: "text",
   158|      text: "You are an expert on this large document...",
   159|      cache_control: { type: "ephemeral", ttl: "1h" } // 1 hour TTL
   160|    }
   161|  ],
   162|  messages: [{ role: "user", content: "Summarize the key points" }]
   163|});
   164|```
   165|
   166|### Verifying Cache Hits
   167|
   168|```typescript
   169|console.log(response.usage.cache_creation_input_tokens); // tokens written to cache (~1.25x cost)
   170|console.log(response.usage.cache_read_input_tokens); // tokens served from cache (~0.1x cost)
   171|console.log(response.usage.input_tokens); // uncached tokens (full cost)
   172|```
   173|
   174|If `cache_read_input_tokens` is zero across repeated identical-prefix requests, a silent invalidator is at work — `Date.now()` or a UUID in the system prompt, non-deterministic key ordering, or a varying tool set. See `shared/prompt-caching.md` for the full audit table.
   175|
   176|---
   177|
   178|## Extended Thinking
   179|
   180|> **Opus 4.7, Opus 4.6, and Sonnet 4.6:** Use adaptive thinking. `budget_tokens` is removed on Opus 4.7 (400 if sent); deprecated on Opus 4.6 and Sonnet 4.6. **Older models:** Use `thinking: {type: "enabled", budget_tokens: N}` (must be < `max_tokens`, min 1024).
   181|
   182|```typescript
   183|// Opus 4.7 / 4.6: adaptive thinking (recommended)
   184|const response = await client.messages.create({
   185|  model: "claude-opus-4-7",
   186|  max_tokens: 16000,
   187|  thinking: { type: "adaptive" },
   188|  output_config: { effort: "high" }, // low | medium | high | max
   189|  messages: [
   190|    {
   191|      role: "user",
   192|      content: "Solve this math problem step by step..."
   193|    }
   194|  ]
   195|});
   196|
   197|for (const block of response.content) {
   198|  if (block.type === "thinking") {
   199|    console.log("Thinking:", block.thinking);
   200|  } else if (block.type === "text") {
   201|    console.log("Response:", block.text);
   202|  }
   203|}
   204|```
   205|
   206|---
   207|
   208|## Error Handling
   209|
   210|Use the SDK's typed exception classes — never check error messages with string matching:
   211|
   212|```typescript
   213|import Anthropic from "@anthropic-ai/sdk";
   214|
   215|try {
   216|  const response = await client.messages.create({...});
   217|} catch (error) {
   218|  if (error instanceof Anthropic.BadRequestError) {
   219|    console.error("Bad request:", error.message);
   220|  } else if (error instanceof Anthropic.AuthenticationError) {
   221|    console.error("Invalid API key");
   222|  } else if (error instanceof Anthropic.RateLimitError) {
   223|    console.error("Rate limited - retry later");
   224|  } else if (error instanceof Anthropic.APIError) {
   225|    console.error(`API error ${error.status}:`, error.message);
   226|  }
   227|}
   228|```
   229|
   230|All classes extend `Anthropic.APIError` with a typed `status` field. Check from most specific to least specific. See [shared/error-codes.md](../../shared/error-codes.md) for the full error code reference.
   231|
   232|---
   233|
   234|## Multi-Turn Conversations
   235|
   236|The API is stateless — send the full conversation history each time. Use `Anthropic.MessageParam[]` to type the messages array:
   237|
   238|```typescript
   239|const messages: Anthropic.MessageParam[] = [
   240|  { role: "user", content: "My name is Alice." },
   241|  { role: "assistant", content: "Hello Alice! Nice to meet you." },
   242|  { role: "user", content: "What's my name?" }
   243|];
   244|
   245|const response = await client.messages.create({
   246|  model: "claude-opus-4-7",
   247|  max_tokens: 16000,
   248|  messages: messages
   249|});
   250|```
   251|
   252|**Rules:**
   253|
   254|- Consecutive same-role messages are allowed — the API combines them into a single turn
   255|- First message must be `user`
   256|- Use SDK types (`Anthropic.MessageParam`, `Anthropic.Message`, `Anthropic.Tool`, etc.) for all API data structures — don't redefine equivalent interfaces
   257|
   258|---
   259|
   260|### Compaction (long conversations)
   261|
   262|> **Beta, Opus 4.7, Opus 4.6, and Sonnet 4.6.** When conversations approach the 200K context window, compaction automatically summarizes earlier context server-side. The API returns a `compaction` block; you must pass it back on subsequent requests — append `response.content`, not just the text.
   263|
   264|```typescript
   265|import Anthropic from "@anthropic-ai/sdk";
   266|
   267|const client = new Anthropic();
   268|const messages: Anthropic.Beta.BetaMessageParam[] = [];
   269|
   270|async function chat(userMessage: string): Promise<string> {
   271|  messages.push({ role: "user", content: userMessage });
   272|
   273|  const response = await client.beta.messages.create({
   274|    betas: ["compact-2026-01-12"],
   275|    model: "claude-opus-4-7",
   276|    max_tokens: 16000,
   277|    messages,
   278|    context_management: {
   279|      edits: [{ type: "compact_20260112" }]
   280|    }
   281|  });
   282|
   283|  // Append full content — compaction blocks must be preserved
   284|  messages.push({ role: "assistant", content: response.content });
   285|
   286|  const textBlock = response.content.find(
   287|    (b): b is Anthropic.Beta.BetaTextBlock => b.type === "text"
   288|  );
   289|  return textBlock?.text ?? "";
   290|}
   291|
   292|// Compaction triggers automatically when context grows large
   293|console.log(await chat("Help me build a Python web scraper"));
   294|console.log(await chat("Add support for JavaScript-rendered pages"));
   295|console.log(await chat("Now add rate limiting and error handling"));
   296|```
   297|
   298|---
   299|
   300|## Stop Reasons
   301|
   302|The `stop_reason` field in the response indicates why the model stopped generating:
   303|
   304|| Value | Meaning |
   305|| --- | --- |
   306|| `end_turn` | Claude finished its response naturally |
   307|| `max_tokens` | Hit the `max_tokens` limit — increase it or use streaming |
   308|| `stop_sequence` | Hit a custom stop sequence |
   309|| `tool_use` | Claude wants to call a tool — execute it and continue |
   310|| `pause_turn` | Model paused and can be resumed (agentic flows) |
   311|| `refusal` | Claude refused for safety reasons — output may not match schema |
   312|
   313|---
   314|
   315|## Cost Optimization Strategies
   316|
   317|### 1. Use Prompt Caching for Repeated Context
   318|
   319|```typescript
   320|// Automatic caching (simplest — caches the last cacheable block)
   321|const response = await client.messages.create({
   322|  model: "claude-opus-4-7",
   323|  max_tokens: 16000,
   324|  cache_control: { type: "ephemeral" },
   325|  system: largeDocumentText, // e.g., 50KB of context
   326|  messages: [{ role: "user", content: "Summarize the key points" }]
   327|});
   328|
   329|// First request: full cost
   330|// Subsequent requests: ~90% cheaper for cached portion
   331|```
   332|
   333|### 2. Use Token Counting Before Requests
   334|
   335|```typescript
   336|const countResponse = await client.messages.countTokens({
   337|  model: "claude-opus-4-7",
   338|  messages: messages,
   339|  system: system
   340|});
   341|
   342|const estimatedInputCost = countResponse.input_tokens * 0.000005; // $5/1M tokens
   343|console.log(
   344|  `Estimated input cost: $${estimatedInputCost.toFixed(4)}`
   345|);
   346|```
   347|