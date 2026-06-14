# multi-agent-research-template — Audit Issues Context

**Generated:** 2026-06-14
**Source File:** `./sample.prompt.txt`
**Purpose:** multi-agent-research-template
**Audit Mode:** Full enhance-markdown audit (fresh run)

---

## Issue Summary

| Severity | Count |
|----------|-------|
| High | 3 |
| Medium | 8 |
| Low | 6 |

---

## Issues Detail

### HIGH-001: Frontmatter missing required `name` field
- **Location:** Lines 1-6 (frontmatter block)
- **Description:** Frontmatter has `title`, `description`, `tags`, `mode` but no `name` field. The `name` field is required per enhance-markdown verification checklist and Hermes prompt convention.
- **Impact:** Cannot resolve purpose from frontmatter; breaks trigger/filename matching; skill registration incomplete
- **Fix:** Add `name: multi-agent-research-template` to frontmatter

### HIGH-002: Frontmatter uses non-standard `mode: agent` field
- **Location:** Line 5
- **Description:** `mode: agent` is not a standard Hermes prompt frontmatter field. Standard fields: name, title, description, trigger, tags, version, author, license, metadata.
- **Impact:** May confuse parsers; not portable across systems
- **Fix:** Remove `mode: agent` or move to `metadata.custom.mode` if needed

### HIGH-003: No `trigger` field in frontmatter
- **Location:** Lines 1-6
- **Description:** Missing `trigger` field which should match the command to invoke this prompt (e.g., `/multi-agent-research`)
- **Impact:** Cannot be invoked via slash command; breaks Hermes prompt convention
- **Fix:** Add `trigger: /multi-agent-research` to frontmatter

### MEDIUM-001: Template Variables table backslash escaping
- **Location:** Lines 17-25
- **Description:** Path values contain unescaped backslashes (`C:\Users\Alexa\Desktop\SandBox`) which render incorrectly in markdown tables
- **Impact:** Display corruption; path misinterpretation
- **Fix:** Wrap path values in inline code or escape backslashes (`C:\\Users\\Alexa\\Desktop\\SandBox`)

### MEDIUM-002: Phase task lists use bullets not checkboxes
- **Location:** Lines 59-65 (Phase 1), 69-112 (Phase 2), 128-141 (Phase 3), 155-160 (Phase 4), 164-168 (Phase 5), 172-178 (Phase 6)
- **Description:** All phase steps use `- ` bullet format instead of `- [ ]` task checkbox format per enhance-markdown template
- **Impact:** Not trackable as actionable tasks; inconsistent with template standard
- **Fix:** Convert all phase bullet lists to `- [ ] Task description` format

### MEDIUM-003: Phase 3 URLs as raw text not markdown links
- **Location:** Lines 130-141
- **Description:** 12 Hermes documentation URLs listed as raw text instead of `[Title](URL)` markdown links
- **Impact:** Not clickable; no descriptive context; harder to audit
- **Fix:** Convert each URL to markdown link with descriptive title

### MEDIUM-004: Phase 2 "After research" section needs Steps/Tasks structure
- **Location:** Lines 113-124
- **Description:** Prose paragraph with bullet points instead of structured Steps with nested Tasks per enhance-markdown template
- **Impact:** Inconsistent phase structure; not parseable as workflow
- **Fix:** Restructure as Steps (numbered) with Tasks (checkboxes) per phase template

### MEDIUM-005: Output Requirements & Verification Gates as lists not tables
- **Location:** Lines 180-196
- **Description:** Both sections use bullet lists instead of markdown tables for scannability
- **Impact:** Harder to scan; inconsistent with enhance-markdown template which uses tables
- **Fix:** Convert to markdown tables with columns (Item, Description, Criteria)

### MEDIUM-006: Agent Mapping as dash list not table
- **Location:** Lines 29-32
- **Description:** Agent mapping uses dash list instead of markdown table
- **Impact:** Inconsistent formatting; harder to extend
- **Fix:** Convert to table with columns (Agent, Approach, Notes)

### MEDIUM-007: Missing Skills Required table
- **Location:** After frontmatter (expected after line 6)
- **Description:** No Skills Required table present; skills only in frontmatter tags
- **Impact:** Inconsistent with enhance-markdown template; no purpose/skill mapping
- **Fix:** Add Skills Required table mapping tags to purposes

