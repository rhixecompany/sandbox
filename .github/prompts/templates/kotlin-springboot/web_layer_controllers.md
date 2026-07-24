# Web Layer (Controllers)

> Extracted from `kotlin-springboot.prompt.md`.

## Web Layer (Controllers)

- **RESTful APIs:** Design clear and consistent RESTful endpoints.
- **Data Classes for DTOs:** Use Kotlin `data class` for all DTOs. This provides `equals()`, `hashCode()`, `toString()`, and `copy()` for free and promotes immutability.
- **Validation:** Use Java Bean Validation (JSR 380) with annotations (`@Valid`, `@NotNull`, `@Size`) on your DTO data classes.
- **Error Handling:** Implement a global exception handler using `@ControllerAdvice` and `@ExceptionHandler` for consistent error responses.
