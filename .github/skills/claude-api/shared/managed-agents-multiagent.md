---
name: shared-managed-agents-multiagent
description: "Managed Agents — Multiagent Sessions"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Multiagent Sessions
     2|
     3|A coordinator agent can delegate to other agents within one session. All agents **share the container and filesystem**; each runs in its own **thread** — a context-isolated event stream with its own conversation history, model, system prompt, tools, MCP servers, and skills (from that agent's own config). Threads are persistent: the coordinator can send a follow-up to a subagent it called earlier and that subagent retains its prior turns.
     4|
     5|The SDK sets the `managed-agents-2026-04-01` beta header automatically on all `client.beta.{agents,sessions}.*` calls; no additional header is required for multiagent.
     6|
     7|---
     8|
     9|## Declare the roster on the coordinator
    10|
    11|`multiagent` is a **top-level field** on `agents.create()` / `agents.update()` — **not** a `tools[]` entry. `agents` lists 1–20 roster entries. Nothing changes on `sessions.create()` — the roster is resolved from the coordinator's config.
    12|
    13|```python
    14|orchestrator = client.beta.agents.create(
    15|    name="Engineering Lead",
    16|    model="{{OPUS_ID}}",
    17|    system="You coordinate engineering work. Delegate code review to the reviewer and test writing to the test agent.",
    18|    tools=[{"type": "agent_toolset_20260401"}],
    19|    multiagent={
    20|        "type": "coordinator",
    21|        "agents": [
    22|            reviewer.id,                                            # bare string — latest version
    23|            {"type": "agent", "id": test_writer.id, "version": 4},  # pinned version
    24|            {"type": "self"},                                       # the coordinator itself
    25|        ],
    26|    },
    27|)
    28|
    29|session = client.beta.sessions.create(agent=orchestrator.id, environment_id=env.id)
    30|```
    31|
    32|| Roster entry | Shape | Notes |
    33|| --- | --- | --- |
    34|| String shorthand | `"agent_abc123"` | References the latest version of a stored agent. |
    35|| Agent reference | `{type: "agent", id, version?}` | Omit `version` to pin the latest at coordinator save time. |
    36|| Self | `{type: "self"}` | The coordinator can spawn copies of itself. |
    37|
    38|Up to **20 unique agents** in the roster; the coordinator may spawn **multiple copies** of each. **One level of delegation only** — depth > 1 is ignored.
    39|
    40|---
    41|
    42|## Threads
    43|
    44|The session-level event stream is the **primary thread** — it shows the coordinator's trace plus a condensed view of subagent activity (thread status transitions and cross-thread messages, not every subagent tool call). Drill into a specific subagent via the per-thread endpoints:
    45|
    46|| Operation | HTTP | SDK (`client.beta.sessions.threads.*`) |
    47|| --- | --- | --- |
    48|| List threads | `GET /v1/sessions/{sid}/threads` | `.list(session_id)` |
    49|| Retrieve one | `GET /v1/sessions/{sid}/threads/{tid}` | `.retrieve(thread_id, session_id=...)` |
    50|| Archive | `POST /v1/sessions/{sid}/threads/{tid}/archive` | `.archive(thread_id, session_id=...)` |
    51|| List thread events | `GET /v1/sessions/{sid}/threads/{tid}/events` | `.events.list(thread_id, session_id=...)` |
    52|| Stream thread events | `GET /v1/sessions/{sid}/threads/{tid}/stream` | `.events.stream(thread_id, session_id=...)` |
    53|
    54|Each `SessionThread` carries `id`, `status` (`running` | `idle` | `rescheduling` | `terminated`), `agent` (a resolved snapshot of the agent config — `id`, `name`, `model`, `system`, `tools`, `skills`, `mcp_servers`, `version`), `parent_thread_id` (null for the primary thread, which is included in the list), `archived_at`, and optional `stats`/`usage`. **Session status aggregates thread statuses** — if any thread is `running`, `session.status` is `running`. Max **25 concurrent threads**. When draining a per-thread stream, break on `session.thread_status_idle` (and check its `stop_reason` as you would for the session-level idle).
    55|
    56|---
    57|
    58|## Multiagent events (on the session stream)
    59|
    60|| Event | Payload highlights | Meaning |
    61|| --- | --- | --- |
    62|| `session.thread_created` | `session_thread_id`, `agent_name` | A new thread was created. |
    63|| `session.thread_status_running` | `session_thread_id`, `agent_name` | Thread started activity. |
    64|| `session.thread_status_idle` | `session_thread_id`, `agent_name`, **`stop_reason`** | Thread is awaiting input. Inspect `stop_reason` (same shape as `session.status_idle.stop_reason`). |
    65|| `session.thread_status_rescheduled` | `session_thread_id`, `agent_name` | Thread is rescheduling after a retryable error. |
    66|| `session.thread_status_terminated` | `session_thread_id`, `agent_name` | Thread was archived or hit a terminal error. |
    67|| `agent.thread_message_sent` | `to_session_thread_id`, `to_agent_name`, `content` | Coordinator sent a follow-up to another thread. |
    68|| `agent.thread_message_received` | `from_session_thread_id`, `from_agent_name`, `content` | An agent delivered its result to the coordinator. |
    69|
    70|---
    71|
    72|## Tool permissions and custom tools from subagent threads
    73|
    74|When a subagent needs your client (an `always_ask` confirmation, or a custom tool result), the request is **cross-posted to the primary thread** with `session_thread_id` identifying the originating thread — so you only need to watch the session stream. Reply with `user.tool_confirmation` (carrying `tool_use_id`) or `user.custom_tool_result` (carrying `custom_tool_use_id`), and **echo the `session_thread_id` from the originating event** (the SDK param type and docstring expect it). The server also routes by the tool-use ID, so the echo is belt-and-suspenders rather than load-bearing — but include it.
    75|
    76|```python
    77|for event_id in stop.event_ids:
    78|    pending = events_by_id[event_id]
    79|    confirmation = {
    80|        "type": "user.tool_confirmation",
    81|        "tool_use_id": event_id,
    82|        "result": "allow",
    83|    }
    84|    if pending.session_thread_id is not None:
    85|        confirmation["session_thread_id"] = pending.session_thread_id
    86|    client.beta.sessions.events.send(session.id, events=[confirmation])
    87|```
    88|
    89|The same pattern applies to `user.custom_tool_result`.
    90|
    91|---
    92|
    93|## Pitfalls
    94|
    95|- **Don't put the roster on `sessions.create()` or in `tools[]`.** `multiagent` is a top-level agent field; update the coordinator, then start a session that references it.
    96|- **Don't assume shared context.** Threads share the filesystem but not conversation history or tools. If the coordinator needs a subagent to act on something, it must say so in the delegated message (or write it to disk).
    97|- **Depth > 1 is ignored.** A subagent's own `multiagent` roster (if any) doesn't cascade — only the session's coordinator delegates.
    98|
    99|For per-language bindings beyond Python, WebFetch `https://platform.claude.com/docs/en/managed-agents/multi-agent.md` (see `shared/live-sources.md`).
   100|