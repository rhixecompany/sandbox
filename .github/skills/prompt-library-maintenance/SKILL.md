---
name: prompt-library-maintenance
title: "Prompt Library Maintenance"
description: "Batch front-matter validation, toolset normalization (VS Code/Help → Hermes), filename-name consistency checks, and bulk YAML fixes for large prompt directories."
version: 1.8.0
author: "Alexa (via Hermes)"
license: MIT
tags: ["prompt", "batch", "maintenance", "audit", "yaml"]
---

# Prompt Library Maintenance

Provide a repeatable workflow for maintaining a large prompt library: validate front-matter, normalize toolsets, fix name inconsistencies, and apply bulk fixes using Python + yaml (not regex/sed).

## When to Use

- After importing a batch of prompts from an external source (Copilot, Codex, etc.)
- When running a scheduled audit of a prompt directory
- When preparing prompts for a new Hermes profile or toolset
- When cleaning up name/trigger mismatches across many prompts
- When canonicalizing prompt trees into a new root and rewriting cross-references
- When regenerating a trusted prompt repair list from a repaired scanner/report generator
- When an orchestrator prompt references child prompt/template files that may be missing

## Library Governance Notes

This umbrella absorbs the older audit, verification, consolidation, and repair variants that used to live as separate narrow skills.

- Audit and quality review: full-library checks, domain registry, and read-only scoring.
- Integrity verification: required-field checks, DEPS==SKILLS sync, and cross-reference validation.
- Near-duplicate consolidation: parameterized merges, toolset normalization, and orphan cleanup.
- Repair of malformed prompt packages: duplicate frontmatter, doubled headers, and missing template materialization.
- Canonical root migration: copy/create canonical tree, rewrite stale path tokens, verify dedupe, then retire legacy dirs only after active references are gone.
- Repair-list regeneration: fix scanner normalization first, then rerun from the actual workspace, verify independently, and clean up temp verifiers.
- Orchestrator child-reference repair: when an orchestrator prompt references child prompt/template files, enumerate referenced paths, verify each exists, report missing paths explicitly, and only then create missing files or ask before fabricating content.

## Skills Required

| Skill | Purpose |-------|---------|
| `prompt-management` | Overall prompt lifecycle (create/update/execute) |
| `validate-memories` | Schema validation patterns |
| `prompt-library-consolidation` | Legacy tree canonicalization and dedupe |

## Workflow

### Phase 1 – Validate Frontmatter
1. Run `scripts/validate_prompt_frontmatter.py` across the prompt directory.
2. Fix any missing/empty required fields (`name`, `description`, `version`).
3. Ensure `tags:` is non-empty (infer from filename/description if needed).

### Phase 2 – Normalize Toolsets
Many prompts carry VS Code/Copilot-specific tool names that are not valid Hermes toolsets:

Known Hermes toolset palette:
`web, browser, terminal, file, code_execution, vision, image_gen, moa, tts, skills, todo, memory, context_engine, session_search, clarify, delegation, cronjob`

Mapping (VS Code → Hermes):
- `edit/editFiles`, `createFile`, `editFiles` → `file`
- `web/fetch`, `fetch`, `openSimpleBrowser` → `web`
- `runCommands`, `terminalCommand`, `runInTerminal`, `execute/runInTerminal`, `runCommands/*` → `terminal`
- `search/codebase`, `codebase`, `search/changes` → `file`
- `githubRepo`, `github`, `github/*` → (remove or use MCP GitHub, not a toolset)
- `vscode.*`, `extensions`, `usages`, `problems`, `todos`, `changes`, `testFailure`, `vscodeAPI` → (remove – VS Code internal)
- `microsoft.docs.mcp`, `context7/*`, `nextjs-docs-mcp/*` → `web` or `fetch`
- `playwright/*`, `io.github.chromedevtools/chrome-devtools-mcp/*` → `browser`
- `search` → `web` (legacy toolset name; `search` is not a valid Hermes toolset. Found en masse in prompt imports — use `web` instead)
- Unknown entries → remove. If nothing valid remains, default to `[terminal, file]`.

Use Python + `yaml.safe_load` for these edits – regex on YAML frontmatter causes array collapsing and key merging.

