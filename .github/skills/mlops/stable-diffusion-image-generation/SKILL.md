---
name: stable-diffusion-image-generation
title: "Stable Diffusion Image Generation"
description: State-of-the-art text-to-image generation with Stable Diffusion models via HuggingFace Diffusers. Use when generating images from text prompts, performing image-to-image translation, inpainting, or building custom diffusion pipelines.
version: 1.0.0
author: Orchestra Research
license: MIT
dependencies: [diffusers>=0.30.0, transformers>=4.41.0, accelerate>=0.31.0, torch>=2.0.0]
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Image Generation, Stable Diffusion, Diffusers, Text-to-Image, Multimodal, Computer Vision]
---

# Stable Diffusion Image Generation

## When to Use
- Generating images from text descriptions
- Image-to-image translation (style transfer, enhancement)
- Inpainting (filling masked regions)
- Outpainting (extending images)
- Creating variations
- Custom image generation workflows

## Quick Start

### Install
```bash
pip install diffusers transformers accelerate torch
pip install xformers  # Optional: memory-efficient attention
```

### Basic Text-to-Image (SD 1.5)
```python
from diffusers import DiffusionPipeline
import torch

pipe = DiffusionPipeline.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cuda")

image = pipe("A serene mountain landscape at sunset, highly detailed",
    num_inference_steps=50, guidance_scale=7.5).images[0]
image.save("output.png")
```

### Using SDXL (Higher Quality)
```python
from diffusers import AutoPipelineForText2Image
import torch

pipe = AutoPipelineForText2Image.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16, variant="fp16"
).to("cuda")

pipe.enable_model_cpu_offload()  # Essential for limited VRAM

image = pipe(prompt="A futuristic city with flying cars, cinematic lighting",
    height=1024, width=1024, num_inference_steps=30).images[0]
```

## Core Concepts

### Architecture
```
Pipeline (orchestration)
├── Model (neural networks)
│   ├── UNet / Transformer (noise prediction)
│   ├── VAE (latent encoding/decoding)
│   └── Text Encoder (CLIP/T5)
└── Scheduler (denoising algorithm)
```

### Pipelines
| Pipeline | Purpose |
|----------|---------|
| `StableDiffusionPipeline` | Text-to-image (SD 1.x/2.x) |
| `StableDiffusionXLPipeline` | Text-to-image (SDXL) |
| `StableDiffusion3Pipeline` | Text-to-image (SD 3.0) |
| `FluxPipeline` | Text-to-image (Flux) |
| `StableDiffusionImg2ImgPipeline` | Image-to-image |
| `StableDiffusionInpaintPipeline` | Inpainting |

### Schedulers (Recommended)
| Scheduler | Steps | Quality | Use Case |
|-----------|-------|---------|----------|
| `DPMSolverMultistepScheduler` | 15-25 | Excellent | Fast, high quality |
| `EulerDiscreteScheduler` | 20-50 | Good | Default |
| `LCMScheduler` | 4-8 | Good | Very fast |

```python
from diffusers import DPMSolverMultistepScheduler
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
image = pipe(prompt, num_inference_steps=20).images[0]
```

### Key Parameters
| Parameter | Default | Description |
|-----------|---------|-------------|
| `prompt` | Required | Text description |
| `negative_prompt` | None | What to avoid |
| `num_inference_steps` | 50 | Denoising steps |
| `guidance_scale` | 7.5 | Prompt adherence (7-12) |
| `height`, `width` | 512/1024 | Output dimensions (multiples of 8) |
| `generator` | None | Torch generator for reproducibility |

## Core Workflows

### Reproducible Generation
```python
import torch
generator = torch.Generator(device="cuda").manual_seed(42)
image = pipe(prompt="A cat wearing a top hat", generator=generator, num_inference_steps=50).images[0]
```

### Negative Prompts
```python
image = pipe(prompt="Professional photo of a dog in a garden",
    negative_prompt="blurry, low quality, distorted, ugly, bad anatomy",
    guidance_scale=7.5).images[0]
```

### Image-to-Image
```python
from diffusers import AutoPipelineForImage2Image
from PIL import Image

pipe = AutoPipelineForImage2Image.from_pretrained(
    "stable-diffusion-v1-5/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cuda")

init_image = Image.open("input.jpg").resize((512, 512))
image = pipe(prompt="A watercolor painting of the scene", image=init_image,
    strength=0.75, num_inference_steps=50).images[0]
```

### Inpainting
```python
from diffusers import AutoPipelineForInpainting
from PIL import Image

pipe = AutoPipelineForInpainting.from_pretrained(
    "runwayml/stable-diffusion-inpainting", torch_dtype=torch.float16).to("cuda")
image = Image.open("photo.jpg")
mask = Image.open("mask.png")
result = pipe(prompt="A red car parked on the street", image=image, mask_image=mask,
    num_inference_steps=50).images[0]
```

## Memory Optimization (Critical for Consumer GPUs)
```python
pipe.enable_model_cpu_offload()      # Move models to CPU when not in use
pipe.enable_attention_slicing()      # Chunk attention computation
pipe.enable_vae_slicing()            # Tile VAE decoding
pipe.enable_vae_tiling()             # For large images (1024+)
# Optional (requires xformers):
# pipe.enable_xformers_memory_efficient_attention()
```

## Advanced Topics (see [references/advanced-usage.md](references/advanced-usage.md))
- **ControlNet** — Spatial conditioning (canny, openpose, depth, scribble, MLSD)
- **LoRA adapters** — Loading, fusing, multiple LoRAs, LoRA training
- **Custom pipelines** — Building from components, custom denoising loops
- **IP-Adapter** — Image prompts alongside text
- **SDXL Refiner** — Two-stage generation
- **T2I-Adapter** — Lightweight conditioning
- **Fine-tuning** — DreamBooth, LoRA training, Textual Inversion
- **Quantization** — 8-bit and 4-bit (NF4) for reduced memory

## Common Issues
**CUDA OOM:** Apply all memory optimizations above. Use lower precision, smaller dimensions, fewer steps.

## Skills Required
| Skill | Purpose |
|-------|---------|
| `context7` | Current Diffusers API documentation |
| `systematic-debugging` | CUDA/memory errors and pipeline failures |

## Pitfalls
- **CUDA required**: CPU inference extremely slow
- **Model variant mismatch**: Ensure `variant="fp16"` matches HuggingFace files
- **Detailed topics**: Moved to `references/advanced-usage.md`, `references/troubleshooting.md`

## Verification Checklist
- [ ] `diffusers`, `transformers`, `accelerate`, `torch` installed
- [ ] Basic text-to-image generation works
- [ ] SDXL loads with memory optimizations enabled
- [ ] Image-to-image and inpainting pipelines functional
- [ ] Scheduler swap works for faster generation
- [ ] Negative prompts affect output as expected

## References
- **[Advanced Usage](references/advanced-usage.md)** — ControlNet, LoRA, IP-Adapter, SDXL Refiner, T2I-Adapter, DreamBooth, LoRA training, Textual Inversion, quantization, custom pipelines, batch generation, production deployment
- **[Troubleshooting](references/troubleshooting.md)** — CUDA OOM, slow generation, model loading failures, quality issues

## Recently Absorbed Skills
- `nano-banana-pro-openrouter` (2026-06-25) — Image generation via OpenRouter (Gemini 3 Pro Image model)
