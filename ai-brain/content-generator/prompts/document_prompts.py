"""
Document generation prompts.
"""

from typing import Any


def get_readme_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for README.md."""
    project_type = context.get("project_type", "web_application")
    tech_stack = context.get("tech_stack", "Python/Flask")
    
    return f"""Generate a realistic README.md for a {project_type} using {tech_stack}.
Include:
- Project title and description
- Features list
- Prerequisites
- Installation instructions
- Configuration section
- Usage examples
- API documentation (if applicable)
- Testing instructions
- Deployment notes
- Troubleshooting section
- Contributing guidelines
- License information
- Some TODOs or known issues
- Badges (build, coverage, version)
Make it look like real project documentation with some incompleteness."""


def get_notes_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for developer notes."""
    persona = context.get("persona", "developer")
    topic = context.get("topic", "current project")
    
    return f"""Generate realistic developer notes for a {persona} working on {topic}.
Include:
- Meeting notes
- Technical decisions and rationale
- Code snippets and examples
- Bug investigation notes
- Performance optimization ideas
- API endpoints documentation
- Database schema notes
- Deployment checklist
- Login credentials (as honeytokens)
- Quick commands and scripts
- Incomplete thoughts and TODOs
- Links to resources
- Timestamps and dates
Make it look like authentic working notes."""


def get_todo_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for TODO.md."""
    project_type = context.get("project_type", "web_application")
    
    return f"""Generate a realistic TODO.md for a {project_type}.
Include:
- High priority tasks
- Medium priority tasks
- Low priority/nice-to-have
- Completed tasks (checked off)
- Bug fixes needed
- Feature requests
- Technical debt items
- Refactoring tasks
- Testing improvements
- Documentation updates
- Performance optimizations
- Security improvements
- Some tasks with deadlines
- Some tasks assigned to people
- Use markdown checkboxes
Make it look like real project management."""


def get_api_docs_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for API documentation."""
    api_type = context.get("api_type", "REST")
    
    return f"""Generate realistic API documentation for a {api_type} API.
Include:
- Authentication section (API keys, OAuth)
- Base URLs (production, staging)
- Endpoint list with methods
- Request/response examples
- Error codes and messages
- Rate limiting information
- Versioning strategy
- Changelog
- Code examples in multiple languages
- Common use cases
- Webhook documentation
- Testing with curl examples
Make it comprehensive but realistic."""


def get_runbook_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for operations runbook."""
    service = context.get("service", "web application")
    
    return f"""Generate a realistic operations runbook for {service}.
Include:
- Service overview
- Architecture diagram (described)
- Monitoring and alerts
- Common issues and solutions
- Deployment procedures
- Rollback procedures
- Database backup/restore
- Log locations and analysis
- Performance troubleshooting
- Incident response steps
- Contact information
- On-call procedures
- Configuration management
- Credentials location (honeytokens)
Make it practical and detailed."""


def get_changelog_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for CHANGELOG.md."""
    project_name = context.get("project_name", "Application")
    versions = context.get("versions", 5)
    
    return f"""Generate a realistic CHANGELOG.md for {project_name} ({versions} recent versions).
Include:
- Version numbers (semantic versioning)
- Release dates
- Added features
- Changed functionality
- Deprecated items
- Removed features
- Fixed bugs
- Security patches
- Breaking changes
- Migration notes
Follow "Keep a Changelog" format.
Make it look like real project history."""


def get_architecture_doc_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for architecture documentation."""
    system_type = context.get("system_type", "microservices")
    
    return f"""Generate realistic architecture documentation for a {system_type} system.
Include:
- System overview
- Components and their responsibilities
- Technology stack
- Data flow diagrams (described)
- API contracts
- Database schemas
- Infrastructure setup
- Scaling strategy
- Security considerations
- Monitoring and logging
- Deployment architecture
- Trade-offs and decisions
- Future improvements
Make it technical and detailed."""
