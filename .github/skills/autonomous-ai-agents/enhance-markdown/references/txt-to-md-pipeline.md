# TXT → Markdown Conversion Mode

## When to Use

Triggered when `$1` is `--txt-to-md`. Converts raw `.txt` prompt files in `Prompts/` to structured `.md` via a two-step sequential pipeline: enhance (Stanford/Anthropic patterns) → apply 9-section template.

## Mode Detection

Check `$ARGUMENTS`:

- **Argument present after `--txt-to-md`** → single-file mode. Target list = the specified `.txt` file path.
- **No argument after `--txt-to-md`** → batch mode. Target list = all `.txt` files found in `Prompts/` (non-recursive, `*.txt` glob).

If batch mode and no `.txt` files are found in `Prompts/`, print:

```
No .txt files found in Prompts/. Nothing to do.
```

…and exit cleanly.

## Per-File Pipeline (Phases 1–5)

Run the following phases for each file in the target list. For a worked example, see `references/txt-to-md-example.md`.

### Phase 1 — Read

Read the full raw content of the target `.txt` file into context.

**Error**: If the file is unreadable, log `ERROR: Could not read <filename> — skipping.` and continue.

### Phase 2 — Enhance

1. Read `.opencode/commands/prompt-engineering-prompt-enhancer.md` into context (OpenCode only)
2. Apply Stanford/Anthropic patterns:
   - Critical rules in first 15% of the prompt
   - Nesting depth ≤ 4 levels
   - Instruction ratio 40–50%
   - Single source of truth (no rule repeated > 2×)
   - Explicit 3-tier prioritization (Safety → Core Workflow → Optimization)
3. Hold the **enhanced text** in context. Do NOT write files.

**Hermes fallback**: If the enhancer file doesn't exist, apply patterns directly from the skill spec.

### Phase 3 — Template

Apply the 9-section template to the enhanced text. Populate each section by extracting and restructuring — **do not invent content**.

**Section order (fixed):** `Skills → Subagents → Personas → Rules → Steps → Tasks → Subtasks → Actions`

Only include optional sections when detection rules match:

| Section | Include when... |
|---------|----------------|
| `Skills` | Prompt references tools, capabilities, or skill invocations |
| `Subagents` | Prompt involves delegation, parallel work, or specialist agents |
| `Personas` | Prompt defines a role, character, or identity for the AI |
| `Phases` | Workflow has 2+ distinct sequential stages |
| `Subtasks` | Any Task entry requires further decomposition |

**11-section variant:** For cross-system prompts (Hermes + Copilot + OpenCode), use the 11-section template in `references/cross-system-prompt-template.md` instead.

### Phase 4 — Write

Write templated output to `Prompts/<same-stem>.md`. Always overwrite.

### Phase 5 — Report

```
Refactor complete.
  Processed: <n>
  Failed:    <n>
  Total:     <n>
```

### Phase 6 — Cross-File Consistency Check

After all `.md` files written, run frontmatter consistency check across all newly created files AND peer `.prompt.md` files. Build field matrix, identify missing fields, report gaps. Apply fixes if gaps found, re-run to confirm zero gaps.

**Pitfall — large peer scopes:** For 50+ peer files, use `terminal("grep -rl '<ref>' <dir>")` instead of `search_files`.
