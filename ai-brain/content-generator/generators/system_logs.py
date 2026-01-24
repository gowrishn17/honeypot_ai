"""
System log generator.
"""

from typing import Any

from prompts.base_prompts import get_system_prompt
from prompts.log_prompts import (
    get_apache_access_prompt,
    get_auth_log_prompt,
    get_bash_history_prompt,
    get_nginx_access_prompt,
    get_syslog_prompt,
)

from .base import BaseGenerator, GeneratedContent


class SystemLogGenerator(BaseGenerator):
    """Generate realistic system log files."""

    def get_system_prompt(self) -> str:
        """Get system prompt for log generation."""
        return get_system_prompt("logs")

    def build_prompt(self, context: dict[str, Any]) -> str:
        """Build prompt for log generation."""
        log_type = context.get("log_type", "auth")
        
        prompt_builders = {
            "auth": get_auth_log_prompt,
            "syslog": get_syslog_prompt,
            "bash_history": get_bash_history_prompt,
            "apache_access": get_apache_access_prompt,
            "nginx_access": get_nginx_access_prompt,
        }
        
        builder = prompt_builders.get(log_type, get_auth_log_prompt)
        return builder(context)

    async def generate(self, context: dict[str, Any]) -> GeneratedContent:
        """
        Generate system log.

        Args:
            context: Must contain 'log_type' and optional params:
                - duration_hours: Duration of log entries
                - attack_activity: Include attack patterns

        Returns:
            GeneratedContent with log data
        """
        log_type = context.get("log_type", "auth")
        
        # Build and generate
        prompt = self.build_prompt(context)
        log_content = await self._generate_with_llm(prompt, temperature=0.9)
        
        # Validate
        validation_results = await self._validate_content(
            content=log_content,
            file_type="generic",
            context=context,
        )
        
        return self._create_content(
            content=log_content,
            content_type="logs",
            file_type="generic",
            validation_results=validation_results,
            log_type=log_type,
            duration_hours=context.get("duration_hours", 24),
        )
