---
name: modal-serverless-gpu
title: "Modal Serverless Gpu"
description: "Serverless GPU cloud platform for running ML workloads. Use when you need on-demand GPU access without infrastructure management, deploying ML models as APIs, or running batch jobs with automatic scaling."
version: 1.0.0
author: "Orchestra Research"
license: MIT
tags: [imported]
metadata:
  hermes:
    tags: [imported]
---
# Modal Serverless GPU

Comprehensive guide to running ML workloads on Modal's serverless GPU cloud platform.

## When to Use
- Running GPU-intensive ML workloads without managing infrastructure
- Deploying ML models as auto-scaling APIs
- Running batch processing jobs (training, inference, data processing)
- Need pay-per-second GPU pricing without idle costs
- Prototyping ML applications quickly
- Running scheduled jobs (cron-like workloads)

## Quick Start

### Install
```bash
pip install modal
modal setup  # Browser auth
```

### Hello World GPU
```python
import modal
app = modal.App("hello-gpu")

@app.function(gpu="T4")
def gpu_info():
    import subprocess
    return subprocess.run(["nvidia-smi"], capture_output=True, text=True).stdout

@app.local_entrypoint()
def main():
    print(gpu_info.remote())
```
Run: `modal run hello_gpu.py`

### Inference Endpoint
```python
import modal
app = modal.App("text-generation")
image = modal.Image.debian_slim().pip_install("transformers", "torch", "accelerate")

@app.cls(gpu="A10G", image=image)
class TextGenerator:
    @modal.enter()
    def load_model(self):
        from transformers import pipeline
        self.pipe = pipeline("text-generation", model="gpt2", device=0)

    @modal.method()
    def generate(self, prompt: str) -> str:
        return self.pipe(prompt, max_length=100)[0]["generated_text"]

@app.local_entrypoint()
def main():
    print(TextGenerator().generate.remote("Hello, world"))
```

## Core Components
| Component | Purpose |
|-----------|---------|
| `App` | Container for functions/resources |
| `Function` | Serverless function with compute specs |
| `Cls` | Class-based functions with lifecycle hooks |
| `Image` | Container image definition |
| `Volume` | Persistent storage |
| `Secret` | Secure credential storage |

## Execution Modes
| Command | Description |
|---------|-------------|
| `modal run script.py` | Execute and exit |
| `modal serve script.py` | Dev with live reload |
| `modal deploy script.py` | Persistent cloud deployment |

## GPU Config
| GPU | VRAM | Best For |
|-----|------|----------|
| `T4` | 16GB | Budget inference |
| `L4` | 24GB | Inference, Ada Lovelace |
| `A10G` | 24GB | Training/inference |
| `L40S` | 48GB | Best cost/perf inference |
| `A100-40/80GB` | 40/80GB | Large model training |
| `H100` | 80GB | Fastest, FP8 |
| `H200` | 141GB | 4.8TB/s bandwidth |
| `B200` | Latest | Blackwell |

```python
@app.function(gpu="A100")           # Single
@app.function(gpu="H100:4")         # Multi (≤8)
@app.function(gpu=["H100","A100"])  # With fallbacks
@app.function(gpu="any")            # Any available
```

## Container Images
```python
image = modal.Image.debian_slim(python_version="3.11").pip_install("torch", "transformers")
image = modal.Image.from_registry("nvidia/cuda:12.1.0-cudnn8-devel", add_python="3.11").pip_install("torch")
image = modal.Image.debian_slim().apt_install("git", "ffmpeg").pip_install("whisper")
```

## Persistent Storage
```python
volume = modal.Volume.from_name("model-cache", create_if_missing=True)

@app.function(gpu="A10G", volumes={"/models": volume})
def load_model():
    import os
    model_path = "/models/llama-7b"
    if not os.path.exists(model_path):
        model = download_model()
        model.save_pretrained(model_path)
        volume.commit()
    return load_from_path(model_path)
```

## Web Endpoints
```python
# Simple
@app.function()
@modal.fastapi_endpoint(method="POST")
def predict(text: str) -> dict:
    return {"result": model.predict(text)}

# Full FastAPI
from fastapi import FastAPI
web_app = FastAPI()
@web_app.post("/predict")
async def predict(text: str):
    return {"result": await model.predict.remote.aio(text)}
@app.function()
@modal.asgi_app()
def fastapi_app():
    return web_app
```

| Decorator | Use Case |
|-----------|----------|
| `@modal.fastapi_endpoint()` | Function → API |
| `@modal.asgi_app()` | Full FastAPI apps |
| `@modal.wsgi_app()` | Django/Flask |
| `@modal.web_server(port)` | Arbitrary HTTP servers |

## Dynamic Batching
```python
@app.function()
@modal.batched(max_batch_size=32, wait_ms=100)
async def batch_predict(inputs: list[str]) -> list[dict]:
    return model.batch_predict(inputs)
```

## Secrets
```bash
modal secret create huggingface HF_TOKEN=hf_xxx...ndef download_model():
    import os
    token = os.environ["HF_TOKEN"]
```

## Scheduling
```python
@app.function(schedule=modal.Cron("0 0 * * *"))  # Daily
def daily_job(): pass

@app.function(schedule=modal.Period(hours=1))
def hourly_job(): pass
```

## Performance
```python
@app.function(container_idle_timeout=300, allow_concurrent_inputs=10)
def inference(): pass

@app.cls(gpu="A100")
class Model:
    @modal.enter()
    def load(self): self.model = load_model()
    @modal.method()
    def predict(self, x): return self.model(x)
```

## Common Issues
| Issue | Solution |
|-------|----------|
| Cold start latency | Increase `container_idle_timeout`, use `@modal.enter()` |
| GPU OOM | Larger GPU, gradient checkpointing |
| Image build fails | Pin versions, check CUDA compatibility |
| Timeout errors | Increase `timeout`, add checkpointing |

## Skills Required
| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Diagnose cold start, GPU OOM, image build failures |
| `context7` | Look up current Modal API documentation |

## Pitfalls
- **Cold starts**: Use `container_idle_timeout` + `@modal.enter()` for preloading
- **GPU OOM**: Switch to larger GPU or enable gradient checkpointing
- **Image builds**: Pin versions, check CUDA compatibility
- **Detailed examples**: Advanced usage, troubleshooting in `references/`

## Verification Checklist
- [ ] `modal setup` completed and authenticated
- [ ] Hello World GPU test passes (`modal run hello_gpu.py`)
- [ ] Image builds successfully with all dependencies
- [ ] Web endpoint deploys and responds
- [ ] Secrets configured via `modal secret create`

## References
- **[Advanced Usage](references/advanced-usage.md)** - Multi-GPU, distributed training, cost optimization
- **[Troubleshooting](references/troubleshooting.md)** - Common issues and solutions
