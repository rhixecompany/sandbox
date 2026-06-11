---
name: claude-api-ruby
description: "Claude API — Ruby"
version: 1.0.0
author: Alexa
---
     1|# Claude API — Ruby
     2|
     3|> **Note:** The Ruby SDK supports the Claude API. A tool runner is available in beta via `client.beta.messages.tool_runner()`. Agent SDK is not yet available for Ruby.
     4|
     5|## Installation
     6|
     7|```bash
     8|gem install anthropic
     9|```
    10|
    11|## Client Initialization
    12|
    13|```ruby
    14|require "anthropic"
    15|
    16|# Default (uses ANTHROPIC_API_KEY env var)
    17|client = Anthropic::Client.new
    18|
    19|# Explicit API key
    20|client = Anthropic::Client.new(api_key: "your-api-key")
    21|```
    22|
    23|---
    24|
    25|## Basic Message Request
    26|
    27|```ruby
    28|message = client.messages.create(
    29|  model: :"claude-opus-4-7",
    30|  max_tokens: 16000,
    31|  messages: [
    32|    { role: "user", content: "What is the capital of France?" }
    33|  ]
    34|)
    35|# content is an array of polymorphic block objects (TextBlock, ThinkingBlock,
    36|# ToolUseBlock, ...). .type is a Symbol — compare with :text, not "text".
    37|# .text raises NoMethodError on non-TextBlock entries.
    38|message.content.each do |block|
    39|  puts block.text if block.type == :text
    40|end
    41|```
    42|
    43|---
    44|
    45|## Streaming
    46|
    47|```ruby
    48|stream = client.messages.stream(
    49|  model: :"claude-opus-4-7",
    50|  max_tokens: 64000,
    51|  messages: [{ role: "user", content: "Write a haiku" }]
    52|)
    53|
    54|stream.text.each { |text| print(text) }
    55|```
    56|
    57|---
    58|
    59|## Tool Use
    60|
    61|The Ruby SDK supports tool use via raw JSON schema definitions and also provides a beta tool runner for automatic tool execution.
    62|
    63|### Tool Runner (Beta)
    64|
    65|```ruby
    66|class GetWeatherInput < Anthropic::BaseModel
    67|  required :location, String, doc: "City and state, e.g. San Francisco, CA"
    68|end
    69|
    70|class GetWeather < Anthropic::BaseTool
    71|  doc "Get the current weather for a location"
    72|
    73|  input_schema GetWeatherInput
    74|
    75|  def call(input)
    76|    "The weather in #{input.location} is sunny and 72°F."
    77|  end
    78|end
    79|
    80|client.beta.messages.tool_runner(
    81|  model: :"claude-opus-4-7",
    82|  max_tokens: 16000,
    83|  tools: [GetWeather.new],
    84|  messages: [{ role: "user", content: "What's the weather in San Francisco?" }]
    85|).each_message do |message|
    86|  puts message.content
    87|end
    88|```
    89|
    90|### Manual Loop
    91|
    92|See the [shared tool use concepts](../shared/tool-use-concepts.md) for the tool definition format and agentic loop pattern.
    93|
    94|---
    95|
    96|## Prompt Caching
    97|
    98|`system_:` (trailing underscore — avoids shadowing `Kernel#system`) takes an array of text blocks; set `cache_control` on the last block. Plain hashes work via the `OrHash` type alias. For placement patterns and the silent-invalidator audit checklist, see `shared/prompt-caching.md`.
    99|
   100|```ruby
   101|message = client.messages.create(
   102|  model: :"claude-opus-4-7",
   103|  max_tokens: 16000,
   104|  system_: [
   105|    { type: "text", text: long_system_prompt, cache_control: { type: "ephemeral" } }
   106|  ],
   107|  messages: [{ role: "user", content: "Summarize the key points" }]
   108|)
   109|```
   110|
   111|For 1-hour TTL: `cache_control: { type: "ephemeral", ttl: "1h" }`. There's also a top-level `cache_control:` on `messages.create` that auto-places on the last cacheable block.
   112|
   113|Verify hits via `message.usage.cache_creation_input_tokens` / `message.usage.cache_read_input_tokens`.
   114|