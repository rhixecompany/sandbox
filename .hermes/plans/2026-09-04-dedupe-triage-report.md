# SandBox Dedupe Triage Report (Read-Only)

**Generated:** 2026-09-04 | **Branch:** clean-development | **Mode:** NO MUTATIONS
**Scope:** Duplicate config files, duplicate/overlapping root markdown, stale tmp files.
**Method:** `find` + `sha256sum` + `stat` + content sampling. No files modified or committed.

---

## 1. MCP Config Files — Detailed Triage

Five `mcp.json` plus one `.mcp.json` exist (the user-requested paths). After JSON canonicalization, `.codex/mcp.json` and `.copilot/mcp.json` are byte-identical (same 30 servers, same fields); they differ only in whitespace/indent. The others are partial subsets.

| Path | Size (B) | SHA-256 (first 12) | Modified | Servers | Role | Recommendation |
|---|---|---|---|---|---|---|
| `.codex/mcp.json` | 3,880 | `21552a5a7f3d` | 2026-09-04 19:30:24 | 30 | canonical (Codex CLI) | **keep** |
| `.copilot/mcp.json` | 4,701 | `eaf5dcdf5eba` | 2026-08-29 01:33:19 | 30 | **duplicate** of `.codex/mcp.json` (identical JSON, different whitespace; older mtime) | **consolidate** → delete and symlink/hardlink to `.codex/mcp.json` (or vice-versa after picking a format owner) |
| `.github/mcp.json` | 2,790 | `514c6dafa88c` | 2026-09-04 19:10:09 | 21 | legacy/partial subset (used by GitHub Copilot Coding-Agent workflow) | **keep** (Copilot Coding-Agent runtime expects this exact path & subset) |
| `.vscode/mcp.json` | 4,007 | `e645da5e8868` | 2026-09-04 19:10:10 | 0 (inputs-only template) | unique (VS Code `mcp.json` schema with `inputs[]`, no servers) | **keep** |
| `projects/Banking/.cursor/mcp.json` | 372 | `e04e0d283dd8` | 2026-07-31 19:08:45 | 2 (exa, MCP_DOCKER) | project-specific (Banking uses Cursor IDE; exa + docker gate) | **keep** |
| `projects/Python-projects/.mcp.json` | 1,433 | `a0e8eed4edaf` | 2026-08-31 20:28:14 | 8 (python-quality, tooling-lint, tooling-config, ast-grep, fetch, filesystem, sequential-thinking, memory) | project-specific (Python tooling subset) | **keep** |

Notes:
- `.codex/mcp.json` ⇄ `.copilot/mcp.json` are JSON-equivalent: `diff` of canonicalized output is empty. Only indent style and possibly key-ordering differ. The older mtime on `.copilot/mcp.json` (Aug 29 vs Sep 04) shows it has not been refreshed since the `.codex` rewrite — safe to retire as a duplicate.
- `.github/mcp.json` lists 21 of the 30 servers in `.codex/mcp.json` — looks like a deliberate Copilot-Coding-Agent allowlist (no payments/billing servers like `plaid`, `stripe`, `django`, `everart`, `python-quality` is included, etc.). Treat as **legacy/runtime-pinned**, not a duplicate.
- `.vscode/mcp.json` contains an `inputs[]` block but **zero servers** — it's a template/skeleton, not a duplicate.

---

## 2. Root Markdown Files — Detailed Triage

### 2a. SOUL.md / AGENTS.md / CLAUDE.md / copilot-instructions.md

All four are intentionally distinct, layered per `.hermes.md` hierarchy (`SOUL.md` > `AGENTS.md` > `CLAUDE.md` > `.cursorrules`). No true duplicates — different content, different purposes.