### Phase 3 – Name/Filename Consistency
1. For each `*.prompt.md` file, extract the slug: `stem = filename.replace('.prompt.md', '')`.
2. Compare to `name:` field in frontmatter.
3. If they differ, set `name:` to the slug.
4. Also verify `trigger:` matches `/` + slug.

### Phase 4 – Run After-Fix Validation
1. Re-run `validate_prompt_frontmatter.py` to confirm zero errors.
2. Run `dry_run_prompts.py` to check toolsets and reference integrity.
3. **Validate all `skills:` frontmatter references** — for every prompt that lists skills in its frontmatter, verify each referenced skill exists on disk under `~/AppData/Local/hermes/skills/`. Missing skill references silently degrade prompt behavior. Use Python: `set(os.listdir(skills_dir))` vs set of referenced names to find gaps.
4. Check with `skill-judge` if prompt-level quality scoring is needed.

### Phase 5 – Read-Only Delegation Map & Domain Registry (no edits)

When asked for a delegation map or a library overview WITHOUT modifying prompts:

1. **Extract cross-prompt edges** from frontmatter `dependencies:` items matching `^prompt:([A-Za-z0-9._-]+)$` (optional `.prompt.md` suffix). Normalize target to `<name>.prompt.md`, check existence on disk, collect dangling refs. See `references/cross-prompt-delegation-and-domain-registry.md`.
2. **Classify domains by FILENAME STEM, not tags** — see pitfall below. One primary domain per file, iterate until 100% coverage (zero `uncategorized`).
3. **Write a report only** (e.g. `docs/prompt-registry.md`); never `patch`/`write_file` the `*.prompt.md` sources. This is a read-only analysis deliverable.
4. **Verify independently** (separate script, different code path) before delivering — re-derive edges/domains and cross-check the report's counts. Write the verifier to `%TEMP%/hermes-verify-*.py`, run, then delete.

### Phase 6 – Canonical Root Migration Checklist

Use this when moving prompt-family assets into a canonical root such as `.github/prompts/`:

1. **Inventory sources and targets** — count files in legacy trees and the proposed canonical tree.
2. **Check for exact duplicates** — hash bodies across the full canonical set after copy; dedupe any duplicate groups before patching.
3. **Rewrite canonical copies first** — update stale path tokens inside the migrated prompt files themselves so they point at the new canonical layout.
4. **Patch active docs/CI/workflows** — update references from old paths to new paths.
5. **Search broadly for stale tokens** — grep the repo for legacy prompt-family path tokens; fix hits in docs, scripts, instructions, and archived files as appropriate.
6. **Retire legacy dirs only after zero active references** — do not delete `.github/agents/`, `.github/instructions/`, `.github/skills/`, or root `prompts/` until searches confirm nothing active still depends on them.

### Phase 7 – Orchestrator Child-Reference Repair

Use this when an orchestrator prompt references child prompt/template files that may be missing.

1. **Enumerate referenced paths** — extract all child prompt and template paths from the orchestrator body/template refs.
2. **Verify existence** — check every referenced prompt file and template file on disk.
3. **Report exact missing paths** — if any are missing, pause and report them instead of fabricating child content.
4. **Create placeholders only when authorized** — if requested, create meaningful placeholder files with a proper header, Purpose, and TODO-to-author; never create empty or malformed stubs.
5. **Re-verify** — after any placeholder creation, rerun the existence check until all referenced paths resolve.
6. **Execute only after references resolve** — do not run the orchestrator while child references are still missing.

## Pitfalls

- **Assembler ≠ prompt**: Editing prompt-building code changes behavior, not prompt text. Only edit the user-facing prompt files.
- **Hardcoded prompt legend**: npm Copilot CLI system prompts are typically embedded in package source, not stored in a dedicated editable prompt file. Treat embedded/packaged prompts as read-only unless explicitly asked to inspect/package internals.
- **Hidden prompt claims**: If research or prior memory asserts an untrusted hidden instruction block exists, verify it on disk first; do not add corrective text based on an unverified injection narrative.
- **Orchestrator with dead child refs**: An orchestrator prompt can appear valid while referencing missing child prompts/templates. Treat it as blocked until every referenced path exists, or is explicitly authorized to be created as a meaningful placeholder.
- **Fabricated child content**: Do not synthesize child prompt bodies to unblock an orchestrator. Create placeholders, or stop and report the missing files.

