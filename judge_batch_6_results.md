# Batch 6 Judge Results — Skills Audit Pipeline

**Date:** 2026-06-14
**Profile:** default
**Batch:** 6 (Skills 36-42)
**Judge Skill:** skill-judge v1.1.0

---

## Summary

| # | Skill | Score | Rating | Status |
|---|-------|-------|--------|--------|
| 36 | hermes-skill-library-maintenance | 58/100 | ⚠️ Needs work | Critical: 557 lines, no structure |
| 37 | template-skill | 55/100 | ⚠️ Needs work | Missing Skills Required, pitfalls |
| 38 | using-superpowers | 61/100 | ⚠️ Needs work | Missing frontmatter fields |
| 39 | algorithmic-art | 63/100 | ⚠️ Needs work | Missing frontmatter, structure |
| 40 | brand-guidelines | 63/100 | ⚠️ Needs work | Missing frontmatter, structure |
| 41 | canvas-design | 63/100 | ⚠️ Needs work | Missing frontmatter, structure |
| 42 | content-research-writer | 51/100 | ⚠️ Needs work | Generic checklist, minimal content |

**Aggregate:** 0/7 AI-ready, 7/7 Need work (1 critical)

---

## Detailed Evaluations

### 36. hermes-skill-library-maintenance — 58/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 14 | Non-standard `status: active` instead of `version`; missing `license`; tags at root not metadata |
| Structure (20) | 12 | 4 phases with Safety Gates; no Skills Required table; has Pitfalls section; no verification checklist |
| Content (20) | 20 | Excellent: concrete Python/bash, error handling, platform detection, resumability, no placeholders |
| DRY (20) | 4 | 557 lines (>250 → capped at 4) |
| References (20) | 8 | No reference files mentioned |

**Priority Fixes (Critical):**
- **High**: Fix frontmatter; add Skills Required table, verification checklist; **split to <250 lines** (move pitfalls/code to refs)
- **Medium**: Create reference files for pitfalls, audit scripts
- **Low**: -

---

### 37. template-skill — 55/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license; tags in metadata, related_skills |
| Structure (20) | 12 | 4 phases, related skills, verification checklist; no Skills Required table, no pitfalls section |
| Content (20) | 12 | Minimal; no concrete examples, no error handling, no platform detection, no resumability |
| DRY (20) | 20 | 94 lines (<250), clean |
| References (20) | 1 | No reference files mentioned |

**Priority Fixes:**
- **High**: Add Skills Required table, pitfalls section
- **Medium**: Add concrete examples/templates, error handling
- **Low**: Add reference files

---

### 38. using-superpowers — 61/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `title` instead) |
| Structure (20) | 16 | 4 phases, related skills, library hygiene, session-derived updates; no Skills Required, no pitfalls, no verification checklist |
| Content (20) | 16 | Good session-derived updates; missing error handling, platform detection; duplicate "Best Practices" header |
| DRY (20) | 18 | 103 lines (<250), clean; minor duplicate header |
| References (20) | -1 | Cites 2 reference files but no reference dir |

**Priority Fixes:**
- **High**: Fix frontmatter; add Skills Required table, pitfalls, verification checklist; remove duplicate "Best Practices" header
- **Medium**: Add error handling details; create reference files
- **Low**: -

---

### 39. algorithmic-art — 63/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `title` instead) |
| Structure (20) | 16 | 4 phases, related skills, best practices; no Skills Required table, no pitfalls, no verification checklist |
| Content (20) | 16 | Good examples referenced; missing error handling, platform detection, resumability |
| DRY (20) | 20 | 82 lines (<250), clean |
| References (20) | -1 | No reference files mentioned |

**Priority Fixes:**
- **High**: Fix frontmatter; add Skills Required table, pitfalls, verification checklist
- **Medium**: Add reference files, error handling
- **Low**: -

---

### 40. brand-guidelines — 63/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `title` instead) |
| Structure (20) | 20 | 4 phases, related skills, tools/references, best practices; no Skills Required table, no pitfalls, no verification checklist |
| Content (20) | 16 | Good best practices; missing error handling, platform detection, resumability |
| DRY (20) | 20 | 85 lines (<250), clean |
| References (20) | -1 | No reference files mentioned |

**Priority Fixes:**
- **High**: Fix frontmatter; add Skills Required table, pitfalls, verification checklist
- **Medium**: Add reference files
- **Low**: -

---

### 41. canvas-design — 63/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `title` instead) |
| Structure (20) | 20 | 4 phases, related skills, tools/references, design principles, best practices; no Skills Required table, no pitfalls, no verification checklist |
| Content (20) | 16 | Good best practices; missing error handling, platform detection, resumability |
| DRY (20) | 20 | 87 lines (<250), clean |
| References (20) | -1 | No reference files mentioned |

