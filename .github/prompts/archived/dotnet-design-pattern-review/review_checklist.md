# Review Checklist

> Extracted from `dotnet-design-pattern-review.prompt.md`.

## Review Checklist

- **Design Patterns**: Identify patterns used. Are Command Handler, Factory, Provider, and Repository patterns correctly implemented? Missing beneficial patterns?
- **Architecture**: Follow namespace conventions (`{Core|Console|App|Service}.{Feature}`)? Proper separation between Core/Console projects? Modular and readable?
- **.NET Best Practices**: Primary constructors, async/await with Task returns, ResourceManager usage, structured logging, strongly-typed configuration?
- **GoF Patterns**: Command, Factory, Template Method, Strategy patterns correctly implemented?
- **SOLID Principles**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion violations?
- **Performance**: Proper async/await, resource disposal, ConfigureAwait(false), parallel processing opportunities?
- **Maintainability**: Clear separation of concerns, consistent error handling, proper configuration usage?
- **Testability**: Dependencies abstracted via interfaces, mockable components, async testability, AAA pattern compatibility?
- **Security**: Input validation, secure credential handling, parameterized queries, safe exception handling?
- **Documentation**: XML docs for public APIs, parameter/return descriptions, resource file organization?
- **Code Clarity**: Meaningful names reflecting domain concepts, clear intent through patterns, self-explanatory structure?
- **Clean Code**: Consistent style, appropriate method/class size, minimal complexity, eliminated duplication?
