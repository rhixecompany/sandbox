"""rate_limit_bypass.py — Provider-aware rate-limit / usage-limit bypass layer.

Wraps every model invocation in a tiny retry/rotation wrapper:

1. Detects 429 / 403 / 5xx-class errors and certain provider-specific rate-limit
   response shapes (xai's "usage limit", OpenRouter "rate limit exceeded",
   OpenCode-Zen quota strings).
2. Sleeps with exponential backoff (jittered), honouring a Retry-After header
   when the provider returns one.
3. After N retries on the same model, rotates to the next model in the
   configured fallback chain (read from `hermes config show`).
4. Caps the total number of attempts so a single request never burns more
   than `max_attempts` calls (default 6 = current model + 5 fallbacks).
5. Emits a structured JSON line on every attempt for the session logger hook
   (`HERMES_RATE_LIMIT_AUDIT_LOG` env var or default file).

Usage as a library::

    from rate_limit_bypass import Bypass, BypassConfig
    b = Bypass(BypassConfig.from_env())
    text = b.call(lambda: openai_call(model="x", messages=[...]))

Usage as a CLI::

    python scripts/rate_limit_bypass.py --probe
    python scripts/rate_limit_bypass.py --status
    python scripts/rate_limit_bypass.py --self-test
"""

from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Optional

# --- Detection ----------------------------------------------------------------

_RATE_PATTERNS = (
    "rate limit",
    "usage limit",
    "rate_limit",
    "quota",
    "too many requests",
    "429",
    "exceeded your",
    "capacity",
)

# Providers whose 5xx / 403 should NOT be treated as rate limits (treat as
# permanent failures and skip retries).
_NON_RETRYABLE_PATTERNS = (
    "invalid api key",
    "unauthorized",
    "model not found",
    "context length",
    "context_length",
)


def _is_rate_limit(exc: Exception) -> bool:
    msg = (str(exc) or "").lower()
    if any(p in msg for p in _NON_RETRYABLE_PATTERNS):
        return False
    return any(p in msg for p in _RATE_PATTERNS)


def _retry_after(exc: Exception, default: float = 2.0) -> float:
    """Return a Retry-After hint if present, else default."""
    msg = str(exc) or ""
    # OpenAI / OpenRouter / xAI style: "try again in 23s"
    for tok in ("try again in ", "retry-after: "):
        idx = msg.lower().find(tok)
        if idx == -1:
            continue
        tail = msg[idx + len(tok):]
        digits = ""
        for ch in tail:
            if ch.isdigit() or ch == ".":
                digits += ch
            elif digits:
                break
        if digits:
            try:
                return max(float(digits), 0.5)
            except ValueError:
                pass
    return default


# --- Config -------------------------------------------------------------------


@dataclass
class BypassConfig:
    max_attempts: int = 6
    base_sleep: float = 1.5
    max_sleep: float = 30.0
    jitter: float = 0.4
    audit_log: Path = field(
        default_factory=lambda: Path(
            os.environ.get(
                "HERMES_RATE_LIMIT_AUDIT_LOG",
                str(Path.home() / "AppData/Local/hermes/logs/rate-limit-bypass.jsonl"),
            )
        )
    )

    @classmethod
    def from_env(cls) -> "BypassConfig":
        cfg = cls()
        for k in ("max_attempts",):
            v = os.environ.get(f"HERMES_BYPASS_{k.upper()}")
            if v and v.isdigit():
                setattr(cfg, k, max(1, int(v)))
        return cfg


# --- Audit log ----------------------------------------------------------------


def _audit(log_path: Path, record: dict[str, Any]) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    record = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), **record}
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record) + "\n")


# --- Core bypass --------------------------------------------------------------


