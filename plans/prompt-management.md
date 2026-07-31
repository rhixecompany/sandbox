# 🎯 PROMPT LIBRARY MANAGEMENT & DE-DUPLICATION PLAN

**Created:** 2026-07-31 18:51 UTC
**Approved:** 2026-07-31 (user: "you are approved create,validate the plan at plans/prompt-management.md and only then output and explain it to me")
**Status:** ✅ COMPLETED — all 6 phases executed; feature branch merged to `development` via PR #9 (commit `edeb8228`)
**Target:** `plans/prompt-management.md`
**Repository:** SandBox (rhixecompany/sandbox)
**Scope:** ~717 prompt files in `.github/prompts/`

---

## 📌 PLAN OVERVIEW

A comprehensive, phased plan for managing the SandBox prompt library.

### 6 Sequential Phases

| Phase | Duration | Risk | Focus |
|-------|----------|------|-------|
| **1. Inventory** | 30 min | Low | Scan, parse, consolidate all 717 prompts |
| **2. Analysis** | 45 min | Low | Detect duplicates, overlaps, templates |
| **3. Dry-Run** | 60 min | Medium | Apply enhancements (session-only) |
| **4. Verification** | 30 min | Low | Validate syntax, lint, spell, cross-refs |
| **5. Apply & Commit** | 35 min | High | Push to repository on feature branch |
| **6. Cleanup** | 10 min | Low | Archive artifacts, final report |

**Total Time:** 4.5-5 hours (including user review gates)

---

## 🚀 KEY FEATURES OF THIS PLAN

### ✅ Three User Approval Gates
- **Gate 1** (After Phase 2): Review analysis → approve enhancement strategy
- **Gate 2** (After Phase 4): Review changelog + diffs → approve repository application
- **Gate 3** (After Phase 5): Review PR → merge feature branch

### ✅ DRY Principles (Don't Repeat Yourself)
- Extract shared templates (not aggressive merging)
- Merge ONLY exact text duplicates (safe)
- Flag semantic overlaps for manual review (preserves intent)

### ✅ Non-Destructive Approach
- All changes happen in session workspace first
- Repository untouched until Phase 5 approval
- Full audit trail (changelog, diffs, commit message with stats)

### ✅ Comprehensive Verification
- **Critical:** YAML syntax, Markdown syntax, cross-reference validation
- **High:** markdownlint-cli2, cspell spell-check
- **Medium:** Behavioral testing (optional)

### ✅ Rollback Strategy
- If issues discovered: `git revert` feature branch
- Session artifacts preserved for re-review
- Zero impact until user explicitly approves Phase 5

---

## 📊 DETAILED DELIVERABLES

### Phase 1 Outputs
- `prompt-management-export.txt` (~10-50 MB consolidated export)
- `inventory-report.md` (human-readable stats)
- `prompts-index.json` (machine-readable index)

### Phase 2 Outputs
- `analysis-manifest.json` + `.md` (findings + recommendations)
- `duplicate-clusters.json` (exact duplicates grouped)
- `semantic-overlap-flags.json` (for manual review)
- `template-candidates.json` (proposed templates)

### Phase 3 Outputs
- Session copies of enhanced prompts
- `.github/prompts/templates/` directory (with extracted templates)
- `CHANGELOG.json` + `CHANGELOG.md` (all changes documented)
- `diffs/` directory (before/after for each file)

### Phase 4 Outputs
- `VERIFICATION_REPORT.json` + `.md`
- Individual check reports (YAML, Markdown, lint, spell, cross-refs)

### Phase 5 Outputs
- Feature branch: `feat/root/prompt-library-enhancement`
- Commit with full audit trail + Co-authored-by trailer
- `POST_APPLY_VERIFICATION.json`

### Phase 6 Outputs
- Archived session artifacts
- `FINAL_REPORT.md` (summary + future recommendations)

---

## 🎯 STRATEGIC DECISIONS MADE

