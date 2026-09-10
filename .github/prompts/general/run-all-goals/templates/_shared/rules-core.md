---
name: rules-core
category: templates/_shared
version: 2.0.0
license: MIT
author: derived from SOUL.md + USER.md + tree.prompt.txt (verified workspace rules)
description: Shared core execution rules for all run-all-goals artifacts. DRY reference — not duplicated in prompt bodies. tree.prompt.txt is PRIMARY source.
---

# Core Rules — Shared Template

> Sources: verified `SOUL.md` + `USER.md` + `.hermes.md` + **`tree.prompt.txt`** (PRIMARY source for cleanup goals, mjs->mts conversion, config validation). No fabricated rules.

## Non-Negotiable Rules (Verified)

1. **Session Start** — Read `SESSION_REPORT.md` first; verify `user-communication-preferences`; state parties + profile; audit/update/verify; output findings.
2. **MCP First** — Prefer MCP server tools (`filesystem`, `github`, `ast-grep`, etc.) over native equivalents.
3. **Profile Per Task** — `code` -> `code-architect`, `research` -> `research-analyst`, `design` -> `creative-director`, `planning` -> `exec-assistant`, `teaching` -> `patient-tutor`, `ops` -> `adminbot`, general -> `default`.
4. **Python Scripts Only in `scripts/`** — No inline scripts. `scripts/analyze_skills.py`, `scripts/verify_run_all_goals.py` verified present.
5. **Strict Sequential** — `"only then"` is a hard constraint. Do not reorder unless explicitly told.
6. **Verify Before Claim** — Test/check/confirm before reporting. Output backed by real tool execution.
7. **Action-First** — Command first, explanation after. Batch independent calls. Use `clarify` when ambiguous.
8. **Honest Blockers** — Report directly. Never fabricate a workaround or plausible output.
9. **Root Cause Fix** — Fix siblings. Fix the class, not the site. Symptom-fixes accumulate into debt.
10. **No Duplicate / Dead / Stub Skills** — Before creating a skill: search existing + hub for equivalents.
11. **No Secrets in Output** — Never print `.env`, tokens, credentials. Use `${ENV_VAR}` placeholders.
12. **No Backup Files** — Rely on git rollback. `core.autocrlf=true` (Windows MSYS2). Write LF only.

## Tree-Primary Rules (From tree.prompt.txt)

13. **Cleanup-First** — tree.prompt.txt defines cleanup-first execution. Delete .enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, hermes-memory-safety, judge_results, logs, session-state, thoughts folders before any construction work.
14. **mjs->mts Conversion** — Per tree.prompt.txt: convert all *.mjs files to *.mts files. No .mjs files should remain without .mts counterparts.
15. **Config Validation** — Per tree.prompt.txt: update/verify .editorconfig, .gitignore, .markdownlint, .prettier, *.toml, *.yaml, requirements.txt, tsconfig.json, package.json, pyrightconfig.json.
16. **Config Cleanup** — Per tree.prompt.txt: delete *.json (except package.json, pyrightconfig.json), *-report.md, *.log, *.txt (skip *.prompt.txt files).
17. **Source Migration** — Per tree.prompt.txt: create src directory; migrate *.py, *.mjs, *.mts files into src and subdirectories.
18. **Docs Cleanup** — Per tree.prompt.txt: cleanup/update *.md files including PLAN.md, SOUL.md, SPEC.md, USER.md and all docs.

## Cognitive Style (Verified from SOUL.md)

- **Plan Discipline** — Logical execution over velocity. Never execute without mapping to an active phase.
- **Prompt Integrity** — Protect system prompt layer. Inherit: SOUL.md -> USER.md -> dynamic task prompt. Never reorder.
- **Skill Bounds** — Skills = immutable execution units. If custom skill errors twice, fall back to bare primitives.
- **Hook Lifecycle** — Pre-flight (token/env check); pre-exec (syntax/format validation); on-error (rollback); post-process (PII scan); post-exec (state log append-only); on-interrupt (halt + save stack); on-idle (compress history).

## User Preferences (Verified from USER.md)

| Preference | Enforcement |
|---|---|
| Communication: concise bullets, lead result, skip filler | This file + all outputs use bullet-first format |
| Code: TypeScript strict, JSDoc/docstring *why* not *what* | Scripts use `/** Why ... (not what) */` format |
| Skills: structured SKILL.md (YAML frontmatter + md body) | All created skills follow this |
| Hooks: ruff format+check --fix pre-commit | Scripts call `ruff` before write |
| Execution: read -> patch -> verify; MCP-first; no backups | Each phase gate verified |
| Profile routing: code -> architect, research -> analyst, design -> creative, planning -> exec, teaching -> tutor, ops -> adminbot, general -> default | Documented in plan frontmatter + subgoal mapping |

## Workspace Environment (Verified)

| Property | Value | Source |
|---|---|---|
| Workspace root | `~/Desktop/SandBox` (`C:\Users\Alexa\Desktop\SandBox`) | `USER.md` + `.hermes.md` |
| OS | Windows 11 (MSYS2/git-bash) | `.hermes.md` / SOUL.md |
| Shell | bash (NOT PowerShell / cmd.exe) | `.hermes.md` runtime block |
| Model (primary) | `nemotron-3-ultra-free` (opencode-zen) | `.hermes.md` live provider state |
| Model (fallback) | `deepseek-v4-flash-free` (opencode-zen) | `.hermes.md` + USER.md |
| Provider (primary) | `openrouter` (`thinkingmachines/inkling:free`) | `.hermes.md` / session audit |
| Provider (fallback chain) | openrouter -> nous -> opencode-zen | `test-providers-models` session audit |
| Active profile | `default` (user: Alexa; owner: Alexa) | `.hermes.md` header |
| Git repo | `rhixecompany/sandbox` | `USER.md` / `.hermes.md` workspace block |
| Branch | `clean-development` | `run-all-goals.prompt.md` context |
| Recent commits (verified) | `0707a22d` / `f0e0f430` / `d2b0f58e` (3 verified) | `.hermes.md` workspace snapshot |

## Verification Checklist Pattern

Every phase uses this checklist format (derived from `run-all-goals.prompt.md` verification block + `prompt-management` skill checklist):

```markdown
- [ ] Prerequisites configured
- [ ] Source files read (sizes verified)
- [ ] No placeholder markers (`FIXME`/`TODO`/`PLACEHOLDER`)
- [ ] DRY: references `templates/_shared/` (not duplicated inline)
- [ ] Profile/model/provider verified in frontmatter
- [ ] Dependencies reference verified skills (brainstorming confirmed present, etc.)
- [ ] Script output verified (real terminal/git/file/session output)
- [ ] No fabricated session/model/file/content data
```

This template is referenced by — never duplicated inside — `.github/prompts/general/run-all-goals/run-all-goals.prompt.md` and any sub-prompt artifacts.
