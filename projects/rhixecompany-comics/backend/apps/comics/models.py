"""Comic, chapter, bookmark, and related models for the comics platform."""
from __future__ import annotations

import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ComicStatus(models.TextChoices):
    COMPLETED = "Completed"
    ONGOING = "Ongoing"
    HIATUS = "Hiatus"
    DROPPED = "Dropped"
    SEASON_END = "Season End"
    COMING_SOON = "Coming Soon"


class TypeStatus(models.TextChoices):
    MANGA = "Manga"
    MANHWA = "Manhwa"
    MANHUA = "Manhua"


class Genre(models.Model):
    name = models.CharField(_("Name"), max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(_("Name"), max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(_("Name"), max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(_("Name"), max_length=6, choices=TypeStatus.choices)

    class Meta:
        verbose_name_plural = "Types"

    def __str__(self):
        return self.name


class Comic(models.Model):
    uuid = models.UUIDField(_("Uuid"), default=uuid.uuid4, editable=False)
    title = models.CharField(_("Title"), max_length=5000, unique=True)
    slug = models.SlugField(_("Slug"), max_length=5000, unique=True, blank=True, null=True)
    description = models.TextField(_("Description"), blank=True)
    status = models.CharField(_("Status"), max_length=15, choices=ComicStatus.choices)
    rating = models.DecimalField(_("Rating"), max_digits=10, decimal_places=1, default=0)
    serialization = models.CharField(_("Serialization"), max_length=5000, blank=True)
    numchapters = models.PositiveIntegerField(_("Total Chapters"), blank=True, default=0)
    spider = models.CharField(_("Spider"), max_length=500, blank=True)
    url = models.URLField(_("Url"), max_length=500, blank=True)
    numitems = models.PositiveSmallIntegerField(_("Total Items"), blank=True, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, blank=True, related_name="comictype")
    genres = models.ManyToManyField(Genre, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name="comicauthor")
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, blank=True, related_name="comicartist")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="comicuser")
    users = models.ManyToManyField(User, through="UserItem", blank=True)

    class Meta:
        verbose_name_plural = "Comics"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("api:comic-detail", kwargs={"slug": self.slug})


class ComicImage(models.Model):
    url = models.URLField(_("Url"), max_length=5000)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name="comicitems")
    image = models.ImageField(_("Image"), upload_to="comics/", max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.url


class UserItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name="followers")
    order = models.PositiveSmallIntegerField(_("Order"))

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "UserItems"

    def __str__(self):
        return f"Order {self.order} — {self.user.email} — {self.comic.title}"


class Chapter(models.Model):
    uuid = models.UUIDField(_("Uuid"), default=uuid.uuid4, editable=False)
    name = models.CharField(_("Name"), max_length=500)
    title = models.CharField(_("Title"), max_length=5000, blank=True)
    slug = models.SlugField(_("Slug"), max_length=5000, unique=True, blank=True, null=True)
    spider = models.CharField(_("Spider"), max_length=500, blank=True)
    url = models.URLField(_("Url"), max_length=500, blank=True)
    updated_at = models.DateField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    numpages = models.PositiveSmallIntegerField(_("Total Pages"), blank=True, default=0)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name="comicchapters")

    class Meta:
        verbose_name_plural = "Chapters"
        ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.comic.title} — {self.name}"

    def get_absolute_url(self):
        return reverse("api:chapter-detail", kwargs={"slug": self.slug})


class ChapterImage(models.Model):
    url = models.URLField(_("Url"), max_length=5000)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="chapteritems")
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    image = models.ImageField(_("Image"), upload_to="chapters/", max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.url


class Comment(models.Model):
    text = models.TextField(_("Text"))
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="chaptercomments")
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name="comiccomments", blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usercomments")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Comments"
        ordering = ["-updated"]

    def __str__(self):
        return f"Comment by {self.user.email} on {self.comic.title}"
