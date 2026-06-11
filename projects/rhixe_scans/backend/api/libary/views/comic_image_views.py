from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser

from api.libary.models import ComicImage
from api.libary.pagination import StandardResultsSetPagination
from api.libary.serializers import ComicImageSerializer


class ComicImageListAPIView(generics.ListCreateAPIView):
    queryset = ComicImage.objects.select_related(
        "comic",
    ).all()
    serializer_class = ComicImageSerializer
    filter_backends = [
        DjangoFilterBackend,  # type: ignore  # noqa: PGH003
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return super().get_queryset()

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


comic_image_list = ComicImageListAPIView.as_view()


class ComicImageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ComicImage.objects.select_related(
        "comic",
    ).all()
    serializer_class = ComicImageSerializer
    lookup_url_kwarg = "id"

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


comic_image_detail = ComicImageDetailAPIView.as_view()
