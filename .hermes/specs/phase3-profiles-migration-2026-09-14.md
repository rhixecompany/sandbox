---
name: phase3-profiles-migration-2026-09-14
version: 1.0.0
author: Alexa / adminbot
license: MIT
description: "Phase 3 spec: update ALL hermes profile descriptions (honcho/user/card); migrate USER.md/MEMORY.md (+ SOUL.md) to ../../AppData/Local/Hermes/memories/ (merge, delete originals); update AGENTS.md/CLAUDE.md/.cursorrules with DRY + honcho data; enforce multi-file-change-protocol 14-skill + 5-step + systematic-debugging 4-phase."
---

# Phase 3 Spec — Profiles / Memory Migration / Context File Updates

## Goal
Update all hermes profiles (14 verified) with honcho/user/card info; migrate `USER.md`/`MEMORY.md` (+ `SOUL.md` identity) to `~/AppData/Local/Hermes/memories/` (merge, delete originals); enhance `AGENTS.md`, `CLAUDE.md`, `.cursorrules` with DRY references + honcho data; enforce rules; verify integrity.

## Evidence Before Fix (like comparing before/after photos)
- Before: `SOUL.md` (hermes root) = 1871 B (verified pre-edit); `USER.md` (memories) = 1846 B; `MEMORY.md` = 7035 B; `.hermes.md` = 2334 B (verified pre-edit)
- After (session 2026-09-13 verified): `SOUL.md` = 17560 B; `USER.md` = 5636 B; `MEMORY.md` = ~11000 B; `.hermes.md` = 2859 B; all with DRY refs + session achievements + rules 1-6 + `.env` note
- Profile identity DRY: 14 profiles under `~/AppData/Local/hermes/profiles/` verified with `SOUL.md`/`USER.md`/`MEMORY.md`; identity preserved; NOT rewritten to change identity/routing
- Memory migration: source files (`~/Desktop/SandBox/MEMORY.md`, `~/Desktop/SandBox/USER.md`, `~/AppData/Local/hermes/MEMORY.md`, `~/AppData/Local/hermes/USER.md`) → target (`~/AppData/Local/Hermes/memories/`); merge (not overwrite); originals deleted; pointers kept if needed

## Subgoals / Tasks
| # | Task | Method | Gate |
|---|---|---|---|
| 3.1 | Load honcho data (`honcho_profile`, `honcho_context`, `honcho_search`) | Call `honcho_profile` + `honcho_context` + `honcho_search` for user/model/preferences/repo info | All 3 calls return real data; no empty responses |
| 3.2 | Update ALL 14 profile descriptions | Read `.hermes.md` (workspace root) — profile routing verified; read profile `.hermes.md` files; apply DRY reference updates (not duplication) | All profiles enhanced; identity preserved; routing verified |
| 3.3 | Update profile `SOUL.md` / `USER.md` / `MEMORY.md` | Apply `patch` edits; enforce DRY (cross-references); add session achievements (2026-09-13 verified evidence); add rules 1-6; add `.env` note; verify size > original | All 3 files per profile verified real; identity preserved |
| 3.4 | Migrate `USER.md` + `MEMORY.md` (+ `SOUL.md`) to `memories/` | Copy source files; merge contents; write to `~/AppData/Local/Hermes/memories/USER.md`, `MEMORY.md`, `SOUL.md`; delete originals in repo + hermes home | Files exist in target; originals removed; no leftover duplicates |
| 3.5 | Update `AGENTS.md` + `CLAUDE.md` + `.cursorrules` | Read current versions (verified real: `AGENTS.md` 8794 B; `CLAUDE.md` 4711 B; `.cursorrules` 197609 B); apply `patch` for DRY refs + honcho data + rules 1-6 + session achievements + `.env` note; verify with `grep` | All 3 files enhanced; identity preserved; size verified; DRY refs present |
| 3.6 | Enforce multi-file-change-protocol + systematic-debugging rules | Verify all artifacts reference skills (not duplicate rules); verify 5-step protocol referenced; verify 4-phase debugging referenced; verify verification gates present in specs/plans | Rules verified by `grep`; no duplication; identity consistent |

## Subagent / Resource
- Subagent: Subagent-3 (delegated with full context + 14 skills + best quality + identity rules + DRY refs)
- Destructive ops approved (delete originals in repo/hermes home; merge in target) — confirmed explicitly

## Verification Checklist (GATE-E / GATE-F)
- [ ] All 14 profiles verified (`ls ~/AppData/Local/hermes/profiles/`); each has enhanced `SOUL.md`/`USER.md`/`MEMORY.md`
- [ ] Memory migration verified (`ls ~/AppData/Local/Hermes/memories/`); originals deleted; pointers preserved if needed
- [ ] `AGENTS.md`, `CLAUDE.md`, `.cursorrules` enhanced (verified by `head` / `grep` / `ls -la`); DRY refs verified; identity preserved
- [ ] `user-communication-preferences` best practices verified (concise/direct/table-first/action-first/DRY/verification-first); NOT rewritten
- [ ] `multi-file-change-protocol` 14-skill stack + 5-step verified; NOT rewritten; identity preserved
- [ ] `systematic-debugging` 4-phase verified; NOT rewritten; 26 vulnerability findings + 41 parsing errors preserved; NOT hidden
- [ ] Integrity PASS: 0 synthetic artifacts; 0 hidden errors; `.env` 3334 B unchanged; 0 new `.bak`; identity preserved; profile routing preserved (`.hermes.md` verified enhanced; NOT rewritten to change routing)
- [ ] All spec/plan artifacts (`.hermes/specs/phase*-...`, `.hermes/plans/phased-execution-...`) verified real; no phantom IDs; no fabricated results
