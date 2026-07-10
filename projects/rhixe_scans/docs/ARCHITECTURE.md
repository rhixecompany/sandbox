# Architecture Documentation

## System Overview

Rhixescans is a comic reading web application built on the Next.js App Router architecture. It provides a platform for users to browse, search, and read comics online with user authentication and bookmarking capabilities.

## Technology Stack

### Frontend Layer

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript (strict mode)
- **UI Library**: React 19
- **Styling**: Tailwind CSS + shadcn/ui components
- **State**: React Hooks + Server Actions

### Backend Layer

- **Runtime**: Next.js API Routes / Server Actions
- **ORM**: Prisma 6
- **Database**: PostgreSQL

### Authentication

- **Provider**: NextAuth v5 (beta)
- **Strategy**: JWT (1-day expiry)
- **Providers**: GitHub OAuth + Credentials (email/password)

### External Services

- **Image Storage**: Uploadthing + external CDN (asuracomic.net)
- **Payments**: Stripe, PayPal

## Data Model

### Core Entities

```
User
├── id: UUID
├── name: String
├── email: String (unique)
├── password: String (hashed)
├── role: Enum (USER, ADMIN)
├── image: String (nullable)
└── createdAt: DateTime

Comic
├── id: UUID
├── title: String
├── slug: String (unique)
├── description: Text
├── rating: Decimal
├── status: Enum (ONGOING, COMPLETED, HIATUS, CANCELLED)
├── link: String
├── serialization: String
├── numimages: Int
├── numchapters: Int
├── has_images: Boolean
├── has_chapters: Boolean
├── updated_at: DateTime
├── category_id: UUID
├── author_id: UUID
├── artist_id: UUID
└── createdAt: DateTime

Chapter
├── id: UUID
├── name: String
├── slug: String
├── title: String (nullable)
├── link: String
├── numimages: Int
├── has_images: Boolean
├── updated_at: DateTime
├── comic_id: UUID
└── createdAt: DateTime

ComicImage
├── id: UUID
├── link: String
├── image: String (nullable)
├── checksum: String (nullable)
├── status: Enum (PENDING, PROCESSING, COMPLETED, FAILED)
├── comic_id: UUID
└── createdAt: DateTime

ChapterImage
├── id: UUID
├── link: String
├── image: String (nullable)
├── checksum: String (nullable)
├── status: Enum
├── comic_id: UUID
├── chapter_id: UUID
└── createdAt: DateTime

Category
├── id: UUID
├── name: String
└── createdAt: DateTime

Genre
├── id: UUID
├── name: String
├── comics: Comic[]
└── createdAt: DateTime

Author / Artist
├── id: UUID
├── name: String
└── createdAt: DateTime

Bookmark
├── id: UUID
├── user_id: UUID (nullable - guest bookmarks)
├── session_id: String
├── items: JSON
└── createdAt: DateTime
```

## Application Structure

### Route Architecture

```
src/app/
├── (auth)/              # Authenticated routes
│   ├── sign-in/         # Sign in page
│   ├── sign-up/         # Sign up page
│   └── logout/          # Logout handler
├── (root)/              # Public routes
│   ├── page.tsx         # Home page (comic listing)
│   └── layout.tsx      # Root layout
├── admin/               # Admin dashboard (protected)
│   ├── page.tsx        # Admin overview
│   ├── main-nav.tsx    # Admin navigation
│   └── layout.tsx      # Admin layout
├── api/                 # API routes
│   └── auth/[...nextauth]/route.ts
├── layout.tsx          # Global layout
├── loading.tsx         # Global loading state
└── not-found.tsx      # 404 page
```

### Component Architecture

```
src/components/
├── ui/                  # shadcn/ui base components
│   ├── button.tsx
│   ├── input.tsx
│   ├── dialog.tsx
│   └── ... (40+ components)
├── auth/               # Auth-related components
│   ├── login-form.tsx
│   ├── sign-up-form.tsx
│   └── credentials-signin-form.tsx
├── shared/
│   ├── header/         # Navigation header
│   └── pagination.tsx
├── admin/              # Admin components
├── chart-area-interactive.tsx
├── data-table.tsx
├── footer.tsx
├── site-header.tsx
└── section-cards.tsx
```

### Data Access Layer

```
src/lib/
├── db.ts               # Prisma client singleton
├── prisma.ts           # Alternative Prisma client
├── utils.ts            # Utility functions
├── validators.ts       # Zod validation schemas
├── schema.ts           # Auth schema
├── constants/          # Application constants
├── data/               # Data access objects
│   ├── user.ts
│   ├── comic.ts
│   ├── chapter.ts
│   └── ...
└── actions/            # Server Actions
    ├── user.actions.ts
    ├── comic.actions.ts
    ├── chapter.actions.ts
    └── bookmark.actions.ts
```

## Authentication Flow

1. **Sign In**: User provides email/password
2. **Validation**: Credentials validated against database
3. **Token Generation**: JWT created with user info
4. **Session**: Token stored in HTTP-only cookie
5. **Middleware**: Protected routes check token validity
6. **Redirect**: Unauthenticated users redirected to `/sign-in`

## API Routes

### Authentication

- `GET /api/auth/[...nextauth]` - NextAuth handler
- Handles GitHub OAuth and credentials flow

### Server Actions

- `createUser`, `updateUser`, `deleteUser`
- `createComic`, `updateComic`, `deleteComic`
- `createChapter`, `updateChapter`, `deleteChapter`
- `addBookmark`, `removeBookmark`

## Security

- **Passwords**: Stored as plain text (not recommended - needs hashing)
- **Route Protection**: Middleware protects `/admin/*`
- **Input Validation**: Zod schemas for all inputs
- **Environment Variables**: AUTH_SECRET required for JWT signing
- **Image Domains**: Whitelisted in next.config.ts

## Performance Considerations

- **Image Optimization**: Next.js Image component with CDN
- **Database**: Prisma with proper indexing
- **Caching**: React cache for server components
- **Debouncing**: use-debounce for search inputs

## Deployment

### Requirements

- Node.js 18+
- PostgreSQL database
- Docker (optional)

### Environment Variables

```
DATABASE_URL=postgresql://...
AUTH_SECRET=...
AUTH_GITHUB_ID=...
AUTH_GITHUB_SECRET=...
UPLOADTHING_SECRET=...
UPLOADTHING_APP_ID=...
STRIPE_SECRET_KEY=...
PAYPAL_CLIENT_ID=...
```

### Docker Support

- `docker-compose.local.yml` - Local development
- `docker-compose.production.yml` - Production deployment
- `compose/production/` - Production configs (Traefik, Redis)
