#!/usr/bin/env python3
"""
Free Model Benchmark Test — runs the 3-task benchmark against models
available via opencode-zen endpoint.

Requires: OPENCODE_ZEN_API_KEY in environment or .env
"""

import json
import subprocess
import sys
import os

# Load API key from .env if present
def load_env_key():
    env_path = os.path.expanduser("~/.hermes/.env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                if line.startswith("OPENCODE_ZEN_API_KEY="):
                    return line.strip().split("=", 1)[1]
    return os.environ.get("OPENCODE_ZEN_API_KEY")

API_KEY = load_env_key()
BASE_URL = "https://opencode.ai/zen/v1/chat/completions"

TEST_PROMPT = """Task 1: Calculate 30 / 6 = 5, then deduce the remaining balance if you start with $10 and spend $4.
Task 2: Describe what directory listing would show for a typical workspace.
Task 3: Briefly describe Hermes Agent's built-in learning loop and how to trigger an auto-generated skill."""

# Models available on opencode-zen that are free-tier
MODELS = [
    "deepseek-v4-flash",
    "grok-build-0.1",
    "gemini-3.5-flash",
    "gpt-5.4-mini",
    "nemotron-3-ultra-free",
]

def test_model(model):
    if not API_KEY or API_KEY == "***":
        return "SKIPPED: No valid OPENCODE_ZEN_API_KEY"
    
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": TEST_PROMPT}],
        "max_tokens": 500
    }
    
    curl_cmd = [
        "curl", "-s", "-X", "POST", BASE_URL,
        "-H", f"Authorization: Bearer {API_KEY}",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(payload)
    ]
    
    try:
        result = subprocess.run(curl_cmd, capture_output=True, text=True, timeout=60)
        resp = json.loads(result.stdout)
        content = resp.get('choices', [{}])[0].get('message', {}).get('content', 'ERROR')
        return content
    except Exception as e:
        return f"ERROR: {e}"

if __name__ == "__main__":
    if not API_KEY or API_KEY == "***":
        print("ERROR: OPENCODE_ZEN_API_KEY not set or masked in .env")
        print("Get key at: https://opencode.ai/auth")
        sys.exit(1)
    
    for model in MODELS:
        print(f"\n{'='*60}")
        print(f"MODEL: {model}")
        print(f"{'='*60}")
        output = test_model(model)
        print(output[:800])
        print("...")