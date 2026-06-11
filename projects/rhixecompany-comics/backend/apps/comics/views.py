"""DRF viewsets for comic models."""
from __future__ import annotations

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination

from apps.comics.models import (
    Artist,
    Author,
    Chapter,
    Comic,
    Comment,
    Genre,
    Type,
    UserItem,
)
from apps.comics.serializers import (
    ArtistSerializer,
    AuthorSerializer,
    ChapterListSerializer,
    ChapterSerializer,
    ComicListSerializer,
    ComicSerializer,
    CommentSerializer,
    GenreSerializer,
    TypeSerializer,
    UserItemSerializer,
)


class StandardPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all().order_by("name")
    serializer_class = GenreSerializer
    pagination_class = StandardPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by("name")
    serializer_class = AuthorSerializer
    pagination_class = StandardPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all().order_by("name")
    serializer_class = ArtistSerializer
    pagination_class = StandardPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    pagination_class = StandardPagination


class ComicViewSet(viewsets.ModelViewSet):
    queryset = Comic.objects.prefetch_related(
        "genres", "comicitems", "comicchapters", "followers",
    ).select_related("author", "artist", "type", "user").all()
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status", "type__name", "genres__name"]
    search_fields = ["title", "description", "author__name", "artist__name"]
    ordering_fields = ["updated_at", "rating", "title", "numchapters"]
    ordering = ["-updated_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return ComicListSerializer
        return ComicSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        status = self.request.query_params.get("status")
        if status:
            qs = qs.filter(status__iexact=status)
        return qs


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.prefetch_related("chapteritems").select_related("comic").all()
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["comic"]
    search_fields = ["name", "title", "comic__title"]
    ordering_fields = ["updated_at", "name"]
    ordering = ["-updated_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return ChapterListSerializer
        return ChapterSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        comic_slug = self.request.query_params.get("comic_slug")
        if comic_slug:
            qs = qs.filter(comic__slug=comic_slug)
        return qs


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("user", "comic", "chapter").all()
    serializer_class = CommentSerializer
    pagination_class = StandardPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["comic", "chapter", "user"]
    ordering = ["-updated"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserItemViewSet(viewsets.ModelViewSet):
    queryset = UserItem.objects.prefetch_related("comic").all()
    serializer_class = UserItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user", "comic"]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            return qs.filter(user=self.request.user)
        return qs.none()
