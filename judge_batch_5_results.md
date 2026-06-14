# Batch 5 Judge Results — Skills Audit Pipeline

**Date:** 2026-06-14
**Profile:** default
**Batch:** 5 (Skills 29-35)
**Judge Skill:** skill-judge v1.1.0

---

## Summary

| # | Skill | Score | Rating | Status |
|---|-------|-------|--------|--------|
| 29 | technology-stack-blueprint-generator | 44/100 | ⚠️ Needs work | Critical: template-in-skill, no structure |
| 30 | agent-browser | 61/100 | ⚠️ Needs work | Missing frontmatter, structure |
| 31 | agent-governance | 66/100 | ⚠️ Needs work | 572 lines, no refs |
| 32 | agentic-eval | 69/100 | ⚠️ Needs work | Borderline, missing frontmatter fields |
| 33 | coding-agents | 71/100 | ✅ AI-ready | Minor: no pitfalls/checklist |
| 34 | customize-opencode | 53/100 | ⚠️ Needs work | Broken frontmatter, minimal content |
| 35 | enhance-markdown | 81/100 | ✅ AI-ready | Minor: verify reference files |

**Aggregate:** 2/7 AI-ready, 5/7 Need work (2 critical)

---

## Detailed Evaluations

### 29. technology-stack-blueprint-generator — 44/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 14 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 4 | No Skills Required, no phased workflow (single massive template), no pitfalls, no verification checklist |
| Content (20) | 8 | Template variables, no concrete examples; missing error handling, platform detection |
| DRY (20) | 4 | 255 lines (>250 → capped) |
| References (20) | 14 | None mentioned |

**Priority Fixes (Critical):**
- **High**: Fix frontmatter; add phased workflow, Skills Required, verification checklist, pitfalls; **move template to references** (<250 lines)
- **Medium**: Add concrete examples, error handling
- **Low**: Add reference files

---

### 30. agent-browser — 61/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 14 | Missing `version`, `license`, `author`, `tags` (has `title` instead) |
| Structure (20) | 12 | Has phased workflow (4 phases), 3 related skills cited; no Skills Required table, no pitfalls, no verification checklist |
| Content (20) | 16 | Good best practices section; missing error handling details, resumability, platform detection |
| DRY (20) | 20 | 85 lines (<250), clean |
| References (20) | -1 | Cites related skills but no reference files |

**Priority Fixes:**
- **High**: Fix frontmatter; add Skills Required table, pitfalls, verification checklist
- **Medium**: Add error handling details, platform detection
- **Low**: Add reference files

---

### 31. agent-governance — 66/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 14 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 16 | 6 patterns as phases; no Skills Required table, no verification checklist, no explicit pitfalls section; no references |
| Content (20) | 20 | Excellent: concrete code, error handling, framework integrations (PydanticAI, CrewAI, OpenAI Agents), no placeholders |
| DRY (20) | 10 | 572 lines (>250 → capped at 10) |
| References (20) | 6 | No reference files mentioned |

**Priority Fixes:**
- **High**: Fix frontmatter; add Skills Required table, verification checklist, explicit pitfalls; **split to <250 lines** (move patterns to references)
- **Medium**: Create reference files for code patterns
- **Low**: -

---

### 32. agentic-eval — 69/100 ⚠️ (Borderline)

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 14 | Missing `version`, `license`, `author`, `tags` |
| Structure (20) | 16 | 3 patterns as phases, best practices table, checklist; no Skills Required, no verification checklist, no pitfalls, no references |
| Content (20) | 20 | Excellent: concrete code, evaluation strategies, best practices |
| DRY (20) | 19 | 195 lines (<250), clean |
| References (20) | -1 | No reference files mentioned |

**Priority Fixes:**
- **High**: Fix frontmatter; add Skills Required table, verification checklist, pitfalls section
- **Medium**: Add reference files
- **Low**: -

---

### 33. coding-agents — 71/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description ("Use when..."), version, author, tags |
| Structure (20) | 20 | Skills Required (implicit via provider table), routing guide as workflow, verification section; no explicit pitfalls but routing covers it |
| Content (20) | 20 | Excellent: provider table, routing guide, YAML config, verification commands |
| DRY (20) | 20 | 76 lines (<250), clean |
| References (20) | -9 | No reference files mentioned; **penalty for missing reference types** |

**Priority Fixes:**
- **High**: Add explicit pitfalls section, verification checklist
- **Medium**: Add reference files for provider configs
- **Low**: -

---

### 34. customize-opencode — 53/100 ⚠️

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 11 | Missing `version`, `license`, `author`, `tags` (has `title` instead); description not standard |
| Structure (20) | 16 | Has phased workflow (4 phases), 2 related skills; no Skills Required table, no pitfalls, no verification checklist |
| Content (20) | 12 | Minimal; no concrete examples, no error handling, no platform detection |
| DRY (20) | 20 | 70 lines (<250), clean |
| References (20) | 4 | Cites 2 related skills + config files but no reference files |

