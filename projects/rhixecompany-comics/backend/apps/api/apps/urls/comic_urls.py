from django.urls import path

from api.apps.views import comic_views as views

app_name = "comics"
urlpatterns = [
    path(
        "",
        view=views.comic_list_view,
        name="comic_list",
    ),
    path(
        "remove/images/",
        view=views.comic_image_delete_all_view,
        name="delete_all_comic_image",
    ),
    path(
        "remove/comics/",
        view=views.comic_delete_all_view,
        name="delete_all_comics",
    ),
    path(
        "remove/images/",
        view=views.comic_image_delete_all_view,
        name="delete_all_comic_image",
    ),
    path(
        "add/",
        view=views.comic_create_view,
        name="add_comic",
    ),
    path(
        "<str:slug>/edit/",
        view=views.comic_update_view,
        name="update_comic",
    ),
    path(
        "<str:slug>/delete/",
        view=views.comic_delete_view,
        name="delete_comic",
    ),
    path(
        "<str:slug>/",
        view=views.comic_detail_view,
        name="comic_detail",
    ),
]
htmxurlpatterns = [
    path(
        "hx/<str:slug>/",
        view=views.comic_detail_hx_view,
        name="hx_comic_detail",
    ),
    path(
        "hx/<str:parent_slug>/chapter/<int:id>/",
        view=views.comic_chapters_update_hx_view,
        name="hx_chapter_update",
    ),
    path(
        "hx/<str:parent_slug>/chapter/",
        view=views.comic_chapters_update_hx_view,
        name="hx_chapter_create",
    ),
    path(
        "hx/<str:parent_slug>/chapter/delete/<int:id>/",
        view=views.comic_chapters_delete_view,
        name="delete_comic_chapter",
    ),
    path(
        "hx/<str:parent_slug>/image/<int:id>/",
        view=views.comic_images_update_hx_view,
        name="hx_image_update",
    ),
    path(
        "hx/<str:parent_slug>/image/",
        view=views.comic_images_update_hx_view,
        name="hx_image_create",
    ),
    path(
        "hx/<str:parent_slug>/image/delete/<int:id>/",
        view=views.comic_images_delete_view,
        name="delete_comic_image",
    ),
]
urlpatterns += htmxurlpatterns
