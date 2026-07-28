#!/usr/bin/env python3
"""Copilot MCP Server — start an MCP server bridging GitHub Copilot with Hermes tools.

Usage:
    python copilot_mcp_server.py [--port INT] [--host STR] [--config PATH]
"""

import argparse
import asyncio
import json
import signal
import sys
from pathlib import Path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Copilot MCP Server for Hermes")
    parser.add_argument("--port", type=int, default=8765, help="Server port (default: 8765)")
    parser.add_argument("--host", default="127.0.0.1", help="Server host (default: 127.0.0.1)")
    parser.add_argument("--config", default=None, help="Path to MCP config file")
    return parser.parse_args(argv)


def load_mcp_config(config_path: str | None) -> dict:
    """Load MCP configuration from JSON file."""
    if not config_path:
        return {}
    path = Path(config_path)
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    print(f"Config not found: {config_path}", file=sys.stderr)
    return {}


AVAILABLE_TOOLS = {
    "skills_list": {"description": "List all available Hermes skills"},
    "skill_view": {"description": "View a skill's content by name"},
    "web_search": {"description": "Search the web for information"},
    "read_file": {"description": "Read a file's contents"},
    "search_files": {"description": "Search file contents or find files"},
    "execute_command": {"description": "Execute a shell command"},
}


async def handle_mcp_request(request: dict) -> dict:
    """Handle a single MCP protocol request."""
    method = request.get("method", "")
    req_id = request.get("id", 0)
    params = request.get("params", {})

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {},
                    "resources": {},
                },
                "serverInfo": {
                    "name": "hermes-copilot-mcp",
                    "version": "1.0.0",
                },
            },
        }

    if method == "tools/list":
        tools = [
            {
                "name": name,
                "description": info["description"],
                "inputSchema": {
                    "type": "object",
                    "properties": {"skill_name": {"type": "string"}}
                    if "skill" in name
                    else {"query": {"type": "string"}},
                    "required": [],
                },
            }
            for name, info in AVAILABLE_TOOLS.items()
        ]
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": tools}}

    if method == "tools/call":
        tool_name = params.get("name", "")
        arguments = params.get("arguments", {})

        if tool_name not in AVAILABLE_TOOLS:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Tool not found: {tool_name}"},
            }

        # Simulate tool execution (in production, would call actual tools)
        result = {"content": [{"type": "text", "text": f"Executed {tool_name} with {arguments}"}]}
        return {"jsonrpc": "2.0", "id": req_id, "result": result}

    if method == "notifications/initialized":
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}

    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32601, "message": f"Method not found: {method}"},
    }


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    """Handle a single MCP client connection."""
    addr = writer.get_extra_info("peername")
    print(f"Client connected: {addr}")

    try:
        buffer = ""
        while True:
            data = await reader.read(4096)
            if not data:
                break
            buffer += data.decode("utf-8")

            # Process complete JSON-RPC messages
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                line = line.strip()
                if not line:
                    continue
                try:
                    request = json.loads(line)
                    response = await handle_mcp_request(request)
                    response_str = json.dumps(response) + "\n"
                    writer.write(response_str.encode("utf-8"))
                    await writer.drain()
                except json.JSONDecodeError:
                    error_response = {
                        "jsonrpc": "2.0",
                        "id": None,
                        "error": {"code": -32700, "message": "Parse error"},
                    }
                    writer.write((json.dumps(error_response) + "\n").encode("utf-8"))
                    await writer.drain()
    except asyncio.CancelledError:
        pass
    except Exception as e:
        print(f"Error handling client {addr}: {e}", file=sys.stderr)
    finally:
        writer.close()
        await writer.wait_closed()
        print(f"Client disconnected: {addr}")


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    config = load_mcp_config(args.config)

    print(f"Starting Copilot MCP Server on {args.host}:{args.port}")
    print(f"Available tools: {', '.join(AVAILABLE_TOOLS.keys())}")

    if config:
        print(f"Loaded config with {len(config)} settings")

    server = await asyncio.start_server(handle_client, args.host, args.port)

    addr = server.sockets[0].getsockname() if server.sockets else (args.host, args.port)
    print(f"MCP Server listening on {addr[0]}:{addr[1]}")

    # Handle shutdown
    stop = asyncio.Future()

    def shutdown():
        print("\nShutting down MCP Server...")
        stop.set_result(True)

    loop = asyncio.get_event_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, shutdown)
        except NotImplementedError:
            # Windows may not support add_signal_handler
            pass

    async with server:
        await stop


if __name__ == "__main__":
    asyncio.run(main())
