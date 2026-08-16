---
name: typescript-tool-use
description: "Tool Use — TypeScript"
version: 1.0.0
author: Alexa
---
     1|# Tool Use — TypeScript
     2|
     3|For conceptual overview (tool definitions, tool choice, tips), see [shared/tool-use-concepts.md](../../shared/tool-use-concepts.md).
     4|
     5|## Tool Runner (Recommended)
     6|
     7|**Beta:** The tool runner is in beta in the TypeScript SDK.
     8|
     9|Use `betaZodTool` with Zod schemas to define tools with a `run` function, then pass them to `client.beta.messages.toolRunner()`:
    10|
    11|```typescript
    12|import Anthropic from "@anthropic-ai/sdk";
    13|import { betaZodTool } from "@anthropic-ai/sdk/helpers/beta/zod";
    14|import { z } from "zod";
    15|
    16|const client = new Anthropic();
    17|
    18|const getWeather = betaZodTool({
    19|  name: "get_weather",
    20|  description: "Get current weather for a location",
    21|  inputSchema: z.object({
    22|    location: z
    23|      .string()
    24|      .describe("City and state, e.g., San Francisco, CA"),
    25|    unit: z.enum(["celsius", "fahrenheit"]).optional()
    26|  }),
    27|  run: async input => {
    28|    // Your implementation here
    29|    return `72°F and sunny in ${input.location}`;
    30|  }
    31|});
    32|
    33|// The tool runner handles the agentic loop and returns the final message
    34|const finalMessage = await client.beta.messages.toolRunner({
    35|  model: "claude-opus-4-7",
    36|  max_tokens: 16000,
    37|  tools: [getWeather],
    38|  messages: [
    39|    { role: "user", content: "What's the weather in Paris?" }
    40|  ]
    41|});
    42|
    43|console.log(finalMessage.content);
    44|```
    45|
    46|**Key benefits of the tool runner:**
    47|
    48|- No manual loop — the SDK handles calling tools and feeding results back
    49|- Type-safe tool inputs via Zod schemas
    50|- Tool schemas are generated automatically from Zod definitions
    51|- Iteration stops automatically when Claude has no more tool calls
    52|
    53|---
    54|
    55|## Manual Agentic Loop
    56|
    57|Use this when you need fine-grained control (custom logging, conditional tool execution, streaming individual iterations, human-in-the-loop approval):
    58|
    59|```typescript
    60|import Anthropic from "@anthropic-ai/sdk";
    61|
    62|const client = new Anthropic();
    63|const tools: Anthropic.Tool[] = [...]; // Your tool definitions
    64|let messages: Anthropic.MessageParam[] = [{ role: "user", content: userInput }];
    65|
    66|while (true) {
    67|  const response = await client.messages.create({
    68|    model: "claude-opus-4-7",
    69|    max_tokens: 16000,
    70|    tools: tools,
    71|    messages: messages,
    72|  });
    73|
    74|  if (response.stop_reason === "end_turn") break;
    75|
    76|  // Server-side tool hit iteration limit; append assistant turn and re-send to continue
    77|  if (response.stop_reason === "pause_turn") {
    78|    messages.push({ role: "assistant", content: response.content });
    79|    continue;
    80|  }
    81|
    82|  const toolUseBlocks = response.content.filter(
    83|    (b): b is Anthropic.ToolUseBlock => b.type === "tool_use",
    84|  );
    85|
    86|  messages.push({ role: "assistant", content: response.content });
    87|
    88|  const toolResults: Anthropic.ToolResultBlockParam[] = [];
    89|  for (const tool of toolUseBlocks) {
    90|    const result = await executeTool(tool.name, tool.input);
    91|    toolResults.push({
    92|      type: "tool_result",
    93|      tool_use_id: tool.id,
    94|      content: result,
    95|    });
    96|  }
    97|
    98|  messages.push({ role: "user", content: toolResults });
    99|}
   100|```
   101|
   102|### Streaming Manual Loop
   103|
   104|Use `client.messages.stream()` + `finalMessage()` instead of `.create()` when you need streaming within a manual loop. Text deltas are streamed on each iteration; `finalMessage()` collects the complete `Message` so you can inspect `stop_reason` and extract tool-use blocks:
   105|
   106|```typescript
   107|import Anthropic from "@anthropic-ai/sdk";
   108|
   109|const client = new Anthropic();
   110|const tools: Anthropic.Tool[] = [...];
   111|let messages: Anthropic.MessageParam[] = [{ role: "user", content: userInput }];
   112|
   113|while (true) {
   114|  const stream = client.messages.stream({
   115|    model: "claude-opus-4-7",
   116|    max_tokens: 64000,
   117|    tools,
   118|    messages,
   119|  });
   120|
   121|  // Stream text deltas on each iteration
   122|  stream.on("text", (delta) => {
   123|    process.stdout.write(delta);
   124|  });
   125|
   126|  // finalMessage() resolves with the complete Message — no need to
   127|  // manually wire up .on("message") / .on("error") / .on("abort")
   128|  const message = await stream.finalMessage();
   129|
   130|  if (message.stop_reason === "end_turn") break;
   131|
   132|  // Server-side tool hit iteration limit; append assistant turn and re-send to continue
   133|  if (message.stop_reason === "pause_turn") {
   134|    messages.push({ role: "assistant", content: message.content });
   135|    continue;
   136|  }
   137|
   138|  const toolUseBlocks = message.content.filter(
   139|    (b): b is Anthropic.ToolUseBlock => b.type === "tool_use",
   140|  );
   141|
   142|  messages.push({ role: "assistant", content: message.content });
   143|
   144|  const toolResults: Anthropic.ToolResultBlockParam[] = [];
   145|  for (const tool of toolUseBlocks) {
   146|    const result = await executeTool(tool.name, tool.input);
   147|    toolResults.push({
   148|      type: "tool_result",
   149|      tool_use_id: tool.id,
   150|      content: result,
   151|    });
   152|  }
   153|
   154|  messages.push({ role: "user", content: toolResults });
   155|}
   156|```
   157|
   158|> **Important:** Don't wrap `.on()` events in `new Promise()` to collect the final message — use `stream.finalMessage()` instead. The SDK handles all error/abort/completion states internally.
   159|
   160|> **Error handling in the loop:** Use the SDK's typed exceptions (e.g., `Anthropic.RateLimitError`, `Anthropic.APIError`) — see [Error Handling](./README.md#error-handling) for examples. Don't check error messages with string matching.
   161|
   162|> **SDK types:** Use `Anthropic.MessageParam`, `Anthropic.Tool`, `Anthropic.ToolUseBlock`, `Anthropic.ToolResultBlockParam`, `Anthropic.Message`, etc. for all API-related data structures. Don't redefine equivalent interfaces.
   163|
   164|---
   165|
   166|## Handling Tool Results
   167|
   168|```typescript
   169|const response = await client.messages.create({
   170|  model: "claude-opus-4-7",
   171|  max_tokens: 16000,
   172|  tools: tools,
   173|  messages: [
   174|    { role: "user", content: "What's the weather in Paris?" }
   175|  ]
   176|});
   177|
   178|for (const block of response.content) {
   179|  if (block.type === "tool_use") {
   180|    const result = await executeTool(block.name, block.input);
   181|
   182|    const followup = await client.messages.create({
   183|      model: "claude-opus-4-7",
   184|      max_tokens: 16000,
   185|      tools: tools,
   186|      messages: [
   187|        { role: "user", content: "What's the weather in Paris?" },
   188|        { role: "assistant", content: response.content },
   189|        {
   190|          role: "user",
   191|          content: [
   192|            {
   193|              type: "tool_result",
   194|              tool_use_id: block.id,
   195|              content: result
   196|            }
   197|          ]
   198|        }
   199|      ]
   200|    });
   201|  }
   202|}
   203|```
   204|
   205|---
   206|
   207|## Tool Choice
   208|
   209|```typescript
   210|const response = await client.messages.create({
   211|  model: "claude-opus-4-7",
   212|  max_tokens: 16000,
   213|  tools: tools,
   214|  tool_choice: { type: "tool", name: "get_weather" },
   215|  messages: [
   216|    { role: "user", content: "What's the weather in Paris?" }
   217|  ]
   218|});
   219|```
   220|
   221|---
   222|
   223|## Server-Side Tools
   224|
   225|Version-suffixed `type` literals; `name` is fixed per interface. Pass plain object literals — the `ToolUnion` type is satisfied structurally. **The `name`/`type` pair must match the interface**: mixing `str_replace_based_edit_tool` (20250728 name) with `text_editor_20250124` (which expects `str_replace_editor`) is a TS2322.
   226|
   227|**Don't type-annotate as `Tool[]`** — `Tool` is just the custom-tool variant. Let structural typing infer from the `tools` param, or annotate as `Anthropic.Messages.ToolUnion[]` if you must:
   228|
   229|```typescript
   230|// ✓ let inference work — no annotation
   231|const response = await client.messages.create({
   232|  model: "claude-opus-4-7",
   233|  max_tokens: 16000,
   234|  tools: [
   235|    {
   236|      type: "text_editor_20250728",
   237|      name: "str_replace_based_edit_tool"
   238|    },
   239|    { type: "bash_20250124", name: "bash" },
   240|    { type: "web_search_20260209", name: "web_search" },
   241|    { type: "code_execution_20260120", name: "code_execution" }
   242|  ],
   243|  messages: [{ role: "user", content: "..." }]
   244|});
   245|
   246|// ✗ this is a TS2352 — Tool is the CUSTOM tool variant only
   247|// const tools: Anthropic.Tool[] = [{ type: "text_editor_20250728", ... }]
   248|```
   249|
   250|| Interface | `name` | `type` |
   251|| --- | --- | --- |
   252|| `ToolTextEditor20250124` | `str_replace_editor` | `text_editor_20250124` |
   253|| `ToolTextEditor20250429` | `str_replace_based_edit_tool` | `text_editor_20250429` |
   254|| `ToolTextEditor20250728` | `str_replace_based_edit_tool` | `text_editor_20250728` |
   255|| `ToolBash20250124` | `bash` | `bash_20250124` |
   256|| `WebSearchTool20260209` | `web_search` | `web_search_20260209` |
   257|| `WebFetchTool20260209` | `web_fetch` | `web_fetch_20260209` |
   258|| `CodeExecutionTool20260120` | `code_execution` | `code_execution_20260120` |
   259|
   260|**Don't mix beta and non-beta types**: if you call `client.beta.messages.create()`, the response `content` is `BetaContentBlock[]` — you cannot pass that to a non-beta `ContentBlockParam[]` without narrowing each element.
   261|
   262|---
   263|
   264|## Code Execution
   265|
   266|### Basic Usage
   267|
   268|```typescript
   269|import Anthropic from "@anthropic-ai/sdk";
   270|
   271|const client = new Anthropic();
   272|
   273|const response = await client.messages.create({
   274|  model: "claude-opus-4-7",
   275|  max_tokens: 16000,
   276|  messages: [
   277|    {
   278|      role: "user",
   279|      content:
   280|        "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
   281|    }
   282|  ],
   283|  tools: [{ type: "code_execution_20260120", name: "code_execution" }]
   284|});
   285|```
   286|
   287|### Reading Local Files (ESM note)
   288|
   289|`__dirname` doesn't exist in ES modules. For script-relative paths use `import.meta.url`:
   290|
   291|```typescript
   292|import { readFileSync } from "fs";
   293|import { fileURLToPath } from "url";
   294|import { dirname, join } from "path";
   295|
   296|const __dirname = dirname(fileURLToPath(import.meta.url));
   297|const pdfBytes = readFileSync(join(__dirname, "sample.pdf"));
   298|```
   299|
   300|Or use a CWD-relative path if the script runs from a known directory: `readFileSync("./sample.pdf")`.
   301|
   302|### Upload Files for Analysis
   303|
   304|```typescript
   305|import Anthropic, { toFile } from "@anthropic-ai/sdk";
   306|import { createReadStream } from "fs";
   307|
   308|const client = new Anthropic();
   309|
   310|// 1. Upload a file
   311|const uploaded = await client.beta.files.upload({
   312|  file: await toFile(createReadStream("sales_data.csv"), undefined, {
   313|    type: "text/csv"
   314|  }),
   315|  betas: ["files-api-2025-04-14"]
   316|});
   317|
   318|// 2. Pass to code execution
   319|// Code execution is GA; Files API is still beta (pass via RequestOptions)
   320|const response = await client.messages.create(
   321|  {
   322|    model: "claude-opus-4-7",
   323|    max_tokens: 16000,
   324|    messages: [
   325|      {
   326|        role: "user",
   327|        content: [
   328|          {
   329|            type: "text",
   330|            text: "Analyze this sales data. Show trends and create a visualization."
   331|          },
   332|          { type: "container_upload", file_id: uploaded.id }
   333|        ]
   334|      }
   335|    ],
   336|    tools: [
   337|      { type: "code_execution_20260120", name: "code_execution" }
   338|    ]
   339|  },
   340|  { headers: { "anthropic-beta": "files-api-2025-04-14" } }
   341|);
   342|```
   343|
   344|### Retrieve Generated Files
   345|
   346|```typescript
   347|import path from "path";
   348|import fs from "fs";
   349|
   350|const OUTPUT_DIR = "./claude_outputs";
   351|await fs.promises.mkdir(OUTPUT_DIR, { recursive: true });
   352|
   353|for (const block of response.content) {
   354|  if (block.type === "bash_code_execution_tool_result") {
   355|    const result = block.content;
   356|    if (
   357|      result.type === "bash_code_execution_result" &&
   358|      result.content
   359|    ) {
   360|      for (const fileRef of result.content) {
   361|        if (fileRef.type === "bash_code_execution_output") {
   362|          const metadata = await client.beta.files.retrieveMetadata(
   363|            fileRef.file_id
   364|          );
   365|          const downloadResponse = await client.beta.files.download(
   366|            fileRef.file_id
   367|          );
   368|          const fileBytes = Buffer.from(
   369|            await downloadResponse.arrayBuffer()
   370|          );
   371|          const safeName = path.basename(metadata.filename);
   372|          if (!safeName || safeName === "." || safeName === "..") {
   373|            console.warn(
   374|              `Skipping invalid filename: ${metadata.filename}`
   375|            );
   376|            continue;
   377|          }
   378|          const outputPath = path.join(OUTPUT_DIR, safeName);
   379|          await fs.promises.writeFile(outputPath, fileBytes);
   380|          console.log(`Saved: ${outputPath}`);
   381|        }
   382|      }
   383|    }
   384|  }
   385|}
   386|```
   387|
   388|### Container Reuse
   389|
   390|```typescript
   391|// First request: set up environment
   392|const response1 = await client.messages.create({
   393|  model: "claude-opus-4-7",
   394|  max_tokens: 16000,
   395|  messages: [
   396|    {
   397|      role: "user",
   398|      content:
   399|        "Install tabulate and create data.json with sample user data"
   400|    }
   401|  ],
   402|  tools: [{ type: "code_execution_20260120", name: "code_execution" }]
   403|});
   404|
   405|// Reuse container
   406|// container is nullable — set only when using server-side code execution
   407|const containerId = response1.container!.id;
   408|
   409|const response2 = await client.messages.create({
   410|  container: containerId,
   411|  model: "claude-opus-4-7",
   412|  max_tokens: 16000,
   413|  messages: [
   414|    {
   415|      role: "user",
   416|      content: "Read data.json and display as a formatted table"
   417|    }
   418|  ],
   419|  tools: [{ type: "code_execution_20260120", name: "code_execution" }]
   420|});
   421|```
   422|
   423|---
   424|
   425|## Memory Tool
   426|
   427|### Basic Usage
   428|
   429|```typescript
   430|const response = await client.messages.create({
   431|  model: "claude-opus-4-7",
   432|  max_tokens: 16000,
   433|  messages: [
   434|    {
   435|      role: "user",
   436|      content: "Remember that my preferred language is TypeScript."
   437|    }
   438|  ],
   439|  tools: [{ type: "memory_20250818", name: "memory" }]
   440|});
   441|```
   442|
   443|### SDK Memory Helper
   444|
   445|Use `betaMemoryTool` with a `MemoryToolHandlers` implementation:
   446|
   447|```typescript
   448|import {
   449|  betaMemoryTool,
   450|  type MemoryToolHandlers,
   451|} from "@anthropic-ai/sdk/helpers/beta/memory";
   452|
   453|const handlers: MemoryToolHandlers = {
   454|  async view(command) { ... },
   455|  async create(command) { ... },
   456|  async str_replace(command) { ... },
   457|  async insert(command) { ... },
   458|  async delete(command) { ... },
   459|  async rename(command) { ... },
   460|};
   461|
   462|const memory = betaMemoryTool(handlers);
   463|
   464|const runner = client.beta.messages.toolRunner({
   465|  model: "claude-opus-4-7",
   466|  max_tokens: 16000,
   467|  tools: [memory],
   468|  messages: [{ role: "user", content: "Remember my preferences" }],
   469|});
   470|
   471|for await (const message of runner) {
   472|  console.log(message);
   473|}
   474|```
   475|
   476|For full implementation examples, use WebFetch:
   477|
   478|- `https://github.com/anthropics/anthropic-sdk-typescript/blob/main/examples/tools-helpers-memory.ts`
   479|
   480|---
   481|
   482|## Structured Outputs
   483|
   484|### JSON Outputs (Zod — Recommended)
   485|
   486|```typescript
   487|import Anthropic from "@anthropic-ai/sdk";
   488|import { z } from "zod";
   489|import { zodOutputFormat } from "@anthropic-ai/sdk/helpers/zod";
   490|
   491|const ContactInfoSchema = z.object({
   492|  name: z.string(),
   493|  email: z.string(),
   494|  plan: z.string(),
   495|  interests: z.array(z.string()),
   496|  demo_requested: z.boolean()
   497|});
   498|
   499|const client = new Anthropic();
   500|
   501|