**Priority Fixes:**
- **High**: Fix frontmatter; add Skills Required table, pitfalls, verification checklist
- **Medium**: Add reference files
- **Low**: -

---

### 42. content-research-writer — 51/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `title` instead) |
| Structure (20) | 12 | 4 phases, related skills, verification checklist; generic boilerplate checklist; no Skills Required table, no pitfalls |
| Content (20) | 8 | Generic workflow; no concrete examples, no error handling, no platform detection, no resumability |
| DRY (20) | 20 | 76 lines (<250), clean |
| References (20) | -1 | No reference files mentioned |

**Priority Fixes:**
- **High**: Fix frontmatter; add Skills Required table, pitfalls, non-generic verification checklist
- **Medium**: Add concrete examples, error handling, platform detection
- **Low**: Add reference files

---

## Cross-Batch Patterns (All 42 Skills)

| Issue | Frequency (of 42) |
|-------|-------------------|
| No Skills Required table | 42/42 (100%) |
| No verification checklist | 39/42 (93%) |
| Missing `version` in frontmatter | 18/42 (43%) |
| Missing `license` in frontmatter | 18/42 (43%) |
| Missing `tags` in frontmatter | 20/42 (48%) |
| Missing `author` in frontmatter | 17/42 (40%) |
| No phased workflow | 13/42 (31%) |
| No pitfalls section | 18/42 (43%) |
| SKILL.md >250 lines | 10/42 (24%) |
| Orphaned/unverified reference files | 19/42 (45%) |

---

## Remediation Priority (All 42 Skills)

| Priority | Skill | Score | Critical Issues |
|----------|-------|-------|-----------------|
| 1 | **template** | 35 | Placeholder text, no structure, must be exemplary |
| 2 | **folder-structure-blueprint-generator** | 41 | Template-in-skill-body, no structure |
| 3 | **architecture-blueprint-generator** | 42 | Template-in-skill-body, no structure |
| 4 | **technology-stack-blueprint-generator** | 44 | Template-in-skill-body, no structure |
| 5 | **validate-memories** | 45 | No structure, no refs |
| 6 | **make-repo-contribution** | 51 | Frontmatter + structure broken |
| 7 | **content-research-writer** | 51 | Generic checklist, minimal content |
| 8 | **customize-opencode** | 53 | Broken frontmatter, minimal content |
| 9 | **skill-creator** | 49 | Frontmatter malformed, orphaned refs |
| 10 | **stable-diffusion-image-generation** | 56 | 523 lines, no structure |
| 11 | **lambda-labs-gpu-cloud** | 58 | 549 lines, no structure |
| 12 | **hermes-skill-library-maintenance** | 58 | 557 lines, no structure |
| 13 | **qdrant-vector-search** | 59 | 497 lines, no structure |
| 14 | **simpo-training** | 60 | Orphaned refs, no structure |
| 15 | **peft-fine-tuning** | 62 | 435 lines, no structure |
| 16 | **agent-browser** | 61 | Missing frontmatter, structure |
| 17 | **qwen-code** | 65 | Duplicate section, orphaned refs |
| 18 | **writing-skills** | 68 | 350 lines, missing refs |
| 19 | **modal-serverless-gpu** | 68 | 345 lines, borderline |
| 20 | **agent-governance** | 66 | 572 lines, no refs |
| 21 | **huggingface-accelerate** | 55 | 336 lines, no structure/checklist |
| 22 | **inference-sh-cli** | 74 | Missing title, refs |
| 23 | **ideation** | 72 | Missing checklist, ref file |
| 24 | **agentic-eval** | 69 | Missing frontmatter fields |
| 25 | **algorithmic-art** | 63 | Missing frontmatter, structure |
| 26 | **brand-guidelines** | 63 | Missing frontmatter, structure |
| 27 | **canvas-design** | 63 | Missing frontmatter, structure |
| 28 | **using-superpowers** | 61 | Missing frontmatter fields |
| 29 | **template-skill** | 55 | Missing Skills Required, pitfalls |
| 30 | **profile-maintenance** | 78 | Missing version/license/tags |
| 31 | **hermes-system-maintenance** | 80 | Missing version |
| 32 | **skill-judge** | 78 | Missing checklist, Skills Required |
| 33 | **using-git-worktrees** | 79 | Missing frontmatter fields |
| 34 | **coding-agents** | 71 | Missing pitfalls/checklist |
| 35 | **enhance-markdown** | 81 | Verify reference files |
| 36 | **qwen-code** | 65 | Duplicate section, orphaned refs |

---

## Next Steps

1. **Batch 7** = excalidraw-diagram-generator, frontend-design, image-manipulation-image-magick, legacy-circuit-mockups, marp-slide, mermaid-diagrams, nano-banana-pro-openrouter

Continue through Batch 28, then apply all patches in priority order.
