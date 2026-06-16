from apps.movies.views import HomeView, MovieDetailView, MovieListView
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('movie_list', MovieListView.as_view(), name='movie_list'),
    path('movie/<slug:slug>', MovieDetailView.as_view(), name='movie_detail')
]
