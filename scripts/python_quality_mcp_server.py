#!/usr/bin/env python3
"""Python Quality MCP Server — ruff lint/format/fix + pyright type checking.

Provides MCP tools for the full Pylance/Ruff workflow:
  - python_lint       Run ruff check on files/directories
  - python_format     Format code with ruff format (check-only or in-place)
  - python_fix        Auto-fix lint violations with ruff check --fix
  - python_typecheck  Run pyright static type checking
  - python_check_all  Run lint + typecheck together
  - python_init_config  Scaffold ruff.toml + pyrightconfig.json

Install: pip install mcp (FastMCP)
Run:     python python_quality_mcp_server.py
         # or via Hermes config as a stdio MCP server
"""

from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# ── Create server ──────────────────────────────────────────────────────
mcp = FastMCP("python-quality", log_level="INFO")

# ── Helpers ────────────────────────────────────────────────────────────


def _find_ruff(project_root: str | None = None) -> str:
    """Locate the ruff binary, preferring venv-local."""
    # Check project venv first
    if project_root:
        for candidate in (
            Path(project_root) / "myvenv" / "Scripts" / "ruff.exe",
            Path(project_root) / "myvenv" / "Scripts" / "ruff",
            Path(project_root) / ".venv" / "Scripts" / "ruff.exe",
            Path(project_root) / ".venv" / "Scripts" / "ruff",
        ):
            if candidate.exists():
                return str(candidate)
    # Fallback: PATH lookup
    for p in os.environ.get("PATH", "").split(os.pathsep):
        for exe in ("ruff.exe", "ruff"):
            candidate = Path(p) / exe
            if candidate.exists():
                return str(candidate)
    return "ruff"  # let subprocess fail with PATH lookup


def _find_pyright() -> str:
    """Locate the pyright binary — prefer .cmd on Windows for subprocess compatibility."""
    # Check for .cmd wrapper first (Windows needs .cmd, not POSIX shell script)
    for p in os.environ.get("PATH", "").split(os.pathsep):
        for exe in ("pyright.cmd", "pyright.exe", "pyright"):
            candidate = Path(p) / exe
            if candidate.exists():
                return str(candidate)
    return "pyright"


def _run_cmd(cmd: list[str], cwd: str | None = None, timeout: int = 120) -> dict:
    """Run a command and return structured result."""
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=cwd,
            timeout=timeout,
        )
        return {
            "exit_code": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
        }
    except subprocess.TimeoutExpired:
        return {"exit_code": -1, "stdout": "", "stderr": f"Command timed out after {timeout}s"}
    except FileNotFoundError:
        return {"exit_code": -2, "stdout": "", "stderr": f"Command not found: {cmd[0]}"}


def _summarize_ruff_output(result: dict) -> str:
    """Format ruff output into a readable summary."""
    parts = []
    if result["stdout"]:
        parts.append("📋 Output:\n" + result["stdout"].strip())
    if result["stderr"]:
        parts.append("⚠️  Stderr:\n" + result["stderr"].strip())

    # Parse summary line from ruff output (e.g. "Found 12 errors.")
    for line in (result["stdout"] + result["stderr"]).splitlines():
        m = re.match(r"Found\s+(\d+)\s+errors?", line)
        if m:
            count = int(m.group(1))
            parts.append(f"\n{'✅ No errors found.' if count == 0 else f'❌ {count} error(s) remaining.'}")
            break
    if not parts:
        parts.append(f"Exit code: {result['exit_code']}")
    return "\n".join(parts)


def _canonical_path(path: str, project_root: str | None = None) -> str:
    """Resolve path relative to project_root if given."""
    if not project_root:
        return path
    p = Path(path)
    if not p.is_absolute():
        return str(Path(project_root) / p)
    return str(p)


# ── Tools ──────────────────────────────────────────────────────────────


@mcp.tool(
    name="python_lint",
    description="Run ruff check on Python files/directories. Returns all lint violations.",
)
def python_lint(
    path: str = ".",
    project_root: str | None = None,
    select: str | None = None,
    ignore: str | None = None,
) -> str:
    """Run ruff check linting.

    Args:
        path: File or directory to lint (relative to project_root or absolute).
        project_root: Project root directory. If None, uses current dir.
        select: Comma-separated rule codes to enable (e.g. 'E,F,I').
        ignore: Comma-separated rule codes to ignore (e.g. 'E501').
    """
    p_root = project_root or os.getcwd()
    target = _canonical_path(path, p_root)
    ruff_bin = _find_ruff(p_root)

    cmd = [ruff_bin, "check", target]
    if select:
        cmd.extend(["--select", select])
    if ignore:
        cmd.extend(["--ignore", ignore])

    result = _run_cmd(cmd, cwd=p_root)
    return _summarize_ruff_output(result)


