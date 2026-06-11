---
name: enhance-markdown
title: Enhance Markdown
trigger: /enhance-markdown
description: >
  Four-phase markdown auditor and enhancer. Catalogs related files, plans, and specs (two-way dependency map), audits for issues in parallel batches, creates a dual-channel-fix plan (plugin system + companion markdown), applies fixes progressively in batches of 7, then independently verifies the result. Fully resumable after interruption — each phase checks for existing artifacts before re-running work.

tags:
  [markdown, audit, enhance, idempotent, plans-and-specs, txt-to-md]
dependencies:
  - subagent:delegate_task (Hermes-native; OpenCode uses codebase-locator/analyzer/openagent/opencoder)
  - skill:plans-and-specs
  - skill:systematic-debugging
  - skill:writing-plans
  - skill:simplify
  - skill:verification-before-completion
---## Goal
Use when > to accomplish the associated tasks and objectives.


# enhance-markdown

## When to Use

- When working with enhance markdown tools or services
- When automating or managing enhance markdown tasks
- When troubleshooting enhance markdown configurations
- **Triggers**: "Enhance Markdown", "enhance markdown" related operations

## Description

`/enhance-markdown` is a four-phase markdown auditor and enhancer. It builds a two-way dependency catalog of the target file and all related files (Phase 1), creates a dual-channel fix plan (plugin system + companion markdown) and applies fixes in batches of 7 with Batch 1 as a proof-of-concept gate (Phase 2), executes any remaining plan items to completion (Phase 3), then independently verifies all fixes against the original issues list (Phase 4). Fully resumable — each phase checks for existing artifacts before re-running work.

---

## Usage

```bash
# Minimal — purpose derived from file frontmatter/first heading, fallback to filename
/enhance-markdown .opencode/commands/review.md

# Explicit purpose label — overrides inference
/enhance-markdown .opencode/commands/review.md review-command

# TXT → Markdown conversion mode (batch or single file)
/enhance-markdown --txt-to-md                    # batch all .txt in Prompts/
/enhance-markdown --txt-to-md Prompts/myprompt.txt  # single file
```

**Pre-Flight (mandatory — run before any phase):**

Before touching anything, clarify with the user when the target list contains 3+ files, or when artifact files from a prior run already exist:

1. **State the current situation** — which target files exist, which artifacts from prior pipeline runs are present
2. **Ask the user's intent** — resume from existing artifacts (the default per entry checks) or re-run everything fresh
3. **If re-run fresh requested:** skip all entry checks, acknowledge that previously-fixed files will audit clean, and proceed. Phase 2 becomes a no-op for clean files — produce empty fix plans and clean verification reports.
4. **If resume requested:** follow the normal entry check logic

> **Pitfall:** The entry checks assume resume-by-default. When the user says "fresh re-run", honour that over the resumability logic. Do not skip phases because artifacts exist.

**Arguments:**

- `$1` — path to the target markdown file (required for audit mode)
- `$2` — purpose label slug (optional; overrides automatic inference)
- `--txt-to-md` — switch to TXT→Markdown conversion mode (optional)

**Error — file not found:** If `$1` does not resolve to an existing file, first search the filesystem for the correct path (search_files or glob for likely candidates — e.g., correct a typo like `promptsupdate` → `prompts/update`). If a single match is found, use the corrected path and log the correction. If zero or multiple matches, then halt and output: `Error: file not found — {$1}`

**Purpose resolution** (resolved once at start, used for all artifact names):

| Priority | Source | Example result |
| --- | --- | --- |
| 1 | Explicit `$2` argument | `review-command` |
| 2 | Semantic slug from frontmatter/first heading | `code-review-standards` |
| 3 | Filename without extension | `review` |

Slug-ification: lowercase → spaces and `_` → `-` → strip non-alphanumeric (except `-`) → truncate at 40 chars.

**Artifact map:**

| Artifact | Written by | Description |
| --- | --- | --- |
| `docs/{purpose}-context.md` | Phase 1 | Two-way dependency catalog |
| `docs/{purpose}-issues-context.md` | Phase 1 | Audit findings |
| `thoughts/plans/{purpose}-debug.md` | Phase 2 | Companion plan markdown |
| `docs/{purpose}-fix-issues-context.md` | Phase 2 | Fix plan + progress log |
| `docs/{purpose}-verify-context.md` | Phase 4 | Verification report |

