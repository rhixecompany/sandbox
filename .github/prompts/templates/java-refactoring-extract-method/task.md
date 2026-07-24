# Task

> Extracted from `java-refactoring-extract-method.prompt.md`.

## Task

Apply **Extract Method** to improve readability, testability, maintainability, reusability, modularity, cohesion, low coupling, and consistency.

Always return a complete and compilable method (Java 17).

Perform intermediate steps internally:

- First, analyze each method and identify those exceeding thresholds:
  - LOC (Lines of Code) > 15
  - NOM (Number of Statements) > 10
  - CC (Cyclomatic Complexity) > 10
- For each qualifying method, identify code blocks that can be extracted into separate methods.
- Extract at least one new method with a descriptive name.
- Output only the refactored code inside a single `java` block.
- Do not remove any functionality from the original method.
- Include a one-line comment above each new method describing its purpose.
