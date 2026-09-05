#!/usr/bin/env python3
"""Build and verify safe Hermes quick commands for root scripts.

The generated commands invoke this module in ``audit`` mode. They validate a
script exists and parses, but never execute the target script's business logic.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

SUPPORTED_SUFFIXES = {".py", ".sh", ".bash", ".ps1", ".ts", ".js"}
EXCLUDED_DIRS = {"node_modules", "__pycache__"}
DEFAULT_HERMES_HOME = Path.home() / "AppData" / "Local" / "hermes"
PRESERVED_COMMANDS: dict[str, dict[str, str]] = {
    "diff": {
        "type": "exec",
        "command": "cd ~/Desktop/SandBox && git diff --stat origin/development...HEAD",
    },
    "gc": {"type": "alias", "target": "/commit"},
    "log": {
        "type": "exec",
        "command": "cd ~/Desktop/SandBox && git log --oneline -10",
    },
    "pr": {
        "type": "exec",
        "command": "cd ~/Desktop/SandBox && git branch --show-current && git log origin/development..HEAD --oneline",
    },
    "st": {
        "type": "exec",
        "command": "cd ~/Desktop/SandBox && git status --short | head -30",
    },
    "tree": {
        "type": "exec",
        "command": "ls -d ~/Desktop/SandBox/projects/*/ | sed 's|.*/projects/||;s|/||'",
    },
    "ws": {"type": "exec", "command": "pwd"},
}


def hermes_home() -> Path:
    """Return the configured Hermes home without requiring credentials."""
    return Path(os.environ.get("HERMES_HOME", DEFAULT_HERMES_HOME)).expanduser()


def scripts_root() -> Path:
    """Return the root script directory used for inventory and audits."""
    return Path(
        os.environ.get("HERMES_SCRIPTS_DIR", hermes_home() / "scripts")
    ).expanduser()


def discover_scripts(root: Path) -> list[Path]:
    """Return sorted, first-party scripts directly under *root*."""
    if not root.is_dir():
        raise FileNotFoundError(f"Scripts directory not found: {root}")
    return sorted(
        (
            path
            for path in root.iterdir()
            if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES
        ),
        key=lambda path: path.name.casefold(),
    )


def command_key(stem: str) -> str:
    """Normalize a filename stem into a slash-command-safe key."""
    key = re.sub(r"[^a-z0-9]+", "-", stem.casefold()).strip("-")
    return key or "script"


def load_existing(path: Path | None) -> dict[str, dict[str, str]]:
    """Load a JSON quick-command mapping or return preserved defaults."""
    if path is None:
        return {key: value.copy() for key, value in PRESERVED_COMMANDS.items()}
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("Existing quick commands must be a JSON object")
    return value


def wrapper_command(script_index: int, wrapper: Path) -> dict[str, str]:
    """Build one non-destructive exec command for a target script."""
    command = f'python "{wrapper.as_posix()}" audit -i {script_index}'
    return {"type": "exec", "command": command}


def bash_executable() -> str | None:
    """Return a working Bash executable, preferring Git Bash on Windows."""
    configured = os.environ.get("HERMES_BASH")
    candidates = [
        configured,
        r"C:/Program Files/Git/usr/bin/bash.exe",
        r"C:/Program Files/Git/bin/bash.exe",
        shutil.which("bash"),
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    return None


def build_registry(
    scripts: list[Path], existing: dict[str, dict[str, str]], wrapper: Path
) -> dict[str, dict[str, str]]:
    """Merge generated audit commands with existing user commands."""
    wrapper_text = wrapper.as_posix().replace("\\\\", "/").casefold()
    registry: dict[str, dict[str, str]] = {}
    for key, value in existing.items():
        command = value.get("command", "") if isinstance(value, dict) else ""
        normalized = command.replace("\\\\", "/").casefold()
        stale_generated = (
            isinstance(value, dict)
            and value.get("type") == "exec"
            and (wrapper_text in normalized or "hermes_quick_commands.py" in normalized)
            and re.search(r"(?:^|\s)(?:audit|a)(?:\s|$)", command, re.IGNORECASE)
        )
        if not stale_generated:
            registry[key] = value.copy() if isinstance(value, dict) else value
    used = set(registry)
    for script_index, script in enumerate(scripts, start=1):
        base = command_key(script.stem)
        key = base
        if key in used:
            key = f"script-{base}"
        suffix = 2
        while key in used:
            key = f"script-{base}-{suffix}"
            suffix += 1
        registry[key] = wrapper_command(script_index, wrapper)
        used.add(key)
    return dict(sorted(registry.items()))


def audit_script(name: str, root: Path) -> dict[str, Any]:
    """Check one script's existence and syntax without executing it."""
    target = root / name
    result: dict[str, Any] = {
        "script": name,
        "exists": target.is_file(),
        "suffix": target.suffix.lower(),
        "syntax_ok": False,
        "detail": "",
    }
    if not target.is_file() or target.parent != root:
        result["detail"] = "script is missing or not directly under scripts root"
        return result
    try:
        if target.suffix.lower() == ".py":
            ast.parse(target.read_text(encoding="utf-8"), filename=str(target))
        elif target.suffix.lower() in {".sh", ".bash"}:
            bash = bash_executable()
            if bash is None:
                result["detail"] = "no working Bash executable found"
                return result
            check = subprocess.run(
                [bash, "-n", str(target)],
                capture_output=True,
                text=True,
                timeout=15,
            )
            if check.returncode:
                result["detail"] = check.stderr.strip()[:400]
                return result
        # PowerShell parsing is intentionally existence-only on this host.
        result["syntax_ok"] = True
    except (OSError, SyntaxError, subprocess.SubprocessError) as exc:
        result["detail"] = str(exc)[:400]
    return result