## Verification Checklist

- [ ] Frontmatter validator returns "All prompt front-matter valid."
- [ ] Dry-run validator returns "All prompts passed dry-run validation."
- [ ] No prompt has a `name:` differing from its filename slug.
- [ ] No prompt has a `trigger:` diverging from `/<name>`.
- [ ] No prompt uses `triggers:` (plural) instead of `trigger:` (singular).
- [ ] No file ends in `.md` instead of `.prompt.md` (except non-prompt markdown).
- [ ] No toolset contains `search` (use `web` instead) or VS Code/CLI-specific entries.
- [ ] No MCP tools are listed with `skill:` prefix in `dependencies:` (use `tool:`)
- [ ] No MCP tools appear in the `skills:` section
- [ ] No prompt has a self-referencing `skill:` in `dependencies:`
- [ ] Every prompt with `tool:mcp-*` deps also has `- mcp` in `toolsets:`
- [ ] No body text references non-existent tools (e.g. dispatching-parallel-agents)
- [ ] `metadata.hermes.related_skills` in sync with corrected `dependencies:` prefix types
- [ ] No duplicate entries in `toolsets:` list
- [ ] Independent second verifier reports `TOTAL=N CLEAN=N WITH_ISSUES=0` (for 100+ files)
- [ ] If a repair list was regenerated: it was rerun from the actual workspace cwd, verified independently from the generator, and any temp verifier artifacts were removed.
- [ ] All changes Git-tracked (no backup files).
- [ ] If size reduction was performed: target-file sizes were measured before/after with an independent check; prompt content/behavior was preserved and not replaced with invented hidden-document text.
- [ ] If an orchestrator prompt was repaired: every referenced child prompt/template path was verified to exist, or explicit placeholders were created and re-verified.

## Pitfalls

