# Tool Patterns

> Extracted from `php-mcp-server-generator.prompt.md`.

## Tool Patterns

### Simple Tool

```php
#[McpTool]
public function simpleAction(string $input): string
{
    return "Processed: {$input}";
}
```

### Tool with Validation

```php
#[McpTool]
public function validateEmail(
    #[Schema(format: 'email')]
    string $email
): bool {
    return filter_var($email, FILTER_VALIDATE_EMAIL) !== false;
}
```

### Tool with Enum

```php
enum Status: string {
    case ACTIVE = 'active';
    case INACTIVE = 'inactive';
}

#[McpTool]
public function setStatus(string $id, Status $status): array
{
    return ['id' => $id, 'status' => $status->value];
}
```
