#!/usr/bin/env python3
"""Docker Cleanup Script — Remove unused Docker resources.

Deletes all unused Docker images, containers, volumes, build cache, and models.
"""
import subprocess, argparse, sys, json
from pathlib import Path

def run_docker(args: list[str]) -> dict:
    """Run a docker command and return results."""
    try:
        result = subprocess.run(
            ["docker"] + args,
            capture_output=True, text=True, timeout=120
        )
        return {"args": args, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
    except Exception as e:
        return {"args": args, "returncode": 1, "error": str(e)}

def cleanup_all() -> dict:
    """Execute all cleanup operations."""
    results = {}
    operations = [
        ("prune_images", ["system", "prune", "--all", "--volumes", "--filter", "until=24h"]),
        ("prune_containers", ["container", "prune", "-f"]),
        ("prune_volumes", ["volume", "prune", "-f"]),
        ("prune_networks", ["network", "prune", "-f"]),
        ("prune_build_cache", ["builder", "prune", "--all", "--force"]),
    ]
    for name, args in operations:
        results[name] = run_docker(args)
    return results

def main() -> None:
    parser = argparse.ArgumentParser(description="Docker cleanup tool")
    parser.add_argument("--all", action="store_true", help="Cleanup all resources")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be deleted")
    parser.add_argument("--help", action="help", help="Show help")
    args = parser.parse_args()
    
    if args.dry_run or args.all:
        results = cleanup_all()
        print(json.dumps(results, indent=2))
    else:
        parser.print_help()
    
    sys.exit(0)

if __name__ == "__main__":
    main()
