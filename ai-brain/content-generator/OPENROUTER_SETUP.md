# OpenRouter Setup Guide

This guide helps you configure the AI Content Generator to use OpenRouter's FREE models.

## Quick Setup

### 1. Get Your FREE API Key

1. Visit https://openrouter.ai/
2. Sign up for a free account
3. Get your API key from https://openrouter.ai/keys
4. Your key will start with `sk-or-v1-`

### 2. Configure Your Environment

Create or edit your `.env` file:

```bash
# LLM Provider (use 'openai' for OpenRouter)
LLM_PROVIDER=openai

# OpenRouter Configuration
OPENAI_API_KEY=sk-or-v1-your-actual-key-here
OPENAI_BASE_URL=https://openrouter.ai/api/v1

# Choose a FREE model (recommended)
LLM_MODEL=google/gemini-2.0-flash-exp:free

# Optional: Adjust generation parameters
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=2048
LLM_TIMEOUT=60
```

### 3. Available FREE Models

OpenRouter provides several FREE models you can use:

| Model | Description | Best For |
|-------|-------------|----------|
| `google/gemini-2.0-flash-exp:free` | Google's latest experimental model (default) | Advanced reasoning |
| `meta-llama/llama-3.2-3b-instruct:free` | Fast, efficient 3B model | General purpose, quick responses |
| `meta-llama/llama-3.2-1b-instruct:free` | Very fast 1B model | Simple tasks, maximum speed |
| `google/gemini-flash-1.5:free` | Fast Google model | Quick tasks |
| `qwen/qwen-2.5-7b-instruct:free` | Alibaba's 7B model | Balanced performance |
| `nousresearch/hermes-3-llama-3.1-405b:free` | Large 405B model | Complex tasks |

**Note**: Model availability may change. Check https://openrouter.ai/models for the latest list.

## Troubleshooting

### Error: "404 - No endpoints found for model"

**Cause**: The model name is incorrect or no longer available.

**Solution**: 
1. Try one of the verified models listed above
2. Check https://openrouter.ai/models for current free models
3. Look for models with the `:free` suffix

### Error: "Authentication failed" or "401"

**Cause**: Missing or invalid API key, or missing required OpenRouter headers.

**Solution**:
1. Verify your API key starts with `sk-or-v1-`
2. Check that `OPENAI_API_KEY` is set in your `.env` file
3. Ensure `OPENAI_BASE_URL` is set to `https://openrouter.ai/api/v1`
4. Make sure you're using an up-to-date version of the code that includes OpenRouter headers (HTTP-Referer and X-Title)
5. Regenerate your API key at https://openrouter.ai/keys if needed

### Error: "Connection failed"

**Cause**: Network issues or incorrect base URL.

**Solution**:
1. Verify `OPENAI_BASE_URL=https://openrouter.ai/api/v1`
2. Check your internet connection
3. Ensure no firewall is blocking the connection

### Error: "Rate limit exceeded"

**Cause**: Too many requests to OpenRouter.

**Solution**:
1. Wait a few minutes before trying again
2. Free tier has rate limits - space out your requests
3. Consider upgrading your OpenRouter plan for higher limits

## Testing Your Setup

Test your configuration with a simple request:

```bash
cd ai-brain/content-generator

# Test the settings load correctly
python -c "
from config.settings import Settings
settings = Settings()
print(f'Provider: {settings.llm_provider}')
print(f'Model: {settings.llm_model}')
print(f'Base URL: {settings.openai_base_url}')
print(f'API Key: {settings.openai_api_key[:20]}...')
"

# Run the test suite
pytest tests/unit/test_openrouter_config.py -v
```

## Using Different Models

To try a different model, simply update your `.env` file:

```bash
# Try Google's Gemini model
LLM_MODEL=google/gemini-2.0-flash-exp:free

# Or try the larger Hermes model
LLM_MODEL=nousresearch/hermes-3-llama-3.1-405b:free
```

Restart your application after changing the model.

## Using Direct OpenAI Instead

If you have an OpenAI API key and want to use GPT models:

```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-openai-key-here
OPENAI_BASE_URL=https://api.openai.com/v1
LLM_MODEL=gpt-4-turbo-preview
```

**Note**: OpenAI models are NOT free and require credits.

## Need Help?

- OpenRouter Documentation: https://openrouter.ai/docs
- OpenRouter Discord: https://discord.gg/openrouter
- Check model availability: https://openrouter.ai/models
- Report issues: https://github.com/gowrishn17/honeypot_ai/issues
