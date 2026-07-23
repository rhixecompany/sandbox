# Configuration

> Extracted from `kotlin-springboot.prompt.md`.

## Configuration

- **Externalized Configuration:** Use `application.yml` for its readability and hierarchical structure.
- **Type-Safe Properties:** Use `@ConfigurationProperties` with `data class` to create immutable, type-safe configuration objects.
- **Profiles:** Use Spring Profiles (`application-dev.yml`, `application-prod.yml`) to manage environment-specific configurations.
- **Secrets Management:** Never hardcode secrets. Use environment variables or a dedicated secret management tool like HashiCorp Vault or AWS Secrets Manager.
