"""
Population strategies for different honeypot profiles.
"""

from typing import Any

from core.llm_client import LLMClient
from generators.config_files import ConfigGenerator
from generators.honeytokens import HoneytokenGenerator
from generators.source_code import SourceCodeGenerator
from generators.system_logs import SystemLogGenerator
from generators.user_documents import UserDocumentGenerator

from .base import BasePopulator, PopulationResult
from .filesystem import FilesystemPopulator


class PopulationStrategy(BasePopulator):
    """Strategies for populating different honeypot types."""

    def __init__(self, llm_client: LLMClient, filesystem_populator: FilesystemPopulator):
        """Initialize strategy with generators."""
        self.llm_client = llm_client
        self.filesystem_populator = filesystem_populator
        
        # Initialize generators
        self.source_code_gen = SourceCodeGenerator(llm_client)
        self.config_gen = ConfigGenerator(llm_client)
        self.log_gen = SystemLogGenerator(llm_client)
        self.doc_gen = UserDocumentGenerator(llm_client)
        self.token_gen = HoneytokenGenerator(llm_client)

    async def populate(self, honeypot_id: str, context: dict[str, Any]) -> PopulationResult:
        """
        Populate using specified profile.

        Args:
            honeypot_id: Honeypot ID
            context: Must contain 'profile' key

        Returns:
            PopulationResult
        """
        profile = context.get("profile", "developer_workstation")
        
        strategies = {
            "developer_workstation": self._populate_developer,
            "production_server": self._populate_production,
            "database_server": self._populate_database,
            "web_server": self._populate_web_server,
        }
        
        strategy_func = strategies.get(profile, self._populate_developer)
        return await strategy_func(honeypot_id, context)

    async def _populate_developer(self, honeypot_id: str, context: dict[str, Any]) -> PopulationResult:
        """Populate developer workstation profile."""
        files = []
        
        # Source code
        for lang in ["python", "javascript"]:
            code = await self.source_code_gen.generate({
                "language": lang,
                "script_type": "webapp",
                "purpose": "API development",
            })
            files.append({
                "path": f"projects/app/src/main.{lang[:2]}",
                "content": code.content,
                "permissions": 0o644,
            })
        
        # Configuration files
        bashrc = await self.config_gen.generate({"config_type": "bashrc", "persona": "developer"})
        files.append({"path": ".bashrc", "content": bashrc.content, "permissions": 0o644})
        
        ssh_config = await self.config_gen.generate({"config_type": "ssh_config", "persona": "developer"})
        files.append({"path": ".ssh/config", "content": ssh_config.content, "permissions": 0o600})
        
        env = await self.config_gen.generate({"config_type": "env", "app_type": "web"})
        files.append({"path": "projects/app/.env", "content": env.content, "permissions": 0o600})
        
        # Documents
        notes = await self.doc_gen.generate({"doc_type": "notes", "persona": "developer"})
        files.append({"path": "Documents/dev-notes.txt", "content": notes.content, "permissions": 0o644})
        
        readme = await self.doc_gen.generate({"doc_type": "readme", "project_type": "web_api"})
        files.append({"path": "projects/app/README.md", "content": readme.content, "permissions": 0o644})
        
        # Bash history
        history = await self.log_gen.generate({"log_type": "bash_history", "persona": "developer"})
        files.append({"path": ".bash_history", "content": history.content, "permissions": 0o600})
        
        # Honeytokens
        aws_key = await self.token_gen.generate({"token_type": "aws_access_key"})
        github_token = await self.token_gen.generate({"token_type": "github_token"})
        
        # Deploy files
        return await self.filesystem_populator.populate(honeypot_id, {"files": files})

    async def _populate_production(self, honeypot_id: str, context: dict[str, Any]) -> PopulationResult:
        """Populate production server profile."""
        files = []
        
        # Server configs
        nginx = await self.config_gen.generate({"config_type": "nginx", "site_type": "web_app"})
        files.append({"path": "etc/nginx/sites-available/app.conf", "content": nginx.content, "permissions": 0o644})
        
        docker_compose = await self.config_gen.generate({"config_type": "docker_compose", "stack": "web"})
        files.append({"path": "app/docker-compose.yml", "content": docker_compose.content, "permissions": 0o644})
        
        # System logs
        auth_log = await self.log_gen.generate({"log_type": "auth", "duration_hours": 48, "attack_activity": True})
        files.append({"path": "var/log/auth.log", "content": auth_log.content, "permissions": 0o640})
        
        syslog = await self.log_gen.generate({"log_type": "syslog", "duration_hours": 48})
        files.append({"path": "var/log/syslog", "content": syslog.content, "permissions": 0o640})
        
        nginx_access = await self.log_gen.generate({"log_type": "nginx_access", "duration_hours": 24})
        files.append({"path": "var/log/nginx/access.log", "content": nginx_access.content, "permissions": 0o640})
        
        # Deployment script
        deploy_script = await self.source_code_gen.generate({
            "language": "shell",
            "script_type": "deployment",
            "purpose": "application deployment",
        })
        files.append({"path": "scripts/deploy.sh", "content": deploy_script.content, "permissions": 0o755})
        
        return await self.filesystem_populator.populate(honeypot_id, {"files": files})

    async def _populate_database(self, honeypot_id: str, context: dict[str, Any]) -> PopulationResult:
        """Populate database server profile."""
        files = []
        
        # Database scripts
        backup_script = await self.source_code_gen.generate({
            "language": "python",
            "script_type": "db_script",
            "purpose": "database backup",
        })
        files.append({"path": "scripts/backup_db.py", "content": backup_script.content, "permissions": 0o755})
        
        # Configuration
        env = await self.config_gen.generate({"config_type": "env", "app_type": "database"})
        files.append({"path": ".env", "content": env.content, "permissions": 0o600})
        
        # Logs
        auth_log = await self.log_gen.generate({"log_type": "auth", "duration_hours": 72})
        files.append({"path": "var/log/auth.log", "content": auth_log.content, "permissions": 0o640})
        
        # Honeytokens
        db_password = await self.token_gen.generate({"token_type": "database_password"})
        
        return await self.filesystem_populator.populate(honeypot_id, {"files": files})

    async def _populate_web_server(self, honeypot_id: str, context: dict[str, Any]) -> PopulationResult:
        """Populate web server profile."""
        files = []
        
        # Web application code
        app_code = await self.source_code_gen.generate({
            "language": "python",
            "script_type": "webapp",
            "purpose": "web API",
        })
        files.append({"path": "app/main.py", "content": app_code.content, "permissions": 0o644})
        
        # Nginx config
        nginx = await self.config_gen.generate({"config_type": "nginx", "site_type": "api"})
        files.append({"path": "nginx.conf", "content": nginx.content, "permissions": 0o644})
        
        # Access logs
        apache_log = await self.log_gen.generate({"log_type": "apache_access", "duration_hours": 24})
        files.append({"path": "logs/access.log", "content": apache_log.content, "permissions": 0o644})
        
        return await self.filesystem_populator.populate(honeypot_id, {"files": files})