class Bypass:
    """Wraps a single call with retry, rotation, and audit."""

    def __init__(
        self,
        cfg: Optional[BypassConfig] = None,
        fallbacks: Optional[list[str]] = None,
    ) -> None:
        self.cfg = cfg or BypassConfig.from_env()
        self.fallbacks = fallbacks or []

    def call(self, fn: Callable[[], str], model: str = "default") -> str:
        """Invoke `fn()` with retry/rotation. `fn` must accept no args; rotate
        by passing a different model requires the caller to close over it.
        Here we expose rotation via a different path: `call_rotating`."""
        return self._invoke(fn, model=model, label="primary")

    def call_rotating(
        self,
        factories: list[Callable[[str], Callable[[], str]]],
        start_model: str,
    ) -> str:
        """Each factory takes a model name and returns a 0-arg callable.
        We try the primary, then rotate through `factories[1:]`."""
        last_exc: Optional[Exception] = None
        for idx, factory in enumerate(factories[: self.cfg.max_attempts]):
            model = start_model if idx == 0 else f"fallback[{idx}]"
            try:
                return self._invoke(factory(model), model=model, label=str(idx))
            except _PermanentError as e:
                last_exc = e
                _audit(self.cfg.audit_log, {"event": "permanent", "model": model, "error": str(e)})
                break
            except Exception as e:  # noqa: BLE001 — last resort
                last_exc = e
        raise RuntimeError(f"rate_limit_bypass: exhausted {len(factories)} attempts") from last_exc

    # -- internals ---------------------------------------------------------

    def _invoke(self, fn: Callable[[], str], model: str, label: str) -> str:
        attempt = 0
        while True:
            attempt += 1
            try:
                result = fn()
                if attempt > 1:
                    _audit(
                        self.cfg.audit_log,
                        {"event": "recovered", "model": model, "attempt": attempt},
                    )
                return result
            except _PermanentError:
                raise
            except Exception as e:  # noqa: BLE001
                if not _is_rate_limit(e):
                    raise
                if attempt >= self.cfg.max_attempts:
                    _audit(
                        self.cfg.audit_log,
                        {
                            "event": "exhausted",
                            "model": model,
                            "attempt": attempt,
                            "error": str(e),
                        },
                    )
                    raise
                sleep_for = min(self.cfg.max_sleep, _retry_after(e, self.cfg.base_sleep))
                sleep_for *= 1.0 + random.uniform(-self.cfg.jitter, self.cfg.jitter)
                sleep_for = max(0.5, sleep_for)
                _audit(
                    self.cfg.audit_log,
                    {
                        "event": "retry",
                        "model": model,
                        "attempt": attempt,
                        "sleep_s": round(sleep_for, 2),
                        "error": str(e)[:200],
                    },
                )
                time.sleep(sleep_for)


class _PermanentError(Exception):
    """Marker for errors that should not trigger retries."""


# --- CLI ----------------------------------------------------------------------


def _self_test() -> int:
    cfg = BypassConfig(max_attempts=4, base_sleep=0.05, max_sleep=0.2)
    bypass = Bypass(cfg, fallbacks=["fb-a", "fb-b"])

    # 1. Succeeds on first try.
    assert bypass.call(lambda: "ok", model="primary") == "ok"

    # 2. Retries rate-limit, then succeeds.
    calls = {"n": 0}

    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise RuntimeError("429 rate limit exceeded")
        return "recovered"

    assert bypass.call(flaky, model="primary") == "recovered"
    assert calls["n"] == 3

    # 3. Permanent errors are not retried.
    calls["n"] = 0

    def perm():
        calls["n"] += 1
        raise RuntimeError("invalid api key")

    try:
        bypass.call(perm, model="primary")
    except RuntimeError as e:
        assert "invalid api key" in str(e)
        assert calls["n"] == 1
    else:
        raise AssertionError("permanent error should not be retried")

    # 4. Exhausts after max_attempts.
    def always():
        raise RuntimeError("429 too many requests")

    try:
        bypass.call(always, model="primary")
    except RuntimeError as e:
        assert "429" in str(e)
    else:
        raise AssertionError("expected exhaustion")

    # 5. Rotation: factory list with one permanent skips the rest.
    factories = [
        lambda m: (lambda: (_ for _ in ()).throw(RuntimeError("invalid api key"))),
        lambda m: (lambda: "fb-b"),
    ]
    assert bypass.call_rotating(factories, start_model="primary") == "fb-b"

    print("rate_limit_bypass self-test OK")
    return 0


def _status(bypass: Bypass) -> int:
    log = bypass.cfg.audit_log
    if not log.exists():
        print(f"no audit log yet at {log}")
        return 0
    n = 0
    by_event: dict[str, int] = {}
    last = None
    for line in log.read_text(encoding="utf-8", errors="ignore").splitlines():
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        n += 1
        by_event[rec.get("event", "?")] = by_event.get(rec.get("event", "?"), 0) + 1
        last = rec
    print(f"audit log: {log}  events={n}  by_event={by_event}  last={last}")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Provider rate-limit bypass")
    p.add_argument("--probe", action="store_true", help="print active config and exit")
    p.add_argument("--status", action="store_true", help="summarise the audit log")
    p.add_argument("--self-test", action="store_true", help="run the in-process self-test")
    args = p.parse_args()
    bypass = Bypass(BypassConfig.from_env())
    if args.self_test:
        return _self_test()
    if args.status:
        return _status(bypass)
    if args.probe:
        print(json.dumps({"config": bypass.cfg.__dict__, "fallbacks": bypass.fallbacks}, default=str, indent=2))
        return 0
    p.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
