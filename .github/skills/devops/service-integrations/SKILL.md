---
name: service-integrations
title: Service Integrations
description: "Wire external services (GitHub, Stripe, Sentry, Cal.com, TypeForm, Helius, Beehiv, Home Assistant) to Hermes webhooks for event-driven automation."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [webhook, integrations, automation, events, github, stripe, sentry, iot]
    related_skills: [webhook-subscriptions, native-mcp]
---

# Service Integrations

Connect external services to Hermes Agent via webhooks so the agent reacts
to events — PRs, payments, errors, form submissions, sensor trips, bookings,
and subscriber changes — without polling.

## Architecture

```
External Service (GitHub, Stripe, Sentry, ...)
  │ POST JSON event
  ▼
ngrok/cloudflared tunnel (exposes localhost:8644)
  │
  ▼
Hermes Gateway → Webhook Adapter (localhost:8644)
  │ match route → format prompt → spawn agent run
  ▼
Agent processes event, loads skills, decides action
  │
  ├─ GitHub: posts PR review comment via API
  ├─ Stripe: drafts email or flags fraud
  ├─ Sentry: pages oncall via Telegram
  ├─ Cal.com: writes pre-meeting briefing
  ├─ TypeForm: creates CRM entry + Slack draft
  ├─ Helius: sends Telegram alert with Solscan link
  ├─ Beehiv: enriches lead, routes to pipeline
  └─ Home Assistant: investigates sensor anomaly
```

## Prerequisites

- Hermes gateway installed (`hermes gateway run`)
- Webhook platform enabled (see Setup below)
- Public tunnel (ngrok / cloudflared) for local dev — webhook URLs must be
  reachable from the internet
- `hermes webhook list` returns subscriptions (not "platform not enabled")

## Setup: Enable Webhook Platform

CLI approach (preferred — avoids manual YAML editing):

```bash
hermes config set platforms.webhook.enabled true
hermes config set platforms.webhook.extra.host "0.0.0.0"
hermes config set platforms.webhook.extra.port 8644
hermes config set platforms.webhook.extra.secret "your-global-hmac-secret"
```

Verify with `curl http://localhost:8644/health` — returns `{"status":"ok"}`.

## Common Integration Patterns

### Action-Dispatching Prompts

Design prompts that embed decision logic so the agent routes the event
without needing a second invocation:

```text
Determine action:
- If amount > 100000 (1000 USD) OR dispute → FLAG FOR FRAUD REVIEW
- If new customer (first payment) → DRAFT welcome email
- If payment_failed → LOG and notify
- Otherwise → ACKNOWLEDGE
```

### Loading Skills per Route

Pass `--skills` to load domain-specific skills into the webhook agent session:

```bash
--skills "github-code-review"
```

The agent has full tool access — it can call GitHub API, search the web,
read files, etc. within the webhook handler session.

### Delivery Targets

All subscriptions default to `deliver: log`. To route agent output to a
messaging platform, add `--deliver <platform> --deliver-chat-id "<id>"`:

```bash
hermes webhook subscribe <name> \
  --deliver telegram \
  --deliver-chat-id "-1001234567890"
```

Supported platforms: telegram, discord, slack, github_comment, email, sms, origin.

## ⚠️ Bash Escaping Pitfall

When running `hermes webhook subscribe` from bash with a complex prompt:

```bash
# THIS FAILS — bash interprets ${...} as variable substitution
hermes webhook subscribe stripe-payments \
  --prompt "Status: {data.object.status} Amount: ${data.object.amount}"
# → bad substitution error
```

**Fix:** Write prompts to temp files with a quoted heredoc:

```bash
cat > /tmp/prompt.txt << 'PROMPT_EOF'
Status: {data.object.status}
Amount: {data.object.amount}
PROMPT_EOF

hermes webhook subscribe stripe-payments \
  --prompt "$(cat /tmp/prompt.txt)" \
  --events "payment_intent.succeeded"

rm /tmp/prompt.txt
```

The `'PROMPT_EOF'` delimiter (single-quoted) prevents ALL bash expansion.
For short single-line prompts, single quotes also work:
`--prompt 'Event {type} from {data.actor}'`

