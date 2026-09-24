"""Model configs and pair presets for Dual LLM Pro Max"""

MODEL_CONFIGS = {
    "gpt-4o": {
        "provider": "openai_compatible",
        "base_url": "https://api.openai.com/v1",
        "api_key_env": "OPENAI_API_KEY",
        "model": "gpt-4o",
        "label": "GPT-4o (ChatGPT)"
    },
    "o1": {
        "provider": "openai_compatible",
        "base_url": "https://api.openai.com/v1",
        "api_key_env": "OPENAI_API_KEY",
        "model": "o1",
        "label": "o1 (ChatGPT Reasoning)"
    },
    "gpt-4o-mini": {
        "provider": "openai_compatible",
        "base_url": "https://api.openai.com/v1",
        "api_key_env": "OPENAI_API_KEY",
        "model": "gpt-4o-mini",
        "label": "GPT-4o Mini"
    },
    "claude-sonnet": {
        "provider": "anthropic",
        "api_key_env": "ANTHROPIC_API_KEY",
        "model": "claude-sonnet-4-20250514",
        "label": "Claude Sonnet 4"
    },
    "claude-opus": {
        "provider": "anthropic",
        "api_key_env": "ANTHROPIC_API_KEY",
        "model": "claude-opus-4-20250514",
        "label": "Claude Opus 4"
    },
    "gemini-2.0-flash": {
        "provider": "openai_compatible",
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
        "api_key_env": "GOOGLE_API_KEY",
        "model": "gemini-2.0-flash",
        "label": "Gemini 2.0 Flash"
    },
    "gemini-2.5-pro": {
        "provider": "openai_compatible",
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai/",
        "api_key_env": "GOOGLE_API_KEY",
        "model": "gemini-2.5-pro-preview-06-05",
        "label": "Gemini 2.5 Pro"
    },
    "grok-3": {
        "provider": "openai_compatible",
        "base_url": "https://api.x.ai/v1",
        "api_key_env": "XAI_API_KEY",
        "model": "grok-3",
        "label": "Grok 3 (xAI)"
    },
    "ollama-llama3.1": {
        "provider": "openai_compatible",
        "base_url": "http://localhost:11434/v1",
        "api_key_env": None,
        "model": "llama3.1:70b",
        "label": "Ollama Llama 3.1 70B"
    },
    "ollama-qwen2.5": {
        "provider": "openai_compatible",
        "base_url": "http://localhost:11434/v1",
        "api_key_env": None,
        "model": "qwen2.5:72b",
        "label": "Ollama Qwen 2.5 72B"
    },
    "lmstudio": {
        "provider": "openai_compatible",
        "base_url": "http://localhost:1234/v1",
        "api_key_env": None,
        "model": "local-model",
        "label": "LM Studio (Local)"
    },
}

PAIR_PRESETS = {
    "chatgpt_claude": {
        "a": "gpt-4o", "b": "claude-sonnet",
        "title": "ChatGPT + Claude",
        "desc": "Strong general ability + careful analysis (recommended default)"
    },
    "claude_gemini": {
        "a": "claude-sonnet", "b": "gemini-2.0-flash",
        "title": "Claude + Gemini",
        "desc": "Structured reasoning + fast multimodal Google model"
    },
    "gemini_grok": {
        "a": "gemini-2.0-flash", "b": "grok-3",
        "title": "Gemini + Grok",
        "desc": "Google speed + truth-seeking unfiltered style"
    },
    "chatgpt_gemini": {
        "a": "gpt-4o", "b": "gemini-2.0-flash",
        "title": "ChatGPT + Gemini",
        "desc": "OpenAI + Google — broad knowledge and speed"
    },
    "chatgpt_grok": {
        "a": "gpt-4o", "b": "grok-3",
        "title": "ChatGPT + Grok",
        "desc": "Polished GPT answers refined by Grok's perspective"
    },
    "claude_grok": {
        "a": "claude-sonnet", "b": "grok-3",
        "title": "Claude + Grok",
        "desc": "Careful analysis + maximal truth-seeking"
    },
    "o1_claude": {
        "a": "o1", "b": "claude-sonnet",
        "title": "o1 + Claude",
        "desc": "Deep reasoning first, then structured critique"
    },
    "o1_gemini": {
        "a": "o1", "b": "gemini-2.0-flash",
        "title": "o1 + Gemini",
        "desc": "OpenAI reasoning + Google synthesis"
    },
    "claude_opus_gpt": {
        "a": "claude-opus", "b": "gpt-4o",
        "title": "Claude Opus + ChatGPT",
        "desc": "Top-tier Claude depth + GPT versatility"
    },
    "gemini_pro_claude": {
        "a": "gemini-2.5-pro", "b": "claude-sonnet",
        "title": "Gemini Pro + Claude",
        "desc": "Google Pro reasoning + Claude refinement"
    },
    "universal": {
        "a": "gpt-4o", "b": "claude-sonnet",
        "title": "Universal (Any + Any)",
        "desc": "Pick any Model A and any Model B freely"
    },
}
