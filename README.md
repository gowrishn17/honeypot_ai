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
- OpenRouter API key (FREE models available) or OpenAI API key

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/gowrishn17/honeypot_ai.git
cd honeypot_ai
```

2. **Get a FREE OpenRouter API key**
   - Go to https://openrouter.ai/
   - Sign up for a free account
   - Get your API key from https://openrouter.ai/keys
   - OpenRouter provides access to FREE models like Llama 4 Scout and Devstral

3. **Configure environment**
```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY (from OpenRouter)
# The default configuration uses OpenRouter with free models
```

4. **Start the services**
```bash
docker-compose up -d
```

5. **Verify the AI Brain is running**
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
- `OPENAI_API_KEY`: Your OpenRouter or OpenAI API key
- `OPENAI_BASE_URL`: API base URL (default: `https://openrouter.ai/api/v1` for free models)
- `LLM_MODEL`: Model to use (default: `meta-llama/llama-4-scout:free`)
- `DATABASE_URL`: SQLite database for honeytoken tracking

### Using OpenRouter (FREE Models)
OpenRouter provides access to many FREE LLM models (as of January 2026):
- `meta-llama/llama-4-scout:free` (default) - MoE, 109B parameters
- `meta-llama/llama-4-maverick:free` - Sparse MoE, 400B parameters, multimodal
- `tngtech/deepseek-r1t-chimera:free` - MoE combining DeepSeek-R1 and DeepSeek-V3
- `mistralai/devstral-2-2512:free` - Dense transformer, 123B parameters, good for coding
- `z-ai/glm-4.5-air:free` - Lightweight agent-centric model

Get your free API key at https://openrouter.ai/keys

### Using OpenAI (Paid)
To use OpenAI directly:
```bash
OPENAI_API_KEY=sk-your-openai-key
OPENAI_BASE_URL=https://api.openai.com/v1
LLM_MODEL=gpt-4-turbo-preview
```

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