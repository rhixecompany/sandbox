from django.urls import path
from video.views import series_views as views

urlpatterns = [
    path('', views.getSeries, name="series"),
    path('top/', views.getTopSeries, name='top-series'),
    path('<str:pk>/', views.getSerie, name="serie"),
    path('create/', views.createSeries, name="series-create"),
    path('upload/', views.uploadImage, name="image-upload"),
    path('update/<str:pk>/', views.updateSeries, name="series-update"),
    path('delete/<str:pk>/', views.deleteSeries, name="series-delete"),
]
