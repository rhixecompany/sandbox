#!/usr/bin/env python3
"""Shared prompt and provider-status helpers for model probes.

The probe runners use provider-level rate-limit filtering so one exhausted
credential cannot cause every model under that provider to be hammered.
"""

from __future__ import annotations

import re
import subprocess
from collections.abc import Iterable

SELF_PROFILE_PROMPT = (
    "hello whoami, who are u, what is ur providers,performance,uptime,apps,Modalities,Price,Context,Released"
)

# Keep this deliberately narrower than the generic fallback capacity matcher:
# 402/403 and 5xx failures are not rate-limit evidence by themselves.
_RATE_LIMIT_PATTERNS = (
    re.compile(
        r"\brate[\s_-]*limit(?:ed|ing|[\s_-]*(?:reached|exceeded|exhausted|error))?\b",
        re.IGNORECASE,
    ),
    re.compile(r"\b429\b"),
    re.compile(r"\btoo[\s_-]+many[\s_-]+requests\b", re.IGNORECASE),
    re.compile(
        r"\b(?:usage|quota)[\s_-]+(?:limit[\s_-]+)?"
        r"(?:reached|exceeded|exhausted|exhaustion)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:daily|weekly|monthly|per[\s_-]*(?:day|week|month))[\s_-]+"
        r"(?:request[\s_-]+)?(?:quota|limit)[\s_-]*"
        r"(?:reached|exceeded|exhausted|error)\b",
        re.IGNORECASE,
    ),
    re.compile(
        r"\brequest[\s_-]+(?:limit[\s_-]*)?"
        r"(?:reached|exceeded|exhausted|error)\b",
        re.IGNORECASE,
    ),
    re.compile(r"\b(?:throttle|throttled|throttling)\b", re.IGNORECASE),
)
_PROVIDER_HEADER = re.compile(
    r"^\s*([A-Za-z0-9][A-Za-z0-9_-]*)\s+\(\d+\s+credentials?\):\s*(.*)$",
    re.IGNORECASE,
)
_PROVIDER_FIELD = re.compile(
    r"[\"']?provider[\"']?\s*[:=]\s*[\"']?"
    r"([A-Za-z0-9][A-Za-z0-9_-]*)\b",
    re.IGNORECASE,
)
_PROVIDER_STATUS_ROW = re.compile(
    r"^\s*\|?\s*([A-Za-z0-9][A-Za-z0-9_-]*)\s*\|\s*(.*?)\s*\|?\s*$",
    re.IGNORECASE,
)


def is_rate_limit_text(*values: object) -> bool:
    """Return whether any supplied output contains rate-limit evidence."""
    text = "\n".join(str(value) for value in values if value is not None)
    return any(pattern.search(text) for pattern in _RATE_LIMIT_PATTERNS)


def is_rate_limit_error(stdout: object = "", stderr: object = "", exit_code: object = None) -> bool:
    """Detect a provider error without treating a model's prose as an error.

    Hermes normally writes failed API calls to stderr or exits non-zero.  A
    few wrappers place an explicit HTTP/status error in stdout, so that case
    is accepted when the output contains an error-context word or ``429``.
    A successful self-profile response that merely discusses rate limits is
    therefore not misclassified as a provider failure.
    """
    if is_rate_limit_text(stderr, exit_code):
        return True
    stdout_text = str(stdout or "")
    if exit_code not in (None, 0) and is_rate_limit_text(stdout_text):
        return True
    return is_rate_limit_text(stdout_text) and bool(
        re.search(r"\b(?:429|error|exception|failed|failure|http|status)\b", stdout_text, re.IGNORECASE)
    )


def rate_limited_providers(auth_output: str) -> set[str]:
    """Extract providers with rate-limit evidence from ``hermes auth list``.

    Hermes prints credential details below a provider header such as
    ``openrouter (2 credentials):``.  The parser also accepts a
    ``provider: <name>`` field for machine-readable/table output.  Provider
    names are returned exactly as shown apart from surrounding whitespace and
    case normalization, so callers can compare them case-insensitively.
    """
    providers: set[str] = set()
    current_provider: str | None = None
    for raw_line in auth_output.splitlines():
        line = raw_line.strip()
        if not line:
            # Credential blocks are separated by blank lines. Do not let a
            # later footer/status line inherit the previous provider.
            current_provider = None
            continue
        header = _PROVIDER_HEADER.match(raw_line)
        if header:
            current_provider = header.group(1).lower()
            if is_rate_limit_text(header.group(2) or ""):
                providers.add(current_provider)
            continue

        field = _PROVIDER_FIELD.search(line)
        if field and is_rate_limit_text(line):
            providers.add(field.group(1).lower())
            continue

        row = _PROVIDER_STATUS_ROW.match(line)
        if row and is_rate_limit_text(row.group(2)):
            providers.add(row.group(1).lower())
            continue

        if current_provider and is_rate_limit_text(line):
            providers.add(current_provider)
    return providers


def provider_is_rate_limited(provider: str, rate_limited: Iterable[str]) -> bool:
    """Compare provider names without allowing case differences to bypass a skip."""
    expected = provider.strip().lower()
    return expected in {name.strip().lower() for name in rate_limited}


def auth_rate_limited_providers(hermes_bin: str = "hermes", timeout: int = 30) -> tuple[set[str], str | None]:
    """Read live auth status without exposing credentials.

    Returns ``(providers, error)``.  A failed inventory is reported to the
    caller so it can retain runtime error detection instead of pretending the
    preflight was successful.
    """
    try:
        result = subprocess.run(
            [hermes_bin, "auth", "list"],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return set(), f"auth inventory unavailable: {exc}"

    output = f"{result.stdout}\n{result.stderr}"
    if result.returncode != 0:
        return rate_limited_providers(output), f"auth inventory exited {result.returncode}"
    return rate_limited_providers(output), None


def skipped_result(
    provider: str,
    model: str,
    reason: str = "provider_rate_limited",
) -> dict[str, object]:
    """Build the stable result shape used by all probe runners."""
    return {
        "provider": provider,
        "model": model,
        "status": "skipped",
        "skip_reason": reason,
        "provider_rate_limited": True,
        "success": False,
        "exit": None,
    }