| Path | Size (B) | SHA-256 (first 12) | Modified | Role | Recommendation |
|---|---|---|---|---|---|
| `SOUL.md` | 12,335 | `f8bf0a419f8b` | 2026-09-04 19:30:35 | canonical (persona + operating principles; ~255 lines) | **keep** |
| `AGENTS.md` | 16,333 | `8ac5823c9e46` | 2026-09-04 19:30:25 | canonical (general agent guidance, ~highest layer below SOUL) | **keep** |
| `CLAUDE.md` | 314 | `e82773fd7210` | 2026-09-04 19:30:25 | legacy stub (7 lines, only Claude-specific pointers, references AGENTS.md + SOUL.md) | **keep** — not a duplicate; intentionally thin per the hierarchy table in `.hermes.md` |
| `copilot-instructions.md` | 12,328 | `072896ff7498` | 2026-09-04 19:30:25 | canonical (GitHub Copilot Coding-Agent runtime instructions) | **keep** |

Note on the task wording "SOUL.md vs SOUL.md" — there is only one `SOUL.md` in the repo (one match from `search_files`). No self-duplicate.

### 2b. Plan Triad: IMPLEMENTATION_PLAN.md vs PLAN.md vs SPEC.md vs .hermes/plans/comprehensive-implementation-plan.md

| Path | Size (B) | SHA-256 (first 12) | Lines | Modified | Role | Recommendation |
|---|---|---|---|---|---|---|
| `IMPLEMENTATION_PLAN.md` | 19,940 | `cac579494b25` | 337 | 2026-09-04 19:30:26 | canonical (workspace-level "Configuration File Consolidation & Optimization" plan) | **keep** (canonical per task context) |
| `PLAN.md` | 5,035 | `d0d27ff7a12d` | 147 | 2026-09-04 19:30:29 | legacy (YAML-frontmatter MCP-skills install plan: "SandBox-root — Plan: MCP Server Install & Skills Creation") | **consolidate** — superseded by IMPLEMENTATION_PLAN.md; consider merging or symlinking once verification confirms parity |
| `SPEC.md` | 4,928 | `96f0944ceb3e` | 102 | 2026-09-04 19:30:35 | companion spec to PLAN.md (per task context: "PLAN.md and SPEC.md are MCP-skills plan/spec") | **keep** as SPEC companion, or merge with PLAN.md |
| `.hermes/plans/comprehensive-implementation-plan.md` | 10,321 | `36c230ce3e84` | 252 | 2026-09-04 19:26:57 | master plan (YAML frontmatter, "Multi-Phase Delivery Framework", 6-phase) | **keep** (master per task context) |

Content sanity check (different headers):
- `IMPLEMENTATION_PLAN.md` → `# Comprehensive Implementation Plan: Configuration File Consolidation & Optimization`
- `PLAN.md` → frontmatter `name: SandBox-root / title: "SandBox-root — Plan: MCP Server Install & Skills Creation"`
- `SPEC.md` → companion spec (see `.hermes.md` reference)
- `.hermes/plans/comprehensive-implementation-plan.md` → frontmatter `name: comprehensive-implementation-plan / title: "Comprehensive Implementation Plan — Multi-Phase Delivery Framework"`

All four have distinct SHA-256 hashes — none are byte-duplicates. **Overlapping scopes, not duplicates**:
- `IMPLEMENTATION_PLAN.md` (root) is the active workspace consolidation plan.
- `PLAN.md` is the older MCP-skills install plan; its content is largely subsumed by the newer comprehensive plans.
- `.hermes/plans/comprehensive-implementation-plan.md` is the master 6-phase delivery framework.

Recommendation: **keep** `IMPLEMENTATION_PLAN.md` + `.hermes/plans/comprehensive-implementation-plan.md` as the two-canonical pair; **consolidate** `PLAN.md` into one of them and convert to either a symlink or delete after a content-diff review (do not delete in this pass).

### 2c. SESSION_REPORT.md / README.md / CONSOLIDATION_SUMMARY.md / exemplars.md

