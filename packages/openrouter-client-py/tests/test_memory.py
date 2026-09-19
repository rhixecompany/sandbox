"""Tests for openrouter_client_py.memory (Supermemory memory layer)."""



from openrouter_client_py.memory import SupermemoryMemory, is_available


class FakeMemory(SupermemoryMemory):
    """SupermemoryMemory with _post replaced (no network)."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sent: list[tuple[str, dict]] = []
        self.responses: list[dict] = []

    def _post(self, path, body):
        self.sent.append((path, body))
        if self.responses:
            return self.responses.pop(0)
        return {}


def test_is_available_without_key(monkeypatch):
    monkeypatch.delenv("SUPERMEMORY_API_KEY", raising=False)
    assert is_available() is False


def test_is_available_with_key(monkeypatch):
    monkeypatch.setenv("SUPERMEMORY_API_KEY", "sm_test")
    assert is_available() is True


def test_store_exchange_posts_documents(monkeypatch):
    monkeypatch.setenv("SUPERMEMORY_API_KEY", "sm_test")
    mem = FakeMemory("user_123")
    cid = mem.store_exchange("user", "Hello memory")
    assert cid and len(cid) == 24
    path, body = mem.sent[0]
    assert path == "/v3/documents"
    assert body["containerTag"] == "user_123"
    assert body["taskType"] == "memory"
    assert body["content"] == "user: Hello memory"
    assert body["metadata"]["role"] == "user"


def test_store_exchange_noop_without_key(monkeypatch):
    monkeypatch.delenv("SUPERMEMORY_API_KEY", raising=False)
    mem = FakeMemory("user_123")
    assert mem.store_exchange("user", "x") is None
    assert mem.sent == []


def test_search_context_normalizes_results(monkeypatch):
    monkeypatch.setenv("SUPERMEMORY_API_KEY", "sm_test")
    mem = FakeMemory("user_123")
    mem.responses = [
        {
            "results": [
                {"memory": "user prefers dark mode", "similarity": 0.9},
                {"chunk": "settings page dark theme", "similarity": 0.71},
            ]
        }
    ]
    results = mem.search_context("dark mode", limit=5)
    assert len(results) == 2
    assert results[0]["source"] == "memory"
    assert results[1]["source"] == "document"
    assert "dark mode" in results[0]["content"]
    # body uses q, not query
    path, body = mem.sent[0]
    assert path == "/v4/search"
    assert body["q"] == "dark mode"
    assert body["searchMode"] == "hybrid"


def test_build_system_context():
    block = SupermemoryMemory.build_system_context(
        [{"content": "coffee", "score": 0.8, "source": "memory"}]
    )
    assert "coffee" in block
    assert block.startswith("Relevant prior context from memory:")
    assert SupermemoryMemory.build_system_context([]) == ""


def test_async_wrappers(monkeypatch):
    import asyncio

    monkeypatch.setenv("SUPERMEMORY_API_KEY", "sm_test")
    mem = FakeMemory("user_123")
    mem.responses = [{"results": [{"memory": "fact", "similarity": 0.5}]}]
    out = asyncio.run(mem.asearch_context("q"))
    assert len(out) == 1
    cid = asyncio.run(mem.astore_exchange("assistant", "ok"))
    assert cid
