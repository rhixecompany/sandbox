# benchmark_models.py — Overview

## Purpose
Benchmarks LLM models for performance comparison within the Hermes ecosystem. This script sends standardized test prompts to one or more configured models and measures response time, token throughput, output quality, and error rates, producing a comparison report suitable for model selection decisions.

## Usage

```bash
python benchmark_models.py [--providers NAMES] [--models NAMES] [--test-file PATH] [--iterations N] [--output FORMAT] [--report FILE] [--warm-up N] [--timeout N]
```

### Options

| Option         | Description                                                    |
|---------------|----------------------------------------------------------------|
| `--providers` | Comma-separated provider names to benchmark (e.g., `openai,anthropic`) |
| `--models`    | Comma-separated model IDs to test (e.g., `gpt-4,claude-3-sonnet`) |
| `--test-file` | Path to a JSON file containing test prompts                     |
| `--iterations` | Number of times to repeat each test for statistical significance (default: 3) |
| `--warm-up`   | Number of warm-up iterations before recording results           |
| `--timeout`   | Max seconds to wait per request (default: 60)                   |
| `--output`    | Output format: `table`, `json`, `markdown`, `csv`               |
| `--report`    | Save the benchmark report to a file                             |

## Behavior

- Reads test prompts from a file or uses built-in standard prompts covering reasoning, coding, creative writing, and instruction-following.
- For each model/provider combination, sends prompts with consistent parameters (temperature=0.7, max_tokens=512).
- Measures: time-to-first-token, total response time, tokens/sec, char/sec, and failure rate.
- Runs a warm-up phase to eliminate cold-start effects.
- Results are averaged across iterations for statistical reliability.
- Outputs formatted comparison tables with speed vs. quality visual indicators.

## Example

**Benchmark all configured providers:**
```bash
python benchmark_models.py --iterations 5 --output table
```

**Compare specific models with JSON output:**
```bash
python benchmark_models.py --models "gpt-4,claude-3-haiku,mistral-large" --iterations 3 --output json --report benchmark.json
```

**Custom test prompts:**
```bash
python benchmark_models.py --test-file my_tests.json --warm-up 2 --iterations 5
```

## Dependencies

- Python 3.8+
- `requests` or `httpx` (API clients)
- `pyyaml` (for config reading)

## See Also

- Hermes provider configuration documentation
- Model selection guide