---
name: shared-managed-agents-webhooks
description: "Managed Agents — Webhooks"
version: 1.0.0
author: Alexa
---
     1|# Managed Agents — Webhooks
     2|
     3|Anthropic can POST to your HTTPS endpoint when a Managed Agents resource changes state — an alternative to holding an SSE stream or polling. Payloads are **thin** (event type + resource IDs only); on receipt, fetch the resource for current state. Every delivery is HMAC-signed.
     4|
     5|> **Direction matters.** This page covers _Anthropic → you_ notifications about session/vault state. It does **not** cover _third-party → you_ webhooks that _trigger_ a session (e.g. a GitHub push handler that calls `sessions.create()`) — that's ordinary application code on your side with no Anthropic-specific wire format.
     6|
     7|---
     8|
     9|## Register an endpoint (Console only)
    10|
    11|Console → **Manage → Webhooks**. There is no programmatic endpoint-management API yet. Secret rotation is supported from the same page.
    12|
    13|| Field | Constraint |
    14|| --- | --- |
    15|| URL | HTTPS on port 443, publicly resolvable hostname |
    16|| Event types | Subscribe per `data.type` — you only receive subscribed types (plus test events) |
    17|| Signing secret | `whsec_`-prefixed, 32 bytes, **shown once at creation** — store it |
    18|
    19|---
    20|
    21|## Verify the signature
    22|
    23|Every delivery is HMAC-signed. **Use the SDK's `client.beta.webhooks.unwrap()`** — it verifies the signature, rejects payloads more than ~5 minutes old, and returns the parsed event. It reads the `whsec_` secret from `ANTHROPIC_WEBHOOK_SIGNING_KEY`.
    24|
    25|```python
    26|import anthropic
    27|from flask import Flask, request
    28|
    29|client = anthropic.Anthropic()  # reads ANTHROPIC_WEBHOOK_SIGNING_KEY from env
    30|app = Flask(__name__)
    31|
    32|
    33|@app.route("/webhook", methods=["POST"])
    34|def webhook():
    35|    try:
    36|        event = client.beta.webhooks.unwrap(
    37|            request.get_data(as_text=True),
    38|            headers=dict(request.headers),
    39|        )
    40|    except Exception:
    41|        return "invalid signature", 400
    42|
    43|    if event.id in seen_event_ids:  # dedupe retries — id is per-event, not per-delivery
    44|        return "", 204
    45|    seen_event_ids.add(event.id)
    46|
    47|    match event.data.type:
    48|        case "session.status_idled":
    49|            session = client.beta.sessions.retrieve(event.data.id)
    50|            notify_user(session)
    51|        case "vault_credential.refresh_failed":
    52|            alert_oncall(event.data.id)
    53|
    54|    return "", 204
    55|```
    56|
    57|Pass the **raw request body** to `unwrap()` — frameworks that re-serialize JSON (Express `.json()`, Flask `.get_json()`) change the bytes and break the MAC. For other languages, look up the `beta.webhooks.unwrap` binding in the SDK repo (`shared/live-sources.md`); don't hand-roll verification.
    58|
    59|---
    60|
    61|## Payload envelope
    62|
    63|```json
    64|{
    65|  "created_at": "2026-03-18T14:05:22Z",
    66|  "data": {
    67|    "type": "session.status_idled",
    68|    "id": "session_01XYZ...",
    69|    "organization_id": "8a3d2f1e-...",
    70|    "workspace_id": "c7b0e4d9-..."
    71|  },
    72|  "id": "event_01ABC...",
    73|  "type": "event"
    74|}
    75|```
    76|
    77|Switch on `data.type`, fetch the resource by `data.id`, return any **2xx** to acknowledge. `created_at` is when the _state transition_ happened, not when the webhook fired.
    78|
    79|---
    80|
    81|## Supported `data.type` values
    82|
    83|| `data.type` | Fires when |
    84|| --- | --- |
    85|| `session.status_scheduled` | Session created and ready to accept events |
    86|| `session.status_run_started` | Agent execution kicked off (every transition to `running`) |
    87|| `session.status_idled` | Agent awaiting input (tool approval, custom tool result, or next message) |
    88|| `session.status_terminated` | Session hit a terminal error |
    89|| `session.thread_created` | Multiagent: coordinator opened a new subagent thread |
    90|| `session.thread_idled` | Multiagent: a subagent thread is waiting for input |
    91|| `session.outcome_evaluation_ended` | Outcome grader finished one iteration |
    92|| `vault.archived` | Vault was archived |
    93|| `vault.created` | Vault was created |
    94|| `vault.deleted` | Vault was deleted |
    95|| `vault_credential.archived` | Vault credential was archived |
    96|| `vault_credential.created` | Vault credential was created |
    97|| `vault_credential.deleted` | Vault credential was deleted |
    98|| `vault_credential.refresh_failed` | MCP OAuth vault credential failed to refresh |
    99|
   100|> These are **webhook** `data.type` values — a separate namespace from SSE event types (`session.status_idle`, `span.outcome_evaluation_end`, etc. in `shared/managed-agents-events.md`). Don't reuse SSE constants in webhook handlers.
   101|
   102|---
   103|
   104|## Delivery behavior & pitfalls
   105|
   106|- **No ordering guarantee.** `session.status_idled` may arrive before `session.outcome_evaluation_ended` even if the evaluation finished first. Sort by envelope `created_at` if order matters.
   107|- **Retries carry the same `event.id`.** At least one retry on non-2xx. Dedupe on `event.id`.
   108|- **3xx is failure.** Redirects are not followed — update the URL in Console if your endpoint moves.
   109|- **Auto-disable** after ~20 consecutive failed deliveries, or immediately if the hostname resolves to a private IP or returns a redirect. Re-enable manually in Console.
   110|- **Thin payload is intentional.** Don't expect `stop_reason`, `outcome_evaluations`, credential secrets, etc. on the webhook body — fetch the resource.
   111|