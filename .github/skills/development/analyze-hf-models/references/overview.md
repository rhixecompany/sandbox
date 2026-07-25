# analyze_hf_models.py — Overview

## Purpose
Analyzes HuggingFace model metadata and configurations to produce structured reports. This script fetches model card information, configuration parameters, and metadata from HuggingFace repositories and outputs summary statistics, comparisons, or compliance checks.

## Usage

```bash
python analyze_hf_models.py [--model MODEL_ID] [--list] [--output FORMAT] [--fields FIELDS] [--compare] [-h]
```

### Options

| Option       | Description                                                      |
|-------------|------------------------------------------------------------------|
| `--model`   | HuggingFace model ID (e.g., `NousResearch/Hermes-3-Llama-3.1-8B`) |
| `--list`    | List all analyzed models in the local cache                       |
| `--output`  | Output format: `table`, `json`, `yaml` (default: `table`)        |
| `--fields`  | Comma-separated fields to include (e.g., `base_model,task,license`) |
| `--compare` | Compare two or more models side by side (requires `--model` list)  |
| `-o`        | Save output to a file instead of stdout                      |

## Behavior

- Fetches model metadata from HuggingFace Hub API (requires `huggingface_hub`).
- Analyzes model configuration (`config.json`) for architecture, parameter count, and quantization.
- Caches model metadata locally to avoid repeated API calls.
- Supports offline analysis of previously fetched models.
- Reports model size, license, task type, base model lineage, and available quantization formats.

## Example

**Analyze a specific model:**
```bash
python analyze_hf_models.py --model NousResearch/Hermes-3-Llama-3.1-8B --output json
```

**Compare two models:**
```bash
python analyze_hf_models.py --model "NousResearch/Hermes-3-Llama-3.1-8B,mistralai/Mistral-7B-v0.1" --compare
```

**List cached models:**
```bash
python analyze_hf_models.py --list
```

## Dependencies

- Python 3.8+
- `huggingface_hub` >= 0.20.0
- `pyyaml` (for YAML output)

## See Also

- HuggingFace Hub API: https://huggingface.co/docs/hub/
- Hermes model provider documentation