## Batch Setup Pattern (5+ Subscriptions)

For mass subscription creation, write all prompts first, subscribe all, then
clean up:

```bash
# Phase 1: Write all prompt files
cat > /tmp/p-github.txt << 'EOF'
Review this PR...
EOF
cat > /tmp/p-stripe.txt << 'EOF'
Payment event...
EOF
# ...

# Phase 2: Subscribe all routes
for route in github stripe sentry cal typeform helius beehive homeassist; do
  hermes webhook subscribe "$route" --prompt "$(cat /tmp/p-$route.txt)" ...
done

# Phase 3: Clean up
rm /tmp/p-*.txt
```

## Service-Specific Configuration

Each service needs its webhook configured with:
- **Payload URL:** `https://<tunnel-url>/webhooks/<route-name>`
- **Secret:** The HMAC secret returned by `hermes webhook subscribe` (or set with `--secret`)
- **Events:** The event types listed in the subscription's `--events` filter

| Service | Setup Location | Recommended Events |
|---------|---------------|-------------------|
| GitHub | Repo → Settings → Webhooks | `pull_request` |
| Stripe | Dashboard → Developers → Webhooks | `payment_intent.succeeded`, `payment_intent.payment_failed`, `charge.dispute.created` |
| Sentry | Settings → Integrations → Webhook | `event.alert` |
| Cal.com | Settings → Webhooks | `BOOKING_CREATED` |
| TypeForm | Connect → Webhook | `form_response` |
| Helius | Dashboard → Webhooks | `transaction`, `nft`, `account` |
| Beehiv | Settings → Integrations → Webhooks | `subscriber.created`, `subscriber.unsubscribed` |
| Home Assistant | Settings → Automations → Webhook | `state_changed` |

## Testing a Subscription

```bash
# Gateway must be running
hermes gateway run

# In another terminal, test the route:
hermes webhook test <name>
hermes webhook test <name> --payload '{"type": "test", "data": {"object": {"amount": 5000}}}'
```

Check gateway logs on failure:
```bash
grep webhook ~/.hermes/logs/gateway.log | tail -20
```

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `404` on POST | Wrong route name | Check `hermes webhook list` |
| `401` on POST | HMAC secret mismatch | Compare secret in service config vs `hermes webhook list` |
| POST times out | No tunnel or gateway not running | Start gateway + tunnel |
| Agent run doesn't fire | Event filter mismatch | Check `--events` matches what the service sends |
| `${...}` error on subscribe | Bash variable expansion | Use prompt file pattern above |

## When to Use

- When wiring external SaaS platforms to trigger Hermes agent runs
- When setting up event-driven automation pipelines (CI, payments, support)
- When replacing polling-based monitoring with push-based webhook alerts
- When you need the agent to triage, decide, and act on external events

## Workflow

### Phase 1: Enable Platform
Use `hermes config set` to enable webhooks. Start gateway. Set up tunnel.

### Phase 2: Create Subscriptions
For each service, write prompt, subscribe route, note the returned URL + secret.

### Phase 3: Configure Services
In each external service's settings, add webhook pointing to tunnel URL + route.

### Phase 4: Test
Use `hermes webhook test <name>` to verify each route. Check logs on failure.

### Phase 5: Go Live
Ensure gateway and tunnel are running persistently (systemd, Docker, or background process).

## Verification Checklist

- [ ] Webhook platform enabled and gateway running
- [ ] Tunnel active and reachable from the internet
- [ ] Each subscription returns 200 on test
- [ ] External service configured with correct URL, secret, and events
- [ ] Agent output delivers to the right target (Telegram, Slack, etc.)

## Best Practices

1. **Use prompt files for complex prompts** — avoids bash escaping and makes prompts easier to edit
2. **Test before going live** — `hermes webhook test <name> --payload '{...}'` catches most issues
3. **Log delivery targets initially** — set up `deliver: log` first, verify the agent's output is correct, then add real delivery channels
4. **Tag subscriptions** — use descriptive names and `--description` so `hermes webhook list` is readable
5. **Keep the gateway running** — webhooks are fire-and-forget; if the gateway is down, events are lost
