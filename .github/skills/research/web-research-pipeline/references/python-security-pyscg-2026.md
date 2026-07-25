# OpenSSF Secure Coding Guide for Python (pyscg) — May 2026

**Source:** <https://openssf.org/blog/2026/05/12/secure-coding-guide-for-python-pyscg-first-release/>
**Guide URL:** <https://best.openssf.org/Secure-Coding-Guide-for-Python/>
**Repository:** <https://github.com/ossf/wg-best-practices-os-developers/tree/main/docs/Secure-Coding-Guide-for-Python>

## Why It Matters

First comprehensive, framework-independent secure coding standard for Python.
Covers CPython ≥ 3.9 and the standard library — no dependency on any web framework or third-party module.

Before pyscg, Python had no dedicated secure coding guide comparable to the SEI CERT standards for
Java, C, and C++. Available resources were either language-agnostic or tied to a single framework
(Django, Flask). The OpenSSF Best Practices Working Group closed this gap.

## Scope

- **50+ rules** across **9 sections**
- Each rule has both `noncompliantXX.py` (vulnerable) and `compliantXX.py` (fixed) code examples
- Each rule maps to a specific MITRE CWE entry
- Evidence-based risk: each rule paired with a real-world CVE, its CVSS score, and EPSS exploit probability

## Rule Categories

| Section | Topics | Rule Count |
|---------|--------|-----------|
| 01 Introduction | Trust boundaries, hardcoded credentials, operator precedence, server-side access control | 4 |
| 02 Encoding & Strings | Locale handling, input canonicalization, consistent encoding | 3 |
| 03 Numbers | Floating-point precision, integer wraparound, numeric truncation, type conversion | 8 |
| 04 Neutralization | Format strings, OS command injection, SQL injection, deserialization, path traversal | 8 |
| 05 Exception Handling | Specific exception types, error propagation, cleanup on exceptions | 5 |
| 06 Logging | Sensitive data in logs, security event logging, log neutralization, error output sanitization | 5 |
| 07 Concurrency | Resource consumption, deadlocks, race conditions, improper initialization | 9 |
| 08 Coding Standards | Mutable iteration, built-in redefinition, value comparison, None checks, assertions | 7 |
| 09 Cryptography | Insufficiently random values | 1 |

## Keywords for Search Queries

Use these in web searches to find pyscg rules by topic:
- `pyscg-0001` through `pyscg-0051` (rule IDs)
- `OSS Secure Coding Guide for Python`
- `OpenSSF Python secure coding`
- `best.openssf.org Secure-Coding-Guide-for-Python`

## Key Mitigations at a Glance

| Risk | Fix |
|------|-----|
| OS command injection | Never `shell=True` in subprocess; pass args as list |
| SQL injection | Always use parameterized queries (not f-strings) |
| Insecure deserialization | Avoid `pickle` on untrusted data; prefer `json` |
| Hardcoded secrets | Environment variables + `.env` files |
| Bare excepts | Catch specific exception types |
| Sensitive data in logs | Sanitize log output; never log passwords/tokens |
| Weak randomness | Use `secrets` module, not `random`, for security contexts |

## Tools to Use Alongside

| Tool | Purpose |
|------|---------|
| `bandit` | Static analysis security scanner for Python |
| `pip-audit` | Dependency vulnerability scanning |
| `safety` | Check installed deps against known vulnerabilities |
| `ruff` (select `S` rules) | flake8-security rules via Ruff |

## When to Reference This File

- Research task involves Python security best practices
- Evaluating tooling for security scanning Python codebases
- Need to validate Python code against an authoritative secure coding standard
