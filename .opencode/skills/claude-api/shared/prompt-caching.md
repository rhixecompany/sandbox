---
name: shared-prompt-caching
description: "Prompt Caching — Design & Optimization"
version: 1.0.0
author: Alexa
---
     1|# Prompt Caching — Design & Optimization
     2|
     3|This file covers how to design prompt-building code for effective caching. For language-specific syntax, see the `## Prompt Caching` section in each language's README or single-file doc.
     4|
     5|## The one invariant everything follows from
     6|
     7|**Prompt caching is a prefix match. Any change anywhere in the prefix invalidates everything after it.**
     8|
     9|The cache key is derived from the exact bytes of the rendered prompt up to each `cache_control` breakpoint. A single byte difference at position N — a timestamp, a reordered JSON key, a different tool in the list — invalidates the cache for all breakpoints at positions ≥ N.
    10|
    11|Render order is: `tools` → `system` → `messages`. A breakpoint on the last system block caches both tools and system together.
    12|
    13|Design the prompt-building path around this constraint. Get the ordering right and most caching works for free. Get it wrong and no amount of `cache_control` markers will help.
    14|
    15|---
    16|
    17|## Workflow for optimizing existing code
    18|
    19|When asked to add or optimize caching:
    20|
    21|1. **Trace the prompt assembly path.** Find where `system`, `tools`, and `messages` are constructed. Identify every input that flows into them.
    22|2. **Classify each input by stability:**
    23|   - Never changes → belongs early in the prompt, before any breakpoint
    24|   - Changes per-session → belongs after the global prefix, cache per-session
    25|   - Changes per-turn → belongs at the end, after the last breakpoint
    26|   - Changes per-request (timestamps, UUIDs, random IDs) → **eliminate or move to the very end**
    27|3. **Check rendered order matches stability order.** Stable content must physically precede volatile content. If a timestamp is interpolated into the system prompt header, everything after it is uncacheable regardless of markers.
    28|4. **Place breakpoints at stability boundaries.** See placement patterns below.
    29|5. **Audit for silent invalidators.** See anti-patterns table.
    30|
    31|---
    32|
    33|## Placement patterns
    34|
    35|### Large system prompt shared across many requests
    36|
    37|Put a breakpoint on the last system text block. If there are tools, they render before system — the marker on the last system block caches tools + system together.
    38|
    39|```json
    40|"system": [
    41|  {"type": "text", "text": "<large shared prompt>", "cache_control": {"type": "ephemeral"}}
    42|]
    43|```
    44|
    45|### Multi-turn conversations
    46|
    47|Put a breakpoint on the last content block of the most-recently-appended turn. Each subsequent request reuses the entire prior conversation prefix. Earlier breakpoints remain valid read points, so hits accrue incrementally as the conversation grows.
    48|
    49|```json
    50|// Last content block of the last user turn
    51|messages[-1].content[-1].cache_control = {"type": "ephemeral"}
    52|```
    53|
    54|### Shared prefix, varying suffix
    55|
    56|Many requests share a large fixed preamble (few-shot examples, retrieved docs, instructions) but differ in the final question. Put the breakpoint at the end of the **shared** portion, not at the end of the whole prompt — otherwise every request writes a distinct cache entry and nothing is ever read.
    57|
    58|```json
    59|"messages": [{"role": "user", "content": [
    60|  {"type": "text", "text": "<shared context>", "cache_control": {"type": "ephemeral"}},
    61|  {"type": "text", "text": "<varying question>"}  // no marker — differs every time
    62|]}]
    63|```
    64|
    65|### Prompts that change from the beginning every time
    66|
    67|Don't cache. If the first 1K tokens differ per request, there is no reusable prefix. Adding `cache_control` only pays the cache-write premium with zero reads. Leave it off.
    68|
    69|---
    70|
    71|## Architectural guidance
    72|
    73|These are the decisions that matter more than marker placement. Fix these first.
    74|
    75|**Keep the system prompt frozen.** Don't interpolate "current date: X", "mode: Y", "user name: Z" into the system prompt — those sit at the front of the prefix and invalidate everything downstream. Inject dynamic context as a user or assistant message later in `messages`. A message at turn 5 invalidates nothing before turn 5.
    76|
    77|**Don't change tools or model mid-conversation.** Tools render at position 0; adding, removing, or reordering a tool invalidates the entire cache. Same for switching models (caches are model-scoped). If you need "modes", don't swap the tool set — give Claude a tool that records the mode transition, or pass the mode as message content. Serialize tools deterministically (sort by name).
    78|
    79|**Fork operations must reuse the parent's exact prefix.** Side computations (summarization, compaction, sub-agents) often spin up a separate API call. If the fork rebuilds `system` / `tools` / `model` with any difference, it misses the parent's cache entirely. Copy the parent's `system`, `tools`, and `model` verbatim, then append fork-specific content at the end.
    80|
    81|---
    82|
    83|## Silent invalidators
    84|
    85|When reviewing code, grep for these inside anything that feeds the prompt prefix:
    86|
    87|| Pattern | Why it breaks caching |
    88|| --- | --- |
    89|| `datetime.now()` / `Date.now()` / `time.time()` in system prompt | Prefix changes every request |
    90|| `uuid4()` / `crypto.randomUUID()` / request IDs early in content | Same — every request is unique |
    91|| `json.dumps(d)` without `sort_keys=True` / iterating a `set` | Non-deterministic serialization → prefix bytes differ |
    92|| f-string interpolating session/user ID into system prompt | Per-user prefix; no cross-user sharing |
    93|| Conditional system sections (`if flag: system += ...`) | Every flag combination is a distinct prefix |
    94|| `tools=build_tools(user)` where set varies per user | Tools render at position 0; nothing caches across users |
    95|
    96|Fix by moving the dynamic piece after the last breakpoint, making it deterministic, or deleting it if it's not load-bearing.
    97|
    98|---
    99|
   100|## API reference
   101|
   102|```json
   103|"cache_control": {"type": "ephemeral"}              // 5-minute TTL (default)
   104|"cache_control": {"type": "ephemeral", "ttl": "1h"} // 1-hour TTL
   105|```
   106|
   107|- Max **4** `cache_control` breakpoints per request.
   108|- Goes on any content block: system text blocks, tool definitions, message content blocks (`text`, `image`, `tool_use`, `tool_result`, `document`).
   109|- Top-level `cache_control` on `messages.create()` auto-places on the last cacheable block — simplest option when you don't need fine-grained placement.
   110|- Minimum cacheable prefix is model-dependent. Shorter prefixes silently won't cache even with a marker — no error, just `cache_creation_input_tokens: 0`:
   111|
   112|| Model                                        |     Minimum |
   113|| -------------------------------------------- | ----------: |
   114|| Opus 4.7, Opus 4.6, Opus 4.5, Haiku 4.5      | 4096 tokens |
   115|| Sonnet 4.6, Haiku 3.5, Haiku 3               | 2048 tokens |
   116|| Sonnet 4.5, Sonnet 4.1, Sonnet 4, Sonnet 3.7 | 1024 tokens |
   117|
   118|A 3K-token prompt caches on Sonnet 4.5 but silently won't on Opus 4.7.
   119|
   120|**Economics:** Cache reads cost ~0.1× base input price. Cache writes cost **1.25× for 5-minute TTL, 2× for 1-hour TTL**. Break-even depends on TTL: with 5-minute TTL, two requests break even (1.25× + 0.1× = 1.35× vs 2× uncached); with 1-hour TTL, you need at least three requests (2× + 0.2× = 2.2× vs 3× uncached). The 1-hour TTL keeps entries alive across gaps in bursty traffic, but the doubled write cost means it needs more reads to pay off.
   121|
   122|---
   123|
   124|## Verifying cache hits
   125|
   126|The response `usage` object reports cache activity:
   127|
   128|| Field | Meaning |
   129|| --- | --- |
   130|| `cache_creation_input_tokens` | Tokens written to cache this request (you paid the ~1.25× write premium) |
   131|| `cache_read_input_tokens` | Tokens served from cache this request (you paid ~0.1×) |
   132|| `input_tokens` | Tokens processed at full price (not cached) |
   133|
   134|If `cache_read_input_tokens` is zero across repeated requests with identical prefixes, a silent invalidator is at work — diff the rendered prompt bytes between two requests to find it.
   135|
   136|**`input_tokens` is the uncached remainder only.** Total prompt size = `input_tokens + cache_creation_input_tokens + cache_read_input_tokens`. If your agent ran for hours but `input_tokens` shows 4K, the rest was served from cache — check the sum, not the single field.
   137|
   138|Language-specific access: `response.usage.cache_read_input_tokens` (Python/TS/Ruby), `$message->usage->cacheReadInputTokens` (PHP), `resp.Usage.CacheReadInputTokens` (Go/C#), `.usage().cacheReadInputTokens()` (Java).
   139|
   140|---
   141|
   142|## Invalidation hierarchy
   143|
   144|Not every parameter change invalidates everything. The API has three cache tiers, and changes only invalidate their own tier and below:
   145|
   146|| Change | Tools cache | System cache | Messages cache |
   147|| --- | :-: | :-: | :-: |
   148|| Tool definitions (add/remove/reorder) | ❌ | ❌ | ❌ |
   149|| Model switch | ❌ | ❌ | ❌ |
   150|| `speed`, web-search, citations toggle | ✅ | ❌ | ❌ |
   151|| System prompt content | ✅ | ❌ | ❌ |
   152|| `tool_choice`, images, `thinking` enable/disable | ✅ | ✅ | ❌ |
   153|| Message content | ✅ | ✅ | ❌ |
   154|
   155|Implication: you can change `tool_choice` per-request or toggle `thinking` without losing the tools+system cache. Don't over-worry about these — only tool-definition and model changes force a full rebuild.
   156|
   157|---
   158|
   159|## 20-block lookback window
   160|
   161|Each breakpoint walks backward **at most 20 content blocks** to find a prior cache entry. If a single turn adds more than 20 blocks (common in agentic loops with many tool_use/tool_result pairs), the next request's breakpoint won't find the previous cache and silently misses.
   162|
   163|Fix: place an intermediate breakpoint every ~15 blocks in long turns, or put the marker on a block that's within 20 of the previous turn's last cached block.
   164|
   165|---
   166|
   167|## Concurrent-request timing
   168|
   169|A cache entry becomes readable only after the first response **begins streaming**. N parallel requests with identical prefixes all pay full price — none can read what the others are still writing.
   170|
   171|For fan-out patterns: send 1 request, await the first streamed token (not the full response), then fire the remaining N−1. They'll read the cache the first one just wrote.
   172|