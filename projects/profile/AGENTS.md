# Profile — Django Blog/CMS

Django 4.x + GCS + CKEditor.

## Stack
- Python 3.11+, PostgreSQL
- Google Cloud Storage for media
- CKEditor 5
- Deploy: Docker + GCP

## Commands
```bash
pip install -r requirements.txt
python manage.py migrate && python manage.py makemigrations
python manage.py collectstatic
python manage.py runserver
python manage.py test
```

## Notes
- `.env` — never commit; GCS credentials required
- CBVs preferred
- Static via GCS
