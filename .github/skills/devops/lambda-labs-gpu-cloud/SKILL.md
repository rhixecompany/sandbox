---
name: lambda-labs-gpu-cloud
title: "Lambda Labs Gpu Cloud"
description: Reserved and on-demand GPU cloud instances for ML training and inference. Use when you need dedicated GPU instances with simple SSH access, persistent filesystems, or high-performance multi-node clusters for large-scale training.
version: 1.0.0
author: Orchestra Research
license: MIT
dependencies: [lambda-cloud-client>=1.0.0]
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Infrastructure, GPU Cloud, Training, Inference, Lambda Labs]
---

# Lambda Labs GPU Cloud

Comprehensive guide to running ML workloads on Lambda Labs GPU cloud with on-demand instances and 1-Click Clusters.

## When to Use
- Need dedicated GPU instances with full SSH access
- Running long training jobs (hours to days)
- Want simple pricing with no egress fees
- Need persistent storage across sessions
- Require high-performance multi-node clusters (16-512 GPUs)
- Want pre-installed ML stack (Lambda Stack: PyTorch, CUDA, NCCL)

## Quick Start

### Account Setup
1. Create account at https://lambda.ai
2. Add payment method
3. Generate API key from dashboard
4. Add SSH key (required before launch)

### Launch via Console
1. Go to https://cloud.lambda.ai/instances
2. Click "Launch instance"
3. Select GPU type and region
4. Choose SSH key
5. Optionally attach filesystem
6. Launch (3-15 min)

### Connect via SSH
```bash
ssh ubuntu@<INSTANCE-IP>
ssh -i ~/.ssh/lambda_key ubuntu@<INSTANCE-IP>
```

## GPU Instances

| GPU | VRAM | Price/hr | Best For |
|-----|------|----------|----------|
| B200 SXM6 | 180GB | $4.99 | Largest models, fastest training |
| H100 SXM | 80GB | $2.99-3.29 | Large model training |
| H100 PCIe | 80GB | $2.49 | Cost-effective H100 |
| GH200 | 96GB | $1.49 | Single-GPU large models |
| A100 80GB | 80GB | $1.79 | Production training |
| A100 40GB | 40GB | $1.29 | Standard training |
| A10 | 24GB | $0.75 | Inference, fine-tuning |
| A6000 | 48GB | $0.80 | Good VRAM/price |
| V100 | 16GB | $0.55 | Budget training |

| Config | Use Case |
|--------|----------|
| 8x GPU | Distributed training (DDP, FSDP) |
| 4x GPU | Large models, multi-GPU |
| 2x GPU | Medium workloads |
| 1x GPU | Fine-tuning, inference, dev |

Launch: Single-GPU 3-5 min, Multi-GPU 10-15 min

## Lambda Stack (Pre-installed)
- Ubuntu 22.04 LTS, NVIDIA drivers, CUDA 12.x, cuDNN 8.x, NCCL
- PyTorch (latest), TensorFlow (latest), JAX, JupyterLab

```bash
nvidia-smi
python -c "import torch; print(torch.cuda.is_available())"
nvcc --version
```

## Python API

### Install
```bash
pip install lambda-cloud-client
```

### Auth
```python
import os, lambda_cloud_client
configuration = lambda_cloud_client.Configuration(
    host="https://cloud.lambdalabs.com/api/v1",
    access_token=os.environ["LAMBDA_API_KEY"]
)
```

### List Instance Types
```python
with lambda_cloud_client.ApiClient(configuration) as client:
    api = lambda_cloud_client.DefaultApi(client)
    types = api.instance_types()
    for name, info in types.data.items():
        print(f"{name}: {info.instance_type.description}")
```

### Launch Instance
```python
from lambda_cloud_client.models import LaunchInstanceRequest
request = LaunchInstanceRequest(
    region_name="us-west-1",
    instance_type_name="gpu_1x_h100_sxm5",
    ssh_key_names=["my-ssh-key"],
    file_system_names=["my-filesystem"],
    name="training-job"
)
response = api.launch_instance(request)
instance_id = response.data.instance_ids[0]
print(f"Launched: {instance_id}")
```

### List/Terminate
```python
instances = api.list_instances()
for i in instances.data: print(f"{i.name}: {i.ip} ({i.status})")
api.terminate_instance(TerminateInstanceRequest(instance_ids=[instance_id]))
```

### SSH Keys
```python
api.add_ssh_key(AddSshKeyRequest(name="my-key", public_key="ssh-rsa AAAA..."))
keys = api.list_ssh_keys()
api.delete_ssh_key(key_id)
```

