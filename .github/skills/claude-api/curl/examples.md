---
name: examples-curl
description: "Reference: examples-curl"
version: 1.0.0
author: Alexa
---
     1|# Claude API — cURL / Raw HTTP
     2|
     3|Use these examples when the user needs raw HTTP requests or is working in a language without an official SDK.
     4|
     5|## Setup
     6|
     7|```bash
     8|export ANTHROPIC_API_KEY="your-api-key"
     9|```
    10|
    11|---
    12|
    13|## Basic Message Request
    14|
    15|```bash
    16|curl https://api.anthropic.com/v1/messages \
    17|  -H "Content-Type: application/json" \
    18|  -H "x-api-key: $ANTHROPIC_API_KEY" \
    19|  -H "anthropic-version: 2023-06-01" \
    20|  -d '{
    21|    "model": "claude-opus-4-7",
    22|    "max_tokens": 16000,
    23|    "messages": [
    24|      {"role": "user", "content": "What is the capital of France?"}
    25|    ]
    26|  }'
    27|```
    28|
    29|### Parsing the response
    30|
    31|Use `jq` to extract fields from the JSON response. Do not use `grep`/`sed` — JSON strings can contain any character and regex parsing will break on quotes, escapes, or multi-line content.
    32|
    33|```bash
    34|# Capture the response, then extract fields
    35|response=$(curl -s https://api.anthropic.com/v1/messages \
    36|  -H "Content-Type: application/json" \
    37|  -H "x-api-key: $ANTHROPIC_API_KEY" \
    38|  -H "anthropic-version: 2023-06-01" \
    39|  -d '{"model":"claude-opus-4-7","max_tokens":16000,"messages":[{"role":"user","content":"Hello"}]}')
    40|
    41|# Print the first text block (-r strips the JSON quotes)
    42|echo "$response" | jq -r '.content[0].text'
    43|
    44|# Read usage fields
    45|input_tokens=$(echo "$response" | jq -r '.usage.input_tokens')
    46|output_tokens=$(echo "$response" | jq -r '.usage.output_tokens')
    47|
    48|# Read stop reason (for tool-use loops)
    49|stop_reason=$(echo "$response" | jq -r '.stop_reason')
    50|
    51|# Extract all text blocks (content is an array; filter to type=="text")
    52|echo "$response" | jq -r '.content[] | select(.type == "text") | .text'
    53|```
    54|
    55|---
    56|
    57|## Streaming (SSE)
    58|
    59|```bash
    60|curl https://api.anthropic.com/v1/messages \
    61|  -H "Content-Type: application/json" \
    62|  -H "x-api-key: $ANTHROPIC_API_KEY" \
    63|  -H "anthropic-version: 2023-06-01" \
    64|  -d '{
    65|    "model": "claude-opus-4-7",
    66|    "max_tokens": 64000,
    67|    "stream": true,
    68|    "messages": [{"role": "user", "content": "Write a haiku"}]
    69|  }'
    70|```
    71|
    72|The response is a stream of Server-Sent Events:
    73|
    74|```
    75|event: message_start
    76|data: {"type":"message_start","message":{"id":"msg_...","type":"message",...}}
    77|
    78|event: content_block_start
    79|data: {"type":"content_block_start","index":0,"content_block":{"type":"text","text":""}}
    80|
    81|event: content_block_delta
    82|data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":"Hello"}}
    83|
    84|event: content_block_stop
    85|data: {"type":"content_block_stop","index":0}
    86|
    87|event: message_delta
    88|data: {"type":"message_delta","delta":{"stop_reason":"end_turn"},"usage":{"output_tokens":12}}
    89|
    90|event: message_stop
    91|data: {"type":"message_stop"}
    92|```
    93|
    94|---
    95|
    96|## Tool Use
    97|
    98|```bash
    99|curl https://api.anthropic.com/v1/messages \
   100|  -H "Content-Type: application/json" \
   101|  -H "x-api-key: $ANTHROPIC_API_KEY" \
   102|  -H "anthropic-version: 2023-06-01" \
   103|  -d '{
   104|    "model": "claude-opus-4-7",
   105|    "max_tokens": 16000,
   106|    "tools": [{
   107|      "name": "get_weather",
   108|      "description": "Get current weather for a location",
   109|      "input_schema": {
   110|        "type": "object",
   111|        "properties": {
   112|          "location": {"type": "string", "description": "City name"}
   113|        },
   114|        "required": ["location"]
   115|      }
   116|    }],
   117|    "messages": [{"role": "user", "content": "What is the weather in Paris?"}]
   118|  }'
   119|```
   120|
   121|When Claude responds with a `tool_use` block, send the result back:
   122|
   123|```bash
   124|curl https://api.anthropic.com/v1/messages \
   125|  -H "Content-Type: application/json" \
   126|  -H "x-api-key: $ANTHROPIC_API_KEY" \
   127|  -H "anthropic-version: 2023-06-01" \
   128|  -d '{
   129|    "model": "claude-opus-4-7",
   130|    "max_tokens": 16000,
   131|    "tools": [{
   132|      "name": "get_weather",
   133|      "description": "Get current weather for a location",
   134|      "input_schema": {
   135|        "type": "object",
   136|        "properties": {
   137|          "location": {"type": "string", "description": "City name"}
   138|        },
   139|        "required": ["location"]
   140|      }
   141|    }],
   142|    "messages": [
   143|      {"role": "user", "content": "What is the weather in Paris?"},
   144|      {"role": "assistant", "content": [
   145|        {"type": "text", "text": "Let me check the weather."},
   146|        {"type": "tool_use", "id": "toolu_abc123", "name": "get_weather", "input": {"location": "Paris"}}
   147|      ]},
   148|      {"role": "user", "content": [
   149|        {"type": "tool_result", "tool_use_id": "toolu_abc123", "content": "72°F and sunny"}
   150|      ]}
   151|    ]
   152|  }'
   153|```
   154|
   155|---
   156|
   157|## Prompt Caching
   158|
   159|Put `cache_control` on the last block of the stable prefix. See `shared/prompt-caching.md` for placement patterns and the silent-invalidator audit checklist.
   160|
   161|```bash
   162|curl https://api.anthropic.com/v1/messages \
   163|  -H "Content-Type: application/json" \
   164|  -H "x-api-key: $ANTHROPIC_API_KEY" \
   165|  -H "anthropic-version: 2023-06-01" \
   166|  -d '{
   167|    "model": "claude-opus-4-7",
   168|    "max_tokens": 16000,
   169|    "system": [
   170|      {"type": "text", "text": "<large shared prompt...>", "cache_control": {"type": "ephemeral"}}
   171|    ],
   172|    "messages": [{"role": "user", "content": "Summarize the key points"}]
   173|  }'
   174|```
   175|
   176|For 1-hour TTL: `"cache_control": {"type": "ephemeral", "ttl": "1h"}`. Top-level `"cache_control"` on the request body auto-places on the last cacheable block. Verify hits via the response `usage.cache_creation_input_tokens` / `usage.cache_read_input_tokens` fields.
   177|
   178|---
   179|
   180|## Extended Thinking
   181|
   182|> **Opus 4.7, Opus 4.6, and Sonnet 4.6:** Use adaptive thinking. `budget_tokens` is removed on Opus 4.7 (400 if sent); deprecated on Opus 4.6 and Sonnet 4.6. **Older models:** Use `"type": "enabled"` with `"budget_tokens": N` (must be < `max_tokens`, min 1024).
   183|
   184|```bash
   185|# Opus 4.7 / 4.6: adaptive thinking (recommended)
   186|curl https://api.anthropic.com/v1/messages \
   187|  -H "Content-Type: application/json" \
   188|  -H "x-api-key: $ANTHROPIC_API_KEY" \
   189|  -H "anthropic-version: 2023-06-01" \
   190|  -d '{
   191|    "model": "claude-opus-4-7",
   192|    "max_tokens": 16000,
   193|    "thinking": {
   194|      "type": "adaptive"
   195|    },
   196|    "output_config": {
   197|      "effort": "high"
   198|    },
   199|    "messages": [{"role": "user", "content": "Solve this step by step..."}]
   200|  }'
   201|```
   202|
   203|---
   204|
   205|## Required Headers
   206|
   207|| Header | Value | Description |
   208|| --- | --- | --- |
   209|| `Content-Type` | `application/json` | Required |
   210|| `x-api-key` | Your API key | Authentication |
   211|| `anthropic-version` | `2023-06-01` | API version |
   212|| `anthropic-beta` | Beta feature IDs | Required for beta features |
   213|