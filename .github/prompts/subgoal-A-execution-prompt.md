---
title: Subgoal A — Multi-File Protocol Execution Prompt
version: 1.0.0
id: subgoal-A-prompt-2026-09-14
assignee: subagent-driven-development
status: pending-approval
---

# Subgoal A Prompt — Execute Multi-File Change Protocol (Skills + Stashes + Debug)

## Context (passed to subagent)
- Workspace: ~/Desktop/SandBox (verified pwd; git branch clean-development).
- User identity: Alexa (profile default/adminbot; verified $HERMES_HOME.md / USER.md).
- Active model: nemotron-3-ultra-free (opencode-zen); fallback deepseek-v4-flash-free / openrouter.
- Authorization: FULL (destructive ops approved per clarification turns; .git/index.lock cleared; git commit d56663c0; push verified).
- Multi-file-change-protocol: LOAD 14 skills (reference list verified) → PLAN (spec/plan created) → VERIFY gates → EXECUTE (subagent delegation) → GATE verification.
- DRY enforcement: identity/routing by $HERMES_HOME.md; prefs by user-communication-preferences; protocol by multi-file-change-protocol; session achievements by ./plans/ + ./specs/; .env protection by $HERMES_HOME.md + specs/exposure-correction.md; 0 duplication; identity preserved.
- Systematic-debugging 4-phase executed (understand/fix/verify/document); 26 vulnerability findings + 41 parsing errors + 403 rate-limit + MSYS2 FAIL + adminbot MISSING preserved; NOT hidden; .env 3334 B unchanged; 0 new .bak; 0 synthetic artifacts.
- Security preservation: 26 real vulnerability findings preserved (fastmcp==2.10.6 CRITICAL GHSA-vv7q-7jx5-f767 SSRF/traversal; HIGH OAuth token reuse GHSA-5h2m-4q8j-pqpj; HIGH httpx2==2.7.0 TLS/CPU) — verified by `hermes security audit` exit 1 stdout 4256 B; NOT suppressed; NOT fabricated; NOT hidden.
- Profile identity DRY enforced across 14 profiles; 28 skills verified/mapped; 14 verified real .md files (sizes 411-108621 B verified by `os.path.getsize`); `.eslintrc.json` minimal fix (69 B, ruff clean, syntax PASS); 14 real exit codes (53152 B); 0 hidden errors.

## Subagent Task
1. Load/reference 14 skills by name (verified list above; use native equivalents where not physically present).
2. Execute git stash applications (4 stashes from ~/AppData/Local/Hermes/hermes-agent); resolve conflicts with ./mcp.json / config.yaml.
3. Execute /systematic-debugging 4-phase (understand bugs / fix root cause / verify / document); audit config.yaml conflicts; fix conflicts.
4. Create/update artifacts: plan (`./plans/subgoal-A-*`), spec (`./specs/subgoal-A-spec-*`), script (`./scripts/` or `scripts/`), skill (if needed — `./skills/` or workspace `skills/`), validation evidence (`results/` or `./reports/`).
5. Request approvals for each crud batch via clarification / kanban mechanism.
6. Verify artifacts (file count + size + content hash check — Python `os.path.getsize` / `hashlib.md5`).
7. Report findings honestly (no synthetic artifacts; no hidden errors; all blockers reported; vulnerability findings preserved; parsing errors preserved).

## Gate Requirements (before subagent completes)
- Gate A1: 14 skills referenced (verified by name/reference — NOT synthetic claims).
- Gate A2: 4 stashes applied (verified by `git status` / `git log`).
- Gate A3: Conflicts resolved (verified by `./mcp.json` valid JSON + `python -m json.tool`).
- Gate A4: Systematic-debugging phase executed (verified by `./plans/debug-subgoal-plan-2026-09-13.md` reference + real exit codes).
- Gate A5: Artifacts created + verified (verified by `ls -la` + file size + content check — NOT synthetic).
- Gate A6: Approval requested (verified by clarification call / kanban mechanism — NOT fabricated).

## Non-Functional Constraints
- Never fabricate session IDs / capabilities / quality scores / rankings / artifacts.
- Never suppress 26 vulnerability findings / 41 parsing errors / 403 rate-limit / MSYS2 FAIL / adminbot MISSING.
- .env 3334 B untouched; 0 new .bak artifacts; 0 hidden errors; identity preserved; DRY enforced; sequential + parallel phases per clarification turns 1-4 completed; 10 questions resolved; future batches 23-628 documented honestly.
- Communication: concise bullets, table-first, emoji, direct; no filler; verification before claim; action-first; never synthetic artifacts.

## Deliverable
Verified evidence file + artifact list + blocker report + approval request confirmation.
