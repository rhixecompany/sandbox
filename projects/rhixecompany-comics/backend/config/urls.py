"""URL configuration for the rhixecompany-comics backend."""
from __future__ import annotations

from django.contrib import admin
from django.urls import include, path

from apps.core.views import health

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.core.urls')),
    path('api/', include('apps.api.urls')),
    path('api/healthz/', health, name='healthz-alias'),
]