| Path | Size (B) | SHA-256 (first 12) | Modified | Role | Recommendation |
|---|---|---|---|---|---|
| `SESSION_REPORT.md` | 13,800 | `5039babbeabe` | 2026-09-04 19:30:34 | canonical (last-session summary, 2026-08-31 13-Subgoal Comprehensive Reimplementation) | **keep** |
| `README.md` | 25,122 | `a9dc385aa1bf` | 2026-09-04 19:30:32 | canonical (root repo README) | **keep** |
| `CONSOLIDATION_SUMMARY.md` | 8,292 | `41c49fbf24f7` | 2026-09-04 19:30:25 | legacy (Aug-24 retrospective: "Successfully consolidated and deduplicated configuration files…eliminating 140+ duplicate files") | **keep** as historical artifact, OR mark as legacy. Not a duplicate of any current file. |
| `exemplars.md` | 34,660 | `29f0ae60ac98` | 2026-09-04 19:30:26 | canonical (root exemplars; 17 sibling copies in `projects/*/code-exemplars.md` and `projects/*/docs/Project_Architecture/exemplars.md`) | **keep** root; sibling project copies are project-specific and stay where they are (out of scope here) |

### 2d. uk-earnings-kit/references/*.md (12 files)

All are unique research artifacts (different sha, different scopes). Not duplicates. Listing for completeness:

| Path | Lines | Modified | Recommendation |
|---|---|---|---|
| `ai_training_platforms.md` | 222 | 2026-08-15 23:06:06 | **keep** (unique) |
| `platform_links.md` | 189 | 2026-08-15 23:06:06 | **keep** (unique) |
| `scam_warnings.md` | 198 | 2026-08-15 23:06:06 | **keep** (unique) |
| `tax_guidance_uk.md` | 215 | 2026-09-04 19:30:36 | **keep** (unique) |
| `uk_bank_switching_offers_july_2026.md` | 130 | 2026-09-04 19:30:36 | **keep** (unique) |
| `UK_Cashback_Receipt_Apps_Research.md` | 125 | 2026-08-15 23:06:06 | **keep** (unique) |
| `uk_market_research_panels_2026.md` | 284 | 2026-08-15 23:06:06 | **keep** (unique) |
| `UK_Survey_Platforms_Comparison.md` | 94 | 2026-09-04 19:30:37 | **keep** (unique) |
| `UK_UX_Research_Platforms_2026.md` | 305 | 2026-09-04 19:30:37 | **keep** (unique) |
| `uk-ai-training-platforms-2026.md` | 405 | 2026-08-15 23:06:06 | **keep** (unique — supersedes `ai_training_platforms.md`?) |
| `uk-freelance-gig-platforms-research.md` | 91 | 2026-08-15 23:06:06 | **keep** (unique) |
| `uk-mystery-shopping-comparison.md` | 95 | 2026-08-15 23:06:06 | **keep** (unique) |

Watch: `ai_training_platforms.md` vs `uk-ai-training-platforms-2026.md` — same domain, possibly overlapping content. Different SHA → different content. Manual review recommended; not flagged as duplicate here.

### 2e. skill_judge_results_95.json vs skill_judge_report_95.txt

| Path | Size (B) | SHA-256 (first 12) | Modified | Role | Recommendation |
|---|---|---|---|---|---|
| `skill_judge_results_95.json` | 97,602 | `792f8abffd2c` | 2026-09-04 19:30:35 | canonical (machine-readable JSON; 95% threshold, 752 skills judged) | **keep** |
| `skill_judge_report_95.txt` | 26,305 | `e44e9b04fc32` | 2026-08-20 05:28:45 | legacy (human-readable text dump from same run; 760 lines, header "Total: 752 \| Passed: 752 \| Failed: 0 \| Threshold: 95") | **consolidate** — same run as the JSON; older mtime (Aug 20 vs Sep 04); regenerate from JSON or symlink. NOT a duplicate of content, but a duplicate **of the underlying run**. |

---

