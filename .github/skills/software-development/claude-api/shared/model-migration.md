---
name: shared-model-migration
description: "Model Migration Guide"
version: 1.0.0
author: Alexa
---
     1|# Model Migration Guide
     2|
     3|How to move existing code to newer Claude models. Covers breaking changes, deprecated parameters, and drop-in replacements for retired models.
     4|
     5|For the latest, authoritative version (with code samples in every supported language), WebFetch the **Migration Guide** URL from `shared/live-sources.md`. Use this file for the consolidated, skill-resident reference; fall back to the live docs whenever a model launch or breaking change may have shifted the picture.
     6|
     7|**This file is large.** Use the section names below to jump (or `Grep` this file for the heading text). Read Step 0 and Step 1 first — they apply to every migration. Then read only the per-target section for the model you are migrating to.
     8|
     9|| Section | When you need it |
    10|| --- | --- |
    11|| Step 0: Confirm the migration scope | Always — before any edits |
    12|| Step 1: Classify each file | Always — decides whether to swap, add-alongside, or skip |
    13|| Per-SDK Syntax Reference | Translate the Python examples in this guide to TypeScript / Go / Ruby / Java / C# / PHP |
    14|| Destination Models / Retired Model Replacements | Picking a target model |
    15|| Breaking Changes by Source Model | Migrating to Opus 4.6 / Sonnet 4.6 |
    16|| Migrating to Opus 4.7 | Migrating to Opus 4.7 (breaking changes, silent defaults, behavioral shifts) |
    17|| Opus 4.7 Migration Checklist | The required vs optional items for 4.7, tagged `[BLOCKS]` / `[TUNE]` |
    18|| Verify the Migration | After edits — runtime spot-check |
    19|
    20|**TL;DR:** Change the model ID string. If you were using `budget_tokens`, switch to `thinking: {type: "adaptive"}`. If you were using assistant prefills, they 400 on both Opus 4.6 and Sonnet 4.6 — switch to one of the prefill replacements (most often `output_config.format`; see the table in Breaking Changes by Source Model). If you're moving from Sonnet 4.5 to Sonnet 4.6, set `effort` explicitly — 4.6 defaults to `high`. Remove the `effort-2025-11-24` and `fine-grained-tool-streaming-2025-05-14` beta headers (GA on 4.6); remove `interleaved-thinking-2025-05-14` once you're on adaptive thinking (keep it only while using the transitional `budget_tokens` escape hatch). Then drop back from `client.beta.messages.create` to `client.messages.create`. Dial back any aggressive "CRITICAL: YOU MUST" tool instructions; 4.6 follows the system prompt much more closely.
    21|
    22|---
    23|
    24|## Step 0: Confirm the migration scope
    25|
    26|**Before any Write, Edit, or MultiEdit call, confirm the scope.** If the user's request does not explicitly name a single file, a specific directory, or an explicit file list, **ask first — do not start editing**. This is non-negotiable: even imperative-sounding requests like "migrate my codebase", "move my project to X", "upgrade to Sonnet 4.6", or bare "migrate to Opus 4.7" leave the scope ambiguous and require a clarifying question. Phrases like "my project", "my code", "my codebase", "the whole thing", "everywhere", or "across the repo" are **ambiguous, not directive** — they tell you _what_ to do but not _where_. Ask before doing.
    27|
    28|Offer the common scopes explicitly and wait for the answer before touching any file:
    29|
    30|1. The entire working directory
    31|2. A specific subdirectory (e.g. `src/`, `app/`, `services/billing/`)
    32|3. A specific file or a list of files
    33|
    34|Surface this as a single clarifying question so the user can answer in one turn. **Proceed without asking only when the scope is already unambiguous** — the user named an exact file ("migrate `extract.py` to Sonnet 4.6"), pointed at a specific directory ("migrate everything under `services/billing/` to Opus 4.6"), listed specific files ("update `a.py` and `b.py`"), or already answered the scope question in an earlier turn. If you can answer the question "which files is this change going to touch?" with a precise list from the prompt alone, proceed. If not, ask.
    35|
    36|**Worked example.** If the user says _"Move my project to Opus 4.6. I want adaptive thinking everywhere it makes sense."_ you do not know whether "my project" means the whole working directory, just `src/`, just the production code, or something else — the `everywhere` makes the intent clear (update every call site _within scope_) but the scope itself is still not defined. Do not start editing. Respond with:
    37|
    38|> Before I start editing, can you confirm the scope? I can migrate:
    39|>
    40|> 1. Every `.py` file in the working directory
    41|> 2. Just the files under `src/` (production code)
    42|> 3. A specific subdirectory or list of files you name
    43|>
    44|> Which one?
    45|
    46|Then wait for the answer. The same applies to _"Migrate to Opus 4.7"_ and bare _"Help me upgrade to Sonnet 4.6"_ — ask before editing.
    47|
    48|**Sizing the scope question (large repos).** Before asking, get a per-directory count so the user can pick concretely:
    49|
    50|```sh
    51|rg -l "<old-model-id>" --type-not md | cut -d/ -f1 | sort | uniq -c | sort -rn
    52|```
    53|
    54|Present the breakdown in your scope question (e.g. _"Found 217 references across 3 directories: api/ (130), api-go/ (62), routing/ (25). Which to migrate?"_). Also confirm `git status` is clean before surveying — unexpected modifications mean a concurrent process; stop and investigate before proceeding.
    55|
    56|---
    57|
    58|## Step 1: Classify each file
    59|
    60|Not every file that contains the old model ID is a **caller** of the API. Before editing, classify each file into one of these buckets — the right action differs:
    61|
    62|| # | Bucket | What it looks like | Action |
    63|| --- | --- | --- | --- |
    64|| 1 | **Calls the API/SDK** | `client.messages.create(model=…)`, `anthropic.Anthropic()`, request payloads | Swap the model ID **and** apply the breaking-change checklist for the target version (below). |
    65|| 2 | **Defines or serves the model** | Model registries, OpenAPI specs, routing/queue configs, model-policy enums, generated catalogs | The old entry **stays** (the model is still served). Ask whether to (a) add the new model alongside, (b) leave alone, or (c) retire the old model — never blind-replace. **If you can't ask, default to (a): add the new model alongside and flag it** — replacing would de-register a model that's still in production. |
    66|| 3 | **References the ID as an opaque string** | UI fallback constants, capability-gate substring checks, generic test fixtures, label parsers, env defaults | Usually swap the string and verify any parser/regex/substring match handles the new ID — but check the sub-cases below first. |
    67|| 4 | **Suffixed variant ID** | `claude-<model>-<suffix>` like `-fast`, `-1024k`, `-200k`, `[1m]`, dated snapshots | These are deployment/routing identifiers, not the public model ID. **Do not assume a new-model equivalent exists.** Verify in the registry first; if absent, leave the string alone and flag it. |
    68|
    69|**Bucket 3 sub-cases — before swapping a string reference, check:**
    70|
    71|- **Capability gate** (e.g. `if 'opus-4-6' in model_id:` enables a feature) → **add the new ID alongside**, don't replace. The old model is still served and still has the capability, so replacing would silently disable the feature for any old-model traffic that still flows through. If you know no old-model traffic will hit this gate (single-caller codebase fully migrating), replacing is fine; if unsure, add alongside.
    72|- **Registry-assert test** (e.g. `assert "claude-X" in supported_models`, `test_X_has_N_clusters`) → **add an assertion for the new model alongside; keep the old one.** The old model is still served, so its assertion stays valid — but the registry should also include the new model, so assert that too. Heuristic: if the test references multiple model versions in a list, it's a registry test; if one model in a struct compared only to itself, it's a generic fixture.
    73|- **Frozen / generated snapshot** → **regenerate**, don't hand-edit.
    74|- **Coupled to a definer** (e.g. an integration test that passes model authorization via a shared `conftest` seed list, or asserts on a billing-tier / rate-limit-group enum or a generated SKU/pricing catalog) → **verify the definer has a new-model entry first.** If not, add a seed entry (reusing the nearest existing tier as a placeholder); if you can't confidently do that, ask the user how to populate the definer. **Do not skip the test.** Swapping without populating the definer will make the test fail at runtime.
    75|
    76|When migrating tests specifically: breaking parameters (`temperature`, `top_p`, `budget_tokens`) are usually absent — test fixtures rarely set sampling params on placeholder models. The breaking-change scan is still required, but expect mostly clean results.
    77|
    78|**Find intentionally-flagged sync points first.** Many codebases tag spots that must change at every model launch with comment markers like `MODEL LAUNCH`, `KEEP IN SYNC`, `@model-update`, or similar. Grep for whatever convention the repo uses _before_ the broad model-ID grep — those markers point at the load-bearing changes.
    79|
    80|---
    81|
    82|## Per-SDK Syntax Reference
    83|
    84|Code examples in this guide are Python. **The same fields exist in every official Anthropic SDK** — Stainless generates all 7 from the same OpenAPI spec, so JSON field names map 1:1 with only case-convention differences. Use the rows below to translate the Python examples to the SDK you are migrating.
    85|
    86|> **Verify type and method names against the SDK source before writing them into customer code.** WebFetch the relevant repository from the SDK source-code table in `shared/live-sources.md` (one row per SDK) and confirm the exact symbol — particularly for typed SDKs (Go, Java, C#) where union/builder names can differ from the JSON shape. Do not guess type names that aren't in the table below or in `<lang>/claude-api/README.md`.
    87|
    88|### `thinking` — `budget_tokens` → adaptive
    89|
    90|| SDK | Before | After |
    91|| --- | --- | --- |
    92|| Python | `thinking={"type": "enabled", "budget_tokens": N}` | `thinking={"type": "adaptive"}` |
    93|| TypeScript | `thinking: { type: 'enabled', budget_tokens: N }` | `thinking: { type: 'adaptive' }` |
    94|| Go | `Thinking: anthropic.ThinkingConfigParamOfEnabled(N)` | `Thinking: anthropic.ThinkingConfigParamUnion{OfAdaptive: &anthropic.ThinkingConfigAdaptiveParam{}}` |
    95|| Ruby | `thinking: { type: "enabled", budget_tokens: N }` | `thinking: { type: "adaptive" }` |
    96|| Java | `.thinking(ThinkingConfigEnabled.builder().budgetTokens(N).build())` | `.thinking(ThinkingConfigAdaptive.builder().build())` |
    97|| C# | `Thinking = new ThinkingConfigEnabled { BudgetTokens = N }` | `Thinking = new ThinkingConfigAdaptive()` |
    98|| PHP | `thinking: ['type' => 'enabled', 'budget_tokens' => N]` | `thinking: ['type' => 'adaptive']` |
    99|
   100|### Sampling parameters — `temperature` / `top_p` / `top_k`
   101|
   102|(Remove the field entirely on Opus 4.7; on Claude 4.x keep at most one of `temperature` or `top_p`.)
   103|
   104|| SDK | Field(s) to remove |
   105|| --- | --- |
   106|| Python | `temperature=…`, `top_p=…`, `top_k=…` |
   107|| TypeScript | `temperature: …`, `top_p: …`, `top_k: …` |
   108|| Go | `Temperature: anthropic.Float(…)`, `TopP: anthropic.Float(…)`, `TopK: anthropic.Int(…)` |
   109|| Ruby | `temperature: …`, `top_p: …`, `top_k: …` |
   110|| Java | `.temperature(…)`, `.topP(…)`, `.topK(…)` |
   111|| C# | `Temperature = …`, `TopP = …`, `TopK = …` |
   112|| PHP | `temperature: …`, `topP: …`, `topK: …` |
   113|
   114|### Prefill replacement — structured outputs via `output_config.format`
   115|
   116|| SDK | Remove (last assistant turn) | Add |
   117|| --- | --- | --- |
   118|| Python | `{"role": "assistant", "content": "…"}` | `output_config={"format": {"type": "json_schema", "schema": SCHEMA}}` |
   119|| TypeScript | `{ role: 'assistant', content: '…' }` | `output_config: { format: { type: 'json_schema', schema: SCHEMA } }` |
   120|| Go | trailing `anthropic.MessageParam{Role: "assistant", …}` | `OutputConfig: anthropic.OutputConfigParam{Format: anthropic.JSONOutputFormatParam{…}}` |
   121|| Ruby | `{ role: "assistant", content: "…" }` | `output_config: { format: { type: "json_schema", schema: SCHEMA } }` |
   122|| Java | trailing `Message.builder().role(ASSISTANT)…` | `.outputConfig(OutputConfig.builder().format(JsonOutputFormat.builder()…build()).build())` |
   123|| C# | trailing `new Message { Role = "assistant", … }` | `OutputConfig = new OutputConfig { Format = new JsonOutputFormat { … } }` |
   124|| PHP | trailing `['role' => 'assistant', 'content' => '…']` | `outputConfig: ['format' => ['type' => 'json_schema', 'schema' => $SCHEMA]]` |
   125|
   126|### `thinking.display` — opt back into summarized reasoning (Opus 4.7)
   127|
   128|| SDK | Add |
   129|| --- | --- |
   130|| Python | `thinking={"type": "adaptive", "display": "summarized"}` |
   131|| TypeScript | `thinking: { type: 'adaptive', display: 'summarized' }` |
   132|| Go | `Thinking: anthropic.ThinkingConfigParamUnion{OfAdaptive: &anthropic.ThinkingConfigAdaptiveParam{Display: anthropic.ThinkingConfigAdaptiveDisplaySummarized}}` |
   133|| Ruby | `thinking: { type: "adaptive", display: "summarized" }` (or `display_:` when constructing the model class directly) |
   134|| Java | `.thinking(ThinkingConfigAdaptive.builder().display(ThinkingConfigAdaptive.Display.SUMMARIZED).build())` |
   135|| C# | `Thinking = new ThinkingConfigAdaptive { Display = Display.Summarized }` |
   136|| PHP | `thinking: ['type' => 'adaptive', 'display' => 'summarized']` |
   137|
   138|For any field not in these tables, the JSON key in the Python example translates directly: `snake_case` for Python/TypeScript/Ruby, `camelCase` named args for PHP, `PascalCase` struct fields for Go/C#, `camelCase` builder methods for Java.
   139|
   140|---
   141|
   142|## Explain every change you make
   143|
   144|Migration edits often look arbitrary to a user who hasn't read the release notes — a removed `temperature`, a deleted prefill, a rewritten system-prompt sentence. **For each edit, tell the user what you changed and why**, tied to the specific API or behavioral change that motivates it. Do this in your summary as you work, not just at the end.
   145|
   146|Be especially explicit about **system-prompt edits**. Users are rightly protective of their prompts, and prompt-tuning changes are judgment calls (not hard API requirements). For any prompt edit:
   147|
   148|- Quote the before and after text.
   149|- State the behavioral shift that motivates it (e.g. _"Opus 4.7 calibrates response length to task complexity, so I added an explicit length instruction"_, or _"4.6 follows instructions more literally, so 'CRITICAL: YOU MUST use the search tool' will now overtrigger — softened to 'Use the search tool when…'"_).
   150|- Make clear which prompt edits are **optional tuning** (tone, length, subagent guidance) versus which code edits are **required to avoid a 400** (sampling params, `budget_tokens`, prefills). Never present an optional prompt change as mandatory.
   151|
   152|If you're applying several prompt-tuning edits at once, offer them as a short list the user can accept or decline item-by-item rather than silently rewriting their system prompt.
   153|
   154|---
   155|
   156|## Before You Migrate
   157|
   158|1. **Confirm the target model ID.** Use only the exact strings from `shared/models.md` — do not append date suffixes to aliases (`claude-opus-4-6`, not `claude-opus-4-6-20251101`). Guessing an ID will 404.
   159|2. **Check which features your code uses** with this checklist:
   160|   - `thinking: {type: "enabled", budget_tokens: N}` → migrate to adaptive thinking on Opus 4.6 / Sonnet 4.6 (still functional but deprecated)
   161|   - Assistant-turn prefills (`messages` ending with `role: "assistant"`) → must change on Opus 4.6 / Sonnet 4.6 (returns 400)
   162|   - `output_format` parameter on `messages.create()` → must change on all models (deprecated API-wide)
   163|   - `max_tokens > ~16000` → must stream on any model (above ~16K risks SDK HTTP timeouts). When streaming, Sonnet 4.6 / Haiku 4.5 cap at 64K and Opus 4.6 caps at 128K
   164|   - Beta headers `effort-2025-11-24`, `fine-grained-tool-streaming-2025-05-14`, `interleaved-thinking-2025-05-14` → GA on 4.6, remove them and switch from `client.beta.messages.create` to `client.messages.create`
   165|   - Moving Sonnet 4.5 → Sonnet 4.6 with no `effort` set → 4.6 defaults to `high`, which may change your latency/cost profile
   166|   - System prompts with `CRITICAL`, `MUST`, `If in doubt, use X` language → likely to overtrigger on 4.6 (see Prompt-Behavior Changes)
   167|   - Coming from 3.x / 4.0 / 4.1: also check sampling params (`temperature` + `top_p`), tool versions (`text_editor_20250728`), `refusal` + `model_context_window_exceeded` stop reasons, trailing-newline tool-param handling
   168|3. **Test on a single request first.** Run one call against the new model, inspect the response, then roll out.
   169|
   170|---
   171|
   172|## Destination Models (recommended targets)
   173|
   174|| If you're on… | Migrate to | Why |
   175|| --- | --- | --- |
   176|| Opus 4.6 | `claude-opus-4-7` | Most capable model; adaptive thinking only; high-res vision; see Migrating to Opus 4.7 |
   177|| Opus 4.0 / 4.1 / 4.5 / Opus 3 | `claude-opus-4-6` | Most intelligent 4.x before 4.7; adaptive thinking; 128K output |
   178|| Sonnet 4.0 / 4.5 / 3.7 / 3.5 | `claude-sonnet-4-6` | Best speed / intelligence balance; adaptive thinking; 64K output |
   179|| Haiku 3 / 3.5 | `claude-haiku-4-5` | Fastest and most cost-effective |
   180|
   181|Default to the latest Opus for the caller's tier unless they explicitly chose otherwise. If you're moving from Opus 4.5 or older directly to Opus 4.7, apply the 4.6 migration first, then layer the Opus 4.7 changes on top (see Migrating to Opus 4.7 below).
   182|
   183|---
   184|
   185|## Retired Model Replacements
   186|
   187|These models return 404 — update immediately:
   188|
   189|| Retired model                | Retired      | Drop-in replacement |
   190|| ---------------------------- | ------------ | ------------------- |
   191|| `claude-3-7-sonnet-20250219` | Feb 19, 2026 | `claude-sonnet-4-6` |
   192|| `claude-3-5-haiku-20241022`  | Feb 19, 2026 | `claude-haiku-4-5`  |
   193|| `claude-3-opus-20240229`     | Jan 5, 2026  | `claude-opus-4-7`   |
   194|| `claude-3-5-sonnet-20241022` | Oct 28, 2025 | `claude-sonnet-4-6` |
   195|| `claude-3-5-sonnet-20240620` | Oct 28, 2025 | `claude-sonnet-4-6` |
   196|| `claude-3-sonnet-20240229`   | Jul 21, 2025 | `claude-sonnet-4-6` |
   197|| `claude-2.1`, `claude-2.0`   | Jul 21, 2025 | `claude-sonnet-4-6` |
   198|
   199|## Deprecated Models (retiring soon)
   200|
   201|| Model                      | Retires       | Replacement         |
   202|| -------------------------- | ------------- | ------------------- |
   203|| `claude-3-haiku-20240307`  | Apr 19, 2026  | `claude-haiku-4-5`  |
   204|| `claude-opus-4-20250514`   | June 15, 2026 | `claude-opus-4-7`   |
   205|| `claude-sonnet-4-20250514` | June 15, 2026 | `claude-sonnet-4-6` |
   206|
   207|---
   208|
   209|## Breaking Changes by Source Model
   210|
   211|### Migrating from Sonnet 4.5 to Sonnet 4.6 (effort default change)
   212|
   213|Sonnet 4.5 had no `effort` parameter; Sonnet 4.6 defaults to `high`. If you just switch the model string and do nothing else, you may see noticeably higher latency and token usage. Set `effort` explicitly.
   214|
   215|**Recommended starting points:**
   216|
   217|| Workload | Start at | Notes |
   218|| --- | --- | --- |
   219|| Chat, classification, content generation | `low` | With `thinking: {"type": "disabled"}` you'll see similar or better performance vs. Sonnet 4.5 no-thinking |
   220|| Most applications (balanced) | `medium` | The default sweet spot for quality vs. cost |
   221|| Agentic coding, tool-heavy workflows | `medium` | Pair with adaptive thinking and a generous `max_tokens` (up to 64K with streaming — Sonnet 4.6's ceiling) |
   222|| Autonomous multi-step agents, long-horizon loops | `high` | Scale down to `medium` if latency/tokens become a concern |
   223|| Computer-use agents | `high` + adaptive | Sonnet 4.6's best computer-use accuracy is on adaptive + high |
   224|
   225|For non-thinking chat workloads specifically:
   226|
   227|```python
   228|client.messages.create(
   229|    model="claude-sonnet-4-6",
   230|    max_tokens=8192,
   231|    thinking={"type": "disabled"},
   232|    output_config={"effort": "low"},
   233|    messages=[{"role": "user", "content": "..."}],
   234|)
   235|```
   236|
   237|**When to use Opus 4.6 instead:** hardest and longest-horizon problems — large code migrations, deep research, extended autonomous work. Sonnet 4.6 wins on fast turnaround and cost efficiency.
   238|
   239|### Migrating to Opus 4.6 / Sonnet 4.6 (from any older model)
   240|
   241|**1. Manual extended thinking is deprecated — use adaptive thinking.**
   242|
   243|`thinking: {type: "enabled", budget_tokens: N}` (manual extended thinking with a fixed token budget) is deprecated on Opus 4.6 and Sonnet 4.6. Replace it with `thinking: {type: "adaptive"}`, which lets Claude decide when and how much to think. Adaptive thinking also enables interleaved thinking automatically (no beta header needed).
   244|
   245|```python
   246|# Old (still works on older models, deprecated on 4.6)
   247|response = client.messages.create(
   248|    model="claude-sonnet-4-5",
   249|    max_tokens=16000,
   250|    thinking={"type": "enabled", "budget_tokens": 8000},
   251|    messages=[...]
   252|)
   253|
   254|# New (Opus 4.6 / Sonnet 4.6)
   255|response = client.messages.create(
   256|    model="claude-opus-4-6",  # or "claude-sonnet-4-6"
   257|    max_tokens=16000,
   258|    thinking={"type": "adaptive"},
   259|    output_config={"effort": "high"},  # optional: low | medium | high | max
   260|    messages=[...]
   261|)
   262|```
   263|
   264|Adaptive thinking is the long-term target, and on internal evaluations it outperforms manual extended thinking. Move when you can.
   265|
   266|**Transitional escape hatch:** manual extended thinking is still _functional_ on Opus 4.6 and Sonnet 4.6 (deprecated, will be removed in a future release). If you need a hard ceiling while migrating — for example, to bound token spend on a runaway workload before you've tuned `effort` — you can keep `budget_tokens` around alongside an explicit `effort` value, then remove it in a follow-up. `budget_tokens` must be strictly less than `max_tokens`:
   267|
   268|```python
   269|# Transitional only — deprecated, plan to remove
   270|client.messages.create(
   271|    model="claude-sonnet-4-6",
   272|    max_tokens=16384,
   273|    thinking={"type": "enabled", "budget_tokens": 8192},  # must be < max_tokens
   274|    output_config={"effort": "medium"},
   275|    messages=[...],
   276|)
   277|```
   278|
   279|If the user asks for a "thinking budget" on 4.6, the preferred answer is `effort` — use `low`, `medium`, `high`, or `max` (Opus-tier only — not Sonnet or Haiku) rather than a token count.
   280|
   281|**2. Effort parameter (Opus 4.5, Opus 4.6, Sonnet 4.6 only).**
   282|
   283|Controls thinking depth and overall token spend. Goes inside `output_config`, not top-level. Default is `high`. `max` is Opus-tier only (Opus 4.6 and later — not Sonnet or Haiku). Errors on Sonnet 4.5 and Haiku 4.5.
   284|
   285|```python
   286|output_config={"effort": "medium"}  # often the best cost / quality balance
   287|```
   288|
   289|### Migrating to the 4.6 family (Opus 4.6 and Sonnet 4.6)
   290|
   291|**3. Assistant-turn prefills return 400 (Opus 4.6 and Sonnet 4.6).**
   292|
   293|Prefilled responses on the final assistant turn are no longer supported on either Opus 4.6 or Sonnet 4.6 — both return a 400. Adding assistant messages _elsewhere_ in the conversation (e.g., for few-shot examples) still works. Pick the replacement that matches what the prefill was doing:
   294|
   295|| Prefill was used for | Replacement |
   296|| --- | --- |
   297|| Forcing JSON / YAML / schema output | `output_config.format` with a `json_schema` — see example below |
   298|| Forcing a classification label | Tool with an enum field containing valid labels, or structured outputs |
   299|| Skipping preambles (`Here is the summary:\n`) | System prompt instruction: _"Respond directly without preamble. Do not start with phrases like 'Here is...' or 'Based on...'."_ |
   300|| Steering around bad refusals | Usually no longer needed — 4.6 refuses far more appropriately. Plain user-turn prompting is sufficient. |
   301|| Continuing an interrupted response | Move continuation into the user turn: _"Your previous response was interrupted and ended with `[last text]`. Continue from there."_ |
   302|| Injecting reminders / context hydration | Inject into the user turn instead. For complex agent harnesses, expose context via a tool call or during compaction. |
   303|
   304|```python
   305|# Old (fails on Opus 4.6 / Sonnet 4.6) — prefill forcing JSON shape
   306|messages=[
   307|    {"role": "user", "content": "Extract the name."},
   308|    {"role": "assistant", "content": "{\"name\": \""},
   309|]
   310|
   311|# New — structured outputs replace the prefill
   312|response = client.messages.create(
   313|    model="claude-opus-4-6",
   314|    max_tokens=1024,
   315|    output_config={"format": {"type": "json_schema", "schema": {...}}},
   316|    messages=[{"role": "user", "content": "Extract the name."}],
   317|)
   318|```
   319|
   320|**4. Stream for `max_tokens > ~16K` (all models); Opus 4.6 alone reaches 128K.**
   321|
   322|Non-streaming requests hit SDK HTTP timeouts at high `max_tokens`, regardless of model — stream for anything above ~16K output. The streamable ceiling differs by model: Sonnet 4.6 and Haiku 4.5 cap at 64K, and Opus 4.6 alone goes up to 128K.
   323|
   324|```python
   325|with client.messages.stream(model="claude-opus-4-6", max_tokens=64000, ...) as stream:
   326|    message = stream.get_final_message()
   327|```
   328|
   329|**5. Tool-call JSON escaping may differ (Opus 4.6 and Sonnet 4.6).**
   330|
   331|Both 4.6 models can produce tool call `input` fields with Unicode or forward-slash escaping. Always parse with `json.loads()` / `JSON.parse()` — never raw-string-match the serialized input.
   332|
   333|### All models
   334|
   335|**6. `output_format` → `output_config.format` (API-wide).**
   336|
   337|The old top-level `output_format` parameter on `messages.create()` is deprecated. Use `output_config.format` instead. This is not 4.6-specific — applies to every model.
   338|
   339|---
   340|
   341|## Beta Headers to Remove on 4.6
   342|
   343|Several beta headers that were required on 4.5 are now GA on 4.6 and should be removed. Leaving them in is harmless but misleading; removing them also lets you move from `client.beta.messages.create(...)` back to `client.messages.create(...)`.
   344|
   345|| Header | Status on 4.6 | Action |
   346|| --- | --- | --- |
   347|| `effort-2025-11-24` | Effort parameter is GA | Remove |
   348|| `fine-grained-tool-streaming-2025-05-14` | GA | Remove |
   349|| `interleaved-thinking-2025-05-14` | Adaptive thinking enables interleaved thinking automatically | Remove when using adaptive thinking; still functional on Sonnet 4.6 _with_ manual extended thinking, but that path is deprecated |
   350|| `token-efficient-tools-2025-02-19` | Built in to all Claude 4+ models | Remove (no effect) |
   351|| `output-128k-2025-02-19` | Built in to Claude 4+ models | Remove (no effect) |
   352|
   353|Once you remove all of these and finish moving to adaptive thinking, you can switch the SDK call site from the beta namespace back to the regular one:
   354|
   355|```python
   356|# Before
   357|response = client.beta.messages.create(
   358|    model="claude-opus-4-5",
   359|    betas=["interleaved-thinking-2025-05-14", "effort-2025-11-24"],
   360|    ...
   361|)
   362|
   363|# After
   364|response = client.messages.create(
   365|    model="claude-opus-4-6",
   366|    thinking={"type": "adaptive"},
   367|    output_config={"effort": "high"},
   368|    ...
   369|)
   370|```
   371|
   372|---
   373|
   374|## Additional Changes When Coming from 3.x / 4.0 / 4.1 → 4.6
   375|
   376|If you're jumping from Opus 4.1, Sonnet 4, Sonnet 3.7, or an older Claude 3.x model directly to 4.6, apply everything above _plus_ the items in this section. Users already on Opus 4.5 / Sonnet 4.5 can skip this.
   377|
   378|**1. Sampling parameters: `temperature` OR `top_p`, not both.**
   379|
   380|Passing both will error on every Claude 4+ model:
   381|
   382|```python
   383|# Old (3.x only — errors on 4+)
   384|client.messages.create(temperature=0.7, top_p=0.9, ...)
   385|
   386|# New
   387|client.messages.create(temperature=0.7, ...)  # or top_p, not both
   388|```
   389|
   390|**2. Update tool versions.**
   391|
   392|Legacy tool versions are not supported on 4+. **Both the `type` and the `name` field change** — `text_editor_20250728` and `str_replace_based_edit_tool` are a pair; updating one without the other 400s. Also remove the `undo_edit` command from your text-editor integration:
   393|
   394|| Old | New |
   395|| --- | --- |
   396|| `text_editor_20250124` + `str_replace_editor` | `text_editor_20250728` + `str_replace_based_edit_tool` |
   397|| `code_execution_*` (earlier versions) | `code_execution_20250825` |
   398|| `undo_edit` command | _(no longer supported — delete call sites)_ |
   399|
   400|```python
   401|# Before
   402|tools = [{"type": "text_editor_20250124", "name": "str_replace_editor"}]
   403|
   404|# After — BOTH fields change
   405|tools = [{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}]
   406|```
   407|
   408|**3. Handle the `refusal` stop reason.**
   409|
   410|Claude 4+ can return `stop_reason: "refusal"` on the response. If your code only handles `end_turn` / `tool_use` / `max_tokens`, add a branch:
   411|
   412|```python
   413|if response.stop_reason == "refusal":
   414|    # Surface the refusal to the user; do not retry with the same prompt
   415|    ...
   416|```
   417|
   418|**4. Handle the `model_context_window_exceeded` stop reason (4.5+).**
   419|
   420|Distinct from `max_tokens`: it means the model hit the _context window_ limit, not the requested output cap. Handle both:
   421|
   422|```python
   423|if response.stop_reason == "model_context_window_exceeded":
   424|    # Context window exhausted — compact or split the conversation
   425|    ...
   426|elif response.stop_reason == "max_tokens":
   427|    # Requested output cap hit — retry with higher max_tokens or stream
   428|    ...
   429|```
   430|
   431|**5. Trailing newlines preserved in tool call string parameters (4.5+).**
   432|
   433|4.5 and 4.6 preserve trailing newlines that older models stripped. If your tool implementations do exact string matching against tool-call `input` values (e.g., `if name == "foo"`), verify they still match when the model sends `"foo\n"`. Normalizing with `.rstrip()` on the receiving side is usually the simplest fix.
   434|
   435|**6. Haiku: rate limits reset between generations.**
   436|
   437|Haiku 4.5 has its own rate-limit pool separate from Haiku 3 / 3.5. If you're ramping traffic as you migrate, check your tier's Haiku 4.5 limits at [API rate limits](https://platform.claude.com/docs/en/api/rate-limits) — a quota that comfortably served Haiku 3.5 traffic may need a tier bump for the same volume on 4.5.
   438|
   439|---
   440|
   441|## Prompt-Behavior Changes (Opus 4.5 / 4.6, Sonnet 4.6)
   442|
   443|These don't break your code, but prompts that worked on 4.5-and-earlier may over- or under-trigger on 4.6. Tune as needed.
   444|
   445|**1. Aggressive instructions cause overtriggering.** Opus 4.5 and 4.6 follow the system prompt much more closely than earlier models. Prompts written to _overcome_ the old reluctance are now too aggressive:
   446|
   447|| Before (worked on 4.0 / 4.5) | After (use on 4.6) |
   448|| --- | --- |
   449|| `CRITICAL: You MUST use this tool when...` | `Use this tool when...` |
   450|| `Default to using [tool]` | `Use [tool] when it would improve X` |
   451|| `If in doubt, use [tool]` | _(delete — no longer needed)_ |
   452|
   453|If the model is now overtriggering a tool or skill, the fix is almost always to dial back the language, not to add more guardrails.
   454|
   455|**2. Overthinking and excessive exploration (Opus 4.6).** At higher `effort` settings, Opus 4.6 explores more before answering. If that burns too many thinking tokens, lower `effort` first (`medium` is often the sweet spot) before adding prose instructions to constrain reasoning.
   456|
   457|**3. Overeager subagent spawning (Opus 4.6).** Opus 4.6 has a strong preference for delegating to subagents. If you see it spawning a subagent for something a direct `grep` or `read` would solve, add guidance: _"Use subagents only for parallel or independent workstreams. For single-file reads or sequential operations, work directly."_
   458|
   459|**4. Overengineering (Opus 4.5 / 4.6).** Both models may add extra files, abstractions, or defensive error handling beyond what was asked. If you want minimal changes, prompt for it explicitly: _"Only make changes directly requested. Don't add helpers, abstractions, or error handling for scenarios that can't happen."_
   460|
   461|**5. LaTeX math output (Opus 4.6).** Opus 4.6 defaults to LaTeX (`\frac{}{}`, `$...$`) for math and technical content. If you need plain text, instruct it explicitly: _"Format all math as plain text — no LaTeX, no `$`, no `\frac{}{}`. Use `/` for division and `^` for exponents."_
   462|
   463|**6. Skipped verbal summaries (4.6 family).** The 4.6 models are more concise and may skip the summary paragraph after a tool call, jumping straight to the next action. If you rely on those summaries for visibility, add: _"After completing a task that involves tool use, provide a brief summary of what you did."_
   464|
   465|**7. "Think" as a trigger word (Opus 4.5 with thinking disabled).** When `thinking` is off, Opus 4.5 is particularly sensitive to the word _think_ and may reason more than you want. Use `consider`, `evaluate`, or `reason through` instead.
   466|
   467|---
   468|
   469|## Model-ID Rename Quick Reference
   470|
   471|| Old string (migration source) | New string          |
   472|| ----------------------------- | ------------------- |
   473|| `claude-opus-4-6`             | `claude-opus-4-7`   |
   474|| `claude-opus-4-5`             | `claude-opus-4-7`   |
   475|| `claude-opus-4-1`             | `claude-opus-4-7`   |
   476|| `claude-opus-4-0`             | `claude-opus-4-7`   |
   477|| `claude-sonnet-4-5`           | `claude-sonnet-4-6` |
   478|| `claude-sonnet-4-0`           | `claude-sonnet-4-6` |
   479|
   480|Older aliases (`claude-opus-4-5`, `claude-sonnet-4-5`, `claude-opus-4-1`, etc.) are still active and can be pinned if you need time before upgrading — see `shared/models.md` for the full legacy list.
   481|
   482|---
   483|
   484|## Migration Checklist
   485|
   486|Every item is tagged: **`[BLOCKS]`** items cause a 400 error, infinite loop, silent timeout, or wrong tool selection if missed — apply these as code edits, not as suggestions. **`[TUNE]`** items are quality/cost adjustments.
   487|
   488|For each file that calls `messages.create()` / equivalent SDK method:
   489|
   490|- [ ] **[BLOCKS]** Update the `model=` string to the new alias
   491|- [ ] **[BLOCKS]** Replace `budget_tokens` with `thinking={"type": "adaptive"}` (deprecated on Opus 4.6 / Sonnet 4.6)
   492|- [ ] **[BLOCKS]** Move `format` from top-level `output_format` into `output_config.format`
   493|- [ ] **[BLOCKS]** Remove any assistant-turn prefills if targeting Opus 4.6 or Sonnet 4.6 (see the prefill replacement table)
   494|- [ ] **[BLOCKS]** Switch to streaming if `max_tokens > ~16000` (otherwise SDK HTTP timeout)
   495|- [ ] **[TUNE]** Set `output_config={"effort": "..."}` explicitly — especially when moving Sonnet 4.5 → Sonnet 4.6 (4.6 defaults to `high`)
   496|- [ ] **[TUNE]** Remove GA beta headers: `effort-2025-11-24`, `fine-grained-tool-streaming-2025-05-14`, `token-efficient-tools-2025-02-19`, `output-128k-2025-02-19`; remove `interleaved-thinking-2025-05-14` once on adaptive thinking
   497|- [ ] **[TUNE]** Switch `client.beta.messages.create(...)` → `client.messages.create(...)` once all betas are removed
   498|- [ ] **[TUNE]** Review system prompt for aggressive tool language (`CRITICAL:`, `MUST`, `If in doubt`) and dial it back
   499|
   500|**Extra items when coming from 3.x / 4.0 / 4.1:**
   501|