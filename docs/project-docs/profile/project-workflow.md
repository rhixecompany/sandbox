# Project Workflow — profile

## Development

```bash
# Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser

# Run
python manage.py runserver

# After model changes
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
```

## Testing
```bash
python manage.py test
# or
pytest
```

## Deployment
```bash
python manage.py check --deploy
python manage.py collectstatic
gunicorn profile.wsgi:application --bind 0.0.0.0:8000
```
