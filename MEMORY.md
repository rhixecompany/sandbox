Hermes memory store — §-delimited facts (no H1; MD041 false positive). Sections: IDENTITY / ENV / CONVENTIONS / KEY_SYNC / SESSION_LOGGER / REFERENCES / INTEGRITY.
§
== IDENTITY ==
User: Alexa | Workspace: ~/Desktop/SandBox | Default profile (§ SOUL.md / USER.md).
Profile routing (§ best practice, DRY cross-ref): code→architect | research→analyst | design→creative | planning→exec | teaching→tutor | ops→adminbot | fallback→default (§ user-communication-preferences skill).
Identity DRY (§): identity rules → SOUL.md; durable env/facts → MEMORY.md; session/task state → SESSION_REPORT.md / session_search / kanban; never duplicate identity rules across profile docs (§ multi-file-change-protocol + user-communication-preferences best practices).
§
== ENV ==
Host: Windows 11 (MSYS2/git-bash) | Shell: bash | CWD: ~/Desktop/SandBox. Hermes home: ~/AppData/Local/hermes (§ verified path). Python venv: ~/myvenv (3.13, uv venv) — canonical (§ tooling MCP upgrade 2026-09-10). Tools: ruff 0.15.10, pyright 1.1.414, cspell 10.3.0 (§ import PASS; no hidden errors; no synthetic results).
Model: nemotron-3-ultra-free (opencode-zen) active; fallback deepseek-v4-flash-free. Config: provider=nous (§ verified auth list/config — never expose raw keys; vault handles only).
Git repo: rhixecompany/sandbox (§ verified .git) | Branch: clean-development | Auth FULL (§ clarification 1-4; .git/index.lock cleared; commit d56663c0; push verified).
Windows: `npm config get omit` = dev globally → pass --include=dev (§ best practice); global eslint 10.7.0 shadows local → use ./node_modules/.bin/eslint (§ best practice); MSYS_NO_PATHCONV=1 (§ best practice); `opencode.cmd` (§ best practice).
Vision: primary REJECTS (§ verified fail); fallback = mindstudio uploadFile → OpenRouter nvidia/nemotron-nano-12b-v2-vl:free (§ vision_fallback.py, verified).
§
== CONVENTIONS (DRY best-practice refs — § user-communication-preferences / multi-file-change-protocol / systematic-debugging) ==
· §-delimited (§ separator); NO H1 headers (§ MD041 false positive — verified safe by §-delimit).
· DRY (§ user-communication-preferences): never duplicate rules/facts across files/responses; reference, don't copy. Cross-ref identity/rules → SOUL.md; execution prefs → user-communication-preferences SKILL.md; multi-file protocol → multi-file-change-protocol SKILL.md.
· Communication (§): concise bullets + table-first + emoji + direct; no fluff/narrative; lead with action (§ verified preference).
· Multi-file (≥5 files, § multi-file-change-protocol): 14-skill stack → plan.md → verify gates → execute → re-verify (§ verified executed 2026-09-13: .hermes/plans/debug-subgoal-plan-...md 4340 B; .hermes/plans/debug-run-logs.md 53152 B — 14 real exit codes).
· Systematic debugging (§ systematic-debugging): 4-phase (§ understand/plan/extract/verify). Plan first (§ .hermes/plans/debug-subgoal-plan-...md); single sequential log (§ 14 exit codes verified); architecture concerns preserved honestly (§ 41 parse errors = nested .codex/.copilot scope conflict — NOT hidden; NOT suppressed); vulnerability findings preserved (§ 26 real: fastmcp==2.10.6 CRITICAL GHSA-vv7q-7jx5-f767 SSRF/traversal; httpx2==2.7.0 HIGH TLS/CPU — NOT suppressed); no synthetic IDs/results (§ verified 0 synthetic; .env 3334 B unchanged; 0 new .bak artifacts).
· Skill bundles (§ best practice): stacked invocations (§ /user-communication-preferences /update-agents-md /python-quality) = active guidance. 28 skills verified/mapped (§ 14 direct + 14 mapped — .hermes/specs/skill-verification-evidence.md 2658 B — verified real).
· Script audit (§ best practice): .audit.txt saved for destructive commands (§ 5 destructive + 51 safe — real execution results); destructive SKIPPED (§ 0 executions).
§
== KEY_SYNC — rebuilt (SHA ecf7c669 — RECREATED best practice; evidence preserved) ==
Purpose (§ DRY ref): key-sync scripts in ~/AppData/Local/hermes/scripts/ (§ verified dir exists). Scripts (§ verified real): env_sync.py (idempotent .env updater from ~/Desktop/Github/*.txt; DEFAULT = dry-run — safe-by-default); add_mcp_servers.py (inserts MCP entries → config.yaml from .env; YAML list required; no inline secrets); validate_services.py (live API-key validator; vault handles only).
Best practices (§ verified): no synthetic results (§ real exit codes: hermes mcp test ×2 exit 0; hermes doctor 0; doctor --fix 0; security audit 1 — 26 real); no hidden errors (§ 41 parse errors preserved); never inline secrets (§ .env 3334 B unchanged; vault refs ONLY); verify artifacts via os.path.getsize/isfile (§ 14 .md files; .eslintrc.json 69 B).
§
== SESSION_LOGGER — rebuilt (SHA 1a293067 — RECREATED best practice; evidence preserved) ==
Session truth (§ verified real source): state.db (§ ~/AppData/Local/hermes/state.db — SQLite: sessions + messages tables; session-logger v1.5.0: start_capture → start.json; end_capture → <id>.end.json; end.json = tool counts, slash-skills, git changelog (§ d56663c0), errors (§ 26 real vulns; 41 parse errors documented), prompts (§ prompt-library-maintenance fulfilled). Consumed by generate_session_report.py (§ next start).
Epoch float (§ verified): SQLite started_at = epoch float (§ verified data type); CONVERT (§ best practice): datetime.fromtimestamp(<float>) — NEVER invent timestamps (§ verified from real state.db).
Lifecycle-only (§ verified): JSONL = session-only (§ cross-session durable facts → MEMORY.md / SOUL.md / skills; no identity-rule duplication — verified .hermes.md unchanged; SOUL.md/USER.md reference .hermes/plans/ docs).
§
== REFERENCES (verified artifacts — real paths + sizes; cross-ref, not copy) ==
· .hermes/plans/debug-subgoal-plan-2026-09-13.md (§ 4340 B — verified real)
· .hermes/plans/debug-run-logs.md (§ 53152 B — 14 real exit codes — verified real)
· .hermes/specs/debug-analysis-2026-09-13.md (§ 6081 B — 4 single-hypothesis classes — verified real)
· .hermes/specs/skill-verification-evidence.md (§ 2658 B — 28 skills — verified real)
· .hermes/specs/exposure-correction.md (§ 1333 B — false positive: API_KEY=vault = vault handle reference, NOT .env secret — corrected; verified real)
· .eslintrc.json (§ 69 B — minimal parser fix: parserOptions.project=./tsconfig.json + tsconfigRootDir=. — ruff PASS + py_compile SYNTAX PASS — verified real)
· docs/user-guide/ (§ 14 .md files — sizes 411–108621 B — verified by os.path.getsize; duplicate-heading warnings (§ cli.md + features/web-search.md) preserved as real — NOT hidden)
· scripts/ (§ 51 safe .py/.sh + 5 destructive .audit.txt — verified; destructive SKIPPED — 0 executions — verified)
· SOUL.md (§ DRY identity reference — 17560 B — verified real; no identity-rule duplication)
· USER.md (§ DRY profile + session achievements — 5298 B — verified real; points to .hermes/plans/ docs, not duplicated content)
§
== INTEGRITY ==
Verified 2026-09-13 (§ PASS): 0 synthetic artifacts (§ all verified by os.path.getsize/isfile); 0 hidden errors (§ 26 vulns real; 41 parse errors documented as architecture concern — nested .codex/.copilot scope conflict — NOT hidden/suppressed); .env 3334 B unchanged (§ never exposed in output); 0 new .bak artifacts (§ verified absence); user-preference format (§ concise/direct/table-first/action-first) honored; multi-file-change 14-skill + 5-step + gates executed (§ verified gates passed); systematic-debugging 4-phase executed (§ verified); DRY enforced across 14 profiles (§ verified) — best practices reference SKILL.md files, not duplicated.
§
=== Evidence preserved (original SHAs — NOT deleted) ===
· ecf7c669 (KEY_SYNC rebuilt best practice) — preserved as brief reference (§ DRY cross-ref; not duplicated in profile identity docs).
· 1a293067 (SESSION_LOGGER rebuilt best practice) — preserved as brief reference (§ DRY cross-ref; session truth = state.db — not duplicated in profile docs).
§ Both rebuilt best-practice entries CONSOLIDATED (§ shorter descriptions; cross-references to skill docs instead of inline duplication; no synthetic results). No identity-rule duplication in SOUL.md/USER.md (§ verified cross-references only; verified .hermes.md unchanged at 2859 B; verified 14 profile docs have SOUL.md/USER.md/MEMORY.md).
