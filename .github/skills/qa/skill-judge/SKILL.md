---
name: skill-judge
title: "Skill Judge"
description: "Evaluate and score skills against defined quality criteria. Use when auditing, reviewing, or improving SKILL.md files."
version: 1.1.0
author: "Hermes Agent"
license: MIT
tags: [imported]
metadata:
  hermes:
    tags: [imported]
---
## Goal

Evaluate a skill's quality against defined criteria, produce a scored assessment with actionable findings, and apply fixes when authorized. **Supports single skill evaluation and batch evaluation of multiple skills or entire skill directories.**

## When to Use

- Auditing an existing skill for quality issues
- Reviewing a skill after creation or modification
- Comparing skill variants to select the best
- Pre-flight check before publishing a skill
- **Batch evaluation of multiple skills or skill directories**
- **Triggers**: `/skill-judge <skill-name>`, `/skill-judge --batch skill1 skill2 ...`, `/skill-judge --folder skills/`, "evaluate this skill", "audit this skill"

## When NOT TO USE

- Using skills (not evaluating them)
- Non-skill markdown files (use `enhance-markdown` instead)
- Quick feedback without rigor

## Skills Required

| Skill | Purpose |
|-------|---------|
| `skill-view` | Read SKILL.md and reference files for evaluation |
| `read_file` | Read skill files directly when skill_view is ambiguous |
| `search_files` | Find skills and reference files on disk |
| `patch` / `skill_manage` | Apply fixes when authorized |

## Workflow

### Phase 0: Batch Discovery (Batch/Folder Modes Only)

**Entry check:** If `judge_results/batch-discovery.md` exists → skip to Phase 1.

1. **Discover targets** — Resolve skill list from:
   - `--batch skill1 skill2 ...` explicit skill arguments
   - `--folder path/to/skills/` recursive scan for SKILL.md files
   - `--category <name>` filter by category subdirectory
   - `--tag <name>` filter by frontmatter tags
2. **Validate targets** — Resolve each skill name to actual file path (handles flat and category subdir paths)
3. **Write discovery artifact** → `judge_results/batch-discovery.md` with skill list and paths

### Phase 1: Identify & Read

1. Resolve the skill name via `skill_view(name="<name>")`
2. Read all linked reference files (`references/`, `templates/`, `scripts/`)
3. Count: total lines, total chars, number of reference files
4. Note: frontmatter fields present, sections present

**Batch mode:** Use `execute_code` to parallelize skill_view and read_file calls across all target skills. Write individual skill assessments to `judge_results/skill_<name>_assessment.md` and aggregate to `judge_results/batch_<N>_results.md`.

### Phase 2: Evaluate — 5 Dimensions

Score each dimension 0-20. Total max = 100.

#### Dimension 1: Frontmatter Compliance (20 pts)

Check for all required fields:

| Field | Points |
|-------|--------|
| `name` | 3 |
| `title` | 3 |
| `description` (≤500 chars, starts with "Use when..." for skills with trigger) | 3 |
| `version` | 3 |
| `author` | 3 |
| `license` | 3 |
| `tags` array | 2 |

