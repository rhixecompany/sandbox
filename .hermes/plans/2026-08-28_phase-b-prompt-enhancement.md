---
title: "Phase B - Prompt Body Enhancement"
description: "Enhance all 226 prompt files: fix broken fences, clarify body content, apply DRY, validate repo-init"
date: 2026-08-28
author: Hermes Agent
status: completed
---

# Phase B - Prompt Body Enhancement

## Goal

Fix structural content issues, enhance body clarity/DRYness, and fully validate the repo-init prompt as a /subgoal target. All 226 files must pass the Phase A auditor unchanged (zero new HIGH issues) after Phase B.

## Audit Findings (Phase B scope)

### Pre-existing structural issues (debug/fix)
| File | Issue | Action |
|------|-------|--------|
| `all-repo-docker-setup.prompt.md` | Broken triple fences (` ``` ` then ` ```bash `), no structure | Rewrite with proper sections |
| `java-mcp-server-generator.prompt.md` | Broken triple fence | Fix fences |
| `ruby-mcp-server-generator.prompt.md` | Broken triple fence | Fix fences |
| `smithery-setup.prompt.md` | Broken triple fence | Fix fences |
| `swift-mcp-server-generator.prompt.md` | Broken triple fence | Fix fences |

### Body content quality issues
- 221 of 226 files have a heavy TOC + section-header boilerplate with thin real content
- Most files follow a template structure (`- [Goal]`, `- [Inputs]`, `- [Outputs]`, `## Steps`, `## Rules`, `## Verification`) but the body prose is often generic
- Phase B will enhance: clarity, active voice, concrete language, missing context (prerequisites, pitfalls)

## Phases

### Phase B-1: Fix broken fences (5 files) — direct patch
Targeted fixes to the 5 files with broken triple-fence patterns. Use `patch` for surgical fixes.

### Phase B-2: Enhance repo-init.prompt.md — /subgoal target
The repo-init prompt is structurally sound (118 lines, 61 real-content lines) but can be enhanced:
- Add concrete prerequisites / environment requirements
- Clarify the canonical precedence rules with examples
- Add pitfalls section for cross-system dedup edge cases
- Strengthen verification criteria

### Phase B-3: Batch enhance 226 files via subagents
Dispatch subagents in batches of ~25 to enhance body content:
1. Strip AI-puffery, vague quantifiers, promotional adjectives
2. Active voice, concrete language
3. Add missing context (prerequisites, pitfalls)
4. Ensure sections are populated with real content, not placeholders
5. Keep TOC accurate post-editing

Batch strategy: 10 batches × ~23 files each. Each subagent gets `['file']` toolsets.

### Phase B-4: Verify
- Run `scripts/verify_prompt_corpus.py` — must PASS (exit 0)
- Manual spot-check of 5 random enhanced files
- Verify no broken fences introduced

## Subgoal: repo-init fully implemented
The `repo-init.prompt.txt` source does not exist (already converted to `.md` in Phase A). The `.md` is valid and complete. Phase B will enhance it per above.

## Out of scope
- Changing file names or extensions
- Adding new prompts
- Modifying frontmatter (Phase A already normalized)
