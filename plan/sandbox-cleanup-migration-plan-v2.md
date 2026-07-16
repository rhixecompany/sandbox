# SandBox Aggressive Cleanup & Migration Plan — v2.0

> **Objective:** Clean workspace root, fix all Markdown issues across the entire repo, migrate scripts to Hermes standard location, then validate everything.

---

## Phase 0: Safety & Baseline (5 min)

- [ ] `git status --short` → capture baseline
- [ ] `git stash push -u -m "pre-cleanup-baseline"` (includes untracked)
- [ ] Verify stash exists: `git stash list`

---

## Phase 1: Delete Specified Root Directories & Files (15 min)

> Delete **only** these exact paths (skip if missing). Do NOT touch `.github/`, `.hermes/`, `.vscode/`, `projects/`, `prompts/`, `scripts/`, `requirements.txt`, `package.json`, `tsconfig.json`, `.editorconfig`, `.gitignore`, `.gitmodules`, `AGENTS.md`, `.hermes.md`, `README.md`, `SESSION_REPORT.md`.

| Target | Type | Notes |
| -------- | ------ | ------- |
| `.playwright-mcp/` | dir | old MCP server cache |
| `.tmp/` | dir | temp workspace |
| `benchmark_output/` | dir | old benchmark runs |
| `benchmark_results/` | dir | old benchmark runs |
| `docs/` | dir | will be regenerated from canonical sources |
| `final_work/` | dir | stale output |
| `judge_results/` | dir | skill judging artifacts |
| `plan/` | dir | plans moved to `.hermes/plans/` |
| `reports/` | dir | old audit reports |
| `results/` | dir | generic results dump |
| `thoughts/` | dir | scratchpad |
| `dev-imp-report.md` | file | stale root report |
| `MEMORY_DUMP.md` | file | stale root dump |
| `lcs.py` | file | orphan script |
| `greeting.py` | file | orphan script |
| `generate_skills.py` | file | migrate → don't delete yet |
| `_agents_fix_discover.py` | file | migrate → don't delete yet |
| `_agents_fix_report.py` | file | migrate → don't delete yet |
| `nvidia_nim_models.json` | file | stale data |
| `opencode_zen_models.json` | file | stale data |
| `openrouter_models.json` | file | stale data |
| `skill_inventory.json` | file | stale data |
| `skill_name_to_path.json` | file | stale data |
| `skills-lock.json` | file | stale data |
| `temp_models_paths.txt` | file | stale data |
| `bun.lock` | file | keep (project lockfile) |
| `package.json` | file | keep |
| `tsconfig.json` | file | keep |
| `requirements.txt` | file | keep |

**Commands:**

```bash
cd ~/Desktop/SandBox
rm -rf .playwright-mcp .tmp benchmark_output benchmark_results docs final_work judge_results plan reports results thoughts
rm -f dev-imp-report.md MEMORY_DUMP.md lcs.py greeting.py nvidia_nim_models.json opencode_zen_models.json openrouter_models.json skill_inventory.json skill_name_to_path.json skills-lock.json temp_models_paths.txt
```

**Verification:** `ls -la` → only keepers remain.

---

## Phase 2: Migrate Root Scripts to Hermes Scripts Folder (10 min)

> Move these root-level Python scripts to `%LOCALAPPDATA%\hermes\scripts\` (canonical location). Update any internal references.

| Source | Destination | Action |
| -------- | ------------- | -------- |
| `generate_skills.py` | `~/AppData/Local/hermes/scripts/generate_skills.py` | move |
| `_agents_fix_discover.py` | `~/AppData/Local/hermes/scripts/_agents_fix_discover.py` | move |
| `_agents_fix_report.py` | `~/AppData/Local/hermes/scripts/_agents_fix_report.py` | move |
| `scripts/execute_workflow.py` | `~/AppData/Local/hermes/scripts/execute_workflow.py` | copy (keep local for project) |
| `scripts/*.py` (all) | `~/AppData/Local/hermes/scripts/` | copy |

**Post-move:** Search for any hardcoded paths referencing old locations and update to `%LOCALAPPDATA%\hermes\scripts\`.

```bash
# Move root scripts
mv generate_skills.py _agents_fix_discover.py _agents_fix_report.py ~/AppData/Local/hermes/scripts/

# Copy project scripts
cp scripts/*.py ~/AppData/Local/hermes/scripts/

# Update references (example)
grep -r "scripts/" --include="*.py" --include="*.md" --include="*.json" . | grep -v ".git" | grep -v node_modules
```

---

## Phase 3: List & Triage All Markdown Files (10 min)

> Inventory every `.md` file in the workspace (including subdirectories). Classify each.

```bash
cd ~/Desktop/SandBox
find . -name "*.md" -not -path "./.git/*" -not -path "./node_modules/*" > /tmp/md-inventory.txt
wc -l /tmp/md-inventory.txt
```

**Triage categories:**

| Category | Criteria | Action |
| ---------- | ---------- | -------- |
| **KEEP** | Authoritative config, active docs, AGENTS.md, README.md, SESSION_REPORT.md, .hermes.md, PROJECT_RULES.md | Preserve |
| **FIX** | Broken links, stale refs, duplicate content, formatting issues | Repair in Phase 4 |
| **ARCHIVE** | Superseded reports, old research, one-time outputs | Move to `docs/archive/` |
| **DELETE** | Empty, duplicate, or completely stale | Remove |

**Output:** `/tmp/md-triage.csv` with columns: `path,category,notes`

---

## Phase 4: Fix All Markdown Issues (30 min)

> Iterate through FIX category. Common issues:

| Issue | Fix |
| ------- | ----- |
| Broken relative links | Update to correct paths |
| References to deleted dirs (`docs/`, `plan/`, `reports/`) | Redirect to canonical locations or remove |
| Duplicate frontmatter keys | Deduplicate |
| CRLF line endings | Normalize to LF (per `.editorconfig`) |
| Trailing whitespace | Strip |
| Missing language hints on fenced code blocks | Add |
| Inconsistent heading hierarchy | Normalize (H1 → H2 → H3) |
| Stale badges/version numbers | Update or remove |

**Tooling:** Use `markdownlint-cli2` (already in toolkit) + custom scripts.

```bash
# Lint all
npx markdownlint-cli2 "**/*.md" --config .markdownlintrc.json

