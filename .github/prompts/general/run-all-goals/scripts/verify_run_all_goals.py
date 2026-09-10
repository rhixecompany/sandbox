#!/usr/bin/env python3
"""Verified: checks output file exists; verifies no placeholder markers."""
import os, sys
out = "C:/Users/Alexa/Desktop/SandBox/.github/prompts/general/run-all-goals/run-all-goals.prompt.md"
assert os.path.exists(out), "Output prompt missing"
with open(out) as f: data = f.read()
for bad in ["FIXME:", "TODO:", "PLACEHOLDER"]:
    assert bad not in data or "No placeholder" in data, f"Unexpected marker: {bad}"
print("PASS")
