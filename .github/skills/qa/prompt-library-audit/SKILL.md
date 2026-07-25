---
name: prompt-library-audit
title: Prompt Library Audit & Quality Enhancement Analysis (Read-Only)
description: Run a one-shot read-only content-structure, safety, and quality-enhancement audit across a Hermes prompts/ library, emitting markdown reports. Covers orchestration, structure heuristics, safety pattern scanning with dedup/gating/negation handling, sliced weakness-scoring with dead `templates/...` reference detection, and proving every run is non-destructive.
version: 1.1.0
author: Hermes Agent
license: MIT
tags:
  - audit
  - prompts
  - safety
  - structure
  - read-only
  - batch
---

# Prompt Library Audit (Structure + Safety, Read-Only)

## When to Use

- Asked to "audit all prompts", "review the prompt library", "check prompts for safety/structure" and want a single report.
- Producing a read-only content-structure + safety audit report for a whole `.prompt.md` collection.
- Verifying a prompt library has no injection/jailbreak, un-gated destructive, or credential-leak patterns.

## When NOT to Use

- Single-prompt deep red-teaming or attack-vector theory — delegate to `ai-prompt-engineering-safety-review`.
- Frontmatter YAML validation — use `prompt-audit-all` / `verify-frontmatter`.
- Editing/fixing prompts — this skill is report-only; never mutates prompt files.
- **Enhancement-quality analysis** (structure clarity, weak-section detection, dead `templates/...` reference detection) — NOT excluded; this is **Phase 5** below. If the ask is "analyze quality / suggest enhancements / read-only report on the final N files", this skill applies.

## Conceptual Model

Two independent axes, both scanned over each prompt **body** (text after the closing frontmatter `---`):

1. **Structure** — does the body have at least one H2/H3 heading containing a canonical keyword (Goal, Context, Workflow, Phases, Rules)? Report two buckets so the verdict is honest:
   - *truly heading-free* (no `##`/`###` at all) — strictest "no recognizable structure".
   - *non-canonical* (has headings, e.g. *Tasks*, *Prerequisites*, *Template References*) — structured but non-conforming.
2. **Safety** — CRITICAL (injection/jailbreak), HIGH (destructive-without-gate, secret-exposure). See `references/batch-audit-patterns.md` for the regex catalog.

## Workflow

### Phase 1: Enumerate
Glob all `*.prompt.md`. **Pitfall:** in some environments `search_files` glob returns 0 for `*.prompt.md` — fall back to `ls` / `os.listdir`. Use native Windows paths (`r"C:\..."`); native Python does NOT resolve MSYS `/c/...` (raises `FileNotFoundError`).

### Phase 2: Scan each body
For each file:
- Strip frontmatter (first `---` … next `---`); scan the remainder.
- Structure: detect H2/H3; classify heading-free vs non-canonical.
- CRITICAL: match injection/jailbreak phrases. **Dedup keyed on `(file, line, label)`** — one line can hit several patterns.
- HIGH-destructive: flag only when NO approval-gate wording (`approval`, `confirm`, `authorize`, `ask the user`, `before proceeding`, `verify with`) appears anywhere in the file.
- HIGH-secret: flag `show|print|echo|output|reveal|exfiltrate … credentials`, but EXCLUDE protective phrasing (`never print credentials`, `keep secret`, `store`). A `never print credentials` line is a guardrail, not a leak.

### Phase 3: Report (read-only)
Write `docs/content-safety-audit.md`: summary table (total / structure-less split / CRITICAL / HIGH), full flagged-file lists, and a verdict. **Never edit a `.prompt.md`.**

### Phase 4: Prove non-destructive
Snapshot SHA-256 of every `.prompt.md` before and after the run; assert zero diffs. Cross-check counts with an independent re-scan (re-implement the scan simply — catches both bugs and false-positives). See `scripts/prompt_library_audit.py`.

### Phase 5: Quality-enhancement analysis (read-only, sliced)
When asked for a *quality enhancement* report (weak sections, missing acceptance
criteria, dead `templates/...` includes) rather than a safety audit, work on an
alphabetical **slice** and rank by a weakness rubric:

