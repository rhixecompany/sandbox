# Hermes Docs Verification & Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Verify all 11 newly created Hermes Agent documentation markdown files are complete, properly formatted, and cross-referenced — then fix any issues found.

**Architecture:** Read each file, validate structure/content/formatting, compare against source URLs for completeness, fix issues, and re-verify.

**Tech Stack:** Markdown, Hermes file tools (read_file, write_file, patch, search_files)

---

## Current State

12 files exist under `docs/`:
- `INDEX.md` — master index
- `user-guide/features/skills/index.md` — 9.3 KB, 299 lines
- `user-guide/features/mcp/index.md` — 7.8 KB, 309 lines
- `user-guide/features/personality/index.md` — 6.7 KB, 218 lines
- `user-guide/features/context-files/index.md` — 8.4 KB, 213 lines
- `user-guide/features/tools/index.md` — 6.5 KB, 163 lines
- `user-guide/features/hooks/index.md` — 13.4 KB, 392 lines
- `user-guide/features/plugins/index.md` — 7.3 KB, 193 lines
- `guides/use-mcp-with-hermes/index.md` — 6.2 KB, 264 lines
- `guides/tips/index.md` — 7.2 KB, 195 lines
- `getting-started/quickstart/index.md` — 4.4 KB, 182 lines
- `getting-started/learning-path/index.md` — 6.9 KB, 106 lines

---

## Phase 1: Structural Verification

### Task 1: Verify all files exist and are non-empty

**Objective:** Confirm all 12 target files exist and have meaningful content.

**Files:**
- Read: all 12 files listed above

**Step 1: Run existence check**

Use `search_files` with `target="files"` and `pattern="index.md"` under `docs/` to list all files.

**Step 2: Verify each file is ≥ 1 KB**

Read each file and confirm `file_size > 1000`. All files should pass (smallest is quickstart at 4.4 KB).

**Step 3: Report any failures**

If any file is missing or < 1 KB, flag it for Phase 3 remediation.

---

### Task 2: Verify markdown structure consistency

**Objective:** Every file should have: source URL blockquote, H1 title, H2 sections, code blocks where appropriate, and "See Also" section.

**Files:**
- Read: all 12 files

**Step 1: Check each file starts with `# ` (H1)**

Read first 3 lines of each file. Expected pattern:
```
# <Title>
>
> **Source:** [...](url)
```

**Step 2: Check each file has `## See Also` section**

Search for `## See Also` in each file. All 12 files should have this section.

**Step 3: Check code block formatting**