### MEDIUM-008: Frontmatter missing recommended fields
- **Location:** Lines 1-6
- **Description:** Missing `version`, `author`, `license`, `metadata.hermes.related_skills`
- **Impact:** Incomplete metadata; skill discovery broken
- **Fix:** Add all recommended fields

### LOW-001: Core Workflow duplicates Phase-specific steps
- **Location:** Lines 45-53 (Core Workflow) vs Lines 126-152 (Phase 3 "For this Phase") and similar in other phases
- **Description:** Core Workflow 7 steps substantially overlap with phase-specific "For this Phase" sections
- **Impact:** Redundancy; maintenance burden; DRY violation
- **Fix:** Reference Core Workflow steps in phases; keep only phase-specific details

### LOW-002: No verification checklist at end of file
- **Location:** End of file (after line 196)
- **Description:** Missing verification checklist with acceptance criteria per enhance-markdown template
- **Impact:** No clear completion gate
- **Fix:** Add verification checklist section

### LOW-003: Phase headings use `### Phase N:` but template expects `## Phase N: Title`
- **Location:** Lines 55, 66, 126, 154, 162, 170
- **Description:** Phase headings are H3 (`###`) but enhance-markdown template uses H2 (`##`) for phases
- **Impact:** Heading hierarchy inconsistency
- **Fix:** Promote phase headings to H2

### LOW-004: Template variables use `{{var}}` syntax but no processing hint
- **Location:** Lines 17-24
- **Description:** Variables use `{{workspace_root}}` etc. but no comment about templating engine
- **Impact:** Ambiguity about how variables are substituted
- **Fix:** Add comment noting templating syntax (Jinja2-style)

### LOW-005: "Shared Rules" section uses numbered list but could be checkboxes
- **Location:** Lines 34-41
- **Description:** 8 rules as numbered list; could be actionable checkboxes
- **Impact:** Not trackable
- **Fix:** Convert to `- [ ]` format or keep as principles with note

### LOW-006: File extension is `.txt` not `.md` or `.prompt.md`
- **Location:** Filename
- **Description:** Content is structured markdown with frontmatter but saved as `.txt`
- **Impact:** Editor support; convention violation; confuse with plain text
- **Fix:** Rename to `multi-agent-research-template.prompt.md` or `.prompt.md`

---

## Frontmatter Parse Check

```
✅ YAML parses as single document
✅ No double-fence repeats in first 60 lines (only 2 fences: open/close)
⚠️  No `skills:` field in frontmatter (tags used instead)
❌ Missing REQUIRED fields: name, trigger
❌ Non-standard field: mode
❌ Missing recommended fields: version, author, license, metadata.hermes.related_skills
```

---

## Structure Validation

| Check | Status | Notes |
|-------|--------|-------|
| H1 title present | ✅ | "# Purpose" (but generic) |
| H2 sections present | ⚠️ | Purpose, Template Variables, Agent Mapping, Shared Rules, Core Workflow, Default Research Targets, Output Requirements, Verification Gates |
| Phase headings at H2 | ❌ | Currently H3 (`### Phase N:`) |
| Skills Required table | ❌ | Missing entirely |
| Verification checklist | ❌ | Missing entirely |
| No placeholder text | ✅ | No `[Add ... here]` found |
| Trigger in frontmatter | ❌ | Missing |
| Name in frontmatter | ❌ | Missing |

---

## Recommendations (Priority Order)

1. **CRITICAL:** Add `name`, `trigger` to frontmatter; remove `mode` field
2. **HIGH:** Convert phase headings to H2; convert all task lists to checkboxes
3. **HIGH:** Convert Phase 3 URLs to markdown links; restructure Phase 2 "After research"
4. **MEDIUM:** Add Skills Required table; fix template variable table escaping
5. **MEDIUM:** Convert Agent Mapping, Output Requirements, Verification Gates to tables
6. **MEDIUM:** Add missing frontmatter fields (version, author, license, metadata.hermes.related_skills)
7. **LOW:** Deduplicate Core Workflow vs Phase steps; add verification checklist; rename file to `.prompt.md`