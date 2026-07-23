#!/usr/bin/env python3
"""Analyze HuggingFace models from saved JSON"""
import asyncio
import json
import sys

async def main():
    path = sys.argv[1] if len(sys.argv) > 1 else '/tmp/hf_models.json'
    loop = asyncio.get_running_loop()
    text = await loop.run_in_executor(None, _read_file, path)
    d = json.loads(text)

    if isinstance(d, dict):
        models = d.get('models', [])
    elif isinstance(d, list):
        models = d
    else:
        models = d.get('data', [])

    print(f'Total text-generation models returned: {len(models)}')
    print('Top 15 by downloads:')
    for m in models[:15]:
        mid = m.get('modelId', m.get('id', '?'))
        downloads = m.get('downloads', '?')
        likes = m.get('likes', '?')
        print(f'  {mid} - downloads: {downloads}, likes: {likes}')

    # Also look for conversational/instruct models specifically
    print('\nConversational/instruct models (by likes):')
    conv = sorted([m for m in models if any(t in m.get('tags', []) for t in ['conversational', 'chat', 'instruct'])], key=lambda x: x.get('likes', 0), reverse=True)
    for m in conv[:10]:
        mid = m.get('modelId', m.get('id', '?'))
        likes = m.get('likes', '?')
        print(f'  {mid} - likes: {likes}')

def _read_file(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    asyncio.run(main())
