# SandBox Aggressive Cleanup & Consolidation Plan

> **Status:** ✅ COMPLETED — All 10 phases executed and verified  
> **Created:** 2026-06-28  
> **Completed:** 2026-06-28  
> **Scope:** tool/, thoughts/, judge_results/, .github/scripts/, .agents/, .hermes/, docs/, root .md files  
> **Rule:** Strict sequential — each phase completes and is verified before next begins

---

## Phase 0: Prerequisites & Safety (5 min)

### 0.1 Verify plan is complete and reviewed
- [ ] Read this entire plan once before starting execution
- [ ] Confirm no destructive action without verification

### 0.2 Pre-cleanup snapshot
```bash
cd ~/Desktop/SandBox
git stash list  # check for stashed changes
git status --short | head -30  # check working tree
```

---

## Phase 1: Migrate `.agents/skills/smithery-ai-cli/SKILL.md` to Hermes Skills (10 min)

**Objective:** Install the smithery-ai-cli skill into the Hermes skills library properly, then clean up .agents directory.

### 1.1 Read the skill file
```bash
cat ~/Desktop/SandBox/.agents/skills/smithery-ai-cli/SKILL.md
```

### 1.2 Install via Hermes CLI (preferred)
```bash
hermes skills install ~/Desktop/SandBox/.agents/skills/smithery-ai-cli/SKILL.md
# OR manually copy:
cp ~/Desktop/SandBox/.agents/skills/smithery-ai-cli/SKILL.md ~/AppData/Local/hermes/skills/smithery-ai-cli/SKILL.md
```

### 1.3 Update `skills-lock.json` reference
- Read current skills-lock.json
- Update path from `.agents/skills/smithery-ai-cli/SKILL.md` to Hermes skills path

### 1.4 Delete `.agents/` directory (empty after migration)
```bash
rm -rf ~/Desktop/SandBox/.agents
```

### 1.5 Verify
- [ ] Skill installed in Hermes skills library
- [ ] skills-lock.json updated
- [ ] `.agents/` directory deleted

---

## Phase 2: Migrate Python Scripts from `.github/scripts/` to Hermes Scripts (15 min)

**Objective:** Copy all unique Python scripts from `.github/scripts/` to `~/AppData/Local/hermes/scripts/`, update any references, then clean up.

### 2.1 Inventory scripts to migrate
39 unique Python files in `.github/scripts/` not present in hermes/scripts:
```
apply_vscode_customizations.py  audit_prompts.py  audit_vscode_config.py
audit_vscode_config_v2.py  batch_remediate_42_59.py  batch_rewrite_worst.py
build_path_mapping.py  categorize_skills.py  configure_hermes.py
consolidate_skills.py  copilot_mcp_server.py  create_missing_memories.py
create_missing_souls.py  dedupe_skills.py  dev-init-code-samples.py
docs-inventory-report.py  fix-skills.py  fix_eslint_mismatches.py
fix_fail_skills.py  fix_orphaned_brackets.py  fix_prompts.py
fix_yaml_frontmatter.py  generate_context_files.py  generate_skills.py
generate_vscode_audit_report.py  generate_vscode_configs.py  hello.py
hello_world.py  merge_config.py  merge_skill.py  score-docs.py
skills-audit.py  trim_banking.py  trim_remaining.py
trim_research_reports.py  trim_research_reports_final.py
update_agents_md.py  validate_vscode_configs.py  validate_vscode_json.py
```

Plus 2 with different sizes in both locations:
- `batch_remediate.py` (.github=5923B, hermes=7892B — keep larger)
- `batch_skill_judge.py` (.github=9354B, hermes=10431B — keep larger)

Plus 1 shell script: `list-cli-tools.sh`

### 2.2 Copy unique scripts to hermes scripts
```bash
# For each unique .py file:
cp ~/Desktop/SandBox/.github/scripts/<file>.py ~/AppData/Local/hermes/scripts/<file>.py
```

### 2.3 For overlapping files, compare and keep the larger/better version
- `batch_remediate.py`: 7892B (hermes) > 5923B (.github) → keep hermes version
- `batch_skill_judge.py`: 10431B (hermes) > 9354B (.github) → keep hermes version

### 2.4 Search for references to `.github/scripts/` paths and update
Use `search_files` across the workspace for references to `.github/scripts/` or `github/scripts/` paths → update to hermes scripts path.

### 2.5 Verify
- [ ] All 39 Python scripts copied to hermes/scripts/
- [ ] 2 overlapped files resolved (keep larger)
- [ ] `list-cli-tools.sh` also migrated
- [ ] All references to old paths updated
- [ ] `.github/scripts/` still intact (scripts were COPIED, not moved — allow deletion later)

