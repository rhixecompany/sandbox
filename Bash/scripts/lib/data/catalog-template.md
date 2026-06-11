# Repository Catalog Template

Template for CATALOG.md output - shows expected structure with markdown formatting.

## Summary Table

| Repository | Organization | Health Score | Category | Vulnerabilities | Last Commit |
| --- | --- | --- | --- | --- | --- |
| frontend-app | acme-corp | 92 | healthy | 0 | 1 day ago |
| backend-api | acme-corp | 85 | healthy | 3 | 2 days ago |
| data-pipeline | acme-corp | 78 | caution | 1 | 5 days ago |
| legacy-monolith | acme-legacy | 45 | warning | 15 | 180 days ago |
| abandoned-tool | acme-legacy | 25 | critical | 31 | 730 days ago |

**Totals:**

- Total Repositories: 5
- Average Health Score: 65.0
- Healthy: 2 (40%)
- Caution: 1 (20%)
- Warning: 1 (20%)
- Critical: 1 (20%)

---

## Repository Cards

### frontend-app

| Field | Value |
| --- | --- |
| **Organization** | acme-corp |
| **URL** | https://github.com/acme-corp/frontend-app |
| **Local Path** | `C:\Users\Alexa\Desktop\SandBox\repos\acme-corp\frontend-app` |
| **Health Score** | 92/100 |
| **Category** | healthy |
| **Vulnerabilities** | 0 |
| **Issues** | 2 |
| **Package Managers** | npm, yarn |
| **Last Commit** | 2026-05-14 (1 day ago) |

**Status:** ✅ All clear - repository is well-maintained

---

### backend-api

| Field | Value |
| --- | --- |
| **Organization** | acme-corp |
| **URL** | https://github.com/acme-corp/backend-api |
| **Local Path** | `C:\Users\Alexa\Desktop\SandBox\repos\acme-corp\backend-api` |
| **Health Score** | 85/100 |
| **Category** | healthy |
| **Vulnerabilities** | 3 (2 medium, 1 low) |
| **Issues** | 5 |
| **Package Managers** | pip, poetry |
| **Last Commit** | 2026-05-13 (2 days ago) |

**Status:** ✅ Generally healthy - address 3 vulnerabilities

---

### legacy-monolith

| Field | Value |
| --- | --- |
| **Organization** | acme-legacy |
| **URL** | https://github.com/acme-legacy/legacy-monolith |
| **Local Path** | `C:\Users\Alexa\Desktop\SandBox\repos\acme-legacy\legacy-monolith` |
| **Health Score** | 45/100 |
| **Category** | warning |
| **Vulnerabilities** | 15 (5 high, 7 medium, 3 low) |
| **Issues** | 28 |
| **Package Managers** | npm, maven |
| **Last Commit** | 2025-11-16 (180 days ago) |

**Status:** ⚠️ Needs attention - significant vulnerabilities and stale code

---

### abandoned-tool

| Field | Value |
| --- | --- |
| **Organization** | acme-legacy |
| **URL** | https://github.com/acme-legacy/abandoned-tool |
| **Local Path** | `C:\Users\Alexa\Desktop\SandBox\repos\acme-legacy\abandoned-tool` |
| **Health Score** | 25/100 |
| **Category** | critical |
| **Vulnerabilities** | 31 (12 high, 14 medium, 5 low) |
| **Issues** | 42 |
| **Package Managers** | pip |
| **Last Commit** | 2024-05-20 (730 days ago) |

**Status:** 🚨 Critical - consider archiving or removing

---

## Field Descriptions

### Summary Table Columns

- **Repository**: Repository name (slug)
- **Organization**: Owner organization name
- **Health Score**: Overall health score (0-100)
- **Category**: Health category (healthy/caution/warning/critical)
- **Vulnerabilities**: Total security vulnerabilities found
- **Last Commit**: Relative time since last commit

### Repository Card Fields

- **Organization**: Owner organization name
- **URL**: Full GitHub HTTPS URL
- **Local Path**: Local filesystem path to cloned repository
- **Health Score**: Score out of 100 with category
- **Category**: health (>=80), caution (60-79), warning (40-59), critical (<40)
- **Vulnerabilities**: Count with severity breakdown in parentheses
- **Issues**: Number of code quality issues detected
- **Package Managers**: Detected package managers (npm, pip, maven, etc)
- **Last Commit**: ISO date with relative time

### Status Indicators

- ✅ All clear: Healthy, no action needed
- ⚠️ Needs attention: Warning/category, review recommended
- 🚨 Critical: Low score, immediate action may be required
