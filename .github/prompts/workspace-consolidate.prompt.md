---

name: workspace-consolidate

title: 'Workspace Consolidation — Scripts, Patches, Docs'

description: 'Consolidate scripts, patches, and documentation across the workspace with bash migration and audit workflows.'

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - file

  - terminal

scripts: []

skills:

  - introspection-only-general

  - no-git-delete

  - no-net-fetch

  - skills-tools-preflight-check

  - context-map

  - brainstorming

  - plans-and-specs

  - dispatching-parallel-agents

  - subagent-driven-development

  - systematic-debugging

  - simplify

  - acpx-executor

  - git-patch-management

  - project-consolidation

formatter: default

plan: None

dependencies:

  - prompt:context-map

  - prompt:update-implementation-plan

  - skill:brainstorming

  - skill:plans-and-specs

  - skill:dispatching-parallel-agents

  - skill:subagent-driven-development

  - skill:systematic-debugging

  - skill:simplify

  - skill:acpx-executor

  - skill:git-patch-management

  - skill:project-consolidation

  - tool:terminal

  - tool:search_files

  - skill:introspection-only-general

  - skill:no-git-delete

  - skill:no-net-fetch

  - skill:skills-tools-preflight-check

  - skill:context-map

tags:

  - agents

  - documentation

  - frontend

  - ml

  - prompts

  - skills

  - typescript

trigger: /workspace-consolidate

metadata:

  hermes: {}

---

## Goal

Consolidate scripts, patches, and documentation across the workspace with bash migration and audit workflows.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)---

## Phases

### Phase 1: Verify Canonical Script Layout (LIGHT)All 54 operational scripts must live under `projects/Bash/` in organized subdirectories.No duplicates outside `projects/projects/projects/projects/Bash/`.

### Target Structure

```
treeBash/├── Banking/                          # 34 scripts│   ├── install.sh│   ├── install-agents.sh│   ├── install/lib/00-config.sh → 08-install.sh│   └── scripts/                      # 23 files (.sh, .ps1, .bat)├── rhixecompany-comics/               # 0 scripts (pending — new Django + Next.js project)├── rhixe_scans/                      # 7 scripts│   ├── docker-clean.sh, git-setup.sh│   ├── install_chrome.sh, install_firefox.sh│   ├── prod-dev.sh, prod.sh, setup.sh├── ecom/                             # 1 script│   └── install.sh├── root/                             # 2 scripts│   ├── analyze-scripts.sh│   └── sandbox-runtime-commands.ps1├── src/                              # TypeScript core migration targets│   ├── cache-clean.ts│   ├── clean-dep.ts│   ├── upgrade.ts│   ├── git-commit-batches.ts│   ├── core/ (ast-transformer, behavior-test, dry-run, script-runner)│   ├── lib/ (cli, colors, errors, logging)│   └── migration/ (templates, ts-morph-helper)├── docs/                             # Moved from Bash/ root below│   ├── AGENTS.md│   ├── ARCHITECTURE.md│   ├── CODE_STYLE.md│   ├── README.md│   ├── bash-scripts-safety-audit.md│   ├── FINAL-SUMMARY.md│   ├── MIGRATION-GUIDE.md│   └── phase5-verification-report.md├── archive/skills-commit-batches/    # 52 archived batch files (keep as dead code reference)├── lib/                              # log-rotate.sh, log-rotate.ps1├── scripts/                          # Auditing/orchestration scripts├── edits/run-audit.sh.patch          # Patch for run-audit.sh├── tsconfig.json, package.json, bun.lock, bunfig.toml├── README.md                         # STUB — links to docs/README.md
```

### Steps

1. **Scan** for any remaining operational scripts outside `projects/projects/Bash/` (exclude   framework seeds, `.husky/`, `.devcontainer/`, `.claude/`)
2. **Move** misplaced project docs into `projects/Bash/docs/`:    - `Bash/AGENTS.md` → `Bash/docs/AGENTS.md` (update internal references)    - `Bash/ARCHITECTURE.md` → `Bash/docs/ARCHITECTURE.md`    - `Bash/CODE_STYLE.md` → `Bash/docs/CODE_STYLE.md`    - `Bash/README.md` → `Bash/docs/README.md` (replace root README with stub)
3. **Create** `Bash/README.md` stub that links to `docs/README.md`
4. **Verify** `docs/bash-migration-final-report.md` counts against actual file   listing
5. **Save** verification report to `docs/bash-canonical-layout-report.md`

### Phase 2: Debug All Patches

### Patch Inventory

