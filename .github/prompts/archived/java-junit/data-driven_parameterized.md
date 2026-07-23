# Data-Driven (Parameterized) Tests

> Extracted from `java-junit.prompt.md`.

## Data-Driven (Parameterized) Tests

- Use `@ParameterizedTest` to mark a method as a parameterized test.
- Use `@ValueSource` for simple literal values (strings, ints, etc.).
- Use `@MethodSource` to refer to a factory method that provides test arguments as a `Stream`, `Collection`, etc.
- Use `@CsvSource` for inline comma-separated values.
- Use `@CsvFileSource` to use a CSV file from the classpath.
- Use `@EnumSource` to use enum constants.
