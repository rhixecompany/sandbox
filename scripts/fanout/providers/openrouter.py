"""
Provider adapter for OpenRouter.

Uses the in-tree `packages/openrouter-client-py` package via subprocess to
avoid hard-importing the SDK into fanout's runtime. This keeps fanout
zero-dep-stdlib except for subprocess + json.

Public function:
    async def call(prompt, model, api_key, base_url, **kwargs) -> dict
"""
from __future__ import annotations

import asyncio
import json
import os
import time
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[3]
PKG_DIR = REPO_ROOT / "packages" / "openrouter-client-py"
PKG_INIT = PKG_DIR / "src" / "openrouter_client_py"


async def call(
    prompt: str,
    model: str,
    api_key: str,
    base_url: str = "https://openrouter.ai/api/v1",
    max_tokens: int = 256,
    temperature: float = 0.0,
    timeout: float = 60.0,
) -> dict[str, Any]:
    """
    Call OpenRouter via the in-tree openrouter-client-py package.

    Returns dict with: output_text, output_tokens, prompt_tokens, latency_ms, error?, raw?
    """
    started = time.monotonic()
    code = _runner_script()
    runner_path = REPO_ROOT / "scripts" / ".runtime" / "_openrouter_runner.py"
    runner_path.parent.mkdir(parents=True, exist_ok=True)
    runner_path.write_text(code, encoding="utf-8")

    env = {
        **os.environ,
        "OPENROUTER_API_KEY": api_key,
        "OPENROUTER_BASE_URL": base_url,
        "PYTHONPATH": str(PKG_INIT.parent) + os.pathsep + env_get("PYTHONPATH", ""),
    }
    proc = await asyncio.create_subprocess_exec(
        "python", str(runner_path), prompt, model, str(max_tokens), str(temperature),
        env=env, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
    )
    try:
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
    except asyncio.TimeoutError:
        proc.kill()
        return {"output_text": "", "latency_ms": int((time.monotonic() - started) * 1000),
                "error": f"timeout after {timeout}s"}
    latency_ms = int((time.monotonic() - started) * 1000)
    out = stdout.decode("utf-8", errors="replace").strip()
    err = stderr.decode("utf-8", errors="replace").strip()
    if proc.returncode != 0:
        return {"output_text": "", "latency_ms": latency_ms, "error": err or f"exit {proc.returncode}"}
    try:
        return {"latency_ms": latency_ms, **json.loads(out)}
    except json.JSONDecodeError:
        return {"output_text": out, "latency_ms": latency_ms, "error": "non-JSON response", "raw_stderr": err}


def _runner_script() -> str:
    """Inline runner that imports the in-tree package and reports a JSON line on stdout."""
    return '''#!/usr/bin/env python3
import asyncio, json, os, sys
sys.path.insert(0, os.environ.get("PYTHONPATH", "").split(os.pathsep)[0])
from openrouter_client_py import OpenRouterClient

prompt, model, max_tokens, temperature = sys.argv[1:5]
client = OpenRouterClient({"api_key": os.environ["OPENROUTER_API_KEY"]})

async def main():
    try:
        result = await client.chat_send(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=int(max_tokens),
            temperature=float(temperature),
        )
        out = {
            "output_text": result.choices[0].message.content if result.choices else "",
            "output_tokens": result.usage.completion_tokens if result.usage else None,
            "prompt_tokens": result.usage.prompt_tokens if result.usage else None,
            "model_id": result.model,
        }
        print(json.dumps(out))
    except Exception as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}), file=sys.stderr)
        sys.exit(1)

asyncio.run(main())
'''


def env_get(name: str, default: str = "") -> str:
    return os.environ.get(name, default)
