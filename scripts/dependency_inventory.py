#!/usr/bin/env python3
"""dependency_inventory.py — SandBox monorepo dependency inventory collector.

Scans every repo under ROOT (root, packages/*, projects/*) for Node and Python
manifests, collects DIRECT dependencies only (no lockfile transitive expansion),
and emits:

  results/dependency-inventory.json   (machine-readable master inventory)
  node-dependency.md                  (per-repo + unique index, direct deps)
  python-packages.md                  (per-repo + unique index, direct deps)
  technology-stacks.md                (per-repo stack summary)

Shared module: node-dep-audit.py / python-dep-audit.py / research-doc-verify.py
import `collect_inventory()` from this file (DRY).

Usage:
  python scripts/dependency_inventory.py            # JSON only
  python scripts/dependency_inventory.py --reports  # JSON + markdown reports

Stdlib only. Python >= 3.11 (tomllib).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = ROOT / "results"
JSON_OUT = RESULTS_DIR / "dependency-inventory.json"

EXCLUDE_SEGMENTS = {
    "node_modules", ".git", ".opencode", ".copilot", ".codex",
    "coderabbit_webhooks", ".hermes", ".github", "venv", ".venv",
    "myvenv", "__pycache__", "dist", "build", ".next", "patches",
}

FRAMEWORK_MAP = {
    "next": "Next.js", "react": "React", "react-dom": "React",
    "vue": "Vue", "@angular/core": "Angular",
    "django": "Django", "flask": "Flask", "fastapi": "FastAPI",
    "express": "Express", "electron": "Electron",
    "selenium": "Selenium", "scrapy": "Scrapy", "playwright": "Playwright",
    "pandas": "pandas", "numpy": "NumPy", "jupyter": "Jupyter",
    "streamlit": "Streamlit", "typer": "Typer", "click": "Click",
    "httpx": "httpx", "requests": "Requests", "aiohttp": "aiohttp",
    "pydantic": "Pydantic", "sqlalchemy": "SQLAlchemy",
    "torch": "PyTorch", "tensorflow": "TensorFlow",
    "capacitor": "Capacitor", "expo": "Expo",
    "typescript": "TypeScript", "tsx": "tsx",
}

DEV_TOOLING = {
    "pytest", "ruff", "mypy", "black", "isort", "flake8", "pre-commit",
    "tox", "nox", "setuptools", "wheel", "build", "twine", "sphinx",
    "coverage", "pytest-cov", "pytest-asyncio", "pytest-xdist",
    "eslint", "prettier", "typescript", "cspell", "markdownlint-cli2",
    "vitest", "jest", "mocha", "chai", "cypress", "playwright",
    "typescript-eslint", "ts-node", "nodemon", "husky", "lint-staged",
    "esbuild", "webpack", "vite", "rollup", "babel-loader",
}

VERSION_SPEC_RE = re.compile(r"^([A-Za-z0-9_.\-]+)(.*)$")


def _is_excluded(path: Path) -> bool:
    for seg in path.parts:
        if seg in EXCLUDE_SEGMENTS:
            return True
        if seg.startswith("{{") and seg.endswith("}}"):
            return True  # cookiecutter template dirs with Jinja placeholders
    return False


def _split_spec(spec: str) -> tuple[str, str]:
    """Split 'name==1.2.3' / 'name>=1' / 'name' into (name, specifier)."""
    spec = spec.strip().strip("\"'")
    if not spec:
        return "", ""
    # strip environment markers: name==1.0 ; python_version < "3.12"
    spec = re.split(r"\s*;\s*", spec)[0]
    m = VERSION_SPEC_RE.match(spec)
    if not m:
        return spec, ""
    return m.group(1), m.group(2).strip()


def find_manifests() -> tuple[list[Path], list[Path]]:
    pkg_json: list[Path] = []
    py_manifests: list[Path] = []
    for p in ROOT.rglob("*"):
        if _is_excluded(p) or p.is_dir():
            continue
        rel = p.relative_to(ROOT).as_posix()
        depth = len(p.relative_to(ROOT).parts)
        if depth > 4:
            continue
        if p.name == "package.json":
            pkg_json.append(p)
        elif p.name == "pyproject.toml" or (
            p.name.startswith("requirements") and p.name.endswith(".txt")
        ):
            py_manifests.append(p)
    pkg_json.sort(key=lambda p: p.as_posix())
    py_manifests.sort(key=lambda p: p.as_posix())
    return pkg_json, py_manifests


def parse_package_json(path: Path) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception:
        try:
            text = path.read_text(encoding="utf-8-sig")
            text = re.sub(r"^\s*//.*$", "", text, flags=re.M)
            data = json.loads(text)
        except Exception as e:
            print(f"  ! unparseable package.json: {path} ({e})", file=sys.stderr)
            return None
    if not isinstance(data, dict):
        return None
    return data


def parse_pyproject(path: Path) -> dict:
    deps: dict[str, list[tuple[str, str]]] = {"dependencies": [], "optional": []}
    try:
        data = tomllib.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as e:
        print(f"  ! unparseable pyproject.toml: {path} ({e})", file=sys.stderr)
        return deps
    proj = data.get("project", {})
    for d in proj.get("dependencies", []) or []:
        name, spec = _split_spec(d)
        if name:
            deps["dependencies"].append((name, spec))
    for group, items in (proj.get("optional-dependencies", {}) or {}).items():
        for d in items or []:
            name, spec = _split_spec(d)
            if name:
                deps["optional"].append((f"{name} (extra: {group})", spec))
    return deps


def parse_requirements(path: Path) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    try:
        lines = path.read_text(encoding="utf-8-sig").splitlines()
    except Exception as e:
        print(f"  ! unreadable requirements: {path} ({e})", file=sys.stderr)
        return out
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("-"):
            continue
        if line.startswith(("-e ", "--editable", "git+", "http://", "https://")):
            out.append((line.split("#")[0].strip(), ""))
            continue
        name, spec = _split_spec(line)
        if name:
            out.append((name, spec))
    return out


def _purpose(name: str) -> str:
    if name in DEV_TOOLING:
        return "dev tooling"
    return ""


def collect_inventory() -> dict:
    pkg_json, py_manifests = find_manifests()
    repos: dict[str, dict] = {}
    node_entries: list[dict] = []
    py_entries: list[dict] = []
    node_index: dict[str, dict] = {}
    py_index: dict[str, dict] = {}

    def add_node(name: str, spec: str, repo: str, kind: str) -> None:
        node_entries.append({"repo": repo, "name": name, "spec": spec, "kind": kind})
        idx = node_index.setdefault(name, {"specs": set(), "repos": set(), "kinds": set()})
        idx["specs"].add(spec or "*")
        idx["repos"].add(repo)
        idx["kinds"].add(kind)

    def add_py(name: str, spec: str, repo: str, kind: str = "direct") -> None:
        clean = name.split(" (extra:")[0]
        py_entries.append({"repo": repo, "name": clean, "spec": spec, "kind": kind})
        idx = py_index.setdefault(clean.lower(), {
            "name": clean, "specs": set(), "repos": set(), "kinds": set(),
        })
        idx["specs"].add(spec or "*")
        idx["repos"].add(repo)
        idx["kinds"].add(kind)

    def repo_key(p: Path) -> str:
        """Repo = parent dir of the manifest relative to ROOT ('root' for top-level)."""
        parent = p.relative_to(ROOT).parent
        return parent.as_posix() if parent.as_posix() != "." else "root"

    for p in pkg_json:
        repo = repo_key(p)
        data = parse_package_json(p)
        if data is None:
            continue
        repos.setdefault(repo, {"node": True, "python": False})["node"] = True
        for kind, section in (("dep", "dependencies"), ("devDep", "devDependencies")):
            for name, spec in (section in data and data[section] or {}).items():
                add_node(name, str(spec), repo, kind)

    for p in py_manifests:
        repo = repo_key(p)
        repos.setdefault(repo, {"node": False, "python": True})["python"] = True
        if p.name == "pyproject.toml":
            parsed = parse_pyproject(p)
            for name, spec in parsed["dependencies"]:
                add_py(name, spec, repo, "direct")
            for name, spec in parsed["optional"]:
                add_py(name, spec, repo, "optional")
        else:
            for name, spec in parse_requirements(p):
                add_py(name, spec, repo, "direct")

    # sort everything deterministically
    repos = {k: repos[k] for k in sorted(repos)}
    node_entries.sort(key=lambda e: (e["repo"], e["name"]))
    py_entries.sort(key=lambda e: (e["repo"], e["name"].lower()))
    node_index = {k: node_index[k] for k in sorted(node_index)}
    py_index = {k: py_index[k] for k in sorted(py_index)}

    # per-repo stack summary
    stacks: dict[str, dict] = {}
    for r in repos:
        stacks[r] = {"node": repos[r]["node"], "python": repos[r]["python"],
                     "frameworks": set(), "manager": None}
    for e in node_entries:
        if e["name"] in FRAMEWORK_MAP:
            stacks[e["repo"]]["frameworks"].add(FRAMEWORK_MAP[e["name"]])
        if e["name"] == "typescript":
            stacks[e["repo"]]["manager"] = "bun/npm (TS)"
    for e in py_entries:
        base = e["name"].replace(" (extra:", "").strip()
        if base in FRAMEWORK_MAP:
            stacks[e["repo"]]["frameworks"].add(FRAMEWORK_MAP[base])

    return {
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "repo_count": len(repos),
        "repos": repos,
        "stacks": {k: {**v, "frameworks": sorted(v["frameworks"])} for k, v in stacks.items()},
        "node_count": len(node_index),
        "node_entries": node_entries,
        "node_index": {k: {**v, "specs": sorted(v["specs"]), "repos": sorted(v["repos"]),
                           "kinds": sorted(v["kinds"]),
                           "purpose": _purpose(k)} for k, v in node_index.items()},
        "python_count": len(py_index),
        "python_entries": py_entries,
        "python_index": {k: {**v, "specs": sorted(v["specs"]), "repos": sorted(v["repos"]),
                             "kinds": sorted(v["kinds"])}
                         for k, v in py_index.items()},
    }


def slug(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s[:80] or "pkg"


def write_reports(inv: dict) -> list[Path]:
    ts = inv["generated"][:10]
    written: list[Path] = []

    # ---- technology-stacks.md ----
    lines = [f"# Technology Stacks — SandBox Monorepo", "",
             f"Generated: {ts} · Repos: {inv['repo_count']}",
             "", "| Repo | Node | Python | Runtime/Manager | Frameworks |", "|---|---|---|---|---|"]
    for repo, s in inv["stacks"].items():
        mgr = s["manager"] or ("bun/npm" if s["node"] else "uv/pip")
        lines.append(f"| `{repo}` | {'✓' if s['node'] else ''} | "
                     f"{'✓' if s['python'] else ''} | {mgr} | "
                     f"{', '.join(s['frameworks']) or '—'} |")
    ts_path = ROOT / "technology-stacks.md"
    ts_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    written.append(ts_path)

    # ---- node-dependency.md ----
    lines = [f"# Node.js Dependency Report — node-dependency.md", "",
             f"Generated: {ts} · Direct deps across {inv['repo_count']} repos · "
             f"Unique packages: {inv['node_count']} · Scope: npm/npx/bun/bunx tooling "
             f"(direct deps + devDeps, no transitive)",
             "", "## Per-Repo Dependencies", ""]
    cur = None
    for e in inv["node_entries"]:
        if e["repo"] != cur:
            cur = e["repo"]
            lines += [f"### `{cur}`", "",
                      "| Package | Version | Type |", "|---|---|---|"]
        lines.append(f"| {e['name']} | `{e['spec']}` | {e['kind']} |")
    lines += ["", "## Unique Package Index", "",
              "| Package | Versions | Type | Used by | Purpose | Cheat-Sheet |",
              "|---|---|---|---|---|---|"]
    for name, idx in inv["node_index"].items():
        sheet = f"`research/packages/node/{slug(name)}.md`"
        lines.append(f"| {name} | {', '.join('`'+s+'`' for s in idx['specs'])} | "
                     f"{'/'.join(idx['kinds'])} | {', '.join('`'+r+'`' for r in idx['repos'])} | "
                     f"{idx['purpose'] or '—'} | {sheet} |")
    lines += ["", "## Runtime Tooling Notes", "",
              "- **npm/npx**: `npm install <pkg>` / `npx <tool>` for npm-managed repos.",
              "- **bun/bunx**: `bun add <pkg>` / `bunx <tool>` for bun-managed repos (packageManager: bun).",
              "- Root sandbox uses bun@1.3.14; per-repo tooling listed in each repo table."]
    node_path = ROOT / "node-dependency.md"
    node_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    written.append(node_path)

    # ---- python-packages.md ----
    lines = [f"# Python Package Report — python-packages.md", "",
             f"Generated: {ts} · Direct packages across {inv['repo_count']} repos · "
             f"Unique packages: {inv['python_count']}",
             "", "## Per-Repo Packages", ""]
    cur = None
    for e in inv["python_entries"]:
        if e["repo"] != cur:
            cur = e["repo"]
            lines += [f"### `{cur}`", "",
                      "| Package | Version | Kind |", "|---|---|---|"]
        lines.append(f"| {e['name']} | `{e['spec']}` | {e['kind']} |")
    lines += ["", "## Unique Package Index", "",
              "| Package | Versions | Used by | Cheat-Sheet |",
              "|---|---|---|---|"]
    for key, idx in inv["python_index"].items():
        sheet = f"`research/packages/python/{slug(idx['name'])}.md`"
        lines.append(f"| {idx['name']} | {', '.join('`'+s+'`' for s in idx['specs'])} | "
                     f"{', '.join('`'+r+'`' for r in idx['repos'])} | {sheet} |")
    py_path = ROOT / "python-packages.md"
    py_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    written.append(py_path)

    return written


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reports", action="store_true", help="also write markdown reports")
    args = ap.parse_args()

    print(f"Scanning {ROOT} ...")
    inv = collect_inventory()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps(inv, indent=2, default=str), encoding="utf-8")
    print(f"Repos: {inv['repo_count']} | Node unique: {inv['node_count']} "
          f"({len(inv['node_entries'])} entries) | Python unique: {inv['python_count']} "
          f"({len(inv['python_entries'])} entries)")
    print(f"JSON: {JSON_OUT.relative_to(ROOT)}")
    if args.reports:
        for p in write_reports(inv):
            print(f"Wrote: {p.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())