# Multi-Agent Research Workflow Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Execute `/multi-agent-research` from `.github/prompts/multi-agent-research-template.prompt.md` end-to-end and produce indexed Markdown research outputs plus verified implementation notes.

**Architecture:** The workflow is executed in strict sequence: plan -> research -> extract -> index -> plan update -> implement -> verify. Outputs are organized by phase under `docs/multi-agent-research/` so the run is resumable and auditable. Each phase ends with a verification checkpoint and a commit.

**Tech Stack:** Copilot CLI tools, PowerShell, `web_fetch`, Markdown docs, git.

---

### Task 1: Initialize Run Artifacts

**Files:**
- Create: `docs/multi-agent-research/README.md`
- Create: `docs/multi-agent-research/index.md`
- Create: `docs/multi-agent-research/phase-1/summary.md`
- Verify: `.github/prompts/multi-agent-research-template.prompt.md` (modify only if the trigger is incorrect)
- Test: `docs/multi-agent-research/index.md`

- [ ] **Step 1: Create output directories**

Run: `New-Item -ItemType Directory -Force docs\multi-agent-research, docs\multi-agent-research\phase-1, docs\multi-agent-research\phase-2, docs\multi-agent-research\phase-3, docs\multi-agent-research\phase-4, docs\multi-agent-research\phase-5, docs\multi-agent-research\phase-6`
Expected: all directories exist.

- [ ] **Step 2: Add run README**

```md
# Multi-Agent Research Run

This directory stores outputs produced by `/multi-agent-research`.
Each phase has its own folder and summary.
```

- [ ] **Step 3: Add master index**

```md
# Multi-Agent Research Index

- [Phase 1](./phase-1/summary.md)
- [Phase 2](./phase-2/index.md)
- [Phase 3](./phase-3/index.md)
- [Phase 4](./phase-4/summary.md)
- [Phase 5](./phase-5/summary.md)
- [Phase 6](./phase-6/summary.md)
```

- [ ] **Step 4: Verify prompt trigger**

Run: `rg "/multi-agent-research" .github\prompts\multi-agent-research-template.prompt.md -n`
Expected: one match on the trigger line; if the trigger is wrong, correct the prompt file before commit.

- [ ] **Step 5: Commit**

```bash
git add docs/multi-agent-research .github/prompts/multi-agent-research-template.prompt.md
git commit -m "docs: initialize multi-agent research execution artifacts"
```

### Task 2: Execute Phase 1 (Skills Discovery and Audit)

**Files:**
- Create: `docs/multi-agent-research/phase-1/skills-browse.md`
- Create: `docs/multi-agent-research/phase-1/skills-search.md`
- Create: `docs/multi-agent-research/phase-1/skills-audit.md`
- Create: `docs/multi-agent-research/phase-1/debug-report.md`
- Modify: `docs/multi-agent-research/phase-1/summary.md`
- Test: `docs/multi-agent-research/phase-1/summary.md`

- [ ] **Step 1: Capture skills browse output**

Run: `hermes skills browse > docs\multi-agent-research\phase-1\skills-browse.md`
Expected: Markdown file with available skills list.

- [ ] **Step 2: Capture targeted skills search output**

Run: `hermes skills search "research" > docs\multi-agent-research\phase-1\skills-search.md`
Expected: Markdown file with research-related skills.

- [ ] **Step 3: Run and capture skills audit**

Run: `hermes /skills audit > docs\multi-agent-research\phase-1\skills-audit.md`
Expected: audit report saved.

- [ ] **Step 4: Run systematic debugging and capture result**

Run: `hermes /systematic-debugging > docs\multi-agent-research\phase-1\debug-report.md`
Expected: debug run output saved.

- [ ] **Step 5: Write phase summary**

```md
# Phase 1 Summary

- Skills discovery completed.
- Audit and debugging outputs captured.
- Any install/security findings are listed in this file.
```

- [ ] **Step 6: Commit**

```bash
git add docs/multi-agent-research/phase-1
git commit -m "docs: capture phase 1 skills discovery and audit outputs"
```

### Task 3: Execute Phase 2 (MCP Server and Tool Research)

**Files:**
- Create: `docs/multi-agent-research/phase-2/index.md`
- Create: `docs/multi-agent-research/phase-2/<tool-name>/<source-title>.md` (one per source page)
- Modify: `docs/multi-agent-research/index.md`
- Test: `docs/multi-agent-research/phase-2/index.md`

- [ ] **Step 1: Build tool target list file**

```md
# Phase 2 Tool Targets

vitest, playwright, django, sequential-thinking, context7, sentry, github official, gitmcp, fetch, scrapegraph, time, memory, youtube transcripts, Desktop Commander, filesystem, node.js sandbox, redis, markitdown, google maps, ast-grep, npm sentinel, sqlite, hacker news, markdownify, postman, cloud run, stripe, apify, chroma, python refactoring assistant, neo4j memory, api gateway, next.js devtools, python interpreter, gemini api docs, hostinger api, google flights, neon, shadcn, uv, linear, mcp-docker
```

- [ ] **Step 2: Research each tool and save one page per source**

Run: `Use web_fetch for each tool and save each source page into docs/multi-agent-research/phase-2/<tool-name>/ as Markdown`
Expected: one or more Markdown pages per tool.

- [ ] **Step 3: Build phase index**

```md
# Phase 2 Index

For each tool, list:
- tool name
- source links
- extracted file paths
- install/test/verify summary
```

