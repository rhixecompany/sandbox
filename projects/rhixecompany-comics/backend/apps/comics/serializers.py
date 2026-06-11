"""DRF serializers for comic models."""
from __future__ import annotations

from rest_framework import serializers

from apps.comics.models import (
    Artist,
    Author,
    Chapter,
    ChapterImage,
    Comic,
    ComicImage,
    Comment,
    Genre,
    Type,
    UserItem,
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "name"]


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ["id", "name"]


class ComicImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComicImage
        fields = ["id", "url", "image", "comic"]


class ChapterImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapterImage
        fields = ["id", "url", "image", "chapter", "comic"]


class ChapterSerializer(serializers.ModelSerializer):
    comic_title = serializers.CharField(source="comic.title", read_only=True)
    chapter_images = ChapterImageSerializer(source="chapteritems", many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = [
            "id", "uuid", "name", "title", "slug", "spider", "url",
            "updated_at", "timestamp", "numpages", "comic", "comic_title",
            "chapter_images",
        ]


class ChapterListSerializer(serializers.ModelSerializer):
    """Compact serializer for list views."""
    class Meta:
        model = Chapter
        fields = ["id", "name", "slug", "numpages", "updated_at", "comic"]


class ComicSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)
    artist = ArtistSerializer(read_only=True)
    type = TypeSerializer(read_only=True)
    chapters = ChapterListSerializer(source="comicchapters", many=True, read_only=True)
    images = ComicImageSerializer(source="comicitems", many=True, read_only=True)

    class Meta:
        model = Comic
        fields = [
            "id", "uuid", "title", "slug", "description", "status",
            "rating", "serialization", "numchapters", "spider", "url",
            "numitems", "timestamp", "updated_at", "type", "genres",
            "author", "artist", "chapters", "images",
        ]


class ComicListSerializer(serializers.ModelSerializer):
    """Compact serializer for list views."""
    type_name = serializers.CharField(source="type.name", read_only=True, allow_null=True)
    author_name = serializers.CharField(source="author.name", read_only=True, allow_null=True)
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Comic
        fields = [
            "id", "title", "slug", "status", "rating",
            "numchapters", "updated_at", "type_name", "author_name", "thumbnail",
        ]

    def get_thumbnail(self, obj):
        first_image = obj.comicitems.first()
        if first_image:
            return first_image.image.url if first_image.image else first_image.url
        return None


class CommentSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "text", "chapter", "comic", "user", "user_email", "timestamp", "updated"]
        read_only_fields = ["user", "timestamp", "updated"]


class UserItemSerializer(serializers.ModelSerializer):
    comic_detail = ComicListSerializer(source="comic", read_only=True)

    class Meta:
        model = UserItem
        fields = ["id", "user", "comic", "comic_detail", "order"]