Plugin planning system also registers plan and specs under namespace `{purpose}-debug`.

---

## Context

- **Target**: a single `.md` file (`$1`), or `--txt-to-md` mode for batch `.txt` → `.md` conversion
- **Purpose slug**: derived from `$2`, frontmatter/heading, or filename — used to name all artifacts
- **Artifacts**: written to `docs/` and `thoughts/plans/`; never overwrite source files
- **Resumability**: every phase checks for its output artifact before running — safe to re-invoke after interruption
- **Plugin planning system**: used when reachable; companion markdown is the fallback
- **Batch size**: exactly 7 files per batch (Phases 1 and 2); Batch 1 is a proof-of-concept gate
- Session notes: see `references/txt-to-md-session-notes.md` for backup-and-verify lessons learned during TXT→Markdown conversions
- Reconstruction helper: see `references/phase1-reconstruction.md` for deterministic Phase 1 reconstruction steps when Phase 1 artifacts are missing but Phase 2/4 artifacts exist.
- **Platform mapping**: see `references/hermes-vs-opencode-platform-guide.md` for Hermes-specific agent mapping and plugin system fallback patterns
- **AI-readiness scoring**: see `references/ai-readiness-scoring.md` for the quantitative methodology to score every `.md` on AI consumption quality (YAML frontmatter, summary paragraphs, language-tagged code blocks, cross-reference resolution, heading density). Run after Phase 4 to produce `docs/ai-readiness-report.md`.
- **Doc symmetry validation**: see `references/doc-symmetry-validation.md` for validating a project's doc set against an expected manifest (e.g., the 11-artifact generator-orchestrator template). Run before Phase 6 to produce `docs/doc-symmetry-report.md`.
- **Audit detection edge cases**: see `references/audit-detection-edge-cases.md` for handling false positives in Phase 1 pipe-balance checks (shell code, YAML frontmatter with pipes) and verification-phase recovery patterns.
- **Prompt file debugging**: see `references/prompt-file-debugging-patterns.md` for the 5-bug taxonomy found when debugging structured `.prompts.md` files (count mismatches, broken table pipes, skills-list divergence, stage label collisions, contradictory conditionals), plus the pre-enhancement workflow checklist and generator context-loading order.

---

## Skills Required

| Skill | Purpose |
| --- | --- |
| `plans-and-specs` | Create and manage the fix plan and specs via plugin system |
| `systematic-debugging` | Audit files for formatting, content, and structural issues |
| `writing-plans` | Author the companion markdown fix plan |
| `simplify` | Ensure fix plan and added sections are concise and non-redundant |
| `verification-before-completion` | Independent re-read verification in Phase 4 |

---
## Subagents

| Subagent / Hermes Equivalent | Role | Phase | Platform |
| --- | --- | --- | --- |
| **Hermes Profiles** (specialized agents) | | | |
| `research-analyst` profile | Forward and reverse dependency scanning | Phase 1 | **Hermes** (profile) |
| `research-analyst` profile | Batch analysis of related files for issues | Phase 1 | **Hermes** (profile) |
| `code-architect` profile | Authoring fix plan; applying batched fixes | Phase 2/3 | **Hermes** (profile) |
| `exec-assistant` profile | Agent readiness check; Phase 3 fix execution | Phases 2, 3 | **Hermes** (profile) |
| **Legacy Delegation** (fallback) | | | |
| `delegate_task(goal="...", toolsets=["file","search_files"])` | Forward and reverse dependency scanning | Phase 1 | **Hermes** (native) |
| `delegate_task(goal="...", toolsets=["file","search_files","terminal"])` | Batch analysis of related files for issues | Phase 1 | **Hermes** |
| Agent readiness check via `skills_list` or `hermes skills list` | Verify plans-and-specs availability | Phase 2 | **Hermes** |
| `delegate_task(goal="...", toolsets=["file","patch"])` | Authoring fix plan; applying batched fixes | Phase 2/3 | **Hermes** |
| **OpenCode Agents** | | | |
| `codebase-locator` | Forward and reverse dependency scanning | Phase 1 | **OpenCode** (agent-based) |
| `codebase-analyzer` | Batch analysis of related files for issues | Phase 1 | **OpenCode** |
| `openagent` | Agent readiness check; Phase 3 fix execution | Phases 2, 3 | **OpenCode** |
| `opencoder` | Authoring fix plan; applying batched fixes | Phase 2, 3 | **OpenCode** |

