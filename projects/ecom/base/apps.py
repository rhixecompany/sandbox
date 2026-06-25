<<<<<<< HEAD
from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'base'

    def ready(self):
        import base.signals
=======
from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'base'

    def ready(self):
        import base.signals
>>>>>>> d330f24 (chore: initial local project setup for ecom)
