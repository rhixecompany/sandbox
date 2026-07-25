#!/usr/bin/env python3
"""
tooling-config MCP Server — pre-commit, git-cliff (changelog), .gitignore, .gitmodules, .editorconfig.

Provides init/validate tools for project configuration files and workflows.
"""

import os
import platform
import shutil
import subprocess


def _find_tool(name: str) -> str | None:
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
    if project_root:
        return os.path.abspath(project_root)
    sandbox = r"C:\Users\Alexa\Desktop\SandBox"
    return sandbox if os.path.isdir(sandbox) else os.getcwd()


def _run(cmd, timeout=30, cwd=None):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=cwd or os.getcwd())
        return {"exit_code": r.returncode, "stdout": r.stdout[:10000], "stderr": r.stderr[:5000]}
    except subprocess.TimeoutExpired:
        return {"exit_code": -1, "stdout": "", "stderr": f"Timed out after {timeout}s"}
    except FileNotFoundError as e:
        return {"exit_code": -2, "stdout": "", "stderr": f"Tool not found: {e}"}


# ---------------------------------------------------------------------------
# pre-commit
# ---------------------------------------------------------------------------
def _precommit_init(project_root: str | None = None) -> dict:
    """Create .pre-commit-config.yaml with basic hooks."""
    cwd = _resolve_root(project_root)
    cfg_path = os.path.join(cwd, ".pre-commit-config.yaml")
    if os.path.exists(cfg_path):
        return {"status": "skipped", "message": ".pre-commit-config.yaml already exists"}
    content = "\n".join(
        [
            "repos:",
            "  - repo: https://github.com/pre-commit/pre-commit-hooks",
            "    rev: v5.0.0",
            "    hooks:",
            "      - id: trailing-whitespace",
            "      - id: end-of-file-fixer",
            "      - id: check-yaml",
            "      - id: check-added-large-files",
            "      - id: check-json",
            "      - id: check-toml",
            "",
        ]
    )
    with open(cfg_path, "w") as f:
        f.write(content)
    return {"status": "created", "path": cfg_path}


def _precommit_install(project_root: str | None = None) -> dict:
    """Run pre-commit install in the project."""
    exe = _find_tool("pre-commit")
    if not exe:
        return {"status": "error", "message": "pre-commit not found on PATH"}
    r = _run([exe, "install"], timeout=30, cwd=_resolve_root(project_root))
    return {
        "status": "ok" if r["exit_code"] == 0 else "error",
        "exit_code": r["exit_code"],
        "stdout": r["stdout"],
        "stderr": r["stderr"],
    }


def _precommit_run(project_root: str | None = None, all_files: bool = True, hook: str = "") -> dict:
    """Run pre-commit on the project."""
    exe = _find_tool("pre-commit")
    if not exe:
        return {"status": "error", "message": "pre-commit not found on PATH"}
    cmd = [exe, "run"]
    if hook:
        cmd.append(hook)
    if all_files:
        cmd.append("--all-files")
    r = _run(cmd, timeout=120, cwd=_resolve_root(project_root))
    return {
        "status": "ok" if r["exit_code"] == 0 else "issues_found",
        "exit_code": r["exit_code"],
        "stdout": r["stdout"],
        "stderr": r["stderr"],
    }


# ---------------------------------------------------------------------------
# git-cliff (changelog)
# ---------------------------------------------------------------------------
def _changelog_init(project_root: str | None = None) -> dict:
    """Create cliff.toml with basic changelog config."""
    cwd = _resolve_root(project_root)
    cfg_path = os.path.join(cwd, "cliff.toml")
    if os.path.exists(cfg_path):
        return {"status": "skipped", "message": "cliff.toml already exists"}
    content = "\n".join(
        [
            "[changelog]",
            'header = "# Changelog\\n\\nAll notable changes to this project will be documented in this file.\\n"',
            'body = """',
            '{% for group, commits in commits | group_by(attribute="group") %}',
            "### {{ group | upper_first }}\\n",
            "{% for commit in commits %}",
            "- {{ commit.message | upper_first }}\\n",
            "{% endfor %}",
            "{% endfor %}",
            '"""',
            "trim = true",
            'footer = ""',
            "",
            "[git]",
            "conventional_commits = true",
            "filter_unconventional = true",
            "commit_parsers = [",
            '    { message = "^feat", group = "Features"},',
            '    { message = "^fix", group = "Bug Fixes"},',
            '    { message = "^docs", group = "Documentation"},',
            '    { message = "^refactor", group = "Refactoring"},',
            '    { message = "^test", group = "Testing"},',
            '    { message = "^chore", group = "Miscellaneous Tasks"},',
            "]",
            'skip_tags = "v0.1.0-beta.1"',
            "",
        ]
    )
    with open(cfg_path, "w") as f:
        f.write(content)
    return {"status": "created", "path": cfg_path}


