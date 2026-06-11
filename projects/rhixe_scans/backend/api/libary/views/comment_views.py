from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser

from api.libary.models import Comment
from api.libary.pagination import StandardResultsSetPagination
from api.libary.serializers import CommentSerializer


class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
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


comment_list = CommentListAPIView.as_view()


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_url_kwarg = "id"

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


comment_detail = CommentDetailAPIView.as_view()
