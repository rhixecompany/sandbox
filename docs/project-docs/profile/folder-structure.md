# Folder Structure — profile

```
profile/
├── profile/                     # Django project config
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── apps/                        # Django applications
│   ├── blog/                    # Blog functionality
│   │   ├── models.py            # Post, Tag, Comment
│   │   ├── views.py
│   │   ├── admin.py
│   │   └── templates/
│   ├── profiles/                # User profiles
│   │   ├── models.py
│   │   ├── views.py
│   │   └── admin.py
│   └── ...                      # Additional apps
├── static/                      # Static files
├── media/                       # User-uploaded media
├── templates/                   # Base templates
├── manage.py
├── requirements.txt
└── AGENTS.md
```
