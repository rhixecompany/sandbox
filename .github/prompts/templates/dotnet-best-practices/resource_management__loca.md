# Resource Management & Localization

> Extracted from `dotnet-best-practices.prompt.md`.

## Resource Management & Localization

- Use ResourceManager for localized messages and error strings
- Separate LogMessages and ErrorMessages resource files
- Access resources via `_resourceManager.GetString("MessageKey")`
