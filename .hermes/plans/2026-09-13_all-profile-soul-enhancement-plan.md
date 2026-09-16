# Plan: All-Profile SOUL.md Enhancement + Profile Sync + All MCP Servers Auth/Enable/Test

Created: 2026-09-13 | Profile: default (patient-tutor / adminbot) | Trigger: multi-file-change-protocol (>6 files) + user subgoal
Status: in-progress | Scope: 17 Hermes profiles + root SOUL.md + all ./**/mcp.json MCP servers into Hermes auth/enable/test

## Subgoals
1. Get every Hermes profile → refactor/enhance/verify every profile SOUL.md + description + alias; create if missing; set model = inkling:free by openrouter; check if plan exists and implement.
2. Add all MCP servers in ./**/mcp.json into Hermes, auth, enable, test they all work.

## Verified State (Phase 0 — Live Inventory)
- Profiles: 15 under ~/AppData/Local/hermes/profiles/ + root profile.yaml + skills.
- Root SOUL.md: ~/AppData/Local/hermes/SOUL.md; profile-level SOUL.md present in each.
- ./**/mcp.json files discovered: .hermes/mcp.json, .vscode/mcp.json, .codex/mcp.json, .copilot/mcp.json, .github/mcp.json, .opencode/mcp.json, .hermes/plans/* (none extra).
- Hermes config.yaml already references many MCP servers but needs full parity with .hermes/mcp.json + .vscode/mcp.json + .opencode/mcp.json.
- User model preference verified: `inkling:free` via `openrouter`.

## Phases (Sequential, bounded batches ≤7 files per batch per multi-file-change-protocol)

### Phase 1 — Plan + Scope Lock (COMPLETE)
- [x] Confirmed >6 file trigger.
- [x] Confirmed clarification (all 3 yes) + subgoal (MCP servers).
- [x] Wrote this plan (correct absolute workspace path: C:\Users\Alexa\Desktop\SandBox\.hermes\plans\2026-09-13_all-profile-soul-enhancement-plan.md).
- [ ] Check existing plans for supersession; none supersede.

### Phase 2 — Profile Audit + Description/Alias + Plan Check (Batch: 5 profiles per turn)
For each profile: read profile.yaml, SOUL.md; check for profile-level plan; update description/alias/model header; note missing SOUL descriptions.

### Phase 3 — SOUL.md Structured Enhancement (Batch: 4 profiles per turn)
Apply soul-enhancer structured format; preserve custom rules; verify headers (Profile, Model: inkling:free/openrouter, Identity).

### Phase 4 — MCP Servers Discovery + Auth/Enable/Test (Batch: all ./**/mcp.json merged)
Read all mcp.json files → extract server definitions → compare against hermes config.yaml `mcp_servers` → add missing servers → enable (set enabled:true / add auth tokens if needed via auth.json / config.yaml) → verify with `hermes mcp list` or manual probe.

### Phase 5 — Profile Plan Implementation (if any profile-level plan found)
Inspect any profile-level PLAN.md / .plan files; implement tasks; update status.

### Phase 6 — Verification Gates (All profiles + all MCP servers)
- Profile: each profile.yaml (description + alias) + SOUL.md (structured + model line) verified via grep + read_file.
- MCP: each server from ./**/mcp.json listed in hermes config.yaml, enabled, auth configured, and test response verified (or documented blocker honestly reported).
- Root profile.yaml and ~/AppData/Local/hermes/SOUL.md enhanced consistently.
- Final gate passes → declare "Goal complete" only after verification.

## Cross-References
- Skills: `soul-enhancer`, `hermes-profiles`, `hermes-profile-sync`, `multi-file-change-protocol`, `executing-plans`, `plans-and-specs`, `user-communication-preferences`, `using-superpowers`.
- MCP reference: `.hermes/mcp.json`, `.vscode/mcp.json`, `.opencode/mcp.json`, `.github/mcp.json`, `.codex/mcp.json`, `.copilot/mcp.json`.
