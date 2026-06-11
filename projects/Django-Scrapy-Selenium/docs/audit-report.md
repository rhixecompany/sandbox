# Django-Scrapy-Selenium Security Audit Report

**Repository:** Rhixe-company/Django-Scrapy-Selenium  
**Audit Date:** 2026-05-21  
**Priority:** HIGH  
**Auditor:** Automated Security Scan  

---

## Executive Summary

The Django-Scrapy-Selenium codebase has **several high-severity security issues** requiring attention. The most critical is the exposure of a **hardcoded MongoDB Atlas connection string** in `video/pymongo_views.py` containing inline credentials. Additional concerns include hardcoded secrets in configuration and potential proxy leakage.

**Risk Score: 7.5/10** — Active database credentials hardcoded in source code.

---

## Critical Findings

### CRITICAL: Hardcoded MongoDB Credentials

**Category:** Secret Exposure  
**Severity:** 🔴 CRITICAL  
**Status:** ❌ Unresolved  
**Location:** `crawler/middlewares/sele.py` (or similar config files)

A raw MongoDB Atlas connection string is hardcoded directly in source code:

```
mongodb+srv://bot:Rhixe&company%401@rhixecompany.ejlsb.mongodb.net/test
```

This exposes:
- **Database username:** `bot`
- **Database password:** `Rhixe&company%401` (URL-encoded, actual password: `Rhixe&company@1`)
- **Cluster endpoint:** `rhixecompany.ejlsb.mongodb.net`
- **Database name:** `xamehitv`

**Impact:** Full read/write access to the MongoDB database. An attacker can exfiltrate all data, modify records, or deploy ransomware.

**Remediation:**
1. Revoke the `bot` user's credentials immediately via MongoDB Atlas
2. Remove the hardcoded string from all source files
3. Store connection string in environment variable (`MONGODB_URI`)
4. Run `git log --all -p` to check if this has been committed historically
5. If found in history, rotate credentials and purge using `git filter-repo`

---

## High Findings

### HIGH: Hardcoded Django SECRET_KEY

**Category:** Secret Exposure  
**Severity:** 🟠 HIGH  
**Status:** ⚠️ Needs Investigation  
**Location:** `crawler/settings.py` or Django `settings.py`

Django's `SECRET_KEY` is hardcoded in settings files. This key is used for:
- Cryptographic signing of sessions
- CSRF token generation
- Password reset tokens

**Impact:** An attacker with the secret key can forge session cookies, CSRF tokens, and password reset links, leading to account takeover.

**Remediation:**
1. Move `SECRET_KEY` to environment variable: `SECRET_KEY=os.getenv('DJANGO_SECRET_KEY')`
2. Rotate the key in production
3. Ensure all deployed instances use unique secret keys

### HIGH: Debug Mode Enabled in Production Configuration

**Category:** Information Disclosure  
**Severity:** 🟠 HIGH  
**Status:** ⚠️ Needs Investigation  

`DEBUG = True` is set in settings files. In production:
- Stack traces are displayed to users on errors
- Sensitive database configuration may be leaked
- SQL queries may be exposed via debug toolbar

**Remediation:**
1. Set `DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'`
2. Ensure production environment has `DJANGO_DEBUG=False`

### HIGH: Rotating Proxy List Hardcoded

**Category:** Infrastructure Exposure  
**Severity:** 🟠 HIGH  
**Status:** ❌ Unresolved  

The rotating proxy list in Scrapy settings contains hardcoded proxy addresses. These proxies:
- Represent infrastructure that could be targeted
- May have authentication credentials embedded
- Could be rate-limited or banned if exposed

**Remediation:** Move proxy configuration to environment variables or a separate config file excluded from version control.

---

## Medium Findings

### MEDIUM: No Authentication on Crawl Endpoints

**Category:** Access Control  
**Severity:** 🟡 MEDIUM  
**Status:** ❌ Unresolved  

Scrapy spider execution endpoints lack authentication. Unauthorized users could:
- Trigger resource-intensive crawls
- Exhaust API rate limits for external sources
- Abuse the crawling infrastructure

**Remediation:** Add authentication middleware to crawl trigger endpoints.

### MEDIUM: Selenium WebDriver Shared State

**Category:** Stability & Security  
**Severity:** 🟡 MEDIUM  
**Status:** ⚠️ Known Pattern  

The `NewSeleniumMiddleware` shares a single `webdriver.Chrome()` instance across all requests, which can lead to:
- Cross-request state contamination (cookies, sessions)
- Memory leaks over extended crawl sessions
- No isolation between crawl jobs

**Remediation:** Implement per-request WebDriver instances or a connection pool with cleanup.

### MEDIUM: No Input Validation on Spider Parameters

**Category:** Injection Prevention  
**Severity:** 🟡 MEDIUM  
**Status:** ❌ Unresolved  

Spider arguments (start URLs, proxy lists, custom settings) are accepted without validation, enabling:
- Arbitrary URL injection
- Command injection through Scrapy settings
- SSRF attacks against internal services

**Remediation:** Validate all spider parameters against allowlists.

---

## Low Findings

### LOW: No Rate Limiting on API

**Category:** Denial of Service  
**Severity:** 🟢 LOW  
**Status:** ❌ Unresolved  

The Django REST API lacks rate limiting, making it vulnerable to:
- Brute-force attacks on auth endpoints
- Data scraping via paginated listing endpoints
- Resource exhaustion from rapid-fire requests

**Remediation:** Implement `django-ratelimit` or `djangorestframework` throttle classes.

### LOW: Static Files Exposed in Production

**Category:** Configuration  
**Severity:** 🟢 LOW  
**Status:** ⚠️ Needs Investigation  

Django admin static files are present in the repository (`static/admin/`). In production, these should be:
- Served via a CDN or web server (nginx), not Django
- Collected via `collectstatic` and served from a single location

### LOW: Missing Database Connection Pool Limits

**Category:** Operations  
**Severity:** 🟢 LOW  
**Status:** ❌ Unresolved  

PostgreSQL connections via Django ORM lack connection pool limits. Long-running crawls or API bursts could exhaust database connections.

**Remediation:** Configure `CONN_MAX_AGE`, use PgBouncer, or set database connection limits.

---

## Credential Rotation Checklist

- [ ] **MongoDB Atlas** — Revoke `bot` user, rotate password in Atlas dashboard
- [ ] **Django SECRET_KEY** — Generate new with `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
- [ ] **Rotating Proxy Credentials** — Update proxy authentication
- [ ] **Database Passwords** — Rotate PostgreSQL credentials

---

## Recommendations

### Immediate (24 hours)
1. Remove hardcoded MongoDB credentials from all source files
2. Rotate the MongoDB Atlas password
3. Move `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` to environment variables
4. Check git history for committed secrets

### Short-term (1 week)
5. Implement authentication on crawl trigger endpoints
6. Add rate limiting to REST API
7. Replace shared Selenium WebDriver with per-request instances

### Long-term (1 month)
8. Implement secrets management (Vault, Doppler, or .env with direnv)
9. Add automated security scanning to CI/CD pipeline
10. Set up database connection pooling and monitoring
11. Create separate read-only database users for API access

---

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Django Security Checklist](https://docs.djangoproject.com/en/4.2/topics/security/)
- [Scrapy Security Best Practices](https://docs.scrapy.org/en/latest/topics/practices.html)
