"""API URL configuration — routes for all comic resources."""
from __future__ import annotations

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.comics.views import (
    ArtistViewSet,
    AuthorViewSet,
    ChapterViewSet,
    ComicViewSet,
    CommentViewSet,
    GenreViewSet,
    TypeViewSet,
    UserItemViewSet,
)

router = DefaultRouter()
router.register(r"comics", ComicViewSet, basename="comic")
router.register(r"chapters", ChapterViewSet, basename="chapter")
router.register(r"genres", GenreViewSet, basename="genre")
router.register(r"authors", AuthorViewSet, basename="author")
router.register(r"artists", ArtistViewSet, basename="artist")
router.register(r"types", TypeViewSet, basename="type")
router.register(r"comments", CommentViewSet, basename="comment")
router.register(r"bookmarks", UserItemViewSet, basename="bookmark")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("apps.users.urls")),
]
