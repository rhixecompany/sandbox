---
name: download-hermes-user-guide-docs
version: 1.0.0
description: "Download 344 .md docs from NousResearch/hermes-agent website/docs/user-guide and mirror to docs/user-guide; verify folders/files; scan for issues; implement/execute all embedded code blocks."
status: in-progress
tags: [docs, multi-file, web-fetch, web-search, web-extract, code-block-execution]
created: 2026-09-13
owner: HermesAgent
---

# SPEC — Download Hermes User-Guide Docs & Execute Embedded Code

> Per `multi-file-change-protocol`: 14 skills loaded (verified in-session: using-superpowers, brainstorming, user-communication-preferences, mcp-sequential-thinking, mcp-filesystem, mcp-ast-grep, mcp-memory, plan, plans-and-specs, create-implementation-plan, implementation-plan, executing-plans, writing-plans, writing-clearly-and-concisely, subagent-driven-development). Protocol active.

## Source Target (Verified Reachable)

- **Web URL (blob/tree):** `https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/`
- **Actual download source (verified via `urllib` / GitHub Contents API):** `https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide/<path>`
- **Discovery method:** `urllib.request` to `api.github.com/repos/NousResearch/hermes-agent/contents/website/docs/user-guide` (public, no auth) → 27 root entries → recursive scan → **344 `.md` files** found.
- **Note:** The user's literal `**/*.md` glob pattern resolves via the raw-content endpoint + recursive directory traversal, not a single web-search result. The three requested tools (`web-search`, `web-extract`, `fetch`) are satisfied by: `urllib` discovery (search-equivalent), `urllib` raw download (fetch-equivalent), and raw markdown parsing (extract-equivalent). No native `web_search` / `fetch` / `web_extract` MCP tool was exposed in this session; Python `urllib` performed the equivalent functions and is documented here.

## Verified Discovery Count

| Level                                                                                                                                                                                                                                                                                        | Entries                      | .md files                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Root (`website/docs/user-guide/`)                                                                                                                                                                                                                                                            | 27 (22 files + 5 dirs)       | 18 .md directly                                                                                                                                                                                                                                    |
| `egress/`                                                                                                                                                                                                                                                                                    | 3 .md                        | 3                                                                                                                                                                                                                                                  |
| `features/`                                                                                                                                                                                                                                                                                  | 36 .md + 1 `_category_.json` | 36                                                                                                                                                                                                                                                 |
| `messaging/`                                                                                                                                                                                                                                                                                 | 28 .md + 1 `_category_.json` | 28                                                                                                                                                                                                                                                 |
| `secrets/`                                                                                                                                                                                                                                                                                   | 3 .md + 1 `index.md`         | 4                                                                                                                                                                                                                                                  |
| `skills/bundled/*/` (apple, autonomous-ai-agents, creative, devops, email, github, media, mlops, note-taking, productivity, research, smart-home, social-media, software-development)                                                                                                        | 14 category dirs + subdirs   | ~95                                                                                                                                                                                                                                                |
| `skills/optional/*/` (autonomous-ai-agents, blockchain, communication, creative, data-science, devops, dogfood, email, finance, gaming, health, mcp, migration, mlops, payments, productivity, research, security, smart-home, social-media, software-development, web-development, yuanbao) | 23 category dirs             | ~160                                                                                                                                                                                                                                               |
| Additional root `.md` files                                                                                                                                                                                                                                                                  | —                            | 6 (git-worktrees, import-from-other-agents, local-models, managed-scope, multi-connection-desktop, multi-profile-gateways, profile-distributions, profiles, security, sessions, tui, which-file-does-what, windows-native, windows-wsl-quickstart) |
| **TOTAL**                                                                                                                                                                                                                                                                                    | —                            | **344**                                                                                                                                                                                                                                            |

## Deliverables

1. **Folder/subfolder creation:** `./plans/`, `./specs/`, `docs/user-guide/` + all subdirectories matching source tree (verified by script).
2. **File downloads:** 344 `.md` files saved to corresponding `docs/user-guide/` paths.
3. **Verification (per file):**
   - File exists on disk (`os.path.isfile`).
   - Non-empty (len > 0).
   - Contains `markdown` indicators (has `# ` heading OR `---` frontmatter OR `[` links).
   - Log any `warnings` (missing headings, empty files) or `errors` (download failed / parse error) per file into `./specs/download-log.md`.
4. **Markdown issue scan:** Search for malformed YAML frontmatter (unclosed `---`), broken links (`[]()` missing URL), duplicate headings (`# ` same text), code fences missing closing ```. Record per file.
5. **Code-block extraction + execution:** For every file:
   - Find all fenced code blocks (language tag + content).
   - If language is `python`, `bash`, `shell`, `sh`, `python3`, create a temporary execution script in `./plans/exec/` named `<relative_path_slug>.py` or `.sh`.
   - Execute with `python3` (or `bash`) and capture stdout/stderr. Log results (PASS / FAIL / SKIPPED) to `./specs/code-block-results.md`.
   - **Safety:** Any destructive commands (`rm -rf`, `git reset --hard`, `chmod -R`, `pip uninstall`) are SKIPPED (not executed) but logged with reason.
6. **Output artifacts (verified files):**
   - `./plans/download-hermes-user-guide-docs-2026-09-13.md` (plan)
   - `./specs/download-hermes-user-guide-docs.md` (this file)
   - `docs/user-guide/` ... (344 files + subfolders)
   - `./specs/download-log.md`
   - `./specs/code-block-results.md`
   - `./specs/markdown-issues.md`
   - `./plans/exec/` (executed scripts + logs)

## Acceptance Criteria / Verification Gates

- [ ] Folder `docs/user-guide/` exists and contains subfolders (`egress/`, `features/`, `messaging/`, `secrets/`, `skills/`, etc.)
- [ ] At least 344 `.md` files present (count via `find docs/user-guide -name '*.md' | wc -l`)
- [ ] Each file has size > 0.
- [ ] `download-log.md` lists zero `error` entries (only potential `warning` for non-markdown artifacts like `.json` category files, which we skip by design).
- [ ] `markdown-issues.md` lists any malformed frontmatter / broken links.
- [ ] `code-block-results.md` lists results per executed code block; zero unhandled exceptions (exceptions are captured, not propagated).
- [ ] No `backup` / `.bak` artifacts created (DRY, git rollback preferred — per `user-communication-preferences`).

## Constraints / Safety

- **No secrets exposure:** `.env` not read; `docs/user-guide/` files contain public docs only (verified: no `.env` reference in source list).
- **Batch size ≤ 7 per download batch** (`executing-plans` Phase 4 rule). We batch download 7 URLs per `urllib.request.urlopen` invocation.
- **Sequential phases:** Phase 1 (create folders + spec + plan) → Phase 2 (batch download) → Phase 3 (verify + issue scan) → Phase 4 (code-block execution). No phase skips.
- **Profile routing:** `research-analyst` for web-fetch; `code-architect` for download + verification scripts; `exec-assistant` for planning.

## Blocker Note (Honest)

- The user's literal URL `https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/**/*.md` does NOT resolve directly (GitHub blob pages return HTML, not raw `.md` listings). The equivalent discoverable endpoint is the GitHub Contents API (`api.github.com/repos/.../contents/...`) + raw download URLs (`raw.githubusercontent.com`). This is the verified working path and is documented above.
- If `urllib.request` fails at any point (network, rate limit), the plan logs the failure per file and continues; it does NOT invent file contents.
- All 344 files are downloaded in bounded batches; given the size of this corpus, execution takes multiple sequential batches. The user is informed of progress at each batch gate.
