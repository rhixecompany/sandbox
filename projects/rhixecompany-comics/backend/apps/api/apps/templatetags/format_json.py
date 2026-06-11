from django import template
from django.http import JsonResponse

register = template.Library()


@register.filter()
def comicsfilter(value):
    queryset = []
    for comic in value:
        items = comic.get_comic_images_children().values().distinct()
        chapters = comic.get_chapters_children().values().distinct()
        if items:
            if not items:
                queryset.append(
                    {
                        "id": comic.id,
                        "uuid": str(comic.uuid),
                        "title": comic.title,
                        "slug": comic.slug,
                        "description": comic.description,
                        "status": comic.status,
                        "rating": str(comic.rating),
                        "serialization": comic.serialization,
                        "numChapters": comic.numChapters,
                        "spider": comic.spider,
                        "url": comic.url,
                        "numItems": comic.numItems,
                        "updated_at": str(comic.updated_at),
                        "type": comic.type.name,
                        "author": comic.author.name,
                        "artist": comic.artist.name,
                        "comicitems": [
                            {
                                "id": 2,
                                "comic_id": 2,
                                "image": "",
                            },
                        ],
                        "chapters": list(chapters),
                    },
                )
            if not chapters:
                queryset.append(
                    {
                        "id": comic.id,
                        "uuid": str(comic.uuid),
                        "title": comic.title,
                        "slug": comic.slug,
                        "description": comic.description,
                        "status": comic.status,
                        "rating": str(comic.rating),
                        "serialization": comic.serialization,
                        "numChapters": comic.numChapters,
                        "spider": comic.spider,
                        "url": comic.url,
                        "numItems": comic.numItems,
                        "updated_at": str(comic.updated_at),
                        "type": comic.type.name,
                        "author": comic.author.name,
                        "artist": comic.artist.name,
                        "comicitems": list(items),
                        "chapters": [
                            {
                                "id": 348,
                                "uuid": "",
                                "name": "",
                                "title": "",
                                "slug": "",
                                "spider": "",
                                "url": "",
                                "created_at": "",
                                "updated_at": "",
                                "numPages": 2,
                                "comic_id": 2,
                            },
                        ],
                    },
                )

            queryset.append(
                {
                    "id": comic.id,
                    "uuid": str(comic.uuid),
                    "title": comic.title,
                    "slug": comic.slug,
                    "description": comic.description,
                    "status": comic.status,
                    "rating": str(comic.rating),
                    "serialization": comic.serialization,
                    "numChapters": comic.numChapters,
                    "spider": comic.spider,
                    "url": comic.url,
                    "numItems": comic.numItems,
                    "updated_at": str(comic.updated_at),
                    "type": comic.type.name,
                    "author": comic.author.name,
                    "artist": comic.artist.name,
                    "comicitems": list(items),
                    "chapters": list(chapters),
                },
            )
        if not items and not chapters:
            queryset.append(
                {
                    "id": comic.id,
                    "uuid": str(comic.uuid),
                    "title": comic.title,
                    "slug": comic.slug,
                    "description": comic.description,
                    "status": comic.status,
                    "rating": str(comic.rating),
                    "serialization": comic.serialization,
                    "numChapters": comic.numChapters,
                    "spider": comic.spider,
                    "url": comic.url,
                    "numItems": comic.numItems,
                    "updated_at": str(comic.updated_at),
                    "type": comic.type.name,
                    "author": comic.author.name,
                    "artist": comic.artist.name,
                    "comicitems": [
                        {
                            "id": 2,
                            "comic_id": 2,
                            "image": "",
                        },
                    ],
                    "chapters": [
                        {
                            "id": 348,
                            "uuid": "",
                            "name": "",
                            "title": "",
                            "slug": "",
                            "spider": "",
                            "url": "",
                            "created_at": "",
                            "updated_at": "",
                            "numPages": 2,
                            "comic_id": 2,
                        },
                    ],
                },
            )

    return JsonResponse(list(queryset), safe=False).content.decode("utf-8")


