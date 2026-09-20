# OpenCode Agent Instructions — SandBox

**Workspace**: `C:\Users\Alexa\Desktop\SandBox`. **Repo**: `rhixecompany/sandbox`. Polyglot monorepo — 17+ subprojects (`projects/*`), each autonomous.

**Init Run**: `init-20260919-212743` — fresh-init enhancement for all 5 agents. See `AGENTS.md` for full artifact pointers and scope.

## Identity

OpenCode agent for the SandBox workspace. Uses the same source of truth as all other agents (`AGENTS.md`). Do not invent a second root prompt or config schema.

## Work Loop

1. **Locate** — identify the nearest applicable `AGENTS.md`, instruction files, package manifest, and tests.
2. **Understand** — inspect existing patterns and confirm the task's exact acceptance criteria.
3. **Plan** — for multi-file or behavioral changes, record the intended files, risks, and validation command before editing.
4. **Implement** — make the smallest complete change; preserve unrelated worktree changes.
5. **Verify** — run the narrowest relevant test, type-check, lint, or build; report blockers plainly.
6. **Document** — update directly related context or docs when behavior or workflow changes.

## Safety Boundaries

- Never read, print, or modify protected secret files such as `.env`, `.pem`, `.key`, or credentials.
- Never claim a tool, model, profile, capability, or verification result that was not observed.
- Never apply root commands to a subproject without checking its local instructions and manifest.
- Prefer existing helpers and project conventions; avoid broad formatting or unrelated cleanup.
- For destructive scripts, run a supported `--dry-run` first and preserve a rollback path.

## Clarification and Artifact Protocol

- For a new request or a changed request, begin with clarification when interaction is available.
- Ask up to three focused questions per turn, covering scope, remaining work, blockers, and approval gates; include required, optional, and recommended choices.
- Before implementation, maintain the current run's spec, plan, and prompt in `ai-agent-home/{specs,plans,prompts}/init-20260919-212743/`.
- Update those artifacts as status changes and mark them complete only after validation.

## DRY References

- Project overrides: `.hermes.md` (workspace root).
- User preferences: `/user-communication-preferences` SKILL.md.
- Multi-file protocol: `/multi-file-change-protocol` SKILL.md.
- Systematic debugging: `/systematic-debugging` SKILL.md.

## Blockers (Real — Never Hidden; refreshed 2026-09-20)

- Profiles: `default` + `adminbot` PRESENT in live `hermes profile list` (2026-09-20). `alexa`/`alexa-alias`/`cto`/`patient-tutor`/`qa`/`skills` dirs remain on disk but NOT registered — preserved honestly.
- Adminbot profile-docs gap (USER.md/MEMORY.md/desc.md absent in its profile dir) — documented, not fabricated.
- MSYS2 FAIL (environment error preserved).
- Rate limit 403 (preserved, not removed).
- `.env` never exposed — contents protected.
- 26 vulnerability findings + 41 parsing errors preserved.
- web-research-628 remaining batches (future; requires new clarification).

## Gate Rules for This Run

User confirms before writing each file individually. Do not claim completion while any current-run artifact or required validation remains unfinished.

## Config

- Config file: `.opencode/opencode.json` (created 2026-09-20 — 467 B; openrouter/deepseek/deepseek-v4-flash-0731; `{env:OPENROUTER_API_KEY}` interpolation; no inline secrets; JSON lint PASS).
- Config uses env/vault references; never inline secrets.
- Provider: openrouter (primary), nous (fallback). See `.hermes/config.yaml` for model details.
