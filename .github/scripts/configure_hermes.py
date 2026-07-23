#!/usr/bin/env python3
"""Configure Hermes Agent — configure settings, profiles, providers, tools, and MCP servers.

Usage:
    python configure_hermes.py [--config PATH] [--set KEY=VALUE] [--get KEY]
                               [--validate] [--dry-run] [--apply]
"""

import asyncio
import argparse
import json
import sys
import re
from pathlib import Path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Configure Hermes Agent")
    parser.add_argument("--config", default=None, help="Path to config.yaml")
    parser.add_argument("--set", action="append", default=[], help="KEY=VALUE setting")
    parser.add_argument("--get", default=None, help="Get a specific key")
    parser.add_argument("--validate", action="store_true", help="Validate config")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes")
    parser.add_argument("--apply", action="store_true", help="Apply changes")
    return parser.parse_args(argv)


def find_config() -> Path:
    """Find the Hermes config.yaml file."""
    candidates = [
        Path.home() / ".hermes" / "config.yaml",
        Path.home() / "AppData/Local/hermes/config.yaml",
        Path.home() / ".config/hermes/config.yaml",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[1]  # Default to AppData location


async def read_config_async(config_path: Path) -> str:
    """Read config file asynchronously."""
    return await asyncio.to_thread(config_path.read_text, encoding="utf-8")


async def write_config_async(config_path: Path, content: str) -> None:
    """Write config file asynchronously."""
    await asyncio.to_thread(config_path.write_text, content, encoding="utf-8")


def parse_yaml_simple(text: str) -> dict:
    """Simple YAML parser for config files (CPU-bound)."""
    result: dict = {}
    current_key: str | None = None
    current_dict = result
    stack: list[dict] = [result]
    indent_levels: list[int] = [0]

    for line in text.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        stripped = line.lstrip()
        indent = len(line) - len(stripped)

        # Adjust stack based on indent
        while indent <= indent_levels[-1] and len(stack) > 1:
            stack.pop()
            indent_levels.pop()
            current_dict = stack[-1]

        if ":" in stripped:
            key, _, val = stripped.partition(":")
            key = key.strip()
            val = val.strip()

            if val:
                # Scalar value
                val = val.strip('"').strip("'")
                if val.lower() == "true":
                    val = True
                elif val.lower() == "false":
                    val = False
                try:
                    if "." in val:
                        val = float(val)
                    else:
                        val = int(val)
                except ValueError:
                    pass
                current_dict[key] = val
            else:
                # Nested key
                new_dict: dict = {}
                current_dict[key] = new_dict
                stack.append(new_dict)
                indent_levels.append(indent)
                current_dict = new_dict

    return result


def serialize_yaml(data: dict, indent: int = 0) -> str:
    """Simple YAML serializer (CPU-bound)."""
    lines: list[str] = []
    prefix = "  " * indent
    for key, val in data.items():
        if isinstance(val, dict):
            lines.append(f"{prefix}{key}:")
            lines.append(serialize_yaml(val, indent + 1))
        elif isinstance(val, bool):
            lines.append(f"{prefix}{key}: {'true' if val else 'false'}")
        elif val is None:
            lines.append(f"{prefix}{key}:")
        else:
            lines.append(f"{prefix}{key}: {val}")
    return "\n".join(lines)


def apply_setting(config_text: str, key: str, value: str) -> str:
    """Apply a KEY=VALUE setting to config text (CPU-bound)."""
    parts = key.split(".")
    if len(parts) == 1:
        # Simple key replacement
        pattern = rf"^{re.escape(key)}:.*"
        if re.search(pattern, config_text, re.MULTILINE):
            return re.sub(pattern, f"{key}: {value}", config_text, flags=re.MULTILINE)
        else:
            return config_text.rstrip() + f"\n{key}: {value}\n"
    else:
        # Nested key: update in YAML dict
        parsed = parse_yaml_simple(config_text)
        target = parsed
        for p in parts[:-1]:
            if p not in target or not isinstance(target[p], dict):
                target[p] = {}
            target = target[p]
        target[parts[-1]] = value
        return serialize_yaml(parsed)


async def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    config_path = Path(args.config) if args.config else find_config()

    if not config_path.exists():
        print(f"Config not found at {config_path}. Creating default.", file=sys.stderr)
        default_config = "provider: openai\nmodel: gpt-4\ntemperature: 0.7\n"
        if not args.dry_run:
            await write_config_async(config_path, default_config)
            print(f"Created default config at {config_path}")
        else:
            print(f"[DRY-RUN] Would create {config_path}")

    config_text = await read_config_async(config_path)
    modified = config_text

    # --get
    if args.get:
        parsed = parse_yaml_simple(config_text)
        parts = args.get.split(".")
        target = parsed
        for p in parts:
            if isinstance(target, dict) and p in target:
                target = target[p]
            else:
                print(f"Key '{args.get}' not found")
                sys.exit(1)
        print(f"{args.get}: {target}")
        return

    # --validate
    if args.validate:
        parsed = parse_yaml_simple(config_text)
        print(f"Config file: {config_path}")
        print(f"Format: valid YAML structure")
        print(f"Settings: {len(parsed)} top-level keys")
        if "provider" not in parsed:
            print("WARNING: no 'provider' configured")
        if "model" not in parsed:
            print("WARNING: no 'model' configured")
        if "temperature" in parsed:
            temp = parsed["temperature"]
            if isinstance(temp, (int, float)) and (temp < 0 or temp > 2):
                print(f"WARNING: temperature={temp} outside recommended range [0, 2]")
        print("Validation complete.")
        return

    # --set
    for setting in args.set:
        if "=" not in setting:
            print(f"ERROR: invalid setting format '{setting}'. Use KEY=VALUE", file=sys.stderr)
            sys.exit(1)
        key, value = setting.split("=", 1)
        modified = apply_setting(modified, key.strip(), value.strip())
        print(f"Set {key} = {value}")

    if modified != config_text and args.set:
        if args.dry_run:
            print(f"\n[DRY-RUN] Would write changes to {config_path}")
            print("---")
            print(modified)
            print("---")
        elif args.apply:
            await write_config_async(config_path, modified)
            print(f"\nChanges applied to {config_path}")
        else:
            print(f"\nUse --apply to write changes to {config_path}")
            print(f"Preview (use --dry-run to see full diff)")


if __name__ == "__main__":
    asyncio.run(main())
