---
name: using-superpowers
title: "Using Superpowers"
description: "Use when starting any conversation. Establishes how to find and use skills, requiring Skill tool invocation before any response."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [skills, workflow, onboarding, meta]
metadata:
  hermes:
    tags: [imported]
---
## Description

Establish how to find and use skills, requiring Skill tool invocation before ANY response including clarifying questions. Foundational skill for accessing all other skills.

## When to Use

- Starting any conversation
- Before any response or action
- When unsure which skill applies
- Establishing skill workflow
- Learning about available skills

## When NOT to Use

- Already in active skill workflow
- Non-skill related work
- Real-time execution without planning

## Workflow

### Phase 1: Identify Task & Session Context

- Understand user request
- Determine task type
- Note any constraints
- **[NEW] Check session continuity:**
  - Search workspace for `SESSION_REPORT.md` and read it (establishes prior work context)
  - Verify global `~/.hermes/USER.md` and `~/.hermes/SOUL.md` exist and are current
  - If model or profile differs from report, update self-identification (e.g., "Active model: <model> (<provider>)")
  - Capture session start state for later reporting (session ID, timestamp, profile, model)
- **Select correct profile for task** — Run `hermes profile use <name>` before execution per routing table:
  | Task Type | Profile |
  |-----------|---------|
  | Code implementation, debugging, refactoring | `code-architect` |
  | Deep research, literature review, synthesis | `research-analyst` |
  | Design, content creation, brainstorming | `creative-director` |
  | Planning, coordination, admin | `exec-assistant` |
  | Tutorials, explanations, teaching | `patient-tutor` |
  | System operations, DevOps, infra | `adminbot` |
  | General purpose | `default` |
- Plan approach

### Phase 2: Check Available Skills

- Review available skills
- Identify relevant skills
- Note skill descriptions
- Plan skill invocation
- **Tool precedence: MCP servers first** — Before using native tools (terminal, read_file, search_files, etc.), check if an MCP server provides equivalent functionality (filesystem, github, ast-grep, memory, playwright, sequential-thinking, cli, code-sandbox, fetch, mcp-docker). MCP tools are more token-efficient and should be preferred.

### Phase 3: Invoke Skills

- Load relevant skills
- Review skill content
- Understand workflow
- Plan execution

### Phase 4: Execute & Respond

- Follow skill workflow
- Execute task
- Provide response
- Document decisions

## Tools & References

## Pitfalls
- If any of the mandatory startup skills (`/using-superpowers`, `/user-communication-preferences`, `/session-audit-report`, `/hermes-profiles`, `/validate-memories`) fail to load or execute, abort further actions and surface an error to the user.
- Do not proceed with task execution until the mandatory skills are confirmed loaded.


- **Related Skills**: All other skills
- **Skill Tool**: Load and access skills
- **Skill List**: Available skills in system
- **Documentation**: Skill descriptions and workflows
- **Library hygiene reference**: `references/skill-library-hygiene.md`

## Skill Library Hygiene

- Prefer patching an existing umbrella skill before creating a new one.
- Add durable detail to `references/`, `templates/`, or `scripts/` instead of bloating `SKILL.md`.
- Create new skills only at the class level; avoid one-off task artifacts and session-specific names.
- When a session reveals a reusable fix, workflow, or user preference, capture it immediately as a pitfall, step, or reference file so future sessions start ahead.
- When auditing markdown prompt libraries, use code-aware scans: ignore fenced code blocks for TODO/FIXME and heading-depth checks, and confirm exact duplicate file contents before deleting duplicates.
- If the user explicitly asks to review the conversation and update the library, treat it as a maintenance pass: leave the library better than you found it, and prefer the smallest reusable improvement over a no-op.
- If two skills overlap, note the overlap in the reply and let the curator consolidate later.

## Best Practices

- Check for skills before responding
- Invoke relevant skills early
- Follow skill workflows exactly
- Document skill usage
- Learn from skill patterns
- Share skill knowledge
- Maintain skill library
- Keep skills class-level; use references for session-specific detail
- When a plan hits a blocked state because key inputs or paths are missing, stop and report the blocker before continuing — do not resume the plan from the next phase by invention.
- After any tool call sequence, process and summarize the actual results before composing the assistant message; do not return an empty response while leaving tool results unhandled.

