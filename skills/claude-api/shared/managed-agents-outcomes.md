---
name: shared-managed-agents-outcomes
description: "Managed Agents — Outcomes"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Outcomes
     2|
     3|An **outcome** elevates a session from _conversation_ to _work_: you state what "done" looks like, and the harness runs an iterate → grade → revise loop until the artifact meets the rubric, hits `max_iterations`, or is interrupted. A separate **grader** (independent context window) scores each iteration against your rubric and feeds per-criterion gaps back to the agent.
     4|
     5|The SDK sets the `managed-agents-2026-04-01` beta header automatically on all `client.beta.sessions.*` calls; no additional header is required for outcomes.
     6|
     7|---
     8|
     9|## The `user.define_outcome` event
    10|
    11|Outcomes are not a field on `sessions.create()`. You create a normal session, then send a `user.define_outcome` event. The agent starts working on receipt — **do not also send a `user.message`** to kick it off.
    12|
    13|```python
    14|session = client.beta.sessions.create(
    15|    agent=AGENT_ID,
    16|    environment_id=ENVIRONMENT_ID,
    17|    title="Financial analysis on Costco",
    18|)
    19|
    20|client.beta.sessions.events.send(
    21|    session_id=session.id,
    22|    events=[
    23|        {
    24|            "type": "user.define_outcome",
    25|            "description": "Build a DCF model for Costco in .xlsx",
    26|            "rubric": {"type": "text", "content": RUBRIC_MD},
    27|            # or: "rubric": {"type": "file", "file_id": rubric.id}
    28|            "max_iterations": 5,  # optional; default 3, max 20
    29|        }
    30|    ],
    31|)
    32|```
    33|
    34|| Field | Type | Notes |
    35|| --- | --- | --- |
    36|| `type` | `"user.define_outcome"` |  |
    37|| `description` | string | The task. This is what the agent works toward — no separate `user.message` needed. |
    38|| `rubric` | `{type: "text", content}` \| `{type: "file", file_id}` | **Required.** Markdown with explicit, independently gradeable criteria. Upload once via `client.beta.files.upload(...)` (beta `files-api-2025-04-14`) to reuse across sessions. |
    39|| `max_iterations` | int | Optional. Default **3**, max **20**. |
    40|
    41|The event is echoed back on the stream with a server-assigned `outcome_id` and `processed_at`.
    42|
    43|> **Writing rubrics.** Use explicit, gradeable criteria ("CSV has a numeric `price` column"), not vibes ("data looks good") — the grader scores each criterion independently, so vague criteria produce noisy loops. If you don't have a rubric, have Claude analyze a known-good artifact and turn that analysis into one.
    44|
    45|---
    46|
    47|## Outcome-specific events
    48|
    49|These appear on the standard event stream (`sessions.events.stream` / `.list`) alongside the usual `agent.*` / `session.*` events.
    50|
    51|| Event | Payload highlights | Meaning |
    52|| --- | --- | --- |
    53|| `span.outcome_evaluation_start` | `outcome_id`, `iteration` (0-indexed) | Grader began scoring iteration _N_. |
    54|| `span.outcome_evaluation_ongoing` | `outcome_id` | Heartbeat while the grader runs. Grader reasoning is opaque — you see _that_ it's working, not _what_ it's thinking. |
    55|| `span.outcome_evaluation_end` | `outcome_evaluation_start_id`, `outcome_id`, `iteration`, `result`, `explanation`, `usage` | Grader finished one iteration. `result` drives what happens next (table below). |
    56|
    57|### `span.outcome_evaluation_end.result`
    58|
    59|| `result` | Next |
    60|| --- | --- |
    61|| `satisfied` | Session → `idle`. Terminal for this outcome. |
    62|| `needs_revision` | Agent starts another iteration. |
    63|| `max_iterations_reached` | No further grader cycles. Agent may run one final revision, then session → `idle`. |
    64|| `failed` | Session → `idle`. Rubric fundamentally doesn't match the task (e.g. description and rubric contradict). |
    65|| `interrupted` | Only emitted if `_start` had already fired before a `user.interrupt` arrived. |
    66|
    67|```json
    68|{
    69|  "explanation": "All 12 criteria met: revenue projections use 5 years of historical data, ...",
    70|  "id": "sevt_01jkl...",
    71|  "iteration": 0,
    72|  "outcome_evaluation_start_id": "sevt_01def...",
    73|  "outcome_id": "outc_01a...",
    74|  "processed_at": "2026-03-25T14:03:00Z",
    75|  "result": "satisfied",
    76|  "type": "span.outcome_evaluation_end",
    77|  "usage": {
    78|    "input_tokens": 2400,
    79|    "output_tokens": 350,
    80|    "cache_creation_input_tokens": 0,
    81|    "cache_read_input_tokens": 1800
    82|  }
    83|}
    84|```
    85|
    86|---
    87|
    88|## Checking status & retrieving deliverables
    89|
    90|**Status** — either watch the stream for `span.outcome_evaluation_end`, or poll the session and read `outcome_evaluations`:
    91|
    92|```python
    93|session = client.beta.sessions.retrieve(session.id)
    94|for ev in session.outcome_evaluations:
    95|    print(f"{ev.outcome_id}: {ev.result}")  # outc_01a...: satisfied
    96|```
    97|
    98|**Deliverables** — the agent writes to `/mnt/session/outputs/`. Once idle, fetch via the Files API with `scope_id=session.id`. This is the same session-outputs mechanism documented in `shared/managed-agents-environments.md` → Session outputs (including the dual-beta-header requirement on `files.list`).
    99|
   100|---
   101|
   102|## Interaction rules & pitfalls
   103|
   104|- **One outcome at a time.** Chain by sending the next `user.define_outcome` only after the previous one's terminal `span.outcome_evaluation_end` (`satisfied` / `max_iterations_reached` / `failed` / `interrupted`). The session retains history across chained outcomes.
   105|- **Steering is allowed but optional.** You _may_ send `user.message` events mid-outcome to nudge direction, but the agent already knows to keep working until terminal — don't send "keep going" prompts.
   106|- **`user.interrupt` pauses the current outcome** — it marks `result: "interrupted"` and leaves the session `idle`, ready for a new outcome or conversational turn.
   107|- **After terminal, the session is reusable** — continue conversationally or define a new outcome.
   108|- **Outcome ≠ session-create field.** Don't put `outcome`, `rubric`, or `description` on `sessions.create()` — outcomes are always sent as a `user.define_outcome` event.
   109|- **Idle-break gate is unchanged.** In your drain loop, keep using `event.type === 'session.status_idle' && event.stop_reason?.type !== 'requires_action'` — do **not** gate on `span.outcome_evaluation_end` alone (on `needs_revision` the session keeps running). See `shared/managed-agents-client-patterns.md` Pattern 5.
   110|
   111|For the raw HTTP shapes and per-language SDK bindings beyond Python, WebFetch `https://platform.claude.com/docs/en/managed-agents/define-outcomes.md` (see `shared/live-sources.md`).
   112|