**Runtime platform detection:**

At skill invocation, the enhance-markdown controller detects the execution context:

- **Hermes context** (this skill invoked via CLI `hermes` or chat) → use specialized Hermes profiles:
  - Phase 1: `research-analyst` profile (data synthesis, dependency scanning)
  - Phase 2-3: `code-architect` profile (system design, fix application)
  - Phase 2-3: `exec-assistant` profile (orchestration, readiness checks)
  - Fallback: `delegate_task` with Hermes toolsets if profiles unavailable
  - Tool-limit fallback: `execute_code` (Python with `from hermes_tools import ...`) if `delegate_task` fails with "array too long" / tool count exceeds provider limit. `execute_code` is a single tool that bundles `file`, `search_files`, `terminal`, `write_file`, `patch` — sidesteps the 128-tool cap. Use for Phase 1 dependency scanning, batch reading, and issue detection when delegate_task is blocked.
- **OpenCode context** (invoked via `opencode` CLI) → use OpenCode agent names directly

The dual-channel plan (plugin system + companion markdown) remains consistent across both platforms.

**Profile Usage Pattern:**

```bash
# Phase 1 — Dependency scanning and audit
research-analyst chat "Scan dependencies for {file} and audit related files"

# Phase 2 — Fix planning and application
code-architect chat "Create fix plan for issues in {purpose}-issues-context.md"
code-architect chat "Apply Batch 1 fixes (proof-of-concept)"

# Phase 3 — Orchestration and completion
exec-assistant chat "Execute remaining plan items from {purpose}-debug"

# Phase 4 — Verification
code-architect chat "Verify all fixes against original issues"
```

---

## Hermes Prompt Normalization Mode

Use this mode when the target is an existing prompt family that should be rewritten into a stricter Hermes-friendly structure.

### Preferred structure for shared prompts

When converting or normalizing prompts for cross-system use, prefer a compact, explicit structure:

- `Goal`
- `Context`
- `Inputs`
- `Outputs`
- `Rules`
- `Phases`
- `Actions Summary`

Keep the workflow readable without long introductory prose. Preserve the original intent, but remove redundant or conflicting instructions.

For a session-derived normalization checklist and examples, see `references/hermes-prompt-normalization.md`.

## TXT → Markdown Conversion Mode

Triggered when `$1` is `--txt-to-md`. Converts raw `.txt` prompt files in `Prompts/` to structured `.md` via a two-step sequential pipeline: enhance (Stanford/Anthropic patterns) → apply 9-section template.

### Mode Detection

Check `$ARGUMENTS`:

- **Argument present after `--txt-to-md`** → single-file mode. Target list = the specified `.txt` file path.
- **No argument after `--txt-to-md`** → batch mode. Target list = all `.txt` files found in `Prompts/` (non-recursive, `*.txt` glob).

If batch mode and no `.txt` files are found in `Prompts/`, print:

```
No .txt files found in Prompts/. Nothing to do.
```

…and exit cleanly.

### Per-File Pipeline (Phases 1–5)

Run the following phases for each file in the target list. For a worked example of the full pipeline applied to a real file, see `references/txt-to-md-example.md` (before/after with template application notes and common pitfalls).

#### Phase 1 — Read

Read the full raw content of the target `.txt` file into context.

**Error**: If the file is unreadable, log:

```
ERROR: Could not read <filename> — skipping.
```

Increment the failed count and continue to the next file.

#### Phase 2 — Enhance

1. Read `.opencode/commands/prompt-engineering-prompt-enhancer.md` into context.
2. Apply its enhancement instructions **inline** to the raw content from Phase 1 — the enhancer applies Stanford/Anthropic patterns:
   - Critical rules positioned in the first 15% of the prompt
   - Nesting depth ≤ 4 levels
   - Instruction ratio 40–50%
   - Single source of truth (no rule repeated > 2×)
   - Explicit 3-tier prioritization (Safety → Core Workflow → Optimization)
3. Hold the **enhanced text** in context. Do NOT write any files at this stage.

**Error**: If the enhancer produces empty or clearly invalid output, log:

```
WARNING: Enhancer returned empty output for <filename> — skipping.
```

