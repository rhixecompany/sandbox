---
name: shared-models
description: "Claude Model Catalog"
version: 1.0.0
author: Alexa
---
     1|# Claude Model Catalog
     2|
     3|**Only use exact model IDs listed in this file.** Never guess or construct model IDs — incorrect IDs will cause API errors. Use aliases wherever available. For the latest information, WebFetch the Models Overview URL in `shared/live-sources.md`, or query the Models API directly (see Programmatic Model Discovery below).
     4|
     5|## Programmatic Model Discovery
     6|
     7|For **live** capability data — context window, max output tokens, feature support (thinking, vision, effort, structured outputs, etc.) — query the Models API instead of relying on the cached tables below. Use this when the user asks "what's the context window for X", "does model X support vision/thinking/effort", "which models support feature Y", or wants to select a model by capability at runtime.
     8|
     9|```python
    10|m = client.models.retrieve("claude-opus-4-7")
    11|m.id                 # "claude-opus-4-7"
    12|m.display_name       # "Claude Opus 4.7"
    13|m.max_input_tokens   # context window (int)
    14|m.max_tokens         # max output tokens (int)
    15|
    16|# capabilities is an untyped nested dict — bracket access, check ["supported"] at the leaf
    17|caps = m.capabilities
    18|caps["image_input"]["supported"]                       # vision
    19|caps["thinking"]["types"]["adaptive"]["supported"]     # adaptive thinking
    20|caps["effort"]["max"]["supported"]                     # effort: max (also low/medium/high)
    21|caps["structured_outputs"]["supported"]
    22|caps["context_management"]["compact_20260112"]["supported"]
    23|
    24|# filter across all models — iterate the page object directly (auto-paginates); do NOT use .data
    25|[m for m in client.models.list()
    26| if m.capabilities["thinking"]["types"]["adaptive"]["supported"]
    27| and m.max_input_tokens >= 200_000]
    28|```
    29|
    30|Top-level fields (`id`, `display_name`, `max_input_tokens`, `max_tokens`) are typed attributes. `capabilities` is a dict — use bracket access, not attribute access. The API returns the full capability tree for every model with `supported: true/false` at each leaf, so bracket chains are safe without `.get()` guards. TypeScript SDK: same method names, also auto-paginates on iteration.
    31|
    32|### Raw HTTP
    33|
    34|```bash
    35|curl https://api.anthropic.com/v1/models/claude-opus-4-7 \
    36|  -H "x-api-key: $ANTHROPIC_API_KEY" \
    37|  -H "anthropic-version: 2023-06-01"
    38|```
    39|
    40|```json
    41|{
    42|  "id": "claude-opus-4-7",
    43|  "display_name": "Claude Opus 4.7",
    44|  "max_input_tokens": 200000,
    45|  "max_tokens": 128000,
    46|  "capabilities": {
    47|    "image_input": {"supported": true},
    48|    "structured_outputs": {"supported": true},
    49|    "thinking": {"supported": true, "types": {"enabled": {"supported": false}, "adaptive": {"supported": true}}},
    50|    "effort": {"supported": true, "low": {"supported": true}, …, "max": {"supported": true}},
    51|    …
    52|  }
    53|}
    54|```
    55|
    56|## Current Models (recommended)
    57|
    58|| Friendly Name | Alias (use this) | Full ID | Context | Max Output | Status |
    59|| --- | --- | --- | --- | --- | --- |
    60|| Claude Opus 4.7 | `claude-opus-4-7` | — | 1M | 128K | Active |
    61|| Claude Opus 4.6 | `claude-opus-4-6` | — | 1M | 128K | Active |
    62|| Claude Sonnet 4.6 | `claude-sonnet-4-6` | - | 1M | 64K | Active |
    63|| Claude Haiku 4.5 | `claude-haiku-4-5` | `claude-haiku-4-5-20251001` | 200K | 64K | Active |
    64|
    65|### Model Descriptions
    66|
    67|- **Claude Opus 4.7** — The most capable Claude model to date — highly autonomous, strong on long-horizon agentic work, knowledge work, vision, and memory. Adaptive thinking only; sampling parameters and `budget_tokens` are removed. 1M context window at standard API pricing (no long-context premium) — see `shared/model-migration.md` → Migrating to Opus 4.7 for breaking changes.
    68|- **Claude Opus 4.6** — Previous-generation Opus. Supports adaptive thinking (recommended), 128K max output tokens (requires streaming for large outputs). 1M context window.
    69|- **Claude Sonnet 4.6** — Our best combination of speed and intelligence. Supports adaptive thinking (recommended). 1M context window. 64K max output tokens.
    70|- **Claude Haiku 4.5** — Fastest and most cost-effective model for simple tasks.
    71|
    72|## Legacy Models (still active)
    73|
    74|| Friendly Name | Alias (use this) | Full ID | Status |
    75|| --- | --- | --- | --- |
    76|| Claude Opus 4.5 | `claude-opus-4-5` | `claude-opus-4-5-20251101` | Active |
    77|| Claude Opus 4.1 | `claude-opus-4-1` | `claude-opus-4-1-20250805` | Active |
    78|| Claude Sonnet 4.5 | `claude-sonnet-4-5` | `claude-sonnet-4-5-20250929` | Active |
    79|| Claude Sonnet 4 | `claude-sonnet-4-0` | `claude-sonnet-4-20250514` | Active |
    80|| Claude Opus 4 | `claude-opus-4-0` | `claude-opus-4-20250514` | Active |
    81|
    82|## Deprecated Models (retiring soon)
    83|
    84|| Friendly Name | Alias (use this) | Full ID | Status | Retires |
    85|| --- | --- | --- | --- | --- |
    86|| Claude Haiku 3 | — | `claude-3-haiku-20240307` | Deprecated | Apr 19, 2026 |
    87|
    88|## Retired Models (no longer available)
    89|
    90|| Friendly Name     | Full ID                      | Retired      |
    91|| ----------------- | ---------------------------- | ------------ |
    92|| Claude Sonnet 3.7 | `claude-3-7-sonnet-20250219` | Feb 19, 2026 |
    93|| Claude Haiku 3.5  | `claude-3-5-haiku-20241022`  | Feb 19, 2026 |
    94|| Claude Opus 3     | `claude-3-opus-20240229`     | Jan 5, 2026  |
    95|| Claude Sonnet 3.5 | `claude-3-5-sonnet-20241022` | Oct 28, 2025 |
    96|| Claude Sonnet 3.5 | `claude-3-5-sonnet-20240620` | Oct 28, 2025 |
    97|| Claude Sonnet 3   | `claude-3-sonnet-20240229`   | Jul 21, 2025 |
    98|| Claude 2.1        | `claude-2.1`                 | Jul 21, 2025 |
    99|| Claude 2.0        | `claude-2.0`                 | Jul 21, 2025 |
   100|
   101|## Resolving User Requests
   102|
   103|When a user asks for a model by name, use this table to find the correct model ID:
   104|
   105|| User says...             | Use this model ID                       |
   106|| ------------------------ | --------------------------------------- |
   107|| "opus", "most powerful"  | `claude-opus-4-7`                       |
   108|| "opus 4.7"               | `claude-opus-4-7`                       |
   109|| "opus 4.6"               | `claude-opus-4-6`                       |
   110|| "opus 4.5"               | `claude-opus-4-5`                       |
   111|| "opus 4.1"               | `claude-opus-4-1`                       |
   112|| "opus 4", "opus 4.0"     | `claude-opus-4-0`                       |
   113|| "sonnet", "balanced"     | `claude-sonnet-4-6`                     |
   114|| "sonnet 4.6"             | `claude-sonnet-4-6`                     |
   115|| "sonnet 4.5"             | `claude-sonnet-4-5`                     |
   116|| "sonnet 4", "sonnet 4.0" | `claude-sonnet-4-0`                     |
   117|| "sonnet 3.7"             | Retired — suggest `claude-sonnet-4-5`   |
   118|| "sonnet 3.5"             | Retired — suggest `claude-sonnet-4-5`   |
   119|| "haiku", "fast", "cheap" | `claude-haiku-4-5`                      |
   120|| "haiku 4.5"              | `claude-haiku-4-5`                      |
   121|| "haiku 3.5"              | Retired — suggest `claude-haiku-4-5`    |
   122|| "haiku 3"                | Deprecated — suggest `claude-haiku-4-5` |
   123|