from pprint import pprint

from api.apps.models import Chapter, ChapterImage, Comic, ComicImage


def run():
    comics = (
        Comic.objects.prefetch_related(
            "comicitems",
            "comicchapters",
            "genres",
            "followers",
        )
        .select_related("author", "type", "artist", "user")
        .all()
    )
    comic_images = ComicImage.objects.select_related("comic").all()
    pprint(
        {
            "Comics": comics.values()[0:2],
            "Comics_Count": comics.count(),
            "ComicsImage": comic_images.values()[0:2],
            "ComicsImage_Count": comic_images.count(),
        },
    )
    chapters = Chapter.objects.prefetch_related("chapteritems").select_related("comic").all()
    chapter_images = ChapterImage.objects.select_related("comic", "chapter").all()
    pprint(
        {
            "Chapters": chapters.values()[0:2],
            "Chapters_Count": chapters.count(),
            "ChaptersImage": chapter_images.values()[0:2],
            "ChaptersImage_Count": chapter_images.count(),
        },
    )
