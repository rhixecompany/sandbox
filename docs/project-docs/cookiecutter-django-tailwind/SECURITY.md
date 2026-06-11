# Cookiecutter Django Tailwind — Security Guide

## Template Security

This template generates secure-by-default Django projects. Below are the security features baked into every generated project.

## 1. Django Security Settings

Generated `config/settings/production.py`:

```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
```

## 2. Secret Management

- **SECRET_KEY**: Generated via `django-environ`, never committed
- **Environment Variables**: `.envs/` directory gitignored in production
- **Database passwords**: Set via environment, never hardcoded

```python
# config/settings/base.py
SECRET_KEY = env("DJANGO_SECRET_KEY")
DATABASES = {"default": env.db("DATABASE_URL")}
```

## 3. Authentication Security

- **Password Hashing**: Django's default PBKDF2 (upgradeable)
- **django-allauth**: Email verification, password reset
- **Session Security**: HTTP-only cookies, secure flag in production
- **Login Rate Limiting**: Via django-allauth's ACCOUNT_RATE_LIMITS

```python
ACCOUNT_RATE_LIMITS = {
    "login_failed": "5/300s",  # 5 attempts per 5 minutes
}
```

## 4. Database Security

- **PostgreSQL**: Industry-standard relational database
- **Parameterized Queries**: Django ORM prevents SQL injection
- **Connection Security**: SSL for production database connections

## 5. Dependency Security

- **Dependabot**: Automated dependency update PRs
- **PyUp**: Automated security scanning (optional)
- **pip-audit**: Check for known vulnerabilities
- **Pre-commit hooks**: Code quality before commit

## 6. Docker Security

- Non-root user in production Dockerfile
- Read-only root filesystem (configurable)
- No sensitive data in Docker layers
- Traefik with auto-renewing Let's Encrypt certificates

## 7. CSRF & XSS Protection

- **CSRF**: Django's built-in CSRF middleware
- **XSS**: Django template auto-escaping
- **CORS**: django-cors-headers if needed

## Security Checklist for Generated Projects

- [ ] Change `DJANGO_SECRET_KEY` to a unique random value
- [ ] Set `DJANGO_ALLOWED_HOSTS` to your domain(s)
- [ ] Set `DEBUG=False` in production
- [ ] Configure HTTPS/SSL
- [ ] Set strong database passwords
- [ ] Enable Sentry for error monitoring (if included)
- [ ] Configure email service for password reset
- [ ] Review `ACCOUNT_RATE_LIMITS` for auth endpoints
- [ ] Set up regular database backups
- [ ] Enable Dependabot for dependency updates
- [ ] Review and update Content Security Policy

## Additional Recommendations

1. Use a web application firewall (WAF)
2. Enable DDoS protection (Cloudflare, AWS Shield)
3. Implement regular security audits
4. Keep Python and Django versions updated
5. Use 2FA for admin accounts
6. Monitor failed login attempts
