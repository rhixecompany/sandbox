# Prompt Library Repair Technique (deterministic, body-preserving)

## Why this exists
The bundled maintenance scripts in `~/AppData/Local/hermes/scripts/` are unreliable for the live
`~/AppData/Local/hermes/prompts/` library:
- `audit_prompts.py` / `fix_prompts.py` are HARDCODED to `C:/Users/Alexa/Desktop/SandBox/Prompts/`
  and `.github/prompts/`, and ignore `--workspace`. They scan 0 files against the real library.
- `boost_prompt.py` (the `boost-prompts` Stage 4 enhance step) is often ABSENT from disk.
- `validate_prompts.py` works but only checks frontmatter schema, not DEPS==SKILLS or toolset validity.

So maintain the library with a deterministic inline Python pass, not the bundled scripts.

## Body-preserving frontmatter rewrite (core pattern)
Parse ONLY the YAML frontmatter with `yaml.safe_load`; keep the body (after the closing `---`)
byte-for-byte. Edit the frontmatter dict, then re-emit:
```python
out = "---\n" + yaml.dump(fm, sort_keys=False, allow_unicode=True, width=4096) + "---\n" + body
```
This preserves every prompt body exactly. NEVER use sed/regex on YAML frontmatter — it collapses
multi-line lists and merges keys. Handle CRLF by checking for both `---\n` and `---\r\n`.

## Repair rules (apply after parsing frontmatter)
- `trigger:` must equal `/<filename-slug>`; rename `triggers:` (plural) -> `trigger:`.
- `name:` must equal the filename slug.
- DEPS==SKILLS: union of `skill:` deps and the `skills:` list, made bidirectional (every skill dep
  appears in `skills:`, every `skills:` entry has a `skill:` dep).
- MCP servers: `dependencies:` uses `tool:mcp-<name>` (NOT `skill:mcp-<name>`); remove `mcp-*` from
  `skills:`; add `- mcp` to `toolsets:` when an mcp dep exists.
- toolset normalization: drop VS Code/Copilot names (`editFiles`, `search`, `github/*`, `vscode.*`);
  map to the Hermes palette; default `[terminal, file]` if empty; dedupe.
- remove self-referencing `skill:<self>` deps.
- duplicate frontmatter blocks: a file with two `---` fences (second bleeding into body as text)
  must be rewritten whole via `write_file` — one merged clean frontmatter + body after the last `---`.

## Independent dual-verifier (run this SEPARATELY after any fixer)
A fixer reporting "0 issues" is not proof — it may share the assumptions it "fixed." Run a second
script with a different code path and confirm 0. Checks:
- frontmatter valid YAML; `name`==slug; `trigger`==`/<slug>`; no `triggers:` (plural).
- DEPS==SKILLS exact match.
- every `skill:` resolves to a real `SKILL.md` under `~/AppData/Local/hermes/skills/`.
- every `tool:mcp-*` is a known server; every `tool:` is a valid native tool OR mcp server
  (`tool:terminal`, `tool:search_files`, `tool:patch`, `tool:write_file`, `tool:execute_code`,
  `tool:delegate_task` are all VALID — not mislabels).
- no duplicate `metadata:` blocks; no `## Legacy Prompt Details`; all `templates/...` links resolve.

## False-positive discipline (verify before acting)
- Injection-safety regexes fire on the literal words "System Prompt" in a heading/title — NOT an
  injection attempt. Require a real override instruction before flagging CRITICAL.
- `rm -rf` is safe only when the same scope says verify/after/confirm/approval.
- `prompt:foo.prompt.md` (with suffix) still resolves to prompt `foo`; not dangling.
- When an audit reports N issues, independently reproduce the check before editing.

## Reference implementations (already on disk, proven this session)
- `~/AppData/Local/hermes/scripts/fix_prompt_library.py` — deterministic repair.
  Usage: `python fix_prompt_library.py --all` (audit) or `--all --apply` (mutate);
  `--files a.prompt.md,b.prompt.md` for a subset.
- `~/AppData/Local/hermes/scripts/verify_prompt_library.py` — independent verifier;
  prints `TOTAL / CLEAN / WITH_ISSUES` and per-issue-type counts.
- `~/AppData/Local/hermes/scripts/audit_prompt_library.py` — deep read-only audit
  (skill/tool/prompt resolution, safety, delegation map) with the false-positive filters.