## Skills Required

| Skill | Purpose |
|-------|---------|
| `skill-creator` | Create and validate new skills |
| `writing-skills` | Write clear skill prose and structure |

## Verification Checklist

- [ ] Task type identified before responding
- [ ] Relevant skills reviewed and loaded
- [ ] Skill workflow followed exactly
- [ ] Results documented and decisions captured
- [ ] Skill library hygiene maintained

## Pitfalls

- Responding without checking skills first leads to inconsistent behavior
- Not loading a skill before acting misses critical workflow steps
- Creating one-off skills instead of reusable classes bloats the library
- Leaving tool results unhandled causes silent failures
- Skipping tool-result synthesis after tool calls leaves work unfinished and frustrates the user. Always read the tool output, then continue with the next concrete step.

## Session-derived updates (practice->skill)

When a conversation reveals reusable patterns, fixes, or user preferences, capture them here so future sessions start ahead. This skill enforces the following lessons observed and validated in recent sessions:

- Respect and encode the user's style preferences: prefer concise responses, avoid unnecessary formatting or verbosity, and follow explicit "read-before-edit" and "backup-before-destructive" rules. When the user corrects tone/verbosity, patch the governing skill rather than relying on memory alone.
- Ensure SOUL.md (agent persona) is authoritative and durable: when a session creates or updates SOUL.md, the agent should ensure hooks (session-logger, session-auto-commit) either call or regenerate SESSION_REPORT.md so the agent's session history is always available for context.
- Standard report fields: session ID, timestamp, profile, model, work completed, tools/skills used, current state, result. Prefer a compact human-readable markdown summary with an optional machine-readable JSON companion if needed.
- Hooks and automation: prefer small, auditable shell hooks that write compact JSON logs to %LOCALAPPDATA%/hermes/logs/hermes and call a verified report-generator script on session_end. Include verification steps: simulate session_start and session_end events and confirm report regeneration.
- Pitfalls to record: permissions under %LOCALAPPDATA% and Desktop paths, profile-specific HERMES_HOME variations, and environments where Python is unavailable in hooks (provide a shell-only alternative in references).
- **Multi-group skill consolidation pattern**: when consolidating many skills into umbrellas, use the audit→plan→execute→verify pattern from `plans-and-specs`. Key: create a timestamped backup BEFORE any mutations; use `skill_manage(action='delete', absorbed_into=...)` for archiving (knowing it archives, not removes); use `rm -rf` for true deletion of thin stubs; verify with `read_file` not `skill_view()` (stale cache). Record all absorbed skills in the umbrella's SKILL.md "Recently Absorbed Skills" section.
- **skill_manage tool limitations**: delete archives rather than removing; can't resolve `software-development/` path variants by bare name; `absorbed_into` must reference an existing skill by bare name only (no paths). Always verify on disk after operations.
- **Strict sequential workflow**: when the user chains commands with "only then", treat it as a first-class workflow constraint — never skip ahead, never reorder. Each phase must fully complete (including verification) before the next begins. This applies to skill maintenance pipelines, package installs, repo clones, and any multi-phase task.

- **Stale SESSION_REPORT.md**: when `SESSION_REPORT.md` exists but contains only stubs/headers (no actionable continuity), treat prior context as absent. Update it to a real rolling summary with at minimum: session id/timestamp, profile, model, work completed, and current state. Do not invent prior work that isn’t in the report.

