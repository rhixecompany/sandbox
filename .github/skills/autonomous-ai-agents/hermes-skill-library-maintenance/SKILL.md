---
name: hermes-skill-library-maintenance
title: "Hermes Skill Library Maintenance"
description: "Audit, plan, and execute large-scale fixes to Hermes skill definitions (metadata, formatting, content). Multi-phase workflow for bulk patching."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [hermes, skills, maintenance, audit, bulk-patching, metadata]
metadata:
  hermes:
    tags: [imported]
---
# Hermes Skill Library Maintenance

## Overview

Audit, plan, and execute large-scale fixes to Hermes skill definitions. Multi-phase workflow for bulk patching.

## Skills Required

| Skill | Purpose |
|-------|---------|
| `skill-creator` | Create and validate new skills |
| `skill-judge` | Audit skills against quality criteria |
| `writing-skills` | Write clear skill prose |
### Phase 1: Preparation

- Understand the context and requirements.
- Gather necessary tools and resources.

### Phase 2: Execution

- Perform the core actions required by the skill.
- Apply the techniques and procedures outlined.

### Phase 3: Verification

- Verify the results against the expected outcomes.
- Confirm that the task has been completed successfully.


## Overview

Large-scale maintenance workflows for Hermes skill library — auditing metadata, identifying inconsistencies, planning fixes, and executing bulk patches across 100+ skills. This skill captures the 4-phase audit → plan → execute → verify pattern.

## When to Use

- Auditing skill library for metadata gaps (missing title, description, empty body)
- Planning large-scale skill fixes (100+ files affected)
- Executing bulk metadata patches (title derivation, frontmatter standardization)
- Verifying fix success across entire library
- Generating audit reports and fix documentation

## Prerequisites

