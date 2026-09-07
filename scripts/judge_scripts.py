#!/usr/bin/env python3
"""Scripts Judge — score scripts/* on 5 dimensions (max 100).

Usage:
    python judge.py --scripts-dir scripts [--output PATH] [--threshold N]
"""
import argparse
import json
import re
import shlex
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from datetime import datetime, timezone

EXT_LANG = {
    ".py": "python",
    ".sh": "bash",
    ".bash": "bash",
    ".ts": "ts",
    ".js": "js",
    ".ps1": "ps1",
}

QUICK_TARGET = re.compile(r'(?:--script|-s)\s+"?([A-Za-z0-9._-]+)"?')
QUICK_INDEX = re.compile(r'(?:--index|-i)\s+(\d+)')


def detect_lang(p: Path) -> str:
    return EXT_LANG.get(p.suffix.lower(), "unknown")


def bash_executable() -> str | None:
    """Return a working Bash executable, preferring Git Bash on Windows."""
    candidates = [
        r"C:/Program Files/Git/usr/bin/bash.exe",
        r"C:/Program Files/Git/bin/bash.exe",
        shutil.which("bash"),
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    return None


def syntax_check(p: Path, lang: str) -> tuple[bool, str]:
    try:
        if lang == "python":
            r = subprocess.run(
                [sys.executable, "-m", "py_compile", str(p)],
                capture_output=True, text=True, timeout=15,
            )
            return r.returncode == 0, r.stderr[:200]
        if lang in {"bash", "sh"}:
            bash = bash_executable()
            if bash is None:
                return False, "no working Bash executable found"
            r = subprocess.run(
                [bash, "-n", str(p)],
                capture_output=True, text=True, timeout=15,
            )
            return r.returncode == 0, r.stderr[:200]
        return True, ""  # ts/js/ps1: skip in bash env
    except Exception as e:
        return False, str(e)[:200]


def score_one(p: Path) -> dict:
    text = p.read_text(encoding="utf-8", errors="ignore")
    lang = detect_lang(p)

    # Syntax (20)
    ok, err = syntax_check(p, lang)
    syn_pts = 20 if ok else 4

    # CLI Surface (20): argparse / getopts / --help
    cli_pts = 0
    if lang == "python" and ("argparse" in text or "ArgumentParser" in text):
        cli_pts = 20
    elif "def main()" in text and '__name__' in text:
        cli_pts = 12
    elif lang == "bash" and re.search(r"getopts|--help|\-h\)", text):
        cli_pts = 14

    # Error Handling (20): try/except, set -e, exit codes
    eh_pts = 0
    if lang == "python":
        if "except" in text and "except:" not in text:
            eh_pts += 8
        if "sys.exit" in text or "return" in text:
            eh_pts += 6
        if "logging" in text or "print(" in text:
            eh_pts += 6
    elif lang == "bash":
        if "set -e" in text or "set -euo pipefail" in text:
            eh_pts += 12
        if "exit " in text:
            eh_pts += 8

    eh_pts = min(eh_pts, 20)

    # Documentation (20): docstrings + comments
    doc_pts = 0
    if text.startswith('"""') or text.startswith("'''") or text.startswith("#!"):
        doc_pts += 8
    if '"""' in text or "'''" in text:
        doc_pts += 6
    if re.search(r'""".*?"""', text, re.DOTALL) or re.search(r"# .*?\n", text):
        doc_pts += 6
    doc_pts = min(doc_pts, 20)

    # DRY (20): line count + helper imports
    n = len(text.splitlines())
    if n <= 100:
        dry_pts = 20
    elif n <= 300:
        dry_pts = 16
    elif n <= 600:
        dry_pts = 10
    else:
        dry_pts = 5

    total = syn_pts + cli_pts + eh_pts + doc_pts + dry_pts
    return {
        "file": str(p),
        "score": total,
        "rating": "PASS" if total >= 70 else "WARN" if total >= 50 else "FAIL",
        "dims": {
            "syntax": syn_pts,
            "cli": cli_pts,
            "error_handling": eh_pts,
            "documentation": doc_pts,
            "dry": dry_pts,
        },
        "lang": lang,
        "syntax_ok": ok,
        "lines": n,
        "syntax_error": err if not ok else "",
    }


def _registry_commands(registry: dict) -> dict:
    """Accept both raw quick_commands and wrapped registry JSON."""
    commands = registry.get("quick_commands", registry)
    return commands if isinstance(commands, dict) else {}


def _smoke_generated_command(key: str, command: str, cwd: Path, timeout: int) -> dict:
    """Run one approved quick-command wrapper without exposing process output."""
    try:
        argv = shlex.split(command, posix=True)
        if not argv:
            return {"key": key, "status": "FAIL", "reason": "empty command"}
        result = subprocess.run(
            argv,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except (OSError, ValueError) as exc:
        return {"key": key, "status": "FAIL", "reason": type(exc).__name__}
    except subprocess.TimeoutExpired:
        return {"key": key, "status": "FAIL", "reason": f"timeout>{timeout}s"}
    if result.returncode:
        return {"key": key, "status": "FAIL", "reason": f"exit={result.returncode}"}
    return {"key": key, "status": "PASS", "returncode": 0}


def quick_command_check(
    sdir: Path,
    registry_path: Path,
    *,
    smoke: bool = True,
    timeout: int = 20,
) -> dict:
    """Validate complete coverage and smoke-test every generated wrapper command."""
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    commands = _registry_commands(registry)
    script_paths = sorted(
        (
            path
            for path in sdir.iterdir()
            if path.is_file() and path.suffix.lower() in EXT_LANG
        ),
        key=lambda path: path.name.casefold(),
    )
    scripts = {path.name for path in script_paths}
    targets: set[str] = set()
    generated: list[tuple[str, str]] = []
    issues: list[str] = []
    for key, value in commands.items():
        if not isinstance(value, dict) or value.get("type") != "exec":
            continue
        command = value.get("command", "")
        match = QUICK_TARGET.search(command)
        index_match = QUICK_INDEX.search(command)
        if not match and not index_match:
            continue
        if match:
            target = match.group(1)
        else:
            index = int(index_match.group(1))
            if index < 1 or index > len(script_paths):
                issues.append(f"{key}: script index {index} is out of range")
                continue
            target = script_paths[index - 1].name
        if target not in scripts:
            issues.append(f"{key}: target {target!r} is not in scripts root")
        elif target in targets:
            issues.append(f"duplicate registry target: {target}")
        targets.add(target)
        try:
            command_tokens = shlex.split(command)
        except ValueError:
            issues.append(f"{key}: malformed command quoting")
            continue
        if not any(
            Path(token.strip('\\"')).name.casefold() in {"hermes_quick_commands.py", "hq.py"}
            for token in command_tokens
        ):
            issues.append(f"{key}: generated entry does not invoke the approved wrapper")
        else:
            generated.append((str(key), command))
    issues.extend(f"missing registry entry: {name}" for name in sorted(scripts - targets))

    smoke_results: list[dict] = []
    if smoke and generated:
        with ThreadPoolExecutor(max_workers=min(8, len(generated))) as pool:
            futures = {
                pool.submit(_smoke_generated_command, key, command, sdir.parent, timeout): key
                for key, command in generated
            }
            for future in as_completed(futures):
                smoke_results.append(future.result())
        smoke_results.sort(key=lambda result: result["key"])
        issues.extend(
            f"{result['key']}: smoke failed ({result['reason']})"
            for result in smoke_results
            if result["status"] != "PASS"
        )

    return {
        "registry": str(registry_path),
        "scripts": len(scripts),
        "commands": len(commands),
        "generated": len(generated),
        "covered": len(targets),
        "smoke_enabled": smoke,
        "smoked": sum(result["status"] == "PASS" for result in smoke_results),
        "smoke_failed": sum(result["status"] != "PASS" for result in smoke_results),
        "issues": issues,
        "passed": not issues and len(targets) == len(scripts),
        "smoke_results": smoke_results,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Scripts Judge")
    ap.add_argument("--scripts-dir", default="scripts")
    ap.add_argument("--output", default="judge_results/scripts_audit")
    ap.add_argument("--threshold", type=int, default=70)
    ap.add_argument(
        "--quick-commands-json",
        type=Path,
        help="Generated/read-back Hermes quick_commands JSON to validate and smoke-test",
    )
    ap.add_argument(
        "--quick-command-timeout",
        type=int,
        default=20,
        help="seconds allowed for each generated wrapper command",
    )
    args = ap.parse_args()

    sdir = Path(args.scripts_dir)
    if not sdir.is_dir():
        print(f"ERR: scripts dir not found: {sdir}", file=sys.stderr)
        return 1

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    results = []
    for p in sorted(sdir.iterdir()):
        if not p.is_file() or p.suffix.lower() not in EXT_LANG:
            continue
        results.append(score_one(p))

    avg = sum(r["score"] for r in results) / max(len(results), 1)
    passed = sum(1 for r in results if r["score"] >= args.threshold)
    syntax_failed = sum(1 for r in results if not r["syntax_ok"])
    quick_check = None
    if args.quick_commands_json:
        try:
            quick_check = quick_command_check(
                sdir,
                args.quick_commands_json,
                timeout=args.quick_command_timeout,
            )
        except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
            quick_check = {
                "registry": str(args.quick_commands_json),
                "issues": [f"registry check failed: {exc}"],
                "passed": False,
            }

    (out.with_suffix(".json")).write_text(json.dumps({
        "ts": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "dir": str(sdir),
        "threshold": args.threshold,
        "count": len(results),
        "avg": round(avg, 1),
        "passed": passed,
        "syntax_failed": syntax_failed,
        "quick_commands": quick_check,
        "results": results,
    }, indent=2))

    md = [
        f"# Scripts Audit — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        f"Dir: `{sdir}` | Threshold: {args.threshold}",
        f"Count: {len(results)} | Avg: {avg:.1f} | Passed: {passed}",
        f"Syntax failures: {syntax_failed}",
        f"Quick-command registry: {'PASS' if quick_check is None or quick_check['passed'] else 'FAIL'}",
        "",
        "| File | Lang | Score | Rating | Syntax | CLI | Err | Doc | DRY |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in results:
        d = r["dims"]
        md.append(
            f"| `{Path(r['file']).name}` | {r['lang']} | {r['score']} | {r['rating']} | "
            f"{d['syntax']} | {d['cli']} | {d['error_handling']} | "
            f"{d['documentation']} | {d['dry']} |"
        )
    (out.with_suffix(".md")).write_text("\n".join(md) + "\n")
    print(f"Scripts Judge: {len(results)} files, avg {avg:.1f}, passed {passed}/{len(results)}")
    print(f"Report: {out.with_suffix('.md')}")
    return 0 if quick_check is None or quick_check["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())