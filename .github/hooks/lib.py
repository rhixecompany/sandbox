#!/usr/bin/env python3
"""Async shared library for Hermes hooks.

Provides:
- canonical path constants
- payload helpers
- colored stderr logging
- JSONL append
- JSONL reader
- subprocess/git helpers
- skip-flag resolution
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from _pathutil import resolve_path

HOOKS_ROOT = resolve_path(__file__).parent.parent
HERMES_HOME = Path(os.environ.get("HERMES_HOME", "") or Path.home() / "AppData" / "Local" / "hermes")
HERMES_LOGS = HERMES_HOME / "logs" / "hermes"
SKIP_PREFIX = "SKIP_"

_COLORS = {
    "red": "\033[0;31m",
    "green": "\033[0;32m",
    "yellow": "\033[1;33m",
    "blue": "\033[0;34m",
    "nc": "\033[0m",
}


def _log(color_key: str, *args: Any) -> None:
    prefix = f"{_COLORS[color_key]}[{color_key.upper()}]{_COLORS['nc']}"
    print(f"{prefix} {' '.join(str(a) for a in args)}", file=sys.stderr)


def log_debug(*args: Any) -> None:
    _log("blue", *args)


def log_info(*args: Any) -> None:
    _log("green", *args)


def log_warn(*args: Any) -> None:
    _log("yellow", *args)


def log_error(*args: Any) -> None:
    _log("red", *args)


def _now_iso() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


now_iso = _now_iso


def json_get(data: dict, key: str, default: str = "") -> str:
    try:
        value = data
        for part in key.lstrip(".").split("."):
            value = value[part]
        return "" if value is None else str(value)
    except (KeyError, TypeError, ValueError):
        return default


def read_payload() -> dict:
    try:
        raw = sys.stdin.read()
        return json.loads(raw) if raw.strip() else {}
    except (json.JSONDecodeError, Exception):
        return {}


def normalize_event(event: str) -> str:
    normalized = event.strip().lower().replace("-", "_").replace(" ", "_")
    return normalized or "unknown"


def resolve_hook_name_from_env(prefix: str, fallback: str) -> str:
    for key, _value in os.environ.items():
        if key == f"{SKIP_PREFIX}{fallback.upper()}":
            return fallback
        if key.startswith(SKIP_PREFIX) and key[len(SKIP_PREFIX) :].lower() == prefix:
            return key[len(SKIP_PREFIX) :].lower()
    return fallback


def is_skipped(prefix: str, fallback_name: str) -> bool:
    hook_name = resolve_hook_name_from_env(prefix, fallback_name)
    return os.environ.get(f"{SKIP_PREFIX}{hook_name.upper()}", "false").lower() == "true"


def skip_context(prefix: str, fallback_name: str) -> dict:
    hook_name = resolve_hook_name_from_env(prefix, fallback_name)
    return {
        "hook_name": hook_name,
        "skip": is_skipped(prefix, fallback_name),
        "skip_var": f"{SKIP_PREFIX}{hook_name.upper()}",
        "timestamp": _now_iso(),
    }


async def ensure_dir(path: Path) -> None:
    await asyncio.to_thread(path.mkdir, parents=True, exist_ok=True)


async def ensure_jsonl(path: Path) -> None:
    await ensure_dir(path.parent)
    if not path.exists():
        await asyncio.to_thread(path.write_text, "", encoding="utf-8")


async def write_jsonl(file: Path, record: dict) -> None:
    await ensure_jsonl(file)
    line = json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"

    def _write() -> None:
        with open(file, "a", encoding="utf-8") as f:
            f.write(line)

    await asyncio.to_thread(_write)


async def read_jsonl(file: Path) -> list[dict]:
    def _read() -> list[dict]:
        if not file.exists():
            return []
        records: list[dict] = []
        with open(file, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        return records

    return await asyncio.to_thread(_read)


async def run_cmd(
    *args: str,
    cwd: Path | None = None,
    timeout: int = 30,
) -> tuple[int, str, str]:
    proc = await asyncio.create_subprocess_exec(
        *args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=str(cwd) if cwd else None,
    )
    try:
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
    except TimeoutError:
        proc.kill()
        await proc.wait()
        return -1, "", f"TIMEOUT after {timeout}s"

    return (
        proc.returncode if proc.returncode is not None else 0,
        stdout.decode("utf-8", errors="replace") if stdout else "",
        stderr.decode("utf-8", errors="replace") if stderr else "",
    )


async def run_git(
    *args: str, cwd: Path | None = None, timeout: int = 30
) -> tuple[int, str, str]:
    return await run_cmd("git", *args, cwd=cwd, timeout=timeout)


# ---------------------------------------------------------------------------
# Session-start capture helpers
# ---------------------------------------------------------------------------

def resolve_user() -> str:
    """Best-effort OS user for the active session (env USERNAME/USER → getpass)."""
    for key in ("USERNAME", "USER", "LOGNAME"):
        value = os.environ.get(key)
        if value:
            return value
    try:
        import getpass

        return getpass.getuser()
    except Exception:
        return "unknown"


def resolve_profile() -> str:
    """Active Hermes profile: env override → config, else 'default'."""
    for key in ("HERMES_PROFILE", "HERMES_PROFILE_NAME", "PROFILE_NAME"):
        value = os.environ.get(key)
        if value:
            return value
    try:
        import yaml as _yaml  # type: ignore[import-untyped]

        cfg = _yaml.safe_load((HERMES_HOME / "config.yaml").read_text(encoding="utf-8"))
        if isinstance(cfg, dict):
            for probe in ("active_profile", "profile", "profiles"):
                val = cfg.get(probe)
                if isinstance(val, str) and val:
                    return val
    except Exception:
        pass
    return "default"


def load_model_config() -> dict:
    """Read canonical model + provider from config.yaml (fail-open)."""
    try:
        import yaml as _yaml  # type: ignore[import-untyped]

        cfg = _yaml.safe_load((HERMES_HOME / "config.yaml").read_text(encoding="utf-8"))
        model = cfg.get("model") or {}
        return {
            "model": str(model.get("default") or "unknown"),
            "provider": str(model.get("provider") or "unknown"),
        }
    except Exception:
        return {"model": "unknown", "provider": "unknown"}


def platform_snapshot() -> dict:
    """Static host snapshot: hostname, OS, python runtime."""
    import platform as _platform

    return {
        "hostname": _platform.node() or "unknown",
        "os": f"{_platform.system()} {_platform.release()}".strip() or "unknown",
        "python": _platform.python_version() or "unknown",
    }


async def git_snapshot(cwd: str | None) -> dict:
    """Best-effort git state of *cwd*: branch, head sha, dirty-file count.

    Every field degrades gracefully when *cwd* is not a git repo or git is
    unavailable — hooks must never fail because of git.
    """
    if not cwd:
        return {"git_branch": "", "git_sha": "", "git_dirty": 0}
    work = Path(cwd)
    code, branch, _err = await run_git("branch", "--show-current", cwd=work, timeout=10)
    code2, sha, _err2 = await run_git("rev-parse", "--short", "HEAD", cwd=work, timeout=10)
    code3, dirty_out, _err3 = await run_git(
        "status", "--porcelain", cwd=work, timeout=10
    )
    dirty = len([ln for ln in dirty_out.splitlines() if ln.strip()]) if code3 == 0 else 0
    return {
        "git_branch": branch.strip() if code == 0 and branch.strip() else "",
        "git_sha": sha.strip() if code2 == 0 and sha.strip() else "",
        "git_dirty": dirty,
    }
