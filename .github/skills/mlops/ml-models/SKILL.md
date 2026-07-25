---
name: ml-models
title: ML Model Tooling (Hub, Inference, Tracking)
description: Operate ML models end-to-end — download from Hugging Face Hub, run local GGUF inference with llama.cpp, and track experiments with Weights & Biases.
license: MIT
author: Hermes Agent
version: 1.0.0
tags: [mlops, huggingface, llama-cpp, gguf, wandb, inference, experiment-tracking]
metadata:
  hermes:
    tags: [mlops, huggingface, llama-cpp, wandb]
---

# ML Model Tooling

Class-level umbrella for the practical "operate ML models" workflow: acquiring weights, running
local inference, and tracking experiments. The detailed command references live under `references/`.

Pick the subsection that matches the task:

- **Acquire / publish models & datasets** → Hugging Face Hub (`hf` CLI). See `references/huggingface-hub.md`.
- **Run local / on-device inference** (GGUF, OpenAI-compatible server, embeddings) → llama.cpp. See `references/llama-cpp.md`.
- **Track experiments, sweeps, artifacts** → Weights & Biases. See `references/weights-and-biases.md`.

## When to Use

- "Download / upload a model or dataset from Hugging Face"
- "Run a GGUF / llama.cpp model locally" or "serve an OpenAI-compatible endpoint"
- "Track training runs, log metrics, compare experiments with W&B"
- "Pick a quant / extract GGUFs from a repo"

## 1. Hugging Face Hub (`hf`) — quick orientation

```bash
hf auth login                       # store credentials
hf download <org>/<repo> --local-dir ./ckpt   # fetch weights/datasets
hf repo create <name> --repo-type model        # publish
hf upload <org>/<repo> ./local_path             # push
```

Auth, repo management, dataset/model interactions, discussions/PRs, storage automation, and global
flags are covered in `references/huggingface-hub.md`.

## 2. llama.cpp + GGUF — quick orientation

```bash
# Run directly from the Hub (no manual download)
llama-cli -hf <org>/<repo>/<file>.gguf -p "Hello"

# OpenAI-compatible server
llama-server -hf <org>/<repo>/<file>.gguf --port 8080
curl http://127.0.0.1:8080/v1/models     # verify

# Python bindings
from llama_cpp import Llama
llm = Llama(model_path="model.gguf", n_ctx=4096)
print(llm("Hello", max_tokens=32)["choices"][0]["text"])
```

Model discovery, quant selection, extracting GGUFs from a repo, streaming/chat/embeddings, and
server checks are in `references/llama-cpp.md`.

## 3. Weights & Biases — quick orientation

```python
import wandb
run = wandb.init(project="my-proj", config={"lr": 3e-4})
for step, loss in train():
    wandb.log({"loss": loss, "step": step})
run.finish()
```

Projects/runs, config tracking, metric logging, artifacts, sweeps, and the PyTorch training-loop
pattern are in `references/weights-and-biases.md`.

## Related Skills

- `ml-models` subsumes the former `huggingface-hub`, `llama-cpp`, `weights-and-biases` skills.
- Orphaned usage-only entries (no on-disk package) also belong to this class: `audiocraft-audio-generation`
  (MusicGen/AudioGen), `segment-anything-model` (SAM), `serving-llms-vllm` (vLLM serving).
- For training/fine-tuning workflows, see the `peft-fine-tuning`, `unsloth`, `simpo-training` skills.

## Reference Library

| File | Contents |
|------|----------|
| `references/huggingface-hub.md` | `hf` auth, repo management, datasets/models, discussions/PRs, storage automation, global flags |
| `references/llama-cpp.md` | Model discovery, install, Hub/server run, Python bindings, quant selection, GGUF extraction |
| `references/weights-and-biases.md` | Init/login, runs/projects, config + metric logging, artifacts, sweeps, PyTorch loop |
