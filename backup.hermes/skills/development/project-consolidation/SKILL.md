---
name: project-consolidation
title: Project Consolidation
description: Five-phase workflow for cleaning up and restructuring a project repository — separating generated outputs from source, removing stale boilerplate, consolidating duplicates, and updating all cross-references.
author: Alexa
tags: [cleanup, repo-organization, consolidation, project-restructuring]
---## Goal
Use when Five-phase workflow for cleaning up and restructuring a project repository — separating generated outputs from source, removing stale boilerplate, consolidating duplicates, and updating all cross-references. to accomplish the associated tasks and objectives.


# Project Consolidation

Systematic approach to cleaning up a repo that has accumulated generated output files, stale scaffolding from other projects, duplicate content, and outdated config files.

## Workflow
### Phase 1: Preparation

- Understand the context and requirements.
- Gather necessary tools and resources.

### Phase 2: Execution

- Perform the core actions required by the skill.
- Apply the techniques and procedures outlined.

### Phase 3: Verification

- Verify the results against the expected outcomes.
- Confirm that the task has been completed successfully.


## When to Use

- Generated `.md`/`.pdf`/`.html` output files are mixed with source code in root
- Stale boilerplate from a scaffold template (OpenCode, cookiecutter, create-* app) is present but unused
- Two or more config files serve the same purpose (e.g. `.markdownlint.yaml` + `.markdownlint.json`)
- A master orchestration document references files that no longer exist
- The repo has drifted from its original purpose and needs a structural reset
- **Workspace-level audit docs are stale** — inventory, normalization, ignore-file, or research-doc reports need refreshing from live `gh api` + filesystem state (see `references/workspace-audit-refresh.md`)

## When NOT to Use

- Versioned infrastructure-as-code repos (Terraform, Kubernetes manifests)
- Monorepos with established conventions (use their existing structure)
- Database or cloud storage organization

## Phase 1 — Inventory

Survey the full directory tree. Categorize every file:

| Category | Description | Typical Action |
|---|---|---|
| **Source code** | `index.ts`, `src/`, `app/` | Keep |
| **Generated output** | `*.md`, `*.pdf`, `*.html` from tool runs | Move to `output/` |
| **Stale boilerplate** | READMEs/CONTRIBUTING from scaffolded templates, unrelated config, logos | Remove |
| **Config** | `tsconfig.json`, `.eslintrc`, `.gitignore`, `.prettierrc` | Keep or prune dupes |
| **Orchestration docs** | Master prompt files, project context files | Update path references |
| **Work-in-progress** | Draft READMEs for other repos, notes, patches | Keep, document location |
| **Input samples** | `sample-input.json`, template data files | Keep (source, not generated) |

```bash
# Quick inventory
find . -maxdepth 1 -type f | sort
ls -d */  # top-level directories
```

## Phase 2 — Check Cross-References

Before moving or deleting anything, find everything that references files targeted for change:

- **Code** — file write paths in `index.ts`, config load paths
- **CLI help text** — `--help` output, docs showing default paths
- **README.md** — examples, output file references, CLI option docs
- **Project context files** — facts mentioning file locations (typically `*AGENTS*` or `*CLAUDE*` files)
- **Master orchestration docs** — `grok_summary*.txt`, `project-plan.md`, portfoio-plan.md
- **CI/CD** — GitHub Actions, Makefile targets referencing paths

```bash
# Find references to a path across the project
grep -rn "output_resume\|resume\.md\|cover-letter\.md" --include="*.ts" --include="*.md" .
```

## Phase 3 — Execute

### 3a — Move generated outputs

```bash
mkdir -p output
mv file1.md file2.md file3.pdf output/
```

Rule: `output/` for anything regeneratable from a build or run command.

### 3b — Remove stale boilerplate

Typical stale files from imported scaffolds:

```
docs/              # agent/skill docs from another project
CONTRIBUTING.md    # points to another project's repo
Makefile           # references non-existent directories
.stowrc            # GNU Stow config (dotfile symlinks)
.pre-commit-config.yaml  # no pre-commit hooks installed
opencode-logo.png  # branding from other project
.markdownlint.yaml # redundant with .markdownlint.json
```

```bash
rm -rf docs CONTRIBUTING.md Makefile .stowrc .pre-commit-config.yaml
```

### 3c — Update code paths

If the code hardcodes output paths (e.g. `writeFile('resume.md')`), update to `output/resume.md`:

```typescript
// Before
const mdFile = `${outputName}.md`;

// After
const mdFile = `output/${outputName}.md`;
```

Also update any PDF generation paths that mirror the markdown path.

### 3d — Update `.gitignore`

Add `output/` if generated files should not be tracked.

## Phase 4 — Update Documentation

| Doc | What to update |
|---|---|
| `README.md` | CLI option defaults, Output Files section, examples |
| Project context files | Output path facts, CLI table |
| Master orchestration doc | Progress tracking, file path references |
| `--help` text (in code) | Default output path mentions |

When updating multi-line help strings in code, patch each line separately rather than trying to insert `\n` — avoids accidentally merging adjacent lines.

## Phase 5 — Verify

1. **Run the tool** — confirm output lands in new location
2. **Check `--help`** — verify updated paths display correctly
3. **Build/typecheck** — `bun tsc --noEmit`, `bun run build`
4. **Spot-check moved files** — open one or two to confirm content is intact
5. **Verify cleanup** — `ls -la root` should show clean separation

## Phase 6 — Replace a Project in the Prompt System