# Auto-fix where possible
npx markdownlint-cli2 "**/*.md" --config .markdownlintrc.json --fix
```

**Manual fixes** for semantic issues (links, refs).

---

## Phase 5: Migrate & Consolidate Canonical Docs (15 min)

> Rebuild `docs/` from authoritative sources only.

**Structure:**

```
docs/
├── Project_Architecture/        # from architecture-blueprint-generator skill
├── architecture/                # architecture blueprints per project
├── folder-structure/            # folder blueprints per project
├── tech-stack/                  # tech stack blueprints per project
├── mcp/                         # MCP server docs
├── audit/                       # current audit reports only
├── catalog/                     # MCP server catalog, API tutorials
├── references/                  # cross-ref indices
└── archive/                     # moved from Phase 3 ARCHIVE category
```

**Sources of truth:**

- `AGENTS.md` (root + each project)
- `.hermes.md`
- Skill outputs in `docs/Project_Architecture/` (already generated)
- `.github/instructions/` + `.github/agents/`

**Do NOT** copy stale pipeline artifacts.

---

## Phase 6: Update All Affected References (15 min)

> After moves/deletes, fix cross-references in:

| File Pattern | What to Update |
| -------------- | ---------------- |
| `*.md` | Internal links, image paths, doc references |
| `*.py` | Import paths, file paths, subprocess calls |
| `*.json` | Path configurations |
| `.github/workflows/*.yml` | Path filters, script paths |
| `skills-lock.json` | Skill paths |
| `.vscode/*.json` | Workspace paths |

**Script:**

```bash
# Find all references to deleted dirs
grep -r "docs/\|plan/\|reports/\|results/\|judge_results/\|thoughts/\|final_work/\|benchmark_" \
  --include="*.md" --include="*.py" --include="*.json" --include="*.yml" --include="*.yaml" \
  . 2>/dev/null | grep -v ".git" | grep -v "node_modules"
```

Fix each occurrence.

---

## Phase 7: Validate Workspace (10 min)

> Run full validation suite.

```bash
# 1. Git status clean-ish
cd ~/Desktop/SandBox
git status --short

# 2. All JSON valid
find . -name "*.json" -not -path "./.git/*" -not -path "./node_modules/*" -exec python -m json.tool {} \; >/dev/null && echo "All JSON valid"

# 3. Markdown lint clean
npx markdownlint-cli2 "**/*.md" --config .markdownlintrc.json

# 4. Python syntax
python -m py_compile scripts/*.py ~/AppData/Local/hermes/scripts/*.py 2>/dev/null && echo "Python OK"

# 5. No broken internal links (basic check)
grep -r "\[.*\](\./" --include="*.md" . | grep -v "node_modules" | while read line; do
  file=$(echo "$line" | cut -d: -f1)
  link=$(echo "$line" | grep -o ']([^)]*)' | sed 's/]//;s/(//')
  # resolve relative to file dir and check exists
done

# 6. Skills lock references valid
python -c "
import json, os
data = json.load(open('skills-lock.json'))
for k, v in data.items():
    if not os.path.exists(v): print(f'MISSING: {k} -> {v}')
"
```

---

## Phase 8: Final Verification Report (5 min)

Generate summary:

| Metric | Before | After |
| -------- | -------- | ------- |
| Root directories | 15+ | ~8 |
| Root files | 40+ | ~15 |
| Markdown files | ~300 | ~250 (deduped) |
| Broken links | X | 0 |
| Scripts in Hermes folder | 0 | 20+ |
| Disk usage | ~5.4 MB | ~3 MB |

**Commit:** `git add -A && git commit -m "chore: aggressive cleanup + script migration + markdown hygiene"`

---

## Execution Rules

1. **Strict sequential** — each phase verified before next
2. **No commits** until Phase 8 passes
3. **Rollback** = `git stash pop` if catastrophic
4. **Log** each phase output to `/tmp/cleanup-phase-{N}.log`

---

## Sign-off Checklist

- [ ] Phase 0: Baseline stashed
- [ ] Phase 1: Target dirs/files gone
- [ ] Phase 2: Scripts migrated, refs updated
- [ ] Phase 3: MD inventory + triage CSV done
- [ ] Phase 4: Markdownlint clean, manual fixes done
- [ ] Phase 5: Canonical docs rebuilt
- [ ] Phase 6: All cross-refs updated
- [ ] Phase 7: Validation suite green
- [ ] Phase 8: Summary report, commit

---

*Plan version 2.0 — created 2026-07-10*
