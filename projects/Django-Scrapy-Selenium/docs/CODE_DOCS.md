# Django-Scrapy-Selenium Code Documentation

## Overview

A web crawling and scraping platform combining Django REST API, Scrapy spiders with Selenium middleware, and PostgreSQL persistence. Used for automated comic data collection from external sources.

**Stack:** Python 3.10+ | Django 4.x | Django REST Framework | Scrapy | Selenium | PostgreSQL

---

## 1. API Models Layer

**File:** `api/apps/models.py`

### Core Models

#### Comic
```python
class Comic(models.Model):
    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'), ('Hiatus', 'Hiatus'),
        ('Completed', 'Completed'), ('Dropped', 'Dropped'),
        ('Season End', 'Season End'), ('Coming Soon', 'Coming Soon'),
    ]
    STATUS_CHOICES.update([('Announcement', 'Announcement')])

    # Identity
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    alt_name = models.CharField(max_length=500, null=True, blank=True)
    link = models.URLField(max_length=500, null=True, blank=True)

    # Content
    description = models.TextField(null=True, blank=True)
    image = models.URLField(max_length=500, null=True, blank=True)
    cover = models.URLField(max_length=500, null=True, blank=True)

    # Metadata
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Ongoing')
    views = models.IntegerField(default=0)
    rating = models.CharField(max_length=10, null=True, blank=True)

    # Relations (nullable FK for gradual data collection)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True)

    # Tracking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['slug']),
            models.Index(fields=['status']),
            models.Index(fields=['name']),
        ]
```

Fields and relationships:

| Model | Key Fields | Relationships |
|-------|-----------|---------------|
| **Comic** | name, slug, alt_name, link, description, image, cover, status (6 choices), views, rating | FK→Type, FK→Author, FK→Artist, M2M→Genre |
| **Chapter** | name, slug, link, release_date, volume, chapter_number | FK→Comic (CASCADE), unique(comic, chapter_number) |
| **ChapterImage** | image, page_number | FK→Chapter (CASCADE), unique(chapter, page_number) |
| **ComicImage** | image, order | FK→Comic (CASCADE) |
| **Genre** | name (unique), slug, description | M2M→Comic (through ComicGenre) |
| **Author** | name (unique) | FK→Comic |
| **Artist** | name (unique) | FK→Comic |
| **Type** | name (unique), slug, description | FK→Comic (Manhwa, Manga, Manhua, Comic) |
| **Bookmark** | status (choices: Reading/Completed/Plan to Read/Dropped/On-Hold), notes | FK→User + FK→Comic (composite) |
| **Follow** | — | FK→User + FK→Comic (composite, unique together) |
| **Comment** | content (text) | FK→User + FK→Chapter, with timestamp |
| **Rating** | rating (1-5 IntegerField with validators) | FK→User + FK→Comic, unique(user, comic) |
| **CrawlLog** | status, pages_crawled, errors, started_at, finished_at | Tracks individual crawl sessions |
| **ScrapeJob** | source_url, status, frequency | FK→Comic, scheduled scraping |

### Database Indexes

Most models have explicit indexes on: `slug`, `name`, foreign keys, and frequently filtered fields (status, created_at, rating). The Comic model has 3 defined indexes; Chapter has unique constraint on `(comic_id, chapter_number)`; ChapterImage has unique on `(chapter_id, page_number)`.

---

## 2. Scrapy Spider Layer

**File:** `crawler/spiders/asuracomic.py`

### AsuracomicSpider

```python
class AsuracomicSpider(scrapy.Spider):
    name = "asuracomics"
    allowed_domains = ["asuracomic.net"]
    start_urls = ["https://asuracomic.net/series"]

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'crawler.middlewares.sele.NewSeleniumMiddleware': 543,
        },
        'PIPELINES': {
            'crawler.pipelines.appsdb.CrawlerAppsDbPipeline': 300,
        },
        'CONCURRENT_REQUESTS': 1,
        'DOWNLOAD_DELAY': 3.0,
        'ROTATING_PROXY_LIST': [...],
    }
```

**Core Methods:**

- `parse(response)` — Parses series listing page. Extracts comic links and paginates. Yields `scrapy.Request` to each comic page.
- `comicpage_parse(response)` — Parses individual comic page: extracts title, description, cover image, status, author, artist, type, genres, and all chapter links. Yields multiple data items for persistence.
- Error handling: Wraps parsing in try/except, logs failures with source URL context.

**Design Patterns:**
- Progressive data collection from listing → detail page
- Selenium middleware for JavaScript-rendered content
- Proxy rotation for anti-bot circumvention
- Configurable delays (DOWNLOAD_DELAY=3.0) for rate limiting
- Single concurrent request to avoid overwhelming sources

---

## 3. Selenium Middleware Layer

**File:** `crawler/middlewares/sele.py`

### NewSeleniumMiddleware

