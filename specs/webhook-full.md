---
sidebar_position: 16
title: "Persistent Goals"
description: "Set a standing goal and let Hermes keep working across turns until it is done. Our take on the Ralph loop."
status: "in_progress"
---


# Webhook Implementation Spec — Hermes Agent

> Status: DRAFT | Version: 1.0.0 | Profile: adminbot | Date: 2026-09-13
> Source: `hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks` (retrieved via search + GitHub mirror).

## 1. Architecture Overview

The webhook adapter is an HTTP server (default port `8644`, bind `0.0.0.0` or loopback) that accepts `POST` requests, validates HMAC signatures, transforms payloads into agent prompts, runs agent loops (or direct delivery), and routes responses back to the source or to a configured messaging platform.

Two config sources coexist; static routes in `platforms.webhook.extra.routes` (in `config.yaml`) take precedence over dynamic subscriptions in `~/./webhook_subscriptions.json` when names collide. Dynamic subscriptions are hot-reloaded (mtime-gated) per incoming request.

## 2. Route Schema (full, per docs)

Every route (static or dynamic) is a JSON/YAML object with these properties:

- `events`: `List[str]` — event types accepted (`pull_request`, `push`, `issues`, `merge_request`, etc.). Empty = all accepted. Read from `X-GitHub-Event`, `X-GitLab-Event`, or `event_type` in payload.
- `secret`: `str` — HMAC secret. Required. Falls back to global `secret`. `"INSECURE_NO_AUTH"` skips validation but is ONLY accepted when bind is loopback (`127.0.0.1`, `localhost`, `::1`); combined with non-loopback bind, adapter refuses to start (security invariant).
- `profile`: `str` — profile binding for multiplex profiles; binds secret to `/p/<profile>/webhooks/<route>`.
- `prompt`: `str` — dot-notation template. Missing keys kept literal (no error). Nested objects/lists JSON-serialized and truncated at 2000 chars. `{__raw__}` dumps full payload (indented JSON, truncated at 4000 chars). If omitted, full payload dumped at 4000.
- `filters`: `List[dict]` — declarative payload filters. Operators: `exists`, `missing`, `equals`, `not_equals`, `contains`, `in`, `in_file`, `regex`, `all`, `any`, `not`. Field paths use dot notation (`payload.foo`, `event`, `headers.Name`). Non-match → `{"status":"ignored","reason":"filter"}` with HTTP 200.
- `script`: `str` — path under `~/./scripts/` (relative resolves there; traversal blocked). `.sh`/`.bash` → bash; others → current Python interpreter. Payload sent as JSON stdin. JSON stdout replaces payload; text stdout added as `script_output`; empty/stdout=`[SILENT]`/`{"__hermes_ignore__":true}` or nonzero exit → `ignored` (HTTP 200, `reason: script`).
- `skills`: `List[str]` — skill names loaded for agent run.
- `toolsets`: `List[str]` — replaces platform-level webhook toolset for this route only. Unknown/restricted names dropped. Manual config-file edit only — `hermes webhook subscribe` does NOT accept `toolsets` (agent cannot self-grant terminal/file/code_execution at runtime).
- `deliver`: `str` — `github_comment`, `telegram`, `discord`, `slack`, `signal`, `sms`, `whatsapp`, `matrix`, `mattermost`, `homeassistant`, `email`, `dingtalk`, `feishu`, `wecom`, `weixin`, `bluebubbles`, `qqbot`, `log` (default). Must be real target (not `log`) when `deliver_only: true`; adapter refuses to start otherwise.
- `deliver_extra`: `dict` — additional delivery config. Keys depend on `deliver`. Values support same `{dot.notation}` templates as `prompt`. Example: `{repo: "{repository.full_name}", pr_number: "{number}"}`.
- `deliver_only`: `bool` — if `true`, skip agent entirely; rendered `prompt` becomes literal message delivered synchronously. Zero LLM cost; sub-second. Same HMAC/auth/rate/idempotency applies. Response: `200 OK` + `{"status":"delivered","route":"...","target":"...","delivery_id":"..."}`; duplicate → `status=duplicate`; target rejection → `502` (generic error, no adapter internals leaked).

## 3. Signature Verification (security layer)

