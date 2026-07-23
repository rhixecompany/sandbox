#!/usr/bin/env python3
"""Fix CRLF frontmatter — fix CRLF (Windows) line endings in frontmatter blocks of markdown files.

Usage:
    python fix_crlf_frontmatter.py [--workspace PATH] [--dry-run] [--verbose] [--report PATH]
"""

import asyncio
import argparse
import sys
from pathlib import Path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fix CRLF line endings in frontmatter blocks")
    parser.add_argument("--workspace", default=None, help="Workspace root directory")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without applying")
    parser.add_argument("--verbose", action="store_true", help="Detailed output")
    parser.add_argument("--report", default=None, help="Save fix report to file")
    return parser.parse_args(argv)


def _fix_crlf_in_frontmatter(text: str) -> tuple[str, bool]:
    """Fix CRLF line endings within YAML frontmatter blocks (CPU-bound)."""
    if not text.startswith("---"):
        return text, False

    # Fix CRLF in the entire frontmatter block
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text, False

    header = parts[0]
    fm = parts[1]
    body = parts[2]

    # Check if frontmatter has CRLF
    if "\r\n" not in fm:
        return text, False

    # Normalize CRLF → LF in frontmatter
    fm_fixed = fm.replace("\r\n", "\n")
    # Also fix the body if it has CRLF
    body_fixed = body.replace("\r\n", "\n")

    fixed = f"---\n{fm_fixed}\n---\n{body_fixed.lstrip()}"
    return fixed, True


def _scan_and_fix(filepath: Path, dry_run: bool) -> dict:
    """Scan and fix a single file (CPU-bound)."""
    try:
        text = filepath.read_bytes()
        original_decoded = text.decode("utf-8")
    except Exception as e:
        return {"file": str(filepath), "status": "error", "error": str(e)}

    # Check if file has CRLF anywhere
    has_crlf = b"\r\n" in text

    if not has_crlf:
        return {"file": str(filepath), "status": "unchanged", "fixes": []}

    fixed_text, changed = _fix_crlf_in_frontmatter(original_decoded)

    if not changed:
        return {"file": str(filepath), "status": "unchanged", "fixes": []}

    if not dry_run:
        filepath.write_text(fixed_text, encoding="utf-8")

    return {"file": str(filepath), "status": "fixed", "fixes": ["CRLF_TO_LF"]}


async def scan_and_fix_async(filepath: Path, dry_run: bool) -> dict:
    """Scan and fix a single file asynchronously."""
    return await asyncio.to_thread(_scan_and_fix, filepath, dry_run)


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    workspace = Path(args.workspace or Path.cwd())

    if not workspace.is_dir():
        print(f"ERROR: workspace not found: {workspace}", file=sys.stderr)
        sys.exit(1)

    # Find markdown files with YAML frontmatter
    md_files = sorted(workspace.rglob("*.md"))

    # Exclude common non-source dirs
    exclude_dirs = {".git", "__pycache__", "node_modules", ".venv", "venv", ".worktrees"}
    md_files = [f for f in md_files if not any(p in exclude_dirs for p in f.relative_to(workspace).parts)]

    print(f"Scanning {len(md_files)} markdown files in {workspace}...")

    # Quick pre-scan: check which files have frontmatter
    def _has_frontmatter(path: Path) -> bool:
        try:
            head = path.read_bytes()[:500]
            return head.startswith(b"---")
        except Exception:
            return False

    fm_files = []
    for f in md_files:
        has_fm = await asyncio.to_thread(_has_frontmatter, f)
        if has_fm:
            fm_files.append(f)

    print(f"Found {len(fm_files)} files with YAML frontmatter")

    tasks = [scan_and_fix_async(f, args.dry_run) for f in fm_files]
    results = await asyncio.gather(*tasks)

    fixed = [r for r in results if r["status"] == "fixed"]
    unchanged = [r for r in results if r["status"] == "unchanged"]
    errors = [r for r in results if r["status"] == "error"]

    mode = "DRY-RUN" if args.dry_run else "APPLIED"
    print(f"\n{mode}: {len(fixed)} fixed, {len(unchanged)} unchanged, {len(errors)} errors")

    if args.verbose:
        for r in fixed:
            print(f"  {r['file']}: {', '.join(r['fixes'])}")
        for r in errors:
            print(f"  ERROR: {r['file']}: {r.get('error', '')}")

    if args.report:
        report_path = Path(args.report)
        import json
        report_path.write_text(
            json.dumps({"fixed": fixed, "errors": errors, "dry_run": args.dry_run}, indent=2),
            encoding="utf-8",
        )
        print(f"\nReport written to {report_path}")


if __name__ == "__main__":
    asyncio.run(main())