```python
class NewSeleniumMiddleware:
    """Custom Selenium middleware for Scrapy.

    Handles JavaScript-rendered pages by intercepting requests
    and using Selenium WebDriver to execute JS and capture
    the fully rendered HTML.
    """

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(options=options)

    def process_request(self, request, spider):
        """Intercept request and render via Selenium."""
        self.driver.get(request.url)
        body = self.driver.page_source
        return scrapy.http.HtmlResponse(
            self.driver.current_url,
            body=body,
            encoding='utf-8',
            request=request
        )
```

**Key Implementation Details:**
- Single WebDriver instance shared across all requests
- Headless mode with production-appropriate window size
- Returns fully rendered HTML as a Scrapy `HtmlResponse`
- No explicit waits — relies on page load completion

**Design Considerations:**
- Shared `webdriver.Chrome()` instance means thread safety must be considered
- No explicit `WebDriverWait` — may fail on slow-loading pages
- Memory leak potential if crawler runs indefinitely without driver restart

---

## 4. Pipeline Layer

**File:** `crawler/pipelines/appsdb.py`

### CrawlerAppsDbPipeline

```python
class CrawlerAppsDbPipeline:
    """Pipeline for persisting scraped items to PostgreSQL via Django ORM."""

    def process_item(self, item, spider):
        """Process a single scraped item and persist to database.

        Handles Comic, Chapter, Genre, Author, Artist, Type items
        using get_or_create pattern to prevent duplicates.
        """
        try:
            if isinstance(item, ComicItem):
                return self._process_comic(item)
            elif isinstance(item, ChapterItem):
                return self._process_chapter(item)
            # ... additional item type handlers
        except Exception as e:
            spider.logger.error(f"Pipeline error: {e}")
            raise DropItem(f"Failed to process item: {e}")
```

**Processing Methods:**
- Comic insertion with `get_or_create` by slug or name
- Chapter insertion with unique constraint `(comic_id, chapter_number)`
- Support for bulk operations when pipelining multiple items
- Error isolation — individual item failures don't stop the pipeline

---

## 5. REST API Layer

**File:** `api/` directory

Django REST Framework viewsets providing:

### Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/comics/` | GET, POST | List/create comics with filtering |
| `/api/comics/{id}/` | GET, PUT, DELETE | Comic CRUD |
| `/api/chapters/` | GET, POST | List/create chapters |
| `/api/chapters/{id}/` | GET, PUT, DELETE | Chapter CRUD |
| `/api/genres/` | GET | List genres |
| `/api/authors/` | GET | List authors |
| `/api/bookmarks/` | GET, POST, DELETE | User bookmark management |
| `/api/comments/` | GET, POST | Chapter comments |
| `/api/ratings/` | GET, POST | Comic ratings |
| `/api/users/` | GET, POST | User management |
| `/api/auth/` | POST | Authentication (JWT-based) |

### Authentication

- JWT-based authentication via `rest_framework_simplejwt`
- Token refresh endpoint for session management
- Permission classes enforce authenticated access for write operations
- Read endpoints are publicly accessible

---

## 6. Scrapy Configuration

**File:** `crawler/` directory structure

```
crawler/
├── spiders/
│   ├── asuracomic.py       # Main spider (AsuraComic source)
│   ├── __init__.py
├── middlewares/
│   ├── sele.py             # NewSeleniumMiddleware
│   ├── __init__.py
├── pipelines/
│   ├── appsdb.py           # CrawlerAppsDbPipeline
│   ├── __init__.py
├── items.py                # Scrapy Item definitions
├── settings.py             # Scrapy project settings
└── __init__.py
```

**Scrapy Settings:**
- `ROBOTSTXT_OBEY = True`
- `CONCURRENT_REQUESTS = 1` (serial crawling)
- `DOWNLOAD_DELAY = 3.0` (rate limiting)
- `COOKIES_ENABLED = False`
- `ROTATING_PROXY_LIST` configured for distributed requests
- Custom middleware pipeline with Selenium integration
- Custom item pipeline with Django ORM persistence

---

## 7. Item Definitions

**File:** `crawler/items.py`

```python
import scrapy

class ComicItem(scrapy.Item):
    name = scrapy.Field()
    slug = scrapy.Field()
    alt_name = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    image = scrapy.Field()
    cover = scrapy.Field()
    status = scrapy.Field()
    type = scrapy.Field()
    author = scrapy.Field()
    artist = scrapy.Field()
    genres = scrapy.Field()  # List of genre names

class ChapterItem(scrapy.Item):
    name = scrapy.Field()
    slug = scrapy.Field()
    link = scrapy.Field()
    chapter_number = scrapy.Field()
    release_date = scrapy.Field()
    comic_name = scrapy.Field()  # Resolved to Comic FK in pipeline
    images = scrapy.Field()  # List of image URLs
```

Items serve as the contract between spiders and pipelines. Fields are dynamically typed via Scrapy's `Field()` with validation in the pipeline layer.
