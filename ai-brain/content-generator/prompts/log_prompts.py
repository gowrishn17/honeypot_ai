"""
Log file generation prompts.
"""

from typing import Any


def get_auth_log_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for auth.log."""
    duration_hours = context.get("duration_hours", 24)
    attack_activity = context.get("attack_activity", False)
    
    attack_note = ""
    if attack_activity:
        attack_note = "\n- Include failed SSH login attempts from suspicious IPs\n- Add some brute force patterns\n- Include blocked connection attempts"
    
    return f"""Generate realistic auth.log entries spanning {duration_hours} hours.
Include:
- Successful SSH logins from legitimate IPs
- PAM authentication events
- Sudo command executions
- User session opening/closing
- Cron job executions
- System service authentications{attack_note}
- Realistic timestamps in syslog format
- Mix of successful and failed events
- Different usernames (admin, deploy, ubuntu, etc.)
- Realistic IP addresses (both internal and external)
Make it look like real server authentication logs."""


def get_syslog_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for syslog."""
    duration_hours = context.get("duration_hours", 24)
    services = context.get("services", ["cron", "systemd", "kernel"])
    
    return f"""Generate realistic syslog entries spanning {duration_hours} hours.
Include entries from services: {', '.join(services)}
Include:
- Kernel messages (device events, network)
- Systemd service start/stop/reload
- Cron job executions
- Network interface events
- Disk I/O events
- System startup/shutdown messages
- Package manager operations
- Realistic timestamps
- Proper severity levels
- Realistic facility tags
Make it look like real system logs."""


def get_bash_history_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for bash history."""
    persona = context.get("persona", "developer")
    num_commands = context.get("num_commands", 100)
    
    return f"""Generate realistic bash history for a {persona} ({num_commands} commands).
Include:
- Git operations (clone, commit, push, pull, branch)
- File operations (ls, cd, cp, mv, cat, grep)
- Package management (apt, yum, pip, npm)
- Docker commands
- SSH connections
- Database queries
- Text editing (vim, nano)
- System monitoring (ps, top, df, netstat)
- Build commands (make, npm run, python)
- Some typos and corrected commands
- Repeated common commands
- Commands with sensitive info (accidentally typed passwords, then deleted)
Make it look authentic with realistic patterns."""


def get_apache_access_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for Apache access log."""
    duration_hours = context.get("duration_hours", 24)
    site_type = context.get("site_type", "web_app")
    
    return f"""Generate realistic Apache access log for a {site_type} spanning {duration_hours} hours.
Include:
- GET/POST requests to various endpoints
- Static file requests (css, js, images)
- API endpoint calls
- Different user agents (browsers, bots, curl)
- Mix of status codes (200, 304, 404, 500)
- Realistic IP addresses
- Referrer headers
- Request sizes
- Response times
- Some bot traffic
- Some suspicious scanning attempts
Use Combined Log Format."""


def get_nginx_access_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for nginx access log."""
    duration_hours = context.get("duration_hours", 24)
    site_type = context.get("site_type", "api")
    
    return f"""Generate realistic nginx access log for a {site_type} spanning {duration_hours} hours.
Include:
- HTTP/HTTPS requests
- API endpoints with different methods
- WebSocket upgrade requests
- Static asset requests
- Health check endpoints
- Load balancer traffic
- Different status codes (200, 201, 400, 401, 404, 500, 502, 503)
- Realistic IP addresses
- User agents
- Request IDs
- Upstream response times
- Some automated scanner traffic
Use nginx combined format with timing."""


def get_nginx_error_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for nginx error log."""
    duration_hours = context.get("duration_hours", 24)
    
    return f"""Generate realistic nginx error log spanning {duration_hours} hours.
Include:
- Upstream connection failures
- Timeout errors
- SSL handshake errors
- File not found errors
- Permission denied errors
- Client disconnects
- Rate limiting messages
- Memory/resource warnings
- Different error levels (error, warn, notice)
- Realistic timestamps
- Connection details
Make it look like real production errors."""


def get_application_log_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for application log."""
    app_type = context.get("app_type", "web_api")
    duration_hours = context.get("duration_hours", 24)
    
    return f"""Generate realistic application log for a {app_type} spanning {duration_hours} hours.
Include:
- INFO level: Request handling, operation success
- WARN level: Deprecated API usage, slow queries
- ERROR level: Exceptions, failed operations
- DEBUG level: Detailed execution flow
- Request IDs and correlation IDs
- Execution times
- Database query logs
- External API call logs
- User IDs and actions
- Stack traces for errors
- JSON structured logs
Make it look like real application logging."""


def get_database_log_prompt(context: dict[str, Any]) -> str:
    """Generate prompt for database log."""
    db_type = context.get("db_type", "postgresql")
    
    return f"""Generate realistic {db_type} log entries.
Include:
- Connection events
- Query execution logs
- Slow query warnings
- Index usage warnings
- Lock wait timeouts
- Transaction commits/rollbacks
- Checkpoint operations
- Vacuum operations
- Authentication success/failure
- Configuration changes
- Error messages with SQL states
- Performance statistics
Make it production-realistic."""
