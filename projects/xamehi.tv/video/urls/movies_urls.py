<<<<<<< HEAD
from django.urls import path
from video.views import movies_views as views

urlpatterns = [
    path('', views.getMovies, name="movies"),
    path('top/', views.getTopMovies, name='top-movies'),
    path('<str:pk>/', views.getMovie, name="movie"),
    path('create/', views.createMovie, name="movie-create"),
    path('upload/', views.uploadFile, name="file-upload"),
    path('update/<str:pk>/', views.updateMovie, name="movie-update"),
    path('delete/<str:pk>/', views.deleteMovie, name="movie-delete"),
]
=======
from django.urls import path
from video.views import movies_views as views

urlpatterns = [
    path('', views.getMovies, name="movies"),
    path('top/', views.getTopMovies, name='top-movies'),
    path('<str:pk>/', views.getMovie, name="movie"),
    path('create/', views.createMovie, name="movie-create"),
    path('upload/', views.uploadFile, name="file-upload"),
    path('update/<str:pk>/', views.updateMovie, name="movie-update"),
    path('delete/<str:pk>/', views.deleteMovie, name="movie-delete"),
]
>>>>>>> 6031d8f (chore: initial local project setup for xamehi.tv)
