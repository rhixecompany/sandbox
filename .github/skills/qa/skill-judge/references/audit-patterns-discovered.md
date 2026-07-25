# Audit Patterns Discovered (2026-06-14)

Systemic patterns found during the complete skills audit pipeline (191 skills, 28 batches) using skill-judge v1.1.0.

---

## Universal Missing Elements (All 191 Skills)

| Element | Missing Count | Percentage |
|---------|---------------|------------|
| Skills Required table | 191/191 | 100% |
| Verification checklist | 174/191 | 91% |

**Remediation:** These are the highest-impact fixes. Every skill needs a Skills Required table and a concrete verification checklist.

---

## Frontmatter Field Deficits

| Field | Missing | Percentage |
|-------|---------|------------|
| `tags` | 107/191 | 56% |
| `version` | 103/191 | 54% |
| `license` | 104/191 | 54% |
| `author` | 102/191 | 53% |
| `title` | ~30/191 | 16% |

**Pattern:** Skills created from the `template` skill often copy its incomplete frontmatter.

---

## Structural Gaps

| Gap | Count | Percentage |
|-----|-------|------------|
| No phased workflow | 56/191 | 29% |
| No pitfalls section | 80/191 | 42% |
| SKILL.md >250 lines | 34/191 | 18% |
| Orphaned/unverified references | 88/191 | 46% |

---

## Template-in-Skill-Body Anti-Pattern

**Skills affected (3):**
- `architecture-blueprint-generator` (42/100)
- `folder-structure-blueprint-generator` (41/100)
- `technology-stack-blueprint-generator` (44/100)

**Issue:** Massive parameterized templates embedded directly in SKILL.md body instead of `references/` or `templates/`.

**Fix:** Move template to `templates/blueprint.md`; keep SKILL.md <250 lines.

---

## Generic Boilerplate Verification Checklists

**Skills affected (15+):** create-readme, frontend-design, marp-slide, mermaid-diagrams, theme-factory, web-artifacts-builder, writing-clearly-and-concisely, content-research-writer, ai-prompt-engineering-safety-review, context-map, convert-plaintext-to-md, create-web-form, copilot-usage-metrics, validate-memories, copilot-cli-quickstart, and others.

**Pattern:** Identical 5-item checklist copied verbatim. Verifies nothing skill-specific.

**Fix:** Replace with skill-specific verification gates.

---

## Pure Placeholder Skills (Rewrite Required)

| Skill | Score | Issue |
|-------|-------|-------|
| `template` | 35 | Must be exemplary; has placeholder text |
| `ai-prompt-engineering-safety-review` | 22 | "This skill is a placeholder" |
| `context-map` | 21 | "This skill is a placeholder" |
| `convert-plaintext-to-md` | 21 | "This skill is a placeholder" |
| `skills` | 21 | "This skill is a placeholder" |
| `rbac-audit-logging` | 18 | "This skill is a placeholder" |

**Root cause:** The `template` skill itself is broken, propagating placeholder content.

---

## Long Skills Needing Split (>250 lines, 34 skills)

**Critical (>500 lines):** copilot-cli-quickstart (769), refactor (645), excalidraw-diagram-generator (660), agent-governance (572), lambda-labs-gpu-cloud (549), hermes-skill-library-maintenance (557), stable-diffusion-image-generation (523), qdrant-vector-search (497)

**High (400-500 lines):** godmode (408), quasi-coder (389), bun-shell (393), systematic-debugging (392), test-driven-development (537), subagent-driven-development (460), django-celery (457), 3-statement-model (433)

**Medium (300-400 lines):** writing-plans (357), executing-plans (316), script-orchestration (323), bun-nextjs (322), web-design-reviewer (370), mindstudio-wrapper (264), web-research-pipeline (268), fluentui-blazor (235)

**Split strategy:** Move detailed examples, code blocks, and reference tables to `references/`. Keep SKILL.md at workflow + pointers.

---

## Scoring Calibration (from 191-skill audit)

**Dimension 1 (Frontmatter):** Strict — missing `version` = -3, missing `tags` = -2.

**Dimension 2 (Structure):** Skills Required table is 0/191. Most skills have phased workflow but not explicitly labeled.

**Dimension 3 (Content):** Placeholder text = auto-cap at 40. No verification checklist = cap at 70.

**Dimension 4 (DRY):** Hard cap at 10/20 for >250 lines. 34/191 skills exceeded this.

**Dimension 5 (References):** 46% cite refs that don't exist. Must verify with read_file().

---

## Remediation Priority Algorithm

1. **Fix `template` skill first** (score 35) — source of placeholder propagation
2. **Rewrite 5 pure placeholders** (18-22) — ai-prompt-engineering-safety-review, context-map, convert-plaintext-to-md, skills, rbac-audit-logging
3. **Split 8 critical long skills** (>500 lines) — start with copilot-cli-quickstart
4. **Extract 3 blueprint templates** to `templates/` directory
5. **Replace generic checklists** on 15+ skills with specific verification gates
6. **Add Skills Required tables** to all 191 skills
7. **Add verification checklists** to 174 skills
8. **Fix frontmatter fields** on 100+ skills
9. **Create/verify reference files** for 88 skills

---

## Audit Methodology Notes

1. **Batch size of 7** worked well — kept context manageable
2. **Sequential execution** (Batch 1→28) revealed cross-batch patterns
3. **skill-judge criteria** are appropriate but need:
   - Skills Required table should be mandatory (not 4 pts)
   - Verification checklist should be mandatory (not 4 pts)
   - Placeholder text should cap score at 40 (not 60)
4. **Ambiguous skill names** require read_file() fallback
5. **Reference file verification** needs automation — currently manual
6. **Criterion drift** is real — calibrate on Batch 1 and lock thresholds
7. **Profile visibility** — default profile may not see all category subdirectories

---

## Cross-Reference

- Related skill: `hermes-skill-library-maintenance` (bulk patching)
- Related skill: `writing-skills` (TDD for skill creation)
- Related skill: `enhance-markdown` (markdown audit pipeline)
- Full data: `references/batch-audit-findings.md`
