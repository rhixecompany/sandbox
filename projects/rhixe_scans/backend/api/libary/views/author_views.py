from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser

from api.libary.models import Author
from api.libary.pagination import StandardResultsSetPagination
from api.libary.serializers import AuthorSerializer


class AuthorListAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.prefetch_related(
        "authorcomics",
    ).all()
    serializer_class = AuthorSerializer
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


author_list = AuthorListAPIView.as_view()


class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.prefetch_related(
        "authorcomics",
    ).all()
    serializer_class = AuthorSerializer
    lookup_url_kwarg = "id"

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


author_detail = AuthorDetailAPIView.as_view()
