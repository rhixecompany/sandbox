# Sandbox Patch Discovery

Generated: 2026-05-29 19:02:34 WCAST

## Patch Discovery Matrix

| patch-file | full-path | suggested-target-project | mapping-confidence | mapping-reason | reviewed-by |
| --- | --- | --- | --- | --- | --- |
| `Bash/edits/run-audit.sh.patch` | `C:/Users/Alexa/Desktop/SandBox/Bash/edits/run-audit.sh.patch` | `Bash/scripts/run-audit.sh` | high | filename and target path align exactly | Hermes |
| `patches/pre-applied/python-projects.patch` | `C:/Users/Alexa/Desktop/SandBox/patches/pre-applied/python-projects.patch` | `projects/Python-projects` | high | git-format patch already represented in the repo history | Hermes |
| `patches/pre-applied/xamehi.patch` | `C:/Users/Alexa/Desktop/SandBox/patches/pre-applied/xamehi.patch` | `projects/xamehi` | high | git-format patch already represented in the repo history | Hermes |
| `patches/pre-applied/youtube-downloader.patch` | `C:/Users/Alexa/Desktop/SandBox/patches/pre-applied/youtube-downloader.patch` | `projects/youtube-downloader` | high | git-format patch already represented in the repo history | Hermes |
| `patches/enhanced/django-scrapy-selenium.patch` | `C:/Users/Alexa/Desktop/SandBox/patches/enhanced/django-scrapy-selenium.patch` | `projects/Django-Scrapy-Selenium` | medium | content paths align to the Django/Scrapy project layout | Hermes |
| `patches/enhanced/xamehi-tv.patch` | `C:/Users/Alexa/Desktop/SandBox/patches/enhanced/xamehi-tv.patch` | `projects/xamehi.tv` | medium | content paths align to the streaming project layout | Hermes |
| `patches/obsolete/cookiecutter-django-tailwind.patch` | `C:/Users/Alexa/Desktop/SandBox/patches/obsolete/cookiecutter-django-tailwind.patch` | `projects/cookiecutter-django-tailwind` | low | cookiecutter template scaffolding; no active project target needs the patch applied | Hermes |

## Totals

- Total patches discovered: 7
- High confidence mappings: 4
- Medium confidence mappings: 2
- Low confidence mappings: 1

## Low-Confidence Review Queue

| patch-file | proposed-target | issue | required-action | owner | status |
| --- | --- | --- | --- | --- | --- |
| `patches/obsolete/cookiecutter-django-tailwind.patch` | `projects/cookiecutter-django-tailwind` | template patch, no active target | mark obsolete and preserve | Hermes | closed |