@mcp.tool(
    name="python_format",
    description="Check or apply ruff formatting on Python files. Use check_only=True to preview changes without modifying files.",
)
def python_format(
    path: str = ".",
    project_root: str | None = None,
    check_only: bool = False,
) -> str:
    """Format Python code with ruff.

    Args:
        path: File or directory to format.
        project_root: Project root directory.
        check_only: If True, only check formatting (no changes). Default False.
    """
    p_root = project_root or os.getcwd()
    target = _canonical_path(path, p_root)
    ruff_bin = _find_ruff(p_root)

    cmd = [ruff_bin, "format", "--diff" if check_only else "--quiet", target]
    result = _run_cmd(cmd, cwd=p_root)

    if result["exit_code"] == 0:
        return "✅ All files already formatted."
    elif check_only:
        # ruff format --diff returns exit code 1 when changes are needed
        return "📋 Changes needed:\n" + (result["stdout"] or result["stderr"]).strip()
    else:
        lines = (result["stdout"] + result["stderr"]).strip().splitlines()
        n_formatted = sum(1 for l in lines if "formatted" in l.lower() or "reformatted" in l.lower())
        return f"✅ Formatted {n_formatted} file(s)." if n_formatted else "✅ Done."


@mcp.tool(
    name="python_fix",
    description="Auto-fix lint violations using ruff check --fix. Can apply unsafe fixes too.",
)
def python_fix(
    path: str = ".",
    project_root: str | None = None,
    unsafe: bool = False,
) -> str:
    """Auto-fix lint violations with ruff.

    Args:
        path: File or directory to fix.
        project_root: Project root directory.
        unsafe: If True, apply unsafe fixes as well. Default False.
    """
    p_root = project_root or os.getcwd()
    target = _canonical_path(path, p_root)
    ruff_bin = _find_ruff(p_root)

    cmd = [ruff_bin, "check", "--fix", target]
    if unsafe:
        cmd.append("--unsafe-fixes")

    result = _run_cmd(cmd, cwd=p_root)

    # Count fixed vs remaining
    remaining = 0
    fixed = 0
    for line in (result["stdout"] + result["stderr"]).splitlines():
        m = re.match(r"Found\s+(\d+)\s+error", line)
        if m:
            remaining = int(m.group(1))
        m2 = re.match(r"(\d+)\s+fixed", line)
        if m2:
            fixed = int(m2.group(1))

    parts = []
    if fixed:
        parts.append(f"🔧 {fixed} error(s) auto-fixed.")
    if remaining:
        parts.append(f"⚠️  {remaining} error(s) remaining (need manual fix).")
    if not fixed and not remaining and result["exit_code"] == 0:
        parts.append("✅ No errors found.")

    if result["stderr"] and "Error" in result["stderr"]:
        parts.append("\n⚠️  Stderr:\n" + result["stderr"].strip())

    return "\n".join(parts) if parts else _summarize_ruff_output(result)


@mcp.tool(
    name="python_typecheck",
    description="Run pyright static type checker on Python files. Returns type errors and warnings.",
)
def python_typecheck(
    path: str = ".",
    project_root: str | None = None,
    level: str | None = None,
) -> str:
    """Static type checking with pyright.

    Args:
        path: File or directory to check.
        project_root: Project root directory.
        level: Verbosity level ('warning' or 'information'). Default shows errors only.
    """
    p_root = project_root or os.getcwd()
    target = _canonical_path(path, p_root)
    pyright_bin = _find_pyright()

    cmd = [pyright_bin, target]
    if level:
        cmd.extend(["--level", level])

    result = _run_cmd(cmd, cwd=p_root, timeout=180)

    # Parse summary
    lines = (result["stdout"] + result["stderr"]).splitlines()
    summary_lines = [l for l in lines if re.search(r"\d+\s+(error|warning|information)", l)]
    diagnostics = [l for l in lines if not l.startswith(" ")]

    parts = []
    if summary_lines:
        parts.append("📊 " + " | ".join(summary_lines))
    if diagnostics:
        # Show last N diagnostic lines (most important)
        important = [l for l in diagnostics if l.strip() and not l.strip().startswith("pyright")]
        if important:
            parts.append("\n📋 Diagnostics (last 15):\n" + "\n".join(important[-15:]))

    # Exit code: 0 = no errors, 1 = type errors found
    if result["exit_code"] == 0:
        parts.append("\n✅ No type errors found.")
    else:
        parts.append(f"\n❌ Type errors found (exit code {result['exit_code']}).")

    return "\n".join(parts)


