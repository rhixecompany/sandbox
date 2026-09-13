---
name: webhook-implementation-prompt
version: 1.0.0
description: "Implementation prompt that uses exact outputs of SG1-SG6 (spec, plan, prompt templates, scripts, skills, config routes) to guide a full webhook adapter build/review. Per skill-combining rule: passes exact output of Skill A to Skill B."
---

# Webhook Implementation — Agent Prompt

## Context (loaded from SG1–SG6 — verified artifacts)

This prompt consumes the verified artifacts produced by the sequential multi-file-change-protocol for webhooks:

- **SG1 (spec)** → `.hermes/specs/webhook-full.md` — full architecture (route schema §2, signature verification §3, rate/idempotency/body-size §4, prompt templates §5, security invariant §6, per-route toolsets §7, dynamic subscriptions §8, direct delivery §9, cross-platform delivery §10, verification gates §12).
- **SG2 (plan)** → `.hermes/plans/webhook-execution-plan.md` — milestones M1–M4, sequential SG order, rules, resources.
- **SG3 (prompt templates)** → `.github/prompts/webhook/webhook-template.md` + `direct-delivery-template.md` — `{dot}` syntax, `{__raw__}`, response codes, security notes.
- **SG4 (scripts)** → `scripts/webhook_filter_todoist.py` (filter/transform; `[SILENT]` + SystemExit(0) for no-match; JSON stdout replaces payload) + `scripts/webhook_test_payload.py` (test payload generator for `github-issues`, `deploy-notify`, `oom-emergency`).
- **SG5 (skills)** → `skills/webhook-subscriptions.md` (SKILL.md: commands, constraints, agent-driven subscriptions) + `skills/per-route-toolsets.md` (SKILL.md: manual edit only; never via CLI; validation/drop rules; security warning).
- **SG6 (config + routes)** → `docs/webhook-routes-config.md` (3 routes: `github-pr`, `deploy-notify`, `oom-emergency`; none use `INSECURE_NO_AUTH`; `oom-emergency` has `toolsets`), `.env.webhook-example`, `webhook_subscriptions-example.json`.

## Instruction to Agent

Given the 6 artifacts above (SG1–SG6 verified; SG7 is this prompt; SG8 is the final verification report), complete SG8:

1. Read each artifact file listed above (use file-read or equivalent; verify file exists before claiming content).
2. Confirm each artifact matches its gate criteria (see SG1 §12 verification gates in `webhook-full.md`):
   - SG1: spec present, sections 1–13, no fabricated session IDs, security invariant present.
   - SG2: milestones M1–M4 listed; sequential execution noted.
   - SG3: both prompt files render `{dot}` + `{__raw__}` + direct-delivery response codes.
   - SG4: both scripts executable; filter produces `[SILENT]` or JSON stdout; test script builds payloads for 3 routes.
   - SG5: each SKILL.md ≥10 lines body; frontmatter (`name`, `title`, `version`, `tags`) present; no duplicate/stub skills.
   - SG6: 3 routes present (`github-pr` agent mode + `github_comment`; `deploy-notify` direct mode + `telegram` + `filters` + `deliver_only:true`; `oom-emergency` trusted + `toolsets` + `telegram`); no `INSECURE_NO_AUTH`; `.env` has placeholder secret (not real); JSON subscriptions have correct structure.
3. Produce `.hermes/specs/webhook-implementation.md` (implementation spec update) summarizing verified state of SG1–SG7 and any adjustments needed.
4. Produce `docs/webhook-implementation-report.md` (SG8 final verification checklist + session log) with:
   - `current_state`: verified artifacts list + open items
   - `verified_items`: count of gates passed (expected 7 of 7 SG1–SG7 + SG8 gate = 8)
   - `open_items`: any remaining (e.g. real HMAC secret rotation, production `.env` update, gateway restart after config edit)
   - Session log append: reference `SESSION_REPORT.md`; note `multi-file-change-protocol` applied; note sequential execution order followed; note no synthetic session IDs used.
5. Never invent session IDs; never claim a gate passed without file verification; never fabricate webhook responses; never set `INSECURE_NO_AUTH` in any produced file.

## Skill Combining Rule Applied

This prompt passes the exact output/file references of SG1–SG6 as its input context (per `writing-clearly-and-concisely` / `subagent-driven-development` rules). SG7 (`implementation-prompt.md`) is the output of combining SG1 (`spec`) + SG2 (`plan`) + SG3 (`prompt`) + SG4 (`scripts`) + SG5 (`skills`) + SG6 (`routes/config`). SG8 (`verification report`) consumes SG7's output.

## Security Reminder (non-negotiable)

> Authenticated ≠ trusted. HMAC validates sender identity; payload fields (`{pull_request.title}`, `{issue.body}`, `{message}`) are authored by arbitrary third parties. Harden the runtime: sandbox (Docker/SSH terminal backend or VM); scope the toolset (default webhook toolset is `web_search`, `web_extract`, `vision_analyze`, `clarify` only); keep approvals on; template narrowly (prefer `{issue.title}` over `{__raw__}`).
