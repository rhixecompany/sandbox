# Code Documentation - Rhixescans

Google Style documentation for core TypeScript/JavaScript files.

---

## Core Library Files

### src/lib/prisma.ts

```typescript
import { PrismaClient } from '@prisma/client';

const globalForPrisma = globalThis as unknown as { prisma: PrismaClient };

export const prisma =
  globalForPrisma.prisma ||
  new PrismaClient().$extends({
    result: {
      comic: {
        rating: {
          compute(comic) {
            return comic.rating.toString();
          },
        },
      },
    },
  });

if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma;
```

**Description:** Prisma client singleton with extended computed fields.
- Uses global singleton pattern to prevent multiple connections in development
- Extends Prisma with computed `rating` field that converts numeric rating to string
- Automatically persists client in development mode

---

### src/lib/db.ts

```typescript
import { PrismaClient } from '@prisma/client';

const prismaClientSingleton = () => {
  return new PrismaClient().$extends({
    result: {
      comic: {
        rating: {
          compute(comic) {
            return comic.rating.toString();
          },
        },
      },
    },
  });
};

declare const globalThis: {
  prismaGlobal: ReturnType<typeof prismaClientSingleton>;
} & typeof global;

const db = globalThis.prismaGlobal ?? prismaClientSingleton();

export default db;

if (process.env.NODE_ENV !== 'production') globalThis.prismaGlobal = db;
```

**Description:** Alternative Prisma client instance with singleton pattern.
- Identical functionality to prisma.ts, provides alternative import
- Ensures single database connection across hot reloads in development

---

### src/lib/utils.ts

Utility functions for the application.

**Functions:**
- `cn(...inputs: ClassValue[]): string` - Merges Tailwind CSS classes
- `convertToPlainObject<T>(value: T): T` - Converts Prisma objects to plain JS objects
- `formatNumberWithDecimal(num: number): string` - Formats numbers with 2 decimal places
- `formatError(error: any): string` - Formats Zod, Prisma, and generic errors
- `round2(value: number | string): number` - Rounds to 2 decimal places
- `formatCurrency(amount: number | string | null): string` - Formats as USD currency
- `formatNumber(number: number): string` - Formats numbers with US locale
- `formatId(id: string): string` - Shortens UUID to last 6 characters
- `formatDateTime(dateString: Date): object` - Returns date, time, and datetime formatted strings
- `formUrlQuery({params, key, value}): string` - Updates URL query parameters

---

### src/lib/validators.ts

Zod validation schemas for forms and API requests.

**Authentication Schemas:**
- `signInFormSchema` - Email and password validation (password min 6 chars)
- `signUpFormSchema` - Name, email, password with confirm password matching
- `updateProfileSchema` - Name and email updates
- `updateUserSchema` - Extends profile with id and role

**Data Schemas:**
- `insertComicImageSchema` / `updateComicImageSchema` - Comic image validation
- `insertChapterImageSchema` / `updateChapterImageSchema` - Chapter image validation
- `insertGenreSchema` / `updateGenreSchema` - Genre validation
- `insertCategorySchema` / `updateCategorySchema` - Category validation
- `insertAuthorSchema` / `updateAuthorSchema` - Author validation
- `insertArtistSchema` / `updateArtistSchema` - Artist validation
- `insertComicSchema` / `updateComicSchema` - Full comic with relations
- `insertChapterSchema` / `updateChapterSchema` - Chapter with nested comic
- `bookmarkItemSchema` / `insertBookmarkSchema` - Bookmark items

---

### src/lib/schema.ts

```typescript
import { z } from 'zod';

const schema = z.object({
  email: z.string().email(),
  password: z.string().min(1),
});

type Schema = z.infer<typeof schema>;

export { schema, type Schema };
```

**Description:** Basic auth credentials validation schema.

---

## Authentication

### src/auth.ts

```typescript
import NextAuth from 'next-auth';
import authConfig from './auth.config';

export const { handlers, auth, signIn, signOut } = NextAuth({
  ...authConfig,
});
```

**Description:** NextAuth configuration entry point.
- Exports handlers, auth, signIn, signOut from NextAuth with custom config

---

### src/auth.config.ts

NextAuth configuration with GitHub and Credentials providers.

**Configuration:**
- `adapter`: PrismaAdapter for database session storage
- `providers`: GitHub OAuth + Credentials (email/password)
- `session.strategy`: JWT with 1-day max age
- `pages.signIn`: `/sign-in`
- `pages.newUser`: `/sign-up`

**Credentials Authorize:**
- Validates credentials using Zod schema
- Queries user by email and password
- Throws error if user not found

---

### src/middleware.ts

```typescript
import { getToken } from 'next-auth/jwt';
import { NextRequest, NextResponse } from 'next/server';

export async function middleware(request: NextRequest) {
  const token = await getToken({
    req: request,
    secret: process.env.AUTH_SECRET,
  });

  if (!token) {
    return NextResponse.redirect(new URL('/sign-in', request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/admin/:path*'],
};
```

**Description:** Route protection middleware.
- Protects `/admin/*` routes requiring authentication
- Redirects unauthenticated users to `/sign-in`
- Uses JWT token validation via next-auth/jwt

---

## Configuration

### next.config.ts

Next.js configuration with image domains and build settings.

**Image Domains:**
- `localhost:8000` - Local media server
- `gg.asuracomic.net` - External comic images
- `utfs.io` - Uploadthing CDN
- `avatars.githubusercontent.com` - GitHub avatars
- `lh3.googleusercontent.com` - Google avatars
- `icons8.com` - Icon assets

**Build Settings:**
- ESLint enabled during builds
- TypeScript strict mode enabled

---

### src/lib/constants/index.ts

(Reference constants file - import COMIC_STATUS, IMAGE_STATUS)

---

## Component Patterns

### UI Components

The project uses Radix UI primitives wrapped with shadcn/ui:
- Button, Input, Select, Dialog, Dropdown, etc.
- All located in `src/components/ui/`

### Shared Components

- `src/components/shared/header/` - Navigation header components
- `src/components/auth/` - Sign-in, sign-up, login forms

---

## Data Access Patterns

### Data Layer (src/lib/data/)

- `user.ts`, `genre.ts`, `category.ts`, `author.ts`, `artist.ts`
- `comic.ts`, `chapter.ts`, `comicimage.ts`, `chapterimage.ts`

### Actions Layer (src/lib/actions/)

- `user.actions.ts`, `comic.actions.ts`, `chapter.actions.ts`, `bookmark.actions.ts`

---

## Notes

- This is a Next.js 15 application with App Router
- Uses TypeScript with strict mode
- Database: PostgreSQL with Prisma ORM
- Authentication: NextAuth v5 with JWT strategy
- UI: Tailwind CSS with shadcn/ui components
- Image hosting: Uploadthing + external CDN