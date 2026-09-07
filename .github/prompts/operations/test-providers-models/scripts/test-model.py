#!/usr/bin/env python3
"""Test individual provider models and record results."""
import subprocess, json, sys, time

def test_model(provider, model, task="What is the current time?"):
    cmd = f'hermes chat --provider "{provider}" --model "{model}" -q "{task}" --oneshot'
    start = time.time()
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        latency = time.time() - start
        return {"provider": provider, "model": model, "latency": latency, "success": result.returncode == 0, "output": result.stdout[:500]}
    except Exception as e:
        return {"provider": provider, "model": model, "latency": None, "success": False, "error": str(e)}

if __name__ == "__main__":
    models = json.loads(sys.argv[1]) if len(sys.argv) > 1 else []
    results = [test_model(m["provider"], m["model"]) for m in models]
    print(json.dumps(results, indent=2))
