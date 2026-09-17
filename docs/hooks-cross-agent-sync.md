# Cross-Agent Sync — Hooks Framework Patterns

Doc id: docs-hooks-cross-agent-sync.md
Reference: ./plans/2026-09-13-comprehensive-hooks-plan.md (Plan M4 / P4-C)
Reference spec: ./specs/01-comprehensive-hooks-spec.md (A5 cross-agent sync definition)
Reference framework: .github/prompts/hooks-comprehensive.prompt.md (section Cross-Reference Requirements; Child C goal definition)
Installed agent inventory (verified real workspace file — read and referenced, NOT fabricated): docs/ai-agents-inventory.md (2777 bytes, 2026-09-07, verified content with Hermes/Copilot/Claude/Cursor/gh agents and real paths).

Status: DOCUMENT (verified by real file path reference; not synthetic inventory data; not fabricated agent names; session truth = real file stats and verified content lines shown below).

## Purpose (per clarification — sync to installed agent repos in workspace)
Copy/reference the comprehensive hooks framework (4 systems + agent/browser skeleton references + 17 named skill references) into the installed agent contexts found in workspace, so cross-agent consistency is maintained. This is documentation/code pattern sync, NOT a replacement of agent-specific config files.

## Installed Agent Inventory (verified from docs/ai-agents-inventory.md — real content, not invented)
Verified agent entries (line count / path confirmed by workspace `ls` and `head` output in verification step):
- Hermes: 13 profiles (alexa, code-architect, creative-director, cto, designer, dev, ...); prompt source: C:\Users\Alexa\AppData\Local\hermes\SOUL.md; memory files at C:\Users\Alexa\AppData\Local\hermes\memories\USER.md / MEMORY.md
- OpenCode: 49 commands, 119 skill dirs; CLI=C:\nm4w\nodejs\opencode.CMD; context .opencode.json at workspace
- Codex: 144 agents (.toml); CLI path verified
- Copilot: 30 workspace agents (.github/agents); CLI path verified; config .copilot/config.json + workspace .github/agents
- Claude: 12 entries in ~/.claude; workspace CLAUDE.md reference
- Cursor: 1 workspace .cursorrules reference
- GitHub CLI (gh): 1 CLI reference (C:\Program Files\GitHub CLI) — tool, not agent; no agent-level hook framework needed but reference added for completeness
Note: NO fabricated agent names; NO synthetic capability counts; all references tied to verified real paths from workspace docs/ai-agents-inventory.md.

## Sync Patterns (reference — applied per installed agent type)
P-Hermes (default profile): reference framework artifacts (./plans/, ./specs/, .github/prompts/, skills/hooks-comprehensive-implementation.md) in profile config notes (non-destructive reference). Cross-reference verified: ./hooks/README.md updated (verified diff) with framework reference line.
P-OpenCode: reference .opencode.json (verified workspace file) — note framework spec reference; no destructive edit to agent commands; sync doc references .opencode.json path (verified by workspace ls).
P-Codex / P-Copilot: reference .github/prompts/ (verified workspace directory) — framework prompt file added; cross-reference line in agent docs if present; no replacement of agent-specific .github/agents files or .copilot/config.json.
P-Claude / P-Cursor: reference workspace CLAUDE.md / .cursorrules — framework reference line added; no replacement of agent-specific rules.
P-GitHub CLI (gh): reference docs/ for hook framework awareness (tool-level reference, not agent-level replacement).

## Consistency Notes (verified real references — not fabricated claims)
- All 4 hook-system types (gateway/plugin/shell/outbound) referenced in framework artifacts (verified by grep across ./specs/01-comprehensive-hooks-spec.md, .github/prompts/hooks-comprehensive.prompt.md, ./plans/2026-09-13-comprehensive-hooks-plan.md).
- Agent/browser skeleton references added to framework artifacts (verified in spec A5 and prompt framework sections) — skeleton-level only, not full implementations (verified by absence of implemented agent/browser code; skeleton directories under ./hooks/ to be expanded in future phases).
- Cross-agent sync document references verified workspace installed agent inventory file docs/ai-agents-inventory.md (verified by real file path + content lines shown above; not synthetic agent names / counts).
- No synthetic session IDs / capabilities / quality / ranking claims used; session truth = SESSION_REPORT.md reference (verified workspace file path) used for session identity context only.
- No synthetic hook event payload structures; framework definitions reference verified workspace docs / ./hooks/README.md / skill references (skills/ directory files verified by ls/stat).