Increment the failed count and continue.

**Note**: The enhancer path `.opencode/commands/prompt-engineering-prompt-enhancer.md` is project-specific (OpenCode environments). In Hermes, this file may not exist — fall back to applying the Stanford/Anthropic patterns directly from the skill spec (critical rules in first 15%, nesting ≤4, 40-50% instruction ratio, single source of truth, 3-tier prioritization). Companion markdown is always written regardless of platform.

#### Phase 3 — Template

Apply the 9-section template below to the enhanced text from Phase 2. Populate each section by extracting and restructuring content from the enhanced text — **do not invent content**. Every populated section must trace back to something in the enhanced text.

**11-section variant:** For prompts that need to work across Hermes, Copilot, and OpenCode (cross-system commands), use the 11-section template documented in `references/cross-system-prompt-template.md` instead of the 9-section template below. The 11-section variant adds YAML frontmatter, Description, and Context sections, with Steps/Tasks/Subtasks nested inside each Phase — required for OpenCode `trigger:` compatibility and multi-agent discoverability.

**When to choose:**
| Scenario | Template |
| --- | --- |
| Simple internal workflow prompt | 9-section |
| Shared command invoked from OpenCode CLI | 11-section |
| Prompt needs to work in Hermes + Copilot + OpenCode | 11-section |
| Quick one-off task, no cross-system needs | 9-section |

##### Section order (fixed)

`Skills → Subagents → Personas → Rules → Steps → Tasks → Subtasks → Actions`

Only include a section if it passes its detection rule (see table below). Absent optional sections are omitted entirely. The 4 core sections are always present.

##### Core 4 — always present

```
## Rules
- <constraint or behavioral guardrail extracted from the enhanced text>

## Steps
1. <high-level ordered step>

## Tasks
- [ ] <discrete actionable unit of work>

## Actions
- `<tool or command>` — <what it does in this context>
```

If the enhanced text genuinely has nothing applicable for a core section, write `- N/A` rather than leaving it empty.

### Optional 5 — include when detection rules match

```
## Skills
- `<skill-name>` — <why it applies to this prompt>

## Personas
> <role definition / identity the AI adopts when running this prompt>

## Phases
### Phase 1: <name>
<what happens in this phase>

## Subtasks
- [ ] <sub-unit of a parent Task>
```

### Detection rules for optional sections

| Section | Include when... |
| --- | --- |
| `Skills` | Prompt references tools, capabilities, or skill invocations |
| `Subagents` | Prompt involves delegation, parallel work, or specialist agents |
| `Personas` | Prompt defines a role, character, or identity for the AI |
| `Phases` | Workflow has 2+ distinct sequential stages |
| `Subtasks` | Any Task entry requires further decomposition |

#### Phase 4 — Write

Write the templated output from Phase 3 to `Prompts/<same-stem>.md`. Always overwrite if the file already exists.

- **Same-stem rule**: `Prompts/myprompt.txt` → `Prompts/myprompt.md`

**Error**: If the write fails, log:

```
ERROR: Could not write <output-filename>.
```

Increment the failed count and continue.

#### Phase 5 — Report (runs once, after all files complete)

Print:

```
Refactor complete.
  Processed: <n>
  Failed:    <n>  (see errors above)
  Total:     <n>
```

#### Phase 6 — Cross-File Consistency Check (runs once, after all files written)

After all `.md` files are written and before the final report, run a frontmatter consistency check across all newly created `.md` files AND any peer `.prompt.md` files in the same scope (e.g., `.github/prompts/`). This catches gaps that individual-file verification misses — e.g., one file missing `dependencies:` while all peers have it.

**Scope:** All `.md` files written in Phase 4, plus any peer `.prompt.md` files under the shared scope directory.

**Procedure:**

1. **Collect frontmatter** — For each file in scope, parse the YAML frontmatter between the first `---` delimiters. Extract the set of top-level keys present (trigger, description, tags, dependencies, skills, etc.).

2. **Build field matrix** — Map each file to the set of fields it has. The matrix reveals which fields are universal, which are common (present in most files), and which are unique to specific files.

3. **Identify missing fields** — For each file, flag fields that are present in ALL peer files but missing from this one. Example: if all `.github/prompts/*.prompt.md` files have `dependencies:` and `skills:`, but `convert-plaintext-to-md.prompt.md` does not.

