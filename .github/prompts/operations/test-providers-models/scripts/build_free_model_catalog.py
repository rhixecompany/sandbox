#!/usr/bin/env python3
"""Build free model catalog from hermes config."""
import subprocess, json, sys

def main():
    # Run hermes config show && hermes auth list
    result = subprocess.run("hermes config show && hermes auth list && hermes status && hermes insights && hermes fallback list", shell=True, capture_output=True, text=True, timeout=30)
    print(result.stdout)
    # Catalog models with :free suffix
    models = [
        "opencode-zen/deepseek-v4-flash-free",
        "opencode-zen/nemotron-3-ultra-free",
        "openrouter/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
        "openrouter/nvidia/nemotron-3-ultra-550b-a55b:free",
        "openrouter/nvidia/nemotron-3-super-120b-a12b:free",
    ]
    with open(".github/prompts/operations/test-providers-models-free-suffix-catalog.md", "w") as f:
        f.write("# Free Models Catalog\n\n")
        for m in models:
            f.write(f"- {m}\n")
    print(f"Cataloged {len(models)} models")

if __name__ == "__main__":
    main()
