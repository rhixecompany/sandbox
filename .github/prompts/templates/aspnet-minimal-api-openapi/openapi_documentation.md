# OpenAPI Documentation

> Extracted from `aspnet-minimal-api-openapi.prompt.md`.

## OpenAPI Documentation

- Use the built-in OpenAPI document support added in .NET 9
- Define operation summary and description
- Add operationIds using the `WithName` extension method
- Add descriptions to properties and parameters with `[Description()]`
- Set proper content types for requests and responses
- Use document transformers to add elements like servers, tags, and security schemes
- Use schema transformers to apply customizations to OpenAPI schemas