---

## Phase 3: Clean Up `judge_results/` — Consolidate to Canonical Set (10 min)

**Objective:** Judge results have 75 files with two interleaved runs (~800B compact + ~1200B detailed). Consolidate to one canonical run.

### 3.1 Categorize files
- **37 batch files (5-zero padding, ~800B each):** Compact summary — `batch_XXXXX_results.md`
- **37 batch files (4-zero padding, ~1200B each):** Detailed results — `batch_XXXX_results.md`  
- **1 TSV:** `all_results.tsv` (41KB)
- **2 reports:** `remediation-log.md`, `summary.md`

### 3.2 Determine which set to keep
- The 4-zero-padded set (0001-0035) is more detailed (larger files) — **keep this set**
- The 5-zero-padded set (00001-00035) has the same data in compact form — **delete**
- Keep: `summary.md`, `remediation-log.md`, `all_results.tsv`

### 3.3 Delete compact duplicates
```bash
cd ~/Desktop/SandBox/judge_results
rm batch_00001_results.md batch_00002_results.md ... batch_00035_results.md
```

### 3.4 Rename canonical set to clean numbering (optional)
If desired, `batch_0001_results.md` → `batch_001_results.md`

### 3.5 Verify
- [ ] Reduced from 75 files → 40 files (37 detailed + 3 reports)
- [ ] ~30KB saved

---

## Phase 4: Clean Up `tool/agent-repos/` (5 min)

**Objective:** Remove shallow clone clutter.

### 4.1 Clean up `.git/` from the shallow clone
```bash
rm -rf ~/Desktop/SandBox/tool/agent-repos/copilot-docs/.git
```

### 4.2 Keep or delete the docs
- `LICENSE.txt` (19KB) — Apache 2.0 license
- `README.md` (362B) — minimal readme
- These are reference docs. If not needed, delete: `rm -rf ~/Desktop/SandBox/tool`

### 4.3 Delete `.logs/subtask2.log` (agent artifact)

### 4.4 Verify
- [ ] tool/ cleaned up or deleted
- [ ] Empty parent directories removed

---

## Phase 5: Clean Up `thoughts/plans/` — Debug Plans (5 min)

**Objective:** Delete stale debug plan files.

### 5.1 Inventory 9 debug files
```
audit-skills-judge-fix-debug.md  bash-scripts-modernization-plan.md
multi-agent-research-template-debug.md  prompt-migration-debug.md
prompts-debug.md  prompts-md-debug.md  sample-prompt-debug.md
sync-hermes-copilot-codex-debug.md  test-providers-models-debug.md
```

### 5.2 Check for references
Use `search_files` to check if any of these files are referenced elsewhere.

### 5.3 Delete all debug files
```bash
rm ~/Desktop/SandBox/thoughts/plans/*.md
rmdir ~/Desktop/SandBox/thoughts/plans  # if empty
rmdir ~/Desktop/SandBox/thoughts        # if empty
```

### 5.4 Verify
- [ ] Debug files deleted
- [ ] Empty directories removed

---

## Phase 6: Clean Up `.hermes/` Plans & Scripts (10 min)

**Objective:** Review `.hermes/` directory, consolidate/remove stale plans.

### 6.1 Inventory `.hermes/` contents
- `approvals/` — 2 approval files (4KB total)
- `plans/` — 8 plan files + 1 triage + 1 debugger (~90KB total)
- `scripts/` — 1 shell script (2.5KB)
- 3 shell scripts at root + mcp-install-plan.md

### 6.2 Triage
- **Keep:** `approvals/`, `hook-health-check.sh`, `full-health-check.sh`, `e2e-session-test.sh`, `bulk-install-skills.sh`
- **Review:** Old plans that are complete → archive or delete
- **Delete:** Plans whose tasks are fully executed (most of them)

### 6.3 Move useful scripts to hermes scripts root if not already there
- `quarantine_skills.sh` → `~/AppData/Local/hermes/scripts/`

### 6.4 Delete empty directories after cleanup

### 6.5 Verify

---

## Phase 7: Clean Up `docs/` — Triage 330 Items (20 min)

**Objective:** Separate real docs from pipeline artifacts. Keep architecture, MCP, and reference docs; delete pipeline temp artifacts.

### 7.1 Categorize docs into groups

**KEEP** (permanent reference):
- `01-07` numbered docs (Hermes guides)
- `mcp-servers/` directory (MCP server docs)
- `Project_Architecture/` (project blueprints)
- `INDEX.md`, `QUICK_REFERENCE.md`
- `categorization-plan.md`, `local-skills.md`
- `prompt-orchestration-*.md` (if actively referenced)
- `prompt-batch-audit-report.md`, `prompt-inventory.md`
- `provider-benchmark-report.md`
- `orchestrator-progress.md`, `orchestrator-verification.md`

