# The Story of Rhixe Company Comics

*Two stacks, one database, the consolidation that worked*

---

## Prologue: The Fragmentation

By mid-2024, the workspace had **three comic projects**:

| Project | Stack | Purpose |
|---------|-------|---------|
| `comicwise` | Next.js + Prisma | Comic streaming (reader-facing) |
| `rhixe_scans` | Next.js + Prisma | Comic reader (user library) |
| `Django-Scrapy-Selenium` | Django + Scrapy + Selenium | Scraping pipeline |

Plus `selenium_webdriver` (Node.js scraper) and `xamehi` (legacy Django + Express + React).

**Five projects. Three languages. Two databases. One domain.**

The consolidation wasn't a plan — it was a survival instinct.

---

## Chapter 1: The Architecture Decision

**Why Django + Next.js?**

| Layer | Choice | Rationale |
|-------|--------|-----------|
| **API** | Django REST Framework | Business logic, auth, scraping orchestration, admin |
| **Frontend** | Next.js 16 App Router | SEO, Server Components, Vercel deploy, TypeScript |
| **Database** | PostgreSQL (shared) | Single source of truth |
| **Async** | Celery + Redis | Scraping, notifications, image processing |

**Why not one stack?**

- Scraping logic (Scrapy, Selenium) is Python-native. Porting to Node.js = bugs.
- Admin/dashboard is Django's superpower. Building in Next.js = reinventing.
- Comic reader needs Server Components, ISR, edge caching. Next.js wins.
- Team knows both. No "right" answer — just "consistent" answer.

---

## Chapter 2: The Shared Database

One PostgreSQL. Two ORMs. One schema.

```prisma
// rhixecompany-comics/frontend/prisma/schema.prisma
// (Prisma for Next.js — type-safe client)

model Comic {
  id          String   @id @default(cuid())
  title       String
  slug        String   @unique
  description String?
  coverUrl    String?
  status      Status   @default(ONGOING)
  chapters    Chapter[]
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
}

model Chapter {
  id        String   @id @default(cuid())
  comicId   String
  comic     Comic    @relation(fields: [comicId], references: [id])
  number    Int
  title     String?
  pages     Page[]
  publishedAt DateTime?
  createdAt DateTime @default(now())
}

// ... User, Subscription, ScrapingJob, etc.
```

```python
# rhixecompany-comics/backend/apps/comics/models.py
# (Django ORM for DRF — same tables, same data)

class Comic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    cover_url = models.URLField(blank=True)
    status = models.CharField(choices=Status.choices, default=Status.ONGOING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

**Migration strategy:** Django owns migrations. Prisma `db pull` syncs the schema. Prisma client is generated from the *actual* database, not from Django models.

---

## Chapter 3: The Scraping Pipeline

This is where Django shines.

```python
# apps/scrapers/tasks.py
@shared_task(bind=True, max_retries=3, default_retry_delay=300)
def scrape_comic_source(self, source_id: str):
    source = ScrapingSource.objects.get(id=source_id)
    
    # Choose engine based on source type
    if source.requires_javascript:
        result = run_selenium_scraper(source)
    else:
        result = run_scrapy_spider(source)
    
    # Normalize to internal format
    comics_data = normalize_result(result)
    
    # Upsert to shared DB
    for comic_data in comics_data:
        comic, created = Comic.objects.update_or_create(
            slug=comic_data['slug'],
            defaults=comic_data
        )
        
        # Trigger Next.js revalidation
        revalidate_comic(comic.slug)
    
    return {'processed': len(comics_data)}
```

```python
# apps/scrapers/engines/selenium_engine.py
def run_selenium_scraper(source):
    driver = get_chrome_driver()
    try:
        driver.get(source.url)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, source.selector))
        )
        return parse_with_beautifulsoup(driver.page_source)
    finally:
        driver.quit()
```

**Celery Beat** schedules periodic scrapes. **Flower** monitors tasks. **Sentry** catches failures.

---

## Chapter 4: The Frontend (Next.js 16)

Server Components by default. Client Components only for:

```tsx
// app/comics/[slug]/reader.tsx
'use client'

