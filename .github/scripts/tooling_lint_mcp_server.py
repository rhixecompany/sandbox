#!/usr/bin/env python3
"""
tooling-lint MCP Server — wraps eslint, prettier, markdownlint-cli2, cspell.
Provides init/check/fix tools for each linter/formatter.
"""

import contextlib
import json
import os
import platform
import shutil
import subprocess


def _find_tool(name: str) -> str | None:
    """Locate a tool on PATH, handling Windows .cmd wrappers."""
    exe = shutil.which(name)
    if exe:
        return exe
    if platform.system() == "Windows":
        for ext in [".cmd", ".bat", ".exe"]:
            exe = shutil.which(name + ext)
            if exe:
                return exe
    return None


def _resolve_root(project_root: str | None = None) -> str:
    """Resolve project root to an absolute path."""
    if project_root:
        return os.path.abspath(project_root)
    # Try SandBox first, then cwd
    sandbox = r"C:\Users\Alexa\Desktop\SandBox"
    return sandbox if os.path.isdir(sandbox) else os.getcwd()


def _run(cmd, timeout=30, cwd=None):
    """Run a command and return structured result."""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=cwd or os.getcwd())
        return {"exit_code": r.returncode, "stdout": r.stdout[:10000], "stderr": r.stderr[:5000]}
    except subprocess.TimeoutExpired:
        return {"exit_code": -1, "stdout": "", "stderr": f"Timed out after {timeout}s"}
    except FileNotFoundError as e:
        return {"exit_code": -2, "stdout": "", "stderr": f"Tool not found: {e}"}


# ---------------------------------------------------------------------------
# eslint
# ---------------------------------------------------------------------------
def _eslint_init(project_root: str | None = None) -> dict:
    """Create eslint.config.mjs if it doesn't exist."""
    cwd = _resolve_root(project_root)
    config_path = os.path.join(cwd, "eslint.config.mjs")
    if os.path.exists(config_path):
        return {"status": "skipped", "message": "eslint.config.mjs already exists"}
    content = "\n".join(
        [
            'import js from "@eslint/js";',
            'import tseslint from "typescript-eslint";',
            "",
            "export default tseslint.config(",
            "  js.configs.recommended,",
            "  ...tseslint.configs.recommended,",
            '  { rules: { "no-unused-vars": "warn", "no-console": "off" } },',
            ");",
            "",
        ]
    )
    with open(config_path, "w") as f:
        f.write(content)
    return {"status": "created", "path": config_path}


def _eslint_check(path: str = ".", project_root: str | None = None, fix: bool = False) -> dict:
    """Run eslint on a file or directory."""
    exe = _find_tool("eslint")
    if not exe:
        return {"status": "error", "message": "eslint not found on PATH"}
    cmd = [exe, "--format", "json"]
    if fix:
        cmd.append("--fix")
    cmd.append(path)
    r = _run(cmd, timeout=60, cwd=_resolve_root(project_root))
    issues = []
    if r["stdout"]:
        with contextlib.suppress(json.JSONDecodeError):
            issues = json.loads(r["stdout"])
    return {
        "status": "ok" if r["exit_code"] in (0, 1) else "error",
        "exit_code": r["exit_code"],
        "issues_count": len(issues) if isinstance(issues, list) else 0,
        "issues": issues if isinstance(issues, list) else [],
        "stderr": r["stderr"],
    }


# ---------------------------------------------------------------------------
# prettier
# ---------------------------------------------------------------------------
def _prettier_init(project_root: str | None = None) -> dict:
    """Create .prettierrc.json with recommended defaults."""
    cwd = _resolve_root(project_root)
    config_path = os.path.join(cwd, ".prettierrc.json")
    if os.path.exists(config_path):
        return {"status": "skipped", "message": ".prettierrc.json already exists"}
    with open(config_path, "w") as f:
        json.dump(
            {"semi": True, "singleQuote": False, "trailingComma": "all", "printWidth": 120, "tabWidth": 2}, f, indent=2
        )
        f.write("\n")
    return {"status": "created", "path": config_path}


def _prettier_check(path: str = ".", project_root: str | None = None, fix: bool = False) -> dict:
    """Run prettier check on files."""
    exe = _find_tool("prettier")
    if not exe:
        return {"status": "error", "message": "prettier not found on PATH"}
    cmd = [exe, "--write" if fix else "--check", path]
    r = _run(cmd, timeout=60, cwd=_resolve_root(project_root))
    return {
        "status": "ok" if r["exit_code"] == 0 else "issues_found",
        "exit_code": r["exit_code"],
        "stdout": r["stdout"],
        "formatted": fix,
    }


