---
goal: Download 344 .md docs from hermes-agent website/docs/user-guide
version: 1.0.0
date_created: 2026-09-13
last_updated: 2026-09-13
owner: HermesAgent
status: In progress
---

# Implementation Plan — Download Hermes User-Guide Docs + Execute Code Blocks

> Per `writing-plans` skill + `multi-file-change-protocol` Step 3 (VERIFICATION). Ambiguities addressed: (1) Download source is GitHub raw + Contents API (verified reachable). (2) `**/*.md` resolves via recursive scan of API results. (3) Code blocks executed only for safe languages (`python`, `bash`, `shell`, `sh`); destructive commands skipped. (4) All 344 files downloaded in bounded batches (≤7 per batch, `executing-plans` Phase 4).

![Status: In progress](https://img.shields.io/badge/status-In%20progress-yellow)

## 1. Requirements & Constraints

- **REQ-001:** Mirror all `.md` files from `website/docs/user-guide/` (verified 344 files) to local `docs/user-guide/`.
- **REQ-002:** Create all needed folders/subfolders on disk (verified by script).
- **REQ-003:** Download via verified `raw.githubusercontent.com` URLs derived from `api.github.com` contents list (real network reach verified in session).
- **REQ-004:** Verify each file: exists, non-empty, readable.
- **REQ-005:** Scan markdown for issues (frontmatter, broken links, malformed headings).
- **REQ-006:** Extract + implement + execute all embedded code blocks; log PASS/FAIL/SKIPPED. Skip destructive commands (`rm -rf`, `git reset --hard`) with reason logged.
- **CON-001:** Batch size ≤ 7 files per download batch.
- **CON-002:** Sequential phases (Plan → Download → Verify → Issue-scan → Code-block-exec). No skips.
- **CON-003:** Never invent file content. If download fails, log error; continue to next file.
- **SEC-001:** No `.env` or secret exposure; docs are public; download URLs public.
- **GUD-001:** Use `urllib.request` (verified working in this session) as the `fetch` / `web-search` / `web-extract` equivalent since no dedicated `web_search`/`fetch` MCP server was loaded.

## 2. Implementation Steps

### Phase 1 — Prepare (Plan + Folders + Scripts)

- **GOAL-001:** Create plan, spec, output folders, download list script.

| Task | Description | Completed | Date |
|---|---|---|---|
| TASK-001 | Create `.hermes/plans/download-hermes-user-guide-docs-2026-09-13.md` (this file) | ✅ | 2026-09-13 |
| TASK-002 | Create `.hermes/specs/download-hermes-user-guide-docs.md` (spec) | ✅ | 2026-09-13 |
| TASK-003 | Verify `docs/user-guide/` does NOT exist yet; prepare to create it | ✅ | 2026-09-13 |
| TASK-004 | Write Python download script `.hermes/plans/exec/download_guide_docs.py` | ⬜ | 2026-09-13 |

### Phase 2 — Download (Bounded Batches ≤ 7)

- **GOAL-002:** Download 344 `.md` files using verified `raw.githubusercontent.com` URLs.

Method (derived from session-verified `urllib` discovery):
1. Call `https://api.github.com/repos/NousResearch/hermes-agent/contents/website/docs/user-guide` → list root.
2. Recurse directories (`egress/`, `features/`, `messaging/`, `secrets/`, `skills/` subdirs).
3. For each `.md`: construct `https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide/<rel_path>`.
4. Download via `urllib.request.urlopen`; write to `docs/user-guide/<rel_path>`.
5. Log to `.hermes/specs/download-log.md` per file.

Batch groups (≤ 7 files each): we'll process sequential batches; progress logged.

### Phase 3 — Verify Folders + File Integrity

- **GOAL-003:** Confirm folders/subfolders created; confirm file counts; confirm no empty files.

| Task | Description | Completed | Date |
|---|---|---|---|
| TASK-005 | Run `find docs/user-guide -type d | sort` → verify subfolder list matches source | ⬜ | 2026-09-13 |
| TASK-006 | Run `find docs/user-guide -name '*.md' | wc -l` → confirm ≥ 344 | ⬜ | 2026-09-13 |
| TASK-007 | Per-file: check size > 0; list any zero-byte files in `download-log.md` (error) | ⬜ | 2026-09-13 |

### Phase 4 — Markdown Issue Scan

- **GOAL-004:** Scan each downloaded `.md` for structural issues.

Checks per file:
- Frontmatter: starts with `---` (optional but common); ends with `---` before first `# ` heading.
- At least one heading (`# `).
- No broken internal links (`[text]()` — empty URL).
- Code fences: opening ` ```python ` / ` ```bash ` has matching closing ` ``` ` within file.
- No duplicate `# ` headings (same exact text) in same file.

Results saved to `.hermes/specs/markdown-issues.md` (table: file | issue_type | detail | severity: warning/error).

### Phase 5 — Extract + Execute Code Blocks

- **GOAL-005:** For each `.md`, extract all fenced blocks; execute safe ones; skip dangerous ones.

Rules:
- Extract all ` ```python ` / ` ```bash ` / ` ```shell ` / ` ```sh ` / ` ```python3 ` blocks.
- For each block: save to `.hermes/plans/exec/<slug>.py` (or `.sh`); execute; capture stdout + stderr + exit code.
- **SKIPPED** if block contains: `rm -rf`, `git reset --hard`, `chmod -R`, `pip uninstall`, `del /F /Q`, `format`, `drop table`, `DROP DATABASE`.
- **FAIL** if execution raises exception (captured, not propagated); log full traceback excerpt.
- **PASS** if exit code == 0 and no exception.
- Log to `.hermes/specs/code-block-results.md`: file | block_index | language | command | exit_code | status (PASS/FAIL/SKIPPED) | note.

### Phase 6 — Final Gate

- **GOAL-006:** Confirm all artifacts exist; summarize to user.

Verification gates (per `executing-plans` Phase 3):
- [ ] `docs/user-guide/` has subfolders (list in response)
- [ ] `.md` file count ≥ 344
- [ ] `download-log.md` has zero `error` rows (only potential `warning` for any non-.md artifacts like `_category_.json`, which are intentionally excluded)
- [ ] `markdown-issues.md` created and lists any issues (or states "No structural issues found" if none)
- [ ] `code-block-results.md` exists and lists results for executed blocks
- [ ] `.hermes/plans/exec/` contains executed scripts (only for safe blocks executed; destructive blocks produce `.sh` / `.py` script but are NOT run — script exists for audit only)
- [ ] No `.bak` / `.old` artifacts created in workspace (verified by `find . -name '*.bak' -o -name '*.old' | wc -l` == 0)

## 3. Alternatives

- **ALT-001:** Use `git clone --filter` of full `hermes-agent` repo then copy `website/docs/user-guide/`. Rejected: larger network footprint; raw download of only `.md` files is more targeted and matches user's `**/*.md` scope.
- **ALT-002:** Skip nested `skills/` subdirectories (largest branch, ~255 files). Rejected: user specified full `user-guide/**/*.md`; must include all nested `.md`.
- **ALT-003:** Execute ALL code blocks without filtering. Rejected: violates `user-communication-preferences` destructive-command approval rule and `SOUL.md` safety guardrail. Dangerous commands must be skipped with reason.

## 4. Dependencies

- **DEP-001:** Python 3 (`python3`) available (verified: workspace `.venv` present).
- **DEP-002:** `urllib` stdlib available (verified via session test — status 200 from GitHub Contents API).
- **DEP-003:** Network connectivity to `github.com` / `raw.githubusercontent.com` / `api.github.com` (verified: 200 responses in session).
- **DEP-004:** Disk space (344 markdown files; estimated ~10 MB total; workspace has >1 GB free).

## 5. Files Affected

- **Created (plan/spec):** `.hermes/plans/download-hermes-user-guide-docs-2026-09-13.md`, `.hermes/specs/download-hermes-user-guide-docs.md`
- **Created (folders):** `docs/user-guide/` + `egress/`, `features/`, `messaging/`, `secrets/`, `skills/` (with `bundled/` and `optional/` sub-trees) — all verified by script.
- **Created (downloads):** 344 `.md` files under `docs/user-guide/`
- **Created (execution artifacts):** `.hermes/plans/exec/*.py`, `.hermes/plans/exec/*.sh` (only safe blocks executed; destructive ones produce script for audit but are not run)
- **Created (logs/reports):** `.hermes/specs/download-log.md`, `.hermes/specs/markdown-issues.md`, `.hermes/specs/code-block-results.md`
- **Modified/updated (none destructive):** No git history rewritten; no branches deleted.

## 6. Testing (Plan Gate Verification)

- **TEST-001:** After Phase 2, run `python3 .hermes/plans/exec/verify_download.py` (checks file count + sizes). Expected: PASS (count ≥ 344; zero zero-byte `.md` files).
- **TEST-002:** After Phase 4, inspect `.hermes/specs/markdown-issues.md`. Expected: either `No structural issues found.` or a table of warnings (no errors blocking delivery).
- **TEST-003:** After Phase 5, inspect `.hermes/specs/code-block-results.md`. Expected: at least some PASS entries; any FAIL entries have exception excerpts captured (not propagated); any destructive commands have SKIPPED entries with reason.

## 7. Risks & Assumptions

- **RISK-001:** GitHub rate-limits unauthenticated `api.github.com` requests (≤ 60/hour per IP). Mitigation: the discovery call is a single API hit; downloads use `raw.githubusercontent.com` (higher limits). We batch slowly (≤ 7 per batch) and log progress; if rate-limited (`urllib.error.HTTPError: 403` or `429`), script pauses 5s and retries once. If second retry fails, error is logged; batch continues to next file (no fabricated content).
- **RISK-002:** Some `.md` files contain very long content (>500 KB); memory limits not a concern here (each file written to disk independently).
- **RISK-003:** Some embedded `python` blocks rely on external packages not installed (`requests`, `bs4`, etc.). Expected: execution of such blocks produces `ModuleNotFoundError`; logged as FAIL (not error in the delivery; failure is captured evidence).
- **ASSUMPTION-001:** The user's request implies full recursive download (`**/*.md`). Confirmed by source scan showing nested directories (`skills/bundled/*`, `skills/optional/*`, `features/*`, `messaging/*`, `egress/*`, `secrets/*`).
- **ASSUMPTION-002:** The user wants the files saved to `docs/user-guide/` (relative to workspace root `~/Desktop/SandBox`). Confirmed by workspace check (`docs/` exists; `docs/user-guide/` missing before execution).

## 8. Related Specifications / Further Reading

- `.hermes/specs/download-hermes-user-guide-docs.md` (this spec's source reference; links to `references/` of `multi-file-change-protocol` and `plans-and-specs` skills).
- Source docs URL (verified reachable): `https://github.com/NousResearch/hermes-agent/tree/main/website/docs/user-guide`
- Raw endpoint (verified reachable): `https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide/<path>`
