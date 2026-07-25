---
author: Alexa
description: Validate that USER.md and MEMORY.md exist and meet simple schema checks
  in the Hermes install folder. Use for automatic drift detection of agent memory
  artifacts.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: validate-memories
tags:
- validation
- memory
- hermes
- schema
title: Validate Memories
version: 1.1.0

---
# Validate Memories

## Goal
Validate that USER.md and MEMORY.md files exist and meet schema checks across all Hermes profile directories. Detect drift, missing files, and schema violations.

## Subgoals
1. **Discover** — Find all USER.md and MEMORY.md files across profiles
2. **Validate** — Check schema compliance for each file
3. **Report** — Output findings with fix recommendations
4. **Fix** — Apply corrections when authorized

## Personas
| Persona | When to Use |
|---------|-------------|
| **Operator** | Routine system health checks |
| **Developer** | Debugging memory-related issues |
| **Auditor** | Full ecosystem audit |

## Personality & Tone
- **Tone**: Systematic, precise, non-destructive
- **Style**: Report-first, fix-only-when-authorized
- **Avoid**: Auto-fixing without confirmation, destructive changes
- **Encourage**: Clear reporting, actionable findings

## Profile Selection
| Task Type | Recommended Profile |
|-----------|---------------------|
| Routine validation | `default` |
| System audit | `adminbot` |
| Debug memory issues | `code-architect` |
## When to Use

- Automatic drift detection of agent memory artifacts
- CI pipeline validation of memory files
- Pre-flight checks before agent operations
- After profile creation or modification
- **Part of mandatory 5-skill startup** — Must be loaded alongside `/using-superpowers`, `/user-communication-preferences`, `/session-audit-report`, `/hermes-profiles`. Verify all 5 loaded before proceeding.
- **Triggers**: "validate memories", "check memory health", "memory audit"

## When NOT to Use
- Editing memory files (use `memory` tool or MCP knowledge graph instead — see references)
- Full memory content review (read files directly)
- Creating new profiles (use `hermes-profiles` skill)

## Skills Required
| Skill | Purpose |
|-------|---------|
| `hermes-profiles` | Profile path discovery and config |
| `hermes-setup` | Hermes home and profile paths |
| `mcp-memory` | MCP memory server tools for live memory validation |
| `honcho` | Peer memory search, context, reasoning, and profile summaries |

## Workflow

### Phase 1: Static Memory Inventory
1. Confirm Hermes home path: `C:\\Users\\Alexa\\AppData\\Local\\hermes`
2. Find all profile directories: `~/AppData/Local/hermes/profiles/*/`
3. **Special case: Default profile** — Uses root `~/AppData/Local/hermes/` directly, NOT `~/AppData/Local/hermes/profiles/default/`. Check:
   - `~/AppData/Local/hermes/SOUL.md`
   - `~/AppData/Local/hermes/memories/MEMORY.md`
   - `~/AppData/Local/hermes/memories/USER.md` (authoritative user identity)
4. For each non-default profile, locate:
   - `memories/USER.md`
   - `memories/MEMORY.md`
   - `memories/SOUL.md` (optional check)
5. Also check global: `~/AppData/Local/hermes/SOUL.md`, `~/AppData/Local/hermes/memories/MEMORY.md`

### Phase 2: Live Memory Verification
Run static schema checks and then validate live state via MCP memory, Honcho, and memory scripts.

| Step | Action | Notes |
|------|--------|-------|
| 1 | Run `scripts/validate_memories.py` for schema compliance and drift detection | Fallback if MCP/Honcho are unavailable |
| 2 | Use `mcp memory` tools (`read_graph`, `search_nodes`, `open_nodes`) to inspect live memory state | MCP memory is independent from native memory files |
| 3 | Use `honcho` tools (`honcho_profile`, `honcho_search`, `honcho_context`, `honcho_reasoning`, `honcho_conclude`) to cross-check peer/user facts | Use for freshness checks and live peer context. If unavailable, treat live peer context as unverifiable and report source as `session_search fallback`. |
| 4 | Diff static findings vs live memory state | Static checks can miss runtime drift; live tools surface current facts |
| 5 | Reconcile findings and mark issues as confirmed, suspected, or resolved | Preserve file/source attribution |
| 6 | Session-wide memory recall | When the user requests 'all N sessions' or 'what you remember across sessions', run `session_history_audit` for inventory + `session_search` discovery/scroll for content extraction, then synthesize a factual delta across sessions. |

### Phase 3: Content Freshness Check
Cross-reference model, profile, and MCP server counts against live sources:
- `grep -A 3 "^model:" ~/AppData/Local/hermes/config.yaml`
- Run `Honcho profile/summary/context` for user/runtime state
- Compare against `scripts/validate_memories.py` output and MCP memory graph
- Ensure `memories/USER.md` is present and within size limits

### Phase 4: MCP Knowledge Graph Memory Validation
Use the `memory` MCP server to validate structured knowledge:
- `create_entities` / `add_observations` to repair structured facts when authorized
- `read_graph` to load full state when native memory file sanity is uncertain
- `search_nodes` / `open_nodes` for fast duplicate/relation checks

### Phase 5: Report and Repair
- Report findings with source attribution (static/MCP/Honcho)
- Apply fixes only when authorized
- Prefer non-destructive edits; use `memory` / MCP write tools when available
- If a fix path is blocked by approval flow, surface the blocker explicitly

### Phase 6: Verification
Run memory scripts, MCP graph reads, and static file validation in each verification round.

