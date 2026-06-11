from django import template
from django.http import JsonResponse

register = template.Library()


@register.filter()
def defaultfilter(value):
    qs = []
    for obj in value:
        if obj.has_chapters:
            qs.append(
                {
                    "id": obj.id,
                    "title": obj.title,
                    "slug": obj.slug,
                    "description": obj.description,
                    "status": obj.status,
                    "rating": str(obj.rating),
                    "serialization": obj.serialization,
                    "numchapters": obj.numchapters,
                    "website": obj.website.name,
                    "numimages": obj.numimages,
                    "updated_at": str(obj.updated_at),
                    "category": obj.category.name,
                    "author": obj.author.name,
                    "artist": obj.artist.name,
                    "images": list(obj.get_images().values().distinct()),
                    "chapters": list(obj.get_chapters().values().distinct()),
                    "genres": list(obj.genres.all().values().distinct()),
                },
            )
        else:
            qs.append(
                {
                    "id": obj.id,
                    "title": obj.title,
                    "slug": obj.slug,
                    "description": obj.description,
                    "status": obj.status,
                    "rating": str(obj.rating),
                    "serialization": obj.serialization,
                    "numchapters": obj.numchapters,
                    "numimages": obj.numimages,
                    "updated_at": str(obj.updated_at),
                    "website": obj.website.name,
                    "category": obj.category.name,
                    "author": obj.author.name,
                    "artist": obj.artist.name,
                    "images": list(obj.get_images().values().distinct()),
                    "genres": list(obj.genres.all().values().distinct()),
                },
            )
    return JsonResponse(list(qs), safe=False).content.decode(
        "utf-8",
    )
