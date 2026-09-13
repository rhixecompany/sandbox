# Implementation Plan — Profile Identity & Model Refactor

> Protocol: multi-file-change-protocol (reloaded for new task). Sequential inspection; parallel execution permitted per user clarification (parallel updates selected, sequential gates enforced). Profile: adminbot (execution + verification). User approved destructive ops.

## Source Reference (verified in user prompt — docs snippet, verified from docs URL)

Title: "Personality & SOUL.md" | sidebar_position: 9 | description: "Customize Hermes Agent's personality with a global SOUL.md, built-in personalities, and custom persona definitions."

Verified sections from docs content (retrieved from docs snippet; original URL not fetched due to previous timeout — noted honestly):
- SOUL.md is primary identity (slot #1 in system prompt); loaded from `HERMES_HOME` (`~/AppData/Local/hermes/SOUL.md` by default).
- SOUL.md never overwritten; falls back to built-in identity if empty/unreadable.
- `/personality` = temporary session-level overlay; `SOUL.md` = durable default.
- Custom personalities in `config.yaml`: `agent.personalities` (or `personalities:` block).
- `agent.system_prompt` reserved for manual system prompt; applies only when no personality selected (`/personality none/default/neutral`).
- Reset overlay: `/personality none` / `default` / `neutral` clears selection.
- Personality never touches `agent.system_prompt` directly.

## User Constraints (from clarification + request)

1. Refactor ALL Hermes profile directories (`~/AppData/Local/hermes/profiles/*` — 15 found: alexa, code-architect, creative-director, cto, default, designer, dev, exec-assistant, ops, patient-tutor, pm, qa, research-analyst, security, skills).
2. Profile identity files: `SOUL.md`, `USER.md`, `MEMORY.md`, `description`, `alias` — create/update/refactor.
3. Set model config: `inkling:free` delivered via `openrouter` for every profile (per docs snippet + user instruction "set every profile model to be inkling:free by openrouter").
4. Include descriptions and aliases for all profiles; set globally.
5. Ensure `config.yaml` and `.env` per profile reflect model/provider settings correctly.
6. Reuse 14-skill protocol; sequential inspection → parallel application → sequential verification gates.
7. No synthetic session IDs; no fabricated results; honest blocker reporting.

## Subgoals (sequential gates with parallel execution within phases)

| # | Phase | Scope | Gate | Verification |
|---|---|---|---|---|
| P1 | Inspect | Read identity files (SOUL.md, USER.md, MEMORY.md, config.yaml, .env) for all 15 profiles | Profile list confirmed; identity content captured | File existence + content summary per profile |
| P2 | Plan | Write `.hermes/plans/profile-refactor-plan.md` + design identity templates (SOUL.md structure, USER.md, MEMORY.md, description/alias, model setting) | Plan file exists; references docs snippet sections verified; includes milestones M1-M4 | Read plan; verify references |
| P3 | Execute (parallel) | Update identity/config for all 15 profiles: SOUL.md (set identity + model note), USER.md (canonical pointer/update), MEMORY.md (update if stale), description/alias (set globally), config.yaml (model: inkling:free via openrouter), .env (provider settings as needed) | Each profile updated; no missing files; model reference present in SOUL.md/config.yaml | Per-profile verification checklist; grep for `inkling:free`, `openrouter`, `description`, `alias` |
| P4 | Verify (sequential) | Verify updated files; compare before/after for all profiles; check for broken pointers; report any remaining open items | Final verification report + session log update; open items listed honestly | Read updated identity files; confirm model settings |

## Design Template (per profile — DRY, from docs snippet)

Based on verified docs content (§Personality & SOUL.md):

- **SOUL.md**: identity line (`Profile: <name> | Alias: ... | Model: inkling:free (openrouter) | ...`); include persona description; stable identity (not task instructions — those go in AGENTS.md/project files per docs distinction).
- **USER.md**: either pointer (`> Canonical source: ~/AppData/Local/hermes/memories/USER.md`) or direct user profile content (`user: Alexa`, environment, preferences).
- **MEMORY.md**: durable facts; no temporary TODO/state (docs: session progress/temp state belongs in session history, not MEMORY.md).
- **Config.yaml**: model override section (`model: base_url: https://openrouter.ai/api/v1; default: ...; provider: openrouter`) ensuring `inkling:free` is the active/default model reference.
- **.env**: provider/auth keys (already present); no removal — only verify/update if needed.
- **Description/Alias**: profile-level descriptor (e.g., `code-architect`: alias="Senior Engineer / Architect"; description="Profile for architecture analysis, code review, system design, and engineering leadership.")

## Milestones
- M1: P1 inspection complete — all 15 profiles listed with identity file inventory.
- M2: P2 plan complete — `.hermes/plans/profile-refactor-plan.md` written; template design verified.
- M3: P3 execution complete — all profiles updated; model settings set; descriptions/aliases set; identity files consistent.
- M4: P4 verification complete — `.hermes/plans/` (or docs) verification report; open items listed; session log appended; no synthetic results.

## Resource Allocation
- Skills: 14-skill stack reused (multi-file-change-protocol, using-superpowers, writing-clearly-and-concisely, user-communication-preferences, plan/plans-and-specs, subagent-driven-development).
- Profiles: 15 target profiles (parallel updates allowed by user clarification; sequential verification enforced).
- Model: user requires `inkling:free` delivered by `openrouter`. Note: docs snippet mentions `openrouter` provider; workspace `default/config.yaml` shows `provider: openrouter` but model `deepseek/deepseek-v4-flash-0731`. Must set model reference correctly to match `inkling:free`.

## Constraints / Rules (reiterated)
- Never invent profile identity content; base updates on existing identity or standard descriptions (from profile names: alexa/default/user; code-architect = architecture; creative-director = design/creative; cto = strategic/technical leadership; designer = design/UX; dev = development/engineering; exec-assistant = execution/planning; ops/adminbot = operations/devops; patient-tutor = teaching; pm = project management; qa = quality assurance; research-analyst = analysis/research; security = security/compliance; skills = skill management; default = general-purpose).
- Model: `inkling:free` by `openrouter` (user instruction verified). Do NOT invent other providers unless docs specify otherwise.
- Sequential gates: P1 → P2 → P3 (parallel within) → P4. No gate skipped.
- No destructive commit/push/deletion of profile directories — only identity/config file updates.
- Report open items honestly (e.g., any profile files that cannot be updated, any broken pointers, any config conflicts).
