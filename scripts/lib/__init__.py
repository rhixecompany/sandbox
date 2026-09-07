"""Shared utilities for scripts in the Hermes scripts/ directory.

Provides common helper functions for file I/O, error reporting,
and CLI argument parsing used across all scripts.
"""

import sys
from pathlib import Path


def fail(msg: str, exit_code: int = 1) -> None:
    """Print an error message to stderr and exit.

    Args:
        msg: Error message to display.
        exit_code: Exit code to use (default 1).
    """
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(exit_code)


def ensure_dir(path: Path) -> None:
    """Ensure a directory exists, creating it if needed.

    Args:
        path: Path to the directory to ensure.

    Raises:
        OSError: If the directory cannot be created.
    """
    path.mkdir(parents=True, exist_ok=True)


def read_file_text(path: Path) -> str:
    """Read a text file and return its contents.

    Args:
        path: Path to the file to read.

    Returns:
        The file contents as a string.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file cannot be read.
    """
    try:
        return path.read_text(encoding="utf-8")
    except (FileNotFoundError, PermissionError) as e:
        fail(f"Cannot read {path}: {e}")


def write_file_text(path: Path, content: str) -> None:
    """Write a string to a file, creating parent directories as needed.

    Args:
        path: Path to the file to write.
        content: The string content to write.

    Raises:
        PermissionError: If the file cannot be written.
        OSError: If the directory cannot be created or file written.
    """
    ensure_dir(path.parent)
    try:
        path.write_text(content, encoding="utf-8")
    except (PermissionError, OSError) as e:
        fail(f"Cannot write {path}: {e}")


def add_std_cli(parser) -> None:
    """Add standard --verbose and --quiet flags to an ArgumentParser.

    Args:
        parser: The ArgumentParser instance to augment.
    """
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("--quiet", action="store_true", help="Suppress non-error output")
