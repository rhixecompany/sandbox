"""
Python MCP Server — A production-ready MCP server with greeting and file search tools.

Uses the MCP Python SDK (FastMCP) with stdio transport.
"""

from __future__ import annotations

import fnmatch
import os
import sys
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Server setup
# ---------------------------------------------------------------------------

server = FastMCP(
    name="python-mcp-server",
    instructions="A Python MCP server providing greeting and file search tools.",
    log_level="INFO",
)


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------


@server.tool(
    name="greeting",
    description="Generate a personalized greeting message.",
)
def greeting(name: str, title: str | None = None, formal: bool = False) -> str:
    """Create a greeting for the given person.

    Args:
        name: The person's name to greet.
        title: Optional honorific (Mr., Ms., Dr., etc.).
        formal: If True, produce a formal greeting; otherwise casual.

    Returns:
        A friendly greeting string.
    """
    if not name or not name.strip():
        return "Hello, stranger!"

    cleaned_name = name.strip()
    prefix = f"{title.strip()} " if title and title.strip() else ""

    if formal:
        return f"Greetings, {prefix}{cleaned_name}. It is a pleasure to meet you."
    return f"Hey {prefix}{cleaned_name}, welcome to the MCP server! 👋"


@server.tool(
    name="search_files",
    description="Search for files matching a glob pattern under a directory.",
)
async def search_files(
    pattern: str,
    root_dir: str = ".",
    max_results: int = 20,
    case_sensitive: bool = False,
) -> list[dict[str, Any]]:
    """Recursively search for files matching *pattern* under *root_dir*.

    Args:
        pattern: Glob-style file pattern (e.g. ``"*.py"``, ``"**/*.md"``).
        root_dir: Root directory to start the search from (default: current dir).
        max_results: Maximum number of results to return (default: 20, max: 200).
        case_sensitive: Whether the pattern matching is case-sensitive.

    Returns:
        A list of dicts with keys ``path`` (absolute), ``size`` (bytes),
        ``modified`` (ISO-8601 timestamp), and ``is_dir``.

    Raises:
        ValueError: If *root_dir* does not exist or *max_results* is out of range.
        PermissionError: If parts of the tree are inaccessible.
    """
    if not 1 <= max_results <= 200:
        raise ValueError("max_results must be between 1 and 200")

    root = Path(root_dir).resolve()
    if not root.is_dir():
        raise ValueError(f"Directory does not exist: {root_dir} (resolved: {root})")

    matches: list[dict[str, Any]] = []

    try:
        for entry in root.rglob("*"):
            if len(matches) >= max_results:
                break

            # Normalise the path we test against
            rel = entry.relative_to(root)
            test = str(rel.as_posix())

            match_fn = fnmatch.fnmatchcase if case_sensitive else fnmatch.fnmatch
            if match_fn(test, pattern):
                try:
                    stat = entry.stat()
                    matches.append(
                        {
                            "path": str(entry.resolve()),
                            "size": stat.st_size,
                            "modified": stat.st_mtime,
                            "is_dir": entry.is_dir(),
                        }
                    )
                except OSError:
                    continue  # skip files we cannot stat
    except PermissionError:
        # Partial results are better than none
        pass

    return matches


# ---------------------------------------------------------------------------
# Entry-point
# ---------------------------------------------------------------------------


def main() -> None:
    """Run the MCP server over stdio."""
    server.run(transport="stdio")


if __name__ == "__main__":
    # When called directly, forward CLI args (e.g. --help) to FastMCP
    # The `run(transport="stdio")` call handles this.
    main()
