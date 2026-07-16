# Enhance Markdown for All Prompts (Batch Audit & Consolidation)

**Goal**:
- Load all plan‑related and prompt‑management skills.
- Scan the `./prompts` directory for every `.prompt.md` file.
- Deduplicate, resolve conflicts, and enhance each prompt’s front‑matter, tags, toolset, and script references.
- Consolidate shared sections into `prompts/templates/_shared` where appropriate.
- Validate the final set of prompts with the provided validation scripts and `skill‑judge`.
- Ensure no unapproved changes remain; user has granted full approval for all actions.

**Current Context / Assumptions**
- Working directory: `C:\Users\Alexa\Desktop\SandBox`.
- All required skills (`plan`, `plans-and-specs`, `prompt-management`) are already loaded (see prior response).
- Prompt files are stored under `./prompts` and may include associated template and script files.
- Validation utilities exist:
  - `scripts/validate_prompt_frontmatter.py`
  - `scripts/dry_run_prompts.py`
  - `scripts/fix_orphan_tags_in_fix_output.py`
  - `scripts/patch_fix_prompts_dedup_tags.py`
  - `skill-judge` (via `hermes-agent`)
- User has approved *all* unapproved actions and approvals.
- No destructive external side‑effects (e.g., API calls) will be triggered during the audit; any such prompts will be handled in dry‑run mode.

**Proposed Approach**
1. **Inventory** – List every `.prompt.md` file and related templates/scripts.
2. **Load & Verify Skills** – Ensure `plan`, `plans-and-specs`, and `prompt‑management` are active (already done).
3. **Front‑Matter Validation** – Run `validate_prompt_frontmatter.py` to detect missing fields, malformed YAML, duplicate `metadata:` blocks, missing `trigger:`, empty `tags:` etc.
4. **Deduplication** – Identify duplicate prompts by matching `name`, `title`, and content hash. Flag exact copies and near‑duplicates (high similarity).
5. **Conflict Resolution** – For each duplicate/conflict:
   - Keep the most recent file (by mtime) as the canonical version.
   - Merge unique tags and dependencies.
   - Update any references (`references:`) in other prompts to point to the canonical file.
6. **Consolidation of Shared Sections** – Detect repeated markdown blocks (e.g., common `## Goals`, `## Personas`, `## Toolsets`).
   - Extract these into shared templates under `prompts/templates/_shared/`.
   - Replace inline copies with `{{> _shared/section-name }}` style includes (or simple reference links if the system uses a templating mechanism).
7. **Enhancement** – For each prompt ensure the front‑matter contains:
   - `name:` (slugified filename without extension)
   - `title:` (human‑readable title)
   - `description:` (short one‑sentence summary)
   - `version:` (semantic version, start at `1.0.0` if missing)
   - `tags:` (non‑empty list – inferred from filename, title, and body using the `prompt‑tag‑inference` reference)
   - `trigger:` (`/<name>`)
   - `toolsets:` (minimal required set, inferred from `dependencies:`)
   - `skills:` (list of referenced Hermes skills)
8. **Validation Pass** – After modifications:
   - Run `validate_prompt_frontmatter.py` (dry‑run) to confirm all prompts pass.
   - Run `skill‑judge` on each prompt to ensure quality thresholds.
   - Execute `scripts/dry_run_prompts.py` for any prompts that invoke external actions to verify they remain safe.
9. **Commit & Record** – (Plan only) – Record intended Git actions (add, rm, commit) in the plan’s *Change Log* section for later execution.
10. **Risk & Open Questions** – Document any prompts requiring manual review (e.g., those with external side‑effects, ambiguous duplicate resolution, or missing scripts).

**Step‑by‑Step Plan**

### Phase 1 – Inventory & Baseline
1. Run `search_files` (target=`files`, pattern=`*.prompt.md`, path=`./prompts`) to collect the full list of prompt files.
2. Record each file’s path, size, and `git log -1 --format=%ci` timestamp.
3. Identify associated template directories (`prompts/templates/*`) and script files (`prompts/scripts/*`).

