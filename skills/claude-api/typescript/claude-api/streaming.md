---
name: typescript-streaming
description: "Streaming — TypeScript"
version: 1.0.0
author: Alexa
---
     1|# Streaming — TypeScript
     2|
     3|## Quick Start
     4|
     5|```typescript
     6|const stream = client.messages.stream({
     7|  model: "claude-opus-4-7",
     8|  max_tokens: 64000,
     9|  messages: [{ role: "user", content: "Write a story" }]
    10|});
    11|
    12|for await (const event of stream) {
    13|  if (
    14|    event.type === "content_block_delta" &&
    15|    event.delta.type === "text_delta"
    16|  ) {
    17|    process.stdout.write(event.delta.text);
    18|  }
    19|}
    20|```
    21|
    22|---
    23|
    24|## Handling Different Content Types
    25|
    26|> **Opus 4.7 / Opus 4.6:** Use `thinking: {type: "adaptive"}`. On older models, use `thinking: {type: "enabled", budget_tokens: N}` instead.
    27|
    28|```typescript
    29|const stream = client.messages.stream({
    30|  model: "claude-opus-4-7",
    31|  max_tokens: 64000,
    32|  thinking: { type: "adaptive" },
    33|  messages: [{ role: "user", content: "Analyze this problem" }]
    34|});
    35|
    36|for await (const event of stream) {
    37|  switch (event.type) {
    38|    case "content_block_start":
    39|      switch (event.content_block.type) {
    40|        case "thinking":
    41|          console.log("\n[Thinking...]");
    42|          break;
    43|        case "text":
    44|          console.log("\n[Response:]");
    45|          break;
    46|      }
    47|      break;
    48|    case "content_block_delta":
    49|      switch (event.delta.type) {
    50|        case "thinking_delta":
    51|          process.stdout.write(event.delta.thinking);
    52|          break;
    53|        case "text_delta":
    54|          process.stdout.write(event.delta.text);
    55|          break;
    56|      }
    57|      break;
    58|  }
    59|}
    60|```
    61|
    62|---
    63|
    64|## Streaming with Tool Use (Tool Runner)
    65|
    66|Use the tool runner with `stream: true`. The outer loop iterates over tool runner iterations (messages), the inner loop processes stream events:
    67|
    68|```typescript
    69|import Anthropic from "@anthropic-ai/sdk";
    70|import { betaZodTool } from "@anthropic-ai/sdk/helpers/beta/zod";
    71|import { z } from "zod";
    72|
    73|const client = new Anthropic();
    74|
    75|const getWeather = betaZodTool({
    76|  name: "get_weather",
    77|  description: "Get current weather for a location",
    78|  inputSchema: z.object({
    79|    location: z
    80|      .string()
    81|      .describe("City and state, e.g., San Francisco, CA")
    82|  }),
    83|  run: async ({ location }) => `72°F and sunny in ${location}`
    84|});
    85|
    86|const runner = client.beta.messages.toolRunner({
    87|  model: "claude-opus-4-7",
    88|  max_tokens: 64000,
    89|  tools: [getWeather],
    90|  messages: [
    91|    {
    92|      role: "user",
    93|      content: "What's the weather in Paris and London?"
    94|    }
    95|  ],
    96|  stream: true
    97|});
    98|
    99|// Outer loop: each tool runner iteration
   100|for await (const messageStream of runner) {
   101|  // Inner loop: stream events for this iteration
   102|  for await (const event of messageStream) {
   103|    switch (event.type) {
   104|      case "content_block_delta":
   105|        switch (event.delta.type) {
   106|          case "text_delta":
   107|            process.stdout.write(event.delta.text);
   108|            break;
   109|          case "input_json_delta":
   110|            // Tool input being streamed
   111|            break;
   112|        }
   113|        break;
   114|    }
   115|  }
   116|}
   117|```
   118|
   119|---
   120|
   121|## Getting the Final Message
   122|
   123|```typescript
   124|const stream = client.messages.stream({
   125|  model: "claude-opus-4-7",
   126|  max_tokens: 64000,
   127|  messages: [{ role: "user", content: "Hello" }]
   128|});
   129|
   130|for await (const event of stream) {
   131|  // Process events...
   132|}
   133|
   134|const finalMessage = await stream.finalMessage();
   135|console.log(`Tokens used: ${finalMessage.usage.output_tokens}`);
   136|```
   137|
   138|---
   139|
   140|## Stream Event Types
   141|
   142|| Event Type | Description | When it fires |
   143|| --- | --- | --- |
   144|| `message_start` | Contains message metadata | Once at the beginning |
   145|| `content_block_start` | New content block beginning | When a text/tool_use block starts |
   146|| `content_block_delta` | Incremental content update | For each token/chunk |
   147|| `content_block_stop` | Content block complete | When a block finishes |
   148|| `message_delta` | Message-level updates | Contains `stop_reason`, usage |
   149|| `message_stop` | Message complete | Once at the end |
   150|
   151|## Best Practices
   152|
   153|1. **Always flush output** — Use `process.stdout.write()` for immediate display
   154|2. **Handle partial responses** — If the stream is interrupted, you may have incomplete content
   155|3. **Track token usage** — The `message_delta` event contains usage information
   156|4. **Use `finalMessage()`** — Get the complete `Anthropic.Message` object even when streaming. Don't wrap `.on()` events in `new Promise()` — `finalMessage()` handles all completion/error/abort states internally
   157|5. **Buffer for web UIs** — Consider buffering a few tokens before rendering to avoid excessive DOM updates
   158|6. **Use `stream.on("text", ...)` for deltas** — The `text` event provides just the delta string, simpler than manually filtering `content_block_delta` events
   159|7. **For agentic loops with streaming** — See the [Streaming Manual Loop](./tool-use.md#streaming-manual-loop) section in tool-use.md for combining `stream()` + `finalMessage()` with a tool-use loop
   160|
   161|## Raw SSE Format
   162|
   163|If using raw HTTP (not SDKs), the stream returns Server-Sent Events:
   164|
   165|```
   166|event: message_start
   167|data: {"type":"message_start","message":{"id":"msg_...","type":"message",...}}
   168|
   169|event: content_block_start
   170|data: {"type":"content_block_start","index":0,"content_block":{"type":"text","text":""}}
   171|
   172|event: content_block_delta
   173|data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":"Hello"}}
   174|
   175|event: content_block_stop
   176|data: {"type":"content_block_stop","index":0}
   177|
   178|event: message_delta
   179|data: {"type":"message_delta","delta":{"stop_reason":"end_turn"},"usage":{"output_tokens":12}}
   180|
   181|event: message_stop
   182|data: {"type":"message_stop"}
   183|```
   184|