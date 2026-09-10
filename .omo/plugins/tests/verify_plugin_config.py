#!/usr/bin/env python3
"""Python plugin verification and config test — DRY, non-destructive.
Used for .opencode and .omo config validation.
"""

import json
import sys
from pathlib import Path

CONFIG_DIR = Path(__file__).parent.parent.parent.parent

def load_json(name):
    path = CONFIG_DIR / name
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def verify_opencode():
    data = load_json(".opencode/opencode.json")
    print("[PASS] .opencode/opencode.json valid JSON")
    plugins = data.get("plugin", [])
    assert isinstance(plugins, list) and len(plugins) >= 2, "Expected >=2 plugins"
    print(f"[PASS] Plugins ({len(plugins)}): {plugins}")
    model = data.get("model", "")
    assert "openrouter" in model, "Expected openrouter model"
    print(f"[PASS] Primary model: {model}")

    context_size = data.get("context_size")
    assert context_size and context_size >= 150000, f"Context too small: {context_size}"
    print(f"[PASS] Context size: {context_size}")

    compaction = data.get("compaction")
    if compaction:
        assert compaction.get("enabled") is True, "Compaction should be enabled"
        print(f"[PASS] Compaction enabled with level={compaction.get('compression_level')}")

    agent_factory = data.get("agent_factory")
    if agent_factory:
        print(f"[PASS] Agent factory: agent={agent_factory.get('default_agent')}, parallel_limit={agent_factory.get('parallel_limit')}")

    performance = data.get("performance")
    if performance:
        assert performance.get("speed_priority") is True, "Speed priority must be true"
        print(f"[PASS] Performance speed_priority=True")

    quality = data.get("quality")
    if quality:
        assert quality.get("multi_stage_review") is True
        assert quality.get("evidence_based_results") is True
        assert quality.get("dr_dry_compliant") is True
        print(f"[PASS] Quality: multi_stage_review=True, evidence_based=True, dry=True")

    experiments = data.get("experiments")
    if experiments:
        print(f"[PASS] Experiments enabled: chat_transform={experiments.get('chat_messages_transform')}, hook={experiments.get('context_injection_hook')}")

    print("\n=== All .opencode checks passed ===")

def verify_omo():
    data = load_json(".omo/config.json")
    print("[PASS] .omo/config.json valid JSON")
    plugins_enabled = data.get("plugins", {}).get("enabled", [])
    assert len(plugins_enabled) >= 2, "Expected >=2 plugins in .omo"
    print(f"[PASS] .omo plugins ({len(plugins_enabled)}): {plugins_enabled}")

    agent = data.get("agent", {})
    print(f"[PASS] Agent default={agent.get('default_agent')}, parallel_limit={agent.get('parallel_limit')}")

    context = data.get("context", {})
    max_ctx = context.get("max_context_tokens")
    assert max_ctx and max_ctx >= 150000
    print(f"[PASS] Context max_tokens={max_ctx}")

    performance = data.get("performance", {})
    assert performance.get("speed_priority") is True
    print(f"[PASS] Performance settings verified")

    quality = data.get("quality", {})
    assert quality.get("dr_dry_compliant") is True
    print(f"[PASS] Quality DRY compliance verified")

    print("\n=== All .omo checks passed ===")

def verify_sync():
    opencode = load_json(".opencode/opencode.json")
    omo = load_json(".omo/config.json")
    op_plugins = set(opencode.get("plugin", []))
    omo_plugins = set(omo.get("plugins", {}).get("enabled", []))
    # Allow superpowers in both; sync means core plugins overlap
    common = op_plugins & omo_plugins
    print(f"[PASS] Plugin overlap: {common}")
    assert len(common) >= 2, "Expected at least 2 common plugins"

if __name__ == "__main__":
    verify_opencode()
    verify_omo()
    verify_sync()
    print(f"\nAll verifications passed for workspace at {CONFIG_DIR}")
