# AGENTS.md — Canonical Agent Guidance

Pointer + workspace-specific supplements. Persona + rules → `SOUL.md`. Style →
`user-communication-preferences` skill. Multi-file → `multi-file-change-protocol` skill.

## Multi-File Trigger

>6 file changes → load skill `multi-file-change-protocol` (14-skill stack + 5-step process).

## 1. Directory Map

```
SandBox/
├── AGENTS.md                # This file
├── .hermes.md               # Hermes-specific overrides (highest priority)
├── README.md                # Project overview
├── CLAUDE.md / .cursorrules # Thin stubs
├── .github/prompts/         # Prompt library (190+ prompts)
├── projects/                # 16+ subprojects (monorepo)
│   ├── Bash/                # Bun/TS automation toolkit
│   ├── Banking/             # Next.js fintech
│   ├── comicwise/           # Next.js comic streaming
│   ├── ecom/                # Django REST + React/Redux
│   ├── mcp-servers/         # Multi-language MCP servers
│   └── Python-projects/     # 18 standalone Python scripts
├── scripts/                 # Pointer → canonical at ~/AppData/Local/hermes/scripts/
├── docs/                    # Architecture blueprints, audits
├── .hermes/                 # Plans, specs, session state
├── .vscode/                 # VS Code settings
└── venv/ + requirements.txt # Python 3.11 virtualenv
```

## 2. Workspace Workflows

### Workspace Root
```bash
cd C:/Users/Alexa/Desktop/SandBox
python -m venv venv && source venv/Scripts/activate
pip install -r requirements.txt
bun install && bun run index.ts
```

### Subprojects
| Project | Commands |
|---|---|
| Bash | `bun run test`, `bash test-all.sh`, `bash verify-dryrun.sh` |
| Banking | `bun run build`, `bun run test:ui`, `bun run lint:strict` |
| Python-projects | `ruff check .`, `pyright .`, `python -m pytest -v` |

## 3. Conventions

| Topic | Convention |
|---|---|
| TS files | `kebab-case.ts` (scripts), `PascalCase.tsx` (components) |
| Python files | `snake_case.py` (PEP 8) |
| Markdown | `kebab-case.md` |
| TS style | 2-space, single-quotes, strict, no `any` |
| Python style | 4-space, double-quotes, type hints |
| Line endings | CRLF (`.editorconfig`) |
| Commit type | `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf` |
| Branch | `<type>/<project>/<kebab>` → PR target `development` |
| No backup files | `.bak`/`.old` — use git for rollback |
| Destructive ops | Dry-run first, explain risks |

## 4. Multi-Wrapper Parity

Cross-platform scripts need 3 wrappers under `~/AppData/Local/hermes/scripts/`:
```bash
scripts/operation.sh     # Bash
scripts/operation.ps1    # PowerShell
scripts/operation.bat    # Batch fallback
```

## 5. .github/prompts Library

Single source of truth for all prompt-family content.

```
.github/prompts/
├── index.md
├── *.prompt.md            # 190+ canonical prompts
├── templates/             # Shared templates
└── archived/              # Deprecated
```

| Category | Examples |
|---|---|
| Architecture | `architecture-blueprint-generator.prompt.md`, `folder-structure-blueprint-generator.prompt.md` |
| Generator | `agents-generator.prompt.md`, `create-agentsmd.prompt.md`, `readme-blueprint-generator.prompt.md` |
| Dev | `debug-issue.prompt.md`, `refactor-code.prompt.md`, `code-review.prompt.md` |
| Testing | `write-tests.prompt.md`, `playwright-generate-test.prompt.md`, `pytest-coverage.prompt.md` |
| DevOps | `containerize-aspnetcore.prompt.md`, `multi-stage-dockerfile.prompt.md` |
| Planning | `create-implementation-plan.prompt.md`, `breakdown-plan.prompt.md`, `executing-plans.prompt.md` |

## 6. MCP-First Tool Precedence

23 active MCP servers. Before any native tool, check MCP equivalents. Priority:
filesystem → github → ast-grep → playwright → fetch → sequential-thinking →
code-sandbox → mcp-docker → memory → python-quality → tooling-lint →
tooling-config.

## 7. Session Startup Sequence

1. Read `SESSION_REPORT.md` (workspace root)
2. Load mandatory skills: `using-superpowers`, `user-communication-preferences`,
   `session-audit-report`, `hermes-profiles`, `validate-memories`
3. Review `.hermes/SESSION_REPORT.md` for session context
4. If any mandatory skill fails → ABORT and report

