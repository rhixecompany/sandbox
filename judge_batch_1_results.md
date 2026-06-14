# Batch 1 Judgment Results — Core Hermes & Infrastructure

**Date:** 2026-06-14
**Profile:** code-architect
**Skills evaluated:** 7
**Evaluator:** skill-judge criteria (5 dimensions × 20 pts = 100 max)

---

## Scoring Summary

| Skill | Frontmatter (20) | Structure (20) | Content (20) | DRY (20) | References (20) | **Total** | Status |
|-------|------------------|----------------|--------------|----------|-----------------|-----------|--------|
| Chainlink | 9 | 0 | 12 | 10 | 0 | **31/100** | ❌ Rewrite |
| copilot-cli | 18 | 12 | 16 | 10 | 0 | **56/100** | ⚠️ Needs work |
| fine-tuning-with-trl | 17 | 12 | 18 | 5 | 15 | **67/100** | ⚠️ Needs work |
| hermes-breakdown | 17 | 12 | 16 | 15 | 0 | **60/100** | ⚠️ Needs work |
| hermes-hooks | 17 | 16 | 18 | 15 | 20 | **86/100** | ✅ AI-ready |
| hermes-mcp | 17 | 12 | 18 | 15 | 15 | **77/100** | ✅ AI-ready |
| hermes-skills | 14 | 14 | 16 | 15 | 20 | **79/100** | ✅ AI-ready |

**Pass rate:** 3/7 (43%) — 4 skills need remediation

---

## Detailed Findings

### 1. Chainlink — **31/100** ❌ Rewrite (<40)

| Dimension | Score | Issues |
|-----------|-------|--------|
| Frontmatter | 9/20 | Missing: `title`, `version`, `author`, `license`, `tags` array. Only `name` and `description` present. Non-standard `metadata.clawdbot` field. |
| Structure | 0/20 | No Skills Required table. No phased workflow (≥3 phases). No Pitfalls section. No Verification checklist. No reference files. |
| Content | 12/20 | Good prose coverage, but **no concrete examples/templates** (all prose). No placeholder text. |
| DRY | 10/20 | No duplicate content. SKILL.md >250 lines (225 lines) — detail should move to references. Cross-references N/A (no refs). |
| References | 0/20 | **No references/, templates/, or scripts/ directories exist.** |

**Critical failures:** Missing 5/7 frontmatter fields, zero structure compliance, no reference ecosystem.

---

### 2. copilot-cli — **56/100** ⚠️ Needs work (40-69)

| Dimension | Score | Issues |
|-----------|-------|--------|
| Frontmatter | 18/20 | ✅ All 7 required fields present. Description starts with "Use when..." ✅ |
| Structure | 12/20 | ✅ Phased workflow (3 phases). ❌ No Skills Required table. ❌ No Pitfalls section. ✅ Verification checklist present. ❌ No reference files. |
| Content | 16/20 | ✅ Concrete examples (commands, configs). ✅ No placeholder text. Good error handling notes. |
| DRY | 10/20 | SKILL.md is 250+ lines — detail should move to references. No duplicate content. |
| References | 0/20 | **No references/, templates/, or scripts/ directories.** |

**Fixes needed (Priority):**
1. **High:** Add Pitfalls section (missing dimension requirement)
2. **High:** Create references/ with at least: `references/commands.md`, `references/auth-setup.md`, `templates/acpx-config.yaml`
3. **Medium:** Move command tables and config examples to references; keep SKILL.md <250 lines

---

### 3. fine-tuning-with-trl — **67/100** ⚠️ Needs work (40-69)

| Dimension | Score | Issues |
|-----------|-------|--------|
| Frontmatter | 17/20 | ✅ name, description, version, author, license, tags present. Missing `title` field (description used instead). |
| Structure | 12/20 | ✅ Phased workflows (3 workflows with checklists). ❌ No Skills Required table. ❌ No explicit Pitfalls section (has "Common issues" but not labeled as Pitfalls). ❌ No Verification checklist. ✅ Reference files cited and exist. |
| Content | 18/20 | ✅ Excellent concrete examples (Python code, CLI). ✅ No placeholder text. ✅ Error handling (OOM, beta tuning, reward model). |
| DRY | 5/20 | ❌ **SKILL.md = 463 lines** — far exceeds 250-line limit. Detail should be in references (and some is, but not enough). |
| References | 15/20 | ✅ References cited and exist (`references/grpo-training.md`, `templates/basic_grpo_training.py`, others mentioned). ✅ Each substantive. ❌ Orphaned? Need to verify all refs are cited. |

