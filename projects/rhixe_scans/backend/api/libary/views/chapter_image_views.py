from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser

from api.libary.models import ChapterImage
from api.libary.pagination import StandardResultsSetPagination
from api.libary.serializers import ChapterImageSerializer


class ChapterImageListAPIView(generics.ListCreateAPIView):
    queryset = ChapterImage.objects.select_related(
        "chapter",
        "comic",
    ).all()
    serializer_class = ChapterImageSerializer
    filter_backends = [
        DjangoFilterBackend,  # type: ignore  # noqa: PGH003
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    # pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return super().get_queryset()

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


chapter_image_list = ChapterImageListAPIView.as_view()


class ChapterImageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChapterImage.objects.select_related(
        "chapter",
        "comic",
    ).all()
    serializer_class = ChapterImageSerializer
    lookup_url_kwarg = "id"

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


chapter_image_detail = ChapterImageDetailAPIView.as_view()
