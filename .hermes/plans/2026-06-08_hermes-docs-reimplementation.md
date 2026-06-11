# Hermes Docs Re-Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Re-create all 12 Hermes Agent documentation markdown files from scratch using only this plan and the source URLs. Each file must match the established format: H1 title, source URL blockquote, structured H2 sections with code blocks, tables, and a `## See Also` section.

**Architecture:** Create directory structure first, then write files in dependency order (leaf pages first, index last). Each file is written via `write_file` with complete content. Verify after each file.

**Tech Stack:** Markdown, Hermes file tools (write_file, read_file, search_files)

---

## Current State

12 files already exist under `docs/` at these paths:
```
docs/INDEX.md
docs/user-guide/features/skills/index.md
docs/user-guide/features/mcp/index.md
docs/user-guide/features/personality/index.md
docs/user-guide/features/context-files/index.md
docs/user-guide/features/tools/index.md
docs/user-guide/features/hooks/index.md
docs/user-guide/features/plugins/index.md
docs/guides/use-mcp-with-hermes/index.md
docs/guides/tips/index.md
docs/getting-started/quickstart/index.md
docs/getting-started/learning-path/index.md
```

All files are verified complete (88.8 KB total, 2,656 lines). This plan re-creates them from scratch.

---

## Phase 1: Directory Setup

### Task 1: Create directory structure

**Objective:** Ensure all target directories exist.

**Files:**
- Create dirs: `docs/user-guide/features/skills`, `docs/user-guide/features/mcp`, `docs/user-guide/features/personality`, `docs/user-guide/features/context-files`, `docs/user-guide/features/tools`, `docs/user-guide/features/hooks`, `docs/user-guide/features/plugins`, `docs/guides/use-mcp-with-hermes`, `docs/guides/tips`, `docs/getting-started/quickstart`, `docs/getting-started/learning-path`

**Step 1: Create directories**

```python
import os
base = r"C:\Users\Alexa\Desktop\SandBox\docs"
dirs = [
    "user-guide/features/skills",
    "user-guide/features/mcp",
    "user-guide/features/personality",
    "user-guide/features/context-files",
    "user-guide/features/tools",
    "user-guide/features/hooks",
    "user-guide/features/plugins",
    "guides/use-mcp-with-hermes",
    "guides/tips",
    "getting-started/quickstart",
    "getting-started/learning-path",
]
for d in dirs:
    os.makedirs(os.path.join(base, d), exist_ok=True)
```

**Step 2: Verify directories exist**

Run `search_files(target="files", pattern="*", path="docs/user-guide/features/skills")` — should return 0 results (empty dir).

---

## Phase 2: Write Leaf Pages (no internal dependencies)

### Task 2: Write Skills page

**Objective:** Create the Skills System documentation page.

**Files:**
- Create: `docs/user-guide/features/skills/index.md`

**Step 1: Write file with `write_file`**

Content must include:
- H1: `# Skills System`
- Source blockquote: `> **Source:** [hermes-agent.nousresearch.com/docs/user-guide/features/skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)`
- Sections: Overview, Starting with a Blank Slate, Using Skills (Slash Commands, Natural Conversation), Progressive Disclosure, SKILL.md Format, Platform-Specific Skills, Skill Output and Media Delivery, Conditional Activation, Secure Setup on Load, Skill Config Settings, Skill Directory Structure, External Skill Directories, Skill Bundles, Agent-Managed Skills, Skills Hub (with Supported Hub Sources table, Trust Levels table), See Also
- Code blocks with `bash`, `yaml`, `markdown` language identifiers
- See Also section with links to Bundled Skills Catalog and Official Optional Skills Catalog

**Step 2: Verify file**

Read back and confirm: H1 present, source URL present, `## See Also` present, size > 8 KB.

---

### Task 3: Write MCP page

**Objective:** Create the MCP documentation page.

**Files:**
- Create: `docs/user-guide/features/mcp/index.md`

**Step 1: Write file with `write_file`**