1. **Duplication Strategy**
   - ✓ Extract shared templates (DRY)
   - ✓ Merge exact duplicates (safe, low-risk)
   - ✓ Flag semantic overlaps (manual review only)

2. **Verification Depth**
   - ✓ Critical + High priority checks MUST pass
   - ✓ Medium priority optional (behavioral testing)

3. **Repository Changes**
   - ✓ Feature branch on `development`
   - ✓ Full audit trail in commit
   - ✓ Co-authored-by trailer included

4. **User Control**
   - ✓ Three approval gates
   - ✓ All manifests available for review
   - ✓ Rollback ready if issues

---

## ⏱️ TIMELINE

```
Day 1:
├─ Phase 1 (Inventory): 30 min
├─ Phase 2 (Analysis): 45 min
├─ 🚪 Gate 1 (User Review): 15-30 min
├─ Phase 3 (Dry-Run): 60 min
├─ Phase 4 (Verification): 30 min
├─ 🚪 Gate 2 (User Review): 15-30 min
├─ Phase 5 (Apply): 35 min
├─ Phase 6 (Cleanup): 10 min
└─ 🚪 Gate 3 (User Merge Decision): Async

Total: 4.5-5 hours (excluding Gate 3 merge)
```

---

## ✅ SUCCESS CRITERIA

- ✓ All 717 prompts consolidated and exported
- ✓ Exact duplicates merged
- ✓ Semantic overlaps flagged (NOT auto-merged)
- ✓ Templates extracted (DRY)
- ✓ Frontmatter normalized
- ✓ All verification checks pass
- ✓ **ZERO loss of prompt intent**
- ✓ Feature branch ready for merge
- ✓ Full audit trail documented

---

## 🎓 HOW TO READ THIS PLAN

| Section | Purpose |
|---------|---------|
| **Executive Summary** | High-level goals and principles |
| **Quick Start** | 3 approval gates and timeline |
| **Phase Breakdown** | Detailed tasks, deliverables, and risks for each phase |
| **Timeline & Effort** | How long each phase takes |
| **Success Criteria** | How to know we succeeded |
| **Assumptions & Constraints** | What we assume about the codebase |
| **Rollback Strategy** | How to undo changes if needed |
| **Todos & Tracking** | 27 tasks organized by phase |

---

## 📋 PHASE BREAKDOWN

### Phase 1: INVENTORY (30 min, Low Risk)
**Objective:** Understand the current prompt library landscape

**Tasks:**
- Scan `.github/prompts/` recursively for all `.md` files
- Parse YAML frontmatter from each file (name, title, version, tags, description, author)
- Create consolidated export by concatenating all prompts
- Generate inventory report with statistics (file count, size distribution, completeness)

**Deliverables:**
- `prompt-management-export.txt` (~10-50 MB consolidated export)
- `inventory-report.md` (human-readable stats and analysis)
- `prompts-index.json` (machine-readable index with all frontmatter)

**Owner:** Agent
**Status:** ✅ Complete (verified 2026-07-31 — see FINAL_REPORT.md)

---

### Phase 2: ANALYSIS (45 min, Low Risk)
**Objective:** Identify duplicates, overlaps, and enhancement opportunities

**Tasks:**
1. **Detect Exact Duplicates** — Hash entire body of each prompt (SHA256), group by hash
2. **Extract Frontmatter Patterns** — Analyze YAML structure, identify repeated patterns
3. **Flag Semantic Overlaps** (Manual Review Required) — Compare names/titles/tags using similarity scoring, flag for USER REVIEW
4. **Identify Template Candidates** — Find shared sections, propose extraction to `.github/prompts/templates/`
5. **Produce Analysis Manifest** — Combine all findings into single comprehensive report

**Deliverables:**
- `analysis-manifest.json` (machine-readable findings)
- `analysis-manifest.md` (human-readable report)
- `duplicate-clusters.json` (exact duplicates grouped)
- `semantic-overlap-flags.json` (flagged for manual review)
- `template-candidates.json` (proposed templates)