import { useReader } from '@/hooks/useReader'
import { ChapterNavigator } from '@/components/ChapterNavigator'

export default function Reader({ params }: { params: { slug: string } }) {
  const { chapter, nextChapter, prevChapter, goToPage } = useReader(params.slug)
  
  return (
    <div className="reader-container">
      <ChapterNavigator 
        current={chapter.number}
        total={chapter.comic.chapters.length}
        onNavigate={goToPage}
      />
      <ImageViewer pages={chapter.pages} />
    </div>
  )
}
```

**ISR (Incremental Static Regeneration):**

```typescript
// app/comics/[slug]/page.tsx
export const revalidate = 3600 // 1 hour

export async function generateStaticParams() {
  const comics = await prisma.comic.findMany({ where: { status: 'COMPLETED' } })
  return comics.map(c => ({ slug: c.slug }))
}
```

**Webhook revalidation:**

```typescript
// api/webhooks/django/route.ts
export async function POST(req: Request) {
  const { slug, event } = await req.json()
  if (event === 'comic.updated') {
    await revalidatePath(`/comics/${slug}`)
    await revalidatePath('/library')
  }
  return NextResponse.json({ ok: true })
}
```

---

## Chapter 5: Authentication — The Hard Part

**Django owns users.** Next.js trusts Django.

```python
# backend/apps/auth/jwt.py
def generate_tokens(user):
    access = AccessToken.for_user(user)
    access['email'] = user.email
    access['roles'] = list(user.groups.values_list('name', flat=True))
    return {
        'access': str(access),
        'refresh': str(RefreshToken.for_user(user))
    }
```

```typescript
// frontend/lib/auth.ts
export async function getServerSession() {
  const token = cookies().get('access_token')?.value
  if (!token) return null
  
  try {
    const payload = await verifyToken(token, DJANGO_JWT_PUBLIC_KEY)
    return { user: payload }
  } catch {
    return null
  }
}
```

**Shared secrets:** `DJANGO_JWT_PRIVATE_KEY` / `PUBLIC_KEY` in both `.env` files. Rotated quarterly.

---

## Chapter 6: Deployment

```
┌─────────────────────────────────────────────────────┐
│                  Docker Compose                      │
├─────────────┬─────────────┬──────────┬──────────────┤
│   Django    │   Next.js   │  Celery  │   Redis      │
│  (API:8000) │  (Web:3000) │ (Worker) │  (Broker)    │
├─────────────┼─────────────┼──────────┼──────────────┤
│   Postgres  │             │  Flower  │  (Monitor)   │
│  (Shared)   │             │          │              │
└─────────────┴─────────────┴──────────┴──────────────┘
```

**Production:**

- Django → Railway/Render (or GCP Cloud Run)
- Next.js → Vercel (edge functions, ISR, image optimization)
- Postgres → Neon (serverless) or managed PG
- Redis → Upstash (serverless)

---

## Chapter 7: What We Consolidated

| From | To | Effort |
|------|-----|--------|
| `comicwise` reader | Next.js frontend | 2 weeks |
| `rhixe_scans` upload/WebSocket | Next.js + Django | 3 weeks |
| `Django-Scrapy-Selenium` scrapers | Django backend | 1 week |
| `selenium_webdriver` | Python Selenium utils | 3 days |
| `xamehi` Django API | Django backend | 1 week |

**Total:** ~8 weeks. **Result:** One comic platform. One team. One deploy.

---

## Epilogue: The Platform That Ate Its Siblings

`rhixecompany-comics` didn't start as a consolidation target. It started as "the Django backend for the Next.js frontend."

Then it absorbed the scrapers. Then the reader. Then the admin. Then the legacy projects.

**The lesson:** Don't design the consolidated architecture upfront. Build the first piece well. Let the gravity of a good foundation pull the fragments in.

The database schema is the constitution. The ORMs are the interpreters. The API is the treaty. The frontend is the citizen.

**One platform. One database. One deploy. Many happy readers.**

---

*Written by the workspace chronicler, July 25, 2025.  
Filed at `projects/rhixecompany-comics/THE_STORY_OF_THIS_REPO.md`.*