def _changelog_generate(project_root: str | None = None, unreleased: bool = True) -> dict:
    """Generate changelog from git history via git-cliff."""
    exe = _find_tool("git-cliff")
    if not exe:
        return {"status": "error", "message": "git-cliff not found on PATH"}
    cmd = [exe, "--output", "CHANGELOG.md"]
    if unreleased:
        cmd.append("--unreleased")
    r = _run(cmd, timeout=60, cwd=_resolve_root(project_root))
    return {
        "status": "ok" if r["exit_code"] == 0 else "error",
        "exit_code": r["exit_code"],
        "stdout": r["stdout"],
        "stderr": r["stderr"],
    }


# ---------------------------------------------------------------------------
# .gitignore
# ---------------------------------------------------------------------------
def _gitignore_init(project_root: str | None = None) -> dict:
    """Create .gitignore with Python/JS common ignores if it doesn't exist."""
    cwd = _resolve_root(project_root)
    cfg_path = os.path.join(cwd, ".gitignore")
    if os.path.exists(cfg_path):
        return {"status": "skipped", "message": ".gitignore already exists"}
    content = "\n".join(
        [
            "# Python",
            "__pycache__/",
            "*.py[cod]",
            "*.egg-info/",
            ".eggs/",
            "dist/",
            "build/",
            "*.egg",
            "myvenv/",
            ".venv/",
            "venv/",
            "",
            "# Node",
            "node_modules/",
            ".next/",
            "out/",
            "",
            "# IDE",
            ".vscode/settings.json.user",
            ".vscode/workspaceStorage/",
            ".idea/",
            "*.swp",
            "*.swo",
            "",
            "# OS",
            ".DS_Store",
            "Thumbs.db",
            "",
            "# Environment",
            ".env",
            ".env.local",
            ".env.*.local",
            "",
        ]
    )
    with open(cfg_path, "w") as f:
        f.write(content)
    return {"status": "created", "path": cfg_path}


def _gitignore_validate(project_root: str | None = None) -> dict:
    """Check .gitignore exists and has expected content."""
    cwd = _resolve_root(project_root)
    cfg_path = os.path.join(cwd, ".gitignore")
    if not os.path.exists(cfg_path):
        return {"status": "missing", "message": ".gitignore not found"}
    with open(cfg_path) as f:
        content = f.read()
    missing = []
    for pattern in ["__pycache__", "node_modules", ".env"]:
        if pattern not in content:
            missing.append(pattern)
    return {
        "status": "ok" if not missing else "incomplete",
        "exists": True,
        "lines": len(content.splitlines()),
        "missing_patterns": missing,
    }


# ---------------------------------------------------------------------------
# .gitmodules
# ---------------------------------------------------------------------------
def _gitmodules_validate(project_root: str | None = None) -> dict:
    """Validate .gitmodules syntax and structure."""
    cwd = _resolve_root(project_root)
    cfg_path = os.path.join(cwd, ".gitmodules")
    if not os.path.exists(cfg_path):
        return {"status": "missing", "message": ".gitmodules not found"}
    try:
        # Parse via git config --file which understands gitmodule format
        r = _run(["git", "config", "--file", cfg_path, "--list"], timeout=10, cwd=cwd)
        if r["exit_code"] == 0:
            sections = set()
            for line in r["stdout"].splitlines():
                if line.startswith("submodule."):
                    parts = line.split(".")
                    if len(parts) >= 2:
                        sections.add(parts[1])
            return {
                "status": "ok",
                "submodules": list(sections),
                "entries": len(r["stdout"].splitlines()),
                "message": f"Valid: {len(sections)} submodule(s)",
            }
        else:
            return {"status": "error", "message": "Invalid .gitmodules format", "stderr": r["stderr"]}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# ---------------------------------------------------------------------------
