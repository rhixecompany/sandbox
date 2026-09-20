---
sidebar_position: 16
title: "Persistent Goals"
description: "Set a standing goal and let Hermes keep working across turns until it is done. Our take on the Ralph loop."
status: "in_progress"
---

# Webhook Implementation — Verified State (SG8 Update)

> Updated: 2026-09-13 | Protocol: multi-file-change-protocol (sequential) | Profile: adminbot

## SG1–SG7 Verified Status (gates passed / total)

| SG         | Deliverable                                      | File(s)                                                                                       | Gate Status                                                                                                                                                                                                                                         |
| ---------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SG1        | Spec                                             | `./specs/webhook-full.md`                                                                     | PASS — 13 sections; no fabricated session IDs; security invariant §6 present                                                                                                                                                                        |
| SG2        | Plan                                             | `./plans/webhook-execution-plan.md`                                                           | PASS — M1–M4 milestones; sequential order; 8 subgoals; resources listed                                                                                                                                                                             |
| SG3        | Prompt templates                                 | `.github/prompts/webhook/webhook-template.md` + `direct-delivery-template.md`                 | PASS — `{dot}`, `{__raw__}`, response codes, security notes                                                                                                                                                                                         |
| SG4        | Scripts                                          | `scripts/webhook_filter_todoist.py` + `scripts/webhook_test_payload.py`                       | PASS — filter produces `[SILENT]` + SystemExit(0) or JSON stdout; test builds payloads for 3 routes                                                                                                                                                 |
| SG5        | Skills                                           | `skills/webhook-subscriptions.md` (SKILL.md), `skills/per-route-toolsets.md` (SKILL.md)       | PASS — both ≥10 body lines; frontmatter complete; no stub/duplicate                                                                                                                                                                                 |
| SG6        | Routes + config refs                             | `docs/webhook-routes-config.md`, `.env.webhook-example`, `webhook_subscriptions-example.json` | PASS — 3 routes present (`github-pr`, `deploy-notify`, `oom-emergency`); none use `INSECURE_NO_AUTH`; `oom-emergency` has `toolsets`; `deliver` real (`github_comment`/`telegram`); filters present on `deploy-notify`; `deliver_only:true` present |
| SG7        | Implementation prompt                            | `.github/prompts/webhook/implementation-prompt.md`                                            | PASS — references SG1–SG6 by exact filenames; includes skill-combining note; security reminder                                                                                                                                                      |
| SG8 (this) | Implementation spec update + verification report | `./specs/webhook-implementation.md`, `docs/webhook-implementation-report.md`                  | IN PROGRESS — final gate after report verified                                                                                                                                                                                                      |

## Adjustments From Original Plan (SG2)

None required. The 8-subgoal sequential plan executed as designed. No parallel delegation was needed (user selected sequential execution). No destructive operations beyond file creation were performed; no `config.yaml` or `.env` file was overwritten in place — only reference/example files created (`.env.webhook-example`, `docs/webhook-routes-config.md`, `webhook_subscriptions-example.json`). The user must manually apply route config to `~/./config.yaml` and rotate placeholder secrets.

## Security Verification (re-checked at SG8)

- No file in SG1–SG7 contains a route with `secret: "INSECURE_NO_AUTH"`.
- `docs/webhook-routes-config.md` explicitly warns: "Secret is real HMAC; never `"INSECURE_NO_AUTH"`; adapter binds to loopback by default but refuses non-loopback + no-auth combo."
- `skills/per-route-toolsets.md` repeats: only manual config-file edit grants `toolsets`; `hermes webhook subscribe` does not accept it; never grant `terminal`/`file` to public/untrusted endpoints.
- Prompt templates (`.github/prompts/webhook/webhook-template.md`) recommend named fields over `{__raw__}` for untrusted routes.
- `.env.webhook-example` uses placeholder `global-fallback-secret-placeholder` (not a real secret) and notes: "REPLACE in production; not for commit."

## References (verified sources — never fabricated)

- `hermes-agent.nousresearch.com/docs/user-guide/messaging/webhooks` (description retrieved via web_search; original page not accessible via web_extract/browser — reported honestly in SG1).
- GitHub mirror snippet: `github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/messaging/webhooks.md` (partial retrieval; full file blocked — noted).
- Related docs retrieved: messaging gateway, event hooks, web dashboard (search snippets verified).
- Memory: `SESSION_REPORT.md` confirms session ID `cron_33eb54fc37c6_20260910_234920`, profile `default`, workspace `~/Desktop/SandBox`, model `nemotron-3.5-lightning-free` (previous session; this session uses `thinking` mode as configured).
- No synthetic session IDs invented; `current_state` in this file reflects real verified artifacts.

## Open Items (post-SG8 — for user to complete)

- [ ] Rotate `.env.webhook-example` placeholder secrets → real values in production `~/./.env`.
- [ ] Apply `docs/webhook-routes-config.md` routes to real `~/./config.yaml`.
- [ ] Configure external webhook sources (GitHub repo Settings → Webhooks; GitLab project Settings → Webhooks) with real URLs (`http://your-server:8644/webhooks/<route>`).
- [ ] Run `gh auth login` on gateway host for `github-pr` `github_comment` delivery.
- [ ] Test routes: `hermes webhook test github-issues --payload '{"issue":{"number":42,"title":"Test"}}'`; verify `/health` (`curl http://localhost:8644/health`).
- [ ] Restart gateway (`hermes gateway restart`) after config changes; confirm adapter starts (fails if route secrets missing or if `INSECURE_NO_AUTH` + non-loopback bind detected).
- [ ] Monitor gateway logs (`Invalid signature` = secret mismatch; `ignored` + `reason: filter/script` = expected non-match behavior).
