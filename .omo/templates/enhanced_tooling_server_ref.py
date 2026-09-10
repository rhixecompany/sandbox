#!/usr/bin/env python3
"""Enhanced Python Quality MCP Server — references ~/myvenv, uv/uvx/uvm, mcp==2.0.0."""

import os
import platform

# Enhanced reference settings applied globally
MCP_VERSION = os.environ.get("MCP_VERSION", "2.0.0")
MYVENV_PATH = os.path.expanduser("~/myvenv")
PYTHON_INTERPRETER = os.path.join(MYVENV_PATH, "bin", "python") if not platform.system() == "Windows" else os.path.join(MYVENV_PATH, "Scripts", "python.exe")
UV_USE = os.environ.get("UV_USE", "true") == "true"
UVM_ACTIVE = os.environ.get("UVM_ACTIVE", MYVENV_PATH)

CONFIG_REF = {
    "mcp_version": MCP_VERSION,
    "myvenv_path": MYVENV_PATH,
    "python_interpreter": PYTHON_INTERPRETER,
    "uv_use": UV_USE,
    "uvm_active": UVM_ACTIVE,
    "package_manager_preference": "uv > uvx > uvm",
    "tooling_servers_enhanced": ["python-quality", "tooling-config", "tooling-lint"],
    "global_config_refs": [
        ".opencode/opencode.json",
        ".omo/config.json",
        ".vscode/mcp.json",
        ".copilot/mcp.json",
        ".codex/mcp.json"
    ]
}

if __name__ == "__main__":
    print(f"Enhanced tooling server reference: mcp=={CONFIG_REF['mcp_version']}")
    print(f"Virtualenv: {CONFIG_REF['myvenv_path']}")
    print(f"Python interpreter: {CONFIG_REF['python_interpreter']}")
    print(f"UV enabled: {CONFIG_REF['uv_use']}")
    print(f"UVM active: {CONFIG_REF['uvm_active']}")
    print(f"Tooling servers: {CONFIG_REF['tooling_servers_enhanced']}")
