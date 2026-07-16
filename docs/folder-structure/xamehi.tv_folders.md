# xamehi.tv - Folder Structure Blueprint

**Project Path:** `C:\Users\Alexa\Desktop\SandBox\projects\xamehi.tv`
**Generated:** 2026-07-10
**Stack:** Django + React

## Directory Tree

```
xamehi.tv/
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/
│       └── ci.yml
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   ├── settings.json
│   └── tasks.json
├── AGENTS.md
├── API_REFERENCE.md
├── ARCHITECTURE.md
├── CHANGELOG.md
├── code-exemplars.md
├── CONTRIBUTING.md
├── copilot-instructions.md
├── cross-linking-report.md
├── DATABASE_SCHEMA.md
├── DEPLOYMENT_GUIDE.md
├── DEVELOPER_GUIDE.md
├── DEVELOPMENT_GUIDE.md
├── docs/
│   ├── audit-report.md
│   ├── CODE_DOCS.md
│   ├── Project_Architecture/
│   │   ├── exemplars.md
│   │   ├── Project_Architecture_Blueprint.md
│   │   ├── Project_Folder_Structure.md
│   │   ├── Technology_Stack_Blueprint.md
│   │   └── Workflow_Analysis.md
│   ├── PROJECT_DOCS.docx
│   └── PROJECT_DOCS.md
├── execution-summary.md
├── folder-structure.md
├── frontend/
│   ├── debug.log
│   ├── package-lock.json
│   ├── package.json
│   ├── public/
│   │   ├── index.html
│   │   ├── robots.txt
│   │   └── static/
│   │       ├── favicon.ico
│   │       ├── logo192.png
│   │       ├── logo512.png
│   │       └── manifest.json
│   └── src/
│       ├── actions/
│       │   ├── movieActions.js
│       │   ├── seriesActions.js
│       │   └── userActions.js
│       ├── App.js
│       ├── bootstrap.min.css
│       ├── components/
│       │   ├── Footer.js
│       │   ├── FormContainer.js
│       │   ├── Header.js
│       │   ├── Loader.js
│       │   ├── Message.js
│       │   ├── Movie.js
│       │   ├── MovieCarousel.js
│       │   ├── MovieForm.js
│       │   ├── Paginate.js
│       │   ├── Rating.js
│       │   ├── SearchBox.js
│       │   ├── SerieForm.js
│       │   ├── series/
│       │   │   ├── SeriesCreate.js
│       │   │   ├── SeriesEdit.js
│       │   │   └── SeriesList.js
│       │   ├── Series.js
│       │   ├── SeriesCarousel.js
│       │   └── SeriesPaginate.js
│       ├── constants/
│       │   ├── movieConstants.js
│       │   ├── seriesConstants.js
│       │   └── userConstants.js
│       ├── index.css
│       ├── index.js
│       ├── reducers/
│       │   ├── movieReducers.js
│       │   ├── seriesReducers.js
│       │   └── userReducers.js
│       ├── reportWebVitals.js
│       ├── screens/
│       │   ├── HomeScreen.js
│       │   ├── LoginScreen.js
│       │   ├── MovieScreen.js
│       │   ├── MoviesEditScreen.js
│       │   ├── MoviesListScreen.js
│       │   ├── MoviesScreen.js
│       │   ├── ProfileScreen.js
│       │   ├── RegisterScreen.js
│       │   ├── SerieScreen.js
│       │   ├── SeriesListScreen.js
│       │   ├── SeriesScreen.js
│       │   ├── UserEditScreen.js
│       │   └── UserListScreen.js
│       └── store.js
├── gunicorn.service
├── gunicorn.socket
├── manage.py
├── player/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Procfile
├── project-workflow.md
├── README.md
├── requirements.txt
├── RESEARCH_REPORT.md
├── runtime.txt
├── SECURITY.md
├── SETUP_GUIDE.md
├── static/
│   └── admin/
│       ├── css/
│       │   ├── autocomplete.css
│       │   ├── base.css
│       │   ├── changelists.css
│       │   ├── dashboard.css
│       │   ├── fonts.css
│       │   ├── forms.css
│       │   ├── login.css
│       │   ├── nav_sidebar.css
│       │   ├── responsive.css
│       │   ├── responsive_rtl.css
│       │   ├── rtl.css
│       │   └── widgets.css
│       ├── fonts/
│       │   ├── LICENSE.txt
│       │   ├── README.txt
│       │   ├── Roboto-Bold-webfont.woff
│       │   ├── Roboto-Light-webfont.woff
│       │   └── Roboto-Regular-webfont.woff
│       ├── img/
│       │   ├── calendar-icons.svg
│       │   ├── gis/
│       │   │   ├── move_vertex_off.svg
│       │   │   └── move_vertex_on.svg
│       │   ├── icon-addlink.svg
│       │   ├── icon-alert.svg
│       │   ├── icon-calendar.svg
│       │   ├── icon-changelink.svg
│       │   ├── icon-clock.svg
│       │   ├── icon-deletelink.svg
│       │   ├── icon-no.svg
│       │   ├── icon-unknown-alt.svg
│       │   ├── icon-unknown.svg
│       │   ├── icon-viewlink.svg
│       │   ├── icon-yes.svg
│       │   ├── inline-delete.svg
│       │   ├── LICENSE
│       │   ├── README.txt
│       │   ├── search.svg
│       │   ├── selector-icons.svg
│       │   ├── sorting-icons.svg
│       │   ├── tooltag-add.svg
│       │   └── tooltag-arrowright.svg
│       └── js/
│           ├── actions.js
│           ├── admin/
│           │   ├── DateTimeShortcuts.js
│           │   └── RelatedObjectLookups.js
│           ├── autocomplete.js
│           ├── calendar.js
│           ├── cancel.js
│           ├── change_form.js
│           ├── collapse.js
│           ├── core.js
│           ├── inlines.js
│           ├── jquery.init.js
│           ├── nav_sidebar.js
│           ├── popup_response.js
│           ├── prepopulate.js
│           ├── prepopulate_init.js
│           ├── SelectBox.js
│           ├── SelectFilter2.js
│           └── urlify.js
├── technology-stack.md
├── TESTING_GUIDE.md
├── USER_GUIDE.md
├── validation-report.md
└── video/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── decorators.py
    ├── filters.py
    ├── forms.py
    ├── migrations/
    │   ├── 0001_initial.py
    │   ├── 0002_alter_series_createdat.py
    │   └── __init__.py
    ├── models.py
    ├── pymongo_views.py
    ├── serializers.py
    ├── tests.py
    ├── url.py
    ├── urls/
    │   ├── movies_urls.py
    │   ├── series_urls.py
    │   └── user_urls.py
    ├── view.py
    └── views/
        ├── movies_views.py
        ├── series_views.py
        └── user_views.py
```

## Key Directories

| Directory | Purpose | Convention |
| ----------- | --------- | ------------ |
| `<app>/` | Django apps | lowercase, plural |
| `config/` / `settings/` | Settings modules | base/local/production |
| `templates/` | HTML templates | app-specific subdirs |
| `static/` | Static assets | Collected by collectstatic |

## Naming Conventions

- **Directories:** kebab-case (multi-word) or lowercase
- **Files:** Match language convention (PascalCase for React, snake_case for Python)
- **Configs:** lowercase with extension (.json, .yaml, .toml)

## File Placement Patterns

- Tests: co-located (`__tests__/`) or mirrored `tests/` structure
- Types: `types/` or co-located with implementation
- Config: Root level for tool configs

---
*Generated by agents-system-prompt-context-fix-runner*
