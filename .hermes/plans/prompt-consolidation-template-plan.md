# Prompt Consolidation & Template Generation Plan

> **Goal:** Consolidate/trim all 215 prompts in `.github/prompts/`, create DRY template folders per prompt, update prompts to reference templates, validate all.

**Architecture:** Each prompt gets a dedicated template folder at `.github/prompts/templates/<prompt-name>/` containing reusable snippets (frontmatter, sections, examples, references). Prompts are trimmed to remove duplicated content — instead, they reference templates via include directives or clear cross-references. Templates follow DRY across prompts: common patterns (YAML frontmatter, skill refs, tool refs, verification checklists) live in shared templates under `templates/_shared/`.

**Phases:**

### Phase 1: Setup Template Infrastructure
- Create `.github/prompts/templates/` directory structure
- Create `_shared/` with reusable common templates:
  - `frontmatter.yaml` — standard YAML frontmatter fields
  - `skill-refs.md` — common skill reference patterns
  - `verification-checklist.md` — standard verification checklist
  - `best-practices.md` — cross-cutting best practices
- Create `templates/_index.md` — template directory index

### Phase 2: Process Prompts (in batches of 10)
For each prompt:
1. Read full prompt content
2. Identify sections suitable for templating (frontmatter, goal, context, rules, phases, verification)
3. Create `templates/<prompt-name>/` folder with template snippets
4. Trim prompt: replace duplicated/boilerplate content with references to templates
5. Ensure trigger, dependencies, skills fields are accurate

### Phase 3: Validate
- Verify all template references resolve
- Verify YAML frontmatter parses correctly
- Verify all prompts still have working triggers

**Total prompts to process:** 215
**Batch size:** 10 prompts per batch
**Batches:** 22 (last batch = 5)
