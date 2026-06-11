"""Admin configuration for comics models."""
from __future__ import annotations

from django.contrib import admin

from apps.comics.models import (
    Artist,
    Author,
    Chapter,
    ChapterImage,
    Comic,
    ComicImage,
    Comment,
    Genre,
    Type,
    UserItem,
)


class ComicImageInline(admin.TabularInline):
    model = ComicImage
    extra = 1


class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1


class ChapterImageInline(admin.TabularInline):
    model = ChapterImage
    extra = 1


@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "type", "author", "rating", "numchapters", "updated_at"]
    list_filter = ["status", "type", "genres"]
    search_fields = ["title", "author__name", "artist__name"]
    prepopulated_fields = {"slug": ["title"]}
    inlines = [ComicImageInline, ChapterInline]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ["name", "comic", "numpages", "updated_at"]
    list_filter = ["comic"]
    search_fields = ["name", "comic__title"]
    prepopulated_fields = {"slug": ["name"]}
    inlines = [ChapterImageInline]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["user", "comic", "chapter", "timestamp"]
    list_filter = ["timestamp"]


@admin.register(UserItem)
class UserItemAdmin(admin.ModelAdmin):
    list_display = ["user", "comic", "order"]


@admin.register(ComicImage)
class ComicImageAdmin(admin.ModelAdmin):
    list_display = ["comic", "url"]


@admin.register(ChapterImage)
class ChapterImageAdmin(admin.ModelAdmin):
    list_display = ["chapter", "comic", "url"]
