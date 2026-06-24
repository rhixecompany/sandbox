# Prompt Migration Issues Context

Generated: 2026-06-24
Total files scanned: 224

## Issue Summary

| Severity | Category | Count |
|----------|----------|-------|
| **HIGH** | YAML parse errors (frontmatter unreadable) | 21 |
| **HIGH** | Body fence bleed (3+ `---` lines in file) | 35 |
| **HIGH** | Files with no frontmatter fences (0 fences) | 8 |
| **MEDIUM** | Missing `dependencies:` field | 187 |
| **MEDIUM** | Missing `skills:` field | 187 |
| **MEDIUM** | Missing `tags:` field | 178 |
| **MEDIUM** | Missing `trigger:` or `name:` field | 154 |
| **MEDIUM** | Broken dependency paths (wrong relative root) | 8 |
| **MEDIUM** | Missing `description:` field | 1 |
| **LOW** | Files >15KB (write-timeout risk) | 4 |

---

## HIGH: YAML Parse Errors (21 files)

These files have frontmatter that cannot be parsed by `yaml.safe_load`. Common causes: inline descriptions in `skills:` that break YAML, multiline strings without proper quoting, `---` bleeding into content text, or completely missing frontmatter.

| # | File | Error |
|---|------|-------|
| 1 | `prompts/workspace-consolidate.prompt.md` | while scanning a simple key |
| 2 | `prompts/run.prompt.md` | while scanning a block scalar |
| 3 | `prompts/plan-updateAiAgentSetupPrompt2.prompt.md` | while scanning a block scalar |
| 4 | `prompts/plan-setup.prompt.md` | No usable YAML doc: empty |
| 5 | `prompts/plan-phase1ComprehensiveValidation.prompt.md` | while scanning a block scalar |
| 6 | `prompts/plan-optimize.prompt.md` | No usable YAML doc: empty |
| 7 | `prompts/plan-fullEslintVscodeAuthModernization.prompt.md` | No usable YAML doc: empty |
| 8 | `prompts/plan-comicWiseImplementation.prompt.md` | while scanning an alias |
| 9 | `prompts/plan-acpx-agent-stack-audit-shared.prompt.md` | No usable YAML doc: empty |
| 10 | `prompts/plan-acpx-agent-stack-audit-hermes.prompt.md` | No usable YAML doc: empty |
| 11 | `prompts/plan-acpx-agent-stack-audit-copilot.prompt.md` | No usable YAML doc: empty |
| 12 | `prompts/optimization.prompt.md` | No usable YAML doc: empty |
| 13 | `prompts/debugger.prompt.md` | No usable YAML doc: empty |
| 14 | `prompts/comicwise-session.prompt.md` | No usable YAML doc: empty |
| 15 | `prompts/dev-init.prompt.md` | while scanning a simple key |
| 16 | `prompts/bash-scripts-fix.prompt.md` | while scanning a block scalar |
| 17 | `prompts/prompts-fix.prompt.md` | No usable YAML doc: empty |
| 18 | `prompts/general.prompt.md` | No usable YAML doc: empty |
| 19 | `prompts/zod-schema-generation.prompt.md` | No usable YAML doc: empty |
| 20 | `prompts/plan-eslintPluginAuditAndUpdate.prompt.md` | mapping values are not allowed |
| 21 | `prompts/java-docs.prompt.md` | No usable YAML doc: empty |

---

## HIGH: Body Fence Bleed (35 files with 3+ `---` fences)

Files that have `---` lines in the markdown body that create false frontmatter boundaries. This confuses YAML parsers and prompt loaders.

| Fences count | Files affected |
|-------------|---------------|
| 3 | 6 files |
| 4 | 10 files |
| 5 | 6 files |
| 6 | 3 files |
| 7 | 1 file |
| 8 | 2 files |
| 9 | 1 file |
| 10 | 2 files |
| 11 | 1 file |
| 12 | 1 file |
| 15 | 1 file (`repo-management.prompt.md`) |
| 17 | 1 file (`debugger.prompt.md`) |

---

## HIGH: No Frontmatter Fences (8 files)

These files have 0 `---` fences, meaning they lack any YAML frontmatter section entirely.

Files identified as having 0 or 1 fence (likely corrupt frontmatter):
- Already captured in YAML errors list above (all "No usable YAML doc: empty" cases)

---

## MEDIUM: Missing Fields Summary

| Field | Missing count | % of total |
|-------|--------------|-----------|
| `dependencies:` | 187 | 83.5% |
| `skills:` | 187 | 83.5% |
| `tags:` | 178 | 79.5% |
| `trigger:` or `name:` | 154 | 68.8% |
| `description:` | 1 | 0.4% |

---

## MEDIUM: Broken Dependency Paths (8 issues)

Source paths prefixed with `.github/prompts/` break when resolved from the `./prompts/` destination (they resolve to `./prompts/.github/prompts/...` which doesn't exist). Affected files:

| File | Broken Dep |
|------|-----------|
| `prompts/repo-management.prompt.md` | `prompt:.github/prompts/context-map.prompt.md` |
| `prompts/repo.prompt.md` | `prompt:.github/prompts/context-map.prompt.md` |
| `prompts/repo.prompt.md` | `prompt:.github/prompts/update-implementation-plan.prompt.md` |
| `prompts/skills-fix.prompt.md` | `prompt:.github/prompts/context-map.prompt.md` |
| `prompts/skills-fix.prompt.md` | `prompt:.github/prompts/update-implementation-plan.prompt.md` |
| `prompts/skills-fix.prompt.md` | `prompt:.github/prompts/skills-debug-prompt.prompt.md` |
| `prompts/agents-fix.prompt.md` | `prompt:.github/prompts/context-map.prompt.md` |
| `prompts/agents-fix.prompt.md` | `prompt:.github/prompts/update-implementation-plan.prompt.md` |

---

## LOW: Large Files (>15KB, write-timeout risk)

| File | Size | Lines |
|------|------|-------|
| `prompts/debugger.prompt.md` | 30,007 bytes | 558 |
| `prompts/workspace-consolidate.prompt.md` | 22,297 bytes | 501 |
| `prompts/repo.prompt.md` | 16,937 bytes | 452 |
| `prompts/dev-init.prompt.md` | 16,427 bytes | 473 |

---

## Fix Priority Order

1. **HIGH: YAML parse errors** — Fix first; unparseable files can't be used at all
2. **HIGH: Body fence bleed** — Remove/quote `---` lines in body that break parsing
3. **HIGH: No frontmatter** — Add minimal valid frontmatter to fence-less files
4. **MEDIUM: Dependency paths** — Fix `.github/prompts/` prefix to `../.github/prompts/` or remove prefix
5. **MEDIUM: Missing fields** — Add `dependencies:`, `skills:`, `tags:`, `trigger:` where practical
6. **LOW: Large files** — Monitor for write timeouts; split if needed
