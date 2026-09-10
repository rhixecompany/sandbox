---
name: rules-core
category: templates/_shared
version: 1.0.0
license: MIT
author: derived from SOUL.md + USER.md (verified workspace rules)
description: Shared core execution rules for all run-all-goals artifacts. DRY reference — not duplicated in prompt bodies.
---

# Core Rules — Shared Template

> Source: verified `SOUL.md` (identity/cognitive-style/architectural-invariants) + `USER.md` (Alexa profile / SandBox workspace) + `.hermes.md` (project overrides). No fabricated rules.

## Non-Negotiable Rules (Verified)

1. **Session Start** — Read `SESSION_REPORT.md` first; verify `user-communication-preferences`; state parties + profile; audit/update/verify; output findings.
2. **MCP First** — Prefer MCP server tools (`filesystem`, `github`, `ast-grep`, etc.) over native equivalents (`read_file` equivalent preferred via MCP).
3. **Profile Per Task** — `code` â `code-architect`, `research` â `research-analyst`, `design` â `creative-director`, `planning` â `exec-assistant`, `teaching` â `patient-tutor`, `ops` â `adminbot`, general â `default`. (Verified in `.hermes.md` profile table + SOUL.md Section 3.)
4. **Python Scripts Only in `scripts/`** — No inline scripts. `scripts/analyze_skills.py`, `verify_run_all_goals.py` verified present.
5. **Strict Sequential** — `"only then"` is a hard constraint. Do not reorder unless explicitly told. (User confirmation recorded in `.hermes/plans/run-all-goals-implementation.md` authorization block.)
6. **Verify Before Claim** — Test/check/confirm before reporting. Output backed by real tool execution (git status, file sizes, AST checks, session IDs). (SOUL.md Rule 6.)
7. **Action-First** — Command first, explanation after. Batch independent calls. Use `clarify` when ambiguous. (SOUL.md Section "Action-First")
8. **Honest Blockers** — Report directly. Never fabricate a workaround or plausible output. (SOUL.md Section 8.)
9. **Root Cause Fix** — Fix siblings. Fix the class, not the site. Symptom-fixes accumulate into debt. (SOUL.md Section 9.)
10. **No Duplicate / Dead / Stub Skills** — Before creating a skill: search existing + hub for equivalents. A skill must have â¥10 line body + real description. (SOUL.md Section 13 / skill safety rule.)
11. **No Secrets in Output** — Never print `.env`, tokens, credentials. Use `${ENV_VAR}` placeholders. (SOUL.md Section 12 / Security block in prompt.)
12. **No Backup Files** — Rely on git rollback. `core.autocrlf=true` (Windows MSYS2). Write LF only. (USER.md execution preference + `.hermes.md` Windows env notes.)

## Cognitive Style (Verified from SOUL.md)

- **Plan Discipline** — Logical execution over velocity. Never execute without mapping to an active phase.
- **Prompt Integrity** — Protect system prompt layer. Inherit: SOUL.md â USER.md â dynamic task prompt. Never reorder.
- **Skill Bounds** — Skills = immutable execution units. If custom skill errors twice, fall back to bare primitives.
- **Hook Lifecycle** — Pre-flight (token/env check); pre-exec (syntax/format validation); on-error (rollback); post-process (PII scan); post-exec (state log append-only); on-interrupt (halt + save stack); on-idle (compress history).

## User Preferences (Verified from USER.md)

| Preference | Enforcement |
|---|---|
| Communication: concise bullets, lead result, skip filler | This file + all outputs use bullet-first format |
| Code: TypeScript strict, JSDoc/docstring *why* not *what* | Scripts use `/** Why ... (not what) */` format |
| Skills: structured SKILL.md (YAML frontmatter + md body) | All created skills follow this |
| Hooks: ruff format+check --fix pre-commit | Scripts call `ruff` before write |
| Execution: read â patch â verify; MCP-first; no backups | Each phase gate verified |
| Profile routing: code â architect, research â analyst, design â creative, planning â exec, teaching â tutor, ops â adminbot, general â default | Documented in plan frontmatter + subgoal mapping |

## Workspace Environment (Verified)

| Property | Value | Source |
|---|---|---|
| Workspace root | `~/Desktop/SandBox` (`C:\Users\Alexa\Desktop\SandBox`) | `USER.md` + `.hermes.md` |
| OS | Windows 11 (MSYS2/git-bash) | `.hermes.md` / SOUL.md |
| Shell | bash (NOT PowerShell / cmd.exe) | `.hermes.md` runtime block |
| Model (primary) | `nemotron-3-ultra-free` (opencode-zen) | `.hermes.md` live provider state |
| Model (fallback) | `deepseek-v4-flash-free` (opencode-zen) | `.hermes.md` + USER.md |
| Provider (primary) | `openrouter` (`thinkingmachines/inkling:free`) | `.hermes.md` / session audit |
| Provider (fallback chain) | openrouter â nous â opencode-zen (verified 3 providers, 4 free models) | `test-providers-models` session audit |
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

This template is referenced by â never duplicated inside â `.github/prompts/general/run-all-goals/run-all-goals.prompt.md` and any sub-prompt artifacts.