**Fixes needed (Priority):**
1. **High:** Add `title` field to frontmatter
2. **High:** Add explicit "## Pitfalls" section (rename/merge "Common issues")
3. **High:** Add Verification checklist at end
4. **Medium:** Split SKILL.md — move workflow detail to `references/sft-training.md`, `references/dpo-variants.md`, `references/reward-modeling.md`, `references/online-rl.md`, `references/grpo-training.md` (already exist per references); keep SKILL.md as index/overview <250 lines

---

### 4. hermes-breakdown — **60/100** ⚠️ Needs work (40-69)

| Dimension | Score | Issues |
|-----------|-------|--------|
| Frontmatter | 17/20 | ✅ All 7 fields present. Description starts with umbrella description. |
| Structure | 12/20 | ✅ Phased workflow (4 phases). ❌ No Skills Required table. ❌ No Pitfalls section. ❌ No Verification checklist. ✅ Reference to absorbed skills table. |
| Content | 16/20 | ✅ Good decomposition table and workflow. ✅ No placeholder text. |
| DRY | 15/20 | ✅ SKILL.md ~130 lines (reasonable). ✅ No duplicate content. Absorbed skills documented. |
| References | 0/20 | **No references/, templates/, or scripts/ directories.** |

**Fixes needed (Priority):**
1. **High:** Add Pitfalls section
2. **High:** Add Verification checklist
3. **Medium:** Add Skills Required table (phases use `create-implementation-plan`, `writing-plans`, `executing-plans`)
4. **Medium:** Create references/ with `references/epic-template.md`, `references/feature-prd-template.md`, `references/test-strategy-template.md`

---

### 5. hermes-hooks — **86/100** ✅ AI-ready (≥70)

| Dimension | Score | Issues |
|-----------|-------|--------|
| Frontmatter | 17/20 | ✅ All 7 fields present. |
| Structure | 16/20 | ✅ Phased workflow (5 phases). ❌ No Skills Required table. ✅ Pitfalls section (extensive, 20+ items). ❌ No Verification checklist (but has "Restack Procedure" as de facto verify). ✅ Reference files exist and substantive. |
| Content | 18/20 | ✅ Excellent concrete examples (every command tested). ✅ No placeholder text. ✅ Error handling table with fixes. ✅ Platform-specific notes. |
| DRY | 15/20 | ✅ SKILL.md ~320 lines (slightly over 250, but dense reference). Cross-references consistent. Some duplicate between Pitfalls and Debug table. |
| References | 20/20 | ✅ 5 reference files: `audit-remediation.md`, `commands.md`, `config-registration-gotcha.md`, `event-payloads.md`, `hook-template.md`. All substantive, all cited. No orphans. |

**Minor improvements (Low priority):**
- Add Skills Required table (uses `hermes-setup`, `hermes-profiles`)
- Add explicit Verification checklist at end
- Trim duplicate Pitfalls ↔ Debug overlap

---

### 6. hermes-mcp — **77/100** ✅ AI-ready (≥70)

| Dimension | Score | Issues |
|-----------|-------|--------|
| Frontmatter | 17/20 | ✅ All 7 fields present. |
| Structure | 12/20 | ✅ Phased workflow (4 phases). ❌ No Skills Required table. ❌ No Pitfalls section. ❌ No Verification checklist. ✅ Reference files exist. |
| Content | 18/20 | ✅ Excellent concrete examples (YAML configs, bash commands). ✅ No placeholder text. ✅ Windows-specific troubleshooting. ✅ Security audit checklist. |
| DRY | 15/20 | ✅ SKILL.md ~300 lines (slightly over). No duplicate content. Good cross-refs. |
| References | 15/20 | ✅ 4 reference files: `commands.md`, `config-examples.md`, `windows-interactive-add.md`, `wsl2-bridge.md`. All substantive, cited. ⚠️ `wsl2-bridge.md` may be orphaned (not explicitly cited in body). |

