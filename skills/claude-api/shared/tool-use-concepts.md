---
name: shared-tool-use-concepts
description: "Tool Use Concepts"
version: 1.0.0
author: Alexa
---
     1|# Tool Use Concepts
     2|
     3|This file covers the conceptual foundations of tool use with the Claude API. For language-specific code examples, see the `python/`, `typescript/`, or other language folders. For decision heuristics on which tools to expose, how to manage context in long-running agents, and caching strategy, see `agent-design.md`.
     4|
     5|## User-Defined Tools
     6|
     7|### Tool Definition Structure
     8|
     9|> **Note:** When using the Tool Runner (beta), tool schemas are generated automatically from your function signatures (Python), Zod schemas (TypeScript), annotated classes (Java), `jsonschema` struct tags (Go), or `BaseTool` subclasses (Ruby). The raw JSON schema format below is for the manual approach — including PHP's `BetaRunnableTool`, which wraps a run closure around a hand-written schema — or SDKs without tool runner support.
    10|
    11|Each tool requires a name, description, and JSON Schema for its inputs:
    12|
    13|```json
    14|{
    15|  "description": "Get current weather for a location",
    16|  "input_schema": {
    17|    "type": "object",
    18|    "properties": {
    19|      "location": {
    20|        "type": "string",
    21|        "description": "City and state, e.g., San Francisco, CA"
    22|      },
    23|      "unit": {
    24|        "type": "string",
    25|        "enum": ["celsius", "fahrenheit"],
    26|        "description": "Temperature unit"
    27|      }
    28|    },
    29|    "required": ["location"]
    30|  },
    31|  "name": "get_weather"
    32|}
    33|```
    34|
    35|**Best practices for tool definitions:**
    36|
    37|- Use clear, descriptive names (e.g., `get_weather`, `search_database`, `send_email`)
    38|- Write detailed descriptions — Claude uses these to decide when to use the tool
    39|- Include descriptions for each property
    40|- Use `enum` for parameters with a fixed set of values
    41|- Mark truly required parameters in `required`; make others optional with defaults
    42|
    43|---
    44|
    45|### Tool Choice Options
    46|
    47|Control when Claude uses tools:
    48|
    49|| Value | Behavior |
    50|| --- | --- |
    51|| `{"type": "auto"}` | Claude decides whether to use tools (default) |
    52|| `{"type": "any"}` | Claude must use at least one tool |
    53|| `{"type": "tool", "name": "..."}` | Claude must use the specified tool |
    54|| `{"type": "none"}` | Claude cannot use tools |
    55|
    56|Any `tool_choice` value can also include `"disable_parallel_tool_use": true` to force Claude to use at most one tool per response. By default, Claude may request multiple tool calls in a single response.
    57|
    58|---
    59|
    60|### Tool Runner vs Manual Loop
    61|
    62|**Tool Runner (Recommended):** The SDK's tool runner handles the agentic loop automatically — it calls the API, detects tool use requests, executes your tool functions, feeds results back to Claude, and repeats until Claude stops calling tools. Available in Python, TypeScript, Java, Go, Ruby, and PHP SDKs (beta). The Python SDK also provides MCP conversion helpers (`anthropic.lib.tools.mcp`) to convert MCP tools, prompts, and resources for use with the tool runner — see `python/claude-api/tool-use.md` for details.
    63|
    64|**Manual Agentic Loop:** Use when you need fine-grained control over the loop (e.g., custom logging, conditional tool execution, human-in-the-loop approval). Loop until `stop_reason == "end_turn"`, always append the full `response.content` to preserve tool_use blocks, and ensure each `tool_result` includes the matching `tool_use_id`.
    65|
    66|**Stop reasons for server-side tools:** When using server-side tools (code execution, web search, etc.), the API runs a server-side sampling loop. If this loop reaches its default limit of 10 iterations, the response will have `stop_reason: "pause_turn"`. To continue, re-send the user message and assistant response and make another API request — the server will resume where it left off. Do NOT add an extra user message like "Continue." — the API detects the trailing `server_tool_use` block and knows to resume automatically.
    67|
    68|```python
    69|# Handle pause_turn in your agentic loop
    70|if response.stop_reason == "pause_turn":
    71|    messages = [
    72|        {"role": "user", "content": user_query},
    73|        {"role": "assistant", "content": response.content},
    74|    ]
    75|    # Make another API request — server resumes automatically
    76|    response = client.messages.create(
    77|        model="claude-opus-4-7", messages=messages, tools=tools
    78|    )
    79|```
    80|
    81|Set a `max_continuations` limit (e.g., 5) to prevent infinite loops. For the full guide, see: `https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons`
    82|
    83|> **Security:** The tool runner executes your tool functions automatically whenever Claude requests them. For tools with side effects (sending emails, modifying databases, financial transactions), validate inputs within your tool functions and consider requiring confirmation for destructive operations. Use the manual agentic loop if you need human-in-the-loop approval before each tool execution.
    84|
    85|---
    86|
    87|### Handling Tool Results
    88|
    89|When Claude uses a tool, the response contains a `tool_use` block. You must:
    90|
    91|1. Execute the tool with the provided input
    92|2. Send the result back in a `tool_result` message
    93|3. Continue the conversation
    94|
    95|**Error handling in tool results:** When a tool execution fails, set `"is_error": true` and provide an informative error message. Claude will typically acknowledge the error and either try a different approach or ask for clarification.
    96|
    97|**Multiple tool calls:** Claude can request multiple tools in a single response. Handle them all before continuing — send all results back in a single `user` message.
    98|
    99|---
   100|
   101|## Server-Side Tools: Code Execution
   102|
   103|The code execution tool lets Claude run code in a secure, sandboxed container. Unlike user-defined tools, server-side tools run on Anthropic's infrastructure — you don't execute anything client-side. Just include the tool definition and Claude handles the rest.
   104|
   105|### Key Facts
   106|
   107|- Runs in an isolated container (1 CPU, 5 GiB RAM, 5 GiB disk)
   108|- No internet access (fully sandboxed)
   109|- Python 3.11 with data science libraries pre-installed
   110|- Containers persist for 30 days and can be reused across requests
   111|- Free when used with web search/web fetch tools; otherwise $0.05/hour after 1,550 free hours/month per organization
   112|
   113|### Tool Definition
   114|
   115|The tool requires no schema — just declare it in the `tools` array:
   116|
   117|```json
   118|{
   119|  "name": "code_execution",
   120|  "type": "code_execution_20260120"
   121|}
   122|```
   123|
   124|Claude automatically gains access to `bash_code_execution` (run shell commands) and `text_editor_code_execution` (create/view/edit files).
   125|
   126|### Pre-installed Python Libraries
   127|
   128|- **Data science**: pandas, numpy, scipy, scikit-learn, statsmodels
   129|- **Visualization**: matplotlib, seaborn
   130|- **File processing**: openpyxl, xlsxwriter, pillow, pypdf, pdfplumber, python-docx, python-pptx
   131|- **Math**: sympy, mpmath
   132|- **Utilities**: tqdm, python-dateutil, pytz, sqlite3
   133|
   134|Additional packages can be installed at runtime via `pip install`.
   135|
   136|### Supported File Types for Upload
   137|
   138|| Type   | Extensions                         |
   139|| ------ | ---------------------------------- |
   140|| Data   | CSV, Excel (.xlsx/.xls), JSON, XML |
   141|| Images | JPEG, PNG, GIF, WebP               |
   142|| Text   | .txt, .md, .py, .js, etc.          |
   143|
   144|### Container Reuse
   145|
   146|Reuse containers across requests to maintain state (files, installed packages, variables). Extract the `container_id` from the first response and pass it to subsequent requests.
   147|
   148|### Response Structure
   149|
   150|The response contains interleaved text and tool result blocks:
   151|
   152|- `text` — Claude's explanation
   153|- `server_tool_use` — What Claude is doing
   154|- `bash_code_execution_tool_result` — Code execution output (check `return_code` for success/failure)
   155|- `text_editor_code_execution_tool_result` — File operation results
   156|
   157|> **Security:** Always sanitize filenames with `os.path.basename()` / `path.basename()` before writing downloaded files to disk to prevent path traversal attacks. Write files to a dedicated output directory.
   158|
   159|---
   160|
   161|## Server-Side Tools: Web Search and Web Fetch
   162|
   163|Web search and web fetch let Claude search the web and retrieve page content. They run server-side — just include the tool definitions and Claude handles queries, fetching, and result processing automatically.
   164|
   165|### Tool Definitions
   166|
   167|```json
   168|[
   169|  { "type": "web_search_20260209", "name": "web_search" },
   170|  { "type": "web_fetch_20260209", "name": "web_fetch" }
   171|]
   172|```
   173|
   174|### Dynamic Filtering (Opus 4.7 / Opus 4.6 / Sonnet 4.6)
   175|
   176|The `web_search_20260209` and `web_fetch_20260209` versions support **dynamic filtering** — Claude writes and executes code to filter search results before they reach the context window, improving accuracy and token efficiency. Dynamic filtering is built into these tool versions and activates automatically; you do not need to separately declare the `code_execution` tool or pass any beta header.
   177|
   178|```json
   179|{
   180|  "tools": [
   181|    { "type": "web_search_20260209", "name": "web_search" },
   182|    { "type": "web_fetch_20260209", "name": "web_fetch" }
   183|  ]
   184|}
   185|```
   186|
   187|Without dynamic filtering, the previous `web_search_20250305` version is also available.
   188|
   189|> **Note:** Only include the standalone `code_execution` tool when your application needs code execution for its own purposes (data analysis, file processing, visualization) independent of web search. Including it alongside `_20260209` web tools creates a second execution environment that can confuse the model.
   190|
   191|---
   192|
   193|## Server-Side Tools: Programmatic Tool Calling
   194|
   195|With standard tool use, each tool call is a round trip: Claude calls, the result enters Claude's context, Claude reasons, then calls the next tool. Chained calls accumulate latency and tokens — most of that intermediate data is never needed again.
   196|
   197|Programmatic tool calling lets Claude compose those calls into a script. The script runs in the code execution container; when it invokes a tool, the container pauses, the call executes, and the result returns to the running code (not to Claude's context). The script processes it with normal control flow. Only the final output returns to Claude. Use it when chaining many tool calls or when intermediate results are large and should be filtered before reaching the context window.
   198|
   199|For full documentation, use WebFetch:
   200|
   201|- URL: `https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling`
   202|
   203|---
   204|
   205|## Server-Side Tools: Tool Search
   206|
   207|The tool search tool lets Claude dynamically discover tools from large libraries without loading all definitions into the context window. Use it when you have many tools but only a few are relevant to any given request. Discovered tool schemas are appended to the request, not swapped in — this preserves the prompt cache (see `agent-design.md` §Caching for Agents).
   208|
   209|For full documentation, use WebFetch:
   210|
   211|- URL: `https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool`
   212|
   213|---
   214|
   215|## Skills
   216|
   217|Skills package task-specific instructions that Claude loads only when relevant. Each skill is a folder containing a `SKILL.md` file. The skill's short description sits in context by default; Claude reads the full file when the current task calls for it. Use skills to keep specialized instructions out of the base system prompt without losing discoverability.
   218|
   219|For full documentation, use WebFetch:
   220|
   221|- URL: `https://platform.claude.com/docs/en/agents-and-tools/skills`
   222|
   223|---
   224|
   225|## Tool Use Examples
   226|
   227|You can provide sample tool calls directly in your tool definitions to demonstrate usage patterns and reduce parameter errors. This helps Claude understand how to correctly format tool inputs, especially for tools with complex schemas.
   228|
   229|For full documentation, use WebFetch:
   230|
   231|- URL: `https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use`
   232|
   233|---
   234|
   235|## Server-Side Tools: Computer Use
   236|
   237|Computer use lets Claude interact with a desktop environment (screenshots, mouse, keyboard). It can be Anthropic-hosted (server-side, like code execution) or self-hosted (you provide the environment and execute actions client-side).
   238|
   239|For full documentation, use WebFetch:
   240|
   241|- URL: `https://platform.claude.com/docs/en/agents-and-tools/computer-use/overview`
   242|
   243|---
   244|
   245|## Context Editing
   246|
   247|Context editing clears stale tool results and thinking blocks from the transcript as a long-running agent accumulates turns. Unlike compaction (which summarizes), context editing prunes — the cleared content is removed, not replaced. Use it when old tool outputs are no longer relevant and you want to keep the transcript lean without losing the conversation structure. Thresholds for what to clear are configurable.
   248|
   249|For full documentation, use WebFetch:
   250|
   251|- URL: `https://platform.claude.com/docs/en/build-with-claude/context-editing`
   252|
   253|---
   254|
   255|## Client-Side Tools: Memory
   256|
   257|The memory tool enables Claude to store and retrieve information across conversations through a memory file directory. Claude can create, read, update, and delete files that persist between sessions.
   258|
   259|### Key Facts
   260|
   261|- Client-side tool — you control storage via your implementation
   262|- Supports commands: `view`, `create`, `str_replace`, `insert`, `delete`, `rename`
   263|- Operates on files in a `/memories` directory
   264|- The Python, TypeScript, and Java SDKs provide helper classes/functions for implementing the memory backend
   265|
   266|> **Security:** Never store API keys, passwords, tokens, or other secrets in memory files. Be cautious with personally identifiable information (PII) — check data privacy regulations (GDPR, CCPA) before persisting user data. The reference implementations have no built-in access control; in multi-user systems, implement per-user memory directories and authentication in your tool handlers.
   267|
   268|For full implementation examples, use WebFetch:
   269|
   270|- Docs: `https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool.md`
   271|
   272|---
   273|
   274|## Structured Outputs
   275|
   276|Structured outputs constrain Claude's responses to follow a specific JSON schema, guaranteeing valid, parseable output. This is not a separate tool — it enhances the Messages API response format and/or tool parameter validation.
   277|
   278|Two features are available:
   279|
   280|- **JSON outputs** (`output_config.format`): Control Claude's response format
   281|- **Strict tool use** (`strict: true`): Guarantee valid tool parameter schemas
   282|
   283|**Supported models:** Claude Opus 4.7, Claude Sonnet 4.6, and Claude Haiku 4.5. Legacy models (Claude Opus 4.5, Claude Opus 4.1) also support structured outputs.
   284|
   285|> **Recommended:** Use `client.messages.parse()` which automatically validates responses against your schema. When using `messages.create()` directly, use `output_config: {format: {...}}`. The `output_format` convenience parameter is also accepted by some SDK methods (e.g., `.parse()`), but `output_config.format` is the canonical API-level parameter.
   286|
   287|### JSON Schema Limitations
   288|
   289|**Supported:**
   290|
   291|- Basic types: object, array, string, integer, number, boolean, null
   292|- `enum`, `const`, `anyOf`, `allOf`, `$ref`/`$def`
   293|- String formats: `date-time`, `time`, `date`, `duration`, `email`, `hostname`, `uri`, `ipv4`, `ipv6`, `uuid`
   294|- `additionalProperties: false` (required for all objects)
   295|
   296|**Not supported:**
   297|
   298|- Recursive schemas
   299|- Numerical constraints (`minimum`, `maximum`, `multipleOf`)
   300|- String constraints (`minLength`, `maxLength`)
   301|- Complex array constraints
   302|- `additionalProperties` set to anything other than `false`
   303|
   304|The Python and TypeScript SDKs automatically handle unsupported constraints by removing them from the schema sent to the API and validating them client-side.
   305|
   306|### Important Notes
   307|
   308|- **First request latency**: New schemas incur a one-time compilation cost. Subsequent requests with the same schema use a 24-hour cache.
   309|- **Refusals**: If Claude refuses for safety reasons (`stop_reason: "refusal"`), the output may not match your schema.
   310|- **Token limits**: If `stop_reason: "max_tokens"`, output may be incomplete. Increase `max_tokens`.
   311|- **Incompatible with**: Citations (returns 400 error), message prefilling.
   312|- **Works with**: Batches API, streaming, token counting, extended thinking.
   313|
   314|---
   315|
   316|## Tips for Effective Tool Use
   317|
   318|1. **Provide detailed descriptions**: Claude relies heavily on descriptions to understand when and how to use tools
   319|2. **Use specific tool names**: `get_current_weather` is better than `weather`
   320|3. **Validate inputs**: Always validate tool inputs before execution
   321|4. **Handle errors gracefully**: Return informative error messages so Claude can adapt
   322|5. **Limit tool count**: Too many tools can confuse the model — keep the set focused
   323|6. **Test tool interactions**: Verify Claude uses tools correctly in various scenarios
   324|
   325|For detailed tool use documentation, use WebFetch:
   326|
   327|- URL: `https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview`
   328|