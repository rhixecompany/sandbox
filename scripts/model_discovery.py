#!/usr/bin/env python3
"""Phase 1-2: Model Catalog Discovery & Free Model Extraction"""
import json
import os
import sys

WORKSPACE = r"C:\Users\Alexa\Desktop\SandBox"
CACHE = r"C:\Users\Alexa\AppData\Local\hermes\provider_models_cache.json"
OPENROUTER_MODELS = r"C:\Users\Alexa\Desktop\SandBox\openrouter_models.json"

def load_cache():
    with open(CACHE) as f:
        return json.load(f)

def load_openrouter_full():
    with open(OPENROUTER_MODELS) as f:
        return json.load(f)

def analyze_providers():
    cache = load_cache()
    
    print("=" * 80)
    print("PHASE 1: MODEL CATALOG DISCOVERY")
    print("=" * 80)
    
    providers_data = {}
    
    # 1. copilot
    print("\n--- Copilot (via GitHub Models / Azure AI) ---")
    copilot_models = cache.get('copilot', {}).get('models', [])
    providers_data['copilot'] = {
        'models': copilot_models,
        'count': len(copilot_models),
        'type': 'GitHub Copilot / Azure AI Inference',
        'auth': 'COPILOT_GITHUB_TOKEN (env) / gh auth token',
        'free_tier': 'Rate-limited per prior run (429)',
    }
    print(f"Total models: {len(copilot_models)}")
    for m in copilot_models:
        print(f"  - {m}")
    
    # 2. huggingface
    print("\n--- HuggingFace Inference Providers ---")
    hf_models = cache.get('huggingface', {}).get('models', [])
    providers_data['huggingface'] = {
        'models': hf_models,
        'count': len(hf_models),
        'type': 'HuggingFace Inference API',
        'auth': 'HF_TOKEN env var',
        'free_tier': 'Free Inference API with rate limits',
        'cred_status': 'Active (key in .env)',
    }
    print(f"Total models: {len(hf_models)}")
    for m in hf_models[:20]:
        print(f"  - {m}")
    if len(hf_models) > 20:
        print(f"  ... and {len(hf_models)-20} more")
    
    # 3. nous
    print("\n--- Nous Portal (OAuth) ---")
    providers_data['nous'] = {
        'models': [],
        'count': 0,
        'type': 'Nous Portal (OAuth device_code)',
        'auth': 'OAuth device_code flow',
        'free_tier': 'Unknown (subscription-based)',
        'cred_status': 'Active but hermes chat --provider nous timed out',
        'note': 'Cannot enumerate models directly; uses Portal subscription model'
    }
    print("Models: Not enumerable directly (OAuth Portal)")
    print("Status: Active (device_code OAuth) but chat connectivity times out")
    
    # 4. ollama-cloud
    print("\n--- Ollama Cloud ---")
    ollama_models = cache.get('ollama-cloud', {}).get('models', [])
    providers_data['ollama-cloud'] = {
        'models': ollama_models,
        'count': len(ollama_models),
        'type': 'Ollama Cloud API',
        'auth': 'OLLAMA_API_KEY env var',
        'free_tier': 'Some models free-tier; rate-limited',
        'cred_status': 'Active',
    }
    print(f"Total models: {len(ollama_models)}")
    for m in ollama_models[:15]:
        print(f"  - {m}")
    if len(ollama_models) > 15:
        print(f"  ... and {len(ollama_models)-15} more")
    
    # 5. openai-api
    print("\n--- OpenAI API ---")
    openai_models = cache.get('openai-api', {}).get('models', [])
    providers_data['openai-api'] = {
        'models': openai_models,
        'count': len(openai_models),
        'type': 'OpenAI API',
        'auth': 'api-key-1 (manual) + OPENAI_API_KEY env',
        'free_tier': 'No free tier (pay-per-use)',
        'cred_status': 'Keys present but NOT exported to subprocess env',
    }
    print(f"Total models: {len(openai_models)}")
    for m in openai_models:
        print(f"  - {m}")
    
    # 6. openrouter
    print("\n--- OpenRouter ---")
    or_models = cache.get('openrouter', {}).get('models', [])
    providers_data['openrouter'] = {
        'models': or_models,
        'count': len(or_models),
        'type': 'OpenRouter API',
        'auth': 'OPENROUTER_API_KEY (Hermes credential store, NOT subprocess env)',
        'free_tier': 'Free models available (prompt cost = 0)',
        'cred_status': 'Active (via hermes chat -q only)',
    }
    print(f"Cached models: {len(or_models)}")
    for m in or_models:
        print(f"  - {m}")
    
    # Full OpenRouter model list with pricing
    try:
        or_full = load_openrouter_full()
        or_data = or_full.get('data', [])
        print(f"\nFull OpenRouter catalog: {len(or_data)} models")
        free_or = [m for m in or_data if m.get('pricing', {}).get('prompt', '0') == '0']
        print(f"Free models (prompt cost = 0): {len(free_or)}")
        for m in free_or[:20]:
            ctx = m.get('context_length', '?')
            print(f"  - {m['id']}: context={ctx}")
        providers_data['openrouter']['free_models_count'] = len(free_or)
        providers_data['openrouter']['free_models'] = [m['id'] for m in free_or]
    except Exception as e:
        print(f"Could not load full OpenRouter data: {e}")
    
    return providers_data

if __name__ == '__main__':
    data = analyze_providers()
    
    print("\n" + "=" * 80)
    print("PHASE 2: FREE MODEL EXTRACTION")
    print("=" * 80)
    
    print("\n--- Copilot ---")
    print("Free models: N/A (Azure AI rate-limited; GitHub Copilot subscription-based)")
    
    print("\n--- HuggingFace Inference ---")
    print("Free models: All 123 models available via free Inference API")
    print("  (Rate-limited but free to use for inference)")
    
    print("\n--- Nous Portal ---")
    print("Free models: N/A (subscription-based OAuth portal)")
    
    print("\n--- Ollama Cloud ---")
    print("Free models: All 25 models runnable locally; cloud tier is pay-per-use")
    print("  Some models may have free usage limits")
    
    print("\n--- OpenAI API ---")
    print("Free models: N/A (pay-per-use; gpt-4o-mini is lowest cost)")
    
    print("\n--- OpenRouter ---")
    free_models = data.get('openrouter', {}).get('free_models', [])
    print(f"Free models: {len(free_models)}")
    for m in free_models:
        print(f"  - {m}")
