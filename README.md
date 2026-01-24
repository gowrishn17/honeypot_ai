# Honeypot AI - Production-Grade Deception Platform

A sophisticated honeypot ecosystem powered by Generative AI for creating realistic synthetic decoys and tracking attacker behavior.

## 🎯 Overview

Honeypot AI is a next-generation deception platform that uses Large Language Models (LLMs) to automatically generate realistic:
- Source code (Python, JavaScript, Shell, Go)
- Configuration files (.bashrc, .env, nginx.conf, etc.)
- System logs (auth.log, syslog, bash_history)
- User documents (notes, todos, meeting logs)
- **Honeytokens** - Trackable fake credentials (AWS keys, SSH keys, API tokens)

## 🏗️ Architecture

```
honeypot_ai/
├── ai-brain/              # Phase 2: AI Content Generator
│   └── content-generator/ # LLM-powered content generation service
├── honeypots/             # Phase 1: Honeypot implementations
│   ├── ssh/              # SSH honeypot
│   └── web/              # Web application honeypot
├── intelligence-hub/      # Phase 3: Analytics and monitoring
└── docs/                  # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- OpenAI API key (or local Ollama installation)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/gowrishn17/honeypot_ai.git
cd honeypot_ai
```

2. **Configure environment**
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

3. **Start the services**
```bash
docker-compose up -d
```

4. **Verify the AI Brain is running**
```bash
curl http://localhost:8000/api/v1/health
```

## 📚 Phase Status

### ✅ Phase 2: AI Content Generator (Current)
The AI Brain service is fully operational and provides:
- **Content Generation API** - Generate realistic synthetic content
- **Filesystem Population** - Deploy content to honeypot filesystems
- **Honeytoken Management** - Create and track fake credentials
- **Multiple LLM Support** - OpenAI, Azure OpenAI, or local Ollama

### 🔄 Phase 1: Honeypot Infrastructure (Planned)
- SSH honeypot with realistic filesystem
- Web application honeypot
- Docker containerization

### 🔄 Phase 3: Intelligence Hub (Planned)
- Real-time attack monitoring
- Honeytoken usage detection
- Analytics dashboard
- Threat intelligence integration

## 🎨 Features

### Content Generation
Generate realistic content using AI:
```bash
# Generate a Python web application
curl -X POST http://localhost:8000/api/v1/generate/source-code \
  -H "Content-Type: application/json" \
  -d '{"language": "python", "type": "webapp", "context": "flask API server"}'

# Generate fake AWS credentials (honeytoken)
curl -X POST http://localhost:8000/api/v1/generate/honeytoken \
  -H "Content-Type: application/json" \
  -d '{"token_type": "aws_access_key"}'
```

### Population Profiles
Deploy complete realistic environments:
```bash
# Deploy a developer workstation profile
curl -X POST http://localhost:8000/api/v1/populate/honeypot-1/profile/developer_workstation

# Deploy a production server profile
curl -X POST http://localhost:8000/api/v1/populate/honeypot-1/profile/production_server
```

### Honeytoken Tracking
All generated credentials are tracked:
```bash
# List all honeytokens
curl http://localhost:8000/api/v1/honeytokens

# Check if a token was used
curl -X POST http://localhost:8000/api/v1/honeytokens/check \
  -d '{"token_value": "AKIA..."}'
```

## 🔧 Configuration

See [`.env.example`](.env.example) for all configuration options.

Key settings:
- `LLM_PROVIDER`: Choose between `openai`, `azure`, or `ollama`
- `OPENAI_API_KEY`: Your OpenAI API key
- `OPENAI_MODEL`: Model to use (default: `gpt-4-turbo-preview`)
- `DATABASE_URL`: SQLite database for honeytoken tracking

## 📖 Documentation

- [Architecture Overview](docs/architecture.md)
- [Phase Tracking](docs/phases.md)
- [AI Brain Documentation](ai-brain/content-generator/README.md)

## 🧪 Testing

```bash
cd ai-brain/content-generator
pytest tests/ -v --cov=. --cov-report=html
```

Target: 80%+ test coverage

## 🛡️ Security

**Important**: This system generates FAKE credentials (honeytokens) for deception purposes. 
- Never use generated credentials in production systems
- All honeytokens are tracked and monitored
- Validators ensure no real secrets are accidentally leaked

## 🤝 Contributing

This is a proof-of-concept implementation. Contributions welcome!

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

Built with:
- FastAPI - Modern Python web framework
- OpenAI GPT-4 - Content generation
- Pydantic - Data validation
- SQLAlchemy - Database ORM
- Jinja2 - Template engine

---

**⚠️ Disclaimer**: This software is for authorized security research and testing only. Deploying honeypots may be subject to legal restrictions in your jurisdiction.