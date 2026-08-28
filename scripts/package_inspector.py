#!/usr/bin/env python3
"""
package_inspector.py — Inspect packages/**/* and emit per-package summary.

Walks the `packages/` directory, identifies each package (TypeScript or Python),
parses its manifest (package.json or pyproject.toml), and emits a structured
summary to scripts/.runtime/packages.json.

Usage:
    python scripts/package_inspector.py
    python scripts/package_inspector.py --packages-dir packages --output scripts/.runtime/packages.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path


def parse_pyproject(text: str) -> dict:
    """Minimal pyproject.toml parser for the [project] table only."""
    result: dict = {}
    in_project = False
    in_deps = False
    current_array: list[str] | None = None
    for line in text.splitlines():
        s = line.strip()
        if s == "[project]":
            in_project = True
            in_deps = False
            continue
        if s.startswith("["):
            in_project = s == "[project]"
            in_deps = False
            continue
        if not in_project:
            continue
        if s.startswith("dependencies") and "=" in s and s.endswith("["):
            in_deps = True
            current_array = []
            continue
        if in_deps:
            if s == "]":
                in_deps = False
                if current_array is not None:
                    result.setdefault("dependencies", []).extend(current_array)
                current_array = None
                continue
            m = re.match(r'^"([^"]+)"\s*,?\s*$', s)
            if m and current_array is not None:
                current_array.append(m.group(1))
                continue
            m = re.match(r"^([\w\-.]+)\s*,?\s*$", s)
            if m and current_array is not None:
                current_array.append(m.group(1))
                continue
        if "=" in s and not s.startswith("#"):
            k, v = s.split("=", 1)
            k = k.strip()
            v = v.strip().strip('"').strip("'")
            if k in ("name", "version", "description", "requires-python"):
                result[k] = v
    return result


def parse_deps_array(deps: list) -> list[str]:
    """Normalize deps to list of strings. Handles both string and {version=...} forms."""
    out: list[str] = []
    for d in deps:
        if isinstance(d, str):
            out.append(d)
        elif isinstance(d, dict):
            name = d.get("name") or d.get("include-group") or "?"
            ver = d.get("version", "")
            out.append(f"{name}{ver}" if ver else name)
        else:
            out.append(str(d))
    return out


def inspect_typescript(pkg_dir: Path) -> dict | None:
    pkg_json = pkg_dir / "package.json"
    if not pkg_json.exists():
        return None
    try:
        data = json.loads(pkg_json.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None
    src_dir = pkg_dir / "src"
    entrypoints = [str(p.relative_to(pkg_dir)) for p in sorted(src_dir.glob("*.ts"))] if src_dir.exists() else []
    test_dir = pkg_dir / "test"
    tests = [str(p.relative_to(pkg_dir)) for p in sorted(test_dir.glob("*.test.ts"))] if test_dir.exists() else []
    src_files = sorted(p.name for p in (src_dir.glob("*.ts") if src_dir.exists() else []))
    return {
        "name": data.get("name", pkg_dir.name),
        "type": "typescript",
        "version": data.get("version", "0.0.0"),
        "description": data.get("description", ""),
        "license": data.get("license", ""),
        "author": data.get("author", ""),
        "package_manager": data.get("packageManager", ""),
        "type_module": data.get("type") == "module",
        "entrypoints": entrypoints,
        "source_files": src_files,
        "exports_public": _detect_ts_exports(src_dir),
        "dependencies": parse_deps_array(data.get("dependencies", [])),
        "dev_dependencies": parse_deps_array(data.get("devDependencies", [])),
        "scripts": data.get("scripts", {}),
        "tests": tests,
        "spec": "SPEC.md" if (pkg_dir / "SPEC.md").exists() else None,
        "plan": "PLAN.md" if (pkg_dir / "PLAN.md").exists() else None,
        "readme": "README.md" if (pkg_dir / "README.md").exists() else None,
    }


def _detect_ts_exports(src_dir: Path) -> list[str]:
    """Crude export-name detection: look for `export class|function|interface|const NAME`."""
    if not src_dir.exists():
        return []
    names: set[str] = set()
    pattern = re.compile(r"^export\s+(?:async\s+)?(?:class|function|interface|const|type|enum)\s+(\w+)", re.MULTILINE)
    for f in src_dir.glob("*.ts"):
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        for m in pattern.finditer(text):
            names.add(m.group(1))
    return sorted(names)


def inspect_python(pkg_dir: Path) -> dict | None:
    pyproject = pkg_dir / "pyproject.toml"
    if not pyproject.exists():
        return None
    try:
        text = pyproject.read_text(encoding="utf-8")
    except OSError:
        return None
    proj = parse_pyproject(text)
    src_dir = pkg_dir / "src"
    py_files = sorted(p.name for p in (src_dir.rglob("*.py") if src_dir.exists() else []) if p.name != "__init__.py")
    tests = sorted(str(p.relative_to(pkg_dir)) for p in (pkg_dir / "tests").rglob("test_*.py")) if (pkg_dir / "tests").exists() else []
    public = _detect_py_public(src_dir) if src_dir.exists() else []
    return {
        "name": proj.get("name", pkg_dir.name),
        "type": "python",
        "version": proj.get("version", "0.0.0"),
        "description": proj.get("description", ""),
        "requires_python": proj.get("requires-python", ""),
        "source_files": py_files,
        "exports_public": public,
        "dependencies": proj.get("dependencies", []),
        "dev_dependencies": [],
        "tests": tests,
        "spec": "SPEC.md" if (pkg_dir / "SPEC.md").exists() else None,
        "plan": "PLAN.md" if (pkg_dir / "PLAN.md").exists() else None,
        "readme": "README.md" if (pkg_dir / "README.md").exists() else None,
    }


def _detect_py_public(src_dir: Path) -> list[str]:
    names: set[str] = set()
    pattern = re.compile(r"^(?:async\s+)?def\s+(\w+)\s*\(|^class\s+(\w+)", re.MULTILINE)
    skip_prefixes = ("_", "test_")
    for f in src_dir.rglob("*.py"):
        if f.name.startswith("_") or f.name == "__init__.py":
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        for m in pattern.finditer(text):
            name = m.group(1) or m.group(2)
            if name and not name.startswith(skip_prefixes):
                names.add(name)
    return sorted(names)


def main() -> int:
    p = argparse.ArgumentParser(description="Inspect packages/ directory and emit summary")
    p.add_argument("--packages-dir", default="packages")
    p.add_argument("--output", default="scripts/.runtime/packages.json")
    args = p.parse_args()

    root = Path(args.packages_dir)
    if not root.exists():
        print(f"ERROR: packages dir not found: {root}", file=sys.stderr)
        return 2

    packages: list[dict] = []
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue
        info = inspect_typescript(child) or inspect_python(child)
        if info:
            info["path"] = str(child.resolve())
            packages.append(info)

    out = {
        "generated": datetime.now().isoformat(timespec="seconds"),
        "packages_dir": str(root.resolve()),
        "package_count": len(packages),
        "packages": packages,
    }
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✓ Wrote {out_path}")
    for pkg in packages:
        print(f"  - {pkg['name']:30s} {pkg['type']:10s} v{pkg['version']:8s} deps={len(pkg['dependencies'])} public={len(pkg['exports_public'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
