---
name: claude-api-php
description: "Claude API — PHP"
version: 1.0.0
author: Alexa
---
     1|# Claude API — PHP
     2|
     3|> **Note:** The PHP SDK is the official Anthropic SDK for PHP. A beta tool runner is available via `$client->beta->messages->toolRunner()`. Structured output helpers are supported via `StructuredOutputModel` classes. Agent SDK is not available. Bedrock, Vertex AI, and Foundry clients are supported.
     4|
     5|## Installation
     6|
     7|```bash
     8|composer require "anthropic-ai/sdk"
     9|```
    10|
    11|## Client Initialization
    12|
    13|```php
    14|use Anthropic\Client;
    15|
    16|// Using API key from environment variable
    17|$client = new Client(apiKey: getenv("ANTHROPIC_API_KEY"));
    18|```
    19|
    20|### Amazon Bedrock
    21|
    22|```php
    23|use Anthropic\Bedrock;
    24|
    25|// Constructor is private — use the static factory. Reads AWS credentials from env.
    26|$client = Bedrock\Client::fromEnvironment(region: 'us-east-1');
    27|```
    28|
    29|### Google Vertex AI
    30|
    31|```php
    32|use Anthropic\Vertex;
    33|
    34|// Constructor is private. Parameter is `location`, not `region`.
    35|$client = Vertex\Client::fromEnvironment(
    36|    location: 'us-east5',
    37|    projectId: 'my-project-id',
    38|);
    39|```
    40|
    41|### Anthropic Foundry
    42|
    43|```php
    44|use Anthropic\Foundry;
    45|
    46|// Constructor is private. baseUrl or resource is required.
    47|$client = Foundry\Client::withCredentials(
    48|    authToken: getenv('ANTHROPIC_FOUNDRY_AUTH_TOKEN'),
    49|    baseUrl: 'https://<resource>.services.ai.azure.com/anthropic',
    50|);
    51|```
    52|
    53|---
    54|
    55|## Basic Message Request
    56|
    57|```php
    58|$message = $client->messages->create(
    59|    model: 'claude-opus-4-7',
    60|    maxTokens: 16000,
    61|    messages: [
    62|        ['role' => 'user', 'content' => 'What is the capital of France?'],
    63|    ],
    64|);
    65|
    66|// content is an array of polymorphic blocks (TextBlock, ToolUseBlock,
    67|// ThinkingBlock). Accessing ->text on content[0] without checking the block
    68|// type will throw if the first block is not a TextBlock (e.g., when extended
    69|// thinking is enabled and a ThinkingBlock comes first). Always guard:
    70|foreach ($message->content as $block) {
    71|    if ($block->type === 'text') {
    72|        echo $block->text;
    73|    }
    74|}
    75|```
    76|
    77|If you only want the first text block:
    78|
    79|```php
    80|foreach ($message->content as $block) {
    81|    if ($block->type === 'text') {
    82|        echo $block->text;
    83|        break;
    84|    }
    85|}
    86|```
    87|
    88|---
    89|
    90|## Streaming
    91|
    92|> **Requires SDK v0.5.0+.** v0.4.0 and earlier used a single `$params` array; calling with named parameters throws `Unknown named parameter $model`. Upgrade: `composer require "anthropic-ai/sdk:^0.7"`
    93|
    94|```php
    95|use Anthropic\Messages\RawContentBlockDeltaEvent;
    96|use Anthropic\Messages\TextDelta;
    97|
    98|$stream = $client->messages->createStream(
    99|    model: 'claude-opus-4-7',
   100|    maxTokens: 64000,
   101|    messages: [
   102|        ['role' => 'user', 'content' => 'Write a haiku'],
   103|    ],
   104|);
   105|
   106|foreach ($stream as $event) {
   107|    if ($event instanceof RawContentBlockDeltaEvent && $event->delta instanceof TextDelta) {
   108|        echo $event->delta->text;
   109|    }
   110|}
   111|```
   112|
   113|---
   114|
   115|## Tool Use
   116|
   117|### Tool Runner (Beta)
   118|
   119|**Beta:** The PHP SDK provides a tool runner via `$client->beta->messages->toolRunner()`. Define tools with `BetaRunnableTool` — a definition array plus a `run` closure:
   120|
   121|```php
   122|use Anthropic\Lib\Tools\BetaRunnableTool;
   123|
   124|$weatherTool = new BetaRunnableTool(
   125|    definition: [
   126|        'name' => 'get_weather',
   127|        'description' => 'Get the current weather for a location.',
   128|        'input_schema' => [
   129|            'type' => 'object',
   130|            'properties' => [
   131|                'location' => ['type' => 'string', 'description' => 'City and state'],
   132|            ],
   133|            'required' => ['location'],
   134|        ],
   135|    ],
   136|    run: function (array $input): string {
   137|        return "The weather in {$input['location']} is sunny and 72°F.";
   138|    },
   139|);
   140|
   141|$runner = $client->beta->messages->toolRunner(
   142|    maxTokens: 16000,
   143|    messages: [['role' => 'user', 'content' => 'What is the weather in Paris?']],
   144|    model: 'claude-opus-4-7',
   145|    tools: [$weatherTool],
   146|);
   147|
   148|foreach ($runner as $message) {
   149|    foreach ($message->content as $block) {
   150|        if ($block->type === 'text') {
   151|            echo $block->text;
   152|        }
   153|    }
   154|}
   155|```
   156|
   157|### Manual Loop
   158|
   159|Tools are passed as arrays. **The SDK uses camelCase keys** (`inputSchema`, `toolUseID`, `stopReason`) and auto-maps to the API's snake_case on the wire — since v0.5.0. See [shared tool use concepts](../shared/tool-use-concepts.md) for the loop pattern.
   160|
   161|```php
   162|use Anthropic\Messages\ToolUseBlock;
   163|
   164|$tools = [
   165|    [
   166|        'name' => 'get_weather',
   167|        'description' => 'Get the current weather in a given location',
   168|        'inputSchema' => [  // camelCase, not input_schema
   169|            'type' => 'object',
   170|            'properties' => [
   171|                'location' => ['type' => 'string', 'description' => 'City and state'],
   172|            ],
   173|            'required' => ['location'],
   174|        ],
   175|    ],
   176|];
   177|
   178|$messages = [['role' => 'user', 'content' => 'What is the weather in SF?']];
   179|
   180|$response = $client->messages->create(
   181|    model: 'claude-opus-4-7',
   182|    maxTokens: 16000,
   183|    tools: $tools,
   184|    messages: $messages,
   185|);
   186|
   187|while ($response->stopReason === 'tool_use') {  // camelCase property
   188|    $toolResults = [];
   189|    foreach ($response->content as $block) {
   190|        if ($block instanceof ToolUseBlock) {
   191|            // $block->name  : string               — tool name to dispatch on
   192|            // $block->input : array<string,mixed>  — parsed JSON input
   193|            // $block->id    : string               — pass back as toolUseID
   194|            $result = executeYourTool($block->name, $block->input);
   195|            $toolResults[] = [
   196|                'type' => 'tool_result',
   197|                'toolUseID' => $block->id,  // camelCase, not tool_use_id
   198|                'content' => $result,
   199|            ];
   200|        }
   201|    }
   202|
   203|    // Append assistant turn + user turn with tool results
   204|    $messages[] = ['role' => 'assistant', 'content' => $response->content];
   205|    $messages[] = ['role' => 'user', 'content' => $toolResults];
   206|
   207|    $response = $client->messages->create(
   208|        model: 'claude-opus-4-7',
   209|        maxTokens: 16000,
   210|        tools: $tools,
   211|        messages: $messages,
   212|    );
   213|}
   214|
   215|// Final text response
   216|foreach ($response->content as $block) {
   217|    if ($block->type === 'text') {
   218|        echo $block->text;
   219|    }
   220|}
   221|```
   222|
   223|`$block->type === 'tool_use'` also works; `instanceof ToolUseBlock` narrows for PHPStan.
   224|
   225|---
   226|
   227|## Extended Thinking
   228|
   229|**Adaptive thinking is the recommended mode for Claude 4.6+ models.** Claude decides dynamically when and how much to think.
   230|
   231|```php
   232|use Anthropic\Messages\ThinkingBlock;
   233|
   234|$message = $client->messages->create(
   235|    model: 'claude-opus-4-7',
   236|    maxTokens: 16000,
   237|    thinking: ['type' => 'adaptive'],
   238|    messages: [
   239|        ['role' => 'user', 'content' => 'Solve: 27 * 453'],
   240|    ],
   241|);
   242|
   243|// ThinkingBlock(s) precede TextBlock in content
   244|foreach ($message->content as $block) {
   245|    if ($block instanceof ThinkingBlock) {
   246|        echo "Thinking:\n{$block->thinking}\n\n";
   247|        // $block->signature is an opaque string — preserve verbatim if
   248|        // passing thinking blocks back in multi-turn conversations
   249|    } elseif ($block->type === 'text') {
   250|        echo "Answer: {$block->text}\n";
   251|    }
   252|}
   253|```
   254|
   255|> **Deprecated:** `['type' => 'enabled', 'budgetTokens' => N]` (fixed-budget extended thinking) still works on Claude 4.6 but is deprecated. Use adaptive thinking above.
   256|
   257|`$block->type === 'thinking'` also works for the check; `instanceof` narrows for PHPStan.
   258|
   259|---
   260|
   261|## Prompt Caching
   262|
   263|`system:` takes an array of text blocks; set `cacheControl` on the last block. Array-shape syntax (camelCase keys) is idiomatic. For placement patterns and the silent-invalidator audit checklist, see `shared/prompt-caching.md`.
   264|
   265|```php
   266|$message = $client->messages->create(
   267|    model: 'claude-opus-4-7',
   268|    maxTokens: 16000,
   269|    system: [
   270|        ['type' => 'text', 'text' => $longSystemPrompt, 'cacheControl' => ['type' => 'ephemeral']],
   271|    ],
   272|    messages: [['role' => 'user', 'content' => 'Summarize the key points']],
   273|);
   274|```
   275|
   276|For 1-hour TTL: `'cacheControl' => ['type' => 'ephemeral', 'ttl' => '1h']`. There's also a top-level `cacheControl:` on `messages->create(...)` that auto-places on the last cacheable block.
   277|
   278|Verify hits via `$message->usage->cacheCreationInputTokens` / `$message->usage->cacheReadInputTokens`.
   279|
   280|---
   281|
   282|## Structured Outputs
   283|
   284|### Using StructuredOutputModel (Recommended)
   285|
   286|Define a PHP class implementing `StructuredOutputModel` and pass it as `outputConfig`:
   287|
   288|```php
   289|use Anthropic\Lib\Contracts\StructuredOutputModel;
   290|use Anthropic\Lib\Concerns\StructuredOutputModelTrait;
   291|use Anthropic\Lib\Attributes\Constrained;
   292|
   293|class Person implements StructuredOutputModel
   294|{
   295|    use StructuredOutputModelTrait;
   296|
   297|    #[Constrained(description: 'Full name')]
   298|    public string $name;
   299|
   300|    public int $age;
   301|
   302|    public ?string $email = null;  // nullable = optional field
   303|}
   304|
   305|$message = $client->messages->create(
   306|    model: 'claude-opus-4-7',
   307|    maxTokens: 16000,
   308|    messages: [['role' => 'user', 'content' => 'Generate a profile for Alice, age 30']],
   309|    outputConfig: ['format' => Person::class],
   310|);
   311|
   312|$person = $message->parsedOutput();  // Person instance
   313|echo $person->name;
   314|```
   315|
   316|Types are inferred from PHP type hints. Use `#[Constrained(description: '...')]` to add descriptions. Nullable properties (`?string`) become optional fields.
   317|
   318|### Raw Schema
   319|
   320|```php
   321|$message = $client->messages->create(
   322|    model: 'claude-opus-4-7',
   323|    maxTokens: 16000,
   324|    messages: [['role' => 'user', 'content' => 'Extract: John (john@co.com), Enterprise plan']],
   325|    outputConfig: [
   326|        'format' => [
   327|            'type' => 'json_schema',
   328|            'schema' => [
   329|                'type' => 'object',
   330|                'properties' => [
   331|                    'name' => ['type' => 'string'],
   332|                    'email' => ['type' => 'string'],
   333|                    'plan' => ['type' => 'string'],
   334|                ],
   335|                'required' => ['name', 'email', 'plan'],
   336|                'additionalProperties' => false,
   337|            ],
   338|        ],
   339|    ],
   340|);
   341|
   342|// First text block contains valid JSON
   343|foreach ($message->content as $block) {
   344|    if ($block->type === 'text') {
   345|        $data = json_decode($block->text, true);
   346|        break;
   347|    }
   348|}
   349|```
   350|
   351|---
   352|
   353|## Beta Features & Server-Side Tools
   354|
   355|**`betas:` is NOT a param on `$client->messages->create()`** — it only exists on the beta namespace. Use it for features that need an explicit opt-in header:
   356|
   357|```php
   358|use Anthropic\Beta\Messages\BetaRequestMCPServerURLDefinition;
   359|
   360|$response = $client->beta->messages->create(
   361|    model: 'claude-opus-4-7',
   362|    maxTokens: 16000,
   363|    mcpServers: [
   364|        BetaRequestMCPServerURLDefinition::with(
   365|            name: 'my-server',
   366|            url: 'https://example.com/mcp',
   367|        ),
   368|    ],
   369|    betas: ['mcp-client-2025-11-20'],  // only valid on ->beta->messages
   370|    messages: [['role' => 'user', 'content' => 'Use the MCP tools']],
   371|);
   372|```
   373|
   374|**Server-side tools** (bash, web_search, text_editor, code_execution) are GA and work on both paths — `Anthropic\Messages\ToolBash20250124` / `WebSearchTool20260209` / `ToolTextEditor20250728` / `CodeExecutionTool20260120` for non-beta, `Anthropic\Beta\Messages\BetaToolBash20250124` / `BetaWebSearchTool20260209` / `BetaToolTextEditor20250728` / `BetaCodeExecutionTool20260120` for beta. No `betas:` header needed for these.
   375|