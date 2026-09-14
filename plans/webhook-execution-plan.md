---
status: "in_progress"
---
# Implementation Plan — Webhooks (Hermes Agent)

> Protocol: multi-file-change-protocol (14 skills loaded; sequential execution; >6 files expected).
> Profile: adminbot (execution + verification gates).
> User approved: destructive operations yes; artifacts + live routes + all subgoals.

## Subgoals (sequential order — each gated before next)

| # | Subgoal | Files (est.) | Gate |
|---|---------|--------------|------|
| SG1 | Spec: full webhook architecture (routes, filters, scripts, security) | `.hermes/specs/webhook-full.md` | File exists; sections verified |
| SG2 | Plan: execution timeline + phases + milestones | `.hermes/plans/webhook-execution-plan.md` | Milestones listed |
| SG3 | Prompt: webhook-template + direct-delivery templates | `.github/prompts/webhook/` (3 files) | All prompts render `{dot}` + `{__raw__}` |
| SG4 | Scripts: filter script (`todoist-hermes-label.py`) + test payload script | `scripts/webhook_*.py` (2) | Scripts exit 0 with `[SILENT]` or JSON |
| SG5 | Skills: webhook-subscriptions + per-route-toolsets + security | `skills/webhook-subscriptions.md`, `skills/per-route-toolsets.md` (2 SKILL.md) | Skill body ≥10 lines |
| SG6 | Config + routes: `config.yaml` snippet + `.env` snippet + `webhook_subscriptions.json` (3 live routes: github-pr, deploy-notify, oom-emergency) | `docs/webhook-routes-config.md`, `.env.webhook-example`, `webhook_subscriptions-example.json` | All 3 routes have secret; none use `INSECURE_NO_AUTH`; `oom-emergency` has `toolsets` |
| SG7 | Implementation prompt + spec update | `.github/prompts/webhook/implementation-prompt.md` + `.hermes/specs/webhook-implementation.md` | References SG1–SG6 |
| SG8 | Final verification checklist + session log append | `docs/webhook-implementation-report.md` | All 8 subgoals verified |

## Rules (per user / multi-file-change-protocol)
- Sequential execution (`only then`): SG1 → SG2 → SG3 → SG4 → SG5 → SG6 → SG7 → SG8.
- Each SG has a verification gate before SG N+1 starts.
- Never invent session IDs; never claim finished until file verified.
- No `INSECURE_NO_AUTH` in any live route file (security invariant from docs).
- Template syntax: `{dot.notation}` + `{__raw__}` + `script_output` handled.

## Milestones
- M1 (SG1–SG2 done): architecture spec + execution plan exist.
- M2 (SG3–SG5 done): prompts, scripts, skills authored.
- M3 (SG6 done): live routes configured; 3 routes present.
- M4 (SG7–SG8 done): implementation prompt + verification report; final gate passes.

## Resources
- Skills active: using-superpowers, multi-file-change-protocol, writing-clearly-and-concisely (SG5), subagent-driven-development (parallel not needed; sequential per user).
- MCP servers used: filesystem (file writes verified), ast-grep (search for existing webhook files), sequential-thinking (plan reasoning in `thinking` tags).
- No external API keys needed; HMAC secrets are example/placeholders (user configures real ones in `.env`).
