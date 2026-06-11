# Contributing to Rhixescans

Thank you for your interest in contributing to Rhixescans!

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. We are committed to providing a welcoming and inclusive environment for all contributors.

## How to Contribute

### Reporting Bugs

1. Check existing issues to avoid duplicates
2. Use the bug report template
3. Include:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots if applicable
   - Environment details

### Suggesting Features

1. Check existing feature requests
2. Use the feature request template
3. Describe:
   - The problem you're solving
   - Proposed solution
   - Alternative approaches considered

### Pull Requests

#### Before Submitting

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Follow the coding standards
4. Write tests for new functionality
5. Update documentation if needed

#### Submitting

1. Push your changes:
   ```bash
   git push origin feature/your-feature-name
   ```
2. Open a Pull Request
3. Fill out the PR template completely
4. Wait for review

## Development Setup

See [DEVELOPER_GUIDE.md](./DEVELOPER_GUIDE.md) for detailed setup instructions.

### Quick Start

```bash
# Clone and install
git clone https://github.com/rhixecompany/rhixe_scans.git
cd rhixe_scans
npm install

# Set up environment
cp .env.example .env

# Run development server
npm run dev
```

## Coding Standards

### TypeScript

- Use strict TypeScript mode
- Avoid `any` types
- Use proper type annotations
- Follow existing patterns in codebase

### React/Next.js

- Use functional components with hooks
- Follow Next.js App Router conventions
- Use Server Components where appropriate
- Keep components small and focused

### Styling

- Use Tailwind CSS classes
- Follow shadcn/ui component patterns
- Maintain responsive design
- Use design tokens from theme

### Git Commit Messages

Follow conventional commits:

```
type(scope): description

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

Example:
```
feat(auth): add password reset functionality

Implements password reset flow with email verification.
Closes #123
```

## Testing

### Running Tests

```bash
# All tests
npm test

# Watch mode
npm run test:watch

# Coverage
npm run test:coverage
```

### Writing Tests

- Use Jest for unit tests
- Follow AAA pattern (Arrange, Act, Assert)
- Test edge cases
- Keep tests focused and isolated

## Documentation

- Update README if needed
- Add JSDoc comments to functions
- Update API documentation
- Include setup instructions for new features

## Review Process

1. **Automated Checks**: CI runs linting, tests, and builds
2. **Code Review**: At least one maintainer reviews
3. **Feedback**: Address review comments
4. **Merge**: Once approved, maintainers merge

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- GitHub profile

## Questions?

- Open an issue for bugs/feature requests
- Start a discussion for general questions
- Join our community chat (link in README)

Thank you for contributing to Rhixescans!