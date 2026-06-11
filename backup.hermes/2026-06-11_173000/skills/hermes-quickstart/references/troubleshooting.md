# Quickstart Troubleshooting

## Common Issues

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| "No model configured" | `hermes model` not run | Run `hermes model` and pick one |
| "Authentication failed" | Bad API key / expired OAuth | Re-run `hermes model`; check `~/.hermes/.env` |
| "Connection refused" | Network / proxy / DNS | Check internet; try different provider |
| "Model not found" | Wrong model name for provider | Use `hermes model` picker (validates names) |

## Platform-Specific

### Windows
- **Must use WSL2** — Install WSL2 first, then run installer inside WSL2
- Path: `C:\Users\<user>\AppData\Local\hermes\` (not `~/.hermes/`)

### Android/Termux
- See dedicated [Termux guide](https://hermes-agent.nousresearch.com/docs/getting-started/termux)

## Reset Everything
```bash
rm -rf ~/.hermes && hermes setup
# Or on Windows:
rm -rf C:\Users\%USERNAME%\AppData\Local\hermes && hermes setup
```

## Logs
```bash
tail -f ~/.hermes/logs/hermes/*.log
# Windows:
tail -f C:\Users\%USERNAME%\AppData\Local\hermes\logs\hermes\*.log
```

## Config Issues
```bash
hermes config show          # View current config
hermes config set key value # Set specific value
hermes config reset         # Reset to defaults
```

## Provider-Specific

### OpenRouter
- Set `OPENROUTER_API_KEY` in `~/.hermes/.env`
- Model format: `provider/model` (e.g., `anthropic/claude-3.5-sonnet`)

### Anthropic
- Requires Max plan + extra credits for OAuth
- Or use `ANTHROPIC_API_KEY`

### AWS Bedrock
- Run `aws configure` first
- Set correct region

### Ollama/LM Studio
- Ensure local server is running
- Set `LM_BASE_URL` if non-default port