Content must include:
- H1: `# MCP (Model Context Protocol)`
- Source blockquote
- Sections: Overview (What MCP Gives You), Quick Start, Catalog (One-Click Install, Tool Selection, Trust Model, ENV_VAR Substitution), Two Kinds of MCP Servers (Stdio, HTTP, OAuth, mTLS), Tool Filtering (Whitelist, Blacklist, Disable Utilities), How Hermes Registers MCP Tools, MCP Utility Tools, Runtime Behavior, Security Model, Parallel Tool Calls, MCP Sampling Support, Running Hermes as an MCP Server (Available Tools table), Troubleshooting, See Also
- Code blocks with `bash`, `yaml`, `json` language identifiers
- See Also: Use MCP with Hermes, CLI Commands, FAQ

**Step 2: Verify file**

Read back and confirm: size > 7 KB, all sections present.

---

### Task 4: Write Personality page

**Objective:** Create the Personality & SOUL.md documentation page.

**Files:**
- Create: `docs/user-guide/features/personality/index.md`

**Step 1: Write file with `write_file`**

Content must include:
- H1: `# Personality & SOUL.md`
- Source blockquote
- Sections: Overview, How SOUL.md Works Now (Important Behavior list), Why This Design, Where to Edit It, What Should Go in SOUL.md, Good SOUL.md Content (with example), Security Scanning, SOUL.md vs AGENTS.md (table), SOUL.md vs /personality (table), Built-in Personalities (table with 14 personalities), Switching Personalities, Custom Personalities in Config, Recommended Workflow, See Also
- Code blocks with `markdown`, `yaml` language identifiers
- See Also: Context Files, Configuration, Tips & Best Practices, SOUL.md Guide, Skins & Themes

**Step 2: Verify file**

Read back and confirm: size > 6 KB, all sections present.

---

### Task 5: Write Context Files page

**Objective:** Create the Context Files documentation page.

**Files:**
- Create: `docs/user-guide/features/context-files/index.md`

**Step 1: Write file with `write_file`**

Content must include:
- H1: `# Context Files`
- Source blockquote
- Sections: Overview, Supported Context Files (table with 6 file types), AGENTS.md (Progressive Subdirectory Discovery, Example AGENTS.md), SOUL.md, .cursorrules, How Context Files Are Loaded (At Startup, During Session, Final Prompt Structure), Security/Prompt Injection Protection, Size Limits (table), Tips for Effective Context Files, Per-Subdirectory Context, See Also
- Code blocks with `markdown` language identifiers
- See Also: Personality & SOUL.md, Configuration, Context References

**Step 2: Verify file**

Read back and confirm: size > 8 KB, all sections present.

---

### Task 6: Write Tools page

**Objective:** Create the Tools & Toolsets documentation page.

**Files:**
- Create: `docs/user-guide/features/tools/index.md`

**Step 1: Write file with `write_file`**

Content must include:
- H1: `# Tools & Toolsets`
- Source blockquote
- Sections: Overview, Available Tools (table with 9 categories), Using Toolsets, Terminal Backends (table with 6 backends), Configuration, Docker Backend, SSH Backend, Singularity/Apptainer, Modal, Container Resources, Container Security, Background Process Management, Sudo Support, See Also
- Code blocks with `bash`, `yaml`, `python` language identifiers
- See Also: Skills System, MCP, Built-in Tools Reference, Toolsets Reference

**Step 2: Verify file**

Read back and confirm: size > 6 KB, all sections present.

---

### Task 7: Write Hooks page

**Objective:** Create the Event Hooks documentation page.

**Files:**
- Create: `docs/user-guide/features/hooks/index.md`

**Step 1: Write file with `write_file`**

