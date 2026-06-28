# Workflow Prompt Phase Maintenance — Worked Example

## Task

Enhance `Prompts/repo.prompts.md` (a multi-repo management workflow prompt) with 3 new phases:
1. Dependency Audit & Optimization
2. Bun Migration (npm/pnpm → bun)
3. CI Workflow Audit & Setup

Constraint: new phases must execute BEFORE the existing consolidation phase (P3).

## Input Document Shape

Existing document had 9 phases (P0-P8) with the following cross-reference sections:

- Frontmatter (description, tags, dependencies, skills)
- Top-level priority summary
- Priority tiers table
- Phase body sections (Phase 0 .. Phase 8)
- Skill cross-reference table
- Verification gate (bash script)
- Pitfalls list
- Actions list

## Edits Made (in order)

### 1. Frontmatter — description
- Bumped "13 repos" → "14 repos"
- Appended "audit dependencies for bloat, migrate npm/pnpm projects to bun, and validate CI workflows"

### 2. Frontmatter — tags
- Added: `dependency-management`, `optimization`, `bun`, `ci`, `workflows`

### 3. Frontmatter — dependencies / skills
- Added `simplify` and `spike` to dependency list
- Added skill descriptions for both
- Added `read_file` to tools

### 4. Top-level summary
- Extended from 4 priorities to 7
- Added Priority 5 (audit & slim deps), 6 (migrate to bun), 7 (validate CI)

### 5. Repo count header
- "13 projects" → "14 projects"

### 6. Priority tiers table
- Inserted P4 (Dependency audit), P5 (Bun migration), P6 (CI workflow setup)
- Renumbered old P4 → P7 (Standalone tooling)
- Updated column content for each tier

### 7. Phase body sections
- Inserted 3 new `### Phase 2a:` / `### Phase 2b:` / `### Phase 2c:` blocks between existing Phase 2 and Phase 3
- Each phase includes: target repos, task checklist, output files, cross-ref

### 8. Skill cross-reference table
- Added 3 rows: P2a (simplify), P2b (spike), P2c (github-pr-workflow)

### 9. Verification gate
- Added bun lockfile check loop over 6 JS/TS repos
- Added CI workflow scan loop over all 14 repos

### 10. Pitfalls list
- Added 3 new pitfalls: dependency audit, bun migration, CI workflow

### 11. Actions list
- Added: `bunx cost-of-modules`, `bun pm ls`, `pipdeptree`, CI workflow scan
- Added: `skill_view(name="simplify")`

### 12. Cleanup — duplicate detection
- `tail -50` scan revealed 24 lines of orphaned duplicate content: a broken code block followed by duplicate Pitfalls + Actions sections from a prior editing session
- Removed the entire orphaned block
- Total file reduction: 812 → 797 lines

## Key Lessons

1. **Skip renumbering existing phase headings** — inserting `2a/2b/2c` avoids touching every subsequent `### Phase N:` heading. Use letter suffixes for insertions between numbered phases.

2. **Patch tool YAML escaping** — when patching markdown containing escaped YAML sequences like `\.\*`, the YAML frontmatter may re-escape them. Prefer plain-text alternatives (`.*` in backticks) where possible, or verify rendering after the patch.

3. **Table formatting on re-patch** — if a patch adds extra pipes to table rows (`|| row |` instead of `| row |`), fix immediately with a follow-up patch. Tables break rendering silently.

4. **Cross-ref sections are the main risk** — the phase body is the easy part. Forgetting to update the skill cross-reference table or verification gate creates a document that contradicts itself. Check off each section from the list above before calling the edit done.
