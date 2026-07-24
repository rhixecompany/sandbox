# Service Layer

> Extracted from `kotlin-springboot.prompt.md`.

## Service Layer

- **Business Logic:** Encapsulate business logic within `@Service` classes.
- **Statelessness:** Services should be stateless.
- **Transaction Management:** Use `@Transactional` on service methods. In Kotlin, this can be applied to class or function level.
