#!/usr/bin/env python3
import asyncio, json, os, sys
sys.path.insert(0, os.environ.get("PYTHONPATH", "").split(os.pathsep)[0])
from openrouter_client_py import OpenRouterClient

prompt, model, max_tokens, temperature = sys.argv[1:5]
client = OpenRouterClient({"api_key": os.environ["OPENROUTER_API_KEY"]})

async def main():
    try:
        result = await client.chat_send(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=int(max_tokens),
            temperature=float(temperature),
        )
        out = {
            "output_text": result.choices[0].message.content if result.choices else "",
            "output_tokens": result.usage.completion_tokens if result.usage else None,
            "prompt_tokens": result.usage.prompt_tokens if result.usage else None,
            "model_id": result.model,
        }
        print(json.dumps(out))
    except Exception as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}), file=sys.stderr)
        sys.exit(1)

asyncio.run(main())
