#!/usr/bin/env python3
"""
test_all_mcp_servers.py — Comprehensive MCP server handshake test.

Tests every enabled MCP server by spawning it with its configured command+args,
sending an initialize JSON-RPC request, and validating the response.

Usage:
    python scripts/test_all_mcp_servers.py              # test all enabled servers
    python scripts/test_all_mcp_servers.py --name ast-grep  # test a single server
    python scripts/test_all_mcp_servers.py --json           # JSON output
    python scripts/test_all_mcp_servers.py --verbose        # show full responses

Exit codes:
    0 — all servers passed
    1 — one or more servers failed
    2 — config error
"""

import json
import os
import shutil
import subprocess
import sys
import yaml

CONFIG_PATH = os.path.expanduser("~/AppData/Local/hermes/config.yaml")
INIT_REQUEST = json.dumps({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "hermes-test", "version": "1.0"}
    }
}) + "\n"
TIMEOUT_PER_SERVER = 30  # seconds
SKIP_SERVERS = {"mcp-docker"}  # disabled/requires docker

def load_config():
    """Load MCP server definitions from Hermes config."""
    if not os.path.exists(CONFIG_PATH):
        print(f"ERROR: Config not found: {CONFIG_PATH}", file=sys.stderr)
        sys.exit(2)
    with open(CONFIG_PATH, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    servers = cfg.get("mcp_servers", {})
    if not servers:
        print("ERROR: No mcp_servers found in config", file=sys.stderr)
        sys.exit(2)
    return servers


def build_cmd(name, srv):
    """Build command list from server config entry."""
    cmd = srv.get("command", "")
    if not cmd:
        return None
    args = srv.get("args", [])
    return [cmd] + list(args)


def test_server(name, cmd, verbose=False):
    """Test a single MCP server via initialize handshake."""
    if not cmd:
        return {"server": name, "status": "SKIP", "reason": "no command"}
    if name in SKIP_SERVERS:
        return {"server": name, "status": "SKIP", "reason": "in skip list"}

    # Resolve command on Windows (.cmd/.bat files need shell=True)
    resolved = shutil.which(cmd[0])
    if not resolved:
        return {"server": name, "status": "FAIL",
                "reason": f"command not found on PATH: {cmd[0]}"}

    use_shell = resolved.endswith((".cmd", ".bat")) if os.name == "nt" else False
    effective_cmd = resolved if use_shell else [resolved] + cmd[1:]

    try:
        proc = subprocess.Popen(
            effective_cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            shell=use_shell,
            cwd=os.path.expanduser("~"),
        )
    except FileNotFoundError as e:
        return {"server": name, "status": "FAIL", "reason": f"command not found: {e}"}
    except OSError as e:
        return {"server": name, "status": "FAIL", "reason": f"OS error: {e}"}

    try:
        stdout, _ = proc.communicate(input=INIT_REQUEST, timeout=TIMEOUT_PER_SERVER)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
        return {"server": name, "status": "FAIL", "reason": "timed out"}
    except Exception as e:
        proc.kill()
        proc.wait()
        return {"server": name, "status": "FAIL", "reason": str(e)}

    try:
        # Find the JSON-RPC response (may be mixed with download output)
        resp = None
        for line in stdout.splitlines():
            line = line.strip()
            if line.startswith("{"):
                try:
                    resp = json.loads(line)
                    break
                except json.JSONDecodeError:
                    continue

        if resp is None:
            return {"server": name, "status": "FAIL",
                    "reason": "no JSON-RPC response in output",
                    "stdout_preview": stdout[:500]}

        init_result = resp.get("result", {})
        proto_ver = init_result.get("protocolVersion", "")
        server_info = init_result.get("serverInfo", {})
        srv_name = server_info.get("name", "?")
        srv_version = server_info.get("version", "?")

        if proto_ver == "2024-11-05" or proto_ver == "2025-03-26":
            caps = list(init_result.get("capabilities", {}).keys())
            tool_count = len(init_result.get("capabilities", {}).get("tools", {}))
            return {
                "server": name,
                "status": "PASS",
                "server_info": f"{srv_name} v{srv_version}",
                "protocol": proto_ver,
                "capabilities": caps,
            }
        else:
            return {"server": name, "status": "FAIL",
                    "reason": f"unexpected protocol: {proto_ver}",
                    "response": stdout[:300]}

    except (json.JSONDecodeError, KeyError) as e:
        return {"server": name, "status": "FAIL",
                "reason": f"parse error: {e}",
                "stdout_preview": stdout[:300]}


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Test all MCP servers")
    parser.add_argument("--name", help="Test only this server")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--verbose", action="store_true", help="Show full responses")
    args = parser.parse_args()

    servers = load_config()

    results = []
    exit_code = 0

    for name in sorted(servers.keys()):
        if args.name and name != args.name:
            continue
        srv = servers[name]
        if not srv.get("enabled", True):
            results.append({"server": name, "status": "SKIP",
                           "reason": "disabled in config"})
            continue

        cmd = build_cmd(name, srv)
        result = test_server(name, cmd, verbose=args.verbose)
        results.append(result)

        if result["status"] == "FAIL":
            exit_code = 1

    # Output
    if args.json:
        print(json.dumps(results, indent=2))
    else:
        passed = sum(1 for r in results if r["status"] == "PASS")
        failed = sum(1 for r in results if r["status"] == "FAIL")
        skipped = sum(1 for r in results if r["status"] == "SKIP")

        print(f"\n{'='*60}")
        print(f"MCP SERVER HEALTH — {passed} passed, {failed} failed, {skipped} skipped")
        print(f"{'='*60}\n")

        for r in results:
            if r["status"] == "PASS":
                caps = ", ".join(r.get("capabilities", []))
                print(f"  ✓ {r['server']:25s} {r['server_info']:20s} [{caps}]")
            elif r["status"] == "FAIL":
                reason = r.get("reason", "unknown")
                print(f"  ✗ {r['server']:25s} FAIL — {reason}")
                if args.verbose and "stdout_preview" in r:
                    print(f"    stdout: {r['stdout_preview'][:200]}")
            else:
                reason = r.get("reason", "")
                print(f"  - {r['server']:25s} SKIP ({reason})")

        print(f"\n{'='*60}")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