- Access to Hermes skills directory: `~/.hermes/skills/` (or `%APPDATA%\Local\hermes\skills\` on Windows)
- Python 3.11+ for bulk file processing
- Terminal/shell for scripting and verification
- No external API keys required (filesystem-only)

---

## Multi-Phase Pattern: Audit → Plan → Execute → Verify

This skill uses a 4-phase workflow for any large-scale skill maintenance task:

1. **Phase 1 (Audit & Debug):** Identify all issues, generate report
2. **Phase 2 (Plan Implementation):** Structure fixes, create patch specifications  
3. **Phase 3 (Execute Fix):** Apply patches with safety gates and verification
4. **Phase 4 (Verification):** Confirm success, generate certification report

Each phase produces **artifacts** (markdown reports, JSON mappings, execution prompts) that feed into the next phase. This separation enables review checkpoints and rollback.

---

## Phase 1: Audit and Debug

**Goal:** Scan all skills, identify inconsistencies, generate audit report.

### Steps

1. **Inventory all skills**
   ```python
   from pathlib import Path
   skills_dir = Path("~/.hermes/skills")  # Unix
   # OR on Windows:
   skills_dir = Path("C:/Users/YourName/AppData/Local/hermes/skills")
   
   skill_files = sorted(skills_dir.rglob("SKILL.md")) + sorted(skills_dir.rglob("DESCRIPTION.md"))
   total = len(skill_files)
   print(f"Total skill files: {total}")
   ```

2. **Scan each skill for structural completeness** (all 5 sections)
   ```python
   required_sections = [
       "frontmatter",       # opens with ---
       "when_to_use",       # ## When to Use
       "workflow",          # ## Workflow | Process | Pipeline | Phases
       "checklist",         # ## Verification Checklist
       "best_practices",    # ## Best Practices
   ]
   missing = []
   for section_name, pattern in required_sections:
       if not re.search(pattern_rules[section_name], content, re.MULTILINE):
           missing.append(section_name)
   ```
   - Check frontmatter: opens with `---`, has closing `---`
   - Check When to Use: `## When to Use` heading present
   - Check Workflow: `## Workflow` (or Process/Pipeline/Phases) heading present
   - Check Verification Checklist: `## Verification Checklist` heading present
   - Check Best Practices: `## Best Practices` heading present
   - Categorize by directory

3. **Triage results**
   - Count missing titles (usually 90%+ in unmaintained libraries)
   - Identify parse errors (malformed frontmatter)
   - Note empty bodies (can be patched but flag for review)
   - Group by category for batch planning

4. **Bare header scan** — Common issue in skills with minimal frontmatter
   ```bash
   # Scan for bare section headers (text that should be ## or #)
   cd ~/AppData/Local/hermes/skills
   grep -rn '^Description$' --include='SKILL.md' .
   grep -rn '^Overview$' --include='SKILL.md' .
   grep -rn '^Purpose$' --include='SKILL.md' .
   grep -rn '^References$' --include='SKILL.md' .
   grep -rn -E '^(When to use|When to load|Core policies|Key principles)$' --include='SKILL.md' .
   grep -rn -E '^Files & scripts$' --include='SKILL.md' .
   ```
   Skills can be classified into two patterns:
   - **Type A** (minimal frontmatter: `name:`, `title:`, `description:` only) — consistently has bare `Description` header at line 8. Fix: `## Description`.
   - **Type B** (rich frontmatter: `version:`, `author:`, `license:`, `metadata:` present) — consistently has correct `# Name` and `## Section` headers.

5. **Classifier for found issues** — Categorize each formatting defect using the 4-category scheme discovered during real skills-fix execution:
   ```
   Category A — Bare header missing `#`
     e.g. "Description" instead of "## Description"
           "Overview" instead of "## Overview"
           "Purpose" / "References" / "When to use" / "Core policies" / "Files & scripts"
     Fix:   Prepend `## ` to each bare line. Verify with grep after fix.
     Trap:  The patch tool's fuzzy matching may truncate content after bare headers —
            always include the FULL text of the block being replaced, not a prefix.
            Verify file content integrity after each patch.

   Category B — Wrong header level
     e.g. `## Template Skill` instead of `# Template Skill`
     Fix:   Change `## ` to `# ` (or vice versa depending on the hierarchy).
     Trap:  Only the top-level title (`# Name`) should be H1. All sections should be `##`.

   Category C — Duplicate content
     e.g. Double `## Overview` section appearing at two different locations in the same file
     Fix:   Deduplicate — keep the richer version, remove the duplicate.
     Trap:  Read both copies fully before deleting; they may have different content.
            Merge unique content from both, then remove one.

   Category D — Potential cross-directory duplicates
     e.g. skills/humanizer/ (root, 79 lines, bare frontmatter, 2KB)
          vs skills/creative/humanizer/ (624 lines, rich frontmatter, 32KB, has LICENSE)
     Action: Compare content, frontmatter depth, and reference files.
             The richer version is authoritative — merge the smaller into it,
             then delete the smaller directory.
     Trap:  Check both for reference files (references/ subdirectories) before merging.
            Copy unique reference files (+LICENSE) into the authoritative directory.
   ```

6. **Duplicate detection sweep** — After fixing bare headers, sweep for same-name skills across directories:
   ```python
   from collections import defaultdict
   from pathlib import Path
   skills_by_name = defaultdict(list)
   for path in Path(skills_dir).rglob("SKILL.md"):
       name = path.parent.name.lower()
       skills_by_name[name].append(path.parent)
   for name, dirs in sorted(skills_by_name.items()):
       if len(dirs) > 1:
           print(f"DUPLICATE NAME: {name}")
           for d in dirs:
               size = (d / "SKILL.md").stat().st_size
               print(f"  {d}  ({size} bytes)")
   ```
   The richer version (larger size, richer frontmatter with version/license/metadata) is authoritative. Merge the smaller into it, never the reverse.

7. **Generate audit report** (Markdown)
   - Executive summary: counts + percentages
   - Breakdown by category
   - Detailed issue lists (grouped by issue type)
   - Export issue mapping to JSON for next phase

### Expected Output

```
Total skills: 176
Frontmatter: 176/176 (100%)   PASS
When to Use: 176/176 (100%)   PASS
Workflow:    176/176 (100%)   PASS
Checklist:   176/176 (100%)   PASS
Best Pracs:  176/176 (100%)   PASS
═════════════════════════════════════
ALL PASS — 176 skills structurally complete
```

---

## Phase 2: Plan Implementation

**Goal:** Design fix strategy, generate patch commands.

## Phase 3: Execute Fixes

**Goal:** Apply all patches. Execute in batches with progress tracking and safety gates.

### Safety Gates (MUST check before executing)

Before starting Phase 3, establish these guardrails:

1. **Active Task Protection**
   ```bash
   # Query: which skills are currently in use?
   hermes tasks list --active
   # If any target skills appear in active tasks, schedule maintenance for later
   ```

2. **Git Checkpoint**
   ```bash
   # Ensure clean state for rollback
   git status  # Must be clean
   git commit -am "pre-skills-fix: checkpoint"  # Or stash changes
   ```

3. **Dependency Graph**
   - Before patching skill X, check if other skills import/reference it
   - Document which skills call which (e.g., `dispatching-parallel-agents` ← `subagent-driven-development`)
   - Tag commits with skill-dependency info if circular or tightly coupled

4. **Rollback Plan**
   ```bash
   # Before Phase 3 starts, document recovery:
   git tag SKILL-FIX-{DATE}-PRE-PATCH
   # During: patches via skill_manage(action='patch')
   # If error: git checkout HEAD -- ~/.hermes/skills/{skill}/SKILL.md
   ```

## Phase 4: Verification

**Goal:** Confirm all fixes applied correctly. Certify library.

## Pitfalls & Prevention

### Pitfall 0: Skipping Phase 1 (Audit)

**Problem:** Attempting to fix skills without understanding the scope. Creates plan for wrong problem. Patches are ineffective or miss issues.

**Prevention:** Always execute Phase 1 completely before Phase 2. Generate audit report artifact. Review it before committing to fixes.

### Pitfall -1: `hermes skills inspect/check/audit` Only Works for Hub-Installed Skills

**Problem:** Running `hermes skills inspect <name>`, `hermes skills check`, or `hermes skills audit` on local or builtin skills returns "No skill found" or "No hub-installed skills to check" — these commands only operate on skills installed via `hermes skills install` from the hub.

**Symptom:** You run `hermes skills check` expecting validation of all local/builtin skills and get "No hub-installed skills to check." Zero issues reported but no validation actually ran.

**Prevention:** For local/builtin skills, inspect by reading `SKILL.md` files directly from `~/AppData/Local/hermes/skills/<name>/SKILL.md` using `read_file` or terminal-based `grep`/`os.walk`. The `hermes skills list` command IS useful for inventory (shows all enabled skills), but the validation commands only cover hub-installed skills.

### Pitfall -2: Patch Tool String Truncation on Fuzzy Match

**Problem:** The patch tool uses fuzzy string matching. When `old_string` includes text from the file but `new_string` doesn't include the FULL replacement for every character the fuzzy matcher consumed, the result is silently truncated — content after the match point is replaced with only what `new_string` provides.

**Symptom:** You patch a "Description" block but the full description text is gone — replaced by only the first few words. The fuzzy matcher consumed more context than your new_string provided.

**Prevention:**
1. Always include the **full text** of the content block being replaced, not a prefix.
2. After every patch, verify the file to confirm content integrity.
3. If you discover truncation, re-patch the truncated text with the full version.
4. For large blocks, use very specific `old_string` that includes unique surrounding context before the replacement point, keeping the text after the replacement point minimal in both old and new strings.

### Pitfall 1: No Artifacts Between Phases

**Problem:** Skills directory path differs between Windows and Unix. Hardcoding `/home/user/.hermes/skills` breaks on Windows.

**Prevention:**
```python
from pathlib import Path
home = Path.home()
skills_dir = home / ".hermes" / "skills"  # Works on both
```

### Pitfall 2: Empty Frontmatter or Missing Closing Delimiter

**Problem:** Some skills have malformed frontmatter (missing `---`, truncated YAML). Extraction breaks silently.

**Prevention:**
```python
fm_end = content.find('\n---\n', 4)
if fm_end == -1:
    print(f"ERROR: {skill_file} has malformed frontmatter")
    continue
```

### Pitfall 3: Batch Size Too Large

**Problem:** 100 patches in one pass risks OOM. Too small batches are inefficient.

**Prevention:** Use batch size 30-50. For 185 skills: 6-7 batches of 25-30 = optimal.

### Pitfall 4: Not Preserving Existing Valid Data

**Problem:** Overwriting files that already have `title:` with auto-derived title (wrong).

**Prevention:**
```python
if 'title:' in fm_text:
    print(f"Skipping {skill_name} (already has title)")
    continue
```

### Pitfall 5: No Audit Before Execution

**Problem:** Discovering issues mid-patch. No rollback plan.

**Prevention:** Always Phase 1 (audit) before Phase 3 (execute). Generate reports + JSON. Version all artifacts.

### Pitfall 6: Tool Call Limit Causes Silent Read Failures in execute_code

**Problem:** Using `hermes_tools.read_file(path, limit=N)` from inside an `execute_code` block hits the 50-tool-call-per-block limit silently. After ~49 `read_file` calls, subsequent calls return empty content *without error*. This makes well-structured skills appear "empty" or "missing sections" — a bulk fixer that then adds generic sections will inject boilerplate into perfectly good skills, corrupting them.

**Symptom:** Well-structured skills (with frontmatter, When to Use, Workflow, Checklist) appear in the audit as "empty" or "score 0" after the 50th read. The fixer adds generic sections on top of existing content.

**Prevention:**
```python
# Prefer terminal-based Python scripts for bulk reads (no tool call limit)
# instead of hermes_tools.read_file inside execute_code blocks:

import os, subprocess
skills_dir = "C:/Users/Alexa/AppData/Local/hermes/skills"
for root, dirs, files in os.walk(skills_dir):
    if "SKILL.md" in files:
        path = os.path.join(root, "SKILL.md")
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        # Always read the full file — no limit parameter needed
```

**Recovery:** If generic sections were injected, sweep for them:
```bash
find skills -name 'SKILL.md' -exec grep -l 'Prerequisites are verified' {} \;
# Then strip the generic sections using regex removal
```

### Pitfall 7: Generic Section Injection from Incomplete Reads

**Problem:** Automated fixers that add missing "When to Use", "Workflow", "Checklist", or "Overview" sections based on partial `read_file` results (see Pitfall 6) inject generic boilerplate into already-complete skills. The injected sections are obviously auto-generated (generic checklist items, placeholder workflows, path references in broken format like `Skills\\product\\name\\skill.md`).

**Prevention:**
1. Always verify a skill is truly missing sections by reading the FULL file — not truncated by tool call limits
2. Never blindly add sections based on audit results from incomplete reads
3. After any bulk fix pass, ALWAYS sweep for contamination:
   ```bash
   find skills -name 'SKILL.md' -exec grep -l 'Prerequisites are verified' {} \;
   find skills -name 'SKILL.md' -exec grep -l 'operations completed without errors' {} \;
   find skills -name 'SKILL.md' -exec grep -l 'Document outcomes and store any configuration' {} \;
   find skills -name 'SKILL.md' -exec grep -l 'skill provides tools and workflows for managing' {} \;
   ```
4. Zero contamination is the only acceptable result before moving to the next phase.

### Pitfall 8: Windows Path Separators in os.walk

**Problem:** On Windows, `os.walk()` returns paths with backslashes (`skills\\creative\\p5js\\SKILL.md`). Code that does `.replace("/SKILL.md", "")` to extract the skill name will fail silently because the path has backslashes, not forward slashes.

**Symptom:** `find` commands that search by category show all results under a single bucket. Name extraction produces wrong values.

**Prevention:**
```python
# Always normalize paths when extracting skill names on Windows:
name = os.path.relpath(os.path.dirname(path), skills_base).replace("\\", "/")
# This produces "creative/p5js" regardless of os.walk's path separator
```

### Pitfall 9: Overwriting Well-Structured Skills

**Problem:** The most dangerous anti-pattern in bulk fixing: detecting a section as "missing" (due to truncation issues or strict pattern matching) and adding a generic version overwrites the skill's carefully crafted content. Once written, the original content is lost.

**Signs you're about to do this:**
- The audit score for a known-good skill (like systematic-debugging) is very low
- Many "empty" or "score 0" results from skills you know have rich content
- Your fixer is adding sections that sound generic ("Prerequisites are verified", "operations completed without errors")

**Prevention:** Before any bulk fix pass, spot-check 3-5 skills flagged as "missing" by the audit. Confirm they actually lack the section. If the audit is wrong, fix the audit logic before proceeding with fixes.

### Pitfall 10: MSYS/git-bash `find -exec grep` Is Unreliable on Windows

**Problem:** Running `find skills -name 'SKILL.md' -exec grep -l '^## When to Use' {} \;` from MSYS/git-bash (Windows) produces false negatives. Path encoding, line-ending differences, and MSYS path translation cause files that actually contain the pattern to be reported as missing. The error is silent — no files appear missing, but the count is always lower than reality.

**Symptom:** An audit reports "22 missing When to Use" but spot-checking those 22 files shows they have `## When to Use` perfectly intact. The `find -exec grep` approach is the root cause.

**Prevention:**
```python
# Use Python os.walk with direct file I/O instead of find -exec grep
import os, re
skills_dir = "C:/Users/YourName/AppData/Local/hermes/skills"
for root, dirs, files in os.walk(skills_dir):
    if "SKILL.md" in files:
        path = os.path.join(root, "SKILL.md")
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        has_section = bool(re.search(r"^## Verification Checklist", content, re.MULTILINE))
```

The reusable `scripts/skills-structural-audit.py` script uses `os.walk` and direct file I/O — run it instead of shell pipelines for reliable results.

**Recovery:** If find-based counts misled you into adding sections to skills that already had them, use the contamination sweep in `references/generic-boilerplate-markers.md` to detect and strip the injected boilerplate.

### Pitfall 12: `metadata.hermes.tags` vs Top-Level `tags` False Positive

**Problem:** Many Hermes skills store tags under `metadata.hermes.tags:` (nested YAML) instead of a top-level `tags:` field. Both are valid conventions — Hermes reads both at load time. But audit scripts that only check for `tags:` at the top level flag these skills as "missing tags" — a false positive that inflates issue counts and wastes time.

**Symptom:** Audit reports 50+ skills "missing tags" but spot-checking shows they have `metadata.hermes.tags:` with rich categories. The audit was only looking for `tags:` at the document root.

**Prevention:**
```python
# Check both locations:
fm = yaml.safe_load(frontmatter_text)
has_tags = (
    "tags" in fm and fm["tags"] is not None       # top-level
    or "metadata" in fm and isinstance(fm["metadata"], dict)
    and "hermes" in fm["metadata"]
    and "tags" in fm["metadata"]["hermes"]        # nested
)
```

**Detection:** If the audit counts "missing tags" at > 30% of the library, run this sweep:
```bash
python3 -c "
import os, yaml
skills_dir = os.path.expanduser('~/.hermes/skills/')
both, top_only, nested_only, neither = 0, 0, 0, 0
for root, dirs, files in os.walk(skills_dir):
    if 'SKILL.md' not in files: continue
    with open(os.path.join(root, 'SKILL.md')) as f:
        parts = f.read().split('---', 2)
    if len(parts) < 3: continue
    fm = yaml.safe_load(parts[1]) or {}
    top = 'tags' in fm
    nested = 'metadata' in fm and isinstance(fm['metadata'], dict) and 'hermes' in fm['metadata'] and 'tags' in fm['metadata']['hermes']
    if top and nested: both += 1
    elif top: top_only += 1
    elif nested: nested_only += 1
    else: neither += 1
print(f'both: {both}, top-level only: {top_only}, nested only: {nested_only}, neither: {neither}')
"
```
If `nested_only` is large, the audit is producing false positives.

**Recovery:** Re-run the audit with a check that accepts either form, or run the sweep above as a post-audit sanity check before reporting totals.

### Pitfall 15: `skill_manage` Delete Archives, Doesn't Remove

**Problem:** `skill_manage(action='delete', absorbed_into='umbrella')` rewrites the SKILL.md with an ARCHIVED header and pointer — the directory and file still exist. It does NOT delete the directory. Future `skills_list` calls still count it.

**Prevention:** If you truly need a skill gone (not just archived), use `rm -rf` directly for the thin stubs. Reserve `skill_manage(action='delete')` for skills that should remain as archived pointers.

### Pitfall 16: `skill_manage` Can't Resolve Some Paths

**Problem:** `skill_manage` fails to find skills under `software-development/` when referenced by bare name (e.g., `software-development/simplify`). It also fails for skills that exist both at root and in subdirectories if the root one is found first.

**Prevention:** For `software-development/` skills, either:
1. Use `rm -rf` directly if the skill is a thin stub you're deleting
2. Use the exact bare name and verify which one was resolved by checking the file on disk afterward
3. Always verify with `ls ~/.hermes/skills/<path>/SKILL.md` after any delete to confirm the right target was hit

### Pitfall 17: Post-Patch `skill_view()` Is Stale (reprise)

**Reminder:** After any `skill_manage(action='patch')` or `write_file`, calling `skill_view()` returns cached content from session start. Always verify patches with `read_file(path=...)` or terminal `head`. This pitfall has been recorded before but bears repeating — it bites every session.

**Problem:** After patching a SKILL.md with `skill_manage(action='patch')` or any other method, calling `skill_view(name)` returns the content as it was at session start — NOT the updated version. The skill content is loaded into memory at session initialization and not refreshed. This means verification like "confirm the fix applied correctly" will show old content and you'll think the patch failed.

**Symptom:** You patch "Description" → "## Description", then call `skill_view()` and see "Description" still there. You re-patch. It still shows the old value. You're stuck in a loop.

**Prevention:** Never use `skill_view()` to verify a patch that was applied in the same session. Instead, read the file directly:
```bash
# After patching, verify the file on disk:
head -30 ~/AppData/Local/hermes/skills/<name>/SKILL.md
# OR use read_file tool:
read_file path="~/AppData/Local/hermes/skills/<name>/SKILL.md" limit=30
```
The disk file IS updated — only the skill_view() cache is stale. A new session (/reset or next hermes invocation) will load the fresh content.

### Pitfall 14: Verification-Only Skills with No Routines

**Problem:** Some Hermes skills contain only verification/checklist sections with no actionable workflows (no step-by-step procedures, no commands, no troubleshooting). These are "read-only checklists" — they say what to verify but not how to do the work. They occupy cognitive space and session overhead without providing execution value.

**Symptom:** A skill that lists "Prerequisites and environment are properly configured" as a checklist item but provides zero instructions on HOW to configure the prerequisites. Loading this skill adds 50+ lines of context with no executable value.

**Action:** When encountering these, consider whether to:
1. Add workflow sections (converting checkboxes to procedures)
2. Mark for consolidation into a parent umbrella skill
3. If the skill has no unique content beyond the boilerplate, note it for potential pruning

**Detection:**
```bash
grep -l 'Prerequisites and environment are properly configured' ~/AppData/Local/hermes/skills/*/SKILL.md
grep -l 'operations completed successfully' ~/AppData/Local/hermes/skills/*/SKILL.md
```
These boilerplate sentences are markers for skills that may lack custom content.

### Pitfall 11: Assuming Previous Audit Output Is Still Accurate

**Problem:** A final report from a prior session claims "3 critical issues, 16 warnings remaining" — but rerunning the audit with the `scripts/skills-structural-audit.py` script discovers 312 actual issues. Previous audits used narrower scope (frontmatter only) and different scan methods (find -exec grep), producing undercounts.

**Prevention:** Never trust a prior session's audit output without fresh verification. Always re-run the audit with `scripts/skills-structural-audit.py` before declaring a fix complete. The tool-call limit of 50 in `execute_code` blocks also means audits run via `hermes_tools.read_file()` inside `execute_code` can silently truncate after 49 reads — producing invalid "pass" results.

---

## Success Metrics

- **Audit Coverage:** 100% of skills scanned
- **Patch Success Rate:** ≥99% (rollback if <95%)
- **Verification:** All skills loadable with `skill_view()`
- **Documentation:** Audit + plan + execution + verification reports generated
- **Traceability:** JSON logs of all patches (skill_name, before, after)

---

## Support Files

- `scripts/skills-structural-audit.py` — Reusable audit script that checks all 5 required structural sections (frontmatter, When to Use, Workflow, Verification Checklist, Best Practices) across the entire skill library. Supports `--fix` for auto-correction.
- `scripts/skills-audit.py` — Weighted scoring audit (user-local, `~/AppData/Local/hermes/scripts/`). Scores each SKILL.md on 15 checks (frontmatter validity, YAML parse, section completeness, name/dir match, file size), generates per-skill reports and consolidated index. Catches YAML quoting errors, name mismatches, and missing workflow sections that structural-only audits miss. Run with `python3 ~/AppData/Local/hermes/scripts/skills-audit.py`.
- `references/class-level-skill-policy.md` — Concise policy for keeping skills class-level, using support files, and capturing reusable maintenance learnings.
- `references/batch-processing-pattern.md` — Batch execution pattern for 100+ patches with checkpointing
- `references/title-derivation-algorithm.md` — Auto-derive skill titles from directory names
- `references/phase3-safety-gates-and-verification.md` — Safety gates pattern, rollback strategies, and verification checklist for Phase 3 execution. Captures 4-gate pattern: active task check, git checkpoint, dependency mapping, rollback plan.
- `references/generic-boilerplate-markers.md` — Exact grep patterns for detecting injected generic sections (checklist, workflow, overview, when-to-use). Use after any bulk fix pass to confirm zero contamination.

## Multi-Phase Workflow (SandBox Pattern)

In SandBox projects, this skill applies a proven multi-phase pattern:

1. **Phase 1 (Audit)** — Enumerate all skills via skill_view(), skills_list(); generate context document (docs/skills-debug-context.md with dependency graph)
2. **Phase 2 (Plan)** — Create implementation plan (docs/plan/skills-debug-plan.md) with tier structure; organize patches by impact (Critical → Documentation → Content)
3. **Phase 3 (Execute)** — Apply patches via skill_manage(action='patch'); verify each patch with skill_view() immediately after
4. **Phase 4 (Verify)** — Confirm all skills remain accessible; test cross-references; generate completion report (e.g., SKILLS_FIX_PHASE_1_3_REPORT.md)

Example skill dependency graph (from SandBox audit 2026-05-29):
- `systematic-debugging` ← `enhance-markdown`, `writing-plans`, `subagent-driven-development`
- `plans-and-specs` ← `executing-plans`, `subagent-driven-development`
- `writing-plans` ← `hermes-skill-library-maintenance` (for structuring plan artifacts)

## Related Skills

- `hermes-agent` — Hermes Agent configuration and extensions
- `hermes-skill-library-maintenance` (root) — canonical maintenance skill

## Recently Absorbed Skills

- `dispatching-parallel-agents`, `skill-creator`, `skill-judge`, `writing-skills` → this skill
- `project-consolidation`, `simplify`, `git-patch-management`, `template`, `boost-prompt` → this skill



## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Leave the library better than found**: If a session reveals a reusable workflow, pitfall, or preference, patch the umbrella skill and add a short reference instead of creating a one-off artifact.
6. **Clean up**: Remove temporary files, release resources after completion

## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