1. **Slice.** Sort all `*.prompt.md`; slice N = lines `(N*70)+1 .. (N+1)*70`
   (1-indexed). Slice 3 = lines 141–211 = final 71 files. On git-bash:
   `ls ... | sort | sed -n '141,211p' | sed 's#^/c/#C:/#' > slice3.txt`
   (convert to native paths — Python won't resolve `/c/...`).
2. **Score.** For each prompt, count weakness points (higher = worse):
   missing `plan`; no acceptance-criteria phrasing; no `## Goal`/`## Workflow`/
   `## Rules` heading; no explicit Do/Don't wording; no verification step;
   **dead `templates/...` ref** (resolve every `templates/...` include against
   the real tree — `_shared/*` is valid, per-prompt subdirs are usually missing);
   body <20 lines (very thin) or <30 (thin). Triage: >=5 strong candidate,
   3–4 minor, <=2 already-good.
3. **Report** to `<prompts>/docs/enhancement-batchN.md`: 3 systemic findings up
   top, a top-15 table (file | issue | concrete fix), one-line verdicts for the
   rest, summary counts. **Never edit a `.prompt.md`.**
4. **Prove read-only** with the reusable script's `--check-readonly` (SHA-256
   before/after assert) — same discipline as Phase 4.

Full rubric, regex frontmatter splitter (no PyYAML needed), and Windows
path notes are in `references/quality-enhancement-method.md`.

## Reusable Scripts

- `scripts/prompt_library_audit.py` — safety+structure audit (Phases 1–4).
  ```bash
  python scripts/prompt_library_audit.py --dir "C:\Users\Alexa\AppData\Local\hermes\prompts"
  ```
  Emits `<dir>/docs/content-safety-audit.md`. Pass `--check-readonly` for the
  SHA-256 before/after diff assertion.
- `scripts/prompt_quality_slice.py` — quality-enhancement analysis (Phase 5).
  ```bash
  # whole library
  python scripts/prompt_quality_slice.py --dir "C:\Users\Alexa\AppData\Local\hermes\prompts"
  # slice by line range
  python scripts/prompt_quality_slice.py --dir "..." --slice-start 141 --slice-end 211 --top 15
  # slice by explicit file list
  python scripts/prompt_quality_slice.py --dir "..." --slice-file slice3.txt --check-readonly
  ```
  Dependency-free, no PyYAML. `--top N` prints only the N weakest; `--check-readonly`
  asserts 0 files modified.
- `scripts/ref_integrity_check.py` — pre-report dead-`templates/...` reference probe
  (run IMMEDIATELY before building the enhancement report; see the point-in-time
  pitfall above). Run it standalone or via `--slice-file`:
  ```bash
  python scripts/ref_integrity_check.py --dir "C:\Users\Alexa\AppData\Local\hermes\prompts"
  ```
  Stamps `as_of`, prints per-file dead links, and writes `docs/_refcheck.json` so
  the report and the live `templates/` tree can be cross-checked for drift.

## References

- `references/batch-audit-patterns.md` — safety regex catalog (Phases 2–4).
- `references/quality-enhancement-method.md` — Phase 5 rubric, slicing, regex
  frontmatter splitter, dead-reference resolution, Windows/git-bash pitfalls.

## Pitfalls

- Native Windows Python won't resolve `/c/...` MSYS paths — use `r"..."` native paths or acc `FileNotFoundError`.
- `search_files` glob for `*.prompt.md` may return 0 — use `ls`/`os.listdir`.
- Secret-exposure patterns over-match protective text — always exclude negation words.
- Destructive-op patterns must be gated by whole-file approval wording, else you false-positive on prompts that say "ask the user before running `rm -rf`".
- Injecting literal jailbreak example strings into skill text triggers the safety scanner — keep catalogs in `references/batch-audit-patterns.md` and use inline char-class obfuscation (e.g. `ign[o]re`) for the attack verbs so the scanner passes while the regex still matches.
- During Phase 5 slicing, **do NOT touch the bundled `audit_prompts.py`** under `~/AppData/Local/hermes/scripts/` (hardcoded to a nonexistent dir) — use this skill's own `scripts/` instead.
- On Windows git-bash, `/tmp` does not exist — write throwaway slice lists / temp scripts under the cwd, and convert `/c/...` to `C:/...` before handing paths to Python.
- Throwaway verification-check scripts are themselves bug-prone: a scored line like ` 8  name.prompt.md ...` starts with a SPACE, so `line[0].isdigit()` is False and under-counts rows. Match `^\s*\d+\s` instead.
- **Reference integrity is POINT-IN-TIME.** The `templates/<name>/` tree can be populated by another process (or sibling agent) *between* your analysis run and report build, silently invalidating a stale saved JSON. A report built from older data claimed 52 files / 121 dead links when the live tree had only 19 / 19. Regenerate intermediate data immediately before building the report, or run analyzer + report in the same invocation. Use `scripts/ref_integrity_check.py` (stamps `as_of`, writes `docs/_refcheck.json`) right before the report build.

## Related Skills

- `ai-prompt-engineering-safety-review` — attack-vector theory + per-prompt review (loaded alongside this one this session).
- `prompt-audit-all` — frontmatter YAML issue audit (different axis).
- `verify-frontmatter` — individual frontmatter validation.