```
textActive:  xamehi.patch                   (6 commits, 32K lines, Django app)  rhixe-company.patch            (3 commits, 1.7K lines, corporate site)  python-projects.patch          (6 commits, 3.3K lines, Python scripts)  youtube-downloader.patch       (23 commits, 5K lines, yt-dlp app)  projects/Bash/edits/run-audit.sh.patch  (local patch for run-audit.sh)Obsolete (patches/obsolete/):  django-scrapy-selenium.patch   (10 commits, 633K lines, cookiecutter template — LIKELY DEAD)  xamehi-tv.patch                (5 commits, 117K lines, React frontend — LIKELY DEAD)  cookiecutter-django-tailwind.patch (4 commits, 54K lines, cookiecutter template — LIKELY DEAD)
```

### Debug Workflow

For EACH patch (skip obsolete unless reclassifying):1. **Identify target project** via prefix match or README inspection2. Run `git apply --check <patch

> ` in target project directory3. **Diagnose failures**:    - If `patch does not apply`: check line endings, whitespace, already-applied      commits    - If`already applied`: flag as`pre-applied`, skip with note    - If`corrupt`: inspect binary sections, check diff line format4. **Reclassify** obsolete patches if they actually apply to an existing project5. **Fix corruption** — repair broken hunks, trailing whitespace, encoding   issues6. **Split multi-patch files** — each logical commit becomes its own`.patch` file7. **Validate isolated patches** — verify each applies independently8. **Dead patch auto-detection** — for each patch classified as `obsolete`:    - Run`git apply --check` against EVERY project directory (not just      prefix-matched)    - If a supposedly-obsolete patch applies cleanly to a live project, **promote      it** with corrected target    - If truly dead (no project found, cookiecutter template, abandoned      framework), leave in `patches/obsolete/` with documented reason    - Flag false-obsolete patches in the debug report with action: `promoted`9. **Save patch debug report** to`docs/patch-debug-report.md` with table:    ```json    [        {            "patch": "xamehi.patch",            "target": "projects/xamehi",            "commits": 6,            "applyable": true,            "issues": [],            "action": "ready"        },        {            "patch": "django-scrapy-selenium.patch",            "target": null,            "commits": 10,            "applyable": false,            "issues": ["no matching project", "obsolete cookiecutter template"],            "action": "archive-only"        }    ]```

### Phase 3: Enhance All Patches

For each patch that passed debug:1. **Enrich commit messages** with:    - Conventional commit format: `type(scope): description`    - Reference to related docs in `docs/project-docs/<name

> /` - Co-author credits if multi-contributor2. **Add metadata headers** to each commit:    ```text    From: <original-author
>    Date: <original-date
>    Subject: feat(xamehi): add user authentication module    References: docs/project-docs/xamehi/architecture.md    Related: #42, #87    ---    ```3. **Ensure portability** — use relative paths, no absolute `C:\...` references4. **Normalize line endings** — LF only (no CRLF)5. **Strip binary blobs** — remove unnecessary binary content that bloats patch6. **Record rollback tags**: `git tag PATCH-<name>-<date>` for each applied   patch7. **Patch content integrity check** — verify structural integrity beyond `--check`:    - No binary blob >1MB (flag for git bloat reduction)    - No absolute Windows paths (`C:\Users\...`,`D:\...`) — use`$HOME`or relative paths    - All author emails have valid format (`<user@domain.tld>`)    - No duplicate commits across patches (detect via commit hash)    - No trailing whitespace on diff context lines    - Flag violations but do not block — log to enhancement report8. **Patch dependency grapher** — build ordering graph before enhancement:    - For each pair of patches (A, B), use`git merge-base --is-ancestor` in      target project to detect dependency    - If B's commits contain A's HEAD as ancestor → A must apply first    - Serialize patches into a DAG-based execution order    - Save dependency graph to `docs/patch-dependency-graph.md` as mermaid      diagram9. **Save enhanced patches** to `patches/enhanced/<name>.patch`10. **Save enhancement log** to`docs/patch-enhancement-log.md`

### Phase 4: Create Missing Patches

### Gap Analysis

For each project in `projects/`, check:1. Does it have local uncommitted changes? (`git diff`, `git status`)2. Does it have a known missing feature or bugfix that should be patched?3. Is documentation out of date compared to the project's actual state?4. Does `docs/project-docs/<name

