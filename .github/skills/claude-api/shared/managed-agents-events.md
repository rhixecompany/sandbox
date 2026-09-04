---
name: shared-managed-agents-events
description: "Managed Agents — Events & Steering"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Events & Steering
     2|
     3|## Events
     4|
     5|### Sending Events
     6|
     7|Send events to a session via `POST /v1/sessions/{id}/events`.
     8|
     9|| Event Type | When to Send |
    10|| --- | --- |
    11|| `user.message` | Send a user message |
    12|| `user.interrupt` | Interrupt the agent while it's running |
    13|| `user.tool_confirmation` | Approve/deny a tool call (when `always_ask` policy) |
    14|| `user.custom_tool_result` | Provide result for a custom tool call |
    15|| `user.define_outcome` | Start a rubric-graded iterate loop — see `shared/managed-agents-outcomes.md` |
    16|
    17|### Receiving Events
    18|
    19|Three methods:
    20|
    21|1. **Streaming (SSE)**: `GET /v1/sessions/{id}/events/stream` — real-time Server-Sent Events. **Long-lived** — the server sends periodic heartbeats to keep the connection alive.
    22|2. **Polling**: `GET /v1/sessions/{id}/events` — paginated event list (query params: `limit` default 1000, `page`). **Returns immediately** — this is a plain paginated GET, not a long-poll.
    23|3. **Webhooks**: Anthropic POSTs session state transitions to your HTTPS endpoint — thin payloads (IDs only), HMAC-signed, Console-registered. See `shared/managed-agents-webhooks.md`.
    24|
    25|All received events carry `id`, `type`, and `processed_at` (ISO 8601; `null` if not yet processed by the agent).
    26|
    27|> ⚠️ **Robust polling (raw HTTP).** If you bypass the SDK and roll your own poll loop, don't rely on `requests` or `httpx` timeouts as wall-clock caps — they're **per-chunk** read timeouts, reset every time a byte arrives. A trickling response (heartbeats, a wedged chunked-encoding body, a misbehaving proxy) can keep the call blocked indefinitely even with `timeout=(5, 60)` or `httpx.Timeout(120)`. Neither library has a "total wall-clock" timeout built in. For a hard deadline: track `time.monotonic()` at the loop level and break/cancel if a single request exceeds your budget (e.g. via a watchdog thread, or `asyncio.wait_for()` around async httpx). **Prefer the SDK** — `client.beta.sessions.events.stream()` and `client.beta.sessions.events.list()` handle timeout + retry sanely.
    28|>
    29|> If `GET /v1/sessions/{id}/events` (paginated) ever hangs after headers, you've likely hit `GET /v1/sessions/{id}/events` by mistake or a server-side stall — report it; don't treat it as a client-config problem.
    30|
    31|### Event Types (Received)
    32|
    33|Event types use dot notation, grouped by namespace:
    34|
    35|| Event Type | Description |
    36|| --- | --- |
    37|| `agent.message` | Agent text output |
    38|| `agent.thinking` | Extended thinking blocks |
    39|| `agent.tool_use` | Agent used a built-in tool (`agent_toolset_20260401`) |
    40|| `agent.tool_result` | Result from a built-in tool |
    41|| `agent.mcp_tool_use` | Agent used an MCP tool |
    42|| `agent.mcp_tool_result` | Result from an MCP tool |
    43|| `agent.custom_tool_use` | Agent invoked a custom tool — session goes idle, you respond with `user.custom_tool_result` |
    44|| `agent.thread_context_compacted` | Conversation context was compacted |
    45|| `session.status_idle` | Agent has finished the current task, and is awaiting input. It's either waiting for input to continue working via a `user.message` or blocked awaiting a `user.custom_tool_result` or `user.tool_confirmation`. The `stop_reason` attached contains more information about why the Agent has stopped working. |
    46|| `session.status_running` | Session has starting running, and the Agent is actively doing work. |
    47|| `session.status_rescheduled` | Session is (re)scheduling after a retryable error has occurred, ready to be picked up by the orchestration system. |
    48|| `session.status_terminated` | Session has terminated, entering an irreversible and unusable state. |
    49|| `session.error` | Error occurred during processing |
    50|| `span.model_request_start` | Model inference started |
    51|| `span.model_request_end` | Model inference completed |
    52|| `span.outcome_evaluation_start` / `_ongoing` / `_end` | Grader progress for outcome-oriented sessions — see `shared/managed-agents-outcomes.md` |
    53|| `session.thread_created` | Subagent thread spawned (multiagent) — see `shared/managed-agents-multiagent.md` |
    54|| `session.thread_status_running` / `_idle` / `_rescheduled` / `_terminated` | Subagent thread status transitions (multiagent). `_idle` carries `stop_reason`. |
    55|| `agent.thread_message_sent` / `_received` | Cross-thread message, carries `to_session_thread_id` / `from_session_thread_id` (multiagent) |
    56|
    57|The stream also echoes back user-sent events (`user.message`, `user.interrupt`, `user.tool_confirmation`, `user.custom_tool_result`, `user.define_outcome`).
    58|
    59|---
    60|
    61|## Steering Patterns
    62|
    63|Practical patterns for driving a session via the events surface.
    64|
    65|### Stream-first ordering
    66|
    67|**Open the stream before sending events.** The stream only delivers events that occur _after_ it's opened — it does not replay current state or historical events. If you send a message first and open the stream second, early events (including fast status transitions) arrive buffered in a single batch and you lose the ability to react to them in real time.
    68|
    69|```ts
    70|// ✅ Correct — stream and send concurrently
    71|const [response] = await Promise.all([
    72|  streamEvents(sessionId), // opens SSE connection
    73|  sendMessage(sessionId, text)
    74|]);
    75|
    76|// ❌ Wrong — events before stream opens arrive as a single buffered batch
    77|await sendMessage(sessionId, text);
    78|const response = await streamEvents(sessionId);
    79|```
    80|
    81|**For full history,** use `GET /v1/sessions/{id}/events` (paginated list) — the stream only gives you live events from connection onward.
    82|
    83|### Reconnecting after a dropped stream
    84|
    85|**The SSE stream has no replay.** If your connection drops (httpx read timeout, network blip) and you reconnect, you only get events emitted _after_ reconnection. Any events emitted during the gap are lost from the stream.
    86|
    87|**The consolidation pattern:** on every (re)connect, overlap the stream with a history fetch and dedupe by event ID:
    88|
    89|```python
    90|def connect_with_consolidation(client, session_id):
    91|    # 1. Open the SSE stream first
    92|    stream = client.beta.sessions.events.stream(session_id=session_id)
    93|
    94|    # 2. Fetch history to cover any gap
    95|    history = client.beta.sessions.events.list(
    96|        session_id=session_id,
    97|    )
    98|
    99|    # 3. Yield history first, then stream — dedupe by event.id
   100|    seen = set()
   101|    for ev in history.data:
   102|        seen.add(ev.id)
   103|        yield ev
   104|    for ev in stream:
   105|        if ev.id not in seen:
   106|            seen.add(ev.id)
   107|            yield ev
   108|```
   109|
   110|### Message queuing
   111|
   112|**You don't have to wait for a response before sending the next message.** User events are queued server-side and processed in order. This is useful for chat bridges where the user sends rapid follow-ups:
   113|
   114|```ts
   115|// All three go into one session; agent processes them in order
   116|await sendMessage(sessionId, "Summarize the README");
   117|await sendMessage(
   118|  sessionId,
   119|  "Actually also check the CONTRIBUTING guide"
   120|);
   121|await sendMessage(sessionId, "And compare the two");
   122|// Stream once — agent responds to all three as a coherent turn
   123|```
   124|
   125|Events can be sent up to the Session at any time. There is no need to wait on a specific session status to enqueue new events via `client.beta.sessions.events.send()`
   126|
   127|### Interrupt
   128|
   129|An `interrupt` event **jumps the queue** (ahead of any pending user messages) and forces the session into `idle`. Use this for "stop" / "nevermind" / "cancel" commands:
   130|
   131|```ts
   132|await client.beta.sessions.events.send(sessionId, {
   133|  events: [{ type: "interrupt" }]
   134|});
   135|```
   136|
   137|The agent stops mid-task. It does not see the interrupt as a message — it just halts. Send a follow-up `user` event to explain what to do instead. If an outcome is active, the interrupt also marks `span.outcome_evaluation_end.result: "interrupted"` (see `shared/managed-agents-outcomes.md`).
   138|
   139|> **Note**: Interrupt events may have empty IDs in the current implementation. When troubleshooting, use the `processed_at` timestamp along with surrounding event IDs.
   140|
   141|### Event payloads
   142|
   143|some events carry useful metadata beyond the status change itself:
   144|
   145|`session.status_idle` — includes a `stop_reason` field which elaborates on why the session stopped and what type of further action is required by the user.
   146|
   147|```json
   148|{
   149|  "id": "sevt_456",
   150|  "processed_at": "2026-04-07T04:27:43.197Z",
   151|  "stop_reason": {
   152|    "event_ids": ["sevt_123"],
   153|    "type": "requires_action"
   154|  },
   155|  "type": "status_idle"
   156|}
   157|```
   158|
   159|`span.model_request_end` contains a `model_usage` field for cost tracking and efficiency analysis:
   160|
   161|```json
   162|{
   163|  "id": "sevt_456",
   164|  "is_error": false,
   165|  "model_request_start_id": "sevt_123",
   166|  "model_usage": {
   167|    "cache_creation_input_tokens": 0,
   168|    "cache_read_input_tokens": 6656,
   169|    "input_tokens": 3571,
   170|    "output_tokens": 727
   171|  },
   172|  "processed_at": "2026-04-07T04:11:32.189Z",
   173|  "type": "span.model_request_end"
   174|}
   175|```
   176|
   177|**`agent.thread_context_compacted`** — emitted when the conversation history was summarized to fit context. Includes `pre_compaction_tokens` so you know how much was squeezed:
   178|
   179|```json
   180|{
   181|  "id": "sevt_abc123",
   182|  "processed_at": "2026-03-24T14:05:15.787Z",
   183|  "type": "agent.thread_context_compacted"
   184|}
   185|```
   186|
   187|### Archive
   188|
   189|When done with a session, archive it to free resources:
   190|
   191|```ts
   192|await client.beta.sessions.archive(sessionId);
   193|```
   194|
   195|> Archiving a **session** is routine cleanup — sessions are per-run and disposable. **Do not generalize this to agents or environments**: those are persistent, reusable resources, and archiving them is permanent (no unarchive; new sessions cannot reference them). See `shared/managed-agents-overview.md` → Common Pitfalls.
   196|