# config.py - Centralized Configuration for the Generalist LLM Endpoints.
import os

# 1. API Configuration Object
# This dictionary stores endpoints, dummy keys, and targeted open-weight model layouts.
MODELS = {
    "local_cheap": {
        # Points to your local machine serving framework or your raw AMD Cloud pod vLLM instance.
        "url": os.getenv("AMD_LOCAL_API_URL", "http://localhost:8000/v1"),
        "key": "fake-local-key",
        "name": "meta-llama/Llama-3-8B-Instruct"
    },
        "remote_premium": {
        # Points directly to the official Fireworks AI managed inference infrastructure engine.
        "url": "http://localhost:8000/v1", # Replace with Fireworks API on Hackathon Day.
        "key": os.getenv("FIREWORKS_API_KEY", "mock-fireworks-token-for-prep"),
        # Using one of the two AMD-hardware optimized models available on Fireworks AI.
        "name": "accounts/fireworks/models/qwen2p5-coder-32b-instruct"
    }
}

# 2. Thresholds constraints for Track 1 Router Logic.
# If a prompt exceeds these metrics, it triggers specific conditional actions.
TOKEN_LIMIT_LOCAL = 150 # Max context token ceiling before routing to Fireworks AI.
MOCK_BUDGET_LIMIT = 5.00 # Total dollar threshold for judging safety calculations.
