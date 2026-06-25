<<<<<<< HEAD
from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'base'
    
    def ready(self):
=======
from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'base'
    
    def ready(self):
>>>>>>> 4ae124d (chore: initial local project setup for profile)
    	import base.signals