@mcp.tool(
    name="python_check_all",
    description="Run comprehensive Python quality check: ruff lint + pyright type check + ruff check-only format. Returns a unified report.",
)
def python_check_all(
    path: str = ".",
    project_root: str | None = None,
) -> str:
    """Full quality check: lint + type check + format check.

    Args:
        path: File or directory to check.
        project_root: Project root directory.
    """
    p_root = project_root or os.getcwd()
    ruff_bin = _find_ruff(p_root)
    pyright_bin = _find_pyright()
    target = _canonical_path(path, p_root)

    report_parts = []
    report_parts.append("# 🔍 Python Quality Check Report")
    report_parts.append(f"Path: {target}\n")

    # 1. Ruff lint
    report_parts.append("## 1. Ruff Lint")
    lint = _run_cmd([ruff_bin, "check", target], cwd=p_root)
    lint_errors = 0
    for line in (lint["stdout"] + lint["stderr"]).splitlines():
        m = re.search(r"Found\s+(\d+)\s+error", line)
        if m:
            lint_errors = int(m.group(1))
    report_parts.append(f"Errors: {lint_errors}")
    if lint_errors > 0:
        report_parts.append(f"```\n{lint['stdout'][:2000]}\n```")
    report_parts.append("")

    # 2. Ruff format check
    report_parts.append("## 2. Ruff Format")
    fmt = _run_cmd([ruff_bin, "format", "--check", "--diff", target], cwd=p_root)
    if fmt["exit_code"] == 0:
        report_parts.append("✅ All formatted.")
    else:
        n_unformatted = sum(1 for l in (fmt["stdout"] + fmt["stderr"]).splitlines() if l.strip())
        report_parts.append(f"⚠️  {n_unformatted} file(s) need formatting.")
    report_parts.append("")

    # 3. Pyright type check
    report_parts.append("## 3. Pyright Type Check")
    tc = _run_cmd([pyright_bin, target], cwd=p_root, timeout=180)
    tc_errors = 0
    tc_lines = (tc["stdout"] + tc["stderr"]).splitlines()
    for line in tc_lines:
        m = re.search(r"(\d+)\s+error", line)
        if m:
            tc_errors += int(m.group(1))
    report_parts.append(f"Errors: {tc_errors}")
    if tc_errors > 0:
        report_parts.append(f"```\n{chr(10).join(tc_lines[-10:])}\n```")

    report_parts.append("")
    summary = "PASS ✅" if (lint_errors == 0 and tc_errors == 0) else "FAIL ❌"
    report_parts.append(f"## Summary: {summary}")

    return "\n".join(report_parts)


@mcp.tool(
    name="python_init_config",
    description="Scaffold ruff.toml and pyrightconfig.json files in a project root with battle-tested defaults.",
)
def python_init_config(
    project_root: str,
    target_python_version: str | None = None,
) -> str:
    """Create default config files for ruff + pyright.

    Args:
        project_root: Project root directory to write configs into.
        target_python_version: Python version target (e.g. '3.11', '3.12'). Default 3.11.
    """
    root = Path(project_root)
    if not root.is_dir():
        return f"❌ Directory does not exist: {project_root}"

    py_version = target_python_version or "3.11"
    created = []

    # ruff.toml
    ruff_path = root / ".ruff.toml"
    if not ruff_path.exists():
        ruff_config = f"""# Ruff configuration — auto-generated by python-quality MCP server
target-version = "{py_version}"
line-length = 120

# Enable rules
select = [
    "E",    # pycodestyle errors
    "F",    # pyflakes (undefined names, syntax)
    "I",    # isort (import sorting)
    "N",    # pep8-naming
    "W",    # pycodestyle warnings
    "UP",   # pyupgrade (modern Python)
    "B",    # flake8-bugbear (bug detection)
    "SIM",  # flake8-simplify (simplification)
    "ARG",  # flake8-unused-arguments
    "RUF",  # ruff-specific rules
]

# Ignore rules
ignore = [
    "E501",   # line too long (formatter handles this)
    "N818",   # exception name convention
]

# Format
[format]
quote-style = "double"
indent-style = "space"
line-ending = "lf"
"""
        ruff_path.write_text(ruff_config.lstrip())
        created.append(f"✅ Created: {ruff_path}")
    else:
        created.append(f"⏭️  Exists: {ruff_path}")

    # pyrightconfig.json
    pyright_path = root / "pyrightconfig.json"
    if not pyright_path.exists():
        pyright_config = {
            "include": ["."],
            "exclude": [
                "**/node_modules",
                "**/__pycache__",
                "**/.git",
                "**/myvenv",
                "**/.venv",
                "**/build",
                "**/dist",
                "**/*.pyc",
                "**/migrations",
            ],
            "typeCheckingMode": "basic",
            "reportMissingImports": "warning",
            "reportMissingTypeStubs": "none",
            "pythonVersion": py_version,
            "pythonPlatform": "Windows",
            "strictListInference": True,
            "strictDictionaryInference": True,
            "strictSetInference": True,
        }
        pyright_path.write_text(json.dumps(pyright_config, indent=2))
        created.append(f"✅ Created: {pyright_path}")
    else:
        created.append(f"⏭️  Exists: {pyright_path}")

    return "\n".join(created) if created else "All configs already exist."


# ── Main ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    mcp.run(transport="stdio")
