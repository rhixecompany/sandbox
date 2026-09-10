---
name: claude-api-tool-use
description: "Tool Use — Python"
version: 1.0.0
author: Alexa
---
     1|# Tool Use — Python
     2|
     3|For conceptual overview (tool definitions, tool choice, tips), see [shared/tool-use-concepts.md](../../shared/tool-use-concepts.md).
     4|
     5|## Tool Runner (Recommended)
     6|
     7|**Beta:** The tool runner is in beta in the Python SDK.
     8|
     9|Use the `@beta_tool` decorator to define tools as typed functions, then pass them to `client.beta.messages.tool_runner()`:
    10|
    11|```python
    12|import anthropic
    13|from anthropic import beta_tool
    14|
    15|client = anthropic.Anthropic()
    16|
    17|@beta_tool
    18|def get_weather(location: str, unit: str = "celsius") -> str:
    19|    """Get current weather for a location.
    20|
    21|    Args:
    22|        location: City and state, e.g., San Francisco, CA.
    23|        unit: Temperature unit, either "celsius" or "fahrenheit".
    24|    """
    25|    # Your implementation here
    26|    return f"72°F and sunny in {location}"
    27|
    28|# The tool runner handles the agentic loop automatically
    29|runner = client.beta.messages.tool_runner(
    30|    model="claude-opus-4-7",
    31|    max_tokens=16000,
    32|    tools=[get_weather],
    33|    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    34|)
    35|
    36|# Each iteration yields a BetaMessage; iteration stops when Claude is done
    37|for message in runner:
    38|    print(message)
    39|```
    40|
    41|For async usage, use `@beta_async_tool` with `async def` functions.
    42|
    43|**Key benefits of the tool runner:**
    44|
    45|- No manual loop — the SDK handles calling tools and feeding results back
    46|- Type-safe tool inputs via decorators
    47|- Tool schemas are generated automatically from function signatures
    48|- Iteration stops automatically when Claude has no more tool calls
    49|
    50|---
    51|
    52|## MCP Tool Conversion Helpers
    53|
    54|**Beta.** Convert [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) tools, prompts, and resources to Anthropic API types for use with the tool runner. Requires `pip install anthropic[mcp]` (Python 3.10+).
    55|
    56|> **Note:** The Claude API also supports an `mcp_servers` parameter that lets Claude connect directly to remote MCP servers. Use these helpers instead when you need local MCP servers, prompts, resources, or more control over the MCP connection.
    57|
    58|### MCP Tools with Tool Runner
    59|
    60|```python
    61|from anthropic import AsyncAnthropic
    62|from anthropic.lib.tools.mcp import async_mcp_tool
    63|from mcp import ClientSession
    64|from mcp.client.stdio import stdio_client, StdioServerParameters
    65|
    66|client = AsyncAnthropic()
    67|
    68|async with stdio_client(StdioServerParameters(command="mcp-server")) as (read, write):
    69|    async with ClientSession(read, write) as mcp_client:
    70|        await mcp_client.initialize()
    71|
    72|        tools_result = await mcp_client.list_tools()
    73|        # tool_runner is sync — returns the runner, not a coroutine
    74|        runner = client.beta.messages.tool_runner(
    75|            model="claude-opus-4-7",
    76|            max_tokens=16000,
    77|            messages=[{"role": "user", "content": "Use the available tools"}],
    78|            tools=[async_mcp_tool(t, mcp_client) for t in tools_result.tools],
    79|        )
    80|        async for message in runner:
    81|            print(message)
    82|```
    83|
    84|For sync usage, use `mcp_tool` instead of `async_mcp_tool`.
    85|
    86|### MCP Prompts
    87|
    88|```python
    89|from anthropic.lib.tools.mcp import mcp_message
    90|
    91|prompt = await mcp_client.get_prompt(name="my-prompt")
    92|response = await client.beta.messages.create(
    93|    model="claude-opus-4-7",
    94|    max_tokens=16000,
    95|    messages=[mcp_message(m) for m in prompt.messages],
    96|)
    97|```
    98|
    99|### MCP Resources as Content
   100|
   101|```python
   102|from anthropic.lib.tools.mcp import mcp_resource_to_content
   103|
   104|resource = await mcp_client.read_resource(uri="file:///path/to/doc.txt")
   105|response = await client.beta.messages.create(
   106|    model="claude-opus-4-7",
   107|    max_tokens=16000,
   108|    messages=[{
   109|        "role": "user",
   110|        "content": [
   111|            mcp_resource_to_content(resource),
   112|            {"type": "text", "text": "Summarize this document"},
   113|        ],
   114|    }],
   115|)
   116|```
   117|
   118|### Upload MCP Resources as Files
   119|
   120|```python
   121|from anthropic.lib.tools.mcp import mcp_resource_to_file
   122|
   123|resource = await mcp_client.read_resource(uri="file:///path/to/data.json")
   124|uploaded = await client.beta.files.upload(file=mcp_resource_to_file(resource))
   125|```
   126|
   127|Conversion functions raise `UnsupportedMCPValueError` if an MCP value cannot be converted (e.g., unsupported content types like audio, unsupported MIME types).
   128|
   129|---
   130|
   131|## Manual Agentic Loop
   132|
   133|Use this when you need fine-grained control over the loop (e.g., custom logging, conditional tool execution, human-in-the-loop approval):
   134|
   135|```python
   136|import anthropic
   137|
   138|client = anthropic.Anthropic()
   139|tools = [...]  # Your tool definitions
   140|messages = [{"role": "user", "content": user_input}]
   141|
   142|# Agentic loop: keep going until Claude stops calling tools
   143|while True:
   144|    response = client.messages.create(
   145|        model="claude-opus-4-7",
   146|        max_tokens=16000,
   147|        tools=tools,
   148|        messages=messages
   149|    )
   150|
   151|    # If Claude is done (no more tool calls), break
   152|    if response.stop_reason == "end_turn":
   153|        break
   154|
   155|    # Server-side tool hit iteration limit; re-send to continue
   156|    if response.stop_reason == "pause_turn":
   157|        messages = [
   158|            {"role": "user", "content": user_input},
   159|            {"role": "assistant", "content": response.content},
   160|        ]
   161|        continue
   162|
   163|    # Extract tool use blocks from the response
   164|    tool_use_blocks = [b for b in response.content if b.type == "tool_use"]
   165|
   166|    # Append assistant's response (including tool_use blocks)
   167|    messages.append({"role": "assistant", "content": response.content})
   168|
   169|    # Execute each tool and collect results
   170|    tool_results = []
   171|    for tool in tool_use_blocks:
   172|        result = execute_tool(tool.name, tool.input)  # Your implementation
   173|        tool_results.append({
   174|            "type": "tool_result",
   175|            "tool_use_id": tool.id,  # Must match the tool_use block's id
   176|            "content": result
   177|        })
   178|
   179|    # Append tool results as a user message
   180|    messages.append({"role": "user", "content": tool_results})
   181|
   182|# Final response text
   183|final_text = next(b.text for b in response.content if b.type == "text")
   184|```
   185|
   186|---
   187|
   188|## Handling Tool Results
   189|
   190|```python
   191|response = client.messages.create(
   192|    model="claude-opus-4-7",
   193|    max_tokens=16000,
   194|    tools=tools,
   195|    messages=[{"role": "user", "content": "What's the weather in Paris?"}]
   196|)
   197|
   198|for block in response.content:
   199|    if block.type == "tool_use":
   200|        tool_name = block.name
   201|        tool_input = block.input
   202|        tool_use_id = block.id
   203|
   204|        result = execute_tool(tool_name, tool_input)
   205|
   206|        followup = client.messages.create(
   207|            model="claude-opus-4-7",
   208|            max_tokens=16000,
   209|            tools=tools,
   210|            messages=[
   211|                {"role": "user", "content": "What's the weather in Paris?"},
   212|                {"role": "assistant", "content": response.content},
   213|                {
   214|                    "role": "user",
   215|                    "content": [{
   216|                        "type": "tool_result",
   217|                        "tool_use_id": tool_use_id,
   218|                        "content": result
   219|                    }]
   220|                }
   221|            ]
   222|        )
   223|```
   224|
   225|---
   226|
   227|## Multiple Tool Calls
   228|
   229|```python
   230|tool_results = []
   231|
   232|for block in response.content:
   233|    if block.type == "tool_use":
   234|        result = execute_tool(block.name, block.input)
   235|        tool_results.append({
   236|            "type": "tool_result",
   237|            "tool_use_id": block.id,
   238|            "content": result
   239|        })
   240|
   241|# Send all results back at once
   242|if tool_results:
   243|    followup = client.messages.create(
   244|        model="claude-opus-4-7",
   245|        max_tokens=16000,
   246|        tools=tools,
   247|        messages=[
   248|            *previous_messages,
   249|            {"role": "assistant", "content": response.content},
   250|            {"role": "user", "content": tool_results}
   251|        ]
   252|    )
   253|```
   254|
   255|---
   256|
   257|## Error Handling in Tool Results
   258|
   259|```python
   260|tool_result = {
   261|    "type": "tool_result",
   262|    "tool_use_id": tool_use_id,
   263|    "content": "Error: Location 'xyz' not found. Please provide a valid city name.",
   264|    "is_error": True
   265|}
   266|```
   267|
   268|---
   269|
   270|## Tool Choice
   271|
   272|```python
   273|response = client.messages.create(
   274|    model="claude-opus-4-7",
   275|    max_tokens=16000,
   276|    tools=tools,
   277|    tool_choice={"type": "tool", "name": "get_weather"},  # Force specific tool
   278|    messages=[{"role": "user", "content": "What's the weather in Paris?"}]
   279|)
   280|```
   281|
   282|---
   283|
   284|## Code Execution
   285|
   286|### Basic Usage
   287|
   288|```python
   289|import anthropic
   290|
   291|client = anthropic.Anthropic()
   292|
   293|response = client.messages.create(
   294|    model="claude-opus-4-7",
   295|    max_tokens=16000,
   296|    messages=[{
   297|        "role": "user",
   298|        "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
   299|    }],
   300|    tools=[{
   301|        "type": "code_execution_20260120",
   302|        "name": "code_execution"
   303|    }]
   304|)
   305|
   306|for block in response.content:
   307|    if block.type == "text":
   308|        print(block.text)
   309|    elif block.type == "bash_code_execution_tool_result":
   310|        print(f"stdout: {block.content.stdout}")
   311|```
   312|
   313|### Upload Files for Analysis
   314|
   315|```python
   316|# 1. Upload a file
   317|uploaded = client.beta.files.upload(file=open("sales_data.csv", "rb"))
   318|
   319|# 2. Pass to code execution via container_upload block
   320|# Code execution is GA; Files API is still beta (pass via extra_headers)
   321|response = client.messages.create(
   322|    model="claude-opus-4-7",
   323|    max_tokens=16000,
   324|    extra_headers={"anthropic-beta": "files-api-2025-04-14"},
   325|    messages=[{
   326|        "role": "user",
   327|        "content": [
   328|            {"type": "text", "text": "Analyze this sales data. Show trends and create a visualization."},
   329|            {"type": "container_upload", "file_id": uploaded.id}
   330|        ]
   331|    }],
   332|    tools=[{"type": "code_execution_20260120", "name": "code_execution"}]
   333|)
   334|```
   335|
   336|### Retrieve Generated Files
   337|
   338|```python
   339|import os
   340|
   341|OUTPUT_DIR = "./claude_outputs"
   342|os.makedirs(OUTPUT_DIR, exist_ok=True)
   343|
   344|for block in response.content:
   345|    if block.type == "bash_code_execution_tool_result":
   346|        result = block.content
   347|        if result.type == "bash_code_execution_result" and result.content:
   348|            for file_ref in result.content:
   349|                if file_ref.type == "bash_code_execution_output":
   350|                    metadata = client.beta.files.retrieve_metadata(file_ref.file_id)
   351|                    file_content = client.beta.files.download(file_ref.file_id)
   352|                    # Use basename to prevent path traversal; validate result
   353|                    safe_name = os.path.basename(metadata.filename)
   354|                    if not safe_name or safe_name in (".", ".."):
   355|                        print(f"Skipping invalid filename: {metadata.filename}")
   356|                        continue
   357|                    output_path = os.path.join(OUTPUT_DIR, safe_name)
   358|                    file_content.write_to_file(output_path)
   359|                    print(f"Saved: {output_path}")
   360|```
   361|
   362|### Container Reuse
   363|
   364|```python
   365|# First request: set up environment
   366|response1 = client.messages.create(
   367|    model="claude-opus-4-7",
   368|    max_tokens=16000,
   369|    messages=[{"role": "user", "content": "Install tabulate and create data.json with sample data"}],
   370|    tools=[{"type": "code_execution_20260120", "name": "code_execution"}]
   371|)
   372|
   373|# Get container ID from response
   374|container_id = response1.container.id
   375|
   376|# Second request: reuse the same container
   377|response2 = client.messages.create(
   378|    container=container_id,
   379|    model="claude-opus-4-7",
   380|    max_tokens=16000,
   381|    messages=[{"role": "user", "content": "Read data.json and display as a formatted table"}],
   382|    tools=[{"type": "code_execution_20260120", "name": "code_execution"}]
   383|)
   384|```
   385|
   386|### Response Structure
   387|
   388|```python
   389|for block in response.content:
   390|    if block.type == "text":
   391|        print(block.text)  # Claude's explanation
   392|    elif block.type == "server_tool_use":
   393|        print(f"Running: {block.name} - {block.input}")  # What Claude is doing
   394|    elif block.type == "bash_code_execution_tool_result":
   395|        result = block.content
   396|        if result.type == "bash_code_execution_result":
   397|            if result.return_code == 0:
   398|                print(f"Output: {result.stdout}")
   399|            else:
   400|                print(f"Error: {result.stderr}")
   401|        else:
   402|            print(f"Tool error: {result.error_code}")
   403|    elif block.type == "text_editor_code_execution_tool_result":
   404|        print(f"File operation: {block.content}")
   405|```
   406|
   407|---
   408|
   409|## Memory Tool
   410|
   411|### Basic Usage
   412|
   413|```python
   414|import anthropic
   415|
   416|client = anthropic.Anthropic()
   417|
   418|response = client.messages.create(
   419|    model="claude-opus-4-7",
   420|    max_tokens=16000,
   421|    messages=[{"role": "user", "content": "Remember that my preferred language is Python."}],
   422|    tools=[{"type": "memory_20250818", "name": "memory"}],
   423|)
   424|```
   425|
   426|### SDK Memory Helper
   427|
   428|Subclass `BetaAbstractMemoryTool`:
   429|
   430|```python
   431|from anthropic.lib.tools import BetaAbstractMemoryTool
   432|
   433|class MyMemoryTool(BetaAbstractMemoryTool):
   434|    def view(self, command): ...
   435|    def create(self, command): ...
   436|    def str_replace(self, command): ...
   437|    def insert(self, command): ...
   438|    def delete(self, command): ...
   439|    def rename(self, command): ...
   440|
   441|memory = MyMemoryTool()
   442|
   443|# Use with tool runner
   444|runner = client.beta.messages.tool_runner(
   445|    model="claude-opus-4-7",
   446|    max_tokens=16000,
   447|    tools=[memory],
   448|    messages=[{"role": "user", "content": "Remember my preferences"}],
   449|)
   450|
   451|for message in runner:
   452|    print(message)
   453|```
   454|
   455|For full implementation examples, use WebFetch:
   456|
   457|- `https://github.com/anthropics/anthropic-sdk-python/blob/main/examples/memory/basic.py`
   458|
   459|---
   460|
   461|## Structured Outputs
   462|
   463|### JSON Outputs (Pydantic — Recommended)
   464|
   465|```python
   466|from pydantic import BaseModel
   467|from typing import List
   468|import anthropic
   469|
   470|class ContactInfo(BaseModel):
   471|    name: str
   472|    email: str
   473|    plan: str
   474|    interests: List[str]
   475|    demo_requested: bool
   476|
   477|client = anthropic.Anthropic()
   478|
   479|response = client.messages.parse(
   480|    model="claude-opus-4-7",
   481|    max_tokens=16000,
   482|    messages=[{
   483|        "role": "user",
   484|        "content": "Extract: Jane Doe (jane@co.com) wants Enterprise, interested in API and SDKs, wants a demo."
   485|    }],
   486|    output_format=ContactInfo,
   487|)
   488|
   489|# response.parsed_output is a validated ContactInfo instance
   490|contact = response.parsed_output
   491|print(contact.name)           # "Jane Doe"
   492|print(contact.interests)      # ["API", "SDKs"]
   493|```
   494|
   495|### Raw Schema
   496|
   497|```python
   498|response = client.messages.create(
   499|    model="claude-opus-4-7",
   500|    max_tokens=16000,
   501|