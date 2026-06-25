from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class MoviesReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesReview
        fields = '__all__'


class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = '__all__'


class SeriesReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesReview
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        field = ['_id', 'name', 'image', 'createdAt',  'season']


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        field = ['id', 'num', 'file', 'series_episode', 'series_season']


class SeriesSerializer(serializers.ModelSerializer):
    episodes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Series
        fields = ['_id', 'name', 'actors', 'category', 'description',
                  'image', 'createdAt', 'rating', 'likes',  'episodes']
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class MoviesReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesReview
        fields = '__all__'


class MoviesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = '__all__'


class SeriesReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeriesReview
        fields = '__all__'


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        field = ['_id', 'name', 'image', 'createdAt',  'season']


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        field = ['id', 'num', 'file', 'series_episode', 'series_season']


class SeriesSerializer(serializers.ModelSerializer):
    episodes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Series
        fields = ['_id', 'name', 'actors', 'category', 'description',
                  'image', 'createdAt', 'rating', 'likes',  'episodes']
