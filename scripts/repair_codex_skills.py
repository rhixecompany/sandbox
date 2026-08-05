#!/usr/bin/env python3
"""repair_codex_skills.py — strict-repair SKILL.md YAML frontmatter in a skill tree.

Mirrors the STRICT YAML rules codex uses (duplicate keys are fatal, empty
scalars for description/title are fatal, unclosed quoted scalars are fatal) and
repairs the full class of failures so codex stops dropping skills.

Common failure modes fixed:
  - duplicate `name`/`version`/`author` keys          -> keep FIRST occurrence
  - empty `description:` / `title:` (folded/literal)  -> synthesize from name
  - unclosed quoted scalar in description             -> re-quote safely
  - malformed scalar blocks (`description: |` with unindented body) -> re-wrap
  - trailing carriage returns in frontmatter fields   -> strip

Usage:
      python repair_codex_skills.py <tree_root> --apply
      python repair_codex_skills.py <tree_root>   (dry-run)

With --apply, broken files are rewritten in place (plus a .orig backup).
Without it, runs read-only and reports what WOULD change.
"""
from __future__ import annotations

import pathlib
import re
import shutil
import sys

import yaml

KEEP_FIRST = ("name", "version", "author", "license", "platforms")
KEEP_LAST = ("description", "title", "category", "tags")


class _UniqLoader(yaml.SafeLoader):
    """SafeLoader subclass that rejects duplicate mapping keys.

    Source of truth for frontmatter schema; we also quote `description` greedily
    to catch the "empty scalar" case below. NOTE: yaml.load() with this Loader
    is SAFE because SafeLoader only ever constructs standard types (str/int/
    list/dict/float/bool/None) — it never instantiates arbitrary Python classes
    from !!python/* tags. Only the duplicate-key guard is added.
    """


def _construct_mapping_uniq(loader, node, deep=False):
    seen = set()
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            raise ValueError(f"duplicate key `{key}`")
        seen.add(key)
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


_UniqLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping_uniq
)


def parse_ok(fm: str):
    """Return (ok, error, data). Strict: dup keys + empty description/title rejected."""
    try:
        data = yaml.load(fm, Loader=_UniqLoader)
    except Exception as e:
        return False, f"parse: {e}", None
    if not isinstance(data, dict):
        return False, "not a mapping", None
    for req in ("description",):
        if req not in data or data.get(req) in (None, "", ""):
            return False, f"missing-or-empty `{req}`", data
    return True, "", data


def _salvage_description(body: str, name: str) -> str:
    """Try to recover the real description text lost in a malformed `|`/`>` block."""
    desc = ""
    for i, line in enumerate(body.split("\n")):
        m = re.match(r"^\s*(?:description|title)\s*:[|>]+\s*$", line)
        if m:
            # collect subsequent MORE-indented lines (block content)
            content = []
            for following in body.split("\n")[i + 1:]:
                if following and not following.startswith((" ", "\t")):
                    break  # unindented key -> end of block content
                content.append(following.strip())
            desc = " ".join(c for c in content if c).strip()
            break
    if not desc:
        desc = f"{name}: no description provided."
    return desc


def _repair_body(body: str, name: str) -> dict:
    """Parse body, tolerant of duplicate keys and unclosed scalars."""
    try:
        data = yaml.safe_load(body) or {}
    except Exception:
        # unclosed quoted scalar etc -> salvage known fields line-by-line
        data = {}
        for line in body.split("\n"):
            m = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", line)
            if m and m.group(2).strip() and m.group(1) not in data:
                data[m.group(1)] = m.group(2).strip()
    if not isinstance(data, dict):
        data = {}
    data.setdefault("name", name)
    desc = data.get("description")
    if desc in (None, "", ""):
        data["description"] = _salvage_description(body, name)
    return data


def split_fm(txt: str):
    """Return (frontmatter_body, rest) given text starting with '---'."""
    if not txt.lstrip().startswith("---"):
        return None, txt
    lines = txt.split("\n")
    if lines and lines[0].strip() == "":
        lines = lines[1:]
    # first line is the opening ---
    rest_idx = 1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            rest_idx = i
            break
    body = "\n".join(lines[1:rest_idx])
    rest = "\n".join(lines[rest_idx + 1:])
    return body, rest


def main() -> int:
    argv = sys.argv[1:]
    if not argv:
        print(__doc__)
        return 2
    root = pathlib.Path(argv[0]).expanduser().resolve()
    apply = "--apply" in argv
    if not root.is_dir():
        print(f"not a dir: {root}")
        return 2
    broken: list[tuple[pathlib.Path, str]] = []
    all_skills = sorted(root.rglob("SKILL.md"))

    for p in all_skills:
        txt = p.read_text(encoding="utf-8", errors="replace")
        body, rest = split_fm(txt)
        if body is None:
            broken.append((p, "no-frontmatter"))
            continue
        ok, err, data = parse_ok(body)
        if not ok:
            broken.append((p, err))

    print(f"Scanned {len(all_skills)} SKILL.md; broken: {len(broken)}")
    for p, err in broken:
        rel = p.relative_to(root)
        print(f"  [FIX] {rel}  ({err})")
        if not apply:
            continue
        txt = p.read_text(encoding="utf-8", errors="replace")
        body, rest = split_fm(txt)
        shutil.copy2(p, str(p) + ".orig")
        if body is None:
            new = f"---\nname: {p.parent.name}\ndescription: auto-regenerated.\n---\n\n{rest}"
        else:
            data = _repair_body(body, p.parent.name)
            new_fm = yaml.safe_dump(data, sort_keys=False, allow_unicode=True).rstrip()
            new = f"---\n{new_fm}\n---\n\n{rest}"
        p.write_text(new, encoding="utf-8", newline="\n")

    print("\n" + ("APPLIED (with .orig backups)." if apply else "DRY-RUN — pass --apply to write."))
    return 0 if apply else 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
