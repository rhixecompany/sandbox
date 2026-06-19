# PROMPTS-AUDIT Context Catalog

**Purpose**: `prompts-audit` — Two-way dependency catalog for all prompt files in `Prompts/` and `.github/prompts/`

**Generated**: 2026-06-17 | Files scanned: 219 | Audit tool: `scripts/audit_prompts.py`

---

## Directory Inventory

### `Prompts/` (8 files, `.prompts.md` extension)

| File | Lines | Size | Trigger / Title | Frontmatter Valid |
|------|-------|------|-----------------|-------------------|
| `agents-fix.prompts.md` | 131 | 4,948 | `/agents-fix` | ❌ Unclosed fence |
| `bash-scripts-fix.prompts.md` | 185 | 8,040 | `/bash-scripts-fix` | ❌ Unclosed fence |
| `dev-init.prompts.md` | 499 | 17,652 | `/dev-init` | ❌ Unclosed fence |
| `general.prompts.md` | 142 | 5,562 | `/general` | ❌ Unclosed fence |
| `prompts-fix.prompts.md` | 135 | 5,140 | `/prompts-fix` | ❌ Unclosed fence |
| `repo-management.prompts.md` | 392 | 14,601 | `/repo-management` | ❌ Parse error |
| `repo.prompts.md` | 472 | 18,581 | `/repo` | ❌ Unclosed fence |
| `skills-fix.prompts.md` | 248 | 11,429 | `/skills-fix` | ❌ Unclosed fence |
| `workspace-consolidate.prompts.md` | 501 | 23,368 | `/workspace-consolidate` | ❌ Unclosed fence |

### `.github/prompts/` (211 files, `.prompt.md` extension)

| File | Lines | Size | Valid FM | Issues (H/M/L) |
|------|-------|------|----------|----------------|
| `add-educational-comments.prompt.md` | 174 | 7,790 | ✅ | 0/0/0 |
| `agents-generator.prompt.md` | 31 | 2,348 | ✅ | 0/0/0 |
| `ai-prompt-engineering-safety-review.prompt.md` | 140 | 5,456 | ✅ | 0/6/0 |
| `apple-appstore-reviewer.prompt.md` | 317 | 9,574 | ✅ | 1/0/0 |
| `arch-linux-triage.prompt.md` | 33 | 1,008 | ✅ | 0/0/0 |
| `architecture-blueprint-generator.prompt.md` | 375 | 15,323 | ✅ | 0/0/0 |
| `aspnet-minimal-api-openapi.prompt.md` | 42 | 1,804 | ✅ | 0/0/0 |
| `az-cost-optimize.prompt.md` | 323 | 12,918 | ✅ | 0/0/0 |
| `azure-resource-health-diagnose.prompt.md` | 356 | 13,182 | ✅ | 0/0/1 |
| `bigquery-pipeline-audit.prompt.md` | 114 | 5,022 | ✅ | 1/0/0 |
| ... (201 more files in JSON) | | | | |

---

## Forward Dependency Graph (extracted from frontmatter)

### Prompts/ → .github/prompts/ references
| Source | Depends On |
|--------|------------|
| `agents-fix.prompts.md` | `context-map.prompt.md`, `update-implementation-plan.prompt.md` |
| `bash-scripts-fix.prompts.md` | `context-map.prompt.md`, `update-implementation-plan.prompt.md` |
| `dev-init.prompts.md` | `context-map.prompt.md`, `convert-plaintext-to-md.prompt.md`, `boost-prompt.prompt.md`, `ai-prompt-engineering-safety-review.prompt.md`, `update-implementation-plan.prompt.md`, `prompt-builder.prompt.md` |
| `general.prompts.md` | `context-map.prompt.md`, `update-implementation-plan.prompt.md` |
| `prompts-fix.prompts.md` | `context-map.prompt.md`, `update-implementation-plan.prompt.md` |
| `repo-management.prompts.md` | `context-map.prompt.md` |
| `repo.prompts.md` | `context-map.prompt.md`, `update-implementation-plan.prompt.md` |
| `skills-fix.prompts.md` | `context-map.prompt.md`, `update-implementation-plan.prompt.md`, `skills-debug-prompt.prompt.md` |
| `workspace-consolidate.prompts.md` | `context-map.prompt.md`, `update-implementation-plan.prompt.md` |

### Shared Skills References (Prompts/)
- `brainstorming`, `plans-and-specs`, `dispatching-parallel-agents`, `subagent-driven-development`, `systematic-debugging`, `simplify`, `acpx-executor`, `hermes-agent`, `copilot-cli`, `skill-judge`, `skill-creator`, `script-orchestration`, `git-patch-management`, `project-consolidation`, `context7`, `spike`, `writing-skills`, `content-research-writer`, `context-map`, `convert-plaintext-to-md`, `boost-prompt`, `ai-prompt-engineering-safety-review`, `executing-plans`, `using-superpowers`

### Shared Tools References (Prompts/)
- `terminal`, `search_files`, `web_search`, `web_extract`, `patch`, `write_file`, `execute_code`, `read_file`, `delegate_task`

### .github/prompts/ → Skills References
Common skills across many files: `codemap`, `enhance-markdown`, `context7`, plus agent-specific skills.

---

## Reverse Dependency Graph (who references these paths)

| Target File | Referenced By |
|-------------|---------------|
| `context-map.prompt.md` | 8 files in `Prompts/` + multiple in `.github/prompts/` |
| `update-implementation-plan.prompt.md` | 7 files in `Prompts/` |
| `convert-plaintext-to-md.prompt.md` | `dev-init.prompts.md` |
| `boost-prompt.prompt.md` | `dev-init.prompts.md` |
| `ai-prompt-engineering-safety-review.prompt.md` | `dev-init.prompts.md` |
| `prompt-builder.prompt.md` | `dev-init.prompts.md` |
| `skills-debug-prompt.prompt.md` | `skills-fix.prompts.md` |

---

## File Format Conventions by Directory

### `Prompts/` — `.prompts.md` format
- YAML frontmatter with `trigger`, `title`, `description`, `tags`, `dependencies`, `skills:` list
- Frontmatter often missing closing `---` fence (8/8 files)
- Some use `dependencies:` with prompt: and skill: prefixes
- Body contains phased implementation plans

### `.github/prompts/` — `.prompt.md` format  
- YAML frontmatter with `name`, `description`, `trigger`, `tags`, `dependencies`, `skills:` list
- Frontmatter issues: missing (17 files), unclosed fences (12), double fences (15)
- Some use `agent:` + `tools:` instead of skills (Copilot agent format)
- Simpler structure: goal, context, skills required

---

## Cross-Directory Relationships

| Relationship | Count |
|--------------|-------|
| Prompts/ → .github/prompts/ deps | 15 explicit references |
| Shared skill dependencies | 28 distinct skills |
| Shared tool dependencies | 8 tools |
| Common planning prompts | `context-map`, `update-implementation-plan` |

---

## Notes

- **Total referenced external files**: 15 unique `.github/prompts/` files from `Prompts/`
- **Orphan check**: No `.github/prompts/` files reference `Prompts/` files (unidirectional)
- **Zombie file**: `zod-schema-generation.prompt.md` is empty (0 bytes)
- **Name collision**: `Developement.prompt.md` (typo) vs standard naming
- **Two formats coexist**: Hermes-style (Prompts/) and Copilot-style (.github/prompts/)
