from django.db.models import Q
from rest_framework import serializers

from api.libary.models import Artist
from api.libary.models import Author
from api.libary.models import Category
from api.libary.models import Chapter
from api.libary.models import ChapterImage
from api.libary.models import Comic
from api.libary.models import ComicImage
from api.libary.models import Comment
from api.libary.models import Genre
from api.libary.models import UserComic
from api.libary.models import Website
from api.users.serializers import UserSerializer


class ArtistSerializer(serializers.ModelSerializer[Artist]):

    class Meta:
        model = Artist
        fields = [
            "name",
            # "id",
        ]


class AuthorSerializer(serializers.ModelSerializer[Author]):

    class Meta:
        model = Author
        fields = [
            "name",
            # "id",
        ]


class CategorySerializer(serializers.ModelSerializer[Category]):

    class Meta:
        model = Category
        fields = [
            "name",
            # "id",
        ]


class WebsiteSerializer(serializers.ModelSerializer[Website]):

    class Meta:
        model = Website
        fields = [
            "name",
            # "id",
        ]


class GenreSerializer(serializers.ModelSerializer[Genre]):

    class Meta:
        model = Genre
        fields = [
            "name",
            # "id",
        ]


class ComicSerializer(serializers.ModelSerializer[Comic]):
    updated_at = serializers.DateTimeField()
    rating = serializers.FloatField()

    class Meta:
        model = Comic
        fields = [
            # "id",
            "title",
            "slug",
            "description",
            "rating",
            "numchapters",
            "numimages",
            "updated_at",
            "serialization",
            "status",
            "link",
        ]


class ChapterSerializer(serializers.ModelSerializer[Chapter]):
    updated_at = serializers.DateTimeField()
    # updated_at = serializers.DateField(format="%d %B, %Y")
    comic = ComicSerializer(read_only=False, required=True)

    class Meta:
        model = Chapter
        fields = [
            "name",
            "title",
            "slug",
            "link",
            "numimages",
            "updated_at",
            "comic",
        ]


class UserComicSerializer(serializers.ModelSerializer[UserComic]):
    user = UserSerializer(read_only=True)
    comic = ComicSerializer(read_only=True)

    class Meta:
        model = UserComic
        fields = [
            "user",
            "comic",
        ]


class ComicImageSerializer(serializers.ModelSerializer[ComicImage]):
    image = serializers.ImageField(use_url=True)
    # comic = ComicSerializer(read_only=True)
    comic = serializers.CharField(source="comic.slug")

    class Meta:
        model = ComicImage
        fields = [
            # "id",
            "link",
            "image",
            "status",
            "checksum",
            "comic",
        ]


class ChapterImageSerializer(serializers.ModelSerializer[ChapterImage]):
    image = serializers.ImageField(use_url=True)
    comic = serializers.CharField(source="comic.slug")
    chapter = serializers.CharField(source="chapter.slug")
    # comic = ComicSerializer(read_only=True)
    # chapter = ChapterSerializer(read_only=True)

    class Meta:
        model = ChapterImage
        fields = [
            # "id",
            "link",
            "image",
            "status",
            "checksum",
            "chapter",
            "comic",
        ]


class CommentSerializer(serializers.ModelSerializer[Comment]):
    comic = ComicSerializer(read_only=True)
    chapter = ChapterSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "text",
            "chapter",
            "comic",
            "user",
            # "id",
        ]


class ComicsInfoSerializer(ComicSerializer):
    # updated_at = serializers.DateField(format="%d/%B/%Y")

    # website = WebsiteSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    author = AuthorSerializer(read_only=True)
    artist = ArtistSerializer(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)

    # chapters = serializers.SerializerMethodField(read_only=True)  # noqa: ERA001
    # comments = serializers.SerializerMethodField(read_only=True)  # noqa: ERA001
    # users = serializers.SerializerMethodField(read_only=True)  # noqa: ERA001
    genres = serializers.SerializerMethodField(read_only=True)
    # first_chapter = serializers.SerializerMethodField(read_only=True)  # noqa: ERA001
    # last_chapter = serializers.SerializerMethodField(read_only=True)  # noqa: ERA001

    def get_genres(self, obj):
        items = obj.genres.all()
        serializer = GenreSerializer(items, many=True)
        return serializer.data

    def get_images(self, obj):
        items = obj.get_images()
        serializer = ComicImageSerializer(items, many=True)
        return serializer.data

    # def get_chapters(self, obj):
    #     items = obj.get_chapters()[0:3]  # noqa: ERA001
    #     serializer = ChapterSerializer(items, many=True)  # noqa: ERA001
    #     return serializer.data  # noqa: ERA001

    # def get_comments(self, obj):
    #     items = obj.get_comments()  # noqa: ERA001
    #     serializer = CommentSerializer(items, many=True)  # noqa: ERA001
    #     return serializer.data  # noqa: ERA001

    # def get_users(self, obj):
    #     items = obj.get_users()  # noqa: ERA001
    #     serializer = UserSerializer(items, many=True)  # noqa: ERA001
    #     return serializer.data  # noqa: ERA001

    # def get_first_chapter(self, obj):
    #     items = obj.get_chapters().last()  # noqa: ERA001
    #     serializer = ChapterSerializer(items, many=False)  # noqa: ERA001
    #     return serializer.data  # noqa: ERA001

    # def get_last_chapter(self, obj):
    #     items = obj.get_chapters().first()  # noqa: ERA001
    #     serializer = ChapterSerializer(items, many=False)  # noqa: ERA001
    #     return serializer.data  # noqa: ERA001

    class Meta:
        model = Comic
        fields = [
            # "id",
            "title",
            "slug",
            "description",
            "rating",
            "numchapters",
            "numimages",
            "updated_at",
            "serialization",
            "status",
            "link",
            # "user",
            "category",
            # "website",
            "has_images",
            "has_chapters",
            "author",
            "artist",
            "genres",
            "images",
            # "chapters",
            # "comments",
            # "users",
            # "first_chapter",
            # "last_chapter",
        ]


