# xamehi — Dual-Backend + React

Django + Express + React 18 legacy app.

## Stack
- Django + DRF (Python 3.10+)
- Express (Node.js, Nodemon)
- React 18 (CRA), Axios
- PostgreSQL

## Commands
```bash
npm install
npm start               # React
npm run server          # Express (nodemon)
python manage.py migrate && python manage.py runserver
python manage.py createsuperuser
npm test                # React
python manage.py test   # Django
```

## Build
```bash
npm run build
python manage.py collectstatic
gunicorn xamehi.wsgi:application --bind 0.0.0.0:8000
NODE_ENV=production node index.js
```

## Notes
- `.env` never commit; Django `SECRET_KEY` in env
- Ports: Express 5000, Django 8000, React 3000
- CORS; production HTTPS
