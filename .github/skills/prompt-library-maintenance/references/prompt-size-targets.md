# Prompt Size Target Verification

Use this when reducing prompt files to a target byte ratio, e.g. ~46% of the original.

## Procedure

1. Measure target files before and after edits.
2. Compare against accepted size bands instead of needing an exact single value.
3. Keep the prompt source editable and the assembler separate.

## Size Bands

| Original to target | Acceptable range |
|---|---|
| Target is 46% of original | 40% to 50% inclusive |

A pair passes when every target file is within 40-50% of its own original size.

## Notes

- Do not use hidden or unverifiable prompt sources as evidence.
- Do not reduce assembler/builderscript source files as if they were prompt text.
