#!/usr/bin/env python3
"""Plugins Judge — score ~/AppData/Local/hermes/plugins/* on 5 dimensions (max 100).

Usage:
    python judge.py --plugins-dir ~/AppData/Local/hermes/plugins [--output PATH]
"""
import argparse
import json
import sys
from pathlib import Path
from datetime import datetime

REQUIRED_FIELDS = ["name", "version", "description", "author"]
PLATFORMS = {"windows", "macos", "linux"}


def parse_yaml_simple(text: str) -> dict:
    """Minimal YAML parser for plugin.yaml flat structure."""
    out = {}
    current_list_key = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and current_list_key:
            out.setdefault(current_list_key, []).append(line[4:].strip())
            continue
        if ":" in line:
            k, v = line.split(":", 1)
            k = k.strip()
            v = v.strip()
            if not v:
                current_list_key = k
                out.setdefault(k, [])
            else:
                current_list_key = None
                out[k] = v.strip('"').strip("'")
    return out


def score_one(pdir: Path) -> dict:
    yaml_path = pdir / "plugin.yaml"
    if not yaml_path.exists():
        yaml_path = pdir / "plugin.yml"
    if not yaml_path.exists():
        return {
            "dir": str(pdir),
            "score": 0,
            "rating": "FAIL",
            "dims": {k: 0 for k in ["manifest", "hooks", "tools", "platforms", "code"]},
            "error": "no plugin.yaml",
        }
    try:
        text = yaml_path.read_text(encoding="utf-8", errors="ignore")
        # Use yaml if available; else fallback
        try:
            import yaml
            manifest = yaml.safe_load(text) or {}
        except ImportError:
            manifest = parse_yaml_simple(text)
    except Exception as e:
        return {"dir": str(pdir), "score": 0, "rating": "FAIL", "error": str(e)[:200]}

    # Manifest Validity (20)
    missing = [f for f in REQUIRED_FIELDS if not manifest.get(f)]
    manifest_pts = max(20 - len(missing) * 5, 0)

    # Hooks Coverage (20)
    hooks_dir = pdir / "hooks"
    hook_scripts = list(hooks_dir.glob("*.sh")) + list(hooks_dir.glob("*.py")) if hooks_dir.exists() else []
    declared_hooks = manifest.get("hooks", None)
    if declared_hooks is None:
        declared_hooks = []
    elif isinstance(declared_hooks, str):
        declared_hooks = [declared_hooks]
    if hook_scripts and declared_hooks:
        hooks_pts = 20
    elif hook_scripts or declared_hooks:
        hooks_pts = 10
    elif "hooks" in manifest:
        hooks_pts = 20  # explicitly declared empty = intentional design
    else:
        hooks_pts = 16  # plugins without hooks are OK

    # Tools Surface (20)
    tools = manifest.get("tools", None)
    if tools is None:
        tools = []
    elif isinstance(tools, str):
        tools = [tools]
    tools_dir = pdir / "tools"
    tool_files = list(tools_dir.glob("*.py")) + list(tools_dir.glob("*.sh")) if tools_dir.exists() else []
    if not tools and not tool_files:
        tools_pts = 16  # plugin without tools is OK
    elif tools and tool_files:
        tools_pts = 20
    else:
        tools_pts = 10

    # Platforms (20)
    platforms_raw = manifest.get("platforms", []) or []
    if isinstance(platforms_raw, str):
        platforms_raw = [platforms_raw]
    platforms = {p.lower() for p in platforms_raw}
    if platforms & PLATFORMS:
        platforms_pts = 20
    elif platforms:
        platforms_pts = 12
    else:
        platforms_pts = 8  # not declared

    # Code Quality (20): hook script passes bash -n or py_compile
    code_pts = 20
    for hs in hook_scripts[:5]:  # sample 5
        import subprocess
        try:
            if hs.suffix == ".py":
                r = subprocess.run([sys.executable, "-m", "py_compile", str(hs)],
                                   capture_output=True, text=True, timeout=10)
            else:
                r = subprocess.run(["bash", "-n", str(hs)],
                                   capture_output=True, text=True, timeout=10)
            if r.returncode != 0:
                code_pts -= 5
        except Exception:
            code_pts -= 5

    total = manifest_pts + hooks_pts + tools_pts + platforms_pts + code_pts
    return {
        "dir": str(pdir),
        "name": manifest.get("name", pdir.name),
        "version": manifest.get("version", "?"),
        "score": total,
        "rating": "PASS" if total >= 70 else "WARN" if total >= 50 else "FAIL",
        "dims": {
            "manifest": manifest_pts,
            "hooks": hooks_pts,
            "tools": tools_pts,
            "platforms": platforms_pts,
            "code": code_pts,
        },
        "platforms": sorted(platforms),
        "hooks_count": len(hook_scripts),
        "tools_count": len(tool_files),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Plugins Judge")
    ap.add_argument("--plugins-dir", default=None,
                    help="plugins dir (default: $LOCALAPPDATA/hermes/plugins)")
    ap.add_argument("--output", default="judge_results/plugins_audit")
    ap.add_argument("--threshold", type=int, default=70)
    args = ap.parse_args()

    if args.plugins_dir is None:
        import os
        local = os.environ.get("LOCALAPPDATA", str(Path.home() / "AppData/Local"))
        args.plugins_dir = str(Path(local) / "hermes/plugins")

    pdir = Path(args.plugins_dir)
    if not pdir.is_dir():
        print(f"ERR: plugins dir not found: {pdir}", file=sys.stderr)
        return 1

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    results = []
    for sub in sorted(pdir.iterdir()):
        if sub.is_dir() and (sub / "plugin.yaml").exists() or (sub / "plugin.yml").exists():
            results.append(score_one(sub))

    avg = sum(r["score"] for r in results) / max(len(results), 1)
    passed = sum(1 for r in results if r["score"] >= args.threshold)

    (out.with_suffix(".json")).write_text(json.dumps({
        "ts": datetime.utcnow().isoformat() + "Z",
        "dir": str(pdir),
        "threshold": args.threshold,
        "count": len(results),
        "avg": round(avg, 1),
        "passed": passed,
        "results": results,
    }, indent=2))

    md = [
        f"# Plugins Audit — {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        f"Dir: `{pdir}` | Threshold: {args.threshold}",
        f"Count: {len(results)} | Avg: {avg:.1f} | Passed: {passed}",
        "",
        "| Plugin | Version | Score | Rating | Manifest | Hooks | Tools | Platforms | Code |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in results:
        d = r["dims"]
        md.append(
            f"| `{r.get('name', Path(r['dir']).name)}` | {r.get('version', '?')} | "
            f"{r['score']} | {r['rating']} | {d['manifest']} | {d['hooks']} | "
            f"{d['tools']} | {d['platforms']} | {d['code']} |"
        )
    (out.with_suffix(".md")).write_text("\n".join(md) + "\n")
    print(f"Plugins Judge: {len(results)} files, avg {avg:.1f}, passed {passed}/{len(results)}")
    print(f"Report: {out.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())