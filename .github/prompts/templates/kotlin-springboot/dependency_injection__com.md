# Dependency Injection & Components

> Extracted from `kotlin-springboot.prompt.md`.

## Dependency Injection & Components

- **Primary Constructors:** Always use the primary constructor for required dependency injection. It's the most idiomatic and concise approach in Kotlin.
- **Immutability:** Declare dependencies as `private val` in the primary constructor. Prefer `val` over `var` everywhere to promote immutability.
- **Component Stereotypes:** Use `@Service`, `@Repository`, and `@RestController` annotations just as you would in Java.
