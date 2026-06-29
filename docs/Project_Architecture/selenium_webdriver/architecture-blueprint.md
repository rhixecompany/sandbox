# Architecture Blueprint: selenium_webdriver

**Generated:** 2026-06-29  
**Generator:** architecture-blueprint-generator  

---

## 1. Architecture Detection and Analysis

### Technology Stack

| Category | Technology |
|---|---|
| **Runtime** | Node.js 18+ |
| **Framework** | Selenium WebDriver 4.x |
| **Language** | JavaScript (ES Modules) |
| **Browser** | Chrome (via ChromeDriver) |
| **Formatting** | Prettier |
| **Package Manager** | npm |

### Architectural Pattern Detected

**Pattern:** Script-Based Browser Automation  
The project follows a **utility script pattern** for web scraping with Selenium:

```
Scrape Script
├── WebDriver Configuration
├── Navigation Logic
├── Data Extraction (with retry for stale elements)
├── JSON Output Generation
└── Cleanup (driver.quit())
```

---

## 2. Architectural Overview

### System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                      Scrape Script                            │
│                                                              │
│  User Input → Selenium WebDriver → Chrome Browser            │
│                                        ↓                     │
│                              Navigate to Target URL          │
│                                        ↓                     │
│                            Extract Data (with retry logic)   │
│                                        ↓                     │
│                                  JSON Output Files           │
│                                        ↓                     │
│                              Cleanup (driver.quit())         │
└──────────────────────────────────────────────────────────────┘
```

### Key Components

| File | Purpose |
|---|---|
| `src/scrape.js` | Main scraper script |
| `src/scrape2.js` | Alternative scraper variant |
| `src/test.js` | Test/demo script |
| `src/test1.js` | Additional test script |
| `src/utils.js` | Shared utility functions |

---

## 3. Key Design Decisions

| Decision | Rationale |
|---|---|
| ES Modules (`"type": "module"`) | Modern JavaScript import/export syntax |
| Explicit WebDriverWait | Reliable scraping, avoids race conditions |
| Stale element retry logic | Handles dynamic content changes during scraping |
| driver.quit() in finally block | Ensures browser cleanup on errors |

### Selenium Patterns

```javascript
// Wait for element explicitly
const wait = new WebDriverWait(driver, 10);
const element = await wait.until(
  By.css('.comic-title')
);

// Stale element retry
async function safeClick(driver, locator) {
  for (let i = 0; i < 3; i++) {
    try {
      const el = await driver.findElement(locator);
      await el.click();
      return;
    } catch (StaleElementReferenceException) {
      await driver.sleep(500);
    }
  }
}
```

---

## 4. Data Output

Scraped data is output as JSON files containing:
- Comic/manga listings
- Chapter details
- Metadata extracted from target sites

---

## 5. Extensibility Points

1. **New scrape targets**: Add new script files following existing patterns
2. **Additional browsers**: Configure Firefox/Edge WebDriver
3. **Database storage**: Replace JSON output with database writes
4. **Scheduled scraping**: Add cron or Celery integration

---

*End of architecture blueprint.*
