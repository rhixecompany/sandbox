#!/usr/bin/env python3
"""Test Models — Test LLM model availability and response quality.

Async CLI for probing model endpoints with sample prompts and measuring
response latency and quality.
"""

import asyncio
import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional


async def test_openai_compatible(
    endpoint: str,
    model: str,
    api_key: str,
    prompt: str = "Say hello in one word.",
    timeout: int = 30,
) -> Dict[str, Any]:
    """Test an OpenAI-compatible chat endpoint via httpt-like call."""
    import urllib.request
    import urllib.error

    url = f"{endpoint.rstrip('/')}/chat/completions"
    payload = json.dumps(
        {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 10,
        }
    ).encode()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    start = time.monotonic()
    try:
        req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
        # Offload blocking HTTP call to thread
        response = await asyncio.to_thread(
            urllib.request.urlopen, req, timeout=timeout
        )
        latency = time.monotonic() - start
        body = json.loads(response.read().decode())
        return {
            "model": model,
            "endpoint": endpoint,
            "latency_s": round(latency, 3),
            "status": "ok",
            "response": body.get("choices", [{}])[0]
            .get("message", {})
            .get("content", ""),
        }
    except Exception as exc:
        latency = time.monotonic() - start
        return {
            "model": model,
            "endpoint": endpoint,
            "latency_s": round(latency, 3),
            "status": "error",
            "error": str(exc),
        }


async def test_models_from_config(config_path: Path) -> List[Dict[str, Any]]:
    """Read JSON config and test all listed models."""
    try:
        content = await asyncio.to_thread(config_path.read_text, encoding="utf-8")
    except Exception as exc:
        return [{"error": f"Cannot read config: {exc}"}]

    config = json.loads(content)
    tests = []
    for entry in config.get("models", []):
        tests.append(
            test_openai_compatible(
                endpoint=entry.get("endpoint", "http://localhost:8080/v1"),
                model=entry["model"],
                api_key=entry.get("api_key", ""),
                prompt=entry.get("prompt", "Say hello in one word."),
            )
        )
    return await asyncio.gather(*tests)


async def main() -> None:
    parser = argparse.ArgumentParser(
        description="Test LLM model availability and response quality."
    )
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Path to JSON config with model list",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Single model name to test",
    )
    parser.add_argument(
        "--endpoint",
        type=str,
        default="http://localhost:8080/v1",
        help="API endpoint (default: http://localhost:8080/v1)",
    )
    parser.add_argument(
        "--api-key",
        type=str,
        default="",
        help="API key",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file (default: stdout)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="JSON output",
    )
    args = parser.parse_args()

    if args.config:
        config_path = Path(args.config).resolve()
        if not config_path.exists():
            print(f"Config not found: {config_path}", file=sys.stderr)
            sys.exit(1)
        results = await test_models_from_config(config_path)
    elif args.model:
        results = [
            await test_openai_compatible(
                endpoint=args.endpoint,
                model=args.model,
                api_key=args.api_key,
            )
        ]
    else:
        # No args — try default configs
        candidates = [
            Path.cwd() / "models.json",
            Path.home() / ".hermes" / "models.json",
        ]
        config_path = None
        for c in candidates:
            if c.exists():
                config_path = c
                break
        if config_path:
            results = await test_models_from_config(config_path)
        else:
            print(
                "No config or model specified. Pass --config or --model.",
                file=sys.stderr,
            )
            sys.exit(2)

    passed = [r for r in results if r.get("status") == "ok"]
    failed = [r for r in results if r.get("status") != "ok"]

    if args.json:
        output = json.dumps(
            {"results": results, "passed": len(passed), "failed": len(failed)},
            indent=2,
        )
        if args.output:
            await asyncio.to_thread(
                Path(args.output).write_text, output, encoding="utf-8"
            )
        else:
            print(output)
    else:
        lines = [f"\n=== Model Test Results ==="]
        lines.append(f"Tested {len(results)} — Passed: {len(passed)}, Failed: {len(failed)}")
        for r in results:
            status = "PASS" if r.get("status") == "ok" else "FAIL"
            model = r.get("model", "?")
            lat = r.get("latency_s", "?")
            lines.append(f"  [{status}] {model} ({lat}s)")
            if r.get("status") == "ok":
                lines.append(f"          Response: {r.get('response', '')[:80]}")
            else:
                lines.append(f"          Error: {r.get('error', 'unknown')}")
        report = "\n".join(lines)
        if args.output:
            await asyncio.to_thread(
                Path(args.output).write_text, report, encoding="utf-8"
            )
        else:
            print(report)

    sys.exit(0 if len(failed) == 0 else 1)


if __name__ == "__main__":
    asyncio.run(main())
