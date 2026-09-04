---
name: shared-managed-agents-client-patterns
description: "Managed Agents — Common Client Patterns"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Common Client Patterns
     2|
     3|Patterns you'll write on the client side when driving a Managed Agent session, grounded in working SDK examples.
     4|
     5|Code samples are TypeScript — Python and cURL follow the same shape; see `python/managed-agents/README.md` and `curl/managed-agents.md` for equivalents.
     6|
     7|---
     8|
     9|## 1. Lossless stream reconnect
    10|
    11|**Problem:** SSE has no replay. If the connection drops mid-session, a naive reconnect re-opens the stream from "now" and you silently miss every event emitted in between.
    12|
    13|**Solution:** on reconnect, fetch the full event history via `events.list()` _before_ consuming the live stream, and dedupe on event ID as the live stream catches up.
    14|
    15|```ts
    16|const seenEventIds = new Set<string>();
    17|const stream = await client.beta.sessions.events.stream(session.id);
    18|
    19|// Stream is now open and buffering server-side. Read history first.
    20|for await (const event of client.beta.sessions.events.list(
    21|  session.id
    22|)) {
    23|  seenEventIds.add(event.id);
    24|  handle(event);
    25|}
    26|
    27|// Tail the live stream. Dedupe only gates handle() — terminal checks must run
    28|// even for already-seen events, or a terminal event that was in the history
    29|// response gets skipped by `continue` and the loop never exits.
    30|for await (const event of stream) {
    31|  if (!seenEventIds.has(event.id)) {
    32|    seenEventIds.add(event.id);
    33|    handle(event);
    34|  }
    35|  if (event.type === "session.status_terminated") break;
    36|  if (
    37|    event.type === "session.status_idle" &&
    38|    event.stop_reason.type !== "requires_action"
    39|  )
    40|    break;
    41|}
    42|```
    43|
    44|---
    45|
    46|## 2. `processed_at` — queued vs processed
    47|
    48|Every event on the stream carries `processed_at` (ISO 8601). For client-sent events (`user.message`, `user.interrupt`, `user.tool_confirmation`, `user.custom_tool_result`) it's `null` when the event has been queued but not yet picked up by the agent, and populated once the agent processes it. The same event appears on the stream twice — once with `processed_at: null`, once with a timestamp.
    49|
    50|```ts
    51|for await (const event of stream) {
    52|  if (event.type === "user.message") {
    53|    if (event.processed_at == null) onQueued(event.id);
    54|    else onProcessed(event.id, event.processed_at);
    55|  }
    56|}
    57|```
    58|
    59|Use this to drive pending → acknowledged UI state for anything you send. How you map a locally-rendered optimistic message to the server-assigned `event.id` is application-specific (typically via the return value of `events.send()` or FIFO ordering).
    60|
    61|---
    62|
    63|## 3. Interrupt a running session
    64|
    65|Send `user.interrupt` as a normal event. The session keeps running until it reaches a safe boundary, then goes idle.
    66|
    67|```ts
    68|await client.beta.sessions.events.send(session.id, {
    69|  events: [{ type: "user.interrupt" }]
    70|});
    71|
    72|// Drain until the session is truly done — see Pattern 5 for the full gate.
    73|for await (const event of stream) {
    74|  if (event.type === "session.status_terminated") break;
    75|  if (
    76|    event.type === "session.status_idle" &&
    77|    event.stop_reason.type !== "requires_action"
    78|  )
    79|    break;
    80|}
    81|```
    82|
    83|Reference: `interrupt.ts` — sends the interrupt the moment it sees `span.model_request_start`, drains to idle, then verifies via `sessions.retrieve()`.
    84|
    85|---
    86|
    87|## 4. `tool_confirmation` round-trip
    88|
    89|When the agent has `permission_policy: { type: 'always_ask' }`, any call to that tool fires an `agent.tool_use` event with `evaluated_permission === 'ask'` and the session goes idle waiting for a decision. Respond with `user.tool_confirmation`.
    90|
    91|```ts
    92|for await (const event of stream) {
    93|  if (
    94|    event.type === "agent.tool_use" &&
    95|    event.evaluated_permission === "ask"
    96|  ) {
    97|    await client.beta.sessions.events.send(session.id, {
    98|      events: [
    99|        {
   100|          type: "user.tool_confirmation",
   101|          tool_use_id: event.id, // not a toolu_ id — use event.id
   102|          result: "allow" // or 'deny'
   103|          // deny_message: '...',        // optional, only with result: 'deny'
   104|        }
   105|      ]
   106|    });
   107|  }
   108|}
   109|```
   110|
   111|Key points:
   112|
   113|- `tool_use_id` is `event.id` (typically `sevt_...`), **not** a `toolu_...` ID.
   114|- `result` is `'allow' | 'deny'`. Use `deny_message` to tell the model _why_ you denied — it gets surfaced back to the agent.
   115|- Multiple pending tools: respond once per `agent.tool_use` event with `evaluated_permission === 'ask'`.
   116|
   117|Reference: `tool-permissions.ts`.
   118|
   119|---
   120|
   121|## 5. Correct idle-break gate
   122|
   123|Do not break on `session.status_idle` alone. The session goes idle transiently — e.g. between parallel tool executions, while waiting for a `user.tool_confirmation`, or while awaiting a `user.custom_tool_result`. Break when idle with a terminal `stop_reason`, or on `session.status_terminated`.
   124|
   125|```ts
   126|for await (const event of stream) {
   127|  handle(event);
   128|  if (event.type === "session.status_terminated") break;
   129|  if (event.type === "session.status_idle") {
   130|    if (event.stop_reason.type === "requires_action") continue; // waiting on you — handle it
   131|    break; // end_turn or retries_exhausted — both terminal
   132|  }
   133|}
   134|```
   135|
   136|`stop_reason.type` values on `session.status_idle`:
   137|
   138|- `requires_action` — agent is waiting on a client-side event (tool confirmation, custom tool result). Handle it, don't break.
   139|- `retries_exhausted` — terminal failure. Break, then check `sessions.retrieve()` for the error state.
   140|- `end_turn` — normal completion.
   141|
   142|---
   143|
   144|## 6. Post-idle status-write race
   145|
   146|The SSE stream emits `session.status_idle` slightly before the session's queryable status reflects it. Clients that break on idle and immediately call `sessions.delete()` or `sessions.archive()` will intermittently 400 with "cannot delete/archive while running."
   147|
   148|Poll before cleanup:
   149|
   150|```ts
   151|let s;
   152|for (let i = 0; i < 10; i++) {
   153|  s = await client.beta.sessions.retrieve(session.id);
   154|  if (s.status !== "running") break;
   155|  await new Promise(r => setTimeout(r, 200));
   156|}
   157|if (s?.status !== "running") {
   158|  await client.beta.sessions.archive(session.id);
   159|} // else: still running after 2s — don't archive, let it settle or escalate
   160|```
   161|
   162|---
   163|
   164|## 7. Stream-first, then send
   165|
   166|Always open the stream **before** sending the kickoff event. Otherwise the agent may process the event and emit the first events before your consumer is attached, and you'll miss them.
   167|
   168|```ts
   169|const stream = await client.beta.sessions.events.stream(session.id);
   170|await client.beta.sessions.events.send(session.id, {
   171|  events: [
   172|    {
   173|      type: "user.message",
   174|      content: [{ type: "text", text: "Hello" }]
   175|    }
   176|  ]
   177|});
   178|for await (const event of stream) {
   179|  /* ... */
   180|}
   181|```
   182|
   183|The `Promise.all([stream, send])` shape works too, but stream-first is simpler and has the same effect — the stream starts buffering the moment it's opened.
   184|
   185|---
   186|
   187|## 8. File-mount gotchas
   188|
   189|**The mounted resource has a different `file_id` than the file you uploaded.** Session creation makes a session-scoped copy.
   190|
   191|```ts
   192|const uploaded = await client.beta.files.upload({ file });
   193|// uploaded.id         → the original file
   194|const session = await client.beta.sessions.create({
   195|  /* ... */
   196|  resources: [
   197|    {
   198|      type: "file",
   199|      file_id: uploaded.id,
   200|      mount_path: "/workspace/data.csv"
   201|    }
   202|  ]
   203|});
   204|// session.resources[0].file_id !== uploaded.id  ← different IDs
   205|```
   206|
   207|Delete the original via `files.delete(uploaded.id)`; the session-scoped copy is garbage-collected with the session. `mount_path` must be absolute — see `shared/managed-agents-environments.md`.
   208|
   209|---
   210|
   211|## 9. Secrets for non-MCP APIs and CLIs — keep them host-side via custom tools
   212|
   213|**Problem:** you want the agent to call a third-party API or run a CLI that needs a secret (API key, token, service-account credential), but there is currently no way to set environment variables inside the session container, and vaults currently hold MCP credentials only — they are not exposed to the container's shell. So `curl`, installed CLIs, or SDK clients running via the `bash` tool have no first-class place to read a secret from.
   214|
   215|**Solution:** move the authenticated call to your side. Declare a custom tool on the agent; when the agent emits `agent.custom_tool_use`, your orchestrator (the process reading the SSE stream) executes the call with its own credentials and responds with `user.custom_tool_result`. The container never sees the key.
   216|
   217|```ts
   218|// Agent template: declare the tool, no credentials
   219|tools: [
   220|  {
   221|    type: "custom",
   222|    name: "linear_graphql",
   223|    input_schema: {
   224|      /* query, vars */
   225|    }
   226|  }
   227|];
   228|
   229|// Orchestrator: handle the call with host-side creds
   230|for await (const event of stream) {
   231|  if (
   232|    event.type === "agent.custom_tool_use" &&
   233|    event.name === "linear_graphql"
   234|  ) {
   235|    const result = await linear.request(
   236|      event.input.query,
   237|      event.input.vars
   238|    ); // host's key
   239|    await client.beta.sessions.events.send(session.id, {
   240|      events: [
   241|        {
   242|          type: "user.custom_tool_result",
   243|          tool_use_id: event.id,
   244|          result
   245|        }
   246|      ]
   247|    });
   248|  }
   249|}
   250|```
   251|
   252|Same shape works for `gh` CLI, local eval scripts, or anything else that needs host-side auth or binaries.
   253|
   254|**Security note:** this does not expose a public endpoint. `agent.custom_tool_use` arrives on the SSE stream your orchestrator already holds open with your Anthropic API key, and `user.custom_tool_result` goes back via `events.send()` under the same key. Your orchestrator is a client, not a server — nothing unauthenticated is listening.
   255|
   256|**Do not embed API keys in the system prompt or user messages as a workaround.** Prompts and messages are stored in the session's event history, returned by `events.list()`, and included in compaction summaries — a secret placed there is durably persisted and readable via the API for the life of the session.
   257|