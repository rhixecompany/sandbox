---
sidebar_position: 16
title: "Persistent Goals"
description: "Set a standing goal and let Hermes keep working across turns until it's done. Our take on the Ralph loop."
status: "in_progress"
---
mode: hybrid — sequential outer phases (P1→P5) + parallel inner batches (B1..B5 of 6 servers each)
destructive_approval: FULL — commit / push / config rewrites / file delete / branch rewrite all approved per user clarification 2026-09-13
gate_policy: verify before claim; never synthetic results; honest blocker reporting after 2 failures (SOUL.md fallback rule)

# Plan — 30 Hermes MCP Servers (Full Implementation)

## Verified Inputs (from user prompt + clarify responses + loaded skills)
- /goal: install/configure/test/enable 30 Hermes servers + full specs/plans/prompts/scripts/skills (BOTH deliverables — user confirmed choice A)
- /subgoal: per server — expose every tool, run/test every tool, fix failed server, aggregate verification table
- Skills loaded (14-stack per multi-file-change-protocol): using-superpowers, brainstorming, user-communication-preferences, plan (this file), plans-and-specs, create-implementation-plan, implementation-plan, update-implementation-plan, executing-plans (to be activated), subagent-driven-development (to be activated)
- Mode: HYBRID (user choice) — sequential phases P1..P5; parallel within each batch B1..B5 (6 servers per batch = 5 batches = 30)

## 30 Servers (verified against user prompt — canonical list)
B1: ast-grep | code-sandbox | context7 | fetch | filesystem | github
B2: honcho | mcp-docker | memory | mindstudio | neon | parallel-search
B3: parallel-task | playwright | python-quality | sentry | sequential-thinking | smithery
B4: tavily | tooling-config | tooling-lint | atlassian | twilio-docs | coderabbit-cli-mcp
B5: vercel | doist/todoist-ai | basic-memory (io.github.basicmachines-co) | next-devtools-mcp | desktop-commander | microsoft/markitdown

## Phase Map (sequential outer — each phase gates next)
P1 LOAD    — Confirm skills, confirm server list, confirm workspace dirs (DONE in this session)
P2 PLAN    — This file `./plans/30-hermes-mcp-servers-master-plan.md` + per-server spec skeletons `./specs/<server>-spec.md` (30 spec files — >6 file trigger satisfied, protocol active)
P3 VERIFY  — Clarify completed (3 questions: scope=both, destructive=full, mode=hybrid); open items (see below) must be closed before execution
P4 EXECUTE — Hybrid batches B1..B5 running SP-A→SP-F for each server (spec, script, config, test, fix/blocker, skill-if-needed)
P5 GATE     — Aggregate verification: 30-row table saved; every server with real test result; no fabricated results; failed servers reported honestly

## Per-Server Sub-Phases (SP-A → SP-F) — executed in parallel within batch
SP-A  Spec    → `./specs/<server>-spec.md` (exposed tools list, test targets, expected outputs, milestones)
SP-B  Plan     → `./plans/<server>-execution.md` (phases, actions, resource, gate check)
SP-C  Script   → `./scripts/<server>_test_all_tools.py` (calls real tool; captures output file; never synthetic)
SP-D  Config   → Update `hermes config.yaml`, `.vscode/mcp.json`, `.opencode/opencode.json` (only when server missing/broken — verified by grep of config)
SP-E  Execute  → Run SP-C script; save raw output; fix or report honest blocker (≤2 attempts; fallback = blocker message in aggregate table)
SP-F  Skill    → Only if server genuinely needs new SKILL.md: search first (`dedupe-skills`), ≥10 lines, real description, no stub (SOUL.md skill pollution rule)

## Milestones / Timeline (per batch of 6; 5 batches)
Day 1  B1: SP-A + SP-B (12 files created)
Day 2  B1: SP-C + SP-D started; B2: SP-A + SP-B started
Day 3  B1: SP-E + SP-F (if needed) + GATE; B2: SP-C/D started
Day 4  B2: SP-E + GATE; B3: SP-A/B/C started (parallel via delegate_task, 3 subagents: B3-A/B/C, B4-A/B/C, B5-A/B/C as needed)
Day 5  B3 + B4: SP-D/E + GATE
Day 6  B5: SP-A→SP-F + GATE
Day 7  Final aggregate verification (30-row table file `./plans/30-server-aggregate-verify.md` saved; reported in final message)