## 3. Stale / Tmp Files — Detailed Triage

Two `.hermes-tmp.*` files; both **0 bytes**, both with the canonical empty-file SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (= sha256 of nothing).

| Path | Size (B) | SHA-256 | Modified | Role | Recommendation |
|---|---|---|---|---|---|
| `.hermes-tmp.A0Bzr5` | 0 | `e3b0c44298fc` | 2026-09-04 19:10:10 | stale (0-byte lock/scratch file at repo root; possibly from a crashed `hermes` invocation) | **delete** (low risk — 0 bytes, no content) |
| `judge_results/.hermes-tmp.A3svhR` | 0 | `e3b0c44298fc` | 2026-09-04 19:10:10 | stale (0-byte lock/scratch file in `judge_results/`; same Hermes tmp pattern) | **delete** (low risk — 0 bytes, no content) |

No `*.tmp` files in the root or anywhere outside the Hermes tmp pattern.

---

## Summary Table (Grouped by Category)

### Category A — MCP Config Files

| Path | SHA-256 (full) | Size (B) | Modified | Role | Recommendation |
|---|---|---|---|---|---|
| `.codex/mcp.json` | `21552a5a7f3dbe4125880f2b1ddbc03e643f12c5eb355452ea9db41200b4ae48` | 3,880 | 2026-09-04 19:30:24 | canonical | keep |
| `.copilot/mcp.json` | `eaf5dcdf5ebab1ccdb773e6c3b7ce4c4fc9136a59e498acc34ecd7fe1561d3bc` | 4,701 | 2026-08-29 01:33:19 | duplicate (JSON-equivalent to `.codex/mcp.json`) | consolidate (delete + symlink to `.codex/mcp.json`) |
| `.github/mcp.json` | `514c6dafa88c653872ba8743bfde4fac1ce3c66b62a7253e455db55d2886b7d5` | 2,790 | 2026-09-04 19:10:09 | legacy/runtime-pinned (Copilot Coding-Agent subset) | keep |
| `.vscode/mcp.json` | `e645da5e88689cc6f2b7180f4350e2eb2d7f0660c18335bc06c9805e6f1ef0d5` | 4,007 | 2026-09-04 19:10:10 | unique (inputs-only template) | keep |
| `projects/Banking/.cursor/mcp.json` | `e04e0d283dd8dd96ff50282a199e62b305de344be09a90157cb4b0d95698b09e` | 372 | 2026-07-31 19:08:45 | unique (project-specific: Cursor + exa + docker) | keep |
| `projects/Python-projects/.mcp.json` | `a0e8eed4edafb8d14c0e53e06007fb88d564b4a50e51d66ee5e3b36c67577ef8` | 1,433 | 2026-08-31 20:28:14 | unique (project-specific: Python tooling subset) | keep |

### Category B — Root Markdown Files

