from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser

from api.libary.models import Chapter
from api.libary.pagination import StandardResultsSetPagination
from api.libary.serializers import ChapterInfoSerializer
from api.libary.serializers import ChaptersInfoSerializer


class ChapterListAPIView(generics.ListCreateAPIView):
    queryset = (
        Chapter.objects.prefetch_related(
            "chapterimages",
        )
        .select_related("comic", "website")
        .all()
    )
    serializer_class = ChaptersInfoSerializer
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


chapter_list = ChapterListAPIView.as_view()


class ChapterDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = (
        Chapter.objects.prefetch_related(
            "chapterimages",
        )
        .select_related("comic", "website")
        .all()
    )
    serializer_class = ChapterInfoSerializer
    lookup_url_kwarg = "slug"
    lookup_field = "slug"

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


chapter_detail = ChapterDetailAPIView.as_view()
