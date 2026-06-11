# Developer Guide

## Prerequisites

- Node.js 18 or later
- npm or pnpm
- PostgreSQL (local or containerized)
- Docker (optional, for containerized setup)

## Setup

### 1. Clone and Install

```bash
git clone https://github.com/rhixecompany/rhixe_scans.git
cd rhixe_scans
npm install
```

### 2. Environment Variables

Copy the example environment file:

```bash
cp .env.example .env
```

Configure the following variables:

```env
# Database
DATABASE_URL="postgresql://user:password@localhost:5432/rhixescans"

# NextAuth
AUTH_SECRET="your-secret-key-here"

# GitHub OAuth (optional)
AUTH_GITHUB_ID="your-github-client-id"
AUTH_GITHUB_SECRET="your-github-client-secret"

# Image Upload (optional)
UPLOADTHING_SECRET="your-uploadthing-secret"
UPLOADTHING_APP_ID="your-uploadthing-app-id"

# Payments (optional)
STRIPE_SECRET_KEY="sk_test_..."
PAYPAL_CLIENT_ID="your-paypal-client-id"
```

### 3. Database Setup

```bash
# Run migrations
npm run db:migrate

# Seed the database (optional)
npm run db:seed
```

### 4. Run Development Server

```bash
npm run dev
```

The application will be available at `http://localhost:3000`.

## Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server with Turbo |
| `npm run build` | Build for production |
| `npm run start` | Start production server |
| `npm run lint` | Run ESLint |
| `npm run db:migrate` | Run Prisma migrations |
| `npm run db:reset` | Reset database and re-migrate |
| `npm run db:studio` | Open Prisma Studio |
| `npm run db:format` | Format Prisma schema |
| `npm run db:seed` | Seed database |
| `npm test` | Run Jest tests |

## Project Structure

```
rhixe_scans/
├── src/
│   ├── app/           # Next.js pages (App Router)
│   ├── components/    # React components
│   │   ├── ui/        # shadcn/ui components
│   │   ├── auth/      # Authentication components
│   │   └── shared/    # Shared components
│   ├── hooks/         # Custom React hooks
│   ├── lib/           # Core utilities
│   │   ├── actions/   # Server Actions
│   │   ├── data/      # Data access layer
│   │   └── constants/ # App constants
│   └── types/         # TypeScript types
├── prisma/
│   └── schema.prisma  # Database schema
├── tests/             # Test files
└── docs/              # Documentation
```

## Key Technologies

### Database (Prisma)

The database schema is defined in `src/db/schema.prisma`. Key models:
- User, Comic, Chapter, ChapterImage, ComicImage
- Category, Genre, Author, Artist
- Bookmark

### Authentication (NextAuth v5)

Configuration in `src/auth.config.ts`:
- GitHub OAuth provider
- Credentials provider (email/password)
- JWT session strategy

### Validation (Zod)

All form inputs are validated using Zod schemas defined in `src/lib/validators.ts`.

## Development Workflow

### Creating a New Component

1. Use shadcn/ui for base components:
   ```bash
   npx shadcn@latest add button
   ```

2. Create feature components in appropriate folder:
   - `src/components/auth/` - Auth forms
   - `src/components/admin/` - Admin UI
   - `src/components/shared/` - Reusable components

### Adding a New Database Model

1. Define schema in `prisma/schema.prisma`
2. Run migration: `npm run db:migrate`
3. Generate types: (automatic with Prisma)
4. Add validation schema in `src/lib/validators.ts`
5. Create data access in `src/lib/data/`
6. Create server action in `src/lib/actions/`

### Testing

```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run specific test file
npm test -- path/to/test.ts
```

## Docker Development

### Local Development with Docker

```bash
# Start PostgreSQL and local services
docker-compose -f docker-compose.local.yml up -d

# Start the application
npm run dev
```

### Production with Docker

```bash
# Start production stack
docker-compose -f docker-compose.production.yml up -d
```

## Troubleshooting

### Database Connection Issues

1. Ensure PostgreSQL is running
2. Check DATABASE_URL in .env
3. Verify database exists

### Build Errors

```bash
# Clean the build cache
npm run clean

# Rebuild
npm run build
```

### TypeScript Errors

Ensure TypeScript is properly configured and all dependencies are installed:
```bash
npx tsc --noEmit
```

## Further Reading

- [Architecture Documentation](./ARCHITECTURE.md)
- [Code Documentation](./code-docs.md)
- [Next.js Documentation](https://nextjs.org/docs)
- [Prisma Documentation](https://www.prisma.io/docs)
- [NextAuth Documentation](https://next-auth.js.org/)