- [ ] **Step 4: Update global index**

Run: `Append Phase 2 artifact counts and links to docs/multi-agent-research/index.md`
Expected: top-level index reflects Phase 2 outputs.

- [ ] **Step 5: Commit**

```bash
git add docs/multi-agent-research/phase-2 docs/multi-agent-research/index.md
git commit -m "docs: add phase 2 MCP/tool research extraction and index"
```

### Task 4: Execute Phase 3 (Hermes Docs and Ecosystem)

**Files:**
- Create: `docs/multi-agent-research/phase-3/index.md`
- Create: `docs/multi-agent-research/phase-3/<topic>/<page>.md`
- Modify: `docs/multi-agent-research/index.md`
- Test: `docs/multi-agent-research/phase-3/index.md`

- [ ] **Step 1: Fetch each required Hermes source**

Run: `Use web_fetch for each Phase 3 URL and save one Markdown file per page`
Expected: all listed pages saved under phase-3 subfolders.

- [ ] **Step 2: Normalize formatting**

Run: `Ensure each page has title, source URL, and clean Markdown body`
Expected: standardized files.

- [ ] **Step 3: Build phase-3 catalog**

```md
# Phase 3 Index

| Topic | Source URL | Local File |
|---|---|---|
```

- [ ] **Step 4: Update main index and plan notes**

Run: `Add phase summary and links to docs/multi-agent-research/index.md`
Expected: main index includes Phase 3.

- [ ] **Step 5: Commit**

```bash
git add docs/multi-agent-research/phase-3 docs/multi-agent-research/index.md
git commit -m "docs: capture phase 3 hermes ecosystem extraction"
```

### Task 5: Execute Phases 4 and 5 (Profiles + Docs Inventory)

**Files:**
- Create: `docs/multi-agent-research/phase-4/summary.md`
- Create: `docs/multi-agent-research/phase-5/summary.md`
- Modify: `docs/multi-agent-research/index.md`
- Test: `docs/multi-agent-research/phase-4/summary.md`

- [ ] **Step 1: Discover and list profiles**

Run: `hermes profile list > docs\multi-agent-research\phase-4\profiles.md`
Expected: profile inventory captured.

- [ ] **Step 2: Capture clone verification checklist**

```md
# Phase 4 Summary

- Verified clone includes config, keys, SOUL.md, memories, skills, sessions.
- Logged install/test/debug/fix outcomes per profile.
```

- [ ] **Step 3: Capture docs inventory execution order**

```md
# Phase 5 Summary

Execution order:
1. plugins
2. hooks
3. skills

Each includes verify/test/debug/fix notes.
```

- [ ] **Step 4: Update top-level index**

Run: `Add links to phase-4 and phase-5 summaries in docs/multi-agent-research/index.md`
Expected: index fully linked.

- [ ] **Step 5: Commit**

```bash
git add docs/multi-agent-research/phase-4 docs/multi-agent-research/phase-5 docs/multi-agent-research/index.md
git commit -m "docs: add phase 4-5 profile and inventory verification outputs"
```

### Task 6: Execute Phase 6 and Final Verification

**Files:**
- Create: `docs/multi-agent-research/phase-6/summary.md`
- Modify: `docs/multi-agent-research/index.md`
- Modify: `.github/prompts/multi-agent-research-template.prompt.md`
- Test: `.github/prompts/multi-agent-research-template.prompt.md`

- [ ] **Step 1: Capture hierarchy and inventory outputs**

Run: `Collect and save lists for hooks, tools, skills, plugins, MCP servers under docs/multi-agent-research/phase-6/`
Expected: inventory artifacts saved.

- [ ] **Step 2: Validate hierarchy order**

Run: `Confirm .hermes.md -> AGENTS.md -> CLAUDE.md -> .cursorrules precedence and record findings`
Expected: summary includes pass/fail per layer.

- [ ] **Step 3: Run verification gate checklist**

```md
# Phase 6 Summary

- Target order verified
- Markdown extraction verified
- Docs index verified
- Plan update before implementation verified
- Verification-before-complete verified
- Native fallback handling verified
```

- [ ] **Step 4: Validate prompt file quality checks**

Run: `Check the checklist at the end of .github/prompts/multi-agent-research-template.prompt.md and mark any gaps in phase-6 summary`
Expected: explicit pass/fail notes.

- [ ] **Step 5: Commit**

```bash
git add docs/multi-agent-research/phase-6 docs/multi-agent-research/index.md .github/prompts/multi-agent-research-template.prompt.md
git commit -m "docs: finalize phase 6 hierarchy audit and verification gates"
```

### Task 7: Final End-to-End Verification

**Files:**
- Modify: `docs/multi-agent-research/index.md`
- Test: `docs/multi-agent-research/index.md`

- [ ] **Step 1: Verify phase directory completeness**

Run: `Get-ChildItem docs\multi-agent-research -Recurse -File`
Expected: all planned phase files exist.

- [ ] **Step 2: Verify all index links resolve**

Run: `Manually open docs/multi-agent-research/index.md and each phase index/summary link`
Expected: no broken links.

- [ ] **Step 3: Verify no incomplete checklist remains**

Run: `rg "\- \[ \]" docs\multi-agent-research -n`
Expected: no unresolved checklist items in finalized summaries.

- [ ] **Step 4: Commit final verification pass**

```bash
git add docs/multi-agent-research/index.md
git commit -m "docs: complete end-to-end verification for multi-agent research run"
```