Use when a project is being retired and replaced by a new one in a multi-project workspace, requiring coordinated updates across master orchestration docs, cross-referenced prompt files, and project scaffolding.

### Steps

#### Step 1 — Inventory all references

Search across ALL `.prompts.md`, `.prompts.txt`, `.md` files in the workspace for the retiring project name:

```bash
grep -rn "retiring-project-name" Prompts/ --include="*.md" --include="*.txt"
```

Also check workspace-consolidate, bash-scripts-fix, and any other prompt files that describe project inventory.

#### Step 2 — Update the master orchestration doc

| Section | Action |
|---------|--------|
| Frontmatter tags | Remove retiring project's tag, add new project's tech tags |
| Overview | Remove retiring project's phase step; renumber remaining phases |
| Rules section | Remove retiring project's merge/workflow rules |
| Workspace Scope | Remove retiring project from scope items |
| Project table | Replace retiring project entry (name, type, research report link) |
| Phase prerequisites | Remove phase gates that reference the retiring project |
| Branch normalization table | Replace entry (source default, extra branches) |
| Generic phase prerequisites | Remove references to retired phase completion |
| Canonical script layout | Replace retiring project directory listing |
| Verification checklist | Replace retiring project's verification items |
| Summary template | Replace retiring project's entry lines |

**Pitfall — table formatting**: When using `patch` to replace table rows, the tool's fuzzy matching may re-add leading `|` pipe characters on the lines above/below your target. After patching, re-read the table and use a second `patch` to strip any stray `||` prefixes.

#### Step 3 — Update cross-referenced files

- `Prompts/workspace-consolidate.prompts.md` — replace retiring project's script/directory listing
- `Prompts/bash-scripts-fix.prompts.md` — if the retiring project's scripts are physically removed, update the inventory; if scripts still exist but the project is retired, note the scripts as unowned
- Any other prompt file that lists, describes, or references the retiring project

#### Step 4 — Scaffold the new project

Create the initial project structure with these files:

| File | Purpose |
|------|---------|
| Agent guidance file (`GUIDE.md`) | Stack signals, setup commands, dev workflow, style, security, PR guidance |
| `RESEARCH_REPORT.md` | Inherited tech signals from source repos, architecture decisions, risks |
| `README.md` | Quick start, stack table, repo origin notes |
| `.gitignore` | Python + Node.js + OS + IDE patterns |
| `.editorconfig` | Consistent indentation (2-space JS/TS, 4-space Python) |
| `backend/requirements.txt` | Django, DRF, Celery, scraping deps |
| `backend/config/` | Django settings placeholders (base, local, production) |
| `backend/apps/` | Django app directories (comics, scraping, users, api) |
| `frontend/package.json` | Next.js, React, Tailwind, shadcn/ui deps at latest major |
| `frontend/tsconfig.json` | Strict TS, bundler module resolution, `@/` path alias |
| `frontend/next.config.ts` | Image remote patterns for external hosts |
| `frontend/src/app/layout.tsx` | Root layout with font loading, metadata |
| `frontend/src/app/page.tsx` | Landing page stub |
| `frontend/src/app/globals.css` | Tailwind directives, CSS variables for theme |

#### Step 5 — Verify

1. **No remaining references** — search for the retiring project name; zero hits in `Prompts/` is the target
2. **Cross-references consistent** — new project name appears in all tables, checklists, and summary lines
3. **Branch table clean** — retiring project removed, new project has correct source default
4. **Scaffold completeness** — new project has GUIDE.md, RESEARCH_REPORT.md, backend scaffold, frontend scaffold
5. **`git status`** — confirm no unintended changes outside the prompt system and new project dir

## Pitfalls

- **Don't delete work-in-progress** — `updated_readmes/`, draft READMEs, patches, or notes for other repos in the portfolio
- **Don't break orchestration docs** — update paths in master prompts that reference moved files. The `grok_summary_prompt.txt` often has progress tracking that references file locations
- **Check for duplicate configs** — e.g., `.markdownlint.yaml` + `.markdownlint.json` (keep the one referenced by scripts in `package.json`)
- **Template vs generated confusion**: `application_materials/COVER_LETTER.md` is a source template; root `cover-letter.md` is generated output. Templates stay, generated moves to `output/`
- **Preserve input samples**: `sample-input.json` is source data for the tool, not generated output
- **Framework-generated scaffold files are real outputs** — if a successful build creates `next-env.d.ts` or rewrites `tsconfig.json`, treat that as part of the scaffold, document it, and only ignore transient build caches like `*.tsbuildinfo`
- **No backup files**: Per SOUL.md, never create `.bak`/`.backup`/`.old` copies. Git is the safety net

See also: `references/nextjs-generated-artifacts.md`


- [ ] Project context files reflect new structure
- [ ] `.gitignore` excludes `output/`
- [ ] Master orchestration doc has updated progress tracking

## See Also

- `references/opencode-boilerplate-patterns.md` — patterns for detecting stale OpenCode scaffolding in repos
- `references/django-nextjs-scaffold.md` — project scaffold template for Django REST backend + Next.js 16 App Router frontend
- `file-organizer` skill — for personal Downloads/Desktop organization (complementary but narrower scope)
- `references/per-repo-checklist-execution.md` — execute structured per-repo action plans across submodule-style repos with no-action detection and per-repo commit workflow
- `references/workspace-audit-refresh.md` — refresh stale workspace-level inventory/audit docs from live `gh api` + filesystem state (branch state, ignore files, research docs, working-tree dirtiness)


