# Django-Scrapy-Selenium — Database Schema

## Overview

The platform uses **PostgreSQL** as its primary database. The schema covers scraped content, user data, job tracking, and application state.

## Core Tables

### `scraping_comic`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | `serial` | `PK` | Unique ID |
| `title` | `varchar(500)` | `NOT NULL` | Comic title |
| `slug` | `varchar(500)` | `UNIQUE` | URL-friendly name |
| `url` | `text` | `NOT NULL` | Source URL |
| `description` | `text` | `NULLABLE` | Synopsis |
| `cover_url` | `text` | `NULLABLE` | Cover image URL |
| `source` | `varchar(100)` | `NOT NULL` | Source website |
| `status` | `varchar(20)` | `DEFAULT 'ongoing'` | Publication status |
| `author` | `varchar(255)` | `NULLABLE` | Author name |
| `artist` | `varchar(255)` | `NULLABLE` | Artist name |
| `genre` | `text` | `NULLABLE` | Comma-separated genres |
| `chapter_count` | `integer` | `DEFAULT 0` | Number of chapters |
| `last_scraped` | `timestamptz` | `NULLABLE` | Last scrape time |
| `created_at` | `timestamptz` | `DEFAULT NOW()` | |
| `updated_at` | `timestamptz` | `DEFAULT NOW()` | |

### `scraping_chapter`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | `serial` | `PK` | |
| `comic_id` | `integer` | `FK → scraping_comic.id` | Parent comic |
| `number` | `decimal(10,2)` | `NOT NULL` | Chapter number |
| `title` | `varchar(500)` | `NULLABLE` | Chapter title |
| `url` | `text` | `NOT NULL` | Chapter URL |
| `content` | `text` | `NULLABLE` | Scraped content |
| `image_urls` | `jsonb` | `NULLABLE` | Array of image URLs |
| `page_count` | `integer` | `DEFAULT 0` | Number of pages |
| `scraped` | `boolean` | `DEFAULT false` | Fully scraped |
| `created_at` | `timestamptz` | `DEFAULT NOW()` | |

### `scraping_scrapejob`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | `serial` | `PK` | |
| `spider_name` | `varchar(100)` | `NOT NULL` | Spider identifier |
| `target_url` | `text` | `NULLABLE` | URL to scrape |
| `status` | `varchar(20)` | `DEFAULT 'pending'` | pending/running/done/failed |
| `items_scraped` | `integer` | `DEFAULT 0` | Items count |
| `error_message` | `text` | `NULLABLE` | Error details |
| `started_at` | `timestamptz` | `NULLABLE` | |
| `finished_at` | `timestamptz` | `NULLABLE` | |
| `created_at` | `timestamptz` | `DEFAULT NOW()` | |

### `users_user`

Standard Django custom user model (django-allauth).

| Column | Type | Constraints |
|--------|------|-------------|
| `id` | `serial` | `PK` |
| `username` | `varchar(150)` | `UNIQUE NOT NULL` |
| `email` | `varchar(254)` | `NOT NULL` |
| `password` | `varchar(128)` | `NOT NULL` |
| `is_active` | `boolean` | `DEFAULT true` |
| `is_staff` | `boolean` | `DEFAULT false` |
| `date_joined` | `timestamptz` | `DEFAULT NOW()` |

### `django_celery_beat_periodictask`

| Column | Type | Description |
|--------|------|-------------|
| `id` | `serial` | PK |
| `name` | `varchar(200)` | Task name |
| `task` | `varchar(200)` | Task path |
| `interval_id` | `integer` | FK → interval schedule |
| `crontab_id` | `integer` | FK → crontab schedule |
| `enabled` | `boolean` | Task active |

## Indexes

| Table | Index | Columns |
|-------|-------|---------|
| `scraping_comic` | `idx_comic_slug` | `slug` |
| `scraping_comic` | `idx_comic_source` | `source` |
| `scraping_comic` | `idx_comic_status` | `status` |
| `scraping_chapter` | `idx_chapter_comic_number` | `comic_id, number` |
| `scraping_scrapejob` | `idx_job_status` | `status` |

## Django Models

```python
# scraping/models.py
from django.db import models

class Comic(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    url = models.URLField()
    source = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='ongoing')
    genre = models.TextField(blank=True)
    chapter_count = models.IntegerField(default=0)
    last_scraped = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Chapter(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    number = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=500, blank=True)
    url = models.URLField()
    content = models.TextField(blank=True)
    image_urls = models.JSONField(default=list)
    scraped = models.BooleanField(default=False)
```
