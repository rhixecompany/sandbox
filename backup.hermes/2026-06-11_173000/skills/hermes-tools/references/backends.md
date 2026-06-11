# Terminal Backends

| Backend | Description | Use Case |
|---------|-------------|----------|
| `local` | Run on your machine (default) | Development, trusted tasks |
| `docker` | Isolated containers | Security, reproducibility |
| `ssh` | Remote server | Sandboxing, keep agent away from its own code |
| `singularity` | HPC containers | Cluster computing, rootless |
| `modal` | Cloud execution | Serverless, scale |
| `daytona` | Cloud sandbox workspace | Persistent remote dev environments |

## Docker Backend Details
```yaml
terminal:
  backend: docker
  docker_image: python:3.11-slim
```
- One persistent container, shared across the whole process
- `docker run -d ... sleep 2h` on first use
- All calls route through `docker exec` into same container
- Working dir, packages, env, and `/workspace` files persist across calls
- Container stopped/removed on shutdown
- Persistence across restarts: `container_persistent` flag

## SSH Backend (Recommended for Security)
```yaml
terminal:
  backend: ssh
```
Set in `~/.hermes/.env`:
```bash
TERMINAL_SSH_HOST=my-server.example.com
TERMINAL_SSH_USER=myuser
TERMINAL_SSH_KEY=~/.ssh/id_ed25519
# or
TERMINAL_SSH_PASSWORD=***
```
Keeps agent's execution environment separate from your development machine.

## Modal Backend
```yaml
terminal:
  backend: modal
  modal_app: "hermes-sandbox"
```
Requires Modal account and `modal setup`. Good for burst workloads, no persistent server cost.

## Daytona Backend
```yaml
terminal:
  backend: daytona
  daytona_image: nikolaik/python-nodejs:python3.11-nodejs20
```
Persistent remote dev environments.