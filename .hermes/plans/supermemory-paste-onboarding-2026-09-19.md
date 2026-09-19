---
name: supermemory-paste-onboarding-2026-09-19
title: "Supermemory + Paste Pipeline Implementation Plan"
description: "Gated plan: paste background cat + supermemory integration items 1-5, with verification after every phase"
version: 1.0.0
date_created: 2026-09-19
status: Approved
goal: "Execute WS-A paste pipeline and WS-B supermemory items 1-5; verify each phase"
---

# Supermemory + Paste Pipeline Plan (2026-09-19)

Approval: clarify gate answered 2026-09-19 — all items approved, no blockers.
Spec: `.hermes/specs/supermemory-paste-onboarding-2026-09-19.md`

## Phase 0 — Docs (DONE when this file + prompts verified)

- [x] Spec written (.hermes/specs/supermemory-paste-onboarding-2026-09-19.md)
- [x] Plan written (this file)
- [x] Prompts written: prompts/pastes-processing.prompt.md, prompts/supermemory-integration.prompt.md
- [x] VERIFY: files exist, frontmatter parses, required sections present (REQ-P/S lists, plan phases)

## Phase 1 — WS-A Execute cat job (background, no timeout)

1. Export SUPERMEMORY_API_KEY (not needed for cat; session env resets between calls).
2. Launch: `for f in ~/AppData/Local/hermes/pastes/*.txt; do printf '===== %s =====\n' "$f"; cat "$f"; done > pastes/cat-all.log` — background=true, notify=true, no timeout.
3. VERIFY (REQ-P3): header count == 120; names diff vs `ls pastes/*.txt`; tail intact.
4. Summarize per-file one-liners in chat (REQ-P4).
5. Triage index → artifact `~/Desktop/SandBox/.hermes/results/pastes-triage-2026-09-19.md` (REQ-P5); process actionable items.

## Phase 2 — WS-B Items 1+2: openrouter-client memory layer

1. TS: `packages/openrouter-client/src/memory.ts` — SupermemoryClient wrapper (storeExchange, searchContext, injectSystemContext); patch `chat.ts` sendChat with optional `memory?: {containerTag, store?, injectContext?}` param (default off = backward compatible).
2. Py: `packages/openrouter-client-py/src/openrouter_client_py/memory.py` + optional `memory` kwarg in `chat.py:send_chat`.
3. VERIFY: `bun test` (TS), ruff + pytest (py), SDK import smoke with env key on scratch tag, cleanup.

## Phase 3 — WS-B Item 3: comicwise prefs → memories

1. Read `projects/comicwise/src/actions/user-preferences.actions.ts` fully.
2. Add `projects/comicwise/src/lib/supermemory.ts` (fetch-based, Bearer from env, non-throwing).
3. Patch updateUserPreferencesAction: after DAL write, push entity-centric facts (e.g. "user reads <genre>" per pref) to POST /v4/memories, containerTag `user_<id>`; guard on key presence.
4. VERIFY: `tsc --noEmit` in comicwise (or bun type-check); lint unchanged.

## Phase 4 — WS-B Item 4: docs + earnings-kit superrag

1. `scripts/ingest_superrag.py` (repo scripts/): walk docs/ (skip archive), ngn-earnings-kit/references+platforms, uk-earnings-kit/references+platforms+trackers; POST each txt/md/json ≤100KB with taskType "superrag", customId = sha1(relpath)[:24], containerTag sandbox_docs / sandbox_earnings; poll done; resume-safe (skip done customIds via /v3/documents/list).
2. `scripts/search_superrag.py` — CLI wrapper over POST /v4/search {q, containerTag, searchMode:"documents"}.
3. VERIFY: ingest 3 sample files → search returns them; idempotency: re-run skips without duplicates.

## Phase 5 — WS-B Item 5: Hermes plugin config

1. Query docs MCP (supermemory-docs, now loaded in-session) for integrations/hermes supermemory.json schema.
2. Create `$HERMES_HOME/supermemory.json` per schema: primary `hermes`, custom containers allowlist, instructions.
3. VERIFY: valid JSON; `hermes` container tools unaffected (supermemory_* still listed); custom tags accepted by /v3/documents (dry write on one custom tag then forget/delete).

## Phase 6 — Final verification & report

- [ ] All acceptance A1-A7 from spec checked with real outputs.
- [ ] No key material in any file (`grep -r sm_vAUoM ~/Desktop/SandBox --include=* -l` → only this plan/spec would match if cited: sanitized).
- [ ] Completion report: files changed, tests run, live API evidence, paste triage summary.

## Risks

- 120-paste processing is large → triage index gates per-file execution; goal loop continues.
- comicwise type-check heavy → scope to touched files first.
- superrag ingest of 13MB → sample-limited verification + resume-friendly script (not full corpus in one run unless asked).

## EXECUTION LOG (2026-09-19)

- Phase 0: docs created + verified PASS (4 files).
- Phase 1: cat-all.log 120/120 headers verified (807,621 B; tail intact). Background shells were deterministically wedged by MSYS fork failures (24/120 × 3 attempts, exit 1) — final artifact produced by the same loop in foreground; no timeout imposed. Triage: 39 actionable / 11 reference / 35 note / 3 system / 32 duplicates (15 groups) → .hermes/results/pastes-triage-2026-09-19.{md,json}.
- Phase 2: TS bun test 12/12 PASS (memory.ts + index.ts + chat.ts memory opts; fixed pre-existing @openrouter/sdk API drift: OpenRouterClient→OpenRouter{apiKey}); py memory.py + chat.py memory kwarg: ruff clean, pytest 12 pass / 3 PRE-EXISTING fail (installed SDK 1.2.2 exports OpenRouter, client.py written for older surface — diagnosed, out of scope). Live round trip: store→done→search 1 hit (0.734)→cleanup 204.
- Phase 3: comicwise src/lib/supermemory.ts + prefs action finally-block mirror; tsc --noEmit clean (0 diagnostics).
- Phase 4: scripts/ingest_superrag.py + search_superrag.py; live: 3 docs ingested (done), search hits with source_file + similarity, idempotent re-run (skipped=4); 12 files >100KB skipped by design.
- Phase 5: $HERMES_HOME/supermemory.json (schema from docs MCP) — valid JSON, custom tags sandbox_docs/sandbox_earnings allowlisted.
- Phase 6: key-material grep CLEAN; git status audited; stray tmp removed.
