from django.urls import path

from api.apps.views import chapter_views as views

app_name = "chapters"
urlpatterns = [
    path(
        "",
        view=views.chapter_list_view,
        name="chapter_list",
    ),
    path(
        "add/",
        view=views.chapter_create_view,
        name="add_chapter",
    ),
    path(
        "<str:slug>/edit/",
        view=views.chapter_update_view,
        name="update_chapter",
    ),
    path(
        "<str:slug>/delete/",
        view=views.chapter_delete_view,
        name="delete_chapter",
    ),
    path(
        "<str:slug>/",
        view=views.chapter_detail_view,
        name="chapter_detail",
    ),
]
htmxurlpatterns = [
    path(
        "hx/<str:slug>/",
        view=views.chapter_detail_hx_view,
        name="hx_chapter_detail",
    ),
    path(
        "hx/<str:parent_slug>/image/<int:id>/",
        view=views.chapter_images_update_hx_view,
        name="hx_image_update",
    ),
    path(
        "hx/<str:parent_slug>/image/",
        view=views.chapter_images_update_hx_view,
        name="hx_image_create",
    ),
    path(
        "hx/<str:parent_slug>/delete/<int:id>/",
        view=views.chapter_images_delete_view,
        name="delete_chapter_image",
    ),
]

urlpatterns += htmxurlpatterns