### Phase 2 – Front‑Matter Audit
1. Execute `python scripts/validate_prompt_frontmatter.py --dry-run ./prompts`.
2. Capture the JSON report – note missing fields, duplicate `metadata:` blocks, malformed YAML, empty `tags:`.
3. For any missing `trigger:` generate `/<slug>` where slug = filename without extension.

### Phase 3 – Deduplication & Conflict Resolution
1. Compute a SHA‑256 hash of each prompt’s body (excluding front‑matter).
2. Group prompts with identical hashes → exact duplicates.
3. For groups with >1 member, keep the newest file (by Git timestamp) as canonical.
4. For near‑duplicates (≥90 % similarity using a simple line‑based diff), create a *consolidation task* to merge unique sections.
5. Update any `references:` or cross‑prompt links to point to the canonical file.

### Phase 4 – Shared Section Consolidation
1. Scan all prompts for repeated markdown blocks (e.g., standard `## Personas`, `## Toolsets`, `## Goals`).
2. Extract each repeated block into `prompts/templates/_shared/<block‑name>.md`.
3. Replace inline blocks with an include directive (`{{> _shared/<block‑name> }}`) or a markdown link placeholder as defined by the project's templating conventions.
4. Verify that the new template files are referenced correctly by all prompts.

### Phase 5 – Prompt Enhancement
For each prompt (including newly created canonical versions):
1. Ensure front‑matter includes all required keys (see Phase 2 list).
2. Infer missing `tags:` using the `prompt‑tag‑inference` reference (keyword mapping from title/body).
3. Add a `version:` field – if missing, set to `1.0.0`; otherwise bump minor version if changes were made.
4. Verify `toolsets:` aligns with `dependencies:` – remove any tool not used.
5. Ensure `skills:` list contains only valid skill names (validate against `skills_list`).

### Phase 6 – Validation Pass
1. Re‑run `validate_prompt_frontmatter.py` (without `--dry-run`) to confirm compliance.
2. Run `hermes skill-judge` on each prompt to check quality score (target ≥ 80 %).
3. Execute `scripts/dry_run_prompts.py` to simulate any external actions; collect any warnings.
4. Record any failures; create a *manual review* ticket for those prompts.

### Phase 7 – Change Log & Commit Plan (Plan‑Only)
- **Add**: All newly created shared template files.
- **Modify**: List of prompts with updated front‑matter and consolidated sections.
- **Delete**: Exact duplicate prompt files (non‑canonical copies).
- **Commit Message**: `feat: enhance prompts – dedup, consolidate, validate`
- **Git Steps** (to be executed later):
  1. `git add .hermes/plans/` (plan file itself)
  2. `git add prompts/**/*.md`
  3. `git rm <duplicate‑files>`
  4. `git commit -m "feat: enhance prompts – dedup, consolidate, validate"`
  5. `git push` (optional, user‑controlled).

**Tests / Validation**
- Run the validation scripts (Phase 6) – success criteria: 0 errors, all prompts pass front‑matter schema, `skill‑judge` score ≥ 80 %.
- Dry‑run any prompt that contains `tool: external` or API calls; ensure they do not attempt real network activity.

**Risks, Trade‑offs, Open Questions**
- **Risk**: Over‑aggressive deduplication could remove a prompt that is intentionally similar but context‑specific. *Mitigation*: Keep the newest version and log the removed file for audit.
- **Risk**: Shared template extraction may break prompts that rely on inline formatting nuances. *Mitigation*: Test each prompt after consolidation (Phase 6).
- **Risk**: Missing external scripts referenced by prompts could cause later execution failures. *Mitigation*: Flag any missing script file as a *manual review* item.
- **Open Question**: Do any prompts require custom `profile` overrides that are not currently captured? If so, add a `profile:` field manually during the enhancement phase.
- **Open Question**: Are there any prompts that intentionally duplicate content for pedagogical reasons? Those should be exempt from deduplication.

**Deliverables**
- The plan file saved at `.hermes/plans/2026-07-16_013954-enhance-markdown-prompts.md` (this file).
- A detailed *Change Log* section (populated in the plan) for later execution.
- No files have been modified yet; the plan is ready for implementation.

**Next Steps**
- Review the plan with the user.
- Upon approval, proceed to actual execution using the described phases.

---
*Generated by the `plan` skill on 2026‑07‑16 at 01:39:54+01:00.*