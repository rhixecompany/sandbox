# Analysis Framework

> Extracted from `power-bi-dax-optimization.prompt.md`.

## Analysis Framework

When provided with a DAX formula, perform this comprehensive analysis:

### 1. **Performance Analysis**

- Identify expensive operations and calculation patterns
- Look for repeated expressions that can be stored in variables
- Check for inefficient context transitions
- Assess filter complexity and suggest optimizations
- Evaluate aggregation function choices

### 2. **Readability Assessment**

- Evaluate formula structure and clarity
- Check naming conventions for measures and variables
- Assess comment quality and documentation
- Review logical flow and organization

### 3. **Best Practices Compliance**

- Verify proper use of variables (VAR statements)
- Check column vs measure reference patterns
- Validate error handling approaches
- Ensure proper function selection (DIVIDE vs /, COUNTROWS vs COUNT)

### 4. **Maintainability Review**

- Assess formula complexity and modularity
- Check for hard-coded values that should be parameterized
- Evaluate dependency management
- Review reusability potential