Deduct 3 for `trigger:` in skill frontmatter (non-standard — that's for prompt files).

#### Dimension 2: Structure & Organization (20 pts)

| Criterion | Points |
|-----------|--------|
| Skills Required table present | 4 |
| Phased workflow with clear phases (≥3) | 4 |
| Pitfalls section present | 4 |
| Verification checklist at end | 4 |
| Reference files exist and are substantive | 4 |

#### Dimension 3: Content Quality (20 pts)

| Criterion | Points |
|-----------|--------|
| Resumability (entry checks at phases) | 4 |
| Error handling (file-not-found, empty output, write failures) | 4 |
| Platform detection/fallback (if cross-platform) | 4 |
| Concrete examples/templates (not just prose) | 4 |
| No placeholder text (`[Add ... here]`) | 4 |

#### Dimension 4: DRY Compliance (20 pts)

| Criterion | Points |
|-----------|--------|
| No duplicate content across sections | 5 |
| No duplicate content vs reference files | 5 |
| SKILL.md is <250 lines (move detail to references) | 5 |
| Cross-reference sections are mutually consistent | 5 |

#### Dimension 5: Reference Files (20 pts)

| Criterion | Points |
|-----------|--------|
| All 3 reference types present (references/, templates/, scripts/) — where applicable | 5 |
| Each reference file is substantive (>3 lines, not a stub) | 5 |
| References are cited from SKILL.md body (one-line pointer) | 5 |
| No orphaned reference files | 5 |

### Phase 3: Findings & Scoring

Produce a structured report:

```
## Skill Judge: <skill-name>
Score: <N>/100 — [✅ AI-ready (≥70) | ⚠️ Needs work (40-69) | ❌ Rewrite (<40)]

### Frontmatter: <score>/20
- [issue or ✅]

### Structure: <score>/20
- [issue or ✅]

### Content: <score>/20
- [issue or ✅]

### DRY: <score>/20
- [issue or ✅]

### References: <score>/20
- [issue or ✅]

### Fixes Applied (when authorized)
| # | Priority | Issue | Fix Applied |
|---|----------|-------|-------------|

### Verification Checklist
- [ ] All 5 dimensions scored and totaled correctly
- [ ] Frontmatter fields checked against spec
- [ ] Structure checklist complete (Skills Required, phases, pitfalls, verification)
- [ ] Content quality criteria evaluated
- [ ] DRY compliance measured (line count, reference duplication)
- [ ] Reference files verified on disk
- [ ] Report format matches template above
- [ ] Priority fixes ordered correctly (High → Medium → Low)
### Batch Execution

For auditing 191+ skills, create a batch Python script at `C:\Users\Alexa\AppData\Local\hermes\scripts\batch_skill_judge.py` that:

1. Finds all SKILL.md files under `~/.hermes/skills/` (supports `--folder`, `--category`, `--tag` filters)
2. Scores each using heuristic scoring (skill-judge v1.1.0 dimensions)
3. Writes `judge_results/batch_NNN_results.md` per batch of 7
4. Writes `judge_results/summary.md` with aggregates
5. Supports `--resume` to skip existing batch files
6. Supports `--parallel` to use `execute_code` for concurrent scoring

**Batch size:** 7 skills per batch (matches existing batch pattern). Each batch writes its own results file for resumability.

### Reference Files — Systemic patterns from 2026-06-14 audit (68 skills): universal missing elements, frontmatter deficits, template anti-patterns, placeholder skills, split candidates, remediation priority.

### Phase 4: Apply Fixes (when authorized)

**Fix priority order:**
1. **High** — Missing frontmatter fields, missing verification checklist, placeholder text
2. **Medium** — Over-length SKILL.md (move detail to references), duplicate content
3. **Low** — Formatting, minor DRY issues

**After applying fixes:**
1. Re-read the file with `skill_view` to confirm changes
2. Re-score the skill
3. Report delta (before → after)

## Pitfalls

- **Protected skills**: Do NOT edit bundled skills (e.g., `hermes-agent`) or hub-installed skills. Pinned skills CAN be improved (patch only, no delete).
- **Over-patching**: Don't reformat or restructure beyond what the score demands. Fix issues, don't rewrite for style.
- **Scoring inflation**: A skill with placeholder text cannot score above 60. A skill missing a verification checklist cannot score above 70.
- **Reference bloat**: If SKILL.md is >250 lines, the DRY dimension caps at 10/20 until content is moved to references.
- **Verification**: Never use `skill_view()` to verify your own edits (stale cache). Read the file on disk after patching.
- **Ambiguous skill names**: When `skill_view()` returns "Ambiguous skill name", use `read_file()` directly on the known path instead of retrying `skill_view()`. Common collision pairs: `accelerate`/`huggingface-accelerate`, `cli`/`inference-sh-cli`, `ideation`/`creative-ideation`, `lambda-labs`/`lambda-labs-gpu-cloud`, `modal`/`modal-serverless-gpu`. The shorter name is usually the canonical one with full content. See `references/batch-audit-findings.md` for confirmed collisions from 2026-06 audit.
- **Profile visibility**: `skill_manage()` running in the `default` profile may report "Skill not found" for skills that exist in `code-architect`. Use `patch()` with the absolute `path` parameter on the actual skill directory as a fallback. See `references/batch-audit-findings.md` for confirmed behavior.
- **Batch audit calibration**: Running skill-judge across many skills in one session causes criterion drift. Calibrate on the first batch, then lock thresholds. See `references/batch-audit-findings.md` for 2026-06 calibration data (28 batches, 191 skills → 368 after dedup).
- **2026-06-17 calibration (352 skills)**: Full re-audit scored 24 ✅ ≥80 (6.8%), 217 ⚠️ 60-79 (61.6%), 111 🔴 <60 (31.5%). Key finding: prior patches improved structure but content depth remains the bottleneck. Skills scoring 60-79 typically need concrete examples + reference files, not just structural additions. The TSV output format (`skill_name|path|score|rating|dim1|dim2|dim3|dim4|dim5|lines`) proved useful for bulk analysis — use `all_results.tsv` for cross-skill queries.
- **Subagent timeout at 600s**: When dispatching subagents for large batch audits (352 skills), the 600s timeout can fire even when work is substantially complete. Always check output files (all_results.tsv, summary.md) before assuming failure. The subagent may have completed the audit but timed out during final reporting. Mitigation: use smaller batch sizes or check for partial results before re-dispatching.
- **Planning skills remediation template**: For planning-class skills (brainstorming, plans-and-specs, prompt-planning-orchestration), the most impactful enhancements are: (1) Add Goals/Subgoals section, (2) Add Personas table, (3) Add Personality & Tone section, (4) Add Profile Selection table, (5) Move class-pattern detail to references/. Tested: brainstorming 65→84, plans-and-specs 60→88, prompt-planning-orchestration 60→84.
- **Stale file deletion pattern**: For bulk cleanup of session artifacts, use `find . -name "*-context.md" -type f -delete` pattern. Classification scheme: Active (referenced by AGENTS.md/.hermes.md/skills), Stale (not referenced, outdated), Invalid (malformed), Unused (no inbound references). Always preview before deleting. On 2026-06-17: deleted 324 files (33 root + 291 docs) safely.
- **Reference file verification**: Always `read_file()` reference files to confirm they exist and are substantive (>3 lines). Skills citing refs that don't exist on disk lose Reference points. See `references/evaluation-criteria.md` for verification checklist.
- **Context window management**: Large audits (191+ skills) will hit context limits. Process in batches of 7, write results to `judge_batch_N_results.md` after each batch, and do NOT retain full skill text between batches. The conversation compaction summary is unreliable for audit continuity — always re-read batch result files on resume. After 28 batches, reconcile totals from the 28 batch files rather than trusting in-context running counts.
- **Template-in-skill-body anti-pattern**: Skills embedding massive parameterized templates (blueprint generators) directly in SKILL.md instead of `references/` or `templates/` score poorly on DRY and Structure. Move templates out; keep SKILL.md under 250 lines.
- **Large-scale remediation strategy**: When fixing 90+ skills, prioritize by impact: (1) Rewrite placeholders (<25 score), (2) Major fix stubs (25-49), (3) Minor patch frontmatter/structure (50-69). Batch by fixing frontmatter fields + adding Skills Required + pitfalls + verification checklist in a single pass per skill. Use write_file with absolute paths for full rewrites, patch for targeted fixes.
- **Profile-agnostic editing**: Skills in category subdirectories (e.g., `development/`, `devops/`, `qa/`) may not resolve via skill_manage from non-code-architect profiles. Always use absolute paths with write_file or patch as fallback.
- **Edit reliability**: `write_file()` with complete content is more reliable than `patch()` for full skill rewrites. Patch often leaves behind broken or duplicated content when the existing file has structural issues. Use `patch()` only for small, targeted fixes on healthy skills.
- **Pagination awareness**: When a file was previously read with offset/limit pagination, `write_file()` warns to re-read the whole file first. Always re-read the current full file before overwriting it.
- **Category path indexing**: Skills may exist at both flat paths (`skills/<name>/SKILL.md`) and category subdirs (`skills/<category>/<name>/SKILL.md`). The subdir version usually has full content. Always check category subdirs when the flat path is missing or returns minimal content.
- **Pagination awareness**: When a file was previously read with offset/limit pagination, `write_file()` warns to re-read the whole file first. Always re-read the current full file before overwriting it. Similarly, `patch()` will fail if `old_string` was constructed from a paginated read — the match must be against actual file content.
- **Category path indexing**: Skills may exist at both flat paths (`skills/<name>/SKILL.md`) and category subdirs (`skills/<category>/<name>/SKILL.md`). The subdir version usually has full content. Always check category subdirs when the flat path is missing or returns minimal content.
- **Verification scoring**: Automated heuristic scoring is a useful gate but not final authority. After batch fixes, verify by reading the final file and applying the skill-judge criteria manually for a sample before declaring the batch complete.
- **Pagination-to-patch failure**: When a file was previously read with offset/limit pagination, `patch()` fails because `old_string` doesn't match the actual file content. Always `read_file(path)` without offset/limit before constructing patch old_string. When `patch()` fails twice on the same file, switch to `write_file()` with full re-read content.
- **Batch remediation template decay**: Targeted patches that only add structural sections (Skills Required, Pitfalls, Verification Checklist) without adding concrete code examples or reference files will NOT move scores above 70 for thin skills (creative cluster, research models). These need content depth, not just structure.
- **References/ directory as primary content sink**: When a SKILL.md exceeds 250 lines, the single most effective fix is moving class-pattern detail (worked examples, conversion models, inventory templates) into `references/<topic>.md` files. This alone can recover 5-10 DRY points. The SKILL.md should retain only the workflow, triggers, and one-line pointers to references. Tested: plans-and-specs went from 289→147 lines (score 60→88) primarily by moving 6 class-pattern sections to references/.
- **Profile-agnostic editing**: Skills in category subdirectories (e.g., `development/`, `devops/`, `qa/`, `architecture/`, `creative/`) may not resolve via `skill_manage` from non-code-architect profiles. Always use absolute paths with `write_file` or `patch` as fallback. Flat-root skills typically have simpler content; category-subdir skills are the canonical locations and usually need the most remediation.
- **Batch remediation loop**: For a set of skills sharing the same deficiency pattern, apply the common fix template in one go: add frontmatter fields (`version`, `author`, `license`, `tags`), add a Skills Required cross-reference table, add a Verification Checklist, and add a Pitfalls section. After patching a batch, re-read and re-score to confirm the score moved into the target range before proceeding.
- **Verification after patch**: Never assume a write succeeded. Re-read the file from disk (not via skill_view) after patching, then re-score. If the score is still below target, apply additional targeted fixes and re-verify. Log before/after deltas for each skill.
- **Plan and tracking**: Keep a tracking plan under `.hermes/plans/` that lists the remaining skills, their paths, original scores, and patch status. Update it after each batch. The active plan is the one approved by the user; do not create parallel plans with conflicting names. Canonical names: `2026-06-14_143000-skills-audit-pipeline.md` for the main pipeline, and a clearly named continuation plan for remaining remediation.
- **Windows line endings**: SKILL.md files on Windows use `
\n` line endings. Regex patterns like `^---\n(.*?)\n---` will FAIL to match. Always normalize: `content.replace('
\n', '\n')` before parsing frontmatter in batch scripts. All five scoring dimensions will silently return 0 on unnormalized content.
- **Path mapping bug (SKILL.md vs directory)**: When building a batch judge script, `find ... -name "SKILL.md"` returns paths ending in `SKILL.md`. If the judge appends `/SKILL.md` again, it becomes a nonexistent path and `skill_md` stays empty. Fix: `get_skill_dir()` that checks `if p.name == "SKILL.md": return p.parent`.
- **`hermes skills list` vs `find` count mismatch**: `hermes skills list --source local` shows ~196 skills (its own inventory). But `find skills/ -name SKILL.md | wc -l` shows ~348. The difference comes from category subdirectory copies (e.g., `accelerate/` + `mlops/huggingface-accelerate/`). The inventory union is real — both paths exist on disk with distinct SKILL.md files. Always use `find` for path enumeration, not `hermes skills list`.
- **Category from frontmatter, not directory**: `hermes skills list --source local` populates the Category column from the `category:` field in YAML frontmatter, NOT from the directory tree. A skill in `skills/development/foo/SKILL.md` with no `category:` field will show empty category. If a skill IS in a category subdirectory but displays empty category, patch the frontmatter to add `category: <name>`.
- **Flat skills with categories**: 82 skills sit flat in `skills/<name>/SKILL.md` (no category subdirectory) but already have `category: <value>` in frontmatter. `hermes skills list` shows them as categorized. Moving them to a category subdirectory is cosmetic — `hermes skills list` already handles it. Skip physical moves unless the user explicitly requests it.
- **Auto-fix title: and metadata:**: The most impactful bulk auto-fix for low-scoring skills is adding missing `title:` (generated from `name:` with `name.replace('-', ' ').title()`) and `metadata:\n  hermes:\n    tags: []`. This alone moved avg 64.0→64.6 across 347 skills. Deeper fixes (phased workflows, examples, code blocks) require content-level writing.
- **Scoring floor effect**: Frontmatter averages 19/20 even for low-scoring skills. The main differentiator is Structure (10/20 avg), Clarity (9/20 avg), and Quality (10/20 avg). Missing changelog (347/348) is the single most common deficiency but also the lowest-impact to fix — it's 4/100 points. Focus on adding phased workflows, Skills Required tables, and code block examples instead.
- **Batch mode pitfalls**: 
  - **Mixed skill types** — Don't mix planning skills, creative skills, and dev skills in one batch; their criteria differ. Filter by `--category` or `--tag`.
  - **Duplicate skill paths** — Flat + category subdir duplicates will double-count. Use `find` with `-type f -name SKILL.md` and deduplicate by skill `name:` field.
  - **Partial batch failure** — If one skill fails to score, write partial results and continue. Don't halt the batch.
  - **Artifact collision** — Each batch writes to `judge_results/batch_<N>_results.md` with zero-padded N. Use `execute_code` for parallel batch processing.
  - **YAML fragments in skill body:** When scanning a skill, check for standalone YAML blocks (`---\nmetadata:\n  hermes:\n    tags: []\n---`) that appear AFTER the frontmatter closing `---`. These are copy-paste artifacts from template scaffolding that get embedded in the body. They break Structure scoring (orphaned `---` fences) and create false-positive frontmatter matches. Detection: grep for `^---` — if the second `---` appears well past line 20 (not the frontmatter close), it's a body fragment. Fix: remove the fragment entirely.
- **Verify before deleting duplicates (2026-06-22):** When instructed to delete duplicate skills, ALWAYS verify the skill exists in ≥2 paths first: `find skills/ -name "SKILL.md" | xargs grep -l "name: <skill-name>"`. If only one path exists, that's the only copy — move it to the correct category directory instead of deleting. Deleting the only copy of a skill with no hub source to reinstall from is an unrecoverable loss.

## Reference Files
- **Auto-fix title: and metadata:**: The most impactful bulk auto-fix for low-scoring skills is adding missing `title:` (generated from `name:` with `name.replace('-', ' ').title()`) and `metadata:\n  hermes:\n    tags: []`. This alone moved avg 64.0→64.6 across 347 skills. Deeper fixes (phased workflows, examples, code blocks) require content-level writing.
- **Scoring floor effect**: Frontmatter averages 19/20 even for low-scoring skills. The main differentiator is Structure (10/20 avg), Clarity (9/20 avg), and Quality (10/20 avg). Missing changelog (347/348) is the single most common deficiency but also the lowest-impact to fix — it's 4/100 points. Focus on adding phased workflows, Skills Required tables, and code block examples instead.

## Reference Files

- `references/batch-audit-findings.md` — Cross-batch pattern summary (49 skills, 7 batches), ambiguous name collisions, profile visibility notes, scoring calibration, remediation priority list, template-in-skill-body anti-pattern, and reusable batch audit workflow from 2026-06-14 audit
- `references/bulk-remediation-pattern.md` — Bulk remediation script pattern (batch_remediate.py), results from 73-skill remediation (62.9→70.7 avg), and duplicate deletion pitfall
- `references/convert-plaintext-enhance-markdown-audit-2026-06-19.md` — Case study: audit of convert-plaintext-to-md (64→92) and enhance-markdown (88→91); demonstrates reference-file gaps, entry-check/resumability patterns, error-handling requirements, platform-fallback docs, and frontmatter description format for triggered skills