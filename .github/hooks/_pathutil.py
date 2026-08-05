"""
_pathutil.py — MSYS-safe path resolution for Windows.

Use::

    from _pathutil import resolve_path

    p = resolve_path(args.workspace)  # instead of Path(args.workspace).resolve()

Automatically converts MSYS /c/... prefix, falling back to cygpath -w.
Safe on non-Windows (passthrough).
"""

import re
import subprocess
import sys
from pathlib import Path

_CYG_WARNED = False


def resolve_path(raw: str) -> Path:
    """Resolve *raw* to an absolute Path, handling MSYS /x/ prefix on Windows.

    Also expands ``~`` (home directory) like ``Path.expanduser()``.

    On Windows with MSYS/git-bash::

        resolve_path("/c/Users/Alexa/Desktop")
        # → WindowsPath("C:/Users/Alexa/Desktop")

    On other platforms this is equivalent to ``Path(raw).resolve()``.
    """
    path_str = _fix_msys(raw)
    return Path(path_str).expanduser().resolve()


def _fix_msys(p: str) -> str:
    """Return a Windows-native path string for *p*.

    Three-tier strategy:
      1. cygpath -w   (most robust, handles symlinks/ junctions/UNC)
      2. Regex strip  (fast: /x/foo → X:/foo)
      3. Passthrough  (not an MSYS path, or not on Windows)

    """
    if sys.platform != "win32":
        return p

    # Tier 1 — native cygpath utility
    if _is_msys_path(p):
        try:
            r = subprocess.run(
                ["cygpath", "-w", p],
                capture_output=True, text=True, check=True, timeout=5,
            )
            if r.returncode == 0:
                return r.stdout.strip()
        except (subprocess.CalledProcessError, FileNotFoundError, OSError):
            pass

    # Tier 2 — regex fallback
    m = re.match(r"^/([a-zA-Z])/(.*)", p)
    if m:
        return f"{m.group(1).upper()}:\\{m.group(2)}"

    # Tier 3 — already a Windows path or unknown format
    return p


def _is_msys_path(p: str) -> bool:
    """Heuristic: starts with /x/ or /x (single-letter root)."""
    return bool(re.match(r"^/[a-zA-Z](/|$)", p))