- **Duplicate frontmatter blocks**: A file with two `---` fences fools a rewrite-from-dict pass into dropping the second block's content into the body. Detect with `len(re.findall(r"^metadata:", raw)) > 1` or by counting `---`. Fix by rewriting the WHOLE file with `write_file`: one merged clean frontmatter + the real body from after the last `---`. Then re-verify.
- **Meta-tag pollution in domain classification**: Library-wide tags (`prompts`, `typescript`, `ml`, `specification`, `frontend`) appear on 80–200 files. Tag-based categorization (`if "ml" in tags`) false-floods domains. Categorize by FILENAME STEM (priority-ordered substring rules, specific→general), giving each file one primary domain; verify 100% coverage with zero `uncategorized`. See `references/cross-prompt-delegation-and-domain-registry.md`.
- **Body-level `prompt:` is NOT a delegation edge**: Only `dependencies:` list items of form `- prompt:NAME` are cross-prompt delegation. Body step definitions like `- name: "X" prompt: "..."` are task descriptors — exclude them. Also `skill:`/`tool:` deps are NOT delegation edges (only the `prompt:` prefix means "delegate to another prompt").
- **Independent verifier required**: See Phase 4b. A self-reporting fixer is not sufficient evidence.
- **search_files glob false-zero on Windows**: `search_files(pattern='*.prompt.md')` on git-bash can return 0 even when hundreds of files exist. Confirm counts with `find`/`ls` in the terminal first.
- **DEPS==SKILLS must be bidirectional**: every `skill:` dep must be in `skills:` AND every `skills:` entry must be a `skill:` dep. A one-directional sync leaves `SKILL_LIST_ONLY` / `SKILL_DEP_ONLY` dangling refs.
- **YAML corruption from regex**: Do NOT use sed/regex on YAML frontmatter. Always parse with yaml.safe_load, edit the dict, then dump with yaml.dump(sort_keys=False). Regex corrupts multi-line lists and nested structures.
- **Over-batch rewrite**: If >2 files get duplicate fields or broken fences from a single script pass, stop and switch to per-file `read_file` + targeted `patch`. Do not retry the same regex at scale.
- **Script-suffixed stubs (-script)**: Auto-generated placeholder skills may be created from Hermes scripts directory. These are wrappers with no standalone value — their functional equivalents live in category subdirs (e.g. development/) without the suffix. Before mass-deleting: search hub for equivalents, then verify cross-references in prompts/other skills. After `hermes skills uninstall`, directories remain on disk — clean with: `find ~/AppData/Local/hermes/skills -maxdepth 1 -name *-script -type d -delete`.
- **VS Code remnants**: Prompts imported from Copilot/Codex often carry dozens of VS Code tool names. Blindly removing them is fine – Hermes does not need them. Default to `[terminal, file]` when uncertain.
- **Name collisions**: Two prompts with the same slug can have overlapping `name:` values. Resolve by keeping the more specific slug.
- **Trigger mismatch**: If a prompt originally had no `trigger:` field, auto-generate as /<name>. If one existed but was /wrong-name, prefer the filename-derived value.
- **.md instead of .prompt.md**: Files ending in plain .md are not discovered by tools expecting .prompt.md suffix. Rename to canonical form.
- **Plural triggers vs singular trigger**: Some prompts use the plural `triggers:` field. Rename to `trigger:` (singular) — only the singular form is recognized.
- **MCP tools labeled as skills in dependencies**: MCP servers are TOOLS, not skills. Their references in dependencies must use `tool:mcp-<name>`, never `skill:mcp-<name>`. A `skill:` prefix causes the prompt loader to search for a Hermes skill that does not exist, silently dropping the tool.
- **MCP tools in skills: section**: The `skills:` frontmatter list is for Hermes SKILLS only. MCP tool names in this list are silently ignored by the loader. Always remove `mcp-*` entries from `skills:`.  
- **Self-referencing dependencies**: A prompt's `dependencies:` should never reference itself via `skill:<filename>`. This creates a circular dependency that loads nothing. Always remove self-refs.  
- **Missing mcp toolset**: When a prompt has `tool:mcp-*` etc. in its dependencies, it must also have `- mcp` in `toolsets:` list. Without the `mcp` toolset, the MCP tools are loaded but not callable — the agent cannot issue MCP tool commands.  
- **Dead tool references in body**: Prompt body text may reference tools that no longer exist (e.g. dispatching-parallel-agents was replaced by delegate_task). After renaming/removing tools, audit the body for dangling refs.  
- **related_skills drift after dep fixes**: After correcting dependency prefixes, the metadata.hermes.related_skills block can silently stay in the old format (bare skill names for MCP tools). Always sync this block to match the corrected `dependencies:` — MCP tools get `tool:` prefix.
- **Duplicate web in toolsets**: When adding `- web` to toolsets, check if it already exists to avoid duplicates. After any toolsets insert, verify no duplicates and remove extras.
- **Repair-list false positives from markdown-aware paths**: A broken normalizer can report existing template files as missing because it extracted backtick-wrapped paths or left a leading `templates/` segment. When the repair list contains known-good files unexpectedly, patch the extractor before touching prompt files.
- **Repair-list false positives from placeholders/globs**: Generic syntax fragments like `<prompt-name>`, `_shared/**`, `suggest-awesome-github-copilot-*`, or directory stems without a filename must be ignored by repair-list generators. They are not concrete missing files. Treat leaked placeholders as detector noise, not repair targets.
- **Trust no report from the patched script on first rerun**: after changing normalization, regenerate once, spot-check a few entries, then verify report structure separately. A patched generator can still emit false positives or malformed entries until its post-fix run is checked with an independent verifier.
- **Temporary verifiers must be cleaned up**: if you drop a temp verification script under `%TEMP%` or the repo, delete it after use. Leaving `hermes-verify-*.py` behind clutters cleanup and may be picked up by later audits.
- **Temp-file path hygiene on Windows**: when writing temporary verification scripts, prefer an actual temp directory instead of assuming the repo contains an `AppData` directory. A bad temp path often fails with `FileNotFoundError` on the first write/run.
- **Orchestrator dead child references**: Do not run an orchestrator prompt while its referenced child prompt/template files are missing. Stop, report the exact missing paths, and only then create placeholders or ask for direction. Do not fabricate missing prompt content to unblock execution.
- **Missing orchestrator runtime**: If an orchestrator workflow depends on `hermes prompt run ...` or a similar runner and that subcommand is unavailable, record the exact unavailable command in the report. Verify the referenced prompt files on disk, continue through available execution paths if possible, and do not silently omit execution evidence.

