import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LibaryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api.libary"
    verbose_name = _("Libary")

    def ready(self):
        with contextlib.suppress(ImportError):
            import api.users.signals  # noqa: F401
