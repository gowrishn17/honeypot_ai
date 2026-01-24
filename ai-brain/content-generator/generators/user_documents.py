"""
User document generator.
"""

from typing import Any

from prompts.base_prompts import get_system_prompt
from prompts.document_prompts import (
    get_notes_prompt,
    get_readme_prompt,
    get_todo_prompt,
)

from .base import BaseGenerator, GeneratedContent


class UserDocumentGenerator(BaseGenerator):
    """Generate realistic user documents."""

    def get_system_prompt(self) -> str:
        """Get system prompt for document generation."""
        return get_system_prompt("document")

    def build_prompt(self, context: dict[str, Any]) -> str:
        """Build prompt for document generation."""
        doc_type = context.get("doc_type", "notes")
        
        prompt_builders = {
            "notes": get_notes_prompt,
            "readme": get_readme_prompt,
            "todo": get_todo_prompt,
        }
        
        builder = prompt_builders.get(doc_type, get_notes_prompt)
        return builder(context)

    async def generate(self, context: dict[str, Any]) -> GeneratedContent:
        """
        Generate user document.

        Args:
            context: Must contain 'doc_type' and type-specific params

        Returns:
            GeneratedContent with document
        """
        doc_type = context.get("doc_type", "notes")
        
        # Build and generate
        prompt = self.build_prompt(context)
        document = await self._generate_with_llm(prompt, temperature=0.8)
        
        # Validate
        validation_results = await self._validate_content(
            content=document,
            file_type="generic",
            context=context,
        )
        
        return self._create_content(
            content=document,
            content_type="document",
            file_type="generic",
            validation_results=validation_results,
            doc_type=doc_type,
        )
