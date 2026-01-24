"""
Dependency injection for FastAPI.
"""

from typing import AsyncGenerator

from config.settings import settings
from core.llm_client import LLMClient
from populator.filesystem import FilesystemPopulator
from populator.strategies import PopulationStrategy
from storage.generation_log import GenerationLog
from storage.honeytoken_store import HoneytokenStore


async def get_llm_client() -> AsyncGenerator[LLMClient, None]:
    """Get LLM client dependency."""
    client = LLMClient()
    try:
        yield client
    finally:
        await client.close()


def get_honeytoken_store() -> HoneytokenStore:
    """Get honeytoken store dependency."""
    return HoneytokenStore()


def get_generation_log() -> GenerationLog:
    """Get generation log dependency."""
    return GenerationLog()


def get_filesystem_populator() -> FilesystemPopulator:
    """Get filesystem populator dependency."""
    return FilesystemPopulator()


async def get_population_strategy(
    llm_client: LLMClient,
) -> PopulationStrategy:
    """Get population strategy dependency."""
    filesystem_populator = get_filesystem_populator()
    return PopulationStrategy(llm_client, filesystem_populator)