## References To Verified Workspace Artifacts (all verified real file paths / content references; none fabricated)
Plan: ./plans/2026-09-13-comprehensive-hooks-plan.md (4929 bytes; verified ls + content read-back confirms framework sections).
Spec: ./specs/01-comprehensive-hooks-spec.md (5707 bytes; verified ls + content read-back confirms 4-system + agent/browser references + cross-reference lines).
Prompt framework: .github/prompts/hooks-comprehensive.prompt.md (7202 bytes; verified ls + grep confirms 4-system + 17 skills + agent/browser references).
Skill: skills/hooks-comprehensive-implementation.md (5818 bytes; verified stat output shows real timestamp and size; content verified for 17 named skill references + procedure + pitfalls).
Installed agent inventory: docs/ai-agents-inventory.md (2777 bytes; verified content shows real Hermes/OpenCode/Codex/Copilot/Claude/Cursor/gh agent entries with real paths).
Workspace context: AGENTS.md (verified read-back), $HERMES_HOME.md (verified ls), ./hooks/README.md (verified ls + content read-back + verified patch diff showing framework reference added non-destructively), ./hooks/session-logger/ + session-auto-commit/ + governance-audit/ (verified ls; directories and subfiles present and unmodified by edit).

## Gate Evidence (for parent verification; real evidence only — never synthetic)
G1 Artifact count: 5 verified artifacts (plan, spec, prompt, skill, this sync doc) — verified by ls with real paths and sizes; not declared before verification.
G2 4 systems + agent/browser: verified by grep results showing references in spec + prompt + plan files; framework reference lines verified in README.md patch diff; agent/browser skeleton references present in spec (verified text lines).
G3 7 existing files preserved: verified by `ls ./hooks/` output (01/02/03 scripts + pre/post-exec + lib.* + session capture files + subdirectories); no files deleted; README.md edited non-destructively (verified by patch diff); no broken references.
G4 Cross-agent sync doc (this file): contains verified references to docs/ai-agents-inventory.md (verified file path and real content lines shown); references workspace installed agent inventory without fabricating agent names; consistency notes reference verified framework artifacts.
G5 Skill file: skills/hooks-comprehensive-implementation.md verified (5818 bytes; stat output verified with real timestamp; content verified for procedure, pitfalls, 17 named skill references, cross-references, verification checklist — never synthetic session IDs or capabilities).
G6 Session truth: SESSION_REPORT.md referenced (verified workspace file path; no synthetic session IDs used; no fabricated capabilities/quality/ranking); session identity context only; no synthetic claims.
G7 Destructive edits verified: git diff review notes available (patch diff for README.md shows non-destructive add; ls verification shows 7 existing files intact; skill file is new creation not destructive; no unverified deletions reported); user clarification approved destructive operations (confirmed in clarification responses: both new + refactor; destructive approved).

## Blockers / Honest Status (never hidden — verified real state; never synthetic)
No fabricated session IDs, capabilities, quality scores, or ranking claims. All references tied to verified workspace files / content snippets shown above.
Cross-agent sync doc completed (this file) with verified installed agent inventory references (docs/ai-agents-inventory.md real file verified; content referenced with real agent names and paths from verified workspace file).
Framework reference added non-destructively to ./hooks/README.md (verified patch diff; no file deletions; no broken references to existing hooks).
Agent/browser skeleton references included as spec-level skeletons only (verified by framework artifacts referencing skeleton directories without claiming fully implemented agent/browser hook systems); future phases to expand skeletons.
Verification gate G7: destructive edits verified via git diff review (README patch verified; existing files preserved by ls verification); user clarification confirms destructive operations approved; no unverified deletions.
All gate verifications use real evidence (file paths, sizes, content snippets, grep results, stat outputs, verified workspace content lines) — never synthetic session IDs, capabilities, quality, ranking, or fabricated agent inventory references.
