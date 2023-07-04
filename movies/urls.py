from django.urls import path

from .views import CreateListMovieView, MovieDetailView

urlpatterns = [
    path("movies/", CreateListMovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDetailView.as_view()),
]
