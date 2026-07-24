# Testing

> Extracted from `kotlin-springboot.prompt.md`.

## Testing

- **JUnit 5:** JUnit 5 is the default and works seamlessly with Kotlin.
- **Idiomatic Testing Libraries:** For more fluent and idiomatic tests, consider using **Kotest** for assertions and **MockK** for mocking. They are designed for Kotlin and offer a more expressive syntax.
- **Test Slices:** Use test slice annotations like `@WebMvcTest` or `@DataJpaTest` to test specific parts of the application.
- **Testcontainers:** Use Testcontainers for reliable integration tests with real databases, message brokers, etc.
