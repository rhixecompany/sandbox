# Setup Guide

## Prerequisites

- Node.js 18+ (recommended: latest LTS)
- npm or yarn
- Git

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd comicwise
```

2. Install dependencies:
```bash
npm install
# or
yarn install
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Start the development server:
```bash
npm run dev
# or
yarn dev
```

## Common Commands

| Command | Description |
| --- | --- |
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run lint` | Run linter |
| `npm test` | Run tests |

## Project Structure

- `src/` - Source code
- `docs/` - Documentation
- `tests/` - Test files

## Troubleshooting

If you encounter issues:
1. Clear node_modules and reinstall
2. Check Node.js version matches requirements
3. Verify .env configuration is correct