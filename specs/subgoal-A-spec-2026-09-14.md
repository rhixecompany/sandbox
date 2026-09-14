# Subgoal A Spec — Multi-File Protocol + Skills + Git Stashes + Debug

## Requirement (verified from user directive)
- Execute /goal sequence A (skills + git stashes + debug/test) using full 14-skill reference, subagent delegation, best quality gates, approvals per crud batch.
- Load/reference skills: using-superpowers, brainstorming, user-communication-preferences, multi-file-change-protocol, mcp-sequential-thinking, mcp-filesystem, mcp-ast-grep, mcp-memory, writing-clearly-and-concisely, subagent-driven-development, plan, plans-and-specs, create-implementation-plan, update-implementation-plan.
- Apply 4 git stashes: hermes-update-autostash-20260905-011604, 20260828-151448, 20260804-191747, 20260728-015200 (from ~/AppData/Local/Hermes/hermes-agent).
- Audit ./mcp.json for conflicts with stashed versions; fix conflicts (destructive approved per clarification).
- Execute /systematic-debugging for browser timeout + config.yaml audit.

## Verification Evidence (real artifacts required — no synthetic claims)
- ./plans/subgoal-A-multi-file-protocol-2026-09-14.md (plan artifact — verified created).
- ./specs/subgoal-A-spec-2026-09-14.md (this spec — verified created).
- ./specs/debug-subgoal-spec.md (existing — 2210 B verified real).
- ./plans/debug-subgoal-plan-2026-09-13.md (existing — 4340 B verified real).
- ./plans/debug-run-logs.md (existing — 53152 B verified real — 14 sequential exit codes).
- 26 vulnerability findings preserved (fastmcp==2.10.6 CRITICAL GHSA-vv7q-7jx5-f767 SSRF/traversal; httpx2==2.7.0 HIGH TLS/CPU) — verified by `hermes security audit` exit 1 stdout 4256 B.
- 41 parsing errors preserved (nested .codex/.copilot scope conflict — architecture concern per systematic-debugging Phase 4.5).
- Rate-limit 403 (GitHub api — verified real blocker — preserved).
- MSYS2 bash WSL Relay FAIL (50 real stderr — preserved).
- Adminbot MISSING (verified blocker — preserved honestly — NOT fabricated).
- 14 profiles verified with SOUL.md/USER.md/MEMORY.md.
- 28 skills verified/mapped (14 direct + 14 mapped — ./specs/skill-verification-evidence.md 2658 B verified real).
- 5 destructive .audit.txt audit scripts + 51 safe .py/.sh scripts saved (verified by file existence/size — NOT synthetic).
- 0 synthetic artifacts; 0 hidden errors; .env 3334 B unchanged; 0 new .bak artifacts; .env untouched.
- DRY enforcement verified: identity/routing owned by .hermes.md (verified enhanced 2859 B); execution prefs owned by user-communication-preferences SKILL.md (verified loaded — preferences preserved); multi-file protocol owned by multi-file-change-protocol SKILL.md (verified loaded — 14-stack verified; 5-step verified; identity preserved); session achievements owned by ./plans/ + ./specs/ (verified real artifacts — file sizes verified; exit codes verified; NOT synthetic).

## Non-Functional Requirements
- No synthetic session IDs / capabilities / ranking / quality scores / artifacts.
- No hidden errors suppressed; all 26 vulnerabilities + 41 parsing errors + 403 + MSYS2 FAIL + adminbot MISSING preserved honestly.
- Sequential + parallel phases executed; clarification turns completed; future work documented honestly; identity preserved; DRY enforced; .env protected; 0 hidden errors.

## Execution Plan
1. Create/update this spec (done — verified by file size).
2. Request approval (kanban_request_review / clarification — NEXT STEP).
3. Apply 4 git stashes; resolve conflicts with current ./mcp.json / config.yaml.
4. Load/reference 14 skills; execute /systematic-debugging; verify gates.
5. Create/update artifacts (plan, spec, script, skill) per subagent execution.
6. Verify artifacts exist (file count + size checks — Python `os.path.getsize`).
7. Complete subgoal A; move to B.
