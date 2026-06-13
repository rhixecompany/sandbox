# multi-agent-research-template — Issues Context

Generated: 2026-06-13  
Source: C:\Users\Alexa\Desktop\SandBox\sample.prompt.md  
Audit Mode: enhance-markdown Phase 1

---

## Frontmatter Validation

| Check | Status | Details |
|-------|--------|---------|
| Single `---` pair | ✅ PASS | Exactly one frontmatter block (lines 1-6) |
| YAML parses cleanly | ✅ PASS | Valid YAML with title, description, tags, agent |
| No `skills:` malformed entries | ✅ PASS | No `skills:` key in frontmatter |
| No dependency-style prose in lists | ✅ PASS | Tags are plain identifiers |

---

## Structure & Formatting Audit

| Check | Status | Details |
|-------|--------|---------|
| Heading hierarchy | ⚠️ MINOR | Uses `# Purpose`, `## Template Variables`, `## Agent Mapping`, `## Shared Rules`, `## Core Workflow`, `### Phase 1-6` — consistent but deep nesting (3+ levels in Phase 2-6) |
| Table pipe balance | ✅ PASS | Template Variables table (lines 17-25) has balanced pipes |
| Code block language tags | ❌ MISSING | No fenced code blocks with language tags (e.g., ```bash) — raw commands in prose |
| Cross-references resolved | ⚠️ PARTIAL | References to `docs/` directory but no specific file links; Hermes URLs are absolute |
| Duplicate frontmatter fences | ✅ PASS | Only one `---` pair |

---

## Content Quality Issues

| Issue ID | Severity | Location | Description | Suggested Fix |
|----------|----------|----------|-------------|---------------|
| ISSUE-001 | Medium | Lines 17-25 | Template Variables table uses `||` separators but values contain backslashes that may need escaping in markdown | Use code fences for paths with backslashes or escape them |
| ISSUE-002 | Medium | Lines 59-65, 69-112, 128-141, 155-160, 164-168, 172-178 | Phase task lists are plain bullet points without checkboxes or clear actionable Task format | Convert to structured Tasks with checkboxes per enhance-markdown template |
| ISSUE-003 | Low | Lines 130-141 | Phase 3 URLs listed as raw URLs — should be markdown links with descriptive text | Convert to `[Title](URL)` format |
| ISSUE-004 | Medium | Lines 113-124 | Phase 2 "After research" steps are procedural but not structured as Tasks/Actions | Apply Steps/Tasks/Actions structure |
| ISSUE-005 | Low | Lines 180-186 | Output Requirements and Verification Gates are prose lists — could be structured tables | Convert to tables for scannability |
| ISSUE-006 | Medium | Lines 29-32 | Agent Mapping uses dash lists — could be a table for consistency | Convert to markdown table |
| ISSUE-007 | Low | Line 5 | `agent: agent` in frontmatter — unclear purpose, possibly redundant | Remove or clarify in description |
| ISSUE-008 | Medium | Lines 126-152 | Phase 3 "For this Phase" repeats procedural steps already in Core Workflow | Deduplicate: reference Core Workflow steps instead |

---

## AI-Readiness Scoring (per ai-readiness-scoring.md)

| Dimension | Score (0-10) | Notes |
|-----------|--------------|-------|
| YAML Frontmatter | 8 | Complete, valid, but `agent: agent` is odd |
| Summary Paragraph | 0 | No summary paragraph after frontmatter — jumps straight to `# Purpose` |
| Language-tagged Code Blocks | 0 | No fenced code blocks with language identifiers |
| Cross-reference Resolution | 5 | External URLs work; internal `docs/` refs are directory-level only |
| Heading Density | 7 | Good structure but 4-level nesting in phases |
| Single Source of Truth | 6 | Some duplication between Core Workflow and Phase-specific steps |

**Overall AI-Readiness: ~4.3/10** — Needs summary paragraph, code blocks, internal links, and deduplication.

---

## Enhancement Opportunities

1. **Add summary paragraph** after frontmatter describing the prompt's purpose in 2-3 sentences
2. **Convert command examples to fenced code blocks** with `bash` language tags
3. **Structure all phase procedures** as Steps → Tasks → Actions per enhance-markdown template
4. **Add internal markdown links** to generated docs (e.g., `[Phase 3 output](../hermes/index.md)`)
5. **Convert Template Variables table** to use code fences for paths
6. **Deduplicate procedural content** between Core Workflow and Phase sections
7. **Add Skills/Subagents/Personas sections** if applicable (per detection rules)
8. **Convert Verification Gates to a table** with Gate #, Description, Status columns

---

## Phase 1 Complete

Artifacts created:
- `docs/multi-agent-research-template-context.md` — Two-way dependency catalog
- `docs/multi-agent-research-template-issues-context.md` — This file

Next: Phase 2 — Create dual-channel fix plan (plugin system + companion markdown)