4. **Report gaps** — Append to the Phase 5 output:
   ```
   Cross-file consistency check:
     Files checked:      <n>
     Fields compared:    <list>
     Gaps found:         <n>
     [If gaps] Fix required:
       - <filename>: missing <field1>, <field2>
   ```

**Action on gaps:** If gaps are found, the agent SHOULD apply fixes (add missing fields) before declaring the pipeline complete. Re-run Phase 6 after fixes to confirm zero gaps.

**Error handling:** If frontmatter parsing fails for any file (malformed YAML, missing `---` delimiters), log the filename and continue — one bad parse should not block the check for other files.

**Cross-reference audit (optional, run when requested):** After the field-matrix check, audit all files for a required cross-reference (e.g., `.github/prompts/context-map`). For each file, check whether the reference appears in dependencies, skills, or body text. Report:

```txt
Cross-reference audit for {ref}:
  Files checked:      <n>
  Files with ref:     <n>
  Files missing ref:  <n>
    - <filename>
```

**Action on missing cross-refs:** Add the reference to each file's `dependencies:` YAML field as `- command:/{ref}` and to the `Skills` or body section. The format is:
- In YAML frontmatter: `- command:/{ref}` under `dependencies:`
- In markdown body: a table row or bullet under the Skills/Phases section

Only flag cross-refs that are genuinely universal across peer files — don't add to files where the ref is semantically irrelevant (e.g., context-map doesn't need to reference itself).

**Pitfall — field universality:** Only flag fields that are genuinely universal across peer files. A field present in only 3 of 6 peers is a style variation, not a gap. The signal is a field present in ALL peer files but absent from one.

**Pitfall — large peer scopes:** When the peer scope contains 50+ files (e.g., `.github/prompts/` with 100+ `.prompt.md` files), Phase 6's field-matrix check across all peers is impractical. In execute_code, `search_files` from `hermes_tools` throws `JSONDecodeError` on large result sets. Two practical alternatives:
- Run the field-matrix check only against the newly-created/enhanced files (the ones Phase 4 just wrote). Skip broad peer-scanning — the peers are already mature and the signal is in the new files matching the established pattern.
- For cross-reference audits, use `terminal("grep -rl '<ref>' <dir>")` instead of `search_files` — reliable at any scale.
- For counting, use `terminal("ls <dir>/*.ext | wc -l")` instead of `search_files` with `target='files'`.

---

## Phase 1 — Catalog & Audit

**@analyst** runs this phase.

### Entry Check

```
IF docs/{purpose}-issues-context.md EXISTS → Phase 1 complete, skip to Phase 2
ELSE IF docs/{purpose}-context.md EXISTS  → catalog exists, skip to Step 1.3
ELSE                                       → run full Phase 1
```

### Step 1.1 — Purpose Resolution

Resolve `{purpose}` using cascading priority:

1. `$2` argument if provided
2. Slug from file's frontmatter `description` or first `# heading` — lowercase, spaces/`_` → `-`, strip non-alphanumeric except `-`, truncate at 40 chars
3. Filename without extension

Use the resolved `{purpose}` for all artifact names in this and subsequent phases.

### Step 1.2 — Two-Way Dependency Scan

**Forward scan** (what the file references):

- Extract all markdown links `[text](path)` pointing to `.md` files
- Extract all `@agent-name` mentions
- Extract all `/command-name` trigger references
- Extract all plan/spec namespace slugs (patterns like `{slug}-debug`, `{slug}-context`)
- Query plugin system (`readPlan`) for matching namespaces

**Reverse scan** (what references this file):

- `grep` all `.md` files in `.opencode/` and `docs/` for this file's path, filename, and trigger
- Query plugin system for plans/specs that reference this file by name

**Write `docs/{purpose}-context.md`:**

```markdown
# {purpose} — Context Catalog

Generated: {date} Source file: {path}

## Summary

{2-3 sentence description of the file's role and relationships}

## Forward References (this file → others)

| Type | Reference | Path | Exists? |
| ---- | --------- | ---- | ------- |

## Reverse References (others → this file)

| Type | Source File | Reference | Context snippet |
| ---- | ----------- | --------- | --------------- |

## Plans & Specs (plugin system)

| Namespace | Type | Status | Linked to source? |
| --------- | ---- | ------ | ----------------- |
```
