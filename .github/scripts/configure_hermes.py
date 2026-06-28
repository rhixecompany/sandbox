#!/usr/bin/env python3
"""
Hermes MCP Docker Configuration Script
Configures Hermes globally and per-project with available Docker MCP servers
"""
import yaml
import os
import json
from pathlib import Path

# Paths
HERMES_CONFIG = Path.home() / "AppData" / "Local" / "hermes" / "config.yaml"
PROJECT_ROOT = Path("C:/Users/Alexa/Desktop/Sandbox")
PROJECT_HERMES_CONFIG = PROJECT_ROOT / ".hermes" / "config.yaml"

# Docker MCP servers from the adminbot profile
DOCKER_MCP_SERVERS = {
    "github": {
        "command": "docker",
        "args": ["run", "--rm", "-i", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN=${GITHUB_TOKEN}",
                 "ghcr.io/github/github-mcp-server:latest"],
        "enabled": True,
        "description": "GitHub repository automation and interaction (26 tools)"
    },
    "github-official": {
        "command": "docker",
        "args": ["run", "--rm", "-i", "-e", "GITHUB_PERSONAL_ACCESS_TOKEN=${GITHUB_TOKEN}",
                 "ghcr.io/github/github-mcp-server:latest"],
        "enabled": True,
        "description": "Official GitHub MCP server (41 tools, 2 prompts)"
    },
    "gitmcp": {
        "command": "docker",
        "args": ["run", "--rm", "-i", "-v", "${CWD}:${CWD}",
                 "mcp/gitmcp:latest"],
        "enabled": True,
        "description": "Git operations MCP server (5 tools)"
    },
    "git": {
        "command": "docker",
        "args": ["run", "--rm", "-i", "-v", "${CWD}:${CWD}",
                 "mcp/git:latest"],
        "enabled": False,  # Disabled due to connection issues
        "description": "Git repository interaction (reference)"
    }
}

def load_yaml(path):
    """Load YAML config file"""
    if not path.exists():
        return {}
    with open(path, 'r') as f:
        return yaml.safe_load(f) or {}

def save_yaml(path, data):
    """Save YAML config file"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)
    print(f"✓ Saved: {path}")

def configure_global_hermes():
    """Configure Hermes globally"""
    print("\n📋 Configuring Hermes Globally...")
    
    config = load_yaml(HERMES_CONFIG)
    
    # Ensure mcp_servers section exists
    if 'mcp_servers' not in config:
        config['mcp_servers'] = {}
    
    # Add Docker MCP servers
    for name, server_config in DOCKER_MCP_SERVERS.items():
        if name not in config['mcp_servers']:
            config['mcp_servers'][name] = server_config
            print(f"  ✓ Added: {name}")
        else:
            # Update existing
            config['mcp_servers'][name].update(server_config)
            print(f"  ↻ Updated: {name}")
    
    # Ensure essential settings
    if 'model' not in config:
        config['model'] = {}
    config['model']['default'] = 'big-pickle'
    config['model']['provider'] = 'opencode-zen'
    
    # Save
    save_yaml(HERMES_CONFIG, config)

def configure_project_hermes():
    """Configure Hermes for this project"""
    print("\n📋 Configuring Hermes for Project...")
    
    PROJECT_HERMES_CONFIG.parent.mkdir(parents=True, exist_ok=True)
    
    project_config = {
        'agent': {
            'max_turns': 100,
            'reasoning_effort': 'medium'
        },
        'terminal': {
            'cwd': str(PROJECT_ROOT),
            'timeout': 300
        },
        'mcp_servers': {
            'docker': {'enabled': True},
            'github': {'enabled': True},
            'github-official': {'enabled': True},
            'gitmcp': {'enabled': True}
        }
    }
    
    save_yaml(PROJECT_HERMES_CONFIG, project_config)

def verify_configuration():
    """Verify Hermes configuration"""
    print("\n✓ Verification Results:")
    print(f"  ✓ Global config: {HERMES_CONFIG}")
    print(f"  ✓ Project config: {PROJECT_HERMES_CONFIG}")
    
    # Check if files exist
    if HERMES_CONFIG.exists():
        print(f"  ✓ Global config exists")
    if PROJECT_HERMES_CONFIG.exists():
        print(f"  ✓ Project config exists")

if __name__ == "__main__":
    try:
        configure_global_hermes()
        configure_project_hermes()
        verify_configuration()
        print("\n✓ Hermes configuration complete!")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
