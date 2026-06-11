from datetime import timedelta

from django.db.models import Q
from django.http import HttpRequest
from django.utils.timezone import now

from api.apps.filters import SearchFilter
from api.apps.models import Comic


def load(request: HttpRequest) -> dict[str, str]:
    mdate = now() - timedelta(weeks=8)
    wdate = now() - timedelta(weeks=4)
    ydate = now() - timedelta(weeks=48)
    mon = (
        Comic.objects.get_feat()
        .prefetch_related(
            "comicitems",
            "genres",
            "followers",
            "comicchapters",
        )
        .select_related("user", "author", "type", "artist")
        .filter(Q(updated_at__gte=mdate))
    )
    week = (
        Comic.objects.get_feat()
        .prefetch_related(
            "comicitems",
            "genres",
            "followers",
            "comicchapters",
        )
        .select_related("user", "author", "type", "artist")
        .filter(Q(updated_at__gte=wdate))
    )
    allc = (
        Comic.objects.get_feat()
        .prefetch_related(
            "comicitems",
            "genres",
            "followers",
            "comicchapters",
        )
        .select_related("user", "author", "type", "artist")
        .filter(Q(updated_at__gte=ydate))
    )

    return {
        "moncomics": mon[0:10],
        "weeklycomics": week[0:10],
        "allcomics": allc[0:10],
        "myfilter": SearchFilter(),
    }
