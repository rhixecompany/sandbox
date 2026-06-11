from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.libary.views import comic_views as views

app_name = "comics"

urlpatterns = [
    path("", views.getcomics, name="comics"),
    path("create/", views.createcomic, name="comic-create"),
    path("upload/", views.uploadimage, name="image-upload"),
    path("top/", views.gettopcomics, name="top-comics"),
    path("featured/", views.getfeaturedcomics, name="featured-comics"),
    path("select/", views.getselectcomics, name="select-comics"),
    path("<str:slug>/", views.getcomic, name="comic"),
    path("update/<str:slug>/", views.updatecomic, name="comic-update"),
    path("delete/<str:slug>/", views.deletecomic, name="comic-delete"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
