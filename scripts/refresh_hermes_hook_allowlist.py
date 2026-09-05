#!/usr/bin/env python3
"""Refresh the shell-hook consent allowlist through Hermes production code.

This intentionally prints only counts and event names. It never reads or
prints credential values and does not rewrite config.yaml.
"""

from __future__ import annotations

import sys
from pathlib import Path


HERMES_AGENT = Path(r"C:/Users/Alexa/AppData/Local/hermes/hermes-agent")
if str(HERMES_AGENT) not in sys.path:
    sys.path.insert(0, str(HERMES_AGENT))

from agent import shell_hooks  # noqa: E402
from hermes_cli.config import load_config  # noqa: E402


def main() -> int:
    config = load_config()
    specs = shell_hooks.iter_configured_hooks(config)
    registered = shell_hooks.register_from_config(config, accept_hooks=True)
    print(f"configured_hooks={len(specs)}")
    print(f"approved_or_registered={len(registered)}")
    print("events=" + ",".join(sorted({spec.event for spec in specs})))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
