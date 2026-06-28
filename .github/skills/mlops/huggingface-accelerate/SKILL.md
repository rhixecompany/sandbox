---
name: huggingface-accelerate
title: "Huggingface Accelerate"
description: Simplest distributed training API. 4 lines to add distributed support to any PyTorch script. Unified API for DeepSpeed/FSDP/Megatron/DDP. Automatic device placement, mixed precision (FP16/BF16/FP8). Interactive config, single launch command. HuggingFace ecosystem standard.
version: 1.0.0
author: Orchestra Research
license: MIT
dependencies: [accelerate, torch, transformers]
platforms: [linux, macos, windows]
category: mlops
metadata:
  hermes:
    tags: [Distributed Training, HuggingFace, Accelerate, DeepSpeed, FSDP, Mixed Precision, PyTorch, DDP, Unified API, Simple]
---

# HuggingFace Accelerate - Unified Distributed Training

Accelerate simplifies distributed training to **4 lines of code**.

## Quick Start

### Installation

```bash
pip install accelerate
```

### Convert PyTorch Script (4 lines)

```python
import torch
from accelerate import Accelerator

accelerator = Accelerator()

model = torch.nn.Transformer()
optimizer = torch.optim.Adam(model.parameters())
dataloader = torch.utils.data.DataLoader(dataset)

model, optimizer, dataloader = accelerator.prepare(model, optimizer, dataloader)

for batch in dataloader:
    optimizer.zero_grad()
    loss = model(batch)
    accelerator.backward(loss)
    optimizer.step()
```

### Run (single command)

```bash
accelerate launch train.py
```

## Common Workflows

### From Single GPU to Multi-GPU

```python
# Original
model = model.to('cuda')
batch = batch.to('cuda')
loss.backward()

# With Accelerate (4 lines added)
from accelerate import Accelerator
accelerator = Accelerator()
model, optimizer, dataloader = accelerator.prepare(model, optimizer, dataloader)
# Remove .to('cuda') - automatic!
accelerator.backward(loss)
```

### Configure (Interactive)

```bash
accelerate config
# Questions: machine type, GPU count, mixed precision, DeepSpeed
```

### Launch Commands

```bash
# Single GPU
accelerate launch train.py

# Multi-GPU (8 GPUs)
accelerate launch --multi_gpu --num_processes 8 train.py

# Multi-node
accelerate launch --multi_gpu --num_processes 16 \
  --num_machines 2 --machine_rank 0 \
  --main_process_ip $MASTER_ADDR \
  train.py
```

### Mixed Precision Training

```python
from accelerate import Accelerator

# FP16 (with gradient scaling)
accelerator = Accelerator(mixed_precision='fp16')

# BF16 (no scaling, more stable)
accelerator = Accelerator(mixed_precision='bf16')

# FP8 (H100+)
accelerator = Accelerator(mixed_precision='fp8')

model, optimizer, dataloader = accelerator.prepare(model, optimizer, dataloader)

for batch in dataloader:
    with accelerator.autocast():
        loss = model(batch)
    accelerator.backward(loss)
```

### DeepSpeed ZeRO Integration

```python
from accelerate import Accelerator

accelerator = Accelerator(
    mixed_precision='bf16',
    deepspeed_plugin={
        "zero_stage": 2,
        "offload_optimizer": False,
        "gradient_accumulation_steps": 4
    }
)

model, optimizer, dataloader = accelerator.prepare(model, optimizer, dataloader)
```

Or via config:
```bash
accelerate config
# Select: DeepSpeed → ZeRO-2
```

### FSDP (Fully Sharded Data Parallel)

```python
from accelerate import Accelerator, FullyShardedDataParallelPlugin

fsdp_plugin = FullyShardedDataParallelPlugin(
    sharding_strategy="FULL_SHARD",
    auto_wrap_policy="TRANSFORMER_AUTO_WRAP",
    cpu_offload=False
)

accelerator = Accelerator(
    mixed_precision='bf16',
    fsdp_plugin=fsdp_plugin
)

model, optimizer, dataloader = accelerator.prepare(model, optimizer, dataloader)
```

### Gradient Accumulation

```python
from accelerate import Accelerator

accelerator = Accelerator(gradient_accumulation_steps=4)
model, optimizer, dataloader = accelerator.prepare(model, optimizer, dataloader)

for batch in dataloader:
    with accelerator.accumulate(model):
        optimizer.zero_grad()
        loss = model(batch)
        accelerator.backward(loss)
        optimizer.step()
```

## When to Use vs Alternatives

| Use Accelerate | Use Alternative |
|----------------|-----------------|
| Simplest distributed training | **PyTorch Lightning**: Need callbacks, high-level abstractions |
| Single script for any hardware | **Ray Train**: Multi-node orchestration, hyperparameter tuning |
| HuggingFace ecosystem | **Raw DeepSpeed**: Direct API control, advanced features |
| Quick prototyping | **Raw DDP**: Maximum control, minimal abstraction |

## Common Issues

| Issue | Solution |
|-------|----------|
| Wrong device placement | Don't manually `.to('cuda')` after `prepare()` |
| Gradient accumulation not working | Use `accelerator.accumulate(model)` context manager |
| Checkpointing in distributed | Use `accelerator.save_state()` / `accelerator.load_state()` |
| Different results with FSDP | Use `accelerate.utils.set_seed(42)` |

## Advanced Topics (see references/)

- **Megatron integration**: Tensor parallelism, pipeline parallelism
- **Custom plugins**: Creating custom distributed plugins
- **Performance tuning**: Profiling, memory optimization

## Hardware Requirements

- **CPU**: Works (slow)
- **Single/Multi-GPU**: DDP, DeepSpeed, FSDP
- **Multi-node**: DDP, DeepSpeed, FSDP, Megatron
- **TPU**: Supported
- **Apple MPS**: Supported

## Skills Required

| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | Diagnose distributed training failures, device placement |
| `context7` | Look up current Accelerate API documentation |

## Pitfalls

- **No manual device placement**: Accelerate handles it automatically after `prepare()`
- **Gradient accumulation requires context manager**: `with accelerator.accumulate(model):`
- **Checkpoint with accelerator methods**: `accelerator.save_state()` / `load_state()`
- **Seed for reproducibility**: `accelerate.utils.set_seed(42)`
- **Detailed advanced topics**: Moved to `references/megatron-integration.md`, `references/custom-plugins.md`, `references/performance.md`

## Verification Checklist

- [ ] `accelerate config` completed for target hardware
- [ ] 4-line conversion applied (import, init, prepare, backward)
- [ ] Mixed precision configured (fp16/bf16/fp8)
- [ ] Checkpoint save/load tested
- [ ] Multi-GPU launch verified with `accelerate launch --multi_gpu`

## References

- **[Megatron Integration](references/megatron-integration.md)** — Tensor parallelism, pipeline parallelism, sequence parallelism
- **[Custom Plugins](references/custom-plugins.md)** — Creating custom distributed plugins and advanced configuration
- **[Performance](references/performance.md)** — Profiling, memory optimization, best practices