"""
Agent adapter: codex CLI.

Public function:
    async def call(prompt, model, **kwargs) -> dict
"""
from __future__ import annotations

import asyncio
import shutil
import time
from typing import Any


async def call(
    prompt: str,
    model: str | None = None,
    timeout: float = 180.0,
) -> dict[str, Any]:
    """
    Run a prompt through `codex exec` non-interactively.
    """
    if shutil.which("codex") is None:
        return {"output_text": "", "latency_ms": 0, "exit_code": -1, "error": "codex binary not on PATH"}
    args = ["codex", "exec", prompt]
    if model:
        args += ["--model", model]
    started = time.monotonic()
    proc = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
    )
    try:
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
    except asyncio.TimeoutError:
        proc.kill()
        return {"output_text": "", "latency_ms": int((time.monotonic() - started) * 1000),
                "exit_code": -1, "error": f"timeout after {timeout}s"}
    latency_ms = int((time.monotonic() - started) * 1000)
    out = stdout.decode("utf-8", errors="replace").strip()
    err = stderr.decode("utf-8", errors="replace").strip()
    return {
        "output_text": out,
        "latency_ms": latency_ms,
        "exit_code": proc.returncode,
        "error": err if proc.returncode != 0 else None,
    }