> /` have all 11 required artifacts from the   generator-orchestrator?

### Patch Creation

Create patches for any gaps found:1. **Missing documentation patches** — update README, add missing doc sections2. **Missing metadata patches** — add `.gitignore`, `.editorconfig`, `LICENSE`   where absent3. **Missing config patches** — add `tsconfig.json`, `eslint.config`,   `.prettierrc` for consistency4. **Consistency patches** — normalize existing files to match `CODE_STYLE.md`   conventions5. **Known bugfix patches** — fix bugs found during Phase 2's   `git apply --check` diagnostics

### Patch Patch Generation

```
plaintextpatches/├── enhanced/                     # Enhanced versions of original patches│   ├── xamehi.patch│   ├── rhixe-company.patch│   ├── python-projects.patch│   └── youtube-downloader.patch├── new/                          # Newly created patches│   ├── <project-name>-docs.patch│   └── <project-name>-config.patch└── obsolete/                     # Unchanged archive    ├── django-scrapy-selenium.patch    ├── xamehi-tv.patch    └── cookiecutter-django-tailwind.patch
```

### Phase 5: Document Organization & Optimization

### All Reports Under docs/All workspace-level reports go under `docs/`. All project-level docs go under`docs/project-docs/<name

> /`. All Bash-specific docs go under`projects/Bash/docs/`.

### Doc Optimization for Humans AND AIEach document must be optimal for both human readers and AI consumption: #

### Required Frontmatter (YAML)Every `.md` file should have standard frontmatter:```yaml---title: Human-Readable Titledescription: One-line summary of the document's purpose.status: draft | review | final | archivedtags: [comma, separated, tags]created: YYYY-MM-DDupdated: YYYY-MM-DD---``` #

### Content Standards

| Requirement                           | Why                             | Check                                                  || ------------------------------------- | ------------------------------- | ------------------------------------------------------ || Clear H1 title                        | Navigation, AI retrieval        | Document starts with `# Title`                         || 2-3 sentence summary after H1         | Quick human scan, AI snippet    | First paragraph is a summary                           || Section headings (H2/H3)              | Scannability, TOC generation    | No walls of text                                       || Code blocks with language tags        | Syntax highlighting, AI context | Every code block has ` ```lang`                        || Table of Contents for docs

> 300 lines | Navigation                      | Use `<!-- TOC -->` comment                             || Cross-references with paths           | Discoverability                 | `See [projects/Bash/docs/AGENTS.md](../../Bash/docs/AGENTS.md)` || Machine-parseable metadata            | AI ingestion                    | YAML frontmatter present                               || One concept per file                  | Modularity, git diff clarity    | No megadocs                                            || Active voice                          | Readability                     | "The script cleans caches" not "Caches are cleaned"    |#

### Optimization Checklist per Document

- [ ] Frontmatter exists with title, description, status, tags, dates
- [ ] First paragraph is a summary (for both humans and AI snippets)
- [ ] Headers use consistent nesting (H1 → H2 → H3, never skip levels)
- [ ] All code blocks specify language (`sh,`json, `ts,`python)
- [ ] External links use full URLs, internal links use relative paths
- [ ] No broken cross-references (validate each relative path)
- [ ] Tables have aligned columns and no empty required cells
- [ ] Terminal commands use `$` prefix to distinguish from output
- [ ] AI directives (if any) are in HTML comments `<!-- like this -->`
- [ ] Status reflects current reality (not copy-pasted from template)#

### Files to Optimize

```
txtdocs/                                         # Workspace-level reports├── bash-migration-final-report.md            → verify frontmatter, add tags├── bash-scripts-audit-results.md             → verify frontmatter, add tags├── bash-scripts-list-context.md              → verify frontmatter, add tags├── bash-fix-implementation-plan.md           → verify frontmatter, add tags├── project-docs/<project>/*.md              → verify each has frontmatterprojects/Bash/docs/                                    # Bash project-specific docs├── AGENTS.md                                 → add frontmatter, optimize├── ARCHITECTURE.md                           → add frontmatter, optimize├── CODE_STYLE.md                             → add frontmatter, optimize├── README.md                                 → add frontmatter, optimize├── bash-scripts-safety-audit.md              → add frontmatter, optimize├── FINAL-SUMMARY.md                          → add frontmatter, optimize├── MIGRATION-GUIDE.md                        → add frontmatter, optimize└── phase5-verification-report.md             → add frontmatter, optimize
```

### AI-Readiness Scoring ScriptCreate `projects/Bash/scripts/score-docs.sh` that scores every `.md` file onAI-readiness:| Criterion                             | Points             | Detection Method                                  || ------------------------------------- | ------------------ | ------------------------------------------------- || YAML frontmatter present              | +20                | grep for `^---$` between first 5 lines            || Summary paragraph in first 3 lines    | +15                | non-empty paragraph within first 3 lines after H1 || Language-tagged code blocks           | +10 each (max +30) | count ` ```lang ` patterns                        || Relative cross-refs that resolve      | +10 each (max +20) | check relative paths with `test -f`               || H2/H3 break every <200 lines          | +15                | count lines between headers                       || **Penalty**:

