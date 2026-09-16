---
name: per-route-toolsets
version: 1.0.0
tags: [security, webhooks, gateway]
---
# Per-Route Toolsets Skill

Default webhook toolset is constrained (`web_search`, `web_extract`, `vision_analyze`, `clarify`) because payloads contain untrusted content. Elevated toolsets (`terminal`, `file`, `code_execution`, `web`) granted ONLY to trusted routes via manual `config.yaml` edit — `hermes webhook subscribe` does NOT accept `toolsets` (prevents agent self-grant at runtime). Route-level list replaces (not merges) platform-level webhook toolset. Only grant to routes with real HMAC secrets on controlled interfaces.
