# Audit Path Normalization Bug

## Observed symptom

A prompt-repair audit reported ~180 missing template references across `.github/prompts/*.prompt.md`. The repository tree already contained the referenced files, so the count was suspect.

## Root cause

The audit script normalized markdown link/backtick paths incorrectly:
- It left literal backticks in extracted paths.
- It sometimes left a leading `templates/` prefix while also later stripping or not stripping it inconsistently.
- It treated bare directory references with trailing `/` as missing files rather than directory existence checks.

That produced normalized “paths” like:
- `` `templates/add-educational-comments/` ``
- `` `templates/add-educational-comments/configuration_reference.md` ``

Because the literal backtick and/or leading `templates/` remained, the existence check always failed even though the actual file or directory was present.

## Repro shortcut

1. Pick one reported missing ref from the audit JSON.
2. Run a direct filesystem check:
   - `python -c "from pathlib import Path; print(Path('C:/.../.github/prompts/templates/add-educational-comments/configuration_reference.md').exists())"`
3. If the direct check is `True`, the audit normalizer is wrong; do not bulk-create or bulk-patch from that report until it is fixed.

## Fix pattern

- Strip markdown syntax first: backticks, `](`/`)`, leading `./` or `../`, leading `templates/`, trailing `/`.
- After normalization, check both:
  - exact relative path under `templates/`
  - filesystem `exists()` for directories.
- Ignore directory placeholders in “missing file” counts.

## Lesson

Always validate the validator before bulk remediation. One true positive repro is enough to prove tooling is trustworthy; many false positives usually mean the detector is wrong.