- **Plan consolidation before execution**: when `.hermes/plans/` contains multiple overlapping fragments covering the same system (skills, hooks, plugins, MCP, docs), the safe move is one consolidated master plan, not executing the most recent fragment in isolation. Consolidate status, scope, blockers, and open work from all related plans into one file before running anything costly or destructive. Preserve original plan paths as sources; do not delete them retroactively.
- **Skill audit pattern**: when asked to audit/enhance/verify a concrete skill, always: (1) load the skill with `skill_view`, (2) read all linked `references/` files, (3) count lines/chars/reference-files, (4) evaluate frontmatter/structure/content/DRY/references, (5) produce a scored report, (6) apply fixes in priority order (High→Medium→Low), (7) re-verify. Don't just describe issues — fix them inline when authorized.
- **Scope discipline when tools are constrained**: during review/memory phases, only `memory` and `skill_manage` tools are available. Don't try to call `terminal`, `read_file`, `execute_code`, or other tools — they'll be denied. Work within the allowed toolset.
- **Windows maintenance pattern**: when optimizing hooks/plugins on Windows, discover the layout with `find` and `ls`, check hook scripts with `cat`, and account for WinError 32 file-lock races in log paths. Plugin manifests (`plugin.yaml`) declare name, version, hooks, platforms, and provided tools. Mixing `plugin.yaml` files at plugin root instead of isolated subdirectories is non-standard and should be noted in audit results.

- **Mandatory 5-skill session startup (2026-06-21)**: User requires loading and verifying 5 specific skills at the start of EVERY session before any response or task:
  1. `/using-superpowers` — foundational skill workflow
  2. `/user-communication-preferences` — concise, action-first, DRY responses
  3. `/session-audit-report` — generate SESSION_REPORT.md with full audit
  4. `/hermes-profiles` — profile identity, provider enumeration, system maintenance
  5. `/validate-memories` — validate USER.md/MEMORY.md across all profiles
  - Verify all 5 skills loaded and executed (not just invoked)
  - This is now encoded in SOUL.md Core Rule #6, USER.md Execution Preferences, MASTER_RULES.md Level 1 Rule #6, PROJECT_RULES.md Level 1 Rules #4-6, AGENTS.md Quick Rules #6-8, .hermes.md Session Startup Rules

- **MCP-first tool precedence (2026-06-21)**: Before any native tool (terminal, read_file, search_files, etc.), check if an MCP server provides equivalent functionality. The 11 configured MCP servers (filesystem, github, ast-grep, memory, playwright, sequential-thinking, cli, code-sandbox, fetch, mcp-docker) are more token-efficient and must be preferred. This is now in Phase 2 of the workflow above.

- **Profile-per-task routing (2026-06-21)**: Run `hermes profile use <name>` matching task type BEFORE execution. Routing table:
  | Task Type | Profile |
  |-----------|---------|
  | Code implementation, debugging, refactoring | `code-architect` |
  | Deep research, literature review, synthesis | `research-analyst` |
  | Design, content creation, brainstorming | `creative-director` |
  | Planning, coordination, admin | `exec-assistant` |
  | Tutorials, explanations, teaching | `patient-tutor` |
  | System operations, DevOps, infra | `adminbot` |
  | General purpose | `default` |
  This is now in Phase 1 of the workflow above and encoded across all context files.

- **Strict sequential creation pattern (2026-06-24)**: When the user chains phases with "only then" (e.g., "create all templates and only then linking to a prompt library and lastly setting up CI checks"), treat each phase as a hard dependency. Complete and verify Phase N fully before starting Phase N+1. This prevents orphaned assets and ensures each layer is testable before the next depends on it. Applied when creating the `prompt-management` skill: templates → references → scripts → CI workflow → skill asset list update.

- **Class-level skill scaffolding pattern (2026-06-24)**: When building a new class-level skill, create the full asset tree in one session:
  1. `SKILL.md` with workflow, rules, verification checklist
  2. `templates/` — one skeleton per required section
  3. `references/` — workflow diagrams + integration guides
  4. `scripts/` — statically re-runnable validation/sync utilities
  5. `.github/workflows/` — CI that exercises the scripts
  6. Update `SKILL.md` Assets list to reference every new file
  This avoids follow-up sessions just to "finish the skill."

See references/session-reporting.md for recommended implementation templates, verification steps, and a short hook snippet.
**See references/session-startup-protocol.md for the complete mandatory 5-skill session startup protocol, profile routing table, and MCP server precedence.**


