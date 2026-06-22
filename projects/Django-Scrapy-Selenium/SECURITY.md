# Django-Scrapy-Selenium — Security Guide

## Security Architecture

This platform handles web scraping at scale and must protect both the application and target websites from harm.

## 1. Application Security

### Django Security Settings

```python
# config/settings/production.py
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True
```

### Authentication
- django-allauth for user registration and login
- Password hashing via Django's PBKDF2
- Session timeout: configurable
- Admin access: staff/superuser only

## 2. Scraping Best Practices

### Rate Limiting & Politeness

```python
# scraping/settings.py
DOWNLOAD_DELAY = 2.0  # 2 second delay between requests
RANDOMIZE_DOWNLOAD_DELAY = True
CONCURRENT_REQUESTS = 8
CONCURRENT_REQUESTS_PER_DOMAIN = 4
ROBOTSTXT_OBEY = True

# AutoThrottle extension (adaptive rate limiting)
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5.0
AUTOTHROTTLE_MAX_DELAY = 60.0
```

### User-Agent Rotation

```python
# scraping/middlewares.py
class RandomUserAgentMiddleware:
    """Rotate user agents to prevent blocking"""
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ...",
        # ...
    ]

    def process_request(self, request, spider):
        request.headers["User-Agent"] = random.choice(self.user_agents)
```

### Proxy Support

```python
# Optional: Rotating proxy middleware
PROXY_ENABLED = True
PROXY_LIST = [
    "http://proxy1.example.com:8080",
    "http://proxy2.example.com:8080",
]
```

## 3. Selenium Security

- **Headless mode**: No visual browser window
- **Sandbox disabled**: Only in Docker containers
- **Timeouts**: Configurable page load and script timeouts
- **No screenshot storage**: Screenshots temp-only unless configured
- **Resource limits**: Memory and CPU limits for browser processes

## 4. Data Storage

- PostgreSQL with parameterized queries (no SQL injection)
- Sensitive data not stored (credentials, tokens)
- Job logs retained with configurable TTL
- Data export requires authentication

## 5. Infrastructure Security

- Docker containers run as non-root user
- Redis password configured in production
- PostgreSQL restricted to private network
- Environment variables for secrets (never committed)
- SSL/TLS enforced via Traefik/Nginx

## 6. Rate Limiting

| Endpoint | Rate | Burst |
|----------|------|-------|
| Scrape triggers | 10/hour | 2/minute |
| API endpoints | 100/minute | 10/second |
| Login attempts | 5/15min | - |
| Registration | 3/hour | - |

## Security Checklist

- [ ] `DEBUG=False` in production
- [ ] `SECRET_KEY` is unique and strong
- [ ] Scrapy `DOWNLOAD_DELAY` configured
- [ ] `ROBOTSTXT_OBEY=True`
- [ ] Selenium in headless mode
- [ ] Redis password set
- [ ] Database access restricted
- [ ] HTTPS enforced
- [ ] User authentication required for admin
- [ ] Regular dependency updates via Dependabot
- [ ] Web scraping complies with target website terms of service
- [ ] Rate limiting configured for all public endpoints