| Path | SHA-256 (full) | Size (B) | Modified | Role | Recommendation |
|---|---|---|---|---|---|
| `SOUL.md` | `f8bf0a419f8bb8ea6a7dbd2a5574a76b394fe1dce869940537f3734b79109203` | 12,335 | 2026-09-04 19:30:35 | canonical (persona) | keep |
| `AGENTS.md` | `8ac5823c9e4602b8e1fb1f8ed8f5775525f503cbe4b2b26f296d9bdd425990de` | 16,333 | 2026-09-04 19:30:25 | canonical (workspace guidance) | keep |
| `CLAUDE.md` | `e82773fd7210afe34e417134004ea12dfc444481b47614029b6d94cf633d6a73` | 314 | 2026-09-04 19:30:25 | unique (7-line Claude-only stub; ref-only) | keep |
| `copilot-instructions.md` | `072896ff749883d01db1aef4c2783af52879e3ff7fdf2677494d3d715d2cc690` | 12,328 | 2026-09-04 19:30:25 | canonical (Copilot Coding-Agent runtime) | keep |
| `IMPLEMENTATION_PLAN.md` | `cac579494b25bb3bd0d175a87fda96c8ccd0dd5cb9292985fcb0bcbd15eb23bb` | 19,940 | 2026-09-04 19:30:26 | canonical (consolidation plan) | keep |
| `PLAN.md` | `d0d27ff7a12d61bc768cafb3eb78b18e2596585b4435b4327e841dddce2ccb8d` | 5,035 | 2026-09-04 19:30:29 | legacy (MCP-skills install plan, largely superseded) | consolidate |
| `SPEC.md` | `96f0944ceb3e5ec9357bff401e4766514dbc60626e2f507443ccd3c8c2273e23` | 4,928 | 2026-09-04 19:30:35 | unique (companion spec to PLAN.md) | keep (paired with PLAN.md) |
| `.hermes/plans/comprehensive-implementation-plan.md` | `36c230ce3e84e26922665debfd66bed1702ade5101ba8006fc41ca70202e6e0c` | 10,321 | 2026-09-04 19:26:57 | canonical (master 6-phase delivery framework) | keep |
| `SESSION_REPORT.md` | `5039babbeabe21d6fce202ed6055f971e4e5927fcc02dbd0ca92ed6a7e0a5469` | 13,800 | 2026-09-04 19:30:34 | canonical | keep |
| `README.md` | `a9dc385aa1bf569d2f9d33156bc0be336b53b3f40c6919addcb9a8666f0f944f` | 25,122 | 2026-09-04 19:30:32 | canonical | keep |
| `CONSOLIDATION_SUMMARY.md` | `41c49fbf24f777d574ed2b55807251e746df0fd9fce3af308a0b121c49526488` | 8,292 | 2026-09-04 19:30:25 | legacy (Aug-24 retrospective) | keep (historical artifact) |
| `exemplars.md` | `29f0ae60ac98342cef9b10f57c1f65f24ebe96c1599e3e6d18356673123b5b54` | 34,660 | 2026-09-04 19:30:26 | canonical (root) | keep |

### Category C — uk-earnings-kit/references (12 unique files, all keep)

| Path | SHA-256 (full) | Size (B) | Modified | Role | Recommendation |
|---|---|---|---|---|---|
| `uk-earnings-kit/references/ai_training_platforms.md` | *(see file)* | 222 lines | 2026-08-15 23:06:06 | unique | keep |
| `uk-earnings-kit/references/platform_links.md` | *(see file)* | 189 lines | 2026-08-15 23:06:06 | unique | keep |
| `uk-earnings-kit/references/scam_warnings.md` | *(see file)* | 198 lines | 2026-08-15 23:06:06 | unique | keep |
| `uk-earnings-kit/references/tax_guidance_uk.md` | *(see file)* | 215 lines | 2026-09-04 19:30:36 | unique | keep |
| `uk-earnings-kit/references/uk_bank_switching_offers_july_2026.md` | *(see file)* | 130 lines | 2026-09-04 19:30:36 | unique | keep |
| `uk-earnings-kit/references/UK_Cashback_Receipt_Apps_Research.md` | *(see file)* | 125 lines | 2026-08-15 23:06:06 | unique | keep |
| `uk-earnings-kit/references/uk_market_research_panels_2026.md` | *(see file)* | 284 lines | 2026-08-15 23:06:06 | unique | keep |
| `uk-earnings-kit/references/UK_Survey_Platforms_Comparison.md` | *(see file)* | 94 lines | 2026-09-04 19:30:37 | unique | keep |
| `uk-earnings-kit/references/UK_UX_Research_Platforms_2026.md` | *(see file)* | 305 lines | 2026-09-04 19:30:37 | unique | keep |
| `uk-earnings-kit/references/uk-ai-training-platforms-2026.md` | *(see file)* | 405 lines | 2026-08-15 23:06:06 | unique (possibly supersedes `ai_training_platforms.md`) | keep; manual review |
| `uk-earnings-kit/references/uk-freelance-gig-platforms-research.md` | *(see file)* | 91 lines | 2026-08-15 23:06:06 | unique | keep |
| `uk-earnings-kit/references/uk-mystery-shopping-comparison.md` | *(see file)* | 95 lines | 2026-08-15 23:06:06 | unique | keep |