| Source | Header(s) | Method |
|---|---|---|
| GitHub | `X-Hub-Signature-256` | HMAC-SHA256 hex, prefixed `sha256=` |
| GitLab | `X-Gitlab-Token` | Plain secret string match (exact) |
| Standard Webhooks | `webhook-id`, `webhook-timestamp`, `webhook-signature` | Signed content = `{id}.{timestamp}.{raw_body}`; `v1,<base64-hmac-sha256>` |
| Generic V2 (recommended) | `X-Webhook-Signature-V2` + `X-Webhook-Timestamp` | HMAC-SHA256 of `<timestamp>.<body>`; timestamp in Unix seconds; must be within ±300s of server clock (replay protection) |
| Generic V1 (legacy) | `X-Webhook-Signature` | Raw HMAC-SHA256 of body; no replay protection; gateway logs deprecation warning once per route; switch senders to V2 |

Rules:
- If secret configured but no recognized header present → reject.
- If `secret` missing (and no global fallback) → adapter fails at startup.
- `INSECURE_NO_AUTH` + loopback only; else adapter refuses to start.
- Multi-profile routing: request with valid route signature rejected if `/p/<profile>/` prefix does not match route `profile` binding.

## 4. Rate Limiting, Idempotency, Body Size

- Rate limit: 30 req/min per route (fixed-window). Configurable globally: `platforms.webhook.extra.rate_limit` (int, requests/min).
- Idempotency: delivery IDs cached 1 hour. Headers used (priority): `X-GitHub-Delivery`, `svix-id`, `webhook-id`, `X-Request-ID`, timestamp fallback. Duplicate → `200` + `status=duplicate`; no re-delivery.
- Max body bytes: default 1 MB (`1048576`). Configurable globally: `platforms.webhook.extra.max_body_bytes`.
- Body > max → `413 Payload Too Large` before reading full body.
- Rate exceeded → `429 Too Many Requests`.

## 5. Prompt Template Syntax (verified from docs)

- `{pull_request.title}` → payload key access (nested dicts serialized; lists serialized; truncated at 2000 chars per nested value).
- `{repository.full_name}` → nested access.
- `{__raw__}` → full indented JSON payload (truncated at 4000 chars).
- Missing key → literal `{key}` string preserved (no error raised).
- `deliver_extra` values use same syntax (e.g. `repo: "{repository.full_name}"`, `pr_number: "{number}"`, `chat_id: "{match.telegram_chat_id}"`).
- `script_output` exposed as a payload field after script execution when stdout is non-JSON text.

## 6. Security Invariant (non-negotiable)

> Authenticated ≠ trusted. HMAC validates sender identity, not payload content. PR titles, commit messages, issue descriptions, and any upstream text authored by arbitrary third parties must be treated as untrusted input.

Hardening rules (from docs warning box):
1. Sandbox runtime: use Docker or SSH terminal backend (or VM) when exposed to internet; a hijacked turn must not touch host.
2. Scope toolset: disable `terminal`, `file`, outbound-action tools on webhook-triggered sessions if route only reads/summarizes. Fewer capabilities = smaller blast radius.
3. Keep approvals on for destructive/outbound operations; injected instruction cannot act unattended.
4. Template narrowly: prefer named fields (`{pull_request.title}`) over `{__raw__}` or empty template that dumps full payload; only intended fields reach prompt.
5. Never set `secret: "INSECURE_NO_AUTH"` on any route that binds to non-loopback interface; adapter refuses to start.

## 7. Per-route Toolsets (subgoal SG5/SG6)

Default webhook toolset is constrained (`web_search`, `web_extract`, `vision_analyze`, `clarify`) because payloads may contain untrusted third-party content.

Grant wider toolsets only to trusted routes (localhost monitor, internal CI) and ONLY via manual `config.yaml` edit — never via `hermes webhook subscribe`. Example route:

```yaml
routes:
  oom-emergency:
    secret: "monitor-secret"
    prompt: "Memory emergency: {detail}. Diagnose with ps/free/py-spy and report."
    toolsets: ["terminal", "file", "code_execution", "web"]
    deliver: "telegram"
```

Validation: unknown/restricted names dropped; route-level list replaces (not merges) platform-level webhook toolset.

## 8. Dynamic Subscriptions (subgoal SG1/SG6)

- CLI: `hermes webhook subscribe <route> --events ... --prompt ... --deliver ... --deliver-extra ... --description ...`
- Storage: `~/./webhook_subscriptions.json` (hot-reloaded per request, mtime-gated).
- `hermes webhook list`, `hermes webhook remove <route>`, `hermes webhook test <route>`, `hermes webhook test --payload '{...}'`.
- Agent-driven: `webhook-subscriptions` skill guides agent; agent runs `hermes webhook subscribe` via terminal tool.
- Dynamic subscriptions CANNOT set `toolsets` (manual file edit only).

