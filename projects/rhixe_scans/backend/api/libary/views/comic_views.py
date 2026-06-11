from datetime import timedelta

from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.timezone import now
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from api.libary.constants import ComicStatus
from api.libary.models import Comic
from api.libary.models import ComicImage
from api.libary.serializers import ComicInfoSerializer
from api.libary.serializers import ComicSerializer
from api.libary.serializers import ComicsInfoSerializer


@api_view(["GET"])
def getcomics(request):
    genre = request.query_params.get("genresearch")
    title = request.query_params.get("titlesearch")
    titlequery = title if title is not None else ""

    genrequery = genre if genre is not None else ""
    if genrequery:
        comics = (
            Comic.objects.prefetch_related(
                "comicimages",
                "genres",
                "users",
                "comicchapters",
            )
            .select_related("user", "author", "category", "artist", "website")
            .filter(Q(genres__name__icontains=genrequery))
            .distinct()
            .order_by("-updated_at")
        )
    if titlequery:
        comics = (
            Comic.objects.prefetch_related(
                "comicimages",
                "genres",
                "users",
                "comicchapters",
            )
            .select_related("user", "author", "category", "artist", "website")
            .filter(Q(title__icontains=titlequery))
            .distinct()
            .order_by("-updated_at")
        )
    if not titlequery and not genrequery:
        comics = (
            Comic.objects.prefetch_related(
                "comicimages",
                "genres",
                "users",
                "comicchapters",
            )
            .select_related("user", "author", "category", "artist", "website")
            .all()
            .order_by("-updated_at")
        )

    page = request.query_params.get("page")
    if page is None:
        page = 1
    if page is None:
        page = 1

    newpage = int(page)
    paginator = Paginator(comics, 300)

    try:
        comics = paginator.page(newpage)
    except PageNotAnInteger:
        comics = paginator.page(1)
    except EmptyPage:
        comics = paginator.page(paginator.num_pages)

    serializer = ComicsInfoSerializer(comics, many=True)

    return Response(
        {
            "total_results": paginator.count,
            "total_pages": paginator.num_pages,
            "results": serializer.data,
        },
    )


@api_view(["GET"])
def gettopcomics(request):
    comics = (
        Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .filter(Q(status=ComicStatus.ONGOING) & Q(rating__gte=9.9))[0:13]
    )
    serializer = ComicsInfoSerializer(comics, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getfeaturedcomics(request):
    comics = (
        Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .filter(
            Q(status=ComicStatus.ONGOING),
        )
        .order_by(
            "-rating",
        )[0:5]
    )
    serializer = ComicsInfoSerializer(comics, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getselectcomics(request):
    week = now() - timedelta(days=31)
    month = now() - timedelta(days=62)
    comics = (
        Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .filter(
            Q(rating__gte=9.7) & Q(status=ComicStatus.ONGOING),
        )
        .order_by(
            "-rating",
        )[0:10]
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
            Q(rating__gte=9.7)
            & Q(status=ComicStatus.ONGOING)
            & Q(updated_at__gte=week),
        )
        .order_by(
            "-rating",
        )[0:10]
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
            Q(rating__gte=9.7)
            & Q(status=ComicStatus.ONGOING)
            & Q(updated_at__gte=month),
        )
        .order_by(
            "-rating",
        )[0:10]
    )
    allserializer = ComicsInfoSerializer(comics, many=True)
    weeklyserializer = ComicsInfoSerializer(weekcomics, many=True)
    monthlyserializer = ComicsInfoSerializer(monthcomics, many=True)

    return Response(
        {
            "weeklycomics": weeklyserializer.data,
            "monthlycomics": monthlyserializer.data,
            "allcomics": allserializer.data,
        },
    )


@api_view(["GET"])
def getcomic(request, slug):
    comic = Comic.objects.get(slug=slug)
    serializer = ComicInfoSerializer(comic, many=False)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([AllowAny])
def createcomic(request):

    serializer = ComicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([AllowAny])
def updatecomic(request, slug):
    try:
        comic = (
            Comic.objects.prefetch_related(
                "comicimages",
                "genres",
                "users",
                "comicchapters",
            )
            .select_related("user", "author", "category", "artist", "website")
            .get(slug=slug)
        )
    except Comic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ComicSerializer(comic, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deletecomic(request, slug):
    try:
        comic = (
            Comic.objects.prefetch_related(
                "comicimages",
                "genres",
                "users",
                "comicchapters",
            )
            .select_related("user", "author", "category", "artist", "website")
            .get(slug=slug)
        )
        comic.delete()
        return Response("Comic Deleted", status=status.HTTP_200_OK)
    except Comic.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def uploadimage(request):
    data = request.data

    comic_slug = data["comic_slug"]
    comic = (
        Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .get(slug=comic_slug)
    )
    ComicImage.objects.get_or_create(
        link=request.POST.get("link"),
        image=request.FILES.get("image"),
        status=request.POST.get("status"),
        checksum=request.POST.get("checksum"),
        comic=comic,
    )[0]

    return Response("Image was uploaded")
