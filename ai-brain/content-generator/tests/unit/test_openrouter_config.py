"""Test OpenRouter configuration and LLM client setup."""

import pytest
from unittest.mock import patch
import os


def test_openrouter_default_settings():
    """Test that default settings use OpenRouter configuration."""
    # Clear environment to get true defaults
    with patch.dict(os.environ, {}, clear=True):
        from config.settings import Settings

        settings = Settings(_env_file=None)

        # Should default to OpenRouter base URL
        assert settings.openai_base_url == "https://openrouter.ai/api/v1"

        # Should default to free Llama 3.2 model
        assert settings.llm_model == "meta-llama/llama-3.2-3b-instruct:free"


def test_openrouter_custom_settings():
    """Test custom OpenRouter settings."""
    env_vars = {
        "OPENAI_API_KEY": "sk-or-v1-test-key",
        "OPENAI_BASE_URL": "https://openrouter.ai/api/v1",
        "LLM_MODEL": "google/gemini-2.0-flash-exp:free",
    }

    with patch.dict(os.environ, env_vars, clear=True):
        from config.settings import Settings

        settings = Settings(_env_file=None)

        assert settings.openai_api_key == "sk-or-v1-test-key"
        assert settings.openai_base_url == "https://openrouter.ai/api/v1"
        assert settings.llm_model == "google/gemini-2.0-flash-exp:free"


def test_openai_direct_settings():
    """Test that direct OpenAI settings can override OpenRouter."""
    env_vars = {
        "OPENAI_API_KEY": "sk-test-key",
        "OPENAI_BASE_URL": "https://api.openai.com/v1",
        "LLM_MODEL": "gpt-4-turbo-preview",
    }

    with patch.dict(os.environ, env_vars, clear=True):
        from config.settings import Settings

        settings = Settings(_env_file=None)

        assert settings.openai_api_key == "sk-test-key"
        assert settings.openai_base_url == "https://api.openai.com/v1"
        assert settings.llm_model == "gpt-4-turbo-preview"


def test_llm_client_accepts_base_url():
    """Test that LLM client can be initialized with custom base_url."""
    # This test verifies that the LLMClient code accepts base_url parameter
    from config import settings as settings_module

    # Patch settings to have test values
    with patch.object(settings_module.settings, "openai_api_key", "test-key"):
        with patch.object(
            settings_module.settings, "openai_base_url", "https://openrouter.ai/api/v1"
        ):
            with patch.object(
                settings_module.settings,
                "llm_model",
                "meta-llama/llama-3.2-3b-instruct:free",
            ):
                from core.llm_client import LLMClient

                # This should not raise an error
                client = LLMClient()

                # Verify client attributes
                assert client.model == "meta-llama/llama-3.2-3b-instruct:free"
                assert hasattr(client, "client")


def test_settings_with_env_variables():
    """Test that settings can be loaded from environment variables."""
    env_vars = {
        "OPENAI_API_KEY": "sk-or-v1-env-key",
        "OPENAI_BASE_URL": "https://openrouter.ai/api/v1",
        "LLM_MODEL": "qwen/qwen-2.5-7b-instruct:free",
    }

    with patch.dict(os.environ, env_vars, clear=True):
        from config.settings import Settings

        settings = Settings(_env_file=None)

        assert settings.openai_api_key == "sk-or-v1-env-key"
        assert settings.openai_base_url == "https://openrouter.ai/api/v1"
        assert settings.llm_model == "qwen/qwen-2.5-7b-instruct:free"