> 500 lines with no H2/H3 | −20                | wall-of-text detection                            |Score threshold: **≥70** = AI-ready, **40–69** = needs work, **<40** = rewriterequired.Output `docs/ai-readiness-report.md` with per-file scores and specificremediation per file.

### Doc Symmetry Validator

Cross-reference Phase 5 output against the generator-orchestrator manifestexpectation from `repo.prompts.md`:```yamlRequired artifacts per project (11 files):    technology-stack.md, folder-structure.md, architecture.md,    project-workflow.md, code-exemplars.md, copilot-instructions.md, readme.md,    artifact-manifest.json, cross-linking-report.md, validation-report.md,    execution-summary.md```For each project under `docs/project-docs/<name

> /`:- Check which of the 11 required artifacts exist- Flag missing files as`gap`- Flag extra files as`bonus`- Generate`docs/doc-symmetry-report.md` with project-by-project completeness  matrix- For projects with <8/11 artifacts, recommend re-running generator-orchestrator

### Phase 6: Final Verification

- [ ] All 54 scripts verified under `projects/Bash/`
- [ ] Patch dependency graph saved to `docs/patch-dependency-graph.md`
- [ ] AI-readiness report saved to `docs/ai-readiness-report.md`
- [ ] Doc symmetry report saved to `docs/doc-symmetry-report.md`
- [ ] All active patches pass `git apply --check`
- [ ] All active patches have enhanced versions in `patches/enhanced/`
- [ ] All missing patches created in `patches/new/`
- [ ] All docs in folders: workspace reports in `docs/`, project docs in      `docs/project-docs/`, Bash docs in `Bash/docs/`
- [ ] Every `.md` file has YAML frontmatter and summary paragraph
- [ ] No dead or misplaced documentation files
- [ ] `git status` cleanGenerate `/workspace-consolidation-summary.md` with counts:```text========================================WORKSPACE CONSOLIDATION COMPLETE========================================Scripts under Bash:             54/54Patches active:                 4 (enhanced in patches/enhanced/)Patches new:                    N (in patches/new/)Patches obsolete:               3 (in patches/obsolete/)Docs in proper folders:         N/NDocs with frontmatter:          N/NAI-readiness score >=70:        N/NProjects with full 11 docs:     N/N========================================```---

## Steps

1. **Phase 1**: Verify canonical script layout — scan for scripts outside `projects/projects/Bash/`, move misplaced docs, verify counts
2. **Phase 2**: Debug all patches — `git apply --check` each, diagnose failures, reclassify obsolete
3. **Phase 3**: Enhance all patches — enrich commit messages, add metadata, normalize line endings, build dependency graph
4. **Phase 4**: Create missing patches — gap analysis, create docs/config/consistency/bugfix patches
5. **Phase 5**: Document organization — move all reports to `docs/`, add YAML frontmatter, optimize for AI-readiness
6. **Phase 6**: Final verification — all scripts under Bash/, all patches enhanced, all docs scored

## Tasks

- [ ] Phase 1: Verify canonical script layout (54 scripts under projects/Bash/)- [ ] Phase 2: Debug all patches (active + obsolete)- [ ] Phase 3: Enhance all active patches + build dependency graph- [ ] Phase 4: Create missing patches (docs, config, consistency)- [ ] Phase 5: Organize all docs + add frontmatter + AI-readiness scoring- [ ] Phase 6: Final verification (all checks pass)- [ ] Generate workspace-consolidation-summary.md

## Actions

- `search_files(pattern="*.sh", target="files")` — Find all bash scripts
- `terminal("git apply --check <patch>")` — Test patch applicability
- `terminal("git merge-base --is-ancestor <a> <b>")` — Detect patch dependencies
- `write_file(path, content)` — Write enhanced patches and reports
- `patch(path, old_string, new_string)` — Apply targeted doc fixes
- `terminal("grep -q '^---$' <file>")` — Check frontmatter presence
- `skill_view(name="git-patch-management")` — Load patch management skill
- `skill_view(name="project-consolidation")` — Load consolidation skill

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Context

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State clearly when something fails.

## Phases

### Phase 1: Intake

- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute

- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify

- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off

- Return final artifact or findings clearly.
- Stop once the requested result is delivered.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions
