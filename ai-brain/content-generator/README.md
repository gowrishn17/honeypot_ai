# AI-Powered Content Generator for Honeypot Systems

Production-grade AI content generator that creates realistic files, configurations, logs, documents, and honeytokens for honeypot deployments.

## Features

- **Multi-LLM Support**: OpenAI, Azure OpenAI, and Ollama
- **Content Generation**:
  - Source code (Python, JavaScript, Shell, Go)
  - Configuration files (.bashrc, ssh_config, nginx.conf, docker-compose.yml)
  - System logs (auth.log, syslog, bash_history, web server logs)
  - User documents (README.md, notes.txt, TODO.md)
  - Honeytokens (AWS keys, GitHub tokens, SSH keys, DB passwords)
- **Validation**: Syntax, realism scoring, and security checks
- **Filesystem Population**: Deploy with correct permissions and timestamps
- **Honeytoken Tracking**: SQLite database for tracking and alerting
- **RESTful API**: FastAPI with automatic OpenAPI documentation
- **Production-Ready**: Structured logging, error handling, async operations

## Architecture

```
┌─────────────┐
│  API Client │
└──────┬──────┘
       │
       v
┌─────────────────┐
│  FastAPI Routes │
└────────┬────────┘
         │
    ┌────┴────┐
    v         v
┌────────┐ ┌──────────┐
│  Gen   │ │ Populate │
└────┬───┘ └────┬─────┘
     │          │
     v          v
┌─────────┐ ┌──────────┐
│   LLM   │ │Filesystem│
│ Client  │ │Populator │
└────┬────┘ └────┬─────┘
     │           │
     v           v
┌──────────┐ ┌─────────┐
│Validators│ │ Storage │
└──────────┘ └─────────┘
```

## Quick Start

### Prerequisites

- Python 3.11+
- OpenAI API key (or Ollama for local LLM)

### Installation

```bash
# Clone repository
cd ai-brain/content-generator

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your API keys
```

### Run API Server

```bash
python main.py api
```

API will be available at:
- API: http://127.0.0.1:8000 or http://localhost:8000
- Docs: http://127.0.0.1:8000/docs or http://localhost:8000/docs
- Health: http://127.0.0.1:8000/api/v1/health

> **Note**: Use `http://127.0.0.1:8000` or `http://localhost:8000` in your browser, **NOT** `http://0.0.0.0:8000`.

### Docker Deployment

```bash
# Build image
docker build -t ai-content-generator .

# Run container
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=your_key_here \
  -v $(pwd)/data:/app/data \
  ai-content-generator
```

## API Endpoints

### Generation

- `POST /api/v1/generate/source-code` - Generate source code
- `POST /api/v1/generate/config` - Generate configuration files
- `POST /api/v1/generate/logs` - Generate system logs
- `POST /api/v1/generate/document` - Generate documents
- `POST /api/v1/generate/honeytoken` - Generate honeytokens

### Population

- `POST /api/v1/populate/{honeypot_id}` - Populate honeypot with custom content
- `POST /api/v1/populate/{honeypot_id}/profile/{profile}` - Use predefined profile

### Honeytokens

- `GET /api/v1/honeytokens` - List honeytokens
- `GET /api/v1/honeytokens/{token_id}` - Get honeytoken details
- `POST /api/v1/honeytokens/check` - Check if value is a honeytoken
- `DELETE /api/v1/honeytokens/{token_id}` - Deactivate honeytoken

### Health & Metrics

- `GET /api/v1/health` - Health check
- `GET /api/v1/metrics` - System metrics

## Usage Examples

### Generate Python Web App

```bash
curl -X POST http://localhost:8000/api/v1/generate/source-code \
  -H "Content-Type: application/json" \
  -d '{
    "language": "python",
    "script_type": "webapp",
    "purpose": "Flask API server"
  }'
```

### Populate Developer Workstation

```bash
curl -X POST http://localhost:8000/api/v1/populate/honeypot-001/profile/developer_workstation
```

### Check Honeytoken

