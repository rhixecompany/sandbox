#!/usr/bin/env python3
"""Sync .env and config.yaml files between SandBox and Hermes root."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any


def find_env_files(root: Path, exclude_dirs: set[str] | None = None) -> list[Path]:
    """Find all .env files under root."""
    if exclude_dirs is None:
        exclude_dirs = {"node_modules", ".git", "__pycache__", ".ruff_cache", ".venv", "venv", "env"}
    
    env_files = []
    for path in root.rglob(".env*"):
        if path.is_file():
            # Check if any parent is in exclude_dirs
            if not any(excl in path.parts for excl in exclude_dirs):
                env_files.append(path)
    return sorted(env_files)


def find_config_files(root: Path, exclude_dirs: set[str] | None = None) -> list[Path]:
    """Find all config.yaml files under root."""
    if exclude_dirs is None:
        exclude_dirs = {"node_modules", ".git", "__pycache__", ".ruff_cache", ".venv", "venv", "env", "state-snapshots"}
    
    config_files = []
    for path in root.rglob("config.yaml"):
        if path.is_file():
            if not any(excl in path.parts for excl in exclude_dirs):
                config_files.append(path)
    return sorted(config_files)


def read_env_file(path: Path) -> dict[str, str]:
    """Read .env file and return variable dict (without values for security)."""
    vars_dict = {}
    try:
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key = line.split("=", 1)[0].strip()
                if key:
                    vars_dict[key] = "***REDACTED***"
    except OSError:
        pass
    return vars_dict


def read_config_yaml(path: Path) -> dict[str, Any]:
    """Read config.yaml file."""
    try:
        import yaml
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}


def inventory_env(sandbox_root: Path, hermes_root: Path) -> dict[str, Any]:
    """Inventory all .env files."""
    sandbox_envs = find_env_files(sandbox_root)
    hermes_envs = find_env_files(hermes_root)
    
    return {
        "sandbox": [
            {
                "path": str(p.relative_to(sandbox_root)),
                "absolute_path": str(p),
                "variables": list(read_env_file(p).keys())
            }
            for p in sandbox_envs
        ],
        "hermes": [
            {
                "path": str(p.relative_to(hermes_root)),
                "absolute_path": str(p),
                "variables": list(read_env_file(p).keys())
            }
            for p in hermes_envs
        ],
        "summary": {
            "sandbox_count": len(sandbox_envs),
            "hermes_count": len(hermes_envs),
            "total": len(sandbox_envs) + len(hermes_envs)
        }
    }


def inventory_config(sandbox_root: Path, hermes_root: Path) -> dict[str, Any]:
    """Inventory all config.yaml files."""
    # SandBox doesn't typically have config.yaml, but check anyway
    sandbox_configs = find_config_files(sandbox_root)
    hermes_configs = find_config_files(hermes_root)
    
    return {
        "sandbox": [
            {
                "path": str(p.relative_to(sandbox_root)),
                "absolute_path": str(p),
                "keys": list(read_config_yaml(p).keys())
            }
            for p in sandbox_configs
        ],
        "hermes": [
            {
                "path": str(p.relative_to(hermes_root)),
                "absolute_path": str(p),
                "keys": list(read_config_yaml(p).keys())
            }
            for p in hermes_configs
        ],
        "summary": {
            "sandbox_count": len(sandbox_configs),
            "hermes_count": len(hermes_configs),
            "total": len(sandbox_configs) + len(hermes_configs)
        }
    }


def sync_configs(source: Path, targets: list[Path], dry_run: bool = False) -> dict[str, Any]:
    """Sync config.yaml from source to targets."""
    results = {"synced": [], "failed": [], "skipped": []}
    
    if not source.exists():
        results["failed"].append({"target": str(source), "error": "Source not found"})
        return results
    
    source_content = source.read_text(encoding="utf-8")
    source_hash = hash(source_content)
    
    for target in targets:
        if target == source:
            results["skipped"].append({"target": str(target), "reason": "Is source"})
            continue
        
        try:
            if target.exists():
                target_content = target.read_text(encoding="utf-8")
                if hash(target_content) == source_hash:
                    results["skipped"].append({"target": str(target), "reason": "Already in sync"})
                    continue
            
            if not dry_run:
                target.parent.mkdir(parents=True, exist_ok=True)
                # Backup existing
                if target.exists():
                    backup = target.with_suffix(target.suffix + ".bak")
                    shutil.copy2(target, backup)
                shutil.copy2(source, target)
            
            results["synced"].append({"target": str(target)})
        except Exception as e:
            results["failed"].append({"target": str(target), "error": str(e)})
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Sync .env and config.yaml files")
    parser.add_argument("--sandbox-root", type=Path, default=Path("C:/Users/Alexa/Desktop/SandBox"))
    parser.add_argument("--hermes-root", type=Path, default=Path("C:/Users/Alexa/AppData/Local/hermes"))
    parser.add_argument("--inventory", action="store_true", help="Only inventory files")
    parser.add_argument("--sync-config", action="store_true", help="Sync config.yaml from root to profiles")
    parser.add_argument("--dry-run", action="store_true", help="Dry run for sync")
    parser.add_argument("--output", type=Path, help="Output JSON file")
    
    args = parser.parse_args()
    
    sandbox_root = args.sandbox_root.resolve()
    hermes_root = args.hermes_root.resolve()
    
    result = {}
    
    if args.inventory:
        print("Inventorying .env files...")
        result["env"] = inventory_env(sandbox_root, hermes_root)
        print(f"  SandBox: {result['env']['summary']['sandbox_count']} files")
        print(f"  Hermes: {result['env']['summary']['hermes_count']} files")
        
        print("Inventorying config.yaml files...")
        result["config"] = inventory_config(sandbox_root, hermes_root)
        print(f"  SandBox: {result['config']['summary']['sandbox_count']} files")
        print(f"  Hermes: {result['config']['summary']['hermes_count']} files")
    
    if args.sync_config:
        print("Syncing config.yaml from root to profiles...")
        source = hermes_root / "config.yaml"
        profile_configs = []
        profiles_dir = hermes_root / "profiles"
        if profiles_dir.exists():
            for profile_dir in profiles_dir.iterdir():
                if profile_dir.is_dir():
                    config_file = profile_dir / "config.yaml"
                    if config_file.exists():
                        profile_configs.append(config_file)
        
        sync_result = sync_configs(source, profile_configs, dry_run=args.dry_run)
        result["sync"] = sync_result
        print(f"  Synced: {len(sync_result['synced'])}")
        print(f"  Skipped: {len(sync_result['skipped'])}")
        print(f"  Failed: {len(sync_result['failed'])}")
        for f in sync_result["failed"]:
            print(f"    FAILED: {f['target']} - {f['error']}")
    
    if args.output:
        args.output.write_text(json.dumps(result, indent=2), encoding="utf-8")
        print(f"Output written to {args.output}")
    else:
        print(json.dumps(result, indent=2))
    
    return 0


if __name__ == "__main__":
    sys.exit(main())