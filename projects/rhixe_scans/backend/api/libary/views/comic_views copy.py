from datetime import timedelta

from django.db.models import Q
from django.utils.timezone import now
from rest_framework import filters
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.libary.constants import ComicStatus
from api.libary.models import Comic
from api.libary.pagination import StandardResultsSetPagination
from api.libary.serializers import ComicInfoSerializer
from api.libary.serializers import ComicsInfoSerializer


class ComicListAPIView(generics.ListCreateAPIView):
    queryset = (
        Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .all()
    )
    serializer_class = ComicsInfoSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        "title",
        "=category__name",
        "=author__name",
        "=artist__name",
        "=genres__name",
    ]
    ordering_fields = ["title", "rating", "status", "updated_at"]
    ordering = ["-updated_at"]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return super().get_queryset()

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


comic_list = ComicListAPIView.as_view()


class ComicDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = (
        Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .all()
    )
    serializer_class = ComicInfoSerializer
    lookup_url_kwarg = "slug"
    lookup_field = "slug"

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


comic_detail = ComicDetailAPIView.as_view()


@api_view(["GET"])
def topcomics(request):
    queryset = (
        Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .filter(
            Q(status=ComicStatus.ONGOING) & Q(rating__gte=9.8),
        )[0:13]
    )
    serializer = ComicsInfoSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def featuredcomics(request):
    queryset = (
        Comic.objects.prefetch_related(
            "comicimages",
            "genres",
            "users",
            "comicchapters",
        )
        .select_related("user", "author", "category", "artist", "website")
        .filter(
            Q(status=ComicStatus.ONGOING),
        )[0:5]
    )
    serializer = ComicsInfoSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def selectedcomics(request):
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
            Q(rating__gte=9.5) & Q(updated_at__gte=week),
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
            Q(rating__gte=9.5) & Q(updated_at__gt=month),
        )[0:10]
    )
    allserializer = ComicsInfoSerializer(comics, many=True)
    weeklyserializer = ComicsInfoSerializer(weekcomics, many=True)
    monthlyserializer = ComicsInfoSerializer(monthcomics, many=True)

    return Response(
        {
            "monthlycomics": monthlyserializer.data,
            "weeklycomics": weeklyserializer.data,
            "allcomics": allserializer.data,
        },
    )
