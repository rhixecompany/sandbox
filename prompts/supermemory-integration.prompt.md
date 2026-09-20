---
name: supermemory-integration
title: "Supermemory Integration (items 1-5)"
description: "Executable prompt: integrate official Supermemory SDK into openrouter-client (TS+py), comicwise prefs, docs/earnings-kit superrag ingest, and Hermes plugin supermemory.json"
version: 1.0.0
date_created: 2026-09-19
status: active
---

# Supermemory Integration Prompt

Integrate Supermemory (https://supermemory.ai, docs MCP `supermemory-docs` is authoritative) into the SandBox monorepo. Approved items 1+2, 3, 4, 5 (clarify 2026-09-19). Spec: `.hermes/specs/supermemory-paste-onboarding-2026-09-19.md`.

## NON-NEGOTIABLE RULES

- Auth: `Authorization: Bearer $SUPERMEMORY_API_KEY` only; key never hardcoded or printed; env only.
- Container tag: singular `containerTag`, `^[a-zA-Z0-9_:-]+$`, one tag per user/project, no cross-tag queries. First write creates it.
- Search body param: `q`. Deprecated: /v3/search, plural containerTags, x-api-key headers.
- Ingest is async: poll GET /v3/documents/{id} until status=="done" before searching. Known facts → POST /v4/memories (immediate). Forgets: dryRun first.
- Graceful degradation: no key → feature off + warning, never crash host app.

## ITEM 1+2 — openrouter-client (TS) + openrouter-client-py

- New `memory.ts` / `memory.py`: class SupermemoryMemory { constructor(containerTag, opts) } with:
  - `storeExchange(role, content, metadata?)` → POST /v3/documents taskType "memory", customId = stable hash of (containerTag, role, content).
  - `searchContext(query, limit=5)` → POST /v4/search {q, containerTag, searchMode:"hybrid"}.
  - `injectSystemContext(messages, query)` → prepend retrieved context into system message.
- Patch `sendChat`/`send_chat`: new optional param `memory?: { containerTag: string; store?: boolean; inject?: boolean }` — default OFF (backward compatible). When store → after completion, store user+assistant exchange. When inject → search before completion, add context block to system turn.
- Tests: unit tests with mock responses; type-check + existing suite passes.

## ITEM 3 — comicwise prefs

- `projects/comicwise/src/lib/supermemory.ts`: fetch-based client (POST /v4/memories, POST /v4/search), reads `process.env.SUPERMEMORY_API_KEY`, never throws (logs + returns).
- In `updateUserPreferencesAction` (src/actions/user-preferences.actions.ts) after DAL success: build entity-centric facts ("user <id> prefers <setting>=<value>" for changed keys), send to /v4/memories with containerTag `user_<id>`, isStatic false, metadata {source:"comicwise_prefs"}.
- Optional read: `getUserPreferencesAction` also fetches /v4/profile (non-blocking, merge nothing — informational only).
- Verification: `bun run type-check` or `tsc --noEmit` scoped; ruff unchanged.

## ITEM 4 — docs + earnings-kit superrag

- `scripts/ingest_superrag.py` (Python 3.13, stdlib only): args `--dir --tag [--dry-run] [--limit N]`. For each file (md/txt/json, ≤100KB): POST /v3/documents {content: file text, containerTag: tag, taskType:"superrag", customId: sha1(rel-path)[:24]}. Poll until done. Idempotent: list existing customIds (POST /v3/documents/list) and skip. Tags: `sandbox_docs` (repo docs/), `sandbox_earnings` (both kits).
- `scripts/search_superrag.py`: `--tag --query [--limit]` → /v4/search, print top results (title/path/chunk/similarity).
- Verify: ingest 3 sample files → search hits each; re-run = 0 new docs.

## ITEM 5 — Hermes plugin config

- Confirm schema via supermemory-docs MCP search "integrations hermes supermemory.json" (or llms.txt page).
- Create `$HERMES_HOME/supermemory.json`: {"container_tag":"hermes","enable_custom_container_tags":true,"custom_containers":["sandbox_docs","sandbox_earnings"],"custom_container_instructions":"..."}.
- Verify JSON validity; confirm supermemory_* tools still listed in-session.

## FINAL GATES

- No key material in diffs (`grep -i 'sm_vAUoM' -r <changed paths>` = 0).
- Every changed file passes its linter/type-check; tests green where they exist.
- Live API evidence for at least one write+search+forget cycle on a scratch tag, cleaned up.
