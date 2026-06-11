from datetime import timedelta

from django.db.models import Q
from django.utils.timezone import now

from api.libary.constants import ComicStatus
from api.libary.filters import SearchFilterSet
from api.libary.models import Comic


def load(request):
    week = now() - timedelta(weeks=1)
    month = now() - timedelta(weeks=4)
    comics = (
        Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .filter(
            Q(rating__gte=9.5) & Q(status=ComicStatus.ONGOING),
        )
    )
    weekcomics = (
        Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .filter(
            Q(rating__gte=9.5) & Q(updated_at__gte=week),
        )
    )
    monthcomics = (
        Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .filter(
            Q(rating__gte=9.5) & Q(updated_at__gt=month),
        )
    )
    myfilter = SearchFilterSet()

    return {
        "monthlycomics": monthcomics[0:10],
        "weeklycomics": weekcomics[0:10],
        "allcomics": comics[0:10],
        "myfilter": myfilter,
    }
