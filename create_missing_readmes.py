import os
import sys
from pathlib import Path
from datetime import date

TARGET_ROOT = Path(r"C:/Users/Alexa/Desktop/SandBox/.github/prompts/templates")
README_NAME = "README.md"
SKIP_DIRS = {"_shared"}

FRONTMATTER_TEMPLATE = """---
name: {slug}-template
title: {title} Template
description: Template notes and extracted content for the {title} prompt.
version: 1.0.0
tags: [template, prompts]
---

# {title} Template

Prompt: {slug}.prompt.md

## Purpose

TODO: describe what this prompt template is for.

## TODO

Author: populate with section inventory, usage notes, and any extracted fragments.
"""


def title_from_slug(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").strip().title()


def normalize_dir_name(slug: str) -> str:
    return slug.strip().replace(" ", "-")


def has_readme(dir_path: Path) -> bool:
    return any(p.name == README_NAME for p in dir_path.iterdir() if p.is_file())


def readme_path_for(dir_path: Path) -> Path:
    return dir_path / README_NAME


def create_readme(dir_path: Path) -> Path:
    slug = normalize_dir_name(dir_path.name)
    title = title_from_slug(slug)
    content = FRONTMATTER_TEMPLATE.format(slug=slug, title=title)
    path = readme_path_for(dir_path)
    path.write_text(content, encoding="utf-8")
    return path


def main() -> int:
    if not TARGET_ROOT.exists() or not TARGET_ROOT.is_dir():
        print(f"Error: target root does not exist or is not a directory:\n{TARGET_ROOT}")
        return 1

    missing_dirs = []
    for dir_path in sorted(TARGET_ROOT.iterdir()):
        if dir_path.is_dir() and dir_path.name not in SKIP_DIRS and not has_readme(dir_path):
            missing_dirs.append(dir_path)

    if not missing_dirs:
        print("No missing README.md files found under:\n" + str(TARGET_ROOT))
        return 0

    created = []
    for dir_path in missing_dirs:
        path = create_readme(dir_path)
        created.append(str(path))
        print(f"Created README.md: {path}")

    print(f"\nCreated {len(created)} README.md file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