## CLI (curl)
```bash
curl -u $LAMBDA_API_KEY: https://cloud.lambdalabs.com/api/v1/instance-types | jq
curl -u $LAMBDA_API_KEY: -X POST https://cloud.lambdalabs.com/api/v1/instance-operations/launch -H "Content-Type: application/json" -d '{"region_name":"us-west-1","instance_type_name":"gpu_1x_h100_sxm5","ssh_key_names":["my-key"]}' | jq
```

## Persistent Storage

### Filesystems (persist across restarts)
Mount: `/lambda/nfs/<FILESYSTEM_NAME>`
```bash
python train.py --checkpoint-dir /lambda/nfs/storage/checkpoints
```

### Create/Attach
1. Console → Storage → Create filesystem (select region)
2. Attach at launch: console or API `file_system_names`

### Best Practices
```
/lambda/nfs/storage/
  ├── datasets/  ├── checkpoints/
  ├── models/    └── outputs/
/home/ubuntu/working/  # Local SSD (ephemeral)
```

## SSH Config
```bash
ssh-keygen -t ed25519 -f ~/.ssh/lambda_key
# Add to console or via API

# Multiple keys
echo 'ssh-rsa AAAA...' >> ~/.ssh/authorized_keys
# From GitHub
ssh-import-id gh:username

# Tunnels
ssh -L 8888:localhost:8888 ubuntu@<IP>   # Jupyter
ssh -L 6006:localhost:6006 ubuntu@<IP>   # TensorBoard
```

## JupyterLab
- Console: Instances → "Launch" in Cloud IDE column
- Manual: `jupyter lab --ip=0.0.0.0 --port=8888` + SSH tunnel

## Training Workflows

### Single-GPU
```bash
ssh ubuntu@<IP>
git clone https://github.com/user/project && cd project
pip install -r requirements.txt
python train.py --epochs 100 --checkpoint-dir /lambda/nfs/storage/checkpoints
```

### Multi-GPU (DDP, single node)
```python
# train_ddp.py
import torch, torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
def main():
    dist.init_process_group("nccl")
    rank = dist.get_rank()
    device = rank % torch.cuda.device_count()
    model = MyModel().to(device)
    model = DDP(model, device_ids=[device])
    # Training loop...
if __name__ == "__main__": main()
```
```bash
torchrun --nproc_per_node=8 train_ddp.py
```

### Checkpoint to Filesystem
```python
checkpoint_dir = "/lambda/nfs/my-storage/checkpoints"
os.makedirs(checkpoint_dir, exist_ok=True)
torch.save({'epoch': epoch, 'model_state': model.state_dict(),
    'optimizer_state': optimizer.state_dict(), 'loss': loss},
    f"{checkpoint_dir}/checkpoint_{epoch}.pt")
```

## 1-Click Clusters (16-512 GPUs, Slurm, InfiniBand)
### Multi-Node Training
```bash
srun --nodes=4 --ntasks-per-node=8 --gpus-per-node=8   torchrun --nnodes=4 --nproc_per_node=8   --rdzv_backend=c10d --rdzv_endpoint=$MASTER_ADDR:29500   train.py
```

## Networking
- Inter-instance: up to 200 Gbps | Outbound: 20 Gbps max | Firewall: port 22 only | Private IP: `ip addr show | grep 'inet '`

## Skills Required
| Skill | Purpose |
|-------|---------|
| `systematic-debugging` | SSH, API, training failures |
| `context7` | Current Lambda Cloud API docs |

## Pitfalls
- **SSH key required** before launch
- **Filesystem attach at launch only** (not after)
- **Terminate when done** — pay-per-minute
- **Region match**: Filesystem and instance must match
- **Detailed workflows**: Moved to `references/advanced-usage.md`, `references/troubleshooting.md`

## Verification Checklist
- [ ] Account created, API key generated
- [ ] SSH key added to console
- [ ] Instance launched, accessible via SSH
- [ ] Lambda Stack verified (`nvidia-smi`, `torch.cuda.is_available()`)
- [ ] Filesystem mounted and persistent
- [ ] Instance terminated after use

## References
- **[Advanced Usage](references/advanced-usage.md)** - Multi-node DDP/FSDP/DeepSpeed, API automation, 1-Click Cluster Slurm, filesystems, env mgmt, monitoring, cost optimization
- **[Troubleshooting](references/troubleshooting.md)** - Launch failures, SSH issues, data loss, slow transfers
