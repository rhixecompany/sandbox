# Example Output Format

> Extracted from `power-bi-dax-optimization.prompt.md`.

## Example Output Format

```dax
/*
ORIGINAL FORMULA ANALYSIS:
- Performance Issues: [List identified issues]
- Readability Concerns: [List readability problems]
- Best Practice Violations: [List violations]

OPTIMIZATION STRATEGY:
- [Explain approach and changes]

PERFORMANCE IMPACT:
- Expected improvement: [Quantify if possible]
- Areas of optimization: [List specific improvements]
*/

-- OPTIMIZED FORMULA:
Optimized Measure Name =
VAR DescriptiveVariableName =
    CALCULATE(
        [Base Measure],
        -- Clear filter logic
        Table[Column] = "Value"
    )
VAR AnotherCalculation =
    DIVIDE(
        DescriptiveVariableName,
        [Denominator Measure]
    )
RETURN
    IF(
        ISBLANK(AnotherCalculation),
        BLANK(),  -- Preserve BLANK behavior
        AnotherCalculation
    )
```
