from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser

from api.libary.models import Genre
from api.libary.serializers import GenreSerializer


class GenreListAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.prefetch_related(
        "genrecomics",
    ).all()
    serializer_class = GenreSerializer
    filter_backends = [
        DjangoFilterBackend,  # type: ignore  # noqa: PGH003
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    def get_queryset(self):
        return super().get_queryset()

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


genre_list = GenreListAPIView.as_view()


class GenreDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.prefetch_related(
        "genrecomics",
    ).all()
    serializer_class = GenreSerializer
    lookup_url_kwarg = "id"

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


genre_detail = GenreDetailAPIView.as_view()
