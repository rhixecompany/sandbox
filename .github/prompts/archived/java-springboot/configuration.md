# Configuration

> Extracted from `java-springboot.prompt.md`.

## Configuration

- **Externalized Configuration:** Use `application.yml` (or `application.properties`) for configuration. YAML is often preferred for its readability and hierarchical structure.
- **Type-Safe Properties:** Use `@ConfigurationProperties` to bind configuration to strongly-typed Java objects.
- **Profiles:** Use Spring Profiles (`application-dev.yml`, `application-prod.yml`) to manage environment-specific configurations.
- **Secrets Management:** Do not hardcode secrets. Use environment variables, or a dedicated secret management tool like HashiCorp Vault or AWS Secrets Manager.
