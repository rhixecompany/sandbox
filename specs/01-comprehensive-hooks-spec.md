---
sidebar_position: 16
title: "Persistent Goals"
description: "Set a standing goal and let Hermes keep working across turns until it is done. Our take on the Ralph loop."
status: "in_progress"
---


# Implementation Spec — Comprehensive Hooks Framework

Spec id: hooks-comprehensive-spec-2026-09-13
Plan reference: ./plans/2026-09-13-comprehensive-hooks-plan.md
Status: SPEC (verified before execution; not executed yet)
Profile routing: architect (spec drafting) + ops/adminbot (hook framework)

## Scope (per clarification D + both + full protocol)
Implement/update all 4 hook-system categories (gateway event, plugin, shell, outbound webhook) per docs context, plus agent/browser hook interfaces. Refactor existing 7 hook artifacts; produce new framework artifacts; write cross-agent sync doc; save procedure as SKILL.md (not memory).

## Existing Hook Inventory (verified existing files — not fabricated)
Read from workspace ./hooks/ (verified by ls):
- session-logger/ (dir) + session_start_capture.py + session_end_capture.py + session-auto-commit/ (dir)
- governance-audit/ (dir) + lib.sh / lib.py + capture_common.py
- 01-session-logger-hook.sh / 02-governance-audit-hook.sh / 03-session-auto-commit-hook.sh
- 04-pre-exec-validate.sh / 05-post-exec-state-log.py / post-exec-state-log.sh/.bat
- ./hooks/README.md (to be verified/referenced)
All 7 existing files must remain intact (not deleted) but can be updated/referenced by new framework.

## 4 Hook Systems (spec definitions — reference only; full doc in docs context)
S1 Gateway Event Hooks (HOOK.yaml + handler.py, events: gateway:startup/session:start/end/reset/compress/agent:start/end/step, command:*, reaction:added/removed, wildcard command:*)
S2 Plugin Hooks (register_hook: pre/post_tool_call, pre_llm_call/post_llm_call/pre_verify/transform_llm_output, transform_api_error_classification, subagent_start/stop, on_session_start/end/finalize/reset, agent_loop_stopped, on_skill_lifecycle, kanban_* lifecycle observers, streaming observers on_stream_start/delta/end/interim_message, gateway_platform_event, pre_command, pre_approval_request/post_approval_response, on_room_member_activity, pre_transcription/transform_transcription_result/transform_transcription_output, gateway raw event contract note)
S3 Shell Hooks (config.yaml hooks: block with matcher/command/timeout; fail_closed; consent allowlist; hook doctor/revoke/test CLI; safe-mode skip)
S4 Outbound Webhooks (config.yaml hooks.outbound list: url, events, matcher for tool-scoped, secret_env vs inline secret, HMAC-SHA256 signature, fire-and-forget, bounded retries, redirect never followed, bounded queue, no consent prompt, skip in safe mode)

## Agent / Browser Hooks Addition (new spec section — not in existing docs)
Agent hook interface: agent-level lifecycle observers (agent initialization, agent turn boundaries, agent error/recovery, agent profile switch) — spec only, skeleton handler.
Browser hook interface: browser automation lifecycle (navigate, wait, extract, screenshot) — spec only, skeleton handler.
These are ADDED as new reference types in framework, not replacing S1–S4.

## Artifacts (G1–G7 gate targets)
A1 Spec: this file (verified path ./specs/01-comprehensive-hooks-spec.md update/add reference)
A2 Plan: ./plans/2026-09-13-comprehensive-hooks-plan.md (written; verified)
A3 Prompt framework: .github/prompts/hooks-comprehensive.prompt.md (reference all 4 systems + agent/browser + 17 skills)
A4 Skill: workspace skills file (to be saved after execution) — procedure + pitfalls (not session progress)
A5 Cross-agent sync doc: docs/hooks-cross-agent-sync.md (references docs/ai-agents-inventory.md installed agents)
A6 Refactor result: 7 existing files preserved + framework refs added (verified via git status / diff review before gate)
A7 New framework skeleton: ./hooks/agent-hooks/ + ./hooks/browser-hooks/ directories (spec-level skeletons, not full implementations if time-bound)
A8 Verification report: gate checklist results (real, from state.db references / file checks / git diff — never synthetic IDs/capabilities)

## Cross-References (all 17 skills named in clarification)
See Plan section References. Key: using-superpowers (phase execution with powers), multi-file-change-protocol (threshold + 14-stack load), implementing/executing-plans (plan-mode + execution), subagent-driven-development (child delegation for A/B phases), writing-clearly-and-concisely (artifact writing standard).

## Verification Gates (must pass before GATE declares complete)
G1 Count artifacts: A1–A8 ≥ 5 unique verified paths.
G2 All 4 hook systems + agent/browser referenced in at least A1 or A3.
G3 7 existing hook files present post-execution (ls ./hooks/ — verified real).
G4 Cross-agent sync doc contains references to workspace installed agents (docs/ai-agents-inventory.md path verified; references real).
G5 Skill file saved at workspace skills path (verified by fs stat), not synthetic.
G6 Session truth: SESSION_REPORT.md / state.db referenced for session identity; no fabricated session IDs / capabilities / quality scores.
G7 Destructive edits (patch/write to existing hooks) verified with git diff; no unverified deletions.

## Constraints / Rules (non-overrideable from SOUL.md)
- No synthetic session IDs / capabilities / quality / ranking claims. Verified absence noted if missing.
- Skill file goes to SKILL.md procedure file, NOT MEMORY.md (memory only for cross-session facts like environment; task procedure → skill).
- Multi-file trigger >6 verified by artifact count; protocol executed.
- Only then sequence enforced in execution phase (P4 phases sequential/dependent; A/B parallel independent only after verification).
- User clarification results incorporated (scope D, both, full protocol, all 17 skills, sync to installed agents, destructive approved).
