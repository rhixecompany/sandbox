---
name: webhook-subscriptions
version: 1.0.0
tags: [messaging, webhooks, gateway]
---
# Webhook Subscriptions Skill

Creates/manages dynamic webhook subscriptions via `hermes webhook subscribe/list/remove/test`. Subscriptions stored at `~/.hermes/webhook_subscriptions.json`, hot-reloaded. Dynamic routes CANNOT set `toolsets` (manual config only — prevents runtime self-grant). Uses same route format/capabilities as static routes (`events`, `prompt`, `filters`, `deliver`, `deliver_only`). Agent-driven: agent runs `hermes webhook subscribe` when guided.
