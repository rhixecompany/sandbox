# 8. Dependencies & External Integrations

> Extracted from `update-specification.prompt.md`.

## 8. Dependencies & External Integrations

[Define the external systems, services, and architectural dependencies required for this specification. Focus on **what** is needed rather than **how** it's implemented. Avoid specific package or library versions unless they represent architectural constraints.]

### External Systems

- **EXT-001**: [External system name] - [Purpose and integration type]

### Third-Party Services

- **SVC-001**: [Service name] - [Required capabilities and SLA requirements]

### Infrastructure Dependencies

- **INF-001**: [Infrastructure component] - [Requirements and constraints]

### Data Dependencies

- **DAT-001**: [External data source] - [Format, frequency, and access requirements]

### Technology Platform Dependencies

- **PLT-001**: [Platform/runtime requirement] - [Version constraints and rationale]

### Compliance Dependencies

- **COM-001**: [Regulatory or compliance requirement] - [Impact on implementation]

**Note**: This section should focus on architectural and business dependencies, not specific package implementations. For example, specify "OAuth 2.0 authentication library" rather than "Microsoft.AspNetCore.Authentication.JwtBearer v6.0.1".
