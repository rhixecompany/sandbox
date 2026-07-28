# profile — Folder Structure

> **Stack:** Django  
> **Type:** Profile/Portfolio Application  
> **Status:** Active

## Directory Tree

```
profile/
├── .github/workflows/
├── .vscode/
├── base/                      # Base Django app
│   ├── migrations/
│   ├── static/                # Static assets
│   │   ├── admin/
│   │   ├── ckeditor/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   └── templates/
├── rhixecompany/              # Company app
│   └── migrations/
├── static/                    # Project-level static assets
│   ├── admin/css/
│   ├── admin/fonts/
│   ├── admin/img/
│   ├── admin/js/
│   ├── ckeditor/
│   │   ├── ckeditor/
│   │   ├── ckeditor_uploader/
│   │   ├── file-icons/
│   │   └── galleriffic/
│   ├── css/
│   ├── images/
│   │   ├── images/
│   │   └── uploads/
│   └── js/
├── templates/
│   └── base/
├── manage.py
├── requirements.txt
└── migrate.yaml
```

## Key Patterns

- **Standard Django layout:** Apps (`base/`, `rhixecompany/`) under project root
- **Dual static structure:** Both app-level and project-level `static/` directories
- **Static subdirectories** mirror Django's static file finder organization
- **CKEditor** has dedicated subdirectory structure under static