**⚠️ GATE 1:** User reviews and approves analysis before proceeding to Phase 3

---

### Phase 3: DRY-RUN ENHANCEMENT (60 min, Medium Risk)
**Objective:** Apply intelligent enhancements in session workspace only

**Tasks:**
1. **Extract Templates** — Create `.github/prompts/templates/` (session only), extract shared sections, update references
2. **Merge Exact Duplicates** — Keep one canonical prompt per duplicate cluster, mark others for deletion or redirect
3. **Normalize Frontmatter** — Standardize YAML: name (kebab-case), title, version, tags, description; normalize tag format
4. **Update Cross-References** — Update paths, add "Supersedes" field, update links
5. **Create Enhancement Changelog** — Document every change: type, file, rationale

**Deliverables:**
- Session copies of enhanced prompts (repository remains untouched)
- `.github/prompts/templates/` (session only)
- `CHANGELOG.json` + `CHANGELOG.md`
- `diffs/` directory with before/after for each changed file

**⚠️ GATE 2:** User reviews changelog + diffs before applying to repository

---

### Phase 4: VERIFICATION (30 min, Low Risk)
**Objective:** Validate all enhanced prompts with comprehensive checks

**Critical Checks (Must Pass):**
- ✓ YAML frontmatter syntax validation
- ✓ Markdown syntax validation
- ✓ Cross-reference deadlink validation

**High-Priority Checks:**
- ✓ markdownlint-cli2 (MD013, MD046, MD048)
- ✓ cspell spell-check

**Medium-Priority Checks (Optional):**
- ✓ Behavioral testing (if automated harness exists)

**Deliverables:**
- `VERIFICATION_REPORT.json` (machine-readable results)
- `VERIFICATION_REPORT.md` (human-readable with remediation)
- Individual check reports (YAML, Markdown, lint, spell, cross-refs)

**Requirement:** All Critical + High priority checks MUST pass

---

### Phase 5: APPLY & COMMIT (35 min, High Risk)
**Objective:** Apply approved changes to repository and commit with audit trail

**Prerequisites:**
- ✓ User approval of analysis + enhancements + verification
- ✓ No conflicts with other branches
- ✓ Feature branch: `feat/root/prompt-library-enhancement`

**Tasks:**
1. Create feature branch based on `development`
2. Apply enhanced prompts to `.github/prompts/`
3. Remove exact duplicates
4. Create `.github/prompts/templates/` with extracted templates
5. Commit with full audit trail and Co-authored-by trailer
6. Re-run post-apply verification

**Commit Message Template:**
```
feat: enhance prompt library (de-duplicate, extract templates, normalize frontmatter)

Changes:
- Extracted X templates to .github/prompts/templates/
- Merged Y exact duplicate prompts
- Normalized frontmatter for Z prompts
- Updated W cross-references

Verification:
- All YAML frontmatter valid
- All Markdown syntax valid
- markdownlint: X warnings (reviewed)
- cspell: Y items (reviewed)
- Cross-references: All valid

See CHANGELOG.md for detailed changes per prompt.

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>
```

**Deliverables:**
- Feature branch on origin
- Commit with full audit trail
- `POST_APPLY_VERIFICATION.json`
- Ready for PR review and merge

---

### Phase 6: CLEANUP (10 min, Low Risk)
**Objective:** Archive artifacts and summarize results

**Tasks:**
1. Archive session artifacts (manifests, reports, diffs)
2. Generate final report with summary, statistics, and recommendations

**Deliverables:**
- Archived session artifacts (optional user export)
- `FINAL_REPORT.md` (summary + future recommendations)

---

## ⏱️ TIMELINE & EFFORT

**Total Estimated Time: 4.5 - 5 hours** (including user review gates)