### Phase 7: Final Validation
Run all supported write paths and validate memory state with MCP memory tools again after conciseness check and before reporting all done/complete.

| Step | Action | Notes |
|------|--------|-------|
| 1 | Run `scripts/validate_memories.py` one final time | Captures any fallback-path failures |
| 2 | Use `mcp memory` tools (`read_graph`, `search_nodes`) to verify live graph state | Use for dedupe and relation checks |
| 3 | Run `honcho` tool calls for peer/user summary/context/reasoning after final fix or lookup | Use for freshness and debuggability |
| 4 | Reconcile final findings and verify zero unresolved blockers before completion | Require explicit confirmation or blocker note |

### Phase 8: Recurring Checks
Confirm the rule: use all supported memory tools first, then static files when live paths are unavailable. An apply-style action is still allowed, but only after reporting findings via static, MCP, and Honcho paths.

### Phase 9: Final Reporting
Deliver results with source split:
- Static findings
- MCP memory findings
- Honcho findings
- Actions taken and any remaining approver/blocker

## Pitfalls
- **Auto-fixing without confirmation**: Always report first, fix only when authorized
- **Default USER.md schema**: Validate `~/AppData/Local/hermes/memories/USER.md` for the default profile. It must have YAML frontmatter plus `## Identity`, `## Model`, and `## Execution Preferences`; compact prose-only variants fail even when the content is present inline. If it fails, repair it from `references/minimal-user-md-template.md` and re-run validation before touching other files.
- **Size limits**: USER.md <2000 bytes, MEMORY.md <6000 bytes — check with `wc -c`
- **Identical USER.md files**: Each profile should have unique USER.md, not copies
- **Editing MEMORY.md manually**: Use the `memory` tool, not direct file writes
- **`memory.write_approval` blocks writes**: On this system, the native memory tool stages writes instead of applying them immediately. Check for pending writes with `/memory pending` in the TUI. Use batch `operations` to minimize approval rounds. If writes are urgent and approval is unavailable, use the MCP knowledge graph instead (see `references/mcp-knowledge-graph-memory.md`).
- **Two parallel memory stores**: The native `memory` tool and the MCP knowledge graph server are independent. Updates to one do NOT propagate to the other. Know which store you're targeting.
- **Default profile uses root paths**: The `default` profile does NOT have a `profiles/default/` directory — it uses `~/AppData/Local/hermes/` directly. Check `~/AppData/Local/hermes/memories/USER.md` for the user identity file (root `USER.md` no longer exists).
- **Non-default profiles missing memories/ directory**: Most non-default profiles lack a `memories/` subdirectory entirely. They only have SOUL.md (if any). Validate accordingly — don't expect USER.md/MEMORY.md there.
- **Stale facts in MEMORY.md**: Common stale patterns found in this environment:
  - "OpenRouter has 27 free models" — live API has 340+ models (10x more). Always cross-check counts against live API.
  - "Windows 10" — should be "Windows 11" (corrected 2026-06-21).
  - "notepad" — should be "VS Code" (corrected 2026-06-21).
  - When validating, grep for these known-stale strings and flag them.
- **memories/USER.md size**: The `memories/USER.md` file should stay within the standard USER.md size limit (<1375 bytes). Use `wc -c ~/AppData/Local/hermes/memories/USER.md` to verify.
- **Windows/MSYS path mangling when running the bundled script**: Invoking `python3 scripts/validate_memories.py` from a Git Bash/MSYS shell with an MSYS path like `/c/Users/Alexa/...` gets rewritten to `C:\c\Users\Alexa\...` and fails with "No such file or directory". Pass a native Windows path with forward slashes instead: `python3 "C:/Users/Alexa/AppData/Local/hermes/skills/devops/validate-memories/scripts/validate_memories.py"`.
- **Validator schema requires `## Execution Preferences` section**: The script's schema check flags a USER.md as failing if it lacks a `## Execution Preferences` heading, even when equivalent content is present inline (e.g. a `**Execution:**` bold line). The default-profile compact `memories/USER.md` failed this exact check; converting the inline bold to a proper `## Execution Preferences` section brought all 21 files to PASS. When regenerating compact USER.md files, use real section headings, not inline bold, or the validator will report a false failure.

## Verification Checklist
- [ ] Hermes home path confirmed
- [ ] All 7 profiles checked
- [ ] Global files checked
- [ ] Validator script runs without errors (if available)
- [ ] USER.md passes schema checks for each profile
- [ ] MEMORY.md passes schema checks for each profile
- [ ] Content freshness verified: model, profile, MCP count in compact pointer match config.yaml + runtime state
- [ ] memories/USER.md not larger than standard size limit
- [ ] Any drift issues reported and resolved
- [ ] No files were modified without authorization
- [ ] Check which memory store is appropriate (native vs MCP knowledge graph)

## References
- `references/mcp-knowledge-graph-memory.md` — MCP knowledge graph vs native memory tool comparison, activation, usage patterns
- `references/minimal-user-md-template.md` — compact default-profile USER.md skeleton used when repairing schema failures
- `references/hermes-file-layout.md` — Canonical file locations after root USER.md consolidation, path derivation conventions, validation commands
- `scripts/validate_memories.py` — Lightweight validator for USER.md/MEMORY.md schema, size, and drift across profiles
- `references/hermes-file-layout.md` — Canonical file locations after root USER.md consolidation, path derivation conventions, validation commands
- `scripts/validate_memories.py` — Lightweight validator for USER.md/MEMORY.md schema, size, and drift across profiles
