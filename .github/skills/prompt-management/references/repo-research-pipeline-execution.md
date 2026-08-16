# Executing the `/repo` Research Pipeline (multi-project, delegated)

Concrete recipe for running a `repo.prompt.md` / `repo-*.prompt.md` research pipeline that
researches N submodule projects under `projects/` and writes one `RESEARCH_REPORT.md`
per project + a master `RESEARCH_INDEX.md`. Derived from a real 16-project run.

## Pre-flight (do this before dispatching)
1. Confirm the target exists: `ls -d projects` and
   `find projects -maxdepth 2 -name RESEARCH_REPORT.md | wc -l` → matches the prompt's expected count.
2. The prompts define the workspace (`$HOME/Desktop/SandBox`); there is no `/repo` path. Read
   `repo.prompt.md` to extract the exact project inventory (name → tech stack → report path) and the
   `## Report Template` (the 9+ `##` section shape) and the Acceptance Criteria (size gate, section count).
3. Respect scope: `repo.prompt.md` says STOP at Phase 4 (verification). Do NOT run `repo-management`
   (branch/CI) or `repo-story-time` (git narrative) unless explicitly asked.

## Dispatch pattern (≤3 concurrent — delegate_task batch cap)
- Split the project list into batches of ≤3 agents (or ≤3 files each if 3 agents × ~5 files).
- Inject FULL context per agent: the project name, exact tech stack (from the inventory table),
  the absolute target report path, the 9-section template, and the prompt's hard rules:
  **NO FABRICATION** (every finding traces to a real web_search/web_extract), **VERIFY links**
  (web_extract 2–3 key URLs, drop 404s), **SIZE GATE 1KB–5KB**, **9+ `##` sections**,
  **symmetric Related Projects** cross-refs. Toolsets: `web`, `file`, `terminal` (real research).
- Agents UPDATE existing reports in place (default action is UPDATE, not CREATE).

## Parent-side verification (subagent self-reports are NOT enough)
After all batches return, independently verify on disk:
```bash
cd "$HOME/Desktop/SandBox/projects"
find . -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l      # expect N
for f in */RESEARCH_REPORT.md; do
  b=$(wc -c <"$f"); s=$(grep -c '^## ' "$f")
  [ "$b" -gt 5120 ] && echo "OVER5K: $f $b"
  [ "$b" -lt 1024 ] && echo "UNDER1K: $f $b"
  [ "$s" -lt 9 ]      && echo "FEWSECS: $f $s"
done
```
- Trim any over-5KB report by removing the trailing `### Methodology` block (subagents often leave
  it; it is outside the template). Re-verify after trimming.

## Rebuild RESEARCH_INDEX.md (Phase 3)
Write a 16-row table: `# | Project | Size (bytes) | Last Updated | Tech Stack`.
**Gotcha — CRLF + blockquote stack extraction:** reports use mixed formats
(`## Project:\n**Tech Stack:** x` OR `> **Tech Stack:** x`). A regex must tolerate the optional `> ` prefix
AND the `:**` (single `**`, not `**...**`). Working pattern:
```python
m = re.search(r"(?:^|>)\s*\*\*(?:Tech Stack|Stack)\b[*:]*\s*(.+)", txt, re.M)
stack = re.sub(r"[*_`]", "", m.group(1)).strip().rstrip(".")[:70]
```
Write the index with `write_file`; run it from a temp script, not a heredoc (Windows CRLF +
shell backtick expansion corrupts inline Python).

## Pitfalls
- Subagents may hit a tool-call limit before final trimming → 2–3 reports land slightly over 5KB.
  The parent must trim + re-verify (don't trust "all within gate" self-reports).
- `search_files(pattern='*.prompt.md')` returns 0 on git-bash even when files exist — use `find`/`ls`.
- The bundled `audit_prompts.py` / `fix_prompts.py` are hardcoded to `SandBox/Prompts` and ignore
  `--workspace`; they are useless here. Use the custom `verify_prompt_library.py` (prompt-library-maintenance).