| Phase | Duration | Cumulative | Owner |
|-------|----------|-----------|-------|
| 1. Inventory | 30 min | 30 min | Agent |
| 2. Analysis | 45 min | 1h 15min | Agent |
| User Review Gate 1 | 15-30 min | 1h 30-45min | User |
| 3. Dry-Run Enhancement | 60 min | 2h 30-45min | Agent |
| 4. Verification | 30 min | 3h 00-45min | Agent |
| User Review Gate 2 | 15-30 min | 3h 15min-1h 15min | User |
| 5. Apply & Commit | 35 min | 3h 50-4h 50min | Agent |
| 6. Cleanup | 10 min | 4h 00-5h 00min | Agent |

**Parallelizable:** Frontmatter parsing, duplicate detection, and verification checks can run in parallel

**Bottlenecks:** User review gates, large file I/O, verification on 717 files

---

## ⚠️ ASSUMPTIONS & CONSTRAINTS

**Assumptions:**
1. `.github/prompts/` contains `.md` and `.prompt.md` files with YAML frontmatter
2. Most YAML is valid (verification catches errors)
3. Prompts are independent; no circular cross-references
4. User prefers DRY (extract templates) over aggressive merging
5. Session workspace can hold ~100 MB temporary copies
6. Repository accessible; git branch creation allowed

**Constraints:**
1. No behavioral testing unless automated harness exists
2. Large scope (717 files) requires careful management
3. Prompt intent must be preserved
4. Semantic changes require manual review
5. All changes must be audit-trailed

**Risks & Mitigations:**
| Risk | Severity | Mitigation |
|------|----------|-----------|
| Merging loses prompt variants | High | Flag overlaps for manual review only |
| Cross-reference breaks | Medium | Validation phase catches deadlinks |
| Repository conflicts | Medium | Use feature branch, coordinate timing |
| Large export unwieldy | Low | Also provide summary + JSON index |
| Performance on 717 files | Medium | Pilot first to estimate |

---

## 🛡️ ROLLBACK STRATEGY

**If issues discovered after applying:**
1. Revert feature branch (`git revert`)
2. Session artifacts preserved for re-review
3. Repository state restored
4. Post-revert verification confirms no issues

**Prevention:**
- Comprehensive verification phase catches issues early
- Post-apply verification double-checks applied changes
- User review gates allow approval/rejection before committing
- Dry-run approach = zero impact until Phase 5 approval

---

## 📊 TODOS & TRACKING

**Total Todos:** 27 tasks organized by phase

**Phase 1:** 4 todos (inventory-prompts, parse-frontmatter, create-consolidated-export, generate-inventory-report)

**Phase 2:** 5 todos (detect-exact-duplicates, extract-frontmatter-patterns, flag-semantic-overlaps, identify-template-candidates, produce-analysis-manifest)

**Gate 1:** 1 user approval

**Phase 3:** 5 todos (extract-templates-dryrun, merge-exact-duplicates-dryrun, normalize-frontmatter-dryrun, update-cross-references-dryrun, create-enhancement-changelog)

**Phase 4:** 6 todos (validate-yaml-frontmatter, validate-markdown-syntax, lint-with-markdownlint, spell-check-with-cspell, validate-cross-references, produce-verification-report)

**Gate 2:** 1 user approval

**Phase 5:** 5 todos (create-feature-branch, apply-changes-to-repository, commit-changes, post-apply-verification, push-to-origin)

**Phase 6:** 2 todos (archive-session-artifacts, generate-final-report)

---

## 🚀 NEXT STEPS

**Plan is finalized. Ready to proceed with Phase 1 (Inventory).**

To begin:
1. ✅ Pilot first (50-100 files) or full scale (all 717)? → **Full scale (all 717)** per standing goal
2. ✅ Ready to proceed? → **Approved**

**Session workspace:** All artifacts (manifests, reports, diffs, etc.) will be saved to `.copilot/session-state/` during execution.

---

**Plan created:** 2026-07-31 18:51 UTC
**File location:** `plans/prompt-management.md`
**Status:** ✅ COMPLETED — implementation verified 2026-07-31 21:20 UTC (see FINAL_REPORT.md; PR #9 merged)
