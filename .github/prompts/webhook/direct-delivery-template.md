---
name: direct-delivery-template
version: 1.0.0
description: Prompt template used in webhook direct-delivery mode (`deliver_only: true`) — zero LLM cost, sub-second synchronous delivery.
---

# Direct Delivery Mode — Webhook Template

## When Used

When a webhook route has `deliver_only: true`, the adapter skips the agent loop entirely. The rendered `prompt` template becomes the literal message body delivered synchronously to the configured `deliver` target (e.g. `telegram`, `discord`, `slack`).

Requirements (verified from docs):
- `deliver` must be a real target (not `log`); adapter refuses to start if misconfigured.
- `skills` is ignored (no agent runs).
- Same `{dot.notation}` syntax as agent-mode templates.
- Same HMAC auth, rate limits, idempotency, body-size limits apply.

## Example — Telegram push from external event

```yaml
prompt: "🎉 New match: {match.user_name} matched with you!"
deliver: "telegram"
deliver_extra:
  chat_id: "{match.telegram_chat_id}"
deliver_only: true
```

External service (e.g. Supabase edge function) signs payload with HMAC-SHA256 and POSTs to `https://your-server:8644/webhooks/antenna-matches`. The adapter validates the signature, renders `{match.user_name}` and `{match.telegram_chat_id}` from the payload, delivers to Telegram, and returns `200 OK`.

## Response Codes (for upstream retry logic)

| Status | Meaning |
|--------|---------|
| `200 OK` | Delivered successfully. Body: `{"status":"delivered","route":"...","target":"...","delivery_id":"..."}` |
| `200 OK` (status=duplicate) | Same delivery ID (`X-GitHub-Delivery`, `svix-id`, `webhook-id`, `X-Request-ID`) within 1-hour TTL. Not re-delivered. |
| `401 Unauthorized` | HMAC signature invalid or missing. |
| `400 Bad Request` | Malformed JSON body. |
| `404 Not Found` | Unknown route name. |
| `413 Payload Too Large` | Body exceeded `max_body_bytes` (default 1 MB; configurable globally). |
| `429 Too Many Requests` | Route rate limit exceeded (default 30/min; configurable globally). |
| `502 Bad Gateway` | Target adapter rejected message or raised. Error logged server-side; response body is generic `"Delivery failed"` (adapter internals never leaked to upstream). |

## Idempotency (same as agent mode)

- Delivery IDs cached for **1 hour**.
- Retries with same ID → `status=duplicate`; no re-delivery.
- Allows upstream services to retry safely without duplicate notifications.

## Security Note

Direct delivery does NOT reduce the trust boundary. The payload is still untrusted upstream content. HMAC validates the sender; it does not sanitize the message. If the payload contains `{message}` that an attacker controls, the attacker controls the delivered text. Design filters (`filters`) and narrow templates accordingly.
