<<<<<<< HEAD
# Contributing to Xamehi

Thank you for your interest in contributing to Xamehi! This guide covers how to contribute to our React + Express.js web application.

## Code of Conduct

Please read our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) to understand the standards we expect from all contributors.

## Getting Started

### 1. Fork and Clone

```bash
git clone https://github.com/rhixecompany/xamehi.git
cd xamehi
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Configure Environment

Create a `.env` file:

```env
REACT_APP_RAPID_API_KEY=your_rapidapi_key_here
```

### 4. Start Development

```bash
# Terminal 1: Backend
npm run server

# Terminal 2: Frontend
npm start
```

## Tech Stack

- **Frontend**: React 18, Axios, React Testing Library
- **Backend**: Express.js, CORS, Nodemon
- **External APIs**: Alpha Vantage, Crypto News Live

## Development Workflow

1. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following existing code patterns

3. **Test your changes**:
   ```bash
   npm test
   ```

4. **Build for production** (verify no build errors):
   ```bash
   npm run build
   ```

5. **Commit with a clear message**:
   ```bash
   git commit -m "feat: add your feature description"
   ```

6. **Push and open a Pull Request**:
   ```bash
   git push origin feature/your-feature-name
   ```

## Standards

- Follow React and Express.js best practices
- Use functional components with hooks
- Write meaningful commit messages (Conventional Commits format)
- Add tests for new components
- Keep PRs focused and atomic

## Pull Request Process

1. Ensure all tests pass (`npm test`)
2. Verify production build succeeds (`npm run build`)
3. Update documentation if needed
4. Request review from maintainers
5. Address review feedback promptly

## Questions?

Open an issue for discussion before starting large contributions.
=======
# Contributing to Xamehi

Thank you for your interest in contributing to Xamehi! This guide covers how to contribute to our React + Express.js web application.

## Code of Conduct

Please read our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) to understand the standards we expect from all contributors.

## Getting Started

### 1. Fork and Clone

```bash
git clone https://github.com/rhixecompany/xamehi.git
cd xamehi
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Configure Environment

Create a `.env` file:

```env
REACT_APP_RAPID_API_KEY=your_rapidapi_key_here
```

### 4. Start Development

```bash
# Terminal 1: Backend
npm run server

# Terminal 2: Frontend
npm start
```

## Tech Stack

- **Frontend**: React 18, Axios, React Testing Library
- **Backend**: Express.js, CORS, Nodemon
- **External APIs**: Alpha Vantage, Crypto News Live

## Development Workflow

1. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following existing code patterns

3. **Test your changes**:
   ```bash
   npm test
   ```

4. **Build for production** (verify no build errors):
   ```bash
   npm run build
   ```

5. **Commit with a clear message**:
   ```bash
   git commit -m "feat: add your feature description"
   ```

6. **Push and open a Pull Request**:
   ```bash
   git push origin feature/your-feature-name
   ```

## Standards

- Follow React and Express.js best practices
- Use functional components with hooks
- Write meaningful commit messages (Conventional Commits format)
- Add tests for new components
- Keep PRs focused and atomic

## Pull Request Process

1. Ensure all tests pass (`npm test`)
2. Verify production build succeeds (`npm run build`)
3. Update documentation if needed
4. Request review from maintainers
5. Address review feedback promptly

## Questions?

Open an issue for discussion before starting large contributions.
>>>>>>> ef7c89f (chore: initial local project setup for xamehi)
