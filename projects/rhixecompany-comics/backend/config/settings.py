"""Django settings for rhixecompany-comics."""
from __future__ import annotations

import os
from pathlib import Path
from urllib.parse import urlparse

BASE_DIR = Path(__file__).resolve().parent.parent

def _env(name: str, default: str = '') -> str:
    return os.getenv(name, default)

def _csv_env(name: str, default: str = '') -> list[str]:
    raw = _env(name, default)
    return [item.strip() for item in raw.split(',') if item.strip()]

def _database_config() -> dict[str, object]:
    database_url = _env('DATABASE_URL')
    if not database_url:
        return {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }

    parsed = urlparse(database_url)
    scheme = parsed.scheme.lower()
    if scheme in {'postgres', 'postgresql'}:
        return {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': parsed.path.lstrip('/') or 'rhixecompany_comics',
            'USER': parsed.username or '',
            'PASSWORD': parsed.password or '',
            'HOST': parsed.hostname or 'localhost',
            'PORT': parsed.port or 5432,
        }
    if scheme == 'sqlite':
        return {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': parsed.path.lstrip('/') or BASE_DIR / 'db.sqlite3',
        }
    return {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

SECRET_KEY = _env('DJANGO_SECRET_KEY', 'django-insecure-rhixecompany-comics-dev-only')
DEBUG = _env('DJANGO_DEBUG', 'true').lower() in {'1', 'true', 'yes', 'on'}
ALLOWED_HOSTS = _csv_env('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1,::1')
CSRF_TRUSTED_ORIGINS = _csv_env('DJANGO_CSRF_TRUSTED_ORIGINS')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_filters',
    'rest_framework',
    'drf_spectacular',
    'apps.core',
    'apps.comics',
    'apps.scraping',
    'apps.users',
    'apps.api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'
DATABASES = {'default': _database_config()}
AUTH_USER_MODEL = 'users.User'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = _env('DJANGO_TIME_ZONE', 'UTC')
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS: list[Path] = []
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = _csv_env('CORS_ALLOWED_ORIGINS')
CORS_ALLOW_ALL_ORIGINS = not CORS_ALLOWED_ORIGINS and DEBUG

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Rhixecompany Comics API',
    'DESCRIPTION': 'API surface for the consolidated comics platform.',
    'VERSION': '0.1.0',
}

CELERY_BROKER_URL = _env('CELERY_BROKER_URL', _env('REDIS_URL', 'redis://localhost:6379/0'))
CELERY_RESULT_BACKEND = _env('CELERY_RESULT_BACKEND', CELERY_BROKER_URL)
CELERY_TASK_ALWAYS_EAGER = _env('CELERY_TASK_ALWAYS_EAGER', 'false').lower() in {'1', 'true', 'yes', 'on'}