### Category D — Skill Judge Pair

| Path | SHA-256 (full) | Size (B) | Modified | Role | Recommendation |
|---|---|---|---|---|---|
| `skill_judge_results_95.json` | `792f8abffd2c9cbb049d2b06325ef841077596ea6f8cdbb051ff46122553d582` | 97,602 | 2026-09-04 19:30:35 | canonical (machine-readable JSON, 752 skills @ 95% threshold) | keep |
| `skill_judge_report_95.txt` | `e44e9b04fc322dcefeb8b7ea3d6dcded690c9df8e7c36b7b4f4531ba45fb141b` | 26,305 | 2026-08-20 05:28:45 | legacy (human-readable dump, same run, older mtime) | consolidate (regenerate from JSON or symlink) |

### Category E — Stale Tmp Files

| Path | SHA-256 (full) | Size (B) | Modified | Role | Recommendation |
|---|---|---|---|---|---|
| `.hermes-tmp.A0Bzr5` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 | 2026-09-04 19:10:10 | stale (0-byte Hermes scratch, repo root) | delete |
| `judge_results/.hermes-tmp.A3svhR` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 | 2026-09-04 19:10:10 | stale (0-byte Hermes scratch, judge_results/) | delete |

---

## Key Findings

1. **One true duplicate confirmed (Category A):** `.codex/mcp.json` ⇄ `.copilot/mcp.json` are JSON-equivalent (same 30 servers, same fields). The only difference is whitespace/indent. `.copilot/mcp.json` is older (Aug 29) and stale.
2. **One legacy/duplicate-of-run pair (Category D):** `skill_judge_results_95.json` and `skill_judge_report_95.txt` come from the same underlying 752-skill judge run; the `.txt` is older (Aug 20) and redundant.
3. **Two stale 0-byte scratch files (Category E):** both `.hermes-tmp.*` files share the canonical empty-file hash and are safe to delete.
4. **No false duplicates in the plan triad (Category B):** `IMPLEMENTATION_PLAN.md`, `PLAN.md`, `SPEC.md`, `.hermes/plans/comprehensive-implementation-plan.md` are all distinct content with distinct SHAs — overlapping scopes, not duplicates.
5. **No self-duplicates:** `SOUL.md` vs `SOUL.md` resolves to a single file in the tree.
6. **All 12 `uk-earnings-kit/references/*.md` are unique** (different content, no overlap detected at the file-name pair level — one possible superset relationship between `ai_training_platforms.md` and `uk-ai-training-platforms-2026.md` flagged for manual review).

## Action Plan (Do NOT execute in this pass — user wants report only)

| Action | Target | Risk | Notes |
|---|---|---|---|
| delete | `.hermes-tmp.A0Bzr5` | none | 0 bytes |
| delete | `judge_results/.hermes-tmp.A3svhR` | none | 0 bytes |
| consolidate (symlink `.copilot/mcp.json` → `.codex/mcp.json`) | `.copilot/mcp.json` | low | After confirming no agent reads `.copilot/mcp.json` with whitespace-sensitive tooling |
| consolidate (regenerate from JSON or symlink) | `skill_judge_report_95.txt` | low | Same source run; the JSON is canonical |
| consolidate (merge into IMPLEMENTATION_PLAN.md or master plan) | `PLAN.md` | low | Largely superseded by newer plans |
| keep | all other files in this report | n/a | Canonical, unique, or runtime-pinned |

## Report-Only Confirmation

No files were deleted. No commits were made. The only file written during this audit is this report itself: `.hermes/plans/2026-09-04-dedupe-triage-report.md`.