# Project Setup & Structure

> Extracted from `kotlin-springboot.prompt.md`.

## Project Setup & Structure

- **Build Tool:** Use Maven (`pom.xml`) or Gradle (`build.gradle`) with the Kotlin plugins (`kotlin-maven-plugin` or `org.jetbrains.kotlin.jvm`).
- **Kotlin Plugins:** For JPA, enable the `kotlin-jpa` plugin to automatically make entity classes `open` without boilerplate.
- **Starters:** Use Spring Boot starters (e.g., `spring-boot-starter-web`, `spring-boot-starter-data-jpa`) as usual.
- **Package Structure:** Organize code by feature/domain (e.g., `com.example.app.order`, `com.example.app.user`) rather than by layer.