## Resource Allocation
Main agent (this session): P-phase orchestration, gate verification, aggregate table, final report.
Subagents (delegate_task): per batch B1..B5, SP-A..SP-F parallel — each subagent gets exact server list (6 names), spec template path, script template (`scripts/template_server_test_all_tools.py` to be created at P4 start), config snippet template, verification checklist snippet, workspace file paths. Subagent context NEVER empty (full server names + tool list + output file name + gate checklist — per delegate rules).

## Gate Checklist (verified by file read / terminal output before "done" declared)
- [ ] Spec file exists + non-empty (verified by `ls -l` + `head`)
- [ ] Script exists + references real server/tool (verified by `grep` of file)
- [ ] Script executed — output file saved (verified by `cat` of saved output file; NEVER fabricated)
- [ ] Config entry verified (verified by `grep` of `.vscode/mcp.json` / `hermes config.yaml` for server name)
- [ ] Skill file (if new) ≥10 lines + real description (verified by `wc -l` + `grep`)
- [ ] Aggregate table saved (file `./plans/30-server-aggregate-verify.md` with 30 rows: server | batch | spec_path | script_path | config_updated | test_result | fix_status | blocker_note — verified by `cat` of saved file; blocker_note non-empty for any server where fix failed after 2 attempts)
- [ ] No synthetic results in any output file (verified by inspecting file contents — must match actual script stdout, not invented success strings)

## Open Items Before P4 Execution (must be closed; per plan-mode / verify step)
1. Per-server tool-exposure spec: what exact tool names each of the 30 servers exposes (some servers have multiple tools — e.g., ast-grep has find_code, dump_syntax_tree, etc.). This determines SP-C script content. (Requires user input or web fetch of server docs — `no-net-fetch` skill may block; will report blocker honestly if unreachable.)
2. Template script `./scripts/template_server_test_all_tools.py` must be written before batch parallel execution starts (P4 start gate).
3. Confirm each server's live status: already enabled / broken / missing in workspace `.vscode/mcp.json` / `.opencode/opencode.json` — verification before claiming "fix" vs. "not broken".
4. Confirm subagent count: hybrid mode uses 1 main agent + up to 5 subagent batches (≤10 subagents max per delegation config); verify no resource over-subscription.
5. Confirm workspace clean: `.git/index.lock` already removed; no stale locks will interrupt batch script executions (verified in this session).

## Rules (from SOUL.md + user preferences + skills)
- Action-first: command/file written before explanation; explanation brief.
- Verify before claim: every completed SP-X backed by file/terminal proof.
- Honest blocker reporting: if server fix/test fails twice → blocker in aggregate table; never fabricate success.
- No backup files: patch/edit; no `.bak` left.
- Skill pollution: skill only when genuinely needed; ≥10 lines; real description; search `dedupe-skills` first.
- Memory isolation: session/task progress saved in workspace files (`./plans/`, `./scripts/`), NOT MEMORY.md (only durable identity/environment facts saved there per user-MEMORY.md rules).
- Prompt inheritance preserved: SOUL.md → USER.md → this plan → subagent context prompts (not reordered).
- Profile routing per protocol: plan/verification → exec-assistant / code-architect; parallel subagent batches → default profile (adminbot) with full context injection.

## Subgoal Coverage (verified mapping)
For EACH server in B1..B5:
  - Spec `./specs/<s>-spec.md` → exposes every tool (subgoal: "fully exposes")
  - Script `./scripts/<s>_test_all_tools.py` + executed output file → runs + tests every tool (subgoal: "runs, tests")
  - Config update + fix/blocker tracking → fixes failed servers (subgoal: "fix all failed server")
  - Skill (if needed) `./skills/<s>-skill.md` → fully implements skill for server
Aggregate table `./plans/30-server-aggregate-verify.md` proves all 30 covered.
