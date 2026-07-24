# Data Layer (Repositories)

> Extracted from `kotlin-springboot.prompt.md`.

## Data Layer (Repositories)

- **JPA Entities:** Define entities as classes. Remember they must be `open`. It's highly recommended to use the `kotlin-jpa` compiler plugin to handle this automatically.
- **Null Safety:** Leverage Kotlin's null-safety (`?`) to clearly define which entity fields are optional or required at the type level.
- **Spring Data JPA:** Use Spring Data JPA repositories by extending `JpaRepository` or `CrudRepository`.
- **Coroutines:** For reactive applications, leverage Spring Boot's support for Kotlin Coroutines in the data layer.