```bash
curl -X POST http://localhost:8000/api/v1/honeytokens/check \
  -H "Content-Type: application/json" \
  -d '{
    "token_value": "AKIAIOSFODNN7EXAMPLE"
  }'
```

## Population Profiles

### Developer Workstation
- Python and JavaScript source code
- Git repositories and config files
- SSH config, .bashrc
- Development notes and TODOs
- Bash history with dev commands

### Production Server
- Nginx and Docker configurations
- System logs (auth, syslog, access logs)
- Deployment scripts
- Service configurations

### Database Server
- Database backup scripts
- Connection configuration with honeytokens
- Auth logs
- Monitoring scripts

### Web Server
- Web application code
- Server configurations
- Access and error logs
- SSL certificates

## Configuration

Key settings in `.env`:

```bash
# Choose LLM provider
LLM_PROVIDER=openai  # or azure_openai, ollama

# OpenAI settings
OPENAI_API_KEY=sk-...
LLM_MODEL=gpt-4
LLM_TEMPERATURE=0.7

# Database
DATABASE_URL=sqlite:///./data/honeypot.db

# Content quality
REALISM_THRESHOLD=0.7
UNIQUENESS_THRESHOLD=0.8
```

## Validation

All generated content goes through three validation layers:

1. **Syntax Validation**: Language-specific syntax checking
2. **Realism Scoring**: Entropy, patterns, structure (0.0-1.0 score)
3. **Security Validation**: Ensures no real secrets leaked

## Honeytoken Formats

Generated honeytokens follow real-world formats:

- AWS Access Key: `AKIA[A-Z0-9]{16}`
- GitHub Token: `ghp_[A-Za-z0-9]{36}`
- SSH Private Key: OpenSSH format
- Database Password: Complex with special chars
- API Token: URL-safe base64
- JWT Secret: 48-byte URL-safe string

## Development

### Run Tests

```bash
pytest tests/ -v --cov=.
```

### Code Quality

```bash
# Format code
black .

# Lint
ruff check .

# Type checking
mypy .
```

### Project Structure

```
ai-brain/content-generator/
├── config/          # Settings and logging
├── core/            # LLM client, exceptions, utils
├── generators/      # Content generators
├── validators/      # Validation logic
├── prompts/         # LLM prompts
├── templates/       # Jinja2 templates
├── storage/         # Database models
├── populator/       # Filesystem deployment
├── api/             # FastAPI application
│   ├── routes/      # API endpoints
│   └── schemas/     # Request/response models
└── main.py          # Entry point
```

## Security

- **No Real Secrets**: Security validator blocks real credentials
- **Honeytoken Marking**: All honeytokens logged and tracked
- **Input Validation**: Pydantic models for all inputs
- **Rate Limiting**: Configurable request limits
- **Audit Logging**: Structured JSON logs for all operations

## Performance

- **Async Operations**: Full async/await for I/O
- **Retry Logic**: Exponential backoff for LLM failures
- **Caching**: Optional response caching
- **Connection Pooling**: Database connection pooling

## Monitoring

Structured JSON logging includes:

```json
{
  "event": "content_generated",
  "content_type": "source_code",
  "validation_score": 0.95,
  "generation_time_ms": 1234,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

Alert on:
- Honeytoken access (`honeytoken_accessed`)
- Validation failures (`validation_failed`)
- LLM errors (`llm_error`)

## Troubleshooting

### LLM Connection Errors

```bash
# Test LLM connectivity
curl http://localhost:8000/api/v1/health
```

Check `LLM_PROVIDER` and API keys in `.env`.

### Database Issues

```bash
# Reset database
rm data/honeypot.db
# Restart application to recreate
```

### Low Realism Scores

Adjust in `.env`:
```bash
REALISM_THRESHOLD=0.6  # Lower threshold
LLM_TEMPERATURE=0.9    # More creative output
```

## License

[Your License Here]

## Support

For issues and questions:
- GitHub Issues: [Your Repo]
- Documentation: http://localhost:8000/docs (when running)

## Roadmap

- [ ] Template system for customization
- [ ] More language support (Java, C++, Rust)
- [ ] Advanced consistency rules
- [ ] Metrics dashboard
- [ ] Integration with SIEM systems
