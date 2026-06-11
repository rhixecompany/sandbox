# ruff: noqa: E501
from .base import *  # noqa: F403
from .base import BASE_DIR
from .base import INSTALLED_APPS
from .base import MIDDLEWARE
from .base import WEBPACK_LOADER
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="UOSOKcOEulAWWuSm3T0fJmNJEVIBcuses60B2Lalb4Rsp43OGlAbUbR0LdI3n3wt",  # type: ignore  # noqa: PGH003
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
# ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]  # noqa: ERA001, RUF100, S104
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost"])  # type: ignore  # noqa: PGH003

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    },
}

# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_ACCESS_KEY_ID = env("DJANGO_AWS_ACCESS_KEY_ID",default="ae187701acd22a77779ce3ebfa32e101")  # type: ignore  # noqa: PGH003
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_SECRET_ACCESS_KEY = env("DJANGO_AWS_SECRET_ACCESS_KEY",default="c92576a34dd08fbd5932efe0a32cf363f5a17c5af1da5ec4c390da815dab6962") # type: ignore  # noqa: PGH003
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME",default="mystore") # type: ignore  # noqa: PGH003
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_QUERYSTRING_AUTH = False
# # DO NOT change these unless you know what you're doing.
# _AWS_EXPIRY = 60 * 60 * 24 * 7
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_S3_OBJECT_PARAMETERS = {
#     "CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate",
# }
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_S3_MAX_MEMORY_SIZE = env.int(
#     "DJANGO_AWS_S3_MAX_MEMORY_SIZE",
#     default=100_000_000,  # 100MB # type: ignore  # noqa: PGH003
# )
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#settings
# AWS_S3_REGION_NAME = env("DJANGO_AWS_S3_REGION_NAME", default="us-east-2")  # type: ignore  # noqa: PGH003
# # https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html#cloudfront
# AWS_S3_CUSTOM_DOMAIN = env("DJANGO_AWS_S3_CUSTOM_DOMAIN", default="fowvdrdkbqhmevigbkyb.supabase.co/storage/v1/s3")  # type: ignore  # noqa: PGH003
# aws_s3_domain = AWS_S3_CUSTOM_DOMAIN or f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
# # STATIC & MEDIA
# # ------------------------
# STORAGES = {
#     "default": {
#         "BACKEND": "storages.backends.s3.S3Storage",
#         "OPTIONS": {
#             "location": "media",
#             "file_overwrite": False,
#         },
#     },
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }
# MEDIA_URL = f"{aws_s3_domain}/media/"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",  # type: ignore  # noqa: PGH003
)

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic", *INSTALLED_APPS]


# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": [
        "debug_toolbar.panels.redirects.RedirectsPanel",
        # Disable profiling panel due to an issue with Python 3.12:
        # https://github.com/jazzband/django-debug-toolbar/issues/1875
        "debug_toolbar.panels.profiling.ProfilingPanel",
    ],
    "SHOW_TEMPLATE_CONTEXT": True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
if env("USE_DOCKER") == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
    try:
        _, _, ips = socket.gethostbyname_ex("node")
        INTERNAL_IPS.extend(ips)
    except socket.gaierror:
        # The node container isn't started (yet?)
        pass
    # RunServerPlus
    # ------------------------------------------------------------------------------
    # This is a custom setting for RunServerPlus to fix reloader issue in Windows docker environment
    # Werkzeug reloader type [auto, watchdog, or stat]
    RUNSERVERPLUS_POLLER_RELOADER_TYPE = "stat"
    # If you have CPU and IO load issues, you can increase this poller interval e.g) 5
    RUNSERVERPLUS_POLLER_RELOADER_INTERVAL = 1

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]
# Celery
# ------------------------------------------------------------------------------

# https://docs.celeryq.dev/en/stable/userguide/configuration.html#task-eager-propagates
CELERY_TASK_EAGER_PROPAGATES = True
# django-webpack-loader
# ------------------------------------------------------------------------------
WEBPACK_LOADER["DEFAULT"]["CACHE"] = not DEBUG
# Your stuff...
# ------------------------------------------------------------------------------
# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASE_ENGINE = env(
    "POSTGRES_ENGINE",
    default="django.db.backends.sqlite3",  # type: ignore  # noqa: PGH003
)
DATABASE_HOST = env(
    "POSTGRES_HOST",
    default="",  # type: ignore  # noqa: PGH003
)
DATABASE_PORT = env(
    "POSTGRES_PORT",
    default="",  # type: ignore  # noqa: PGH003
)
DATABASE_DB = env(
    "POSTGRES_DB",
    default="",  # type: ignore  # noqa: PGH003
)
DATABASE_USER = env(
    "POSTGRES_USER",
    default="",  # type: ignore  # noqa: PGH003
)
DATABASE_PASSWORD = env(
    "POSTGRES_PASSWORD",
    default="",  # type: ignore  # noqa: PGH003
)
if DATABASE_ENGINE == "django.db.backends.postgresql":
    DATABASES = {
        "default": {
            "ENGINE": DATABASE_ENGINE,
            "NAME": DATABASE_DB,
            "USER": DATABASE_USER,
            "PASSWORD": DATABASE_PASSWORD,
            "HOST": DATABASE_HOST,
            "PORT": DATABASE_PORT,
        },
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": DATABASE_ENGINE,
            "NAME": BASE_DIR / "api.sqlite3",
            "USER": "",
            "PASSWORD": "",
            "HOST": "",
            "PORT": "",
        },
    }
# DATABASES = {"default": env.db("DATABASE_URL")}  # noqa: ERA001
DATABASES["default"]["ATOMIC_REQUESTS"] = True
