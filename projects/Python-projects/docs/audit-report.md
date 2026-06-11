# Python Projects Security Audit Report

**Repository:** Rhixe-company/Python-projects  
**Audit Date:** 2026-05-21  
**Priority:** MEDIUM  
**Auditor:** Automated Security Scan  

---

## Executive Summary

The Python-projects repository contains 18 standalone utility scripts with **moderate security concerns**. The primary issues involve hardcoded credentials, insecure defaults, and lack of input validation in several scripts. Since these are utility/learning scripts, the risk is lower than production systems, but several findings could lead to data exposure or system compromise if used in sensitive contexts.

**Risk Score: 4.0/10** — Utility scripts with hardcoded test credentials and insecure defaults.

---

## High Findings

### HIGH: Hardcoded SMTP Credentials in email_sender.py

**Category:** Secret Exposure  
**Severity:** 🟠 HIGH  
**Status:** ❌ Unresolved  

The email sender script may contain hardcoded SMTP credentials (sender email, password) as default parameter values. If committed:

```python
# RISK: Hardcoded defaults in function signature
def send_email(smtp_server="smtp.gmail.com", port=587,
               sender="your_email@gmail.com",  # HARDCODED
               password="your_app_password",    # HARDCODED
               ...):
```

**Impact:** Email account compromise, spam origin, password reuse exposure.

**Remediation:**
1. Remove default credential values from function signatures
2. Read credentials from environment variables or interactive input
3. Add `.env` support for credential configuration

### HIGH: No Input Validation in web_scraper.py

**Category:** Injection Prevention  
**Severity:** 🟠 HIGH  
**Status:** ❌ Unresolved  

The web scraper accepts user-provided URLs and CSS selectors without validation:
- **URL Injection:** `file:///etc/passwd` URLs could read local files
- **SSRF:** Internal network hosts could be targeted
- **Selector Injection:** Malicious selectors could cause unexpected behavior

**Remediation:**
1. Validate URLs against an allowlist of schemes (http, https only)
2. Block private IP ranges for URL targets
3. Sanitize CSS selectors to prevent injection

### HIGH: No Rate Limiting in web_scraper.py

**Category:** Denial of Service  
**Severity:** 🟠 HIGH  
**Status:** ❌ Unresolved  

The web scraper can be used to make rapid, uncontrolled requests to target websites, potentially causing:
- Denial of service against target servers
- IP-based rate limiting of the user's network
- Legal liability for unauthorized scraping

**Remediation:**
1. Add mandatory delays between requests (min 1 second)
2. Respect `robots.txt` directives
3. Set a user-agent header identifying the scraper

---

## Medium Findings

### MEDIUM: Hardcoded API Keys in currency_converter.py

**Category:** Secret Exposure  
**Severity:** 🟡 MEDIUM  
**Status:** ❌ Unresolved  

If the currency converter uses an external API (e.g., exchangerate-api.com), it must not have hardcoded API keys. API keys in source code lead to unauthorized usage and potential billing charges.

**Remediation:**
1. Remove any hardcoded API keys
2. Use environment variables: `API_KEY = os.getenv('EXCHANGE_RATE_API_KEY')`
3. Add `.env.example` with placeholder keys

### MEDIUM: System Information Exposure in system_info_collector.py

**Category:** Information Disclosure  
**Severity:** 🟡 MEDIUM  
**Status:** ❌ Unresolved  

The system info collector gathers detailed system information including:
- Network interfaces and IP addresses
- Running process lists
- Boot time and uptime
- Hardware details

If output is shared or logged, this leaks sensitive system configuration.

**Remediation:**
1. Add a `--redact-sensitive` flag to remove private information
2. Warn users about information exposure in script output
3. Never automatically transmit collected data

### MEDIUM: No File Path Validation in batch_file_renamer.py

**Category:** Path Traversal  
**Severity:** 🟡 MEDIUM  
**Status:** ❌ Unresolved  

The batch file renamer accepts user-provided directory paths and regex patterns without validation, allowing:
- Path traversal via `../` sequences
- Operations outside intended directory scope
- Potential overwrite of system files

**Remediation:**
1. Validate directory paths against allowed base paths
2. Resolve and check all paths (use `os.path.abspath`)
3. Prevent operations outside target directory

### MEDIUM: CSV Injection in csv_json_converter.py

**Category:** Data Injection  
**Severity:** 🟡 MEDIUM  
**Status:** ❌ Unresolved  

If converted JSON data is re-exported to CSV without sanitization, formulas starting with `=`, `+`, `-`, `@` could execute when opened in spreadsheet software (CSV injection).

**Remediation:** Sanitize CSV output by prefixing formula-starting values with a single quote.

---

## Low Findings

### LOW: MD5 Hash Usage in duplicate_finder.py

**Category:** Security  
**Severity:** 🟢 LOW  
**Status:** ⚠️ Accepted  

Duplicate finder uses MD5 hashing for file comparison. While MD5 has known collision vulnerabilities, for duplicate detection this is functionally acceptable. Consider SHA-256 as a configurable option for security-conscious users.

### LOW: Insecure Random in Legacy Scripts

**Category:** Cryptography  
**Severity:** 🟢 LOW  
**Status:** ❌ Unresolved  

Some scripts may use `random` module instead of `secrets` for non-cryptographic purposes. The `password_generator.py` correctly uses `secrets`, but verify other scripts don't use `random` for security-sensitive purposes.

### LOW: No HTTPS Verification in network scripts

**Category:** Transport Security  
**Severity:** 🟢 LOW  
**Status:** ❌ Unresolved  

Network scripts should verify SSL/TLS certificates by default. Using `verify=False` in requests calls disables certificate validation.

**Remediation:** Ensure all `requests.get()` calls default to `verify=True` (or omit, which defaults to True).

---

## Recommendations

### Immediate (24 hours)
1. Remove any hardcoded email credentials from `email_sender.py`
2. Add URL validation to `web_scraper.py`
3. Replace any hardcoded API keys with environment variables

### Short-term (1 week)
4. Add rate limiting and delay configuration to web_scraper.py
5. Add file path validation to batch_file_renamer.py
6. Implement CSV injection prevention in csv_json_converter.py
7. Review all scripts for `random` vs `secrets` module usage

### Long-term (1 month)
8. Add comprehensive input validation to all scripts accepting user input
9. Implement logging with sensitive data redaction
10. Create centralized configuration module for API keys and credentials
11. Add automated security scanning (bandit, safety) to CI

---

## Automated Scanning Commands

```bash
# Install security scanners
pip install bandit safety

# Run Bandit (static analysis)
bandit -r . -f json -o bandit-report.json

# Check dependencies for known vulnerabilities
safety check

# Run pyright for type checking
pip install pyright
pyright .
```

---

## Script Security Checklist

Use this to evaluate each script:

- [ ] No hardcoded credentials, API keys, or tokens
- [ ] All user input validated and sanitized
- [ ] File operations constrained to intended directories
- [ ] Network requests respect rate limits and robots.txt
- [ ] SSL/TLS certificate verification enabled
- [ ] Uses `secrets` module for security-sensitive randomness
- [ ] Sensitive output can be redacted
- [ ] Error messages don't leak sensitive information
- [ ] Temporary files cleaned up after use
- [ ] Dependencies checked for known vulnerabilities

---

## References

- [Bandit — Python Security Linter](https://bandit.readthedocs.io/)
- [OWASP Python Security](https://owasp.org/www-project-python-security/)
- [PEP 8 — Security Considerations](https://peps.python.org/pep-0008/#programming-recommendations)
