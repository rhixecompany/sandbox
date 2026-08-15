"""Tests for openrouter_client_py (Python package)."""

import pytest
from unittest.mock import patch, MagicMock
from dataclasses import dataclass
from typing import List, Optional


# Re-import the types we need
from openrouter_client_py.types import (
    OpenRouterClientConfig,
    Message,
    ToolCall,
    ModelChoice,
    Usage,
    ChatCompletion,
)


class MockOpenRouterClient:
    """Mock for the openrouter SDK's OpenRouterClient."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.chat = MagicMock()
        self.chat.completions = MagicMock()
        self.chat.completions.create = MagicMock()

    async def create(self, **kwargs):
        return MagicMock(
            id="test-id",
            object="chat.completion",
            created=1234567890,
            model=kwargs.get("model", ""),
            choices=[
                MagicMock(
                    index=0,
                    message=MagicMock(
                        role="assistant",
                        content="Hello from mocked OpenRouter!",
                    ),
                    finish_reason="stop",
                )
            ],
            usage=MagicMock(
                prompt_tokens=10,
                completion_tokens=8,
                total_tokens=18,
            ),
        )


class TestSendChat:
    """Tests for the send_chat convenience function."""

    @pytest.mark.asyncio
    async def test_basic_completion(self):
        """Test send_chat returns a ChatCompletion with a user message."""
        from openrouter_client_py.chat import send_chat

        with patch("openrouter_client_py.client.openrouter.OpenRouterClient", MockOpenRouterClient):
            messages = [Message(role="user", content="Hello, world!")]
            result = await send_chat(
                api_key="test-key",
                model="openai/gpt-4o",
                messages=messages,
            )

            assert result is not None
            assert result.id == "test-id"
            assert result.object == "chat.completion"
            assert len(result.choices) == 1
            assert result.choices[0].message.role == "assistant"
            assert result.choices[0].finish_reason == "stop"
            assert result.usage.total_tokens == 18

    @pytest.mark.asyncio
    async def test_with_http_referer_and_app_title(self):
        """Test send_chat passes optional headers."""
        from openrouter_client_py.chat import send_chat
        from openrouter_client_py.client import OpenRouterClient

        with patch("openrouter_client_py.client.openrouter.OpenRouterClient", MockOpenRouterClient):
            messages = [Message(role="user", content="Test message")]
            result = await send_chat(
                api_key="test-key",
                model="google/gemma-2-9b-it",
                messages=messages,
                http_referer="https://example.com",
                app_title="My App",
            )

            assert result.model == "google/gemma-2-9b-it"

    @pytest.mark.asyncio
    async def test_empty_messages(self):
        """Test send_chat handles empty messages array."""
        from openrouter_client_py.chat import send_chat

        with patch("openrouter_client_py.client.openrouter.OpenRouterClient", MockOpenRouterClient):
            messages: List[Message] = []
            result = await send_chat(
                api_key="test-key",
                model="openai/gpt-4o",
                messages=messages,
            )

            assert result is not None
            assert result.choices is not None


class TestOpenRouterClient:
    """Tests for the OpenRouterClient class."""

    def test_instantiation(self):
        """Test client instantiates with config."""
        from openrouter_client_py.client import OpenRouterClient

        config = OpenRouterClientConfig(
            api_key="test-key",
            http_referer="https://example.com",
            app_title="Test App",
        )
        client = OpenRouterClient(config)
        assert client is not None
        assert client._config.api_key == "test-key"

    def test_chat_send_method_exists(self):
        """Test client has chat_send method."""
        from openrouter_client_py.client import OpenRouterClient

        client = OpenRouterClient(OpenRouterClientConfig(api_key="test-key"))
        assert hasattr(client, "chat_send")
        assert callable(client.chat_send)


class TestTypes:
    """Tests for data types."""

    def test_message_creation(self):
        """Test Message dataclass."""
        from openrouter_client_py.types import Message

        msg = Message(role="user", content="Hello!")
        assert msg.role == "user"
        assert msg.content == "Hello!"

    def test_tool_call_creation(self):
        """Test ToolCall dataclass."""
        from openrouter_client_py.types import ToolCall

        tc = ToolCall(id="call-1", type="function", function_name="test", function_arguments='{"arg": "val"}')
        assert tc.id == "call-1"
        assert tc.type == "function"

    def test_chat_completion_creation(self):
        """Test ChatCompletion dataclass."""
        from openrouter_client_py.types import ChatCompletion, Message, ModelChoice, Usage

        msg = Message(role="assistant", content="Response")
        choice = ModelChoice(index=0, message=msg, finish_reason="stop")
        usage = Usage(prompt_tokens=5, completion_tokens=3, total_tokens=8)
        completion = ChatCompletion(
            id="test-id",
            object="chat.completion",
            created=1234567890,
            model="test-model",
            choices=[choice],
            usage=usage,
        )
        assert completion.id == "test-id"
        assert len(completion.choices) == 1
        assert completion.usage.total_tokens == 8
