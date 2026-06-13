# multi-agent-research-template — Fix Plan (Debug)

**Purpose:** multi-agent-research-template  
**Generated:** 2026-06-13  
**Source Issues:** `docs/multi-agent-research-template-issues-context.md`  
**Target File:** `C:\Users\Alexa\Desktop\SandBox\sample.prompt.md`

---

## Fix Plan Overview

| Batch | Issues | Files | Status |
|-------|--------|-------|--------|
| 1 (PoC) | ISSUE-001, ISSUE-002, ISSUE-003, ISSUE-004, ISSUE-005, ISSUE-006, ISSUE-007 | sample.prompt.md (7 issues) | 🔄 Ready |
| 2 | ISSUE-008, AI-readiness enhancements | sample.prompt.md | ⏳ Pending |

**Batch Size:** 7 issues (matches enhance-markdown batch size)  
**Proof-of-Concept Gate:** Batch 1 must pass verification before Batch 2

---

## Batch 1 Fixes (Proof-of-Concept)

### ISSUE-001: Template Variables table backslash escaping
- **Location:** Lines 17-25
- **Fix:** Wrap path values in inline code or code fences; escape backslashes in markdown table
- **Action:** `patch` — replace table rows with escaped versions

### ISSUE-002: Phase task lists need Task checkbox format
- **Location:** Lines 59-65 (Phase 1), 69-112 (Phase 2), 128-141 (Phase 3), 155-160 (Phase 4), 164-168 (Phase 5), 172-178 (Phase 6)
- **Fix:** Convert bullet points to `- [ ] Task description` format per enhance-markdown template
- **Action:** `patch` — replace each phase's bullet list with checkbox tasks

### ISSUE-003: Phase 3 URLs as raw text
- **Location:** Lines 130-141
- **Fix:** Convert to markdown links with descriptive titles
- **Action:** `patch` — replace URL list with `[Title](URL)` format

### ISSUE-004: Phase 2 "After research" needs Steps/Tasks structure
- **Location:** Lines 113-124
- **Fix:** Restructure as Steps with nested Tasks per enhance-markdown template
- **Action:** `patch` — replace prose with Steps/Tasks format

### ISSUE-005: Output Requirements & Verification Gates as tables
- **Location:** Lines 180-196
- **Fix:** Convert to markdown tables for scannability
- **Action:** `patch` — replace lists with tables

### ISSUE-006: Agent Mapping as table
- **Location:** Lines 29-32
- **Fix:** Convert dash list to markdown table
- **Action:** `patch` — replace with table

### ISSUE-007: Frontmatter `agent: agent` cleanup
- **Location:** Line 5
- **Fix:** Remove or clarify the `agent` field
- **Action:** `patch` — remove line or update value

---

## Batch 2 Fixes (Post-PoC Verification)

### ISSUE-008: Deduplicate Core Workflow vs Phase steps
- **Location:** Lines 45-53 (Core Workflow) vs Lines 126-152 (Phase 3 "For this Phase") and similar
- **Fix:** Reference Core Workflow steps instead of repeating; keep Phase-specific details only
- **Action:** `patch` — consolidate

### AI-Readiness Enhancements
- **Add summary paragraph** after frontmatter (2-3 sentences)
- **Add language-tagged code blocks** for all command examples
- **Add internal markdown links** to generated docs
- **Add Skills/Subagents/Personas sections** per detection rules
- **Convert to 11-section template** (cross-system prompt for Codex/Copilot/Hermes)

---

## Execution Strategy

**Tool:** `patch` (targeted find-and-replace)  
**Order:** Apply fixes sequentially, verify after each  
**Verification:** Re-read file, check frontmatter parses, check markdown renders

---

## Plugin System Registration

Plan registered under namespace: `multi-agent-research-template-debug`  
Specs registered for: fix application, verification