class ComicInfoSerializer(ComicSerializer):

    user = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    website = WebsiteSerializer(read_only=True)
    author = AuthorSerializer(read_only=True)
    artist = ArtistSerializer(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    related_series = serializers.SerializerMethodField(read_only=True)
    chapters = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)
    users = serializers.SerializerMethodField(read_only=True)
    genres = serializers.SerializerMethodField(read_only=True)
    first_chapter = serializers.SerializerMethodField(read_only=True)
    last_chapter = serializers.SerializerMethodField(read_only=True)

    def get_genres(self, obj):

        items = obj.genres.all()

        serializer = GenreSerializer(items, many=True)
        return serializer.data

    def get_images(self, obj):
        items = obj.get_images()
        serializer = ComicImageSerializer(items, many=True)
        return serializer.data

    def get_related_series(self, obj):

        if obj.category:
            category = obj.category.name
            items = (
                Comic.objects.prefetch_related(
                    "comicimages",
                    "genres",
                    "users",
                    "comicchapters",
                )
                .select_related("user", "author", "category", "artist", "website")
                .filter(
                    Q(category__name__icontains=category),
                )[0:5]
            )
            serializer = ComicsInfoSerializer(items, many=True)
            return serializer.data
        items = (
            Comic.objects.prefetch_related(
                "comicimages",
                "genres",
                "users",
                "comicchapters",
            )
            .select_related("user", "author", "category", "artist", "website")
            .first()
        )
        serializer = ComicsInfoSerializer(items, many=False)
        return serializer.data

    def get_chapters(self, obj):
        items = obj.get_chapters()
        serializer = ChapterSerializer(items, many=True)
        return serializer.data

    def get_comments(self, obj):
        items = obj.get_comments()
        serializer = CommentSerializer(items, many=True)
        return serializer.data

    def get_users(self, obj):
        items = obj.get_users()
        serializer = UserSerializer(items, many=True)
        return serializer.data

    def get_first_chapter(self, obj):
        items = obj.get_chapters().last()
        serializer = ChapterSerializer(items, many=False)
        return serializer.data

    def get_last_chapter(self, obj):
        items = obj.get_chapters().first()
        serializer = ChapterSerializer(items, many=False)
        return serializer.data

    class Meta:
        model = Comic
        fields = [
            # "id",
            "title",
            "slug",
            "description",
            "rating",
            "numchapters",
            "numimages",
            "updated_at",
            "serialization",
            "status",
            "link",
            "user",
            "category",
            "website",
            "has_images",
            "has_chapters",
            "author",
            "artist",
            "genres",
            "images",
            "chapters",
            "comments",
            "users",
            "related_series",
            "first_chapter",
            "last_chapter",
        ]


class ChapterInfoSerializer(ChapterSerializer):
    # website = WebsiteSerializer(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    # related_series = serializers.SerializerMethodField(read_only=True)
    # comments = serializers.SerializerMethodField(read_only=True)

    def get_images(self, obj):
        items = obj.get_images()
        serializer = ChapterImageSerializer(items, many=True)
        return serializer.data

    # def get_related_series(self, obj):

    #     category = obj.comic.category.name

    #     items = (
    #         Comic.objects.prefetch_related(
    #             "comicimages",
    #             "genres",
    #             "users",
    #             "comicchapters",
    #         )
    #         .select_related("user", "author", "category", "artist", "website")
    #         .filter(
    #             Q(author__name__icontains=category),
    #         )[0:5]
    #     )
    #     serializer = ComicsInfoSerializer(items, many=True)
    #     return serializer.data

    # def get_comments(self, obj):
    #     items = obj.get_comments()
    #     serializer = CommentSerializer(items, many=True)
    #     return serializer.data

    class Meta:
        model = Chapter
        fields = [
            # "id",
            "name",
            "title",
            "slug",
            "link",
            "numimages",
            "updated_at",
            "comic",
            # "website",
            "has_images",
            "images",
            # "related_series",
            # "comments",
        ]


class ChaptersInfoSerializer(ChapterSerializer):
    # updated_at = serializers.DateField(format="%d/%B/%Y")

    # website = WebsiteSerializer(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    # comicSlug = serializers.CharField(source="comic.slug")

    # comments = serializers.SerializerMethodField(read_only=True)

    def get_images(self, obj):
        items = obj.get_images()
        serializer = ChapterImageSerializer(items, many=True)
        return serializer.data

    # def get_comments(self, obj):
    #     items = obj.get_comments()
    #     serializer = CommentSerializer(items, many=True)
    #     return serializer.data

    class Meta:
        model = Chapter
        fields = [
            # "id",
            "name",
            "title",
            "slug",
            "link",
            "numimages",
            "updated_at",
            "comic",
            # "website",
            "has_images",
            "images",
            # "comments",
        ]
