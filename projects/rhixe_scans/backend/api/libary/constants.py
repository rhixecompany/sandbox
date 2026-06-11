from django.db import models


class ComicStatus(models.TextChoices):
    COMPLETED = "completed", "Completed"
    ONGOING = "ongoing", "Ongoing"
    HIATUS = "hiatus", "Hiatus"
    DROPPED = "dropped", "Dropped"
    SEASON_END = "season end", "Season End"
    COMING_SOON = "coming soon", "Coming Soon"


class ImageStatus(models.TextChoices):
    DOWNLOADED = "downloaded"
    UPTODATE = "uptodate"
    CACHED = "cached"