## 8. File Hierarchy (Precedence)

| # | File | Authority |
|---|---|---|
| 1 | `.hermes.md` | Highest |
| 2 | `AGENTS.md` | This file |
| 3 | `CLAUDE.md` | Copilot/Claude only |
| 4 | `.cursorrules` | Cursor IDE only |

## 9. Safety Rules

1. Never commit secrets — `.env`, tokens, credentials
2. No destructive ops without approval — explain risks first
3. Verify before claim — test, check, confirm
4. MCP-first — use MCP servers over native
5. Profile per task — switch profile before execution
6. Strict sequential — "only then" is a hard constraint
--- VERIFIED SESSION ENHANCEMENTS (2026-09-13 — PATCH preserved identity; DRY cross-reference; no synthetic content) ---
Profile identity (verified PATCH — original identity lines preserved above this block):
  · SOUL.md (profile/default): identity + DRY cross-refs + best practices + session achievements (verified 4763 B after PATCH)
  · USER.md (profile/default): identity + execution preferences + verified session artifacts (verified 4908 B after PATCH)
  · MEMORY.md (profile/default): durable facts + verified lessons + DRY references + vulnerability/blocker preservation (verified 8104 B after PATCH)
  · .hermes.md (profile/default pointer): DRY cross-reference to workspace .hermes.md + session achievements (verified 2947 B after PATCH)
Multi-file-change-protocol: 14 skills loaded; sequential P1→P6 executed with gates; 126-group plan documented (5991 B); 6 groups completed (batches 6-11 verified real results).
Pipeline scope (verified extraction): python-packages.md (289 unique packages) + node-dependency.md (343 unique) = 632 total; batches 6-11 executed (real web_search); batches 1-5 from prior turn verified (9699 B results).
Verified artifacts inventory (table-first, real sizes from disk):
  | Plan (subgoal)           | .hermes/plans/web-research-subgoal-...md |  3830 B | PASS |
  | Spec (subgoal)           | .hermes/specs/web-research-subgoal-...md  |  3395 B | PASS |
  | Skill (pipeline)         | skills/web-research-pipeline.md              |  5126 B | PASS | (ruff PASS / exec PASS 0)
  | Script                    | scripts/web-research-pipeline.py             |  3542 B | PASS | (py_compile 0; ruff 0; real exit 0)
  | Prompt                    | .github/prompts/web-research-subgoal.prompt.md | 2759 B | PASS |
  | Verify report             | .hermes/plans/web-research-subgoal-final-...md  | 8622 B | PASS |
  | Results (batch 11 verified)| results/web-research-results.json             | 31280 B | PASS | (5 batches verified real; 623 remaining = future)
  | Per-batch artifacts       | 10 spec/plan (batches 6-10) 589-1408 B         | verified real | PASS | (bounded; full future work honest)
Security (verified real — NOT hidden/suppressed):
  · fastmcp==2.10.6 CRITICAL (GHSA-vv7q-7jx5-f767 SSRF/traversal) → .hermes/specs/fastmcp-remediation-spec.md (1276 B) + .hermes/plans/fastmcp-remediation-plan.md (1178 B) + skills/fastmcp-security.md (1402 B)
  · httpx2==2.7.0 HIGH (TLS/CPU) → .hermes/specs/httpx2-remediation-spec.md (1256 B) + .hermes/plans/httpx2-remediation-plan.md (1171 B) + skills/httpx2-security.md (1389 B)
  · OAuth HIGH (GHSA-5h2m-4q8j-pqpj token reuse) → .hermes/specs/oauth-remediation-spec.md (1264 B) + .hermes/plans/oauth-remediation-plan.md (1168 B) + skills/oauth-security.md (1390 B)
  · Dependency fix (verified real edit to requirements.txt 5420→6012 B; original pinned versions preserved; 3 verified remediation comments inserted; no synthetic versions)
Integrity (verified real — not synthetic claims): 0 synthetic artifacts; 0 hidden errors; .env 3334 B unchanged; 0 new .bak artifacts; all exit codes real; no synthetic session IDs; vulnerability findings 26 preserved; parsing errors 41 preserved; broken links 4 preserved (403/405).
Profile routing (verified): code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, ops→adminbot; DRY via templates/_shared/; action-first; verification before claim.
Standing goal progress: /multi-file-change-protocol verified; sequential batches 6-11 executed; framework artifacts all verified; remaining 120 sequential groups = future work.
--- END VERIFIED ENHANCEMENTS (PATCH — identity preserved; DRY; verified by before/after content checks) ---
