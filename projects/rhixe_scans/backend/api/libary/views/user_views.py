from django.contrib.auth.hashers import make_password
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from api.libary.pagination import StandardResultsSetPagination
from api.users.models import User
from api.users.serializers import MyTokenObtainPairSerializer
from api.users.serializers import UserSerializer


class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.prefetch_related(
        "usercomics",
        "usercomments",
    ).all()
    serializer_class = UserSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = [
        "email",
        "username",
    ]
    ordering_fields = ["email", "username"]
    ordering = ["-id"]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return super().get_queryset()

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == "POST":
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


user_list = UserListAPIView.as_view()


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.prefetch_related(
        "usercomics",
        "usercomments",
    ).all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "id"

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()


user_detail = UserDetailAPIView.as_view()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


user_obtain_token = MyTokenObtainPairView.as_view()


@api_view(["POST"])
def registeruser(request):
    data = request.data
    try:
        user = User.objects.create(
            username=data["username"],
            email=data["email"],
            password=make_password(data["password"]),
        )

        serializer = MyTokenObtainPairSerializer(user, many=False)
        return Response(serializer.data)
    except:  # noqa: E722
        message = {"detail": "User with this email already exists"}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
