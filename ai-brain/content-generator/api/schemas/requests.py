"""
Pydantic request models for API endpoints.
"""

from typing import Any, Optional

from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    """Base request for content generation."""

    context: dict[str, Any] = Field(default_factory=dict, description="Generation context parameters")
    honeypot_id: Optional[str] = Field(None, description="Associated honeypot ID")


class SourceCodeRequest(GenerateRequest):
    """Request for source code generation."""

    language: str = Field(..., description="Programming language (python, javascript, shell, go)")
    script_type: Optional[str] = Field(None, description="Type of script (webapp, cli, etc.)")
    purpose: Optional[str] = Field(None, description="Purpose description")


class ConfigRequest(GenerateRequest):
    """Request for configuration file generation."""

    config_type: str = Field(..., description="Config type (bashrc, ssh_config, env, nginx, docker_compose)")
    persona: Optional[str] = Field("developer", description="User persona")


class LogRequest(GenerateRequest):
    """Request for log file generation."""

    log_type: str = Field(..., description="Log type (auth, syslog, bash_history, apache_access, nginx_access)")
    duration_hours: int = Field(24, description="Duration in hours", ge=1, le=168)
    attack_activity: bool = Field(False, description="Include attack patterns")


class DocumentRequest(GenerateRequest):
    """Request for document generation."""

    doc_type: str = Field(..., description="Document type (notes, readme, todo)")
    persona: Optional[str] = Field("developer", description="User persona")
    topic: Optional[str] = Field(None, description="Document topic")


class HoneytokenRequest(GenerateRequest):
    """Request for honeytoken generation."""

    token_type: str = Field(
        ...,
        description="Token type (aws_access_key, github_token, ssh_private_key, database_password, api_token)",
    )


class PopulateRequest(BaseModel):
    """Request for honeypot population."""

    profile: str = Field(
        "developer_workstation",
        description="Population profile (developer_workstation, production_server, database_server, web_server)",
    )
    custom_files: list[dict[str, Any]] = Field(
        default_factory=list,
        description="Additional custom files to include",
    )
    context: dict[str, Any] = Field(default_factory=dict, description="Additional context")


class HoneytokenCheckRequest(BaseModel):
    """Request to check if token is a honeytoken."""

    token_value: str = Field(..., description="Token value to check")