# .editorconfig
# ---------------------------------------------------------------------------
def _editorconfig_init(project_root: str | None = None) -> dict:
    """Create .editorconfig with standard Python/JS defaults."""
    cwd = _resolve_root(project_root)
    cfg_path = os.path.join(cwd, ".editorconfig")
    if os.path.exists(cfg_path):
        return {"status": "skipped", "message": ".editorconfig already exists"}
    content = "\n".join(
        [
            "root = true",
            "",
            "[*]",
            "indent_style = space",
            "indent_size = 2",
            "end_of_line = crlf",
            "charset = utf-8",
            "trim_trailing_whitespace = true",
            "insert_final_newline = true",
            "",
            "[*.py]",
            "indent_size = 4",
            "",
            "[*.md]",
            "indent_size = 2",
            "",
            "[Makefile]",
            "indent_style = tab",
            "",
        ]
    )
    with open(cfg_path, "w") as f:
        f.write(content)
    return {"status": "created", "path": cfg_path}


def _editorconfig_validate(project_root: str | None = None) -> dict:
    """Check .editorconfig exists and has valid sections."""
    cwd = _resolve_root(project_root)
    cfg_path = os.path.join(cwd, ".editorconfig")
    if not os.path.exists(cfg_path):
        return {"status": "missing", "message": ".editorconfig not found"}
    with open(cfg_path) as f:
        content = f.read()
    sections = []
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("[") and line.endswith("]"):
            sections.append(line)
    return {
        "status": "ok",
        "sections": sections,
        "lines": len(content.splitlines()),
        "message": f"Valid: {len(sections)} section(s)",
    }


# ---------------------------------------------------------------------------
# Main — register all tools
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP(
        "tooling-config",
        description="Project tooling: pre-commit, git-cliff (changelog), .gitignore, .gitmodules, .editorconfig",
    )

    # pre-commit
    @mcp.tool
    def precommit_init(project_root: str | None = None) -> dict:
        """Create .pre-commit-config.yaml with basic hooks."""
        return _precommit_init(project_root)

    @mcp.tool
    def precommit_install(project_root: str | None = None) -> dict:
        """Run pre-commit install."""
        return _precommit_install(project_root)

    @mcp.tool
    def precommit_run(project_root: str | None = None, all_files: bool = True, hook: str = "") -> dict:
        """Run pre-commit. all_files=true runs on all files; pass hook name to run specific hook."""
        return _precommit_run(project_root, all_files, hook)

    # changelog
    @mcp.tool
    def changelog_init(project_root: str | None = None) -> dict:
        """Create cliff.toml for git-cliff changelog generation."""
        return _changelog_init(project_root)

    @mcp.tool
    def changelog_generate(project_root: str | None = None, unreleased: bool = True) -> dict:
        """Generate CHANGELOG.md from git history via git-cliff."""
        return _changelog_generate(project_root, unreleased)

    # .gitignore
    @mcp.tool
    def gitignore_init(project_root: str | None = None) -> dict:
        """Create .gitignore with Python/JS common ignores."""
        return _gitignore_init(project_root)

    @mcp.tool
    def gitignore_validate(project_root: str | None = None) -> dict:
        """Validate .gitignore exists and checks for common patterns."""
        return _gitignore_validate(project_root)

    # .gitmodules
    @mcp.tool
    def gitmodules_validate(project_root: str | None = None) -> dict:
        """Validate .gitmodules syntax and list submodules."""
        return _gitmodules_validate(project_root)

    # .editorconfig
    @mcp.tool
    def editorconfig_init(project_root: str | None = None) -> dict:
        """Create .editorconfig with standard defaults."""
        return _editorconfig_init(project_root)

    @mcp.tool
    def editorconfig_validate(project_root: str | None = None) -> dict:
        """Validate .editorconfig exists and has sections."""
        return _editorconfig_validate(project_root)

    mcp.run(transport="stdio")
