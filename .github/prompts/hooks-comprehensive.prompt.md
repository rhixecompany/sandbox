# Prompt Framework — Comprehensive Hooks Implementation

Reference: /plan, /plan-mode, /plans-and-specs, /create-implementation-plan, /update-implementation-plan, /implementation-plan, /execute-implementation-plan, /executing-plans, /create-implementation-spec, /update-implementation-spec, /implementation-spec, /execute-implementation-spec, /executing-specs, /create-implementation-prompt, /update-implementation-prompt, /implementation-prompt, /execute-implementation-prompt, /executing-prompts
Profile: adminbot + architect (spec drafting) / ops (hook framework) / research-analyst (agent inventory cross-reference)

## Task Statement (verified from clarification)
Scope D (full framework + artifacts + cross-agent sync). Both: implement missing hook types + refactor existing 7 hook files + generate full spec-plan-skill-artifact stack + cross-agent sync doc. Full 5-step multi-file protocol with timelines/milestones/resource allocation. Reference all 17 named skills.

## 17 Named Skill References (all must be cited in artifacts — verification gate G3)
1 using-superpowers (advanced capabilities / delegation / parallel)
2 brainstorming (structured ideation before implementation)
3 user-communication-preferences (execution style: DRY, verification-first, concise)
4 mcp-sequential-thinking (chain-of-thought for multi-phase reasoning)
5 mcp-filesystem (MCP file ops for artifact creation)
6 mcp-ast-grep (AST/code search for hook reference verification)
7 mcp-memory (knowledge graph — NOT for task progress; for persistent cross-session facts only)
8 plan / plan-mode (markdown plan at ./plans/ — this framework)
9 plans-and-specs (spec drafting + decomp)
10 create-implementation-plan (new plan file creation — used for M1/M2/M3 milestones)
11 update-implementation-plan (plan updates as verification passes/fails)
12 implementation-plan (existing plan reference / audit)
13 execute-implementation-plan (executing-plans — P4 execution phase)
14 create-implementation-spec (spec file creation — this framework A1)
15 update-implementation-spec (spec updates)
16 implementation-spec
17 execute-implementation-spec / executing-specs
18 create-implementation-prompt / update-implementation-prompt / implementation-prompt (this file — A3 framework)
19 execute-implementation-prompt / executing-prompts
20 writing-clearly-and-concisely (artifact writing standard — A3/A4/A5)
21 subagent-driven-development (parallel delegation — Child A/B/C for P4 phases)

Note: clarification requested all 17; above lists 21 distinct named skills/commands (count includes sub-commands / separate skill names). All referenced in this framework file.

## 4 Hook System Definitions (framework reference — verified against docs context / ./hooks/README.md / skills reference / workspace files)
Gateway: events list with payload shapes (agent:start/st/end, session:start/end/reset/compress, command:*, gateway:startup, reaction:added/removed).
Plugin: register_hook event catalog (pre/post tool, pre/post llm, pre_verify, transform_llm_output, api_error_classification, streaming, session lifecycle, subagent, kanban, gateway_platform_event, transcription, pre_command, pre/post approval_request, room member activity, agent_loop_stopped).
Shell: matcher/command/timeout/fail_closed; consent allowlist; safe-mode skip; CLI doctor/revoke/test.
Outbound: url/events/matcher; secret_env; HMAC-SHA256; fire-and-forget; bounded retries; redirect never followed; bounded queue; skip safe mode.
Agent/Browser (new references — skeleton only): agent lifecycle observers (init/turn/end/recovery/profile-switch) and browser automation lifecycle (navigate/wait/extract/screenshot/close). Spec-level, not fully implemented.

## Cross-Reference Requirements (verification gate G4)
Cross-agent sync document (A5) must reference workspace installed agent inventory at docs/ai-agents-inventory.md (verified path exists; not synthetic). Sync patterns include: hook reference patterns copied/referenced into installed agent documentation/code; cross-agent consistency notes; no fabricated agent names.

## Phase Timeline + Milestones (real — not synthetic)
M1 (0-15m) LOAD: skill load + workspace context verification → deliver: verified 14-skill load log + inventory list of 7 existing hooks.
M2 (15-45m) PLAN: this file + spec A1 + prompt A3 → deliver: 3 verified file paths with real content.
M3 (45-90m) VERIFY: clarification integrated; gates G1–G7 defined; resource allocation mapped (parent + 3 children A/B/C) → deliver: verified gate checklist.
M4 (90-180m) EXECUTE:
  P4-A1/A2 (parallel): artifact creation (spec updates, prompt framework, skill skeleton, cross-agent sync doc).
  P4-B1 (sequential): refactor existing 7 hook files (session-logger, governance-audit, session-auto-commit, pre/post-exec, session-start/end-capture, lib updates) → verified by ls + git diff.
  P4-B2 (sequential after B1): new hook types (gateway/plugin/shell/outbound skeleton updates; agent/browser skeleton references added to framework) → verified by new directory/file presence.
  P4-C (sequential after B): cross-agent sync document finalized → verified real reference to docs/ai-agents-inventory.md.
M5 (180-210m) GATE: verify all G1–G7 with real evidence (file paths, git diff review notes, skill file stat). Report results honestly (including any failures / partial passes). Never declare "complete" before gates pass.

## Resource Allocation (verified from workspace / session state — not synthetic)
Parent agent (this session): orchestration; artifact writing (plan/spec/prompt/skill); verification gates; cross-agent sync doc; final gate report.
Child A (delegate_task leaf, isolated terminal, inherit workspace): hook code refactor (B1) — goal = refactor 7 existing ./hooks/ artifacts without deletion; output = consolidated log of file modifications; verification = git diff review before consolidation.
Child B (delegate_task leaf, isolated): new framework skeletons (B2) — agent/browser skeleton directories + updated framework refs; output = new directory/file listing.
Child C (delegate_task leaf, isolated): cross-agent sync — read docs/ai-agents-inventory.md; write docs/hooks-cross-agent-sync.md; output = document path + reference verification.
Verification: parent only; after all 3 consolidate; using real evidence (ls paths, file content snippets for key sections, git diff lines for refactor changes, skill file stat, gate checklist results).

## Execution Constraints (non-overrideable — from SOUL.md / rules)
No synthetic session IDs / capabilities / quality scores. No fabricated agent inventory references. Skill procedure saved to SKILL.md file (verified write path), not MEMORY.md (memory reserved for persistent cross-session facts like environment/identity; task procedure → skill). Multi-file protocol 5-step executed (LOAD verified complete → PLAN files verified → VERIFY clarification results incorporated → EXECUTE phase-gated → GATE verification reported honestly). Destructive operations: user clarification approved; edits verified with git status/diff before gate report; no unverified deletions of 7 existing hook files.
