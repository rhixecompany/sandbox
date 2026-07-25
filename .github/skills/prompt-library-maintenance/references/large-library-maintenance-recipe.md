# Large-Library Prompt Maintenance Recipe

Condensed, reusable recipe for batch-maintaining a prompt directory of 100+ `.prompt.md`
files (e.g. `~/AppData/Local/hermes/prompts/`). Derived from a 211-file maintenance pass.

## The 5-phase loop

1. **Recon (terminal, not search_files).** Count files with `find "$LOCALAPPDATA/hermes/prompts" -name '*.prompt.md' | wc -l`.
   > GOTCHA: `search_files` glob `*.prompt.md` on Windows git-bash can return 0 even when
   > hundreds of files exist. Always confirm counts with `find`/`ls` in the terminal first.
2. **Audit (no writes).** Run a script in audit mode that parses only the frontmatter with
   `yaml.safe_load`, edits the dict, and reports proposed changes. Never trust a cached
   `read_file` for counts — re-read from disk.
3. **Apply.** Rewrite frontmatter from the edited dict with `yaml.dump(sort_keys=False)`;
   preserve the body (everything after the FIRST closing `---`) byte-for-byte.
4. **Independent verify.** Run a SECOND script with a different code path that re-checks the
   schema, DEPS==SKILLS, skill resolution on disk, toolset validity, name/trigger consistency.
   Do NOT trust the fixer's own "0 issues" self-report — a separate verifier catches
   regressions the fixer introduced (e.g. collapsed metadata).
5. **Deep validation via subagents.** Dispatch ≤3 parallel leaf `delegate_task` agents (toolsets
   `file`+`terminal`, READ ONLY) for: (a) skill-resolution + MCP-reference audit, (b) content-structure
   + safety review, (c) cross-prompt delegation map + registry. Give each the absolute paths, the
   exact known-good MCP set, and the output report path inline — subagents know nothing.

## Corruption class 1 — Duplicate frontmatter blocks

**Symptom:** file has two `---` fences; the second block's YAML bleeds into the body as
malformed text before the first real `# Heading`. `yaml.safe_load` on the first block
succeeds, so a naive "rewrite from dict" pass can DROP the second block's content into the
body, leaving a partial duplicate.

**Fix:** rewrite the whole file with `write_file` — ONE clean frontmatter (merge the two
blocks, keep the first's values) + the real body from after the last `---`. Then re-verify
with the independent checker (it flags `DUPLICATE_METADATA` via `len(re.findall(r"^metadata:", raw)) > 1`).

## Corruption class 2 — MCP server mislabeled as a skill

**Symptom:** `dependencies:` has `skill:mcp-fetch` and `skills:` lists `mcp-fetch`; or a
prompt references itself via `skill:<self>`.

**Fix:**
- `skill:mcp-<name>` → `tool:mcp-<name>` (MCP servers are TOOLS, not Hermes skills).
- Remove `mcp-*` entries from `skills:` entirely.
- Remove any `skill:<self>` self-reference.
- If `tool:mcp-*` deps remain, ensure `- mcp` is in `toolsets:`.
- Sync `metadata.hermes.related_skills` to match (prefix MCP with `tool:`).

## DEPS==SKILLS must be bidirectional

`dependencies:` (`skill:` entries) and `skills:` must contain the SAME set. When fixing,
make it bidirectional: every `skill:` dep must appear in `skills:`, AND every `skills:` entry
must appear as a `skill:` dep. A one-directional sync leaves either `SKILL_LIST_ONLY` or
`SKILL_DEP_ONLY` dangling refs that the verifier flags.

## Known-good MCP server set (validate `tool:mcp-*` against this)

ast-grep, code-sandbox, codex, copilot-mcp, fetch, filesystem, github, linear, mcp-docker,
memory, mindstudio, playwright, sequential-thinking, smithery.

Any `tool:` entry naming a Hermes toolset (terminal, file, web, browser, …) instead of an MCP
server is mislabeled — those are `toolsets:`, not `tool:` deps.
