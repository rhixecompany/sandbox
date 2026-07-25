---
name: hermes-platform-debugging
title: "Hermes Platform Debugging"
description: "Debug Hermes platform connectivity and log-noise issues without over-editing installed provider code."
version: 0.1.0
author: Alexa
license: MIT
tags: [hermes, debugging, platforms, telegram, verification]
metadata:
  hermes:
    tags: [imported]
---
# Hermes Platform Debugging

Use when investigating Hermes platform issues from logs/status/diagnostics, especially when a DEBUG log shows tracebacks but the platform appears connected.

## Trigger
- `hermes logs --level DEBUG --since 24h` shows sparse output with one repeating platform traceback.
- `hermes doctor --fix` and `hermes status` otherwise pass.
- Platform state in `gateway_state.json` shows `connected` despite log noise.

## Non-Goal
- Do not use this workflow as a first pass for clearly broken auth, missing tokens, or fatal connect failures that block startup.

## Workflow

### 1. Inspect State Before Patching Code
Read platform state and gateway health first:
- `hermes status`
- `gateway_state.json` platform block
- relevant config/env files only for targeted diagnostic fields

### 2. Probe Reachability
Use live session probes to test whether the failure is current:
- API reachability to the platform host
- bootstrap dependencies if relevant: DNS, DoH, proxy endpoint

### 3. Inspect Code Path as Evidence
Read installed adapter/network files only to understand whether the failure mode is already handled:
- look for best-effort handling
- retry/reconnect behavior
- config/env switches that could explain repeated bootstrap failures

### 4. Decide: Document vs Patch
- If current state is healthy/reconnected, document the diagnostic evidence and stop.
- If the failure is reproducible on demand, minimized, and the exact failure mode changes after the edit, proceed with a minimal code change.

## Hermes-Platform Verification Recipe

### Telegram Example
1. Check `gateway_state.json` for `platforms.telegram.state`.
2. If `connected`, probe `https://api.telegram.org` from the session.
3. If reachable, inspect Telegram adapter bootstrap/webhook cleanup paths only for understanding.
4. Record traceback, state snapshot, and reachability result in a workspace note.
5. Leave installed plugin code untouched unless reproduction + verification prove a code-side fix.

## Pitfalls
- **Symptom patch trap**: A traceback in logs is evidence, not necessarily a code regression. Fixing the wrong layer wastes time and risks new failures.
- **Installed-code edit discipline**: Prefer root-cause documentation/config checks over edits to `~/AppData/Local/hermes/...` plugin files.
- **Transient-event over-correction**: Reconnect/bootstrap failures often recover automatically. Do not paper over them with broad fallback toggles.

## Reference
- `references/hermes-telegram-debug-log-pattern.md`