**DELETE** (pipeline artifacts — one-time runs):
- `*-issues-context.md`, `*-fix-issues-context.md`, `*-verify-context.md`, `*-context.md`
- `*-context-map.md`
- `audit-skills-judge-fix-*.md`
- `sync-hermes-copilot-codex-*.md`
- `test-providers-models-*.md` (except benchmark.md)
- `prompt-migration-*.md` (except batch-audit-report)
- `prompts-*.md` (except inventory)
- `dev-init-*.md`
- `sandbox-*.md`
- `bash-*-report.md`
- `WORKFLOW_*.txt`, `PHASE-*.txt`
- `dirs_to_delete*.txt`
- `patch-*.{md,json}`
- `final-verification.*`
- `per-project-research-queries.md`, `per-repo-*.md`
- `research-doc-cross-reference.md`
- `consolidation-report.md`, `workspace-consolidation-*.md`
- `skill-consolidation-report.md`, `skill-dedup-*.md`
- `soul-audit-verification-report.md`
- `reports/`, `hermes-docs/`, `plans/` subdirectories (if stale)

**REVIEW** (keep if actively used):
- `ai-readiness-report.md`
- `hermes-current-state.md`
- `multi-agent-research-template-debug.md`
- `tools/` subdirectory

### 7.2 Execute deletions
```bash
cd ~/Desktop/SandBox/docs
# Delete pipeline artifact groups
```

### 7.3 Clean up empty subdirectories
```bash
find docs -type d -empty -delete
```

### 7.4 Verify
- [ ] Pipeline artifacts deleted (~100-150 files removed)
- [ ] Architecture and MCP docs preserved
- [ ] No empty directories remaining
- [ ] All referenced docs still accessible

---

## Phase 8: Clean Up Root Markdown Files (5 min)

**Objective:** Delete or archive stale root .md files.

### 8.1 Triage root .md files

**KEEP:**
- `.hermes.md` — project config
- `AGENTS.md` — agent instructions
- `HERMES_PROFILE_REPORT.md` — profile audit
- `PROJECT_RULES.md` — project rules
- `README.md` — project readme
- `SESSION_REPORT.md` — session continuity

**DELETE (superseded/stale):**
- `architecture.md` (798B) — superseded by docs/Project_Architecture/
- `cli-tools.md` (6773B) — one-time CLI inventory, stale
- `dev-imp-report.md` (4774B) — old report
- `folder-structure.md` (1682B) — superseded by docs/folder-structure.md
- `tech-stack.md` (451B) — superseded by docs/tech-stack.md or docs/Project_Architecture/

**ARCHIVE (move to docs/archive/ if desired):**
- `RESEARCH_REPORT.md` (43KB) — large, might still be useful

### 8.2 Delete/archive files
```bash
cd ~/Desktop/SandBox
# delete stale root .md files
```

### 8.3 Verify
- [ ] Only 8 essential .md files remain at root
- [ ] No broken references from other files

---

## Phase 9: Delete All Empty Directories (5 min)

### 9.1 Find and remove empty dirs
```bash
cd ~/Desktop/SandBox
find . -type d -empty -not -path './.git/*' -delete
find . -type d -empty -not -path './.git/*'  # verify none remain
```

### 9.2 Verify

---

## Phase 10: Final Verification (5 min)

### 10.1 Check git status
```bash
cd ~/Desktop/SandBox
git status --short | wc -l  # should be manageable
git diff --stat  # see what changed
```

### 10.2 Verify no broken references
- [ ] `skills-lock.json` references valid paths
- [ ] `.github/` still functional (instructions, agents, workflows preserved)
- [ ] No files reference deleted paths (unless updated in earlier phases)

### 10.3 Summary report
- Files deleted/consolidated
- Disk space saved
- Directories cleaned

---

## Execution Order (Strict Sequential)

Phase 0 → Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6 → Phase 7 → Phase 8 → Phase 9 → Phase 10

**Each phase must be fully verified before the next begins.**

## Disk Savings Estimate

| Area | Current Size | After | Savings |
|------|-------------|-------|---------|
| judge_results/ | 120KB | ~90KB | ~30KB |
| thoughts/ | ~40KB | 0 | ~40KB |
| tool/ | ~25KB | 0 | ~25KB |
| .agents/ | 4KB | 0 | ~4KB |
| docs/ | ~5MB | ~3MB | ~2MB |
| Root .md files | ~70KB | ~50KB | ~20KB |
| .hermes/ | ~100KB | ~50KB | ~50KB |
| **Total** | **~5.4MB** | **~3.2MB** | **~2.2MB** |
