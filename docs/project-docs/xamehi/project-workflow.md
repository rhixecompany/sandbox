# Project Workflow — xamehi

## Development

```bash
# Install Node dependencies
npm install

# Install Python dependencies
pip install -r requirements.txt

# Copy environment
cp .env.example .env

# Django migrations
python manage.py migrate

# Start all 3 services (separate terminals)
# Terminal 1: Express backend
node index.js
# or: npm run server (nodemon)

# Terminal 2: Django backend
python manage.py runserver

# Terminal 3: React frontend
npm start
```

## Testing
```bash
npm test                 # React tests
python manage.py test    # Django tests
```

## Deployment
```bash
# React
npm run build

# Django
python manage.py collectstatic
gunicorn xamehi.wsgi:application --bind 0.0.0.0:8000

# Express
NODE_ENV=production node index.js
```
