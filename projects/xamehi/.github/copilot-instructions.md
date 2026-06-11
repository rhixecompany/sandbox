# Copilot Instructions

Project-wide guidance for Xamehi.

## Source of truth

- `projects/xamehi/AGENTS.md`
- `README.md`
- `manage.py`
- `index.js`
- `src/`

## Commands

Run from the project root:

```bash
npm install
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
node index.js
npm start
python manage.py test
npm test
python manage.py makemigrations
python manage.py collectstatic
```

## Architecture

- Legacy dual-backend app combining Django and Express.js with a React frontend.
- Django serves core backend concerns; Express is a separate Node entrypoint.
- The frontend communicates with both backends through Axios.

## Conventions

- Keep Python and JavaScript concerns separated by backend.
- Use Django ORM and DRF patterns on the Python side.
- Use CommonJS in Express files and ES modules in React code where the repo already does.
- Keep CORS and secret handling environment-driven.

