# Profile — Django Blog/CMS
## Architecture

- **Blueprint**: [profile Architecture](../docs/Project_Architecture/profile_architecture.md)
- **Folders**: [profile Folder Structure](../docs/Project_Architecture/profile_folders.md)
- **Tech Stack**: [profile Technology Stack](../docs/Project_Architecture/profile_techstack.md)
- **Stack Type**: Unknown


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
