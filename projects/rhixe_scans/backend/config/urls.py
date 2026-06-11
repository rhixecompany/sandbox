from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views import defaults as default_views
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    # Your stuff: custom urls includes go here
    # ...
]

# API URLS
urlpatterns += [
    # API base url
    path("api/users/", include("libary.urls.user_urls", namespace="users")),
    path("api/comics/", include("libary.urls.comic_urls", namespace="comics")),
    path("api/chapters/", include("libary.urls.chapter_urls", namespace="chapters")),
    path(
        "api/comicimages/",
        include("libary.urls.comic_image_urls", namespace="comicimages"),
    ),
    path(
        "api/chapterimages/",
        include("libary.urls.chapter_image_urls", namespace="chapterimages"),
    ),
    path(
        "api/genres/",
        include("libary.urls.genre_urls", namespace="genres"),
    ),
    path(
        "api/categorys/",
        include("libary.urls.category_urls", namespace="categorys"),
    ),
    path(
        "api/artists/",
        include("libary.urls.artist_urls", namespace="artists"),
    ),
    path(
        "api/authors/",
        include("libary.urls.author_urls", namespace="authors"),
    ),
    # DRF auth token
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/auth/", include("rest_framework.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
            *urlpatterns,
        ]
