#!/usr/bin/env python3
"""Docs inventory report — generate an inventory report of all documentation files.

Usage:
    python docs-inventory-report.py [--workspace PATH] [--output PATH] [--format json|md|csv]
"""

import argparse
import asyncio
import json
import sys
from collections import defaultdict
from pathlib import Path

DOC_EXTS = {".md", ".rst", ".txt", ".pdf", ".html"}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate docs inventory report")
    parser.add_argument("--workspace", default=None, help="Workspace root directory")
    parser.add_argument("--output", default=None, help="Output path for report")
    parser.add_argument("--format", choices=["json", "md", "csv"], default="md", help="Output format")
    return parser.parse_args(argv)


def _scan_docs(root: Path) -> dict:
    """Scan for documentation files (CPU-bound)."""
    inventory: dict[str, list[dict]] = defaultdict(list)

    for ext in DOC_EXTS:
        for filepath in root.rglob(f"*{ext}"):
            # Skip hidden dirs and common non-doc dirs
            parts = filepath.relative_to(root).parts
            if any(p.startswith(".") for p in parts):
                continue
            if any(p in parts for p in ("node_modules", "__pycache__", ".venv", "venv", ".git")):
                continue

            rel_path = str(filepath.relative_to(root))
            ext_key = ext.lstrip(".")
            try:
                stat = filepath.stat()
                size = stat.st_size
            except OSError:
                size = 0

            inventory[ext_key].append(
                {
                    "path": rel_path,
                    "size": size,
                    "size_kb": round(size / 1024, 1),
                    "name": filepath.name,
                    "directory": str(filepath.parent),
                }
            )

    return dict(inventory)


async def scan_docs_async(root: Path) -> dict:
    """Scan docs asynchronously."""
    return await asyncio.to_thread(_scan_docs, root)


def format_markdown(inventory: dict, root_path: str) -> str:
    """Format inventory as markdown."""
    total_files = sum(len(files) for files in inventory.values())
    total_size = sum(f["size"] for files in inventory.values() for f in files)

    lines = [
        "# Documentation Inventory Report",
        "",
        f"**Workspace:** {root_path}",
        f"**Total files:** {total_files}",
        f"**Total size:** {round(total_size / 1024, 1)} KB",
        "",
        "## Summary by Type",
        "",
        "| Type | Count | Total Size |",
        "|------|-------|-----------|",
    ]
    for ext in sorted(inventory.keys()):
        ext_files = inventory[ext]
        ext_size = sum(f["size"] for f in ext_files)
        lines.append(f"| {ext} | {len(ext_files)} | {round(ext_size / 1024, 1)} KB |")

    lines.extend(["", "## All Files", "", "| File | Type | Size | Directory |"])
    lines.append("|------|------|------|-----------|")

    for ext in sorted(inventory.keys()):
        for f in sorted(inventory[ext], key=lambda x: x["path"]):
            lines.append(f"| {f['path']} | {ext} | {f['size_kb']} KB | {f['directory']} |")

    return "\n".join(lines)


def format_csv(inventory: dict) -> str:
    """Format inventory as CSV."""
    lines = ["type,path,name,directory,size_kb"]
    for ext in sorted(inventory.keys()):
        for f in sorted(inventory[ext], key=lambda x: x["path"]):
            lines.append(f"{ext},{f['path']},{f['name']},{f['directory']},{f['size_kb']}")
    return "\n".join(lines)


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    workspace = Path(args.workspace or Path.cwd())

    if not workspace.is_dir():
        print(f"ERROR: workspace not found: {workspace}", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning documentation files in {workspace}...")
    inventory = await scan_docs_async(workspace)

    total_files = sum(len(files) for files in inventory.values())
    print(f"Found {total_files} documentation file(s) across {len(inventory)} type(s)")

    output = ""
    if args.format == "json":
        output = json.dumps(inventory, indent=2)
    elif args.format == "csv":
        output = format_csv(inventory)
    else:
        output = format_markdown(inventory, str(workspace))

    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        print(f"\nReport written to {args.output}")
    else:
        # Show summary only
        print("\n--- Summary ---")
        for ext in sorted(inventory.keys()):
            ext_files = inventory[ext]
            ext_size = sum(f["size"] for f in ext_files)
            print(f"  .{ext}: {len(ext_files)} files, {round(ext_size / 1024, 1)} KB")


if __name__ == "__main__":
    asyncio.run(main())
