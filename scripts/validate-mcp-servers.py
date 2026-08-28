#!/usr/bin/env python3
"""
MCP Server Validation Script — SandBox

Audits all MCP servers in opencode.json and generates a validation report.
Tests connectivity, configuration, and environment variables.
"""

import json
import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Tuple
import urllib.request
import urllib.error

# Configuration
WORKSPACE_ROOT = Path("C:/Users/Alexa/Desktop/SandBox")
OPENCODE_JSON = WORKSPACE_ROOT / "opencode.json"
REPORT_PATH = WORKSPACE_ROOT / ".hermes/mcp-validation-report.md"

# Ensure report directory exists
REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)


class MCPValidator:
    """Validates MCP server configurations and connectivity."""

    def __init__(self):
        self.results: Dict[str, Dict[str, Any]] = {}
        self.timestamp = datetime.now().isoformat()
        self.working_count = 0
        self.broken_count = 0
        self.env_vars = self._load_env_vars()

    def _load_env_vars(self) -> Dict[str, str]:
        """Load environment variables from .env file."""
        env_vars = dict(os.environ)
        env_file = WORKSPACE_ROOT / ".env"
        if env_file.exists():
            with open(env_file) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, value = line.split("=", 1)
                        env_vars[key.strip()] = value.strip()
        return env_vars

    def _resolve_env_var(self, value: str) -> str:
        """Resolve ${env:VAR_NAME} placeholders."""
        if not isinstance(value, str):
            return str(value)
        if "${env:" in value:
            parts = value.split("${env:")
            result = parts[0]
            for part in parts[1:]:
                var_name, rest = part.split("}", 1)
                result += self.env_vars.get(var_name, f"${{{var_name}}}") + rest
            return result
        return value

    def _test_remote_server(self, url: str) -> Tuple[bool, str]:
        """Test connectivity to remote HTTP MCP server."""
        try:
            url_resolved = self._resolve_env_var(url)
            req = urllib.request.Request(url_resolved, method="HEAD")
            req.add_header("User-Agent", "MCP-Validator/1.0")
            urllib.request.urlopen(req, timeout=5)
            return True, "HTTP response OK"
        except urllib.error.HTTPError as e:
            return False, f"HTTP Error {e.code}"
        except urllib.error.URLError as e:
            return False, f"Connection error: {str(e.reason)}"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def _test_local_command(self, command: List[str], env_dict: Dict[str, str] = None) -> Tuple[bool, str]:
        """Test local command availability."""
        try:
            # First test: check if command exists
            test_cmd = command[0]
            if test_cmd.endswith(".exe") or test_cmd.endswith(".py"):
                # Check file existence
                if not Path(test_cmd).exists():
                    return False, f"Command not found: {test_cmd}"
            else:
                # Try to run with --help or --version
                result = subprocess.run(
                    [command[0], "--version"],
                    capture_output=True,
                    timeout=5,
                    text=True,
                    env={**os.environ, **(env_dict or {})}
                )
                if result.returncode != 0 and "--version" not in result.stderr:
                    # Some commands don't support --version, that's OK
                    pass

            return True, "Command available"
        except subprocess.TimeoutExpired:
            return False, "Command timeout"
        except FileNotFoundError:
            return False, f"Command not found: {command[0]}"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def validate_server(self, name: str, config: Dict[str, Any]) -> None:
        """Validate a single MCP server."""
        server_type = config.get("type", "unknown")
        enabled = config.get("enabled", True)

        result = {
            "name": name,
            "type": server_type,
            "enabled": enabled,
            "status": "unknown",
            "message": "",
            "timestamp": self.timestamp,
        }

        if not enabled:
            result["status"] = "disabled"
            result["message"] = "Server is disabled"
            self.results[name] = result
            return

        if server_type == "remote":
            url = config.get("url", "")
            success, message = self._test_remote_server(url)
            result["status"] = "working" if success else "broken"
            result["message"] = message
            result["url"] = url

        elif server_type == "local":
            cmd = config.get("command")
            if isinstance(cmd, str):
                cmd = [cmd]
            elif not isinstance(cmd, list):
                cmd = config.get("args", [])

            if not cmd:
                result["status"] = "broken"
                result["message"] = "No command specified"
            else:
                env_dict = config.get("env", {})
                # Resolve env vars
                resolved_env = {}
                for k, v in env_dict.items():
                    resolved_env[k] = self._resolve_env_var(v)

                success, message = self._test_local_command(cmd, {**os.environ, **resolved_env})
                result["status"] = "working" if success else "broken"
                result["message"] = message
                result["command"] = " ".join(cmd[:2])  # First 2 parts for brevity

        self.results[name] = result
        if result["status"] == "working":
            self.working_count += 1
        elif result["status"] == "broken":
            self.broken_count += 1

    def validate_all(self) -> None:
        """Validate all servers in opencode.json."""
        try:
            with open(OPENCODE_JSON, encoding='utf-8-sig') as f:
                config = json.load(f)
        except Exception as e:
            print(f"Error loading opencode.json: {e}")
            sys.exit(1)

        mcp_config = config.get("mcp", {})
        print(f"Validating {len(mcp_config)} MCP servers...")

        for server_name, server_config in mcp_config.items():
            self.validate_server(server_name, server_config)
            status = self.results[server_name]["status"]
            print(f"  {server_name:<25} {status:>10}")

    def generate_report(self) -> str:
        """Generate markdown report."""
        report = f"""# MCP Server Validation Report — SandBox

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary

- **Working**: {self.working_count} servers ✅
- **Broken**: {self.broken_count} servers ❌
- **Disabled**: {len(self.results) - self.working_count - self.broken_count} servers ⊘
- **Total**: {len(self.results)} servers

## Detailed Server Status

| # | Server | Type | Status | Message | Notes |
|---|--------|------|--------|---------|-------|
"""

        for i, (name, result) in enumerate(self.results.items(), 1):
            status_icon = "✅" if result["status"] == "working" else ("❌" if result["status"] == "broken" else "⊘")
            report += f"| {i} | `{name}` | {result['type']} | {status_icon} {result['status']} | {result['message']} | |\n"

        report += "\n## Issues Found\n\n"
        broken_servers = [name for name, result in self.results.items() if result["status"] == "broken"]
        if broken_servers:
            report += f"**{len(broken_servers)} broken servers:**\n"
            for name in broken_servers:
                result = self.results[name]
                report += f"- `{name}`: {result['message']}\n"
        else:
            report += "✅ No broken servers found.\n"

        report += "\n## Environment Variables Status\n\n"
        required_vars = ["GITHUB_TOKEN", "TAVILY_API_KEY", "DATABASE_URL", "OPENCODE_ZEN_API_KEY"]
        report += "| Variable | Status | Value Preview |\n"
        report += "|----------|--------|----------------|\n"
        for var in required_vars:
            value = self.env_vars.get(var, "NOT SET")
            preview = f"{value[:20]}..." if len(value) > 20 else value
            status = "✅" if var in self.env_vars else "❌"
            report += f"| `{var}` | {status} | {preview} |\n"

        report += "\n## Configuration Files Status\n\n"
        config_files = [
            ("opencode.json", WORKSPACE_ROOT / "opencode.json"),
            (".copilot/mcp.json", WORKSPACE_ROOT / ".copilot/mcp.json"),
            (".codex/mcp.json", WORKSPACE_ROOT / ".codex/mcp.json"),
            ("Hermes config.yaml", Path("C:/Users/Alexa/AppData/Local/hermes/config.yaml")),
        ]

        for name, path in config_files:
            status = "✅" if path.exists() else "❌"
            report += f"- {status} `{name}`: {path}\n"

        report += "\n## Recommended Next Steps\n\n"
        report += "1. **Add Missing MCP Servers**:\n"
        report += "   - Stripe MCP for comicwise project\n"
        report += "   - Plaid MCP for Banking project\n"
        report += "   - Additional AI/LLM integrations\n\n"
        report += "2. **Fix Broken Servers**:\n"
        for name in broken_servers:
            report += f"   - Review configuration for `{name}`\n"
        report += "\n3. **Sync Configuration**:\n"
        report += "   - Ensure all agent configs (OpenCode, Copilot, Codex) are synchronized\n"
        report += "   - Run sync script regularly\n\n"
        report += "4. **Environment Setup**:\n"
        report += "   - Verify all API keys are loaded correctly\n"
        report += "   - Test remote MCP endpoints with `curl`\n"

        return report

    def save_report(self) -> None:
        """Save report to file."""
        report = self.generate_report()
        with open(REPORT_PATH, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n[Report] Report saved to: {REPORT_PATH}")


def main():
    """Main entry point."""
    validator = MCPValidator()
    validator.validate_all()
    validator.save_report()

    # Print summary
    print(f"\n{'='*60}")
    print(f"Summary: {validator.working_count} working, {validator.broken_count} broken")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
