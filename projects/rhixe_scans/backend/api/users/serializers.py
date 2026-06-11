from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from api.users.models import User


class UserSerializer(serializers.ModelSerializer[User]):
    image = serializers.ImageField(use_url=True)

    is_admin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "full_name",
            "image",
            "is_admin",
        ]

    def get_is_admin(self, obj):
        return obj.is_superuser


class UserSerializerWithToken(UserSerializer):
    refreshedtoken = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "full_name",
            "image",
            "is_admin",
            "refreshedtoken",
        ]

    def get_refreshedtoken(self, obj):
        refreshedtoken = RefreshToken.for_user(obj)
        return str(refreshedtoken.access_token)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = UserSerializerWithToken(self.user).data  # type: ignore  # noqa: PGH003
        for k, v in serializer.items():
            data[k] = v

        return data