@register.filter()
def bookmarksfilter(value):
    queryset = []
    for comic in value:
        items = comic.comic.get_comic_images_children().values().distinct()
        chapters = comic.comic.get_chapters_children().values().distinct()
        if items:
            queryset.append(
                {
                    "id": comic.comic.id,
                    "uuid": str(comic.comic.uuid),
                    "title": comic.comic.title,
                    "slug": comic.comic.slug,
                    "description": comic.comic.description,
                    "status": comic.comic.status,
                    "rating": str(comic.comic.rating),
                    "serialization": comic.comic.serialization,
                    "numChapters": comic.comic.numChapters,
                    "spider": comic.comic.spider,
                    "url": comic.comic.url,
                    "numItems": comic.comic.numItems,
                    "updated_at": str(comic.comic.updated_at),
                    "type": comic.comic.type.name,
                    "author": comic.comic.author.name,
                    "artist": comic.comic.artist.name,
                    "comicitems": list(items),
                    "chapters": list(chapters),
                },
            )

    return JsonResponse(list(queryset), safe=False).content.decode("utf-8")


@register.filter()
def defaultfilter(value):
    return JsonResponse(list(value.values().distinct()), safe=False).content.decode(
        "utf-8",
    )


@register.filter()
def comicfilter(value):
    items = value.get_comic_images_children().values().distinct()
    chapters = value.get_chapters_children().values().distinct()

    if items:
        if not items:
            comic = JsonResponse(
                {
                    "id": value.id,
                    "uuid": str(value.uuid),
                    "title": value.title,
                    "slug": value.slug,
                    "description": value.description,
                    "status": value.status,
                    "rating": str(value.rating),
                    "serialization": value.serialization,
                    "numChapters": value.numChapters,
                    "spider": value.spider,
                    "url": value.url,
                    "numItems": value.numItems,
                    "updated_at": str(value.updated_at),
                    "type": value.type.name,
                    "author": value.author.name,
                    "artist": value.artist.name,
                    "comicitems": [
                        {
                            "id": 2,
                            "comic_id": 2,
                            "image": "",
                        },
                    ],
                    "chapters": list(chapters),
                },
            ).content.decode("utf-8")
        if not chapters:
            comic = JsonResponse(
                {
                    "id": value.id,
                    "uuid": str(value.uuid),
                    "title": value.title,
                    "slug": value.slug,
                    "description": value.description,
                    "status": value.status,
                    "rating": str(value.rating),
                    "serialization": value.serialization,
                    "numChapters": value.numChapters,
                    "spider": value.spider,
                    "url": value.url,
                    "numItems": value.numItems,
                    "updated_at": str(value.updated_at),
                    "type": value.type.name,
                    "author": value.author.name,
                    "artist": value.artist.name,
                    "comicitems": list(items),
                    "chapters": [
                        {
                            "id": 348,
                            "uuid": "",
                            "name": "",
                            "title": "",
                            "slug": "",
                            "spider": "",
                            "url": "",
                            "created_at": "",
                            "updated_at": "",
                            "numPages": 2,
                            "comic_id": 2,
                        },
                    ],
                },
            ).content.decode("utf-8")
        comic = JsonResponse(
            {
                "id": value.id,
                "uuid": str(value.uuid),
                "title": value.title,
                "slug": value.slug,
                "description": value.description,
                "status": value.status,
                "rating": str(value.rating),
                "serialization": value.serialization,
                "numChapters": value.numChapters,
                "spider": value.spider,
                "url": value.url,
                "numItems": value.numItems,
                "updated_at": str(value.updated_at),
                "type": value.type.name,
                "author": value.author.name,
                "artist": value.artist.name,
                "comicitems": list(items),
                "chapters": list(chapters),
            },
        ).content.decode("utf-8")
    if not items and not chapters:
        comic = JsonResponse(
            {
                "id": value.id,
                "uuid": str(value.uuid),
                "title": value.title,
                "slug": value.slug,
                "description": value.description,
                "status": value.status,
                "rating": str(value.rating),
                "serialization": value.serialization,
                "numChapters": value.numChapters,
                "spider": value.spider,
                "url": value.url,
                "numItems": value.numItems,
                "updated_at": str(value.updated_at),
                "type": value.type.name,
                "author": value.author.name,
                "artist": value.artist.name,
                "comicitems": [
                    {
                        "id": 2,
                        "comic_id": 2,
                        "image": "",
                    },
                ],
                "chapters": [
                    {
                        "id": 348,
                        "uuid": "",
                        "name": "",
                        "title": "",
                        "slug": "",
                        "spider": "",
                        "url": "",
                        "created_at": "",
                        "updated_at": "",
                        "numPages": 2,
                        "comic_id": 2,
                    },
                ],
            },
        ).content.decode("utf-8")

    return comic