Content must include:
- H1: `# Event Hooks`
- Source blockquote
- Sections: Overview (3 hook systems table), Gateway Event Hooks (Creating a Hook, HOOK.yaml, handler.py, Available Events table, Wildcard Matching, 3 Examples: Telegram Alert/Command Logger/Session Webhook, BOOT.md Tutorial), Plugin Hooks (Quick Reference table with 15 hook types, callback signatures for pre_tool_call/post_tool_call/pre_llm_call/post_llm_call/on_session_start/on_session_end/subagent_stop/pre_gateway_dispatch/transform_tool_result/transform_terminal_output/transform_llm_output), Shell Hooks (Config schema, JSON wire protocol, 4 Worked Examples, Consent Model, hermes hooks CLI table, Security, Ordering and Precedence), See Also
- Code blocks with `python`, `yaml`, `bash`, `json` language identifiers
- See Also: Plugins, Build a Hermes Plugin, Scheduled Tasks (Cron)

**Step 2: Verify file**

Read back and confirm: size > 13 KB, all sections present.

---

### Task 8: Write Plugins page

**Objective:** Create the Plugins documentation page.

**Files:**
- Create: `docs/user-guide/features/plugins/index.md`

**Step 1: Write file with `write_file`**

Content must include:
- H1: `# Plugins`
- Source blockquote
- Sections: Overview, Quick Overview, Minimal Working Example (hello-world plugin with plugin.yaml and __init__.py), Plugin Capabilities (table with 17 ctx.* APIs), Plugin Discovery (table with 5 sources), Plugin Sub-Categories (table with 6 sub-dirs), Plugin Manifest (plugin.yaml example), Enabling/Disabling Plugins, Distribution (Via pip, Via Nix), See Also
- Code blocks with `yaml`, `python`, `toml`, `nix`, `bash` language identifiers
- See Also: Build a Hermes Plugin, Event Hooks, Built-in Plugins, Adding Tools

**Step 2: Verify file**

Read back and confirm: size > 7 KB, all sections present.

---

### Task 9: Write Use MCP with Hermes guide

**Objective:** Create the practical MCP integration guide.

**Files:**
- Create: `docs/guides/use-mcp-with-hermes/index.md`

**Step 1: Write file with `write_file`**

Content must include:
- H1: `# Use MCP with Hermes`
- Source blockquote
- Sections: Overview, Installation (Standard, Separate, Prerequisites), Quick Start Workflow (3 steps), Tool Filtering (Whitelist, Blacklist, Disable Utilities, What Filtering Affects), WSL2: Bridge to Windows Chrome (Setup, Architecture, When to Use, Testing, Known Pitfalls), Common Usage Patterns (4 patterns: Local Project Assistant, GitHub Triage, Internal API, Documentation), End-to-End Setup Tutorial (3 phases), Safety Recommendations (5 rules), Troubleshooting, See Also
- Code blocks with `bash`, `yaml` language identifiers
- See Also: MCP Feature Reference, Tools & Toolsets, FAQ

**Step 2: Verify file**

Read back and confirm: size > 6 KB, all sections present.

---

### Task 10: Write Tips page

**Objective:** Create the Tips & Best Practices page.

**Files:**
- Create: `docs/guides/tips/index.md`

**Step 1: Write file with `write_file`**

Content must include:
- H1: `# Tips & Best Practices`
- Source blockquote
- Sections: Getting the Best Results (Be Specific, Provide Context, Use Context Files, Let Agent Use Tools, Use Skills), CLI Power User Tips (Multi-Line Input, Paste Detection, Interrupt/Redirect, Resume Sessions, Clipboard Image Paste, Slash Command Autocomplete, Verbose Mode), Context Files (AGENTS.md, SOUL.md, .cursorrules, Discovery), Memory & Skills (Memory vs Skills table, When to Create Skills, Managing Memory Capacity, Let Agent Remember), Performance & Cost (Prompt Cache, Appropriate Models, Background Processes), Messaging Platform Tips (Telegram, Discord, Slack), Safety (Never Commit Secrets, Review Context Files, Least-Privilege Credentials), See Also
- Code blocks with `bash`, `markdown` language identifiers
- See Also: CLI Usage, Context Files, Personality, Skills, FAQ

