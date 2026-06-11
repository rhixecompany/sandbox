"""Configures Django app config for the scraping module."""
from __future__ import annotations

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ScrapingConfig(AppConfig):
    name = "apps.scraping"
    verbose_name = _("Scraping")

    def ready(self):
        """Register Celery tasks if applicable."""
        try:
            from . import tasks  # noqa: F401
        except ImportError:
            pass