# ---------------------------------------------------------------------------
# markdownlint-cli2
# ---------------------------------------------------------------------------
def _markdownlint_check(
    path: str = "*.md", project_root: str | None = None, config: str = ".markdownlintrc.json", fix: bool = False
) -> dict:
    """Run markdownlint on files."""
    exe = _find_tool("bunx") or _find_tool("npx")
    if not exe:
        return {"status": "error", "message": "bunx/npx not found on PATH"}
    cmd = [exe, "markdownlint-cli2", "--config", config, "--no-globs"]
    if fix:
        cmd.append("--fix")
    cmd.append(path)
    r = _run(cmd, timeout=60, cwd=_resolve_root(project_root))
    return {
        "status": "ok" if r["exit_code"] == 0 else "issues_found",
        "exit_code": r["exit_code"],
        "stdout": r["stdout"],
    }


# ---------------------------------------------------------------------------
# cspell (spellcheck)
# ---------------------------------------------------------------------------
def _cspell_init(project_root: str | None = None) -> dict:
    """Create cspell.json with basic config."""
    cwd = _resolve_root(project_root)
    config_path = os.path.join(cwd, "cspell.json")
    if os.path.exists(config_path):
        return {"status": "skipped", "message": "cspell.json already exists"}
    cfg = {
        "version": "0.2",
        "language": "en",
        "words": [],
        "ignoreWords": [],
        "flagWords": [],
        "dictionaries": ["python", "bash", "typescript", "css", "html", "markdown"],
        "ignorePaths": [
            "node_modules",
            "myvenv",
            ".git",
            "**/__pycache__/**",
            "**/build/**",
            "**/dist/**",
            "*.{png,jpg,jpeg,gif,svg,ico}",
            "projects/**",
        ],
    }
    with open(config_path, "w") as f:
        json.dump(cfg, f, indent=2)
        f.write("\n")
    return {"status": "created", "path": config_path}


def _cspell_check(path: str = ".", project_root: str | None = None) -> dict:
    """Run cspell spellcheck."""
    exe = _find_tool("cspell")
    if not exe:
        return {"status": "error", "message": "cspell not found on PATH"}
    r = _run([exe, "check", "--no-progress", path], timeout=60, cwd=_resolve_root(project_root))
    lines = [l.strip() for l in r["stdout"].splitlines() if " - " in l] if r["stdout"] else []
    return {
        "status": "ok" if r["exit_code"] == 0 else "issues_found",
        "exit_code": r["exit_code"],
        "issues_count": len(lines),
        "issues": lines,
        "stderr": r["stderr"],
    }


if __name__ == "__main__":
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("tooling-lint", description="Linting & formatting: eslint, prettier, markdownlint-cli2, cspell")

    @mcp.tool
    def eslint_init(project_root: str | None = None) -> dict:
        """Create eslint.config.mjs with recommended JS/TS config."""
        return _eslint_init(project_root)

    @mcp.tool
    def eslint_check(path: str = ".", project_root: str | None = None, fix: bool = False) -> dict:
        """Run eslint check. fix=true to auto-fix issues."""
        return _eslint_check(path, project_root, fix)

    @mcp.tool
    def prettier_init(project_root: str | None = None) -> dict:
        """Create .prettierrc.json with recommended defaults."""
        return _prettier_init(project_root)

    @mcp.tool
    def prettier_check(path: str = ".", project_root: str | None = None, fix: bool = False) -> dict:
        """Run prettier check. fix=true to format in-place."""
        return _prettier_check(path, project_root, fix)

    @mcp.tool
    def markdownlint_check(
        path: str = "*.md", project_root: str | None = None, config: str = ".markdownlintrc.json", fix: bool = False
    ) -> dict:
        """Run markdownlint on files. fix=true to auto-fix."""
        return _markdownlint_check(path, project_root, config, fix)

    @mcp.tool
    def cspell_init(project_root: str | None = None) -> dict:
        """Create cspell.json with basic spellcheck config."""
        return _cspell_init(project_root)

    @mcp.tool
    def cspell_check(path: str = ".", project_root: str | None = None) -> dict:
        """Run cspell spellcheck on files/directory."""
        return _cspell_check(path, project_root)

    mcp.run(transport="stdio")
