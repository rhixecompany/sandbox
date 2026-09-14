---
name: shared-agent-design
description: "Agent Design Patterns"
version: 1.0.0
author: Alexa
---
     1|# Agent Design Patterns
     2|
     3|This file covers decision heuristics for building agents on the Claude API: which primitives to reach for, how to design your tool surface, and how to manage context and cost over long runs. For per-tool mechanics and code examples, see `tool-use-concepts.md` and the language-specific folders.
     4|
     5|---
     6|
     7|## Model Parameters
     8|
     9|| Parameter | When to use it | What to expect |
    10|| --- | --- | --- |
    11|| **Adaptive thinking** (`thinking: {type: "adaptive"}`) | When you want Claude to control when and how much to think. | Claude determines thinking depth per request and automatically interleaves thinking between tool calls. No token budget to tune. |
    12|| **Effort** (`output_config: {effort: ...}`) | When adjusting the tradeoff between thoroughness and token efficiency. | Lower effort → fewer and more-consolidated tool calls, less preamble, terser confirmations. `medium` is often a favorable balance. Use `max` when correctness matters more than cost. |
    13|
    14|See `SKILL.md` §Thinking & Effort for model support and parameter details.
    15|
    16|---
    17|
    18|## Designing Your Tool Surface
    19|
    20|### Bash vs. dedicated tools
    21|
    22|Claude doesn't know your application's security boundary, approval policy, or UX surface. Claude emits tool calls; your harness handles them. The shape of those tool calls determines what the harness can do.
    23|
    24|A **bash tool** gives Claude broad programmatic leverage — it can perform almost any action. But it gives the harness only an opaque command string, the same shape for every action. Promoting an action to a **dedicated tool** gives the harness an action-specific hook with typed arguments it can intercept, gate, render, or audit.
    25|
    26|**When to promote an action to a dedicated tool:**
    27|
    28|- **Security boundary.** Actions that require gating are natural candidates. Reversibility is a useful criterion: hard-to-reverse actions (external API calls, sending messages, deleting data) can be gated behind user confirmation. A `send_email` tool is easy to gate; `bash -c "curl -X POST ..."` is not.
    29|- **Staleness checks.** A dedicated `edit` tool can reject writes if the file changed since Claude last read it. Bash can't enforce that invariant.
    30|- **Rendering.** Some actions benefit from custom UI. Claude Code promotes question-asking to a tool so it can render as a modal, present options, and block the agent loop until answered.
    31|- **Scheduling.** Read-only tools like `glob` and `grep` can be marked parallel-safe. When the same actions run through bash, the harness can't tell a parallel-safe `grep` from a parallel-unsafe `git push`, so it must serialize.
    32|
    33|**Rule of thumb:** Start with bash for breadth. Promote to dedicated tools when you need to gate, render, audit, or parallelize the action.
    34|
    35|---
    36|
    37|## Anthropic-Provided Tools
    38|
    39|| Tool | Side | When to use it | What to expect |
    40|| --- | --- | --- | --- |
    41|| **Bash** | Client | Claude needs to execute shell commands. | Claude emits commands; your harness executes them. Reference implementation provided. |
    42|| **Text editor** | Client | Claude needs to read or edit files. | Claude views, creates, and edits files via your implementation. Reference implementation provided. |
    43|| **Computer use** | Client or Server | Claude needs to interact with GUIs, web apps, or visual interfaces. | Claude takes screenshots and issues mouse/keyboard commands. Can be self-hosted (you run the environment) or Anthropic-hosted. |
    44|| **Code execution** | Server | Claude needs to run code in a sandbox you don't want to manage. | Anthropic-hosted container with built-in file and bash sub-tools. No client-side execution. |
    45|| **Web search / fetch** | Server | Claude needs information past its training cutoff (news, current events, recent docs) or the content of a specific URL. | Claude issues a query or URL; Anthropic executes it and returns results with citations. |
    46|| **Memory** | Client | Claude needs to save context across sessions. | Claude reads/writes a `/memories` directory. You implement the storage backend. |
    47|
    48|**Client-side** tools are defined by Anthropic (name, schema, Claude's usage pattern) but executed by your harness. Anthropic provides reference implementations. **Server-side** tools run entirely on Anthropic infrastructure — declare them in `tools` and Claude handles the rest.
    49|
    50|---
    51|
    52|## Composing Tool Calls: Programmatic Tool Calling
    53|
    54|With standard tool use, each tool call is a round trip: Claude calls the tool, the result lands in Claude's context, Claude reasons about it, then calls the next tool. Three sequential actions (read profile → look up orders → check inventory) means three round trips. Each adds latency and tokens, and most of the intermediate data is never needed again.
    55|
    56|**Programmatic tool calling (PTC)** lets Claude compose those calls into a script instead. The script runs in the code execution container. When the script calls a tool, the container pauses, the call is executed (client-side or server-side), and the result returns to the running code — not to Claude's context. The script processes it with normal control flow (loops, filters, branches). Only the script's final output returns to Claude.
    57|
    58|| When to use it | What to expect |
    59|| --- | --- |
    60|| Many sequential tool calls, or large intermediate results you want filtered before they hit the context window. | Claude writes code that invokes tools as functions. Runs in the code execution container. Token cost scales with final output, not intermediate results. |
    61|
    62|---
    63|
    64|## Scaling the Tool and Instruction Set
    65|
    66|| Feature | When to use it | What to expect |
    67|| --- | --- | --- |
    68|| **Tool search** | Many tools available, but only a few relevant per request. Don't want all schemas in context upfront. | Claude searches the tool set and loads only relevant schemas. Tool definitions are appended, not swapped — preserves cache (see Caching below). |
    69|| **Skills** | Task-specific instructions Claude should load only when relevant. | Each skill is a folder with a `SKILL.md`. The skill's description sits in context by default; Claude reads the full file when the task calls for it. |
    70|
    71|Both patterns keep the fixed context small and load detail on demand.
    72|
    73|---
    74|
    75|## Long-Running Agents: Managing Context
    76|
    77|| Pattern | When to use it | What to expect |
    78|| --- | --- | --- |
    79|| **Context editing** | Context grows stale over many turns (old tool results, completed thinking). | Tool results and thinking blocks are cleared based on configurable thresholds. Keeps the transcript lean without summarizing. |
    80|| **Compaction** | Conversation likely to reach or exceed the context window limit. | Earlier context is summarized into a compaction block server-side. See `SKILL.md` §Compaction for the critical `response.content` handling. |
    81|| **Memory** | State must persist across sessions (not just within one conversation). | Claude reads/writes files in a memory directory. Survives process restarts. |
    82|
    83|**Choosing between them:** Context editing and compaction operate within a session — editing prunes stale turns, compaction summarizes when you're near the limit. Memory is for cross-session persistence. Many long-running agents use all three.
    84|
    85|---
    86|
    87|## Caching for Agents
    88|
    89|**Read `prompt-caching.md` first.** It covers the prefix-match invariant, breakpoint placement, the silent-invalidator audit, and why changing tools or models mid-session breaks the cache. This section covers only the agent-specific workarounds for those constraints.
    90|
    91|| Constraint (from `prompt-caching.md`) | Agent-specific workaround |
    92|| --- | --- |
    93|| Editing the system prompt mid-session invalidates the cache. | Append a `<system-reminder>` block in the `messages` array instead. The cached prefix stays intact. Claude Code uses this for time updates and mode transitions. |
    94|| Switching models mid-session invalidates the cache. | Spawn a **subagent** with the cheaper model for the sub-task; keep the main loop on one model. Claude Code's Explore subagents use Haiku this way. |
    95|| Adding/removing tools mid-session invalidates the cache. | Use **tool search** for dynamic discovery — it appends tool schemas rather than swapping them, so the existing prefix is preserved. |
    96|
    97|For multi-turn breakpoint placement, use top-level auto-caching — see `prompt-caching.md` §Placement patterns.
    98|
    99|---
   100|
   101|For live documentation on any of these features, see `live-sources.md`.
   102|