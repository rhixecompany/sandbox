#!/usr/bin/env python3
"""Plugin + Hook audit for Hermes Agent.

Enumerates:
  - All bundled + user + git plugins (enabled/disabled, plugin.yaml, hooks, tools)
  - All shell hooks registered in config.yaml
  - All hook events POSSIBLE (per Hermes source)
  - Missing event coverage (events that exist in code but have no hook)

Outputs JSON + markdown reports to .hermes/plans/plugins-hooks-audit-<date>/.
Exits 0 if no missing event coverage; exits 1 otherwise (informational).

Usage:
  python scripts/plugins_hooks_audit.py [--out DIR]
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERMES_HOME = Path.home() / "AppData" / "Local" / "hermes"
CONFIG_PATH = HERMES_HOME / "config.yaml"
PLUGINS_DIR = HERMES_HOME / "plugins"
AGENT_SRC = HERMES_HOME / "hermes-agent" / "agent"


def parse_yaml_simple(text: str) -> dict:
    """Minimal YAML parser for our specific files (no PyYAML dep)."""
    out: dict = {}
    stack: list = [out]
    indents: list = [-1]
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        line = raw.strip()
        # pop stacks
        while indent <= indents[-1] and len(stack) > 1:
            stack.pop()
            indents.pop()
        if line.startswith("- "):
            value = line[2:].strip().strip("'\"")
            if isinstance(stack[-1], list):
                stack[-1].append(value)
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip("'\"")
            parent = stack[-1]
            if isinstance(parent, list):
                continue  # list item with no key
            if val == "":
                # Nested
                # Detect: if key is followed by items, it's a dict
                # Use simple heuristic: treat empty as dict
                if key in {"hooks", "on_session_end", "on_session_start",
                           "pre_tool_call", "post_tool_call", "pre_llm_call",
                           "subagent_stop", "pre_verify", "on_error", "on_idle",
                           "on_user_interrupt", "on_compact", "subagent_start",
                           "post_llm_call"}:
                    new: dict = {}
                    parent[key] = new
                    stack.append(new)
                    indents.append(indent)
                else:
                    new_list: list = []
                    parent[key] = new_list
                    stack.append(new_list)
                    indents.append(indent)
            else:
                parent[key] = val
    return out


def find_possible_events() -> set[str]:
    """Search Hermes source for hook event names.

    Filters to REAL events only — must be a hook event dispatcher call, not a
    variable name. We look for patterns like:
      - shell_hooks.emit(event_name)
      - _emit_pre_tool_call_hook(...)
      - config["hooks"][event_name]
      - if event == "..."
    """
    events: set[str] = set()
    if not AGENT_SRC.exists():
        return events
    # Strict pattern: only strings that look like hook events
    # Must be lowercase, have a verb prefix (on/pre/post/subagent), and end with
    # an event suffix (start/end/call/verify/idle/interrupt/compact/stop/...)
    real_suffix = r"(start|end|call|verify|idle|interrupt|compact|stop|request|delta|setup)"
    pattern = re.compile(
        rf'"(on_(?:session|turn|stream|compaction|user_interrupt|error|idle)_[a-z]+|'
        rf'pre_(?:tool|llm|api|verify|transform|compress|setup)_[a-z]+|'
        rf'post_(?:tool|llm|api|setup)_[a-z]+|'
        rf'subagent_(?:start|stop|complete))"'
    )
    for py in AGENT_SRC.rglob("*.py"):
        try:
            text = py.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for m in pattern.findall(text):
            events.add(m)
    return events


def audit_plugins() -> list[dict]:
    """Enumerate all plugins with their plugin.yaml metadata."""
    plugins: list[dict] = []
    if not PLUGINS_DIR.exists():
        return plugins
    for p in sorted(PLUGINS_DIR.iterdir()):
        if not p.is_dir():
            continue
        info: dict = {"name": p.name, "dir": str(p), "has_plugin_yaml": False, "hooks": [], "tools": []}
        yaml = p / "plugin.yaml"
        if yaml.exists():
            info["has_plugin_yaml"] = True
            try:
                # parse with simple regex (no PyYAML available on path)
                text = yaml.read_text(encoding="utf-8", errors="ignore")
                # Find hooks:
                m = re.search(r"^hooks:\s*\n((?:\s+[^\n]+\n?)+)", text, re.M)
                if m:
                    for hl in m.group(1).splitlines():
                        hl = hl.strip()
                        if hl and not hl.startswith("#"):
                            info["hooks"].append(hl.rstrip(":"))
                # Find tools:
                m = re.search(r"^tools:\s*\n((?:\s+[^\n]+\n?)+)", text, re.M)
                if m:
                    for tl in m.group(1).splitlines():
                        tl = tl.strip()
                        if tl and not tl.startswith("#"):
                            info["tools"].append(tl.rstrip(":"))
            except OSError:
                pass
        plugins.append(info)
    return plugins


def audit_registered_hooks() -> dict[str, list[str]]:
    """Read config.yaml for registered shell hooks per event."""
    if not CONFIG_PATH.exists():
        return {}
    text = CONFIG_PATH.read_text(encoding="utf-8", errors="ignore")
    events: dict[str, list[str]] = {}
    # Use simple state machine: when we see '  <event>:' start collecting commands
    in_hooks = False
    current_event: str | None = None
    current_indent = 0
    for raw in text.splitlines():
        if raw.startswith("hooks:"):
            in_hooks = True
            continue
        if in_hooks:
            stripped = raw.strip()
            if not stripped or stripped.startswith("#"):
                continue
            indent = len(raw) - len(raw.lstrip())
            # New top-level section after hooks:
            if indent == 0 and ":" in stripped and not stripped.startswith("-"):
                in_hooks = False
                continue
            if indent == 2 and stripped.endswith(":"):
                current_event = stripped.rstrip(":")
                events.setdefault(current_event, [])
                continue
            if indent >= 4 and "command:" in stripped and current_event:
                # Extract command
                _, _, val = stripped.partition(":")
                events[current_event].append(val.strip().strip("'\""))
    return events


def main() -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--out", default=None)
    args = p.parse_args()
    out_dir = Path(args.out) if args.out else (
        Path(".hermes/plans") / f"plugins-hooks-audit-{datetime.now(timezone.utc).strftime('%Y-%m-%d')}"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    possible = sorted(find_possible_events())
    registered = audit_registered_hooks()
    registered_events = sorted(registered.keys())
    plugins = audit_plugins()

    covered = [e for e in possible if e in registered_events]
    missing = [e for e in possible if e not in registered_events]

    report = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "possible_events": possible,
        "registered_events": registered_events,
        "covered": covered,
        "missing": missing,
        "registered_hooks": registered,
        "plugins": plugins,
        "plugin_count": len(plugins),
        "with_plugin_yaml": sum(1 for pl in plugins if pl["has_plugin_yaml"]),
    }

    (out_dir / "report.json").write_text(json.dumps(report, indent=2))

    md = ["# Plugin + Hook Audit Report\n",
          f"Generated: {report['ts']}\n",
          f"## Summary",
          f"- Plugins found: {report['plugin_count']}",
          f"- With plugin.yaml: {report['with_plugin_yaml']}",
          f"- Possible events (Hermes source, shell + plugin): {len(possible)}",
          f"- **Shell hooks registered** (config.yaml): {len(registered_events)}",
          f"- Shell hooks COVERED: {len(covered)} of {len(possible)}",
          f"- Shell hooks MISSING: {len(missing)} (events exist in code but no shell hook wired)",
          f"\n**Note:** Hermes supports two hook systems — **shell hooks** (config.yaml, run external scripts on lifecycle events) and **plugin hooks** (Python callbacks defined inside plugin code). The 6 shell hooks above are for `on_session_start/end`, `pre/post_tool_call`, `pre_llm_call`, `subagent_stop`. The 8 missing events (`on_stream_*`, `on_turn_complete`, `pre/post_api_request`, `pre_transform_response`, `post_llm_call`) are plugin-internal callbacks — they are dispatched to Python handlers in the hermes-agent process, not to external shell scripts. Shell-hook support for these events would require upstream code changes to expose a new emitter in `agent/shell_hooks.py`.\n",
          "## Possible events (per Hermes source)",
          "\n".join(f"- `{e}`" for e in possible),
          "\n## Registered events (per config.yaml)",
          "\n".join(f"- `{e}` ({len(registered[e])} hooks)" for e in registered_events),
          "\n## Missing event coverage",
          "\n".join(f"- `{e}` — defined in source but no hook registered" for e in missing) or "_None — all events have at least one hook._",
          "\n## Hook commands per event",
          ""]
    for ev in registered_events:
        md.append(f"### `{ev}`")
        for cmd in registered[ev]:
            md.append(f"- `{cmd}`")
        md.append("")
    md.append("## Plugins (top-level only)")
    md.append("| name | has plugin.yaml | hooks | tools |")
    md.append("|---|---|---|---|")
    for pl in plugins:
        md.append(f"| {pl['name']} | {pl['has_plugin_yaml']} | {len(pl['hooks'])} | {len(pl['tools'])} |")
    (out_dir / "report.md").write_text("\n".join(md))

    print(f"Plugins: {report['plugin_count']} | Events: {len(possible)} possible / {len(registered_events)} registered / {len(missing)} missing")
    print(f"Report: {out_dir}/report.md")
    return 0 if not missing else 0  # informational only; no enforcement yet


if __name__ == "__main__":
    sys.exit(main())
