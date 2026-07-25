# Prompt Quality Enhancement Analysis — method & rubric

Companion to `SKILL.md` Phase 5. Use this when asked for a *quality enhancement*
report (structure + clarity + reference-integrity), as opposed to the
structure+safety audit or frontmatter validation. Read-only; never mutates
`.prompt.md` files.

## Slicing the library

The full `~/.hermes/prompts/` set is large (211+ `.prompt.md` at time of
writing). Work in alphabetical slices to keep reports reviewable:

- Sort all `*.prompt.md` by name.
- Slice N = lines `(N*70)+1 .. (N+1)*70` (1-indexed). Slice 3 = lines 141–211
  = the final 71 files.
- To get an exact slice on Windows git-bash, `ls ... | sort | sed -n '141,211p'`
  then **convert MSYS `/c/...` paths to native `C:/...`** (Python won't resolve
  `/c/...`). Drop the list to `slice3.txt`.

## Weakness rubric (dependency-free scoring)

For each prompt, count how many of these hold TRUE (each = 1 weakness point;
higher score = poorer quality):

1. `missing plan`            — no `plan:` frontmatter key.
2. `no acceptance criteria`  — body has no "acceptance criteria / definition of
                               done / done when / success criteria".
3. `no Goal section`         — no H2/H3 containing goal|objective|purpose.
4. `no Workflow/Phases`      — no heading containing workflow|steps|phase|
                               process|procedure|approach.
5. `no Rules section`        — no heading containing rule|guideline|constraint|
                               don't|do not.
6. `no explicit Do/Don't`    — body lacks do|don't|do not|never|always|must|
                               avoid|ensure (case-insensitive).
7. `no verification step`    — body lacks verif|check that|confirm that|test
                               that|self-check.
8. `dead template refs`      — any `templates/...` ref that does not resolve on
                               disk (see Reference Integrity below).
9. `very thin (<20 lines)`   — body < 20 non-empty lines.
10. `thin (<30 lines)`       — body < 30 non-empty lines.

Triage bands observed in practice: score >=5 = structurally broken / strong
candidate; 3–4 = minor (mostly dead refs + library-wide missing plan/acceptance);
<=2 = already-good (only missing the library-wide plan/acceptance fields).

## Reference integrity (dead-link detection)

The richest finding in real libraries: prompts `include` `templates/<name>/*.md`
that do not exist. Method:

- Extract refs with `templates/[^\s\)\]\"\'`]+` on each body.
- Resolve each against the real `templates/` tree with `os.path`:
  - ends in `/`  -> `os.path.isdir`
  - contains `*`/`...` -> unknown, skip
  - file path -> `os.path.isfile`
- `_shared/*` (rules-core.md, skills-table-core.md, section-skeleton.md,
  verification-checklist.md, frontmatter.md, phases.md) almost always exist and
  are VALID — keep them. Per-prompt `templates/<name>/...` dirs are frequently
  MISSING -> flag as dead.

Note: `template.md` (a single template *file*) is distinct from the `templates/`
*include directory* — both legitimately exist; the dead-ref problem is the
missing per-prompt subdirs, not the `_shared` set.

## Frontmatter parsing without PyYAML

The analysis box may not have `yaml` installed (PEP 668). Use a regex frontmatter
splitter instead of `yaml.safe_load` so the script has zero third-party deps:

```
m = re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$', text, re.DOTALL)
fmb, body = m.group(1), m.group(2)
# description / tags / plan / formatter via per-key regex
```

(If `yaml` IS available, prefer it; the regex fallback is for the locked-down box.)

## Report shape

Emit to `<prompts>/docs/enhancement-batchN.md`:
- intro: slice range, count, method, "read-only / no edits made".
- 3 systemic findings (library-wide gaps) up top.
- Top-15 table: file | issue | concrete suggested enhancement.
- Remaining files: one-line verdict each.
- Summary counts (total / strong / minor / already-good).

## Non-destructive proof

This is a report skill. Run the reusable script with `--check-readonly` to assert
SHA-256 of every scanned `.prompt.md` is unchanged before vs after, exactly like
the safety audit's Phase 4. The script lives at `scripts/prompt_quality_slice.py`.

## Pitfalls (Windows / git-bash)

- Native Python does NOT resolve MSYS `/c/...` paths -> `FileNotFoundError`.
  Convert slice list with `sed 's#^/c/#C:/#'` or use `r"C:\..."`.
- `/tmp` does not exist on Windows git-bash -> write temp files under the cwd.
- `search_files` glob for `*.prompt.md` can return 0 -> use `ls`/`os.listdir`.
- Do NOT touch the bundled `audit_prompts.py` under `~/AppData/Local/hermes/scripts/`
  (hardcoded to a nonexistent dir) — use the skill's own `scripts/` instead.
- The "verify filter" in throwaway checkers is itself bug-prone: a scored line
  like ` 8  name.prompt.md ...` starts with a SPACE, so `line[0].isdigit()` is
  False and under-counts. Match `^\s*\d+\s` instead.

## Pitfalls (analysis correctness — learned the hard way)

- **Reference integrity is POINT-IN-TIME. Regenerate intermediate data IMMEDIATELY
  before building the report, and re-resolve templates/... at report time.** A
  sibling process (or another agent) can populate the templates/<name>/ tree
  between your analysis run and your report build, making a saved JSON stale.
  Symptom observed: a report claimed 52 files / 121 dead links, but after the
  templates/ tree was populated by another process the true state was 19 files /
  19 dead links — every top-candidate dead-reference claim was wrong. Fix: run
  the analyzer and build the report in the SAME invocation, or re-run the analyzer
  immediately before. Prefer the reusable scripts/ref_integrity_check.py, which
  stamps as_of and writes docs/_refcheck.json so report and live tree agree.

- **skill: / tool: / prompt: refs are NOT files.** Frontmatter uses these as
  namespace identifiers (real skills/tools/prompts). Only PATH-LIKE refs
  (templates/...) should be existence-checked. Checking skill:<name> against the
  filesystem produces false-positive broken-reference flags, and a hardcoded skill
  allowlist will wrongly mark legitimate skills as missing.

- **Header detection must match on the HEADER LINE, not a body-wide regex.** A
  pattern like re.search(r'#{1,4}\s+.*\brule\b', body) does NOT anchor to the
  heading and misses plural headings (## Rules, ## Phases, ## Workflow).
  Extract headings first ([l for l in body.splitlines() if re.match(r'^\s*#{1,4}\s', l)])
  then test each heading with re.search(pat, h, re.I). A body-wide check falsely
  flags ~59/60 files as no Rules / no Phases.

- **Dedupe per file.** Count DISTINCT dead links (and distinct dirs), not every
  regex occurrence. The same templates/_shared/rules-core.md is cited 2-3x per
  prompt; counting raw matches over-reports by ~2x and conflates valid _shared
  refs with missing per-prompt dirs.

- **Slice header vs enumerated count may differ.** A delegation header said 70
  files but enumerated 60 unique paths. Verify the actual enumerated count exists
  on disk and report the REAL number, not the header's.

- **Filename collisions with sibling agents.** Multiple agents may write the same
  scratch filename (e.g. analyze_prompts.py). Use a slice-specific name
  (analyze_slice1.py) and check ls -l timestamps if results look off.
