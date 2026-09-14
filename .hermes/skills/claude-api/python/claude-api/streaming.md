---
name: streaming-python
description: "Streaming — Python"
version: 1.0.0
author: Alexa
---
     1|# Streaming — Python
     2|
     3|## Quick Start
     4|
     5|```python
     6|with client.messages.stream(
     7|    model="claude-opus-4-7",
     8|    max_tokens=64000,
     9|    messages=[{"role": "user", "content": "Write a story"}]
    10|) as stream:
    11|    for text in stream.text_stream:
    12|        print(text, end="", flush=True)
    13|```
    14|
    15|### Async
    16|
    17|```python
    18|async with async_client.messages.stream(
    19|    model="claude-opus-4-7",
    20|    max_tokens=64000,
    21|    messages=[{"role": "user", "content": "Write a story"}]
    22|) as stream:
    23|    async for text in stream.text_stream:
    24|        print(text, end="", flush=True)
    25|```
    26|
    27|---
    28|
    29|## Handling Different Content Types
    30|
    31|Claude may return text, thinking blocks, or tool use. Handle each appropriately:
    32|
    33|> **Opus 4.7 / Opus 4.6:** Use `thinking: {type: "adaptive"}`. On older models, use `thinking: {type: "enabled", budget_tokens: N}` instead.
    34|
    35|```python
    36|with client.messages.stream(
    37|    model="claude-opus-4-7",
    38|    max_tokens=64000,
    39|    thinking={"type": "adaptive"},
    40|    messages=[{"role": "user", "content": "Analyze this problem"}]
    41|) as stream:
    42|    for event in stream:
    43|        if event.type == "content_block_start":
    44|            if event.content_block.type == "thinking":
    45|                print("\n[Thinking...]")
    46|            elif event.content_block.type == "text":
    47|                print("\n[Response:]")
    48|
    49|        elif event.type == "content_block_delta":
    50|            if event.delta.type == "thinking_delta":
    51|                print(event.delta.thinking, end="", flush=True)
    52|            elif event.delta.type == "text_delta":
    53|                print(event.delta.text, end="", flush=True)
    54|```
    55|
    56|---
    57|
    58|## Streaming with Tool Use
    59|
    60|The Python tool runner currently returns complete messages. Use streaming for individual API calls within a manual loop if you need per-token streaming with tools:
    61|
    62|```python
    63|with client.messages.stream(
    64|    model="claude-opus-4-7",
    65|    max_tokens=64000,
    66|    tools=tools,
    67|    messages=messages
    68|) as stream:
    69|    for text in stream.text_stream:
    70|        print(text, end="", flush=True)
    71|
    72|    response = stream.get_final_message()
    73|    # Continue with tool execution if response.stop_reason == "tool_use"
    74|```
    75|
    76|---
    77|
    78|## Getting the Final Message
    79|
    80|```python
    81|with client.messages.stream(
    82|    model="claude-opus-4-7",
    83|    max_tokens=64000,
    84|    messages=[{"role": "user", "content": "Hello"}]
    85|) as stream:
    86|    for text in stream.text_stream:
    87|        print(text, end="", flush=True)
    88|
    89|    # Get full message after streaming
    90|    final_message = stream.get_final_message()
    91|    print(f"\n\nTokens used: {final_message.usage.output_tokens}")
    92|```
    93|
    94|---
    95|
    96|## Streaming with Progress Updates
    97|
    98|```python
    99|def stream_with_progress(client, **kwargs):
   100|    """Stream a response with progress updates."""
   101|    total_tokens = 0
   102|    content_parts = []
   103|
   104|    with client.messages.stream(**kwargs) as stream:
   105|        for event in stream:
   106|            if event.type == "content_block_delta":
   107|                if event.delta.type == "text_delta":
   108|                    text = event.delta.text
   109|                    content_parts.append(text)
   110|                    print(text, end="", flush=True)
   111|
   112|            elif event.type == "message_delta":
   113|                if event.usage and event.usage.output_tokens is not None:
   114|                    total_tokens = event.usage.output_tokens
   115|
   116|        final_message = stream.get_final_message()
   117|
   118|    print(f"\n\n[Tokens used: {total_tokens}]")
   119|    return "".join(content_parts)
   120|```
   121|
   122|---
   123|
   124|## Error Handling in Streams
   125|
   126|```python
   127|try:
   128|    with client.messages.stream(
   129|        model="claude-opus-4-7",
   130|        max_tokens=64000,
   131|        messages=[{"role": "user", "content": "Write a story"}]
   132|    ) as stream:
   133|        for text in stream.text_stream:
   134|            print(text, end="", flush=True)
   135|except anthropic.APIConnectionError:
   136|    print("\nConnection lost. Please retry.")
   137|except anthropic.RateLimitError:
   138|    print("\nRate limited. Please wait and retry.")
   139|except anthropic.APIStatusError as e:
   140|    print(f"\nAPI error: {e.status_code}")
   141|```
   142|
   143|---
   144|
   145|## Stream Event Types
   146|
   147|| Event Type | Description | When it fires |
   148|| --- | --- | --- |
   149|| `message_start` | Contains message metadata | Once at the beginning |
   150|| `content_block_start` | New content block beginning | When a text/tool_use block starts |
   151|| `content_block_delta` | Incremental content update | For each token/chunk |
   152|| `content_block_stop` | Content block complete | When a block finishes |
   153|| `message_delta` | Message-level updates | Contains `stop_reason`, usage |
   154|| `message_stop` | Message complete | Once at the end |
   155|
   156|## Best Practices
   157|
   158|1. **Always flush output** — Use `flush=True` to show tokens immediately
   159|2. **Handle partial responses** — If the stream is interrupted, you may have incomplete content
   160|3. **Track token usage** — The `message_delta` event contains usage information
   161|4. **Use timeouts** — Set appropriate timeouts for your application
   162|5. **Default to streaming** — Use `.get_final_message()` to get the complete response even when streaming, giving you timeout protection without needing to handle individual events
   163|