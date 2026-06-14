# sample-prompt — Dependency Context Catalog

**Generated:** 2026-06-14
**Source File:** `./sample.prompt.md`
**Purpose:** sample-prompt

---

## Forward Dependencies (Extracted from Source)

### Markdown Links
| Link Text | Target | Status |
|-----------|--------|--------|
| (none found) | — | — |

### @mentions
| Mention | Context |
|---------|---------|
| (none found) | — |

### /commands Referenced
| Command | Location | Context |
|---------|----------|---------|
| `/plan` | Phase 1, Step 1; Core Workflow Step 1 | Update existing plan |
| `/skills browse` | Phase 1, Step 2 | List available skills |
| `/skills search` | Phase 1, Step 4 | Find skills by keyword |
| `/skills audit` | Phase 1, Step 6 | Run skills audit |
| `/systematic-debugging` | Phase 1, Step 7 | Debug and fix issues |

### Plan Namespaces Referenced
| Namespace | Location |
|-----------|----------|
| (none explicit) | — |

### Skills Referenced (Frontmatter + Body)
| Skill | Location |
|-------|----------|
| `skill-creator` | Skills Required table |
| `writing-skills` | Skills Required table |
| `plans-and-specs` | Skills Required table |

### Template Variables
| Variable | Value |
|----------|-------|
| `{{workspace_root}}` | `C:\Users\Alexa\Desktop\SandBox` |
| `{{docs_root}}` | `docs/` |
| `{{agent_name}}` | `Codex` \| `Copilot` \| `Hermes` |
| `{{native_plan}}` | Active agent's planning command |
| `{{native_search}}` | Active agent's search command |
| `{{native_extract}}` | Active agent's extraction command |
| `{{native_files}}` | Active agent's file read/write command |

---

## Reverse Dependencies (Files Referencing This File)

| Referencing File | Reference Type | Context |
|------------------|----------------|---------|
| `docs/sample-prompt-execution-index.md` | Markdown link | Maps `sample.prompt.txt` targets to docs |
| `docs/sample-prompt-execution-summary.md` | Text reference | Execution summary for all 6 phases |
| `docs/multi-agent-research-template-context.md` | Text reference | Phase 3 targets, Phase 2 inputs, Phase 1 audit log |
| `docs/multi-agent-research-template-verify-context.md` | Source file reference | Verification context |
| `docs/multi-agent-research-template-issues-context.md` | Source file reference | Issues context |
| `docs/phase3-hermes-docs-extraction-log.md` | Text reference | Verified target URL list from Phase 3 |
| `docs/phase2-mcp-research-log.md` | Text reference | Phase 2 start, inputs from Phase 2 target list |
| `docs/phase1-skills-audit.md` | Text reference | Skills selected mapping to Phase 2/3 needs |
| `docs/phase1-skills-audit-log.md` | Text reference | Execution began against this file |
| `docs/phase4-profiles-log.md` | Text reference | Verified profile list and target names |
| `docs/hermes/index.md` | Markdown link | Phase 3 targets source |
| `thoughts/plans/multi-agent-research-template-debug.md` | Target file reference | Fix plan target file |

---

## Related Artifacts (Existing)

| Artifact | Type | Description |
|----------|------|-------------|
| `docs/sample-prompt-execution-index.md` | Execution index | Maps prompt targets to workspace docs |
| `docs/sample-prompt-execution-summary.md` | Execution summary | All 6 phases complete with verification |
| `docs/phase1-skills-audit.md` | Phase 1 output | Skills audit results |
| `docs/phase1-skills-audit-log.md` | Phase 1 log | Audit execution log |
| `docs/phase2-mcp-research-log.md` | Phase 2 log | MCP research execution log |
| `docs/phase3-hermes-docs-extraction-log.md` | Phase 3 log | Hermes docs extraction log |
| `docs/phase4-profiles-log.md` | Phase 4 log | Profile creation log |
| `docs/phase5-docs-inventory-log.md` | Phase 5 log | Docs inventory log |
| `docs/phase6-config-hierarchy-audit.md` | Phase 6 log | Config hierarchy audit |
| `docs/hermes/index.md` | Index | Hermes docs catalog with 12 extracted pages |

---

## Notes

- This file (`sample.prompt.md`) is a **template** for creating new `.prompt.md` files
- The reverse dependencies show it was **executed as a prompt** (not audited) — the 6-phase workflow was run against it
- No prior enhance-markdown audit artifacts exist for purpose `sample-prompt`
- The file has valid YAML frontmatter with all required fields (name, title, description, trigger, tags)
- Skills Required table present and populated
- 4 phases with numbered steps + verification checklist
- No placeholder text detected