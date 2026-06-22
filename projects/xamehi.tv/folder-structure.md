# Folder Structure — xamehi.tv

```
xamehi.tv/
├── backend/                     # Django project
│   ├── player/                  # Django project config
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── apps/                    # Django applications
│   │   ├── movies/              # Movie management
│   │   ├── reviews/             # User reviews
│   │   ├── users/               # User accounts
│   │   └── payments/            # PayPal integration
│   ├── static/
│   ├── templates/
│   ├── manage.py
│   └── requirements.txt
├── frontend/                    # React frontend
│   ├── public/
│   ├── src/
│   │   ├── components/          # React components (MUI)
│   │   ├── screens/             # Page components
│   │   ├── actions/             # Redux actions
│   │   ├── reducers/            # Redux reducers
│   │   └── constants/           # Action constants
│   ├── package.json
│   └── ...
├── Procfile                     # Heroku deployment
└── AGENTS.md
```