**Fixes needed (Priority):**
1. **High:** Add Pitfalls section
2. **High:** Add Verification checklist
3. **Medium:** Add Skills Required table (uses `hermes-setup`, `hermes-hooks`, `hermes-profiles`, `hermes-plugins`, `mcp-security-audit`)
4. **Low:** Verify all 4 reference files are cited; remove or cite orphaned ones

---

### 7. hermes-skills — **79/100** ✅ AI-ready (≥70)

| Dimension | Score | Issues |
|-----------|-------|--------|
| Frontmatter | 14/20 | ✅ name, description, version, platforms, metadata (tags, category, requires_toolsets, config). ❌ Missing `title` field. ❌ Missing `author` field. ❌ Missing `license` field. |
| Structure | 14/20 | ✅ Implicit phased workflow (Procedure 1-6). ❌ No Skills Required table. ✅ Pitfalls section (extensive, 12 items). ✅ Verification section present. ✅ Reference files exist and substantive. |
| Content | 16/20 | ✅ Concrete examples (CLI commands, SKILL.md template). ✅ No placeholder text. ✅ Security scan results documented. |
| DRY | 15/20 | ✅ SKILL.md ~280 lines (reasonable). No duplicate content. Good cross-refs. |
| References | 20/20 | ✅ 7 reference files: `audit-findings-2026-06-11.md`, `audit-results.md`, `batch-install.md`, `commands.md`, `curator.md`, `skill-format.md`, `skills_install_templates.md`. All substantive, all cited. No orphans. |

**Fixes needed (Priority):**
1. **High:** Add `title`, `author`, `license` to frontmatter (currently missing 3/7 required fields)
2. **Medium:** Add Skills Required table (uses `terminal`, `file`, `skills` toolsets)

---

## Batch 1 Remediation Plan

| Skill | Priority Fixes | Estimated Effort |
|-------|----------------|------------------|
| **Chainlink** | Add 5 frontmatter fields; add phased workflow (3+ phases); add Pitfalls, Verification, Skills Required; create references/ with at least 3 files | High (needs near-rewrite) |
| **copilot-cli** | Add Pitfalls section; create references/ + 3 files; move detail to refs | Medium |
| **fine-tuning-with-trl** | Add `title` frontmatter; rename "Common issues" → "Pitfalls"; add Verification checklist; split SKILL.md to <250 lines | Medium |
| **hermes-breakdown** | Add Pitfalls; add Verification checklist; add Skills Required table; create references/ + 3 templates | Medium |
| **hermes-hooks** | Add Skills Required table; add Verification checklist; trim duplicate Pitfalls/Debug | Low |
| **hermes-mcp** | Add Pitfalls; add Verification checklist; add Skills Required table; verify ref citations | Medium |
| **hermes-skills** | Add `title`, `author`, `license` to frontmatter; add Skills Required table | Low |

---

## Files to Patch

| Skill | Files to Modify |
|-------|-----------------|
| Chainlink | `Chainlink/SKILL.md` (major); create `Chainlink/references/`, `templates/`, `scripts/` |
| copilot-cli | `copilot-cli/SKILL.md`; create `copilot-cli/references/` |
| fine-tuning-with-trl | `fine-tuning-with-trl/SKILL.md` (patch); verify references exist |
| hermes-breakdown | `hermes-breakdown/SKILL.md`; create `hermes-breakdown/references/` |
| hermes-hooks | `hermes-hooks/SKILL.md` (minor patches) |
| hermes-mcp | `hermes-mcp/SKILL.md` (patches); verify `wsl2-bridge.md` citation |
| hermes-skills | `hermes-skills/SKILL.md` (frontmatter patch) |

---

## Authorization Required

**Ready to apply patches for Batch 1.** Want me to:
1. **Proceed with all 7 skills** (high/medium priority fixes first)?
2. **Start with Chainlink** (most critical, lowest score)?
3. **Skip Chainlink** for now (needs near-rewrite; defer to dedicated session)?
4. **Adjust priorities** before patching?

**Note:** Chainlink scores 31/100 — the only skill below the 40 "Rewrite" threshold. It needs substantial restructuring, not just patches.