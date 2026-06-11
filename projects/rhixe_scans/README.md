# Rhixescans

Read Comics Online!!!

A full-featured web application for reading comics online, built with Next.js, TypeScript, and PostgreSQL.

## Quick Start

```bash
# Install dependencies
npm install

# Set up environment variables
cp .env.example .env

# Run development server
npm run dev
```

Visit `http://localhost:3000` to view the application.

## Features

- **Comic Library**: Browse and search comics by genre, category, author, artist
- **Chapter Reading**: Read comics chapter by chapter with image viewer
- **User Accounts**: Sign up, sign in, manage profile
- **Bookmarks**: Save favorite comics for later
- **Admin Dashboard**: Manage comics, chapters, images (protected route)
- **Search**: Full-text search across comic library
- **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Next.js 15, React 19, TypeScript |
| Styling | Tailwind CSS, shadcn/ui |
| Database | PostgreSQL, Prisma ORM |
| Auth | NextAuth v5 (JWT) |
| Image Storage | Uploadthing, external CDN |
| Payments | Stripe, PayPal |

## Project Structure

```
rhixe_scans/
├── src/
│   ├── app/           # Next.js App Router pages
│   ├── components/    # React components (UI + feature)
│   ├── hooks/         # Custom React hooks
│   ├── lib/           # Utilities, actions, data access
│   └── types/         # TypeScript type definitions
├── docs/              # Documentation
├── tests/             # Test files
├── compose/           # Docker compose configs
└── public/            # Static assets
```

## Documentation

- [Architecture](./docs/ARCHITECTURE.md) - System design and data flow
- [Developer Guide](./docs/DEVELOPER_GUIDE.md) - Setup and development
- [User Guide](./docs/USER_GUIDE.md) - End-user documentation
- [Contributing](./docs/CONTRIBUTING.md) - Contribution guidelines
- [Code Docs](./docs/code-docs.md) - API documentation

## License

MIT