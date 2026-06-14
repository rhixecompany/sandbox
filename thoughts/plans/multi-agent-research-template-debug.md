# multi-agent-research-template — Fix Plan (Debug)

**Purpose:** multi-agent-research-template
**Generated:** 2026-06-14
**Source Issues:** `docs/multi-agent-research-template-issues-context.md`
**Target File:** `./sample.prompt.txt`

---

## Fix Plan Overview

| Batch | Issues | Files | Status |
|-------|--------|-------|--------|
| 1 (PoC) | HIGH-001, HIGH-002, HIGH-003, MEDIUM-001, MEDIUM-002, MEDIUM-003, MEDIUM-004 | sample.prompt.txt (7 issues) | 🔄 Ready |
| 2 | MEDIUM-005, MEDIUM-006, MEDIUM-007, MEDIUM-008, LOW-001, LOW-002, LOW-003 | sample.prompt.txt (7 issues) | ⏳ Pending |
| 3 | LOW-004, LOW-005, LOW-006 | sample.prompt.txt (3 issues) | ⏳ Pending |

**Batch Size:** 7 issues (matches enhance-markdown batch size)
**Proof-of-Concept Gate:** Batch 1 must pass verification before Batch 2

---

## Batch 1 Fixes (Proof-of-Concept — Critical/High Priority)

### HIGH-001: Frontmatter missing required `name` field
- **Location:** Lines 1-6 (frontmatter block)
- **Fix:** Add `name: multi-agent-research-template` to frontmatter
- **Action:** `patch` — insert after `title:` line

### HIGH-002: Frontmatter uses non-standard `mode: agent` field
- **Location:** Line 5
- **Fix:** Remove `mode: agent` line entirely
- **Action:** `patch` — delete line 5

### HIGH-003: No `trigger` field in frontmatter
- **Location:** Lines 1-6
- **Fix:** Add `trigger: /multi-agent-research` to frontmatter
- **Action:** `patch` — insert after `tags:` line

### MEDIUM-001: Template Variables table backslash escaping
- **Location:** Lines 17-25
- **Fix:** Wrap path values in inline code: `` `C:\Users\Alexa\Desktop\SandBox` `` and `` `docs/` ``
- **Action:** `patch` — replace table rows with escaped versions

### MEDIUM-002: Phase task lists use bullets not checkboxes
- **Location:** Lines 59-65 (Phase 1), 69-112 (Phase 2), 128-141 (Phase 3), 155-160 (Phase 4), 164-168 (Phase 5), 172-178 (Phase 6)
- **Fix:** Convert all `- ` bullets to `- [ ] ` in all six phases
- **Action:** `patch` — six separate replacements (one per phase block)

### MEDIUM-003: Phase 3 URLs as raw text not markdown links
- **Location:** Lines 130-141
- **Fix:** Convert 12 URLs to `[Title](URL)` format with descriptive titles
- **Action:** `patch` — replace URL list with markdown links

### MEDIUM-004: Phase 2 "After research" needs Steps/Tasks structure
- **Location:** Lines 113-124
- **Fix:** Restructure as Steps (numbered) with Tasks (checkboxes):
  1. Step: Web search for installation/testing/config guidance
     - [ ] Search each MCP/tool
     - [ ] Extract relevant links
  2. Step: Save one Markdown file per page
     - [ ] Create docs/ subfolders
     - [ ] Build index catalog
  3. Step: Read generated Markdown files
     - [ ] Update plan from findings
  4. Step: Implement only after plan is complete
     - [ ] Execute plan
  5. Step: Verify implementation
     - [ ] Run verification checks
- **Action:** `patch` — replace prose block with structured Steps/Tasks

---

## Batch 2 Fixes (Post-PoC Verification)

### MEDIUM-005: Output Requirements & Verification Gates as tables
- **Location:** Lines 180-196
- **Fix:** Convert both sections to markdown tables with columns (Item, Description/Criteria)
- **Action:** `patch` — two table replacements

### MEDIUM-006: Agent Mapping as table
- **Location:** Lines 29-32
- **Fix:** Convert to table: | Agent | Approach | Notes |
- **Action:** `patch` — replace dash list with table

### MEDIUM-007: Missing Skills Required table
- **Location:** After frontmatter (after line 6)
- **Fix:** Add Skills Required table mapping frontmatter tags to purposes:
  | Skill | Purpose |
  |-------|---------|
  | codex | Codex agent execution |
  | copilot | Copilot agent execution |
  | hermes | Hermes agent execution |
  | research | Research workflow |
  | planning | Planning workflow |
  | automation | Automation workflow |
- **Action:** `patch` — insert table after frontmatter

### MEDIUM-008: Frontmatter missing recommended fields
- **Location:** Lines 1-6
- **Fix:** Add `version: "1.0.0"`, `author: "Hermes Agent"`, `license: "MIT"`, `metadata.hermes.related_skills: []`
- **Action:** `patch` — insert before closing `---`

### LOW-001: Core Workflow duplicates Phase steps
- **Location:** Lines 45-53 vs Phase-specific sections
- **Fix:** Reference Core Workflow in phases; keep only phase-specific details in "For this Phase" sections
- **Action:** `patch` — consolidate duplicate content

### LOW-002: No verification checklist at end of file
- **Location:** End of file (after line 196)
- **Fix:** Add verification checklist section with 7+ items
- **Action:** `patch` — append new section

### LOW-003: Phase headings use H3 but template expects H2
- **Location:** Lines 55, 66, 126, 154, 162, 170
- **Fix:** Change `### Phase N:` to `## Phase N:` for all 6 phases
- **Action:** `patch` — six heading level changes

---

## Batch 3 Fixes (Final Polish)

### LOW-004: Template variables use `{{var}}` syntax but no processing hint
- **Location:** Lines 17-24
- **Fix:** Add comment: `<!-- Template variables use Jinja2-style {{var}} syntax -->`
- **Action:** `patch` — insert comment after Template Variables heading

### LOW-005: "Shared Rules" section could be checkboxes
- **Location:** Lines 34-41
- **Fix:** Convert numbered list to `- [ ]` format with note: "These are principles, not tasks"
- **Action:** `patch` — replace numbered list

### LOW-006: File extension is `.txt` not `.prompt.md`
- **Location:** Filename
- **Fix:** Rename `sample.prompt.txt` → `multi-agent-research-template.prompt.md`
- **Action:** `terminal` — `mv` command; update any references

---

## Execution Strategy

**Tool:** `patch` (targeted find-and-replace) + `terminal` (for rename)
**Order:** Frontmatter fixes first (HIGH-001, HIGH-002, HIGH-003), then structural (MEDIUM-002, MEDIUM-003, MEDIUM-004), then table/escaping (MEDIUM-001)
**Verification:** After each batch: re-read file, check frontmatter parses, check markdown renders, verify issues resolved

---

## Plugin System Registration

Plan registered under namespace: `multi-agent-research-template-debug`
Specs registered for: fix application, verification