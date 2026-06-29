# File Templates

> Extracted from `php-mcp-server-generator.prompt.md`.

## File Templates

### composer.json

```json
{
  "autoload": {
    "psr-4": {
      "App\\\\": "src/"
    }
  },
  "autoload-dev": {
    "psr-4": {
      "Tests\\\\": "tests/"
    }
  },
  "config": {
    "optimize-autoloader": true,
    "preferred-install": "dist",
    "sort-packages": true
  },
  "description": "{Server description}",
  "name": "your-org/{project-name}",
  "require": {
    "php": "^8.2",
    "mcp/sdk": "^0.1"
  },
  "require-dev": {
    "phpunit/phpunit": "^10.0",
    "symfony/cache": "^6.4"
  },
  "type": "project"
}
```

### .gitignore

```
/vendor
/cache
composer.lock
.phpunit.cache
phpstan.neon
```

### README.md

````markdown
# {Project Name}

{Server description}