**Priority Fixes:**
- **High**: Fix frontmatter; add Skills Required table, pitfalls, verification checklist
- **Medium**: Add concrete examples, error handling
- **Low**: Add reference files

---

### 35. enhance-markdown — 81/100 ✅

| Dimension | Score | Findings |
|-----------|-------|----------|
| Frontmatter (20) | 20 | All fields: name, title, description, version, author, license, tags, metadata.related_skills |
| Structure (20) | 20 | Skills Required table, 4 phases with entry checks, explicit pitfalls, verification checklist with gates, 9 refs cited |
| Content (20) | 20 | Excellent: resumability, error handling, concrete bash examples, no placeholders |
| DRY (20) | 19 | 171 lines (<250), clean |
| References (20) | 2 | 9 refs cited but reference dir existence not verified; **penalty for unverified refs** |

**Priority Fixes:**
- **High**: Verify/create 9 reference files
- **Medium**: Add explicit pitfalls section (some in Phase 1/2 notes)
- **Low**: -

---

## Cross-Batch Patterns (All 35 Skills)

| Issue | Frequency (of 35) |
|-------|-------------------|
| No Skills Required table | 35/35 (100%) |
| No verification checklist | 32/35 (91%) |
| Missing `version` in frontmatter | 14/35 (40%) |
| Missing `license` in frontmatter | 14/35 (40%) |
| Missing `tags` in frontmatter | 16/35 (46%) |
| Missing `author` in frontmatter | 13/35 (37%) |
| No phased workflow | 13/35 (37%) |
| No pitfalls section | 14/35 (40%) |
| SKILL.md >250 lines | 9/35 (26%) |
| Orphaned/unverified reference files | 16/35 (46%) |

---

## Remediation Priority (All 35 Skills)

| Priority | Skill | Score | Critical Issues |
|----------|-------|-------|-----------------|
| 1 | **template** | 35 | Placeholder text, no structure, must be exemplary |
| 2 | **folder-structure-blueprint-generator** | 41 | Template-in-skill-body, no structure |
| 3 | **architecture-blueprint-generator** | 42 | Template-in-skill-body, no structure |
| 4 | **technology-stack-blueprint-generator** | 44 | Template-in-skill-body, no structure |
| 5 | **validate-memories** | 45 | No structure, no refs |
| 6 | **make-repo-contribution** | 51 | Frontmatter + structure broken |
| 7 | **stable-diffusion-image-generation** | 56 | 523 lines, no structure |
| 8 | **lambda-labs-gpu-cloud** | 58 | 549 lines, no structure |
| 9 | **qdrant-vector-search** | 59 | 497 lines, no structure |
| 10 | **simpo-training** | 60 | Orphaned refs, no structure |
| 11 | **peft-fine-tuning** | 62 | 435 lines, no structure |
| 12 | **agent-browser** | 61 | Missing frontmatter, structure |
| 13 | **customize-opencode** | 53 | Broken frontmatter, minimal content |
| 14 | **agent-governance** | 66 | 572 lines, no refs |
| 15 | **qwen-code** | 65 | Duplicate section, orphaned refs |
| 16 | **writing-skills** | 68 | 350 lines, missing refs |
| 17 | **modal-serverless-gpu** | 68 | 345 lines, borderline |
| 18 | **skill-creator** | 49 | Frontmatter malformed, orphaned refs |
| 19 | **huggingface-accelerate** | 55 | 336 lines, no structure/checklist |
| 20 | **inference-sh-cli** | 74 | Missing title, refs |
| 21 | **ideation** | 72 | Missing checklist, ref file |
| 22 | **agentic-eval** | 69 | Missing frontmatter fields |
| 23 | **profile-maintenance** | 78 | Missing version/license/tags |
| 24 | **hermes-system-maintenance** | 80 | Missing version |
| 25 | **skill-judge** | 78 | Missing checklist, Skills Required |
| 26 | **using-git-worktrees** | 79 | Missing frontmatter fields |
| 27 | **coding-agents** | 71 | Missing pitfalls/checklist |
| 28 | **enhance-markdown** | 81 | Verify reference files |

---

## Next Steps

1. **Batch 6** = hermes-skill-library-maintenance, template-skill, using-superpowers, algorithmic-art, brand-guidelines, canvas-design, content-research-writer
2. **Batch 7** = excalidraw-diagram-generator, frontend-design, image-manipulation-image-magick, legacy-circuit-mockups, marp-slide, mermaid-diagrams, nano-banana-pro-openrouter
3. ... continue through Batch 28, then apply all patches in priority order.
