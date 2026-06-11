from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from api.libary.constants import ComicStatus
from api.libary.filters import SearchFilterSet
from api.libary.models import Comic
from api.libary.models import UserComic


def index(request):
    qs = (
        Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .all()
    )
    paginator = Paginator(qs, 20)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    page_obj = paginator.get_page(page_number)
    context = {
        "objects": page_obj,
        "topcomics": Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .filter(
            Q(status=ComicStatus.ONGOING) & Q(rating__gte=9.8),
        )[0:13],
        "featuredcomics": Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .filter(
            Q(status=ComicStatus.ONGOING),
        )[0:5],
    }
    return render(request, "home/index.html", context)


def series(request):
    f = SearchFilterSet(
        request.GET,
        queryset=Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .all(),
    )
    paginator = Paginator(f.qs, 20)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    page_obj = paginator.get_page(page_number)
    context = {
        "objects": page_obj,
    }
    return render(request, "home/series.html", context)


def bookmarks(request):
    qs = UserComic.objects.all()
    paginator = Paginator(qs, 20)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    page_obj = paginator.get_page(page_number)
    context = {
        "objects": page_obj,
    }
    return render(request, "home/bookmarks.html", context)


def privacy(request):
    context = {}
    return render(request, "home/privacy.html", context)


def dmca(request):
    context = {}
    return render(request, "home/dmca.html", context)


def terms(request):
    context = {}
    return render(request, "home/terms.html", context)
