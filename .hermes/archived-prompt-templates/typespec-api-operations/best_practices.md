# Best Practices

> Extracted from `typespec-api-operations.prompt.md`.

## Best Practices

### Parameter Naming

- Use descriptive parameter names: `userId` not `uid`
- Be consistent across operations
- Use optional parameters (`?`) for filters

### Documentation

- Add JSDoc comments to all operations
- Describe what each parameter does
- Document expected responses

### Models

- Use `@visibility(Lifecycle.Read)` for read-only fields like `id`
- Use `@format("date-time")` for date fields
- Use union types for enums: `"active" | "completed"`
- Make optional fields explicit with `?`

### Confirmations

- Always add confirmations to destructive operations (DELETE, PATCH)
- Show key details in confirmation body
- Use warning emoji (⚠️) for irreversible actions

### Adaptive Cards

- Keep cards simple and focused
- Use conditional rendering with `${if(..., ..., 'N/A')}`
- Include action buttons for common next steps
- Test data binding with actual API responses

### Routing

- Use RESTful conventions:
  - `GET /items` - List
  - `GET /items/{id}` - Get one
  - `POST /items` - Create
  - `PATCH /items/{id}` - Update
  - `DELETE /items/{id}` - Delete
- Group related operations in the same namespace
- Use nested routes for hierarchical resources
