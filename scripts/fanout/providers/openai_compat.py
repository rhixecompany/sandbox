"""
Generic OpenAI-compatible provider adapter.

Many providers expose an OpenAI-compatible /chat/completions endpoint
(deepseek, gemini, xai, nous, ollama-cloud, huggingface, etc.).
This adapter speaks that protocol directly via stdlib urllib so it
needs no SDK install.

Public function:
    async def call(prompt, model, api_key, base_url, **kwargs) -> dict
"""
from __future__ import annotations

import asyncio
import json
import time
import urllib.error
import urllib.request
from typing import Any


async def call(
    prompt: str,
    model: str,
    api_key: str,
    base_url: str,
    max_tokens: int = 256,
    temperature: float = 0.0,
    timeout: float = 60.0,
    extra_headers: dict[str, str] | None = None,
) -> dict[str, Any]:
    """
    Call any OpenAI-compatible /chat/completions endpoint.

    Returns dict with: output_text, output_tokens, prompt_tokens, latency_ms, error?, raw?
    """
    if not base_url.rstrip("/").endswith("/v1"):
        base_url = base_url.rstrip("/") + "/v1"
    url = base_url.rstrip("/") + "/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    if extra_headers:
        headers.update(extra_headers)

    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stream": False,
    }).encode("utf-8")

    started = time.monotonic()

    def _do_request() -> tuple[int, dict, str]:
        req = urllib.request.Request(url, data=body, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.status, dict(resp.headers), resp.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            return e.code, dict(e.headers or {}), e.read().decode("utf-8", errors="replace")
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            return 0, {}, f"{type(e).__name__}: {e}"

    status, _hdrs, text = await asyncio.to_thread(_do_request)
    latency_ms = int((time.monotonic() - started) * 1000)

    if status == 0:
        return {"output_text": "", "latency_ms": latency_ms, "error": text or "network error"}
    if status >= 400:
        # Try to extract error message from common shapes:
        #   {"error": {"message": "..."}}
        #   {"error": "..."}
        #   {"error": [{"message": "..."}]}
        #   {"errors": [{"message": "..."}]}
        #   [{"error": {"message": "..."}}]   <-- gemini sometimes
        #   {"error": {"code": ..., "message": "..."}}
        try:
            j = json.loads(text)
        except json.JSONDecodeError:
            return {"output_text": "", "latency_ms": latency_ms, "error": f"HTTP {status}: {text[:200]}"}
        err_msg = text[:200]

        def _first_msg(obj, _depth: int = 0) -> str | None:
            """Recursively find the first 'message' string in any nested dict/list."""
            if _depth > 5:  # safety
                return None
            if isinstance(obj, dict):
                m = obj.get("message")
                if isinstance(m, str):
                    return m
                # Recurse into all values
                for v in obj.values():
                    found = _first_msg(v, _depth + 1)
                    if found:
                        return found
            elif isinstance(obj, list) and obj:
                for item in obj:
                    found = _first_msg(item, _depth + 1)
                    if found:
                        return found
            return None

        if isinstance(j, list):
            m = _first_msg(j)
            if m:
                err_msg = m[:200]
        elif isinstance(j, dict):
            err = j.get("error")
            m = _first_msg(err)
            if m:
                err_msg = m[:200]
            elif isinstance(err, str):
                err_msg = err[:200]
            else:
                m = _first_msg(j.get("errors"))
                if m:
                    err_msg = m[:200]
        return {
            "output_text": "",
            "latency_ms": latency_ms,
            "error": f"HTTP {status}: {err_msg}",
        }
    try:
        j = json.loads(text)
    except json.JSONDecodeError:
        return {"output_text": text[:500], "latency_ms": latency_ms, "error": "non-JSON response"}
    choices = j.get("choices") or []
    output_text = ""
    if choices:
        msg = choices[0].get("message") or {}
        output_text = msg.get("content", "") or ""
    usage = j.get("usage") or {}
    return {
        "output_text": output_text,
        "output_tokens": usage.get("completion_tokens"),
        "prompt_tokens": usage.get("prompt_tokens"),
        "model_id": j.get("model", model),
        "latency_ms": latency_ms,
    }
