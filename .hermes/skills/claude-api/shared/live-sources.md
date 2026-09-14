---
name: shared-live-sources
description: "Live Documentation Sources"
version: 1.0.0
author: Alexa
---
     1|# Live Documentation Sources
     2|
     3|This file contains WebFetch URLs for fetching current information from platform.claude.com and Agent SDK repositories. Use these when users need the latest data that may have changed since the cached content was last updated.
     4|
     5|## When to Use WebFetch
     6|
     7|- User explicitly asks for "latest" or "current" information
     8|- Cached data seems incorrect
     9|- User asks about features not covered in cached content
    10|- User needs specific API details or examples
    11|
    12|## Claude API Documentation URLs
    13|
    14|### Models & Pricing
    15|
    16|| Topic | URL | Extraction Prompt |
    17|| --- | --- | --- |
    18|| Models Overview | `https://platform.claude.com/docs/en/about-claude/models/overview.md` | "Extract current model IDs, context windows, and pricing for all Claude models" |
    19|| Migration Guide | `https://platform.claude.com/docs/en/about-claude/models/migration-guide.md` | "Extract breaking changes, deprecated parameters, and per-model migration steps when moving to a newer Claude model" |
    20|| Pricing | `https://platform.claude.com/docs/en/pricing.md` | "Extract current pricing per million tokens for input and output" |
    21|
    22|### Core Features
    23|
    24|| Topic | URL | Extraction Prompt |
    25|| --- | --- | --- |
    26|| Extended Thinking | `https://platform.claude.com/docs/en/build-with-claude/extended-thinking.md` | "Extract extended thinking parameters, budget_tokens requirements, and usage examples" |
    27|| Adaptive Thinking | `https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking.md` | "Extract adaptive thinking setup, effort levels, and Claude Opus 4.7 usage examples" |
    28|| Effort Parameter | `https://platform.claude.com/docs/en/build-with-claude/effort.md` | "Extract effort levels, cost-quality tradeoffs, and interaction with thinking" |
    29|| Tool Use | `https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview.md` | "Extract tool definition schema, tool_choice options, and handling tool results" |
    30|| Streaming | `https://platform.claude.com/docs/en/build-with-claude/streaming.md` | "Extract streaming event types, SDK examples, and best practices" |
    31|| Prompt Caching | `https://platform.claude.com/docs/en/build-with-claude/prompt-caching.md` | "Extract cache_control usage, pricing benefits, and implementation examples" |
    32|
    33|### Media & Files
    34|
    35|| Topic | URL | Extraction Prompt |
    36|| --- | --- | --- |
    37|| Vision | `https://platform.claude.com/docs/en/build-with-claude/vision.md` | "Extract supported image formats, size limits, and code examples" |
    38|| PDF Support | `https://platform.claude.com/docs/en/build-with-claude/pdf-support.md` | "Extract PDF handling capabilities, limits, and examples" |
    39|
    40|### API Operations
    41|
    42|| Topic | URL | Extraction Prompt |
    43|| --- | --- | --- |
    44|| Batch Processing | `https://platform.claude.com/docs/en/build-with-claude/batch-processing.md` | "Extract batch API endpoints, request format, and polling for results" |
    45|| Files API | `https://platform.claude.com/docs/en/build-with-claude/files.md` | "Extract file upload, download, and referencing in messages, including supported types and beta header" |
    46|| Token Counting | `https://platform.claude.com/docs/en/build-with-claude/token-counting.md` | "Extract token counting API usage and examples" |
    47|| Rate Limits | `https://platform.claude.com/docs/en/api/rate-limits.md` | "Extract current rate limits by tier and model" |
    48|| Errors | `https://platform.claude.com/docs/en/api/errors.md` | "Extract HTTP error codes, meanings, and retry guidance" |
    49|
    50|### Tools
    51|
    52|| Topic | URL | Extraction Prompt |
    53|| --- | --- | --- |
    54|| Code Execution | `https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool.md` | "Extract code execution tool setup, file upload, container reuse, and response handling" |
    55|| Computer Use | `https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use.md` | "Extract computer use tool setup, capabilities, and implementation examples" |
    56|| Bash Tool | `https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool.md` | "Extract bash tool schema, reference implementation, and security considerations" |
    57|| Text Editor | `https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool.md` | "Extract text editor tool commands, schema, and reference implementation" |
    58|| Memory Tool | `https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool.md` | "Extract memory tool commands, directory structure, and implementation patterns" |
    59|| Tool Search | `https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool.md` | "Extract tool search setup, when to use, and cache interaction" |
    60|| Programmatic Tool Calling | `https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling.md` | "Extract PTC setup, script execution model, and tool invocation from code" |
    61|| Skills | `https://platform.claude.com/docs/en/agents-and-tools/skills.md` | "Extract skill folder structure, SKILL.md format, and loading behavior" |
    62|
    63|### Advanced Features
    64|
    65|| Topic | URL | Extraction Prompt |
    66|| --- | --- | --- |
    67|| Structured Outputs | `https://platform.claude.com/docs/en/build-with-claude/structured-outputs.md` | "Extract output_config.format usage and schema enforcement" |
    68|| Compaction | `https://platform.claude.com/docs/en/build-with-claude/compaction.md` | "Extract compaction setup, trigger config, and streaming with compaction" |
    69|| Context Editing | `https://platform.claude.com/docs/en/build-with-claude/context-editing.md` | "Extract context editing thresholds, what gets cleared, and configuration" |
    70|| Citations | `https://platform.claude.com/docs/en/build-with-claude/citations.md` | "Extract citation format and implementation" |
    71|| Context Windows | `https://platform.claude.com/docs/en/build-with-claude/context-windows.md` | "Extract context window sizes and token management" |
    72|
    73|### Managed Agents
    74|
    75|Use these when a managed-agents binding, behavior, or wire-level detail isn't covered in the cached `shared/managed-agents-*.md` concept files or in `{lang}/managed-agents/README.md`.
    76|
    77|| Topic | URL | Extraction Prompt |
    78|| --- | --- | --- |
    79|| Overview | `https://platform.claude.com/docs/en/managed-agents/overview.md` | "Extract the high-level architecture and how agents/sessions/environments/vaults fit together" |
    80|| Quickstart | `https://platform.claude.com/docs/en/managed-agents/quickstart.md` | "Extract the minimal end-to-end agent → environment → session → stream code path" |
    81|| Agent Setup | `https://platform.claude.com/docs/en/managed-agents/agent-setup.md` | "Extract agent create/update/list-versions/archive lifecycle and parameters" |
    82|| Define Outcomes | `https://platform.claude.com/docs/en/managed-agents/define-outcomes.md` | "Extract outcome definitions, evaluation hooks, and success criteria configuration" |
    83|| Sessions | `https://platform.claude.com/docs/en/managed-agents/sessions.md` | "Extract session lifecycle, status transitions, idle/terminated semantics, and resume rules" |
    84|| Environments | `https://platform.claude.com/docs/en/managed-agents/environments.md` | "Extract environment config (cloud/networking), management endpoints, and reuse model" |
    85|| Events and Streaming | `https://platform.claude.com/docs/en/managed-agents/events-and-streaming.md` | "Extract event stream types, stream-first ordering, reconnect/dedupe, and steering patterns" |
    86|| Tools | `https://platform.claude.com/docs/en/managed-agents/tools.md` | "Extract built-in toolset, custom tool definitions, and tool result wire format" |
    87|| Files | `https://platform.claude.com/docs/en/managed-agents/files.md` | "Extract file upload, mount paths, session resources, and listing/downloading session outputs" |
    88|| Permission Policies | `https://platform.claude.com/docs/en/managed-agents/permission-policies.md` | "Extract permission policy types (allow/deny/confirm) and per-tool config" |
    89|| Multi-Agent | `https://platform.claude.com/docs/en/managed-agents/multi-agent.md` | "Extract multi-agent composition patterns, sub-agent invocation, and result handoff" |
    90|| Observability | `https://platform.claude.com/docs/en/managed-agents/observability.md` | "Extract logging, tracing, and usage telemetry exposed by managed agents" |
    91|| Webhooks | `https://platform.claude.com/docs/en/managed-agents/webhooks.md` | "Extract webhook endpoint registration, HMAC signature verification, supported event types, and delivery semantics" |
    92|| GitHub | `https://platform.claude.com/docs/en/managed-agents/github.md` | "Extract github_repository resource shape, multi-repo mounting, and token rotation" |
    93|| MCP Connector | `https://platform.claude.com/docs/en/managed-agents/mcp-connector.md` | "Extract MCP server declaration on agents and vault-based credential injection at session" |
    94|| Vaults | `https://platform.claude.com/docs/en/managed-agents/vaults.md` | "Extract vault create, credential add/rotate, OAuth refresh shape, and archive" |
    95|| Skills | `https://platform.claude.com/docs/en/managed-agents/skills.md` | "Extract skill packaging and loading model for managed agents" |
    96|| Memory | `https://platform.claude.com/docs/en/managed-agents/memory.md` | "Extract memory resource shape, scoping, and lifecycle" |
    97|| Onboarding | `https://platform.claude.com/docs/en/managed-agents/onboarding.md` | "Extract first-run setup, prerequisites, and account/region requirements" |
    98|| Cloud Containers | `https://platform.claude.com/docs/en/managed-agents/cloud-containers.md` | "Extract cloud container runtime, image config, and network/storage knobs" |
    99|| Migration | `https://platform.claude.com/docs/en/managed-agents/migration.md` | "Extract migration paths from earlier APIs/preview shapes to GA managed agents" |
   100|
   101|### Anthropic CLI
   102|
   103|The `ant` CLI provides terminal access to the Claude API. Every API resource is exposed as a subcommand. It is one convenient way to create agents, environments, sessions, and other resources from version-controlled YAML, and to inspect responses interactively.
   104|
   105|| Topic | URL | Extraction Prompt |
   106|| --- | --- | --- |
   107|| Anthropic CLI | `https://platform.claude.com/docs/en/api/sdks/cli.md` | "Extract CLI install, authentication, command structure, and the beta:agents/environments/sessions commands" |
   108|
   109|---
   110|
   111|## Claude API SDK Repositories
   112|
   113|WebFetch these when a binding (class, method, namespace, field) isn't covered in the cached `{lang}/` skill files or in the managed-agents docs above. The SDKs include beta managed-agents support for `/v1/agents`, `/v1/sessions`, `/v1/environments`, and related resources — search the repo for `BetaManagedAgents`, `beta.agents`, `beta.sessions`, or the equivalent namespace for that language.
   114|
   115|| SDK | URL | Extraction Prompt |
   116|| --- | --- | --- |
   117|| Python | `https://github.com/anthropics/anthropic-sdk-python` | "Extract beta managed-agents namespaces, classes, and method signatures (`client.beta.agents`, `client.beta.sessions`)" |
   118|| TypeScript | `https://github.com/anthropics/anthropic-sdk-typescript` | "Extract beta managed-agents namespaces, classes, and method signatures (`client.beta.agents`, `client.beta.sessions`)" |
   119|| Java | `https://github.com/anthropics/anthropic-sdk-java` | "Extract beta managed-agents classes, builders, and method signatures (`client.beta().agents()`, `BetaManagedAgents*`)" |
   120|| Go | `https://github.com/anthropics/anthropic-sdk-go` | "Extract beta managed-agents types and method signatures (`client.Beta.Agents`, `BetaManagedAgents*` event types)" |
   121|| Ruby | `https://github.com/anthropics/anthropic-sdk-ruby` | "Extract beta managed-agents methods and parameter shapes (`client.beta.agents`, `client.beta.sessions`)" |
   122|| C# | `https://github.com/anthropics/anthropic-sdk-csharp` | "Extract beta managed-agents classes and method signatures (NuGet package, `BetaManagedAgents*` types)" |
   123|| PHP | `https://github.com/anthropics/anthropic-sdk-php` | "Extract beta managed-agents classes and method signatures (`$client->beta->agents`, `BetaManagedAgents*` params)" |
   124|
   125|---
   126|
   127|## Fallback Strategy
   128|
   129|If WebFetch fails (network issues, URL changed):
   130|
   131|1. Use cached content from the language-specific files (note the cache date)
   132|2. Inform user the data may be outdated
   133|3. Suggest they check platform.claude.com or the GitHub repos directly
   134|