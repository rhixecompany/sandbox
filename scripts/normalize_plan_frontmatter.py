#!/usr/bin/env python3
"""Minimal frontmatter normalizer for plan files.

For each plan file passed as argv, if it lacks YAML frontmatter (does not start
with '---\n'), prepend a frontmatter block with status: completed (the live
inventory already confirmed the end-state artifacts exist on disk). Preserves the
original first heading and the blank separator line.

Idempotent: skips files that already have a '---' frontmatter opener.
Read-only wrt content: only adds a header; body untouched.
"""
import sys

STATUS = "completed"


def has_frontmatter(text):
    return text.startswith("---")


def add_frontmatter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if has_frontmatter(text):
        return f"skip (has frontmatter): {path}"
    # Build frontmatter; keep a single blank line before original body.
    fm = f"---\nstatus: {STATUS}\n---\n\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(fm + text)
    return f"added frontmatter: {path}"


def main():
    for p in sys.argv[1:]:
        try:
            print(add_frontmatter(p))
        except Exception as exc:  # pragma: no cover
            print(f"ERROR {p}: {exc}")


if __name__ == "__main__":
    raise SystemExit(main())
