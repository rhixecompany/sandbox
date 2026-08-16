---
name: readme-python
description: "Claude API — Python"
version: 1.0.0
author: Alexa
---
     1|# Claude API — Python
     2|
     3|## Installation
     4|
     5|```bash
     6|pip install anthropic
     7|```
     8|
     9|## Client Initialization
    10|
    11|```python
    12|import anthropic
    13|
    14|# Default (uses ANTHROPIC_API_KEY env var)
    15|client = anthropic.Anthropic()
    16|
    17|# Explicit API key
    18|client = anthropic.Anthropic(api_key="your-api-key")
    19|
    20|# Async client
    21|async_client = anthropic.AsyncAnthropic()
    22|```
    23|
    24|---
    25|
    26|## Basic Message Request
    27|
    28|```python
    29|response = client.messages.create(
    30|    model="claude-opus-4-7",
    31|    max_tokens=16000,
    32|    messages=[
    33|        {"role": "user", "content": "What is the capital of France?"}
    34|    ]
    35|)
    36|# response.content is a list of content block objects (TextBlock, ThinkingBlock,
    37|# ToolUseBlock, ...). Check .type before accessing .text.
    38|for block in response.content:
    39|    if block.type == "text":
    40|        print(block.text)
    41|```
    42|
    43|---
    44|
    45|## System Prompts
    46|
    47|```python
    48|response = client.messages.create(
    49|    model="claude-opus-4-7",
    50|    max_tokens=16000,
    51|    system="You are a helpful coding assistant. Always provide examples in Python.",
    52|    messages=[{"role": "user", "content": "How do I read a JSON file?"}]
    53|)
    54|```
    55|
    56|---
    57|
    58|## Vision (Images)
    59|
    60|### Base64
    61|
    62|```python
    63|import base64
    64|
    65|with open("image.png", "rb") as f:
    66|    image_data = base64.standard_b64encode(f.read()).decode("utf-8")
    67|
    68|response = client.messages.create(
    69|    model="claude-opus-4-7",
    70|    max_tokens=16000,
    71|    messages=[{
    72|        "role": "user",
    73|        "content": [
    74|            {
    75|                "type": "image",
    76|                "source": {
    77|                    "type": "base64",
    78|                    "media_type": "image/png",
    79|                    "data": image_data
    80|                }
    81|            },
    82|            {"type": "text", "text": "What's in this image?"}
    83|        ]
    84|    }]
    85|)
    86|```
    87|
    88|### URL
    89|
    90|```python
    91|response = client.messages.create(
    92|    model="claude-opus-4-7",
    93|    max_tokens=16000,
    94|    messages=[{
    95|        "role": "user",
    96|        "content": [
    97|            {
    98|                "type": "image",
    99|                "source": {
   100|                    "type": "url",
   101|                    "url": "https://example.com/image.png"
   102|                }
   103|            },
   104|            {"type": "text", "text": "Describe this image"}
   105|        ]
   106|    }]
   107|)
   108|```
   109|
   110|---
   111|
   112|## Prompt Caching
   113|
   114|Cache large context to reduce costs (up to 90% savings). **Caching is a prefix match** — any byte change anywhere in the prefix invalidates everything after it. For placement patterns, architectural guidance (frozen system prompt, deterministic tool order, where to put volatile content), and the silent-invalidator audit checklist, read `shared/prompt-caching.md`.
   115|
   116|### Automatic Caching (Recommended)
   117|
   118|Use top-level `cache_control` to automatically cache the last cacheable block in the request — no need to annotate individual content blocks:
   119|
   120|```python
   121|response = client.messages.create(
   122|    model="claude-opus-4-7",
   123|    max_tokens=16000,
   124|    cache_control={"type": "ephemeral"},  # auto-caches the last cacheable block
   125|    system="You are an expert on this large document...",
   126|    messages=[{"role": "user", "content": "Summarize the key points"}]
   127|)
   128|```
   129|
   130|### Manual Cache Control
   131|
   132|For fine-grained control, add `cache_control` to specific content blocks:
   133|
   134|```python
   135|response = client.messages.create(
   136|    model="claude-opus-4-7",
   137|    max_tokens=16000,
   138|    system=[{
   139|        "type": "text",
   140|        "text": "You are an expert on this large document...",
   141|        "cache_control": {"type": "ephemeral"}  # default TTL is 5 minutes
   142|    }],
   143|    messages=[{"role": "user", "content": "Summarize the key points"}]
   144|)
   145|
   146|# With explicit TTL (time-to-live)
   147|response = client.messages.create(
   148|    model="claude-opus-4-7",
   149|    max_tokens=16000,
   150|    system=[{
   151|        "type": "text",
   152|        "text": "You are an expert on this large document...",
   153|        "cache_control": {"type": "ephemeral", "ttl": "1h"}  # 1 hour TTL
   154|    }],
   155|    messages=[{"role": "user", "content": "Summarize the key points"}]
   156|)
   157|```
   158|
   159|### Verifying Cache Hits
   160|
   161|```python
   162|print(response.usage.cache_creation_input_tokens)  # tokens written to cache (~1.25x cost)
   163|print(response.usage.cache_read_input_tokens)      # tokens served from cache (~0.1x cost)
   164|print(response.usage.input_tokens)                 # uncached tokens (full cost)
   165|```
   166|
   167|If `cache_read_input_tokens` is zero across repeated identical-prefix requests, a silent invalidator is at work — `datetime.now()` or a UUID in the system prompt, unsorted `json.dumps()`, or a varying tool set. See `shared/prompt-caching.md` for the full audit table.
   168|
   169|---
   170|
   171|## Extended Thinking
   172|
   173|> **Opus 4.7, Opus 4.6, and Sonnet 4.6:** Use adaptive thinking. `budget_tokens` is removed on Opus 4.7 (400 if sent); deprecated on Opus 4.6 and Sonnet 4.6. **Older models:** Use `thinking: {type: "enabled", budget_tokens: N}` (must be < `max_tokens`, min 1024).
   174|
   175|```python
   176|# Opus 4.7 / 4.6: adaptive thinking (recommended)
   177|response = client.messages.create(
   178|    model="claude-opus-4-7",
   179|    max_tokens=16000,
   180|    thinking={"type": "adaptive"},
   181|    output_config={"effort": "high"},  # low | medium | high | max
   182|    messages=[{"role": "user", "content": "Solve this step by step..."}]
   183|)
   184|
   185|# Access thinking and response
   186|for block in response.content:
   187|    if block.type == "thinking":
   188|        print(f"Thinking: {block.thinking}")
   189|    elif block.type == "text":
   190|        print(f"Response: {block.text}")
   191|```
   192|
   193|---
   194|
   195|## Error Handling
   196|
   197|```python
   198|import anthropic
   199|
   200|try:
   201|    response = client.messages.create(...)
   202|except anthropic.BadRequestError as e:
   203|    print(f"Bad request: {e.message}")
   204|except anthropic.AuthenticationError:
   205|    print("Invalid API key")
   206|except anthropic.PermissionDeniedError:
   207|    print("API key lacks required permissions")
   208|except anthropic.NotFoundError:
   209|    print("Invalid model or endpoint")
   210|except anthropic.RateLimitError as e:
   211|    retry_after = int(e.response.headers.get("retry-after", "60"))
   212|    print(f"Rate limited. Retry after {retry_after}s.")
   213|except anthropic.APIStatusError as e:
   214|    if e.status_code >= 500:
   215|        print(f"Server error ({e.status_code}). Retry later.")
   216|    else:
   217|        print(f"API error: {e.message}")
   218|except anthropic.APIConnectionError:
   219|    print("Network error. Check internet connection.")
   220|```
   221|
   222|---
   223|
   224|## Multi-Turn Conversations
   225|
   226|The API is stateless — send the full conversation history each time.
   227|
   228|```python
   229|class ConversationManager:
   230|    """Manage multi-turn conversations with the Claude API."""
   231|
   232|    def __init__(self, client: anthropic.Anthropic, model: str, system: str = None):
   233|        self.client = client
   234|        self.model = model
   235|        self.system = system
   236|        self.messages = []
   237|
   238|    def send(self, user_message: str, **kwargs) -> str:
   239|        """Send a message and get a response."""
   240|        self.messages.append({"role": "user", "content": user_message})
   241|
   242|        response = self.client.messages.create(
   243|            model=self.model,
   244|            max_tokens=kwargs.get("max_tokens", 16000),
   245|            system=self.system,
   246|            messages=self.messages,
   247|            **kwargs
   248|        )
   249|
   250|        assistant_message = next(
   251|            (b.text for b in response.content if b.type == "text"), ""
   252|        )
   253|        self.messages.append({"role": "assistant", "content": assistant_message})
   254|
   255|        return assistant_message
   256|
   257|# Usage
   258|conversation = ConversationManager(
   259|    client=anthropic.Anthropic(),
   260|    model="claude-opus-4-7",
   261|    system="You are a helpful assistant."
   262|)
   263|
   264|response1 = conversation.send("My name is Alice.")
   265|response2 = conversation.send("What's my name?")  # Claude remembers "Alice"
   266|```
   267|
   268|**Rules:**
   269|
   270|- Messages must alternate between `user` and `assistant`
   271|- First message must be `user`
   272|
   273|---
   274|
   275|### Compaction (long conversations)
   276|
   277|> **Beta, Opus 4.7, Opus 4.6, and Sonnet 4.6.** When conversations approach the 200K context window, compaction automatically summarizes earlier context server-side. The API returns a `compaction` block; you must pass it back on subsequent requests — append `response.content`, not just the text.
   278|
   279|```python
   280|import anthropic
   281|
   282|client = anthropic.Anthropic()
   283|messages = []
   284|
   285|def chat(user_message: str) -> str:
   286|    messages.append({"role": "user", "content": user_message})
   287|
   288|    response = client.beta.messages.create(
   289|        betas=["compact-2026-01-12"],
   290|        model="claude-opus-4-7",
   291|        max_tokens=16000,
   292|        messages=messages,
   293|        context_management={
   294|            "edits": [{"type": "compact_20260112"}]
   295|        }
   296|    )
   297|
   298|    # Append full content — compaction blocks must be preserved
   299|    messages.append({"role": "assistant", "content": response.content})
   300|
   301|    return next(block.text for block in response.content if block.type == "text")
   302|
   303|# Compaction triggers automatically when context grows large
   304|print(chat("Help me build a Python web scraper"))
   305|print(chat("Add support for JavaScript-rendered pages"))
   306|print(chat("Now add rate limiting and error handling"))
   307|```
   308|
   309|---
   310|
   311|## Stop Reasons
   312|
   313|The `stop_reason` field in the response indicates why the model stopped generating:
   314|
   315|| Value | Meaning |
   316|| --- | --- |
   317|| `end_turn` | Claude finished its response naturally |
   318|| `max_tokens` | Hit the `max_tokens` limit — increase it or use streaming |
   319|| `stop_sequence` | Hit a custom stop sequence |
   320|| `tool_use` | Claude wants to call a tool — execute it and continue |
   321|| `pause_turn` | Model paused and can be resumed (agentic flows) |
   322|| `refusal` | Claude refused for safety reasons — output may not match your schema |
   323|
   324|---
   325|
   326|## Cost Optimization Strategies
   327|
   328|### 1. Use Prompt Caching for Repeated Context
   329|
   330|```python
   331|# Automatic caching (simplest — caches the last cacheable block)
   332|response = client.messages.create(
   333|    model="claude-opus-4-7",
   334|    max_tokens=16000,
   335|    cache_control={"type": "ephemeral"},
   336|    system=large_document_text,  # e.g., 50KB of context
   337|    messages=[{"role": "user", "content": "Summarize the key points"}]
   338|)
   339|
   340|# First request: full cost
   341|# Subsequent requests: ~90% cheaper for cached portion
   342|```
   343|
   344|### 2. Choose the Right Model
   345|
   346|```python
   347|# Default to Opus for most tasks
   348|response = client.messages.create(
   349|    model="claude-opus-4-7",  # $5.00/$25.00 per 1M tokens
   350|    max_tokens=16000,
   351|    messages=[{"role": "user", "content": "Explain quantum computing"}]
   352|)
   353|
   354|# Use Sonnet for high-volume production workloads
   355|standard_response = client.messages.create(
   356|    model="claude-sonnet-4-6",  # $3.00/$15.00 per 1M tokens
   357|    max_tokens=16000,
   358|    messages=[{"role": "user", "content": "Summarize this document"}]
   359|)
   360|
   361|# Use Haiku only for simple, speed-critical tasks
   362|simple_response = client.messages.create(
   363|    model="claude-haiku-4-5",  # $1.00/$5.00 per 1M tokens
   364|    max_tokens=256,
   365|    messages=[{"role": "user", "content": "Classify this as positive or negative"}]
   366|)
   367|```
   368|
   369|### 3. Use Token Counting Before Requests
   370|
   371|```python
   372|count_response = client.messages.count_tokens(
   373|    model="claude-opus-4-7",
   374|    messages=messages,
   375|    system=system
   376|)
   377|
   378|estimated_input_cost = count_response.input_tokens * 0.000005  # $5/1M tokens
   379|print(f"Estimated input cost: ${estimated_input_cost:.4f}")
   380|```
   381|
   382|---
   383|
   384|## Retry with Exponential Backoff
   385|
   386|> **Note:** The Anthropic SDK automatically retries rate limit (429) and server errors (5xx) with exponential backoff. You can configure this with `max_retries` (default: 2). Only implement custom retry logic if you need behavior beyond what the SDK provides.
   387|
   388|```python
   389|import time
   390|import random
   391|import anthropic
   392|
   393|def call_with_retry(
   394|    client: anthropic.Anthropic,
   395|    max_retries: int = 5,
   396|    base_delay: float = 1.0,
   397|    max_delay: float = 60.0,
   398|    **kwargs
   399|):
   400|    """Call the API with exponential backoff retry."""
   401|    last_exception = None
   402|
   403|    for attempt in range(max_retries):
   404|        try:
   405|            return client.messages.create(**kwargs)
   406|        except anthropic.RateLimitError as e:
   407|            last_exception = e
   408|        except anthropic.APIStatusError as e:
   409|            if e.status_code >= 500:
   410|                last_exception = e
   411|            else:
   412|                raise  # Client errors (4xx except 429) should not be retried
   413|
   414|        delay = min(base_delay * (2 ** attempt) + random.uniform(0, 1), max_delay)
   415|        print(f"Retry {attempt + 1}/{max_retries} after {delay:.1f}s")
   416|        time.sleep(delay)
   417|
   418|    raise last_exception
   419|```
   420|