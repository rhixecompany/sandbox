from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser

from api.libary.models import Category
from api.libary.pagination import StandardResultsSetPagination
from api.libary.serializers import CategorySerializer


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.prefetch_related(
        "categorycomics",
    ).all()
    serializer_class = CategorySerializer
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


category_list = CategoryListAPIView.as_view()


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.prefetch_related(
        "categorycomics",
    ).all()
    serializer_class = CategorySerializer
    lookup_url_kwarg = "id"

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


category_detail = CategoryDetailAPIView.as_view()
