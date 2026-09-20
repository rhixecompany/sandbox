---
name: supermemory-paste-onboarding-2026-09-19
title: "Supermemory + Paste Pipeline Onboarding"
description: "Process ~/AppData/Local/hermes/pastes/*.txt in background with verification, and integrate Supermemory (items 1-5 approved) into the SandBox monorepo"
version: 1.0.0
date_created: 2026-09-19
status: In progress
goal: "Pastes: background cat → log → verify → summarize → triage. Supermemory: implement approved items 1-5 into openrouter-client, comicwise, docs/earnings-kit, and Hermes plugin config"
---

# Supermemory + Paste Pipeline Onboarding Spec

## Goal

Two workstreams, both user-approved via clarify 2026-09-19 (no blockers):

- WS-A (Pastes): run `cat ~/AppData/Local/hermes/pastes/*.txt` as a background one-shot with NO timeout, log to `~/AppData/Local/hermes/pastes/cat-all.log`, verify every file landed, summarize contents, and treat each paste as an instruction/request to process.
- WS-B (Supermemory): implement approved items 1+2 (openrouter-client TS/Python memory wrapper + search-then-answer), 3 (comicwise prefs → profile/memories), 4 (docs/ + earnings-kit superrag ingest), 5 ($HERMES_HOME/supermemory.json).

## Requirements

### WS-A — Paste pipeline

- REQ-P1: Command runs `cat` over `~/AppData/Local/hermes/pastes/*.txt` (120 files, verified count) as a background process, no timeout, completion notification on.
- REQ-P2: Log file: `~/AppData/Local/hermes/pastes/cat-all.log`. Each file delimited by `===== <name> =====` header for machine-verifiable diff.
- REQ-P3: Verification: log contains exactly 120 unique file headers; header set matches `ls pastes/*.txt` names 1:1; no truncated tail (compare last bytes).
- REQ-P4: Summarize contents back to the user in chat (per-file one-liner classification).
- REQ-P5: Treat each paste as an instruction/request: triage into actionable / reference / duplicate / system, produce a triage index artifact, and process actionable items.

### WS-B — Supermemory integration

- REQ-S1: Use official SDK (`supermemory` npm / PyPI); client reads `SUPERMEMORY_API_KEY` from env only. Never print or hardcode the key.
- REQ-S2: Container tags: singular `containerTag`, format `^[a-zA-Z0-9_:-]+$`, one tag per user or project, no cross-tag queries. First write creates the tag.
- REQ-S3 (item 1): openrouter-client (TS) + openrouter-client-py: add memory wrapper so each exchange is stored (POST /v3/documents, taskType "memory", customId per exchange) and searched (POST /v4/search) before the model answers. Backward-compatible: existing sendChat/send_chat signatures unchanged unless memory options passed.
- REQ-S4 (item 2): search-then-answer in sendChat: retrieved context from /v4/search injected into the system message instead of replaying full history (opt-in flag).
- REQ-S5 (item 3): comicwise: mirror user preferences to Supermemory (containerTag `user_<id>`); writes via POST /v4/memories (entity-centric facts, immediately searchable — feeds /v4/profile); wire into `updateUserPreferencesAction`; graceful no-op when key absent. Read profile at session start (optional, non-blocking).
- REQ-S6 (item 4): ingest script for docs/ (13MB) + ngn/uk-earnings-kit reference dirs: POST /v3/documents, taskType "superrag", stable containerTags (`sandbox_docs`, `sandbox_earnings`); search helper using /v4/search + searchMode "documents". Idempotent via stable `customId` (relative path hash).
- REQ-S7 (item 5): `$HERMES_HOME/supermemory.json`: primary container_tag stays `hermes`; enable_custom_container_tags: true; custom_containers: [sandbox_docs, sandbox_earnings, user_comicwise_demo]; custom_container_instructions explaining when each is used.
- REQ-S8: Async ingestion: poll GET /v3/documents/{id} until status == "done" before searching. For known facts use POST /v4/memories (immediately searchable).
- REQ-S9: Search body param is `q` (not `query`); /v3/search deprecated — never use. Auth: `Authorization: Bearer` only.
- REQ-S10: Graceful degradation everywhere: missing env key → feature disabled, log a warning, never crash the host app.
- REQ-S11: Verification per item: type-check / tests pass where they exist (bun test for openrouter-client, ruff for py, tsc for comicwise) + live API round-trip on scratch tag + cleanup (forget-matching dryRun first).
- REQ-S12: No secrets in code, docs, or artifacts. Key referenced as `$SUPERMEMORY_API_KEY` only.

## Out of scope

- Ingesting the 120 pastes into Supermemory (evaluation after triage; separate task).
- Banking/other project integrations (not approved).
- Changes to `.env` (protected, 3334 B, rule 6).

## Acceptance

- A1: cat-all.log exists, 120 file headers, matches source names.
- A2: Triage index artifact produced; summary delivered in chat.
- A3: openrouter-client TS+py build/test pass with memory wrapper optional.
- A4: comicwise type-check passes; prefs action writes memories when key present.
- A5: Ingest script runs idempotently; document search returns hits for docs corpus.
- A6: supermemory.json valid JSON, tags allowlisted, Hermes plugin tools unaffected.
- A7: No key material in any file or output.
