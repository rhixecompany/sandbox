# Skills Hub Update/Check Loop — Windows Hash-Asymmetry Root Cause (2026-08-11)

## Symptom

- `hermes skills check` reported 26 `update_available` across 36 skills.
- `hermes skills update` exited 0 and printed `Updated 26 skill(s).`
- Immediate re-check: **31 updates across 41 skills** — the count GREW.
- Some files genuinely updated on disk (code-wiki, godmode → SKILL.md mtime
  Aug 11 20:05) while others did not (subagent-driven-development → Jul 31)
  despite the update log claiming `Installed:` for them.
- `lock.json` recorded hash `sha256:6d70…` for subagent-driven-development;
  a direct `check_for_skill_updates(name=...)` call computed upstream
  `sha256:6432…` — mismatch that never heals.

## Root cause 1 — hash functions asymmetric on Windows

Two functions must produce the same digest for the same skill content
(the docstring in `tools/skills_guard.py` at `content_hash` explicitly
says: "any change to the hash shape MUST land in both places at once"):

| | `bundle_content_hash` (in-memory, tools/skills_hub.py:4057) | `content_hash` → `_content_digest` (on-disk, tools/skills_guard.py:699) |
|---|---|---|
| Path separators | hashes `rel_path` **as fetched** — on Windows `Path.relative_to()` yields **backslashes** (`references\context-budget-discipline.md`) | normalizes `Path.as_posix()` → **forward slashes** (`references/context-budget-discipline.md`) |
| Sort order | `sorted(bundle.files)` — raw string sort, **case-sensitive** | `sorted(skill_path.rglob("*"))` — pathlib `Path` sort, **case-insensitive on Windows** (normcase) |

Consequence: same files → different digests → `check_for_skill_updates`
(line ~4136) compares `entry["content_hash"]` vs `bundle_content_hash(bundle)`
and reports `update_available` forever. Every multi-file skill is affected;
single-file skills (only `SKILL.md`, no subdirs) happened to match.

## Root cause 2 — backslash identifiers break category auto-detect

`OfficialSkillSource.fetch` (tools/skills_hub.py:3396) built the identifier
as `f"official/{skill_dir.relative_to(self._optional_dir)}"` — on Windows
this yields `official/software-development\subagent-driven-development`
(mixed separators). Then in `do_install` (hermes_cli/skills_hub.py:622):

```python
if bundle.source == "official" and not category:
    id_parts = bundle.identifier.split("/")
    if len(id_parts) >= 3:
        category = "/".join(id_parts[1:-1])
```

`split("/")` sees only 2 parts (`["official", "software-development\\subagent…"]`)
→ `category=""` → the skill installs **flat** at `skills/<name>/` instead of
`skills/<category>/<name>/`. The loader (`iter_skill_index_files` + dedupe
in `_find_all_skills`) resolves the **categorized** copy — so the loader
keeps serving the stale categorized copy while updates write to the flat
copy the loader ignores. That's why "updates never stick" from the user's
perspective.

## Fixes applied (all in tools/skills_hub.py)

1. **`_sort_key` must mirror pathlib's component-wise ordering — full-string
   normcase is NOT enough.** The disk walker (`tools/skills_guard._content_digest`)
   sorts `Path` objects, which compare by *parts* (`Path.__lt__` on parts), NOT
   by the full string. They diverge whenever a directory and a file share a
   prefix: sorted by Path, `references/styles/blueprint.md` sorts BEFORE
   `references/styles.md`; sorted as full strings (normcased), `styles.md`
   comes first because `.` < `/`. Same bytes → different digests → perpetual
   update_available. The correct sort key is
   `tuple(os.path.normcase(part) for part in path.replace("\\", "/").split("/"))`.
   Verified empirically: this tuple key reproduces `sorted(Path)` exactly while
   full-string normcase does not (proof probe in session 2026-08-11).
2. **CRLF write bug in `quarantine_bundle`.** It wrote `str`-typed bundle
   content via `file_dest.write_text(content)` — on Windows the default
   `newline=None` translates `\n`→`\r\n` on disk. skills.sh/browse-sh
   bundles arrive as `str` (LF); official bundles arrive as `bytes` and were
   fine. So installed single-file skills (e.g. prompt-engineering,
   hooks-pattern, agentmemory-hooks, data-migration-scripts) landed CRLF while
   the in-memory bundle stayed LF → lock hash (computed from disk, CRLF) never
   matched the fresh-fetch bundle hash (LF) → update loop. Fix: encode to
   bytes and write verbatim (`file_dest.write_bytes(content.encode("utf-8"))`).
   `shutil.move` from quarantine → install preserves bytes, so fixing the
   quarantine write fixes the install.
3. **Official identifier `.as_posix()`** (from the first fix round, still
   required): `OfficialSkillSource.fetch` must build the identifier with
   `relative_to(...).as_posix()` or mixed `\` separators break the
   `split("/")` category auto-detect in `hermes_cli/skills_hub.py:622`.

Reporting bug (not fixed, noted): `do_update` in hermes_cli/skills_hub.py
counts every `update_available` entry as "Updated" regardless of whether
`do_install` actually succeeded (log even says "already installed" per
skill while still counting it).

## Verification methodology (reuse)

- Prove hash symmetry with a standalone probe script rather than guessing:
  fetch the bundle, compute both digests, assert equality. Write the probe
  to a temp `.py` and run `MSYS_NO_PATHCONV=1 <venv-python> probe.py` from
  `~/.hermes/skills/.hub/` — inline `python -c` mangles backslashes in
  MSYS (SyntaxError on `replace('\\', '/')`).
- Distinguish "did the update actually land" vs "check bug":
  `lock.get_installed(name)["content_hash"]` vs
  `content_hash(install_dir)` — equal means the update recorded correctly
  and the failure is in the comparison layer.
- `hermes skills update` fetch comes from the local `optional-skills/`
  checkout for official skills — check its mtimes vs the installed dir to
  see whether upstream content actually changed.

## Remaining data repair (dual-path skills)

Four skills had BOTH flat + categorized copies after the buggy updates;
the loader prefers whichever sorted first:

| skill | flat copy | categorized copy | loader serves |
|---|---|---|---|
| subagent-driven-development | new (Aug 11, digest 6d70…) | stale (Jul 31, digest 4b62…) | categorized (stale) → needs reconciliation |
| code-wiki | new | stale | flat (new) ✓ |
| cloudflare-temporary-deploy | new | stale | flat (new) ✓ |
| prompt-engineering | hub flat (skills.sh) | user dev/ copy (Jul 27) | categorized (user copy) — leave unless user wants hub version |

Repair for subagent-driven-development class: overwrite categorized copy
from flat (or move flat→categorized), update lock `install_path` to
`software-development/<name>`, recompute `content_hash` from the new
location, remove the flat duplicate, then re-run `hermes skills check`
and `hermes skills update` to confirm the loop clears.

## Key files

- `tools/skills_hub.py` — `bundle_content_hash` (4057), `OfficialSkillSource.fetch` (3347/3396), `check_for_skill_updates` (4081)
- `tools/skills_guard.py` — `content_hash` (854), `_content_digest` (699)
- `hermes_cli/skills_hub.py` — `do_update` (1055), `do_install` category detect (622)
- `agent/skill_utils.py` — `iter_skill_index_files` (877), loader dedupe
- `tools/skills_tool.py` — `_find_all_skills` (673)
- `~/.hermes/skills/.hub/lock.json` — `installed.<name>.content_hash`