## Scripts Shipped With This Skill

Three statically re-runnable scripts (run with `python3`):
- `scripts/verify_prompt_library.py` — **independent second verifier** (separate code path from any fixer). Reports `TOTAL=N CLEAN=N WITH_ISSUES=M` across all prompts: missing fields, NAME≠SLUG, TRIGGER≠/slug, DEPS==SKILLS, MCP mislabels, invalid toolsets, duplicate `metadata:`, CRLF, and legacy sections. Run after every batch fix.
- `scripts/audit_prompt_library.py` — **deep audit** with the false-positive filters above: skill/tool/prompt dependency resolution, content-structure + safety scan, cross-prompt delegation map; writes `docs/` reports. Read-only except reports.
- `scripts/fix_prompt_library.py` — **deterministic frontmatter repair** (audit by default; pass `--apply` to mutate). Parses ONLY the YAML frontmatter, preserves the body byte-for-byte, rewrites frontmatter from the edited dict. Handles trigger/name sync, bidirectional DEPS==SKILLS, toolset normalization, MCP→`tool:` relabel, self-ref removal. `--all` or `--files a,b`.

## Verification Checklist
- [ ] Frontmatter validator returns "All prompt front-matter valid."
- [ ] Dry-run validator returns "All prompts passed dry-run validation."
- [ ] No prompt has a `name:` differing from its filename slug.
- [ ] No prompt has a `trigger:` diverging from `/<name>`.
- [ ] No prompt uses `triggers:` (plural) instead of `trigger:` (singular).
- [ ] No file ends in `.md` instead of `.prompt.md` (except non-prompt markdown).
- [ ] No toolset contains `search` (use `web` instead) or VS Code/CLI-specific entries.
- [ ] No MCP tools are listed with `skill:` prefix in `dependencies:` (use `tool:`)
- [ ] No MCP tools appear in the `skills:` section
- [ ] No prompt has a self-referencing `skill:` in `dependencies:`
- [ ] Every prompt with `tool:mcp-*` deps also has `- mcp` in `toolsets:`
- [ ] No body text references non-existent tools (e.g. dispatching-parallel-agents)
- [ ] `metadata.hermes.related_skills` in sync with corrected `dependencies:` prefix types
- [ ] No duplicate entries in `toolsets:` list
- [ ] Independent second verifier reports `TOTAL=N CLEAN=N WITH_ISSUES=0` (for 100+ files)
- [ ] If a repair list was regenerated: it was rerun from the actual workspace cwd, verified independently from the generator, and any temp verifier artifacts were removed.
- [ ] All changes Git-tracked (no backup files).
- [ ] If size reduction was performed: target-file sizes were measured before/after with an independent check; prompt content/behavior was preserved and not replaced with invented hidden-document text.
- [ ] If an orchestrator prompt was repaired: every referenced child prompt/template path was verified to exist, or explicit placeholders were created and re-verified.

## Assets
- **Reference**: `references/toolset-mapping.md` — full mapping table from VS Code/Copilot tool names to Hermes toolsets
- **Reference**: `references/large-library-maintenance-recipe.md` — 5-phase loop, duplicate-frontmatter + MCP-mislabel corruption fixes, and the independent-second-verifier pattern for 100+ prompt libraries
- **Reference**: `references/cross-prompt-delegation-and-domain-registry.md` — read-only delegation-edge extraction + stem-based domain classifier (avoids meta-tag pollution) for producing a prompt-registry.md without editing sources
- **Reference**: `references/repair-list-generation.md` — repair-list generator pitfalls and trusted regeneration workflow, including markdown path normalization, placeholder/glob filtering, independent verification, temp-artifact cleanup, and workspace-cwd rerun requirements.
- **Reference**: `references/prompt-size-targets.md` — size-target verification guidance for prompt reduction work, including acceptable range checks.
- **Reference**: `references/orchestrator-child-references.md` — orchestrator child-reference repair workflow, missing-path enumeration, placeholder authoring rules, and re-verification checklist for execute-all-prompts-style workflows.
- **Reference**: `references/missing-orchestrator-runner.md` — fallback behavior when the Hermes runtime lacks a direct prompt-runner subcommand for an orchestrator workflow.