Verify code blocks use triple backticks with language identifiers (e.g., ` ```yaml `, ` ```bash `, ` ```python `).

**Step 4: Report structural issues**

Log any files missing expected sections for Phase 3.

---

### Task 3: Verify cross-references between files

**Objective:** Internal links between docs should point to correct relative paths.

**Files:**
- Read: all 12 files (focus on "See Also" sections)

**Step 1: Extract all internal links**

Search for patterns like `[...](` in each file's See Also section.

**Step 2: Verify link targets exist**

Expected cross-references:
- Skills → MCP, Tools, Hooks, Plugins (external URLs — OK)
- MCP → Use MCP with Hermes (external URL — OK)
- Personality → Context Files, Tips (external URLs — OK)
- Context Files → Personality (external URL — OK)
- Tools → Skills, MCP (external URLs — OK)
- Hooks → Plugins (external URL — OK)
- Plugins → Hooks (external URL — OK)
- Use MCP with Hermes → MCP, Tools (external URLs — OK)
- Tips → Context Files, Personality, Skills (external URLs — OK)
- Quickstart → Learning Path, Tips (external URLs — OK)
- Learning Path → Tips (external URL — OK)

**Step 3: Note that all See Also links use external URLs**

This is acceptable since the docs are standalone files. No broken internal links to fix.

---

## Phase 2: Content Completeness Verification

### Task 4: Verify Skills page completeness

**Objective:** Ensure the Skills page covers all major topics from the source.

**Files:**
- Read: `docs/user-guide/features/skills/index.md`
- Compare against: source URL content already captured

**Step 1: Check for required sections**

Verify these sections exist:
- [x] Overview
- [x] Starting with a Blank Slate
- [x] Using Skills (Slash Commands, Natural Conversation)
- [x] Progressive Disclosure
- [x] SKILL.md Format
- [x] Platform-Specific Skills
- [x] Skill Output and Media Delivery
- [x] Conditional Activation (Fallback Skills)
- [x] Secure Setup on Load
- [x] Skill Config Settings
- [x] Skill Directory Structure
- [x] External Skill Directories
- [x] Skill Bundles
- [x] Agent-Managed Skills
- [x] Skills Hub (with Supported Hub Sources, Trust Levels)
- [x] See Also

**Step 2: Verify code examples are complete**

Check that SKILL.md format example has full YAML frontmatter + markdown body.

**Step 3: No action needed if all sections present**

---

### Task 5: Verify MCP page completeness

**Objective:** Ensure the MCP page covers all major topics.

**Files:**
- Read: `docs/user-guide/features/mcp/index.md`

**Step 1: Check for required sections**

- [x] Overview (What MCP Gives You)
- [x] Quick Start
- [x] Catalog: One-Click Install
- [x] Tool Selection at Install Time
- [x] Trust Model
- [x] Runtime ENV_VAR Substitution
- [x] Two Kinds of MCP Servers (Stdio, HTTP, OAuth, mTLS)
- [x] Tool Filtering (Whitelist, Blacklist, Disable Utilities)
- [x] How Hermes Registers MCP Tools
- [x] MCP Utility Tools
- [x] Runtime Behavior (Discovery, Dynamic, Reloading, Toolsets)
- [x] Security Model
- [x] Parallel Tool Calls
- [x] MCP Sampling Support
- [x] Running Hermes as an MCP Server
- [x] Troubleshooting
- [x] See Also

---

### Task 6: Verify Hooks page completeness

**Objective:** Ensure the Hooks page covers all three hook systems and all plugin hook types.

**Files:**
- Read: `docs/user-guide/features/hooks/index.md`

**Step 1: Check for required sections**

- [x] Overview (3 hook systems table)
- [x] Gateway Event Hooks (Creating, HOOK.yaml, handler.py, Events, Examples, BOOT.md tutorial)
- [x] Plugin Hooks (Quick Reference table, all callback signatures)
- [x] Shell Hooks (Config schema, JSON wire protocol, worked examples, consent model, CLI, security)
- [x] See Also

**Step 2: Verify all plugin hook types are documented**

Check for: pre_tool_call, post_tool_call, pre_llm_call, post_llm_call, on_session_start, on_session_end, on_session_finalize, on_session_reset, subagent_stop, pre_gateway_dispatch, pre_approval_request, post_approval_response, transform_tool_result, transform_terminal_output, transform_llm_output

---

### Task 7: Verify remaining pages completeness

**Objective:** Quick check that remaining 8 pages have proper structure.

**Files:**
- Read first 20 lines of each remaining file:
  - `personality/index.md`
  - `context-files/index.md`
  - `tools/index.md`
  - `plugins/index.md`
  - `use-mcp-with-hermes/index.md`
  - `tips/index.md`
  - `quickstart/index.md`
  - `learning-path/index.md`

**Step 1: Verify each has H1 + source URL + Overview section**

All files should start with `# Title`, followed by source blockquote, then `## Overview`.

**Step 2: No action needed if structure is correct**

---

## Phase 3: Remediation (if issues found)

### Task 8: Fix any structural issues found in Phase 1

**Objective:** Repair any files with missing sections or formatting issues.

**Files:**
- Modify: any files flagged in Tasks 1-3

**Step 1: For each flagged issue, use `patch` to fix**

Example fixes:
- Add missing `## See Also` section
- Fix broken markdown formatting
- Add missing code block language identifiers

**Step 2: Re-verify fixed files**

Re-read patched files to confirm fixes applied correctly.

---

### Task 9: Fix any content gaps found in Phase 2

**Objective:** Add missing sections to any pages that lack required content.

**Files:**
- Modify: any pages with missing sections

**Step 1: For each missing section, use `patch` to add content**

Use the source URL content (already captured in conversation context) to fill gaps.

**Step 2: Re-verify fixed pages**

---

## Phase 4: Final Verification

### Task 10: Run final validation pass

**Objective:** Confirm all 12 files pass structural and content checks.

**Files:**
- Read: all 12 files

**Step 1: Count total files**

Run `search_files(pattern="index.md", target="files", path="docs/")` — expect 12 results in our subdirectories.

**Step 2: Verify total content size**

Sum of all file sizes should be ≥ 70 KB (current total: ~84 KB).

**Step 3: Generate final report**

Output a summary table with:
- File path
- Size (KB)
- Line count
- Status (PASS/FAIL)

**Step 4: Commit**

```bash
cd C:\Users\Alexa\Desktop\SandBox
git add docs/
git commit -m "docs: add Hermes Agent documentation (11 pages + index)"
```

---

## Risks & Tradeoffs

- **Risk:** Some source pages may have been updated since capture. Mitigation: files are comprehensive snapshots.
- **Tradeoff:** All See Also links use external URLs rather than relative paths. This is intentional for standalone file readability.
- **Risk:** The `docs/` directory has 1156 existing .md files from prior work. Our 12 new files are in freshly created subdirectories and don't conflict.

## Open Questions

1. Should internal cross-references use relative paths instead of external URLs?
2. Should the INDEX.md include file sizes and line counts?
3. Is the current directory structure (`user-guide/features/`, `guides/`, `getting-started/`) the preferred organization?
