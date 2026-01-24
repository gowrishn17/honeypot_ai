"""
Honeytoken generator for fake credentials and secrets.
"""

import random
import secrets
import string
from typing import Any

from .base import BaseGenerator, GeneratedContent


class HoneytokenGenerator(BaseGenerator):
    """Generate realistic but fake honeytokens."""

    def get_system_prompt(self) -> str:
        """Honeytokens don't use LLM, so this returns empty."""
        return ""

    def build_prompt(self, context: dict[str, Any]) -> str:
        """Honeytokens don't use LLM prompts."""
        return ""

    async def generate(self, context: dict[str, Any]) -> GeneratedContent:
        """
        Generate honeytoken.

        Args:
            context: Must contain 'token_type':
                - aws_access_key
                - aws_secret_key
                - github_token
                - ssh_private_key
                - database_password
                - api_token
                - jwt_secret

        Returns:
            GeneratedContent with honeytoken
        """
        token_type = context.get("token_type", "api_token")
        
        generators = {
            "aws_access_key": self._generate_aws_access_key,
            "aws_secret_key": self._generate_aws_secret_key,
            "github_token": self._generate_github_token,
            "ssh_private_key": self._generate_ssh_private_key,
            "database_password": self._generate_database_password,
            "api_token": self._generate_api_token,
            "jwt_secret": self._generate_jwt_secret,
        }
        
        generator = generators.get(token_type, self._generate_api_token)
        token_content = generator(context)
        
        # Validate
        validation_results = await self._validate_content(
            content=token_content,
            file_type="generic",
            context=context,
        )
        
        return self._create_content(
            content=token_content,
            content_type="honeytoken",
            file_type="generic",
            validation_results=validation_results,
            token_type=token_type,
            is_honeytoken=True,
        )

    def _generate_aws_access_key(self, context: dict[str, Any]) -> str:
        """Generate fake AWS access key (AKIA format)."""
        chars = string.ascii_uppercase + string.digits
        key_id = "AKIA" + ''.join(random.choices(chars, k=16))
        return key_id

    def _generate_aws_secret_key(self, context: dict[str, Any]) -> str:
        """Generate fake AWS secret key."""
        chars = string.ascii_letters + string.digits + "+/="
        return ''.join(random.choices(chars, k=40))

    def _generate_github_token(self, context: dict[str, Any]) -> str:
        """Generate fake GitHub personal access token (ghp_ format)."""
        chars = string.ascii_letters + string.digits
        token = "ghp_" + ''.join(random.choices(chars, k=36))
        return token

    def _generate_ssh_private_key(self, context: dict[str, Any]) -> str:
        """Generate fake SSH private key structure."""
        # Generate fake key data
        key_data_lines = []
        chars = string.ascii_letters + string.digits + "+/="
        
        for _ in range(25):
            line = ''.join(random.choices(chars, k=64))
            key_data_lines.append(line)
        
        # Last line is shorter
        key_data_lines.append(''.join(random.choices(chars, k=random.randint(20, 40))))
        
        key = "-----BEGIN OPENSSH PRIVATE KEY-----\n"
        key += "\n".join(key_data_lines)
        key += "\n-----END OPENSSH PRIVATE KEY-----\n"
        
        return key

    def _generate_database_password(self, context: dict[str, Any]) -> str:
        """Generate realistic but fake database password."""
        # Mix of uppercase, lowercase, numbers, and special chars
        parts = [
            ''.join(random.choices(string.ascii_uppercase, k=3)),
            ''.join(random.choices(string.ascii_lowercase, k=5)),
            ''.join(random.choices(string.digits, k=3)),
            ''.join(random.choices("!@#$%^&*", k=2)),
        ]
        random.shuffle(parts)
        return ''.join(parts)

    def _generate_api_token(self, context: dict[str, Any]) -> str:
        """Generate generic API token."""
        return secrets.token_urlsafe(32)

    def _generate_jwt_secret(self, context: dict[str, Any]) -> str:
        """Generate JWT secret."""
        return secrets.token_urlsafe(48)
