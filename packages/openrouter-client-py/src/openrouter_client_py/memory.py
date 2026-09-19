"""supermemory - Optional memory layer for openrouter_client_py.

Store exchanges (POST /v3/documents, taskType "memory") and retrieve prior
context (POST /v4/search) scoped to ONE singular ``containerTag``
(``^[a-zA-Z0-9_:-]+$``, first write creates the tag, never cross-tag).

The API key is read from ``SUPERMEMORY_API_KEY`` in the environment only.
Every method degrades gracefully: missing key or any request failure returns
``None`` / ``[]`` so the host application never breaks.
"""

from __future__ import annotations

import asyncio
import hashlib
import json
import logging
import os
import urllib.request
from typing import Any

logger = logging.getLogger(__name__)

DEFAULT_API_BASE = "https://api.supermemory.ai"


def is_available() -> bool:
    """True when SUPERMEMORY_API_KEY is present in the environment."""
    return bool(os.environ.get("SUPERMEMORY_API_KEY"))


def _stable_id(*parts: str) -> str:
    """Stable 24-char id from parts (customId for idempotent ingests)."""
    return hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()[:24]


class SupermemoryMemory:
    """Dependency-free memory client (stdlib urllib only)."""

    def __init__(
        self,
        container_tag: str,
        api_key: str | None = None,
        api_base: str | None = None,
        timeout: float = 15.0,
    ) -> None:
        self.container_tag = container_tag
        self.api_base = api_base or os.environ.get("SUPERMEMORY_API_BASE") or DEFAULT_API_BASE
        self.api_key = api_key or os.environ.get("SUPERMEMORY_API_KEY")
        self.timeout = timeout

    def _post(self, path: str, body: dict[str, Any]) -> dict[str, Any] | None:
        if not self.api_key:
            return None
        req = urllib.request.Request(
            f"{self.api_base}{path}",
            data=json.dumps(body).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=self.timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def store_exchange(
        self,
        role: str,
        content: str,
        metadata: dict[str, str] | None = None,
    ) -> str | None:
        """Store one exchange with the full memory pipeline.

        Returns the stable customId, or ``None`` when unavailable/failed.
        """
        if not self.api_key or not content.strip():
            return None
        try:
            custom_id = _stable_id(self.container_tag, role, content)
            self._post(
                "/v3/documents",
                {
                    "content": f"{role}: {content}"[:100_000],
                    "containerTag": self.container_tag,
                    "taskType": "memory",
                    "customId": custom_id,
                    "metadata": {"role": role, **(metadata or {})},
                },
            )
            return custom_id
        except Exception as exc:
            logger.warning("supermemory store failed: %s", exc)
            return None

    def search_context(
        self,
        query: str,
        limit: int = 5,
        search_mode: str = "hybrid",
    ) -> list[dict[str, Any]]:
        """Search prior memories + documents.

        Returns normalized [{"id", "content", "score", "source"}] entries,
        or ``[]`` when unavailable/failed.
        """
        if not self.api_key or not query.strip():
            return []
        try:
            data = self._post(
                "/v4/search",
                {
                    "q": query,
                    "containerTag": self.container_tag,
                    "searchMode": search_mode,
                    "limit": limit,
                },
            )
            out: list[dict[str, Any]] = []
            for r in (data or {}).get("results", []) or []:
                chunk = r.get("chunk") or r.get("memory") or r.get("content")
                out.append(
                    {
                        "id": r.get("id") or r.get("memoryId"),
                        "content": chunk if isinstance(chunk, str) else json.dumps(chunk),
                        "score": float(r.get("similarity") or r.get("score") or 0.0),
                        "source": "document" if r.get("chunk") else "memory",
                    }
                )
            return out[:limit]
        except Exception as exc:
            logger.warning("supermemory search failed: %s", exc)
            return []

    @staticmethod
    def build_system_context(results: list[dict[str, Any]], max_chars: int = 2000) -> str:
        """Turn results into a compact system-context block ("" when empty)."""
        if not results:
            return ""
        lines = ["Relevant prior context from memory:"]
        used = len(lines[0])
        for r in results:
            line = f"- [{r['source']}·{r['score']:.2f}] {r['content']}"
            if used + len(line) + 1 > max_chars:
                break
            lines.append(line)
            used += len(line) + 1
        return "\n".join(lines)

    # Async wrappers (stdlib-safe, no event loop blocking).
    async def astore_exchange(
        self,
        role: str,
        content: str,
        metadata: dict[str, str] | None = None,
    ) -> str | None:
        return await asyncio.to_thread(self.store_exchange, role, content, metadata)

    async def asearch_context(
        self,
        query: str,
        limit: int = 5,
        search_mode: str = "hybrid",
    ) -> list[dict[str, Any]]:
        return await asyncio.to_thread(self.search_context, query, limit, search_mode)


__all__ = ["SupermemoryMemory", "is_available"]