## 9. Direct Delivery Mode (subgoal SG3/SG6)

`deliver_only: true` skips agent; rendered `prompt` becomes literal message delivered synchronously.
- Requires `deliver` to be real target (not `log`); adapter refuses to start otherwise.
- `skills` ignored (no agent runs).
- Template uses same `{dot}` syntax, including `{__raw__}`.
- Idempotency same headers (`X-GitHub-Delivery`, etc.); duplicates return `status=duplicate`.
- Response codes: `200 OK` delivered; duplicate `200` (status=duplicate); auth fail `401`; bad body `400`; unknown route `404`; body too large `413`; rate limit `429`; target reject `502` (generic `"Delivery failed"` body; adapter internals never leaked).

## 10. Cross-Platform Delivery (verified from docs)

Supported `deliver` targets (must be enabled/connected in gateway): `github_comment`, `telegram`, `discord`, `slack`, `signal`, `sms`, `whatsapp`, `matrix`, `mattermost`, `homeassistant`, `email`, `dingtalk`, `feishu`, `wecom`, `weixin`, `bluebubbles`, `qqbot`, `log`.

`github_comment`: uses `gh` CLI; requires `gh auth login` and write access; requires `deliver_extra.repo` and `deliver_extra.pr_number`.

`telegram` forum topic delivery: include `message_thread_id` (or `thread_id`) in `deliver_extra`. If `chat_id` missing in `deliver_extra`, falls back to platform home channel.

## 11. Subgoals → Deliverable Mapping (verified)

| Subgoal | Deliverable file(s) | Section reference |
|---|---|---|
| SG1 (spec) | `./specs/webhook-full.md` (this file) | Sections 1–11 |
| SG2 (plan) | `./plans/webhook-execution-plan.md` | Milestones M1–M4 |
| SG3 (prompt) | `.github/prompts/webhook/webhook-template.md`, `.github/prompts/webhook/direct-delivery-template.md` | Section 5 |
| SG4 (scripts) | `scripts/webhook_filter_todoist.py` (filter/transform), `scripts/webhook_test_payload.py` (test) | Section 2 (`script`) |
| SG5 (skills) | `skills/webhook-subscriptions.md` (SKILL.md), `skills/per-route-toolsets.md` (SKILL.md) | Sections 7–8 |
| SG6 (routes/config) | `docs/webhook-routes-config.md`, `.env.webhook-example`, `webhook_subscriptions-example.json` | Sections 2–4, 6–9 |
| SG7 (impl prompt) | `.github/prompts/webhook/implementation-prompt.md` | References SG1–SG6 |
| SG8 (verify) | `docs/webhook-implementation-report.md` | Checklist of 8 gates |

## 12. Verification Gates (per subgoal)

- SG1: file exists; sections 1–11 present; no fabricated session IDs; security invariant (§6) present.
- SG2: milestones M1–M4 listed; sequential order noted; resources listed.
- SG3: both prompt files render `{dot}` + `{__raw__}`; no invented APIs.
- SG4: both scripts executable; `todoist` script produces either JSON stdout or `[SILENT]` + SystemExit(0) for non-match case.
- SG5: each SKILL.md ≥10 lines body; frontmatter (`name`, `title`, `version`, `tags`) present.
- SG6: all 3 routes (`github-pr`, `deploy-notify`, `oom-emergency`) have real secrets; none is `INSECURE_NO_AUTH`; `oom-emergency` has `toolsets`; `deliver:` for `github-pr` is real (`github_comment`); `deploy-notify` uses `deliver_only: true` + real `deliver`.
- SG7: prompt references SG1–SG6 by file name; uses exact output of SG1–SG6 as inputs (per skill-combining rule).
- SG8: final checklist verified against real files; session log appended with `current_state`, `verified_items`, `open_items`.

## 13. References (verified sources used)

- `hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks` (description retrieved via web_search; original page did not load via web_extract/browser — reported honestly).
- GitHub mirror: `github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/messaging/webhooks.md` (search snippet; full fetch blocked — noted).
- Related docs retrieved: messaging gateway (`messaging.md`), event hooks (`hooks.md`), web dashboard (`web-dashboard.md`), GitHub PR review walkthrough (same docs page), security vulnerability issue #6440 (critical `INSECURE_NO_AUTH` RCE — cited as blocker, not followed).
- Memory: `SESSION_REPORT.md` read; profile=default/adminbot + tutor; workspace `~/Desktop/SandBox`; branch clean.