def generated_command_items(
    registry: dict[str, Any], wrapper: Path
) -> list[tuple[str, str]]:
    """Return generated wrapper commands without returning arbitrary exec entries."""
    wrapper_text = wrapper.as_posix().replace("\\\\", "/").casefold()
    items: list[tuple[str, str]] = []
    for key, value in registry.items():
        if not isinstance(value, dict) or value.get("type") != "exec":
            continue
        command = value.get("command")
        if not isinstance(command, str):
            continue
        if wrapper_text in command.replace("\\\\", "/").casefold():
            items.append((key, command))
    return items


def smoke_command(key: str, command: str) -> dict[str, Any]:
    """Execute one generated wrapper command, never the target script itself."""
    try:
        tokens = shlex.split(command, posix=True)
        if not tokens:
            return {"key": key, "passed": False, "detail": "empty command"}
        executable = shutil.which(tokens[0])
        if executable is None:
            return {"key": key, "passed": False, "detail": f"executable not found: {tokens[0]}"}
        result = subprocess.run(
            [executable, *tokens[1:]],
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        return {
            "key": key,
            "passed": result.returncode == 0,
            "returncode": result.returncode,
            "detail": (result.stderr or result.stdout).strip()[-400:],
        }
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        return {"key": key, "passed": False, "detail": str(exc)[:400]}


def validate_registry(registry: dict[str, Any], scripts: list[Path], wrapper: Path) -> list[str]:
    """Return actionable registry coverage and shape errors."""
    issues: list[str] = []
    script_names = {path.name for path in scripts}
    script_by_index = {index: path.name for index, path in enumerate(scripts, start=1)}
    seen_targets: set[str] = set()
    for key, value in registry.items():
        if not isinstance(key, str) or not key:
            issues.append("registry contains an empty or non-string key")
            continue
        if not isinstance(value, dict):
            issues.append(f"{key}: command must be an object")
            continue
        kind = value.get("type")
        if kind not in {"exec", "alias"}:
            issues.append(f"{key}: unsupported type {kind!r}")
            continue
        if kind == "alias" and not isinstance(value.get("target"), str):
            issues.append(f"{key}: alias target is missing")
        if kind == "exec":
            command = value.get("command")
            if not isinstance(command, str) or not command.strip():
                issues.append(f"{key}: exec command is missing")
                continue
            wrapper_text = wrapper.as_posix().replace("\\\\", "/").casefold()
            command_text = command.replace("\\\\", "/").casefold()
            is_generated = key.startswith("script-") or wrapper_text in command_text
            if not is_generated:
                continue
            match = re.search(r'(?:--script|-s)\s+"?([A-Za-z0-9._-]+)"?', command)
            index_match = re.search(r'(?:--index|-i)\s+(\d+)', command)
            if not match:
                if not index_match:
                    issues.append(f"{key}: generated command lacks a script target")
                    continue
                index = int(index_match.group(1))
                target = script_by_index.get(index)
                if target is None:
                    issues.append(f"{key}: script index {index} is not inventoried")
                    continue
            else:
                target = match.group(1)
                if target not in script_names:
                    issues.append(f"{key}: target {target!r} is not inventoried")
                    continue
            if target in seen_targets:
                issues.append(f"duplicate generated target: {target}")
            else:
                seen_targets.add(target)
            if wrapper_text not in command_text:
                issues.append(f"{key}: command does not invoke the wrapper")
            if not re.search(r"(?:^|\s)audit(?:\s|$)", command, re.IGNORECASE):
                issues.append(f"{key}: command does not use audit mode")
    missing = script_names - seen_targets
    issues.extend(f"missing quick command for {name}" for name in sorted(missing))
    return issues


def env_inventory(repo: Path, root: Path) -> list[dict[str, Any]]:
    """List env files and variable names without emitting secret values."""
    paths = sorted(
        {
            path
            for base, scope in ((repo, "repo"), (root, "hermes"))
            for path in base.rglob(".env*")
            if path.is_file()
            and "node_modules" not in path.parts
            and ".git" not in path.parts
        },
        key=lambda path: str(path).casefold(),
    )
    records: list[dict[str, Any]] = []
    for path in paths:
        scope = "repo" if repo in path.parents or path == repo else "hermes"
        names: list[str] = []
        try:
            for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
                match = re.match(r"\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=", line)
                if match:
                    names.append(match.group(1))
        except OSError:
            names = []
        records.append(
            {
                "path": str(path),
                "scope": scope,
                "kind": "example" if ".example" in path.name else "runtime",
                "variable_names": sorted(set(names)),
            }
        )
    return records


def parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--scripts-dir", type=Path, default=None)
    sub = ap.add_subparsers(dest="command", required=True)
    sub.add_parser("inventory")
    generate = sub.add_parser("generate")
    generate.add_argument("--existing-file", type=Path)
    generate.add_argument("--wrapper", type=Path, default=None)
    audit = sub.add_parser("audit", aliases=["a"])
    target = audit.add_mutually_exclusive_group(required=True)
    target.add_argument("-s", "--script")
    target.add_argument("-i", "--index", type=int)
    audit.add_argument("--json", action="store_true")
    verify = sub.add_parser("verify-registry")
    verify.add_argument("--registry", type=Path, required=True)
    verify.add_argument("--wrapper", type=Path, default=None)
    smoke = sub.add_parser("smoke")
    smoke.add_argument("--registry", type=Path, required=True)
    env = sub.add_parser("env-inventory")
    env.add_argument("--repo", type=Path, default=Path.cwd())
    return ap


def main(argv: list[str] | None = None) -> int:
    """Execute one inventory, generation, audit, or verification command."""
    args = parser().parse_args(argv)
    root = args.scripts_dir or scripts_root()
    wrapper = getattr(args, "wrapper", None) or root / Path(__file__).name
    scripts = discover_scripts(root)

    if args.command == "inventory":
        print(json.dumps({"scripts_dir": str(root), "scripts": [p.name for p in scripts]}, indent=2))
        return 0
    if args.command == "generate":
        existing = load_existing(args.existing_file)
        print(json.dumps(build_registry(scripts, existing, wrapper), indent=2))
        return 0
    if args.command in {"audit", "a"}:
        script_name = args.script
        if args.index is not None:
            if args.index < 1 or args.index > len(scripts):
                result = {"exists": False, "syntax_ok": False, "detail": "script index is out of range"}
            else:
                script_name = scripts[args.index - 1].name
                result = audit_script(script_name, root)
        else:
            result = audit_script(script_name, root)
        result.setdefault("script", script_name or f"index:{args.index}")
        output = json.dumps(result, indent=2) if args.json else f"{script_name}: {result['detail'] or 'OK'}"
        print(output)
        return 0 if result["exists"] and result["syntax_ok"] else 1
    if args.command == "verify-registry":
        registry = json.loads(args.registry.read_text(encoding="utf-8"))
        issues = validate_registry(registry, scripts, wrapper)
        print(json.dumps({"scripts": len(scripts), "commands": len(registry), "issues": issues}, indent=2))
        return 0 if not issues else 1
    if args.command == "smoke":
        registry = json.loads(args.registry.read_text(encoding="utf-8"))
        generated = generated_command_items(registry, wrapper)
        results = [smoke_command(key, command) for key, command in generated]
        failed = [item for item in results if not item["passed"]]
        print(
            json.dumps(
                {
                    "tested": len(results),
                    "commands_executed": True,
                    "failed": failed,
                },
                indent=2,
            )
        )
        return 0 if results and not failed else 1
    if args.command == "env-inventory":
        print(json.dumps(env_inventory(args.repo.resolve(), hermes_home().resolve()), indent=2))
        return 0
    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
