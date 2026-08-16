#!/usr/bin/env python3
"""
mcp_preflight_check.py — Lightweight MCP server health check for hooks.

Checks which MCP servers are currently connected via `hermes mcp list`
output. Exits 0 if all critical servers are healthy, 1 otherwise.

Usage:
    python scripts/mcp_preflight_check.py                         # all servers
    python scripts/mcp_preflight_check.py --critical ast-grep,github,fetch  # critical subset only
    python scripts/mcp_preflight_check.py --hook                  # hook-compatible output
    python scripts/mcp_preflight_check.py --hook --critical ast-grep  # as hook

Exit codes:
    0 — all checked servers healthy
    1 — one or more critical servers down

Designed to run in < 5s. Does NOT spawn MCP servers — reads live Hermes state only.
"""

import json
import os
import subprocess
import sys
import time

HERMES_CONFIG = os.path.expanduser("~/AppData/Local/hermes/config.yaml")
ERROR_LOG = os.path.expanduser("~/AppData/Local/hermes/logs/errors.log")
LIVE_SERVER_CHECK_TIMEOUT = 8  # seconds

# Servers that are always critical if not explicitly specified
DEFAULT_CRITICAL = {"ast-grep", "github", "fetch", "sequential-thinking", "memory"}


def run_cmd(cmd, timeout=10):
    """Run a command and return (stdout, stderr, exit_code)."""
    try:
        proc = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
            cwd=os.path.expanduser("~")
        )
        stdout, stderr = proc.communicate(timeout=timeout)
        return stdout.strip(), stderr.strip(), proc.returncode
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
        return "", "timeout", -1
    except FileNotFoundError:
        return "", "command not found", -1


def get_connected_servers():
    """
    Query Hermes for currently connected MCP servers.
    Tries `hermes mcp list` first, falls back to reading config.
    Returns dict of {name: status_string}.
    """
    stdout, stderr, code = run_cmd(["hermes", "mcp", "list"],
                                    timeout=LIVE_SERVER_CHECK_TIMEOUT)

    connected = {}
    if code == 0 and stdout:
        # Parse: "ast-grep           ✓ enabled  7 tools"
        for line in stdout.splitlines():
            parts = line.strip().split()
            if len(parts) >= 3:
                name = parts[0].rstrip(":")
                status = " ".join(parts[1:])
                connected[name] = status
        return connected

    # Fallback: read config (less accurate, but always available)
    if os.path.exists(HERMES_CONFIG):
        import yaml
        with open(HERMES_CONFIG, encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
        for name, srv in cfg.get("mcp_servers", {}).items():
            if srv.get("enabled", False):
                connected[name] = "enabled (config)"
        return connected

    return connected


def log_error(message):
    """Append to errors.log for persistence."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{timestamp} WARNING mcp_preflight_check: {message}\n"
    try:
        os.makedirs(os.path.dirname(ERROR_LOG), exist_ok=True)
        with open(ERROR_LOG, "a", encoding="utf-8") as f:
            f.write(log_line)
    except OSError:
        pass  # best-effort logging


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="MCP preflight health check (hook-friendly)")
    parser.add_argument("--critical", help="Comma-separated critical server names")
    parser.add_argument("--hook", action="store_true",
                        help="Hook-compatible output (quiet pass, noisy fail)")
    args = parser.parse_args()

    # Determine critical set
    if args.critical:
        critical_set = set(s.strip() for s in args.critical.split(","))
    else:
        critical_set = DEFAULT_CRITICAL

    # Get current server state
    connected = get_connected_servers()
    if not connected:
        msg = "Cannot determine MCP server state (hermes mcp list failed)"
        log_error(msg)
        if args.hook:
            print(f"mcp_preflight FAIL: {msg}", file=sys.stderr)
        sys.exit(1)

    # Check each critical server
    failures = []
    for name in sorted(critical_set):
        status = connected.get(name, "NOT FOUND")
        if "enabled" in status and "disabled" not in status:
            # Server is connected — pass
            continue
        failures.append((name, status))

    # Report
    if failures:
        for name, status in failures:
            msg = f"MCP server '{name}' preflight failed: {status}"
            log_error(msg)
            print(f"mcp_preflight FAIL: {msg}", file=sys.stderr)
        sys.exit(1)
    else:
        if not args.hook:
            healthy = ", ".join(sorted(
                n for n in critical_set if connected.get(n, "").startswith("✓")
            ))
            print(f"mcp_preflight OK: {len(critical_set)} critical servers healthy")
            if healthy:
                print(f"  connected: {healthy}")
        sys.exit(0)


if __name__ == "__main__":
    main()
