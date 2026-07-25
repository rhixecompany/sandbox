# lcs.py — Overview

## Purpose
Longest Common Subsequence (LCS) utility for string comparison. This script implements the classic dynamic programming LCS algorithm to find the longest sequence of characters that appears in the same order in two or more input strings. Useful for file diffing, plagiarism detection, code comparison, and sequence alignment tasks.

## Usage

```bash
python lcs.py [--strings STR1 STR2] [--file FILE1 FILE2] [--output FORMAT] [--highlight] [--diff] [--tokenize MODE] [--all]
```

### Options

| Option       | Description                                                    |
|-------------|----------------------------------------------------------------|
| `--strings`  | Two input strings to compare (inline mode)                      |
| `--file`     | Two file paths to read strings from                             |
| `--output`   | Output format: `text`, `json`, `diff` (default: `text`)       |
| `--highlight`| Highlight the common subsequence in context                    |
| `--diff`     | Show LCS-based diff (common lines preserved, differences marked) |
| `--tokenize` | Tokenize mode: `char`, `word`, `line` (default: `char`)       |
| `--percent`  | Show similarity as a percentage of the longer string       |

## Behavior

- Implements the classic O(n*m) dynamic programming LCS algorithm.
- Supports character-level (default), word-level, and line-level comparisons.
- With `--file` mode, reads file contents as the two input strings.
- With `--diff`, displays a unified-diff-like output showing common lines and differing lines.
- Returns the length of the LCS plus the actual common subsequence/sequence.
- For files, provides additional metrics: file sizes, LCS length, similarity ratio.

## Example

**Compare two strings:**
```bash
python lcs.py --strings "abcdef" "acbdf"
# Output: LCS = "abdf" (length 4)
```

**Compare two files with diff output:**
```bash
python lcs.py --file original.py modified.py --diff
```

**Word-level comparison with JSON output:**
```bash
python lcs.py --strings "The quick brown fox" "The brown fox" --tokenize word --output json
```

## Dependencies

- Python 3.6+
- No external dependencies

## See Also

- Sequence alignment algorithms
- Python `difflib` module documentation