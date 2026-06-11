from __future__ import annotations

from django.urls import path

from .views import health

urlpatterns = [path('health/', health, name='health')]