**Step 2: Verify file**

Read back and confirm: size > 7 KB, all sections present.

---

### Task 11: Write Quickstart page

**Objective:** Create the Quickstart page.

**Files:**
- Create: `docs/getting-started/quickstart/index.md`

**Step 1: Write file with `write_file`**

Content must include:
- H1: `# Quickstart`
- Source blockquote
- Sections: Overview, Prerequisites, Installation (3 variants), First Run (Setup, Nous Portal, Start Conversation), Basic CLI Usage, Configuration (config.yaml example), Profiles, Key Features at a Glance (table), Next Steps, Troubleshooting, See Also
- Code blocks with `bash`, `yaml` language identifiers
- See Also: Learning Path, Tips & Best Practices, Skills System, Tools & Toolsets (relative paths: `learning-path/index.md`, `../guides/tips/index.md`, `../user-guide/features/skills/index.md`, `../user-guide/features/tools/index.md`)

**Step 2: Verify file**

Read back and confirm: size > 4 KB, all sections present.

---

### Task 12: Write Learning Path page

**Objective:** Create the Learning Path page.

**Files:**
- Create: `docs/getting-started/learning-path/index.md`

**Step 1: Write file with `write_file`**

Content must include:
- H1: `# Learning Path`
- Source blockquote
- Sections: Overview, By Experience Level (table with 3 levels), By Use Case (6 use cases: CLI coding assistant, Telegram/Discord bot, automate tasks, build custom tools/skills, train models, Python library), Key Features at a Glance (table with 11 features), Tips, See Also
- See Also: Quickstart, Tips & Best Practices, Skills System, MCP (relative paths: `../quickstart/index.md`, `../guides/tips/index.md`, `../user-guide/features/skills/index.md`, `../user-guide/features/mcp/index.md`)

**Step 2: Verify file**

Read back and confirm: size > 6 KB, all sections present.

---

## Phase 3: Write Index Page

### Task 13: Write INDEX.md

**Objective:** Create the master index page that catalogs all 11 docs.

**Files:**
- Create: `docs/INDEX.md`

**Step 1: Write file with `write_file`**

Content must include:
- H1: `# Hermes Agent Documentation`
- Source blockquote with generation date
- Index section with 3 tables: User Guide — Features (7 pages), Guides (2 pages), Getting Started (2 pages)
- Source URLs table (11 rows)
- Directory Structure code block (full tree)
- See Also section (11 relative links to all pages)

**Step 2: Verify file**

Read back and confirm: size > 5 KB, all 11 pages indexed, directory tree renders correctly.

---

## Phase 4: Final Verification

### Task 14: Validate all 12 files

**Objective:** Confirm all files pass structural and content checks.

**Files:**
- Read: all 12 files

**Step 1: Check all files exist**

Run `execute_code` to verify each file path exists and is ≥ 4 KB.

**Step 2: Check markdown structure**

For each file, verify:
- Starts with `# ` (H1)
- Has `**Source:**` blockquote in first 5 lines
- Has `## See Also` section
- Has ≥ 3 `## ` (H2) sections
- Code blocks use language identifiers

**Step 3: Check total content**

Total size should be ≥ 80 KB. Total lines should be ≥ 2,500.

**Step 4: Report results**

Output a table: file path, size, line count, PASS/FAIL.

---

## Risks & Tradeoffs

- **Risk:** Writing 12 large files in sequence may hit context limits. Mitigation: each task is self-contained; subagent-driven-development can parallelize.
- **Tradeoff:** Files are written fresh, overwriting existing verified content. This is intentional — the plan must be able to recreate everything from scratch.
- **Risk:** Code block content may drift from existing verified files. Mitigation: Phase 4 validation catches discrepancies.

## Open Questions

1. Should the plan include the full content of each file inline, or reference the existing files as templates?
2. Should cross-references use relative paths or external URLs? (Current: mix of both)
3. Is the current 3-level directory structure preferred over a flatter layout?
