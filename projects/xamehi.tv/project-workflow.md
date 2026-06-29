# Project Workflow — xamehi.tv

## Development

```bash
# Backend
python -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver  # :8000

# Frontend (separate terminal)
cd frontend
npm install
npm start  # :3000 (proxied to :8000)
```

## Testing
```bash
python manage.py test        # Django tests
cd frontend && npm test      # React tests
```

## Deployment
```bash
# Backend
python manage.py collectstatic
gunicorn player.wsgi:application --bind 0.0.0.0:8000

# Frontend
cd frontend && npm run build
```
