# Contributing to Xamehi.tv

Thank you for your interest in contributing to Xamehi.tv! This guide covers how to contribute to our Django + React movie streaming platform.

## Code of Conduct

Please read our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) to understand the standards we expect from all contributors.

## Getting Started

### 1. Fork and Clone

```bash
git clone https://github.com/rhixecompany/xamehi.tv.git
cd xamehi.tv
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate
```

### 3. Set Up Frontend

```bash
cd frontend
npm install
npm run build
cd ..
```

### 4. Start Development Server

```bash
python manage.py runserver
```

## Tech Stack

- **Backend**: Django, Django REST Framework, DRF SimpleJWT, Django AllAuth
- **Frontend**: React (built as static files)
- **Database**: SQLite (dev) / PostgreSQL (production)
- **Deployment**: Heroku, Gunicorn, WhiteNoise

## Development Workflow

1. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following existing Django and React patterns

3. **Test your changes**:
   ```bash
   python manage.py test
   ```

4. **Commit with a clear message**:
   ```bash
   git commit -m "feat: add your feature description"
   ```

5. **Push and open a Pull Request**:
   ```bash
   git push origin feature/your-feature-name
   ```

## Standards

- Follow Django and React best practices
- Use Django REST Framework serializers for API endpoints
- Write meaningful commit messages (Conventional Commits format)
- Add tests for new functionality
- Keep PRs focused and atomic

## Pull Request Process

1. Ensure all tests pass (`python manage.py test`)
2. Update documentation if needed
3. Request review from maintainers
4. Address review feedback promptly

## Questions?

Open an issue for discussion before starting large contributions.
# Contributing to Xamehi.tv

Thank you for your interest in contributing to Xamehi.tv! This guide covers how to contribute to our Django + React movie streaming platform.

## Code of Conduct

Please read our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) to understand the standards we expect from all contributors.

## Getting Started

### 1. Fork and Clone

```bash
git clone https://github.com/rhixecompany/xamehi.tv.git
cd xamehi.tv
```

### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate
```

### 3. Set Up Frontend

```bash
cd frontend
npm install
npm run build
cd ..
```

### 4. Start Development Server

```bash
python manage.py runserver
```

## Tech Stack

- **Backend**: Django, Django REST Framework, DRF SimpleJWT, Django AllAuth
- **Frontend**: React (built as static files)
- **Database**: SQLite (dev) / PostgreSQL (production)
- **Deployment**: Heroku, Gunicorn, WhiteNoise

## Development Workflow

1. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following existing Django and React patterns

3. **Test your changes**:
   ```bash
   python manage.py test
   ```

4. **Commit with a clear message**:
   ```bash
   git commit -m "feat: add your feature description"
   ```

5. **Push and open a Pull Request**:
   ```bash
   git push origin feature/your-feature-name
   ```

## Standards

- Follow Django and React best practices
- Use Django REST Framework serializers for API endpoints
- Write meaningful commit messages (Conventional Commits format)
- Add tests for new functionality
- Keep PRs focused and atomic

## Pull Request Process

1. Ensure all tests pass (`python manage.py test`)
2. Update documentation if needed
3. Request review from maintainers
4. Address review feedback promptly

## Questions?

Open an issue for discussion before starting large contributions.
