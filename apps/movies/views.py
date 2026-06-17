from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from apps.movies.models import Movie, Contacts
from apps.session.models import Session
from apps.promotions.models import Promotion

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
         
        context['movies'] = Movie.objects.prefetch_related('session_set')
        context['movies_showing'] = Movie.objects.filter(status='showing').prefetch_related('session_set')[:3]
        context['movies_soon'] = Movie.objects.filter(status='soon').prefetch_related('session_set')[:3]
        context['movies_archive'] = Movie.objects.filter(status='archive').prefetch_related('session_set')[:3]

        context['promotions'] = Promotion.objects.all()
        context['sessions'] = Session.objects.select_related(
            'movie', 'hall'
        ).order_by('data', 'time')[:5]

        return context

class MovieListView(ListView):
    model = Movie
    template_name = 'pages/movie_list.html'
    context_object_name = 'movies'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["movies_soon"] = Movie.objects.filter(status='soon').prefetch_related('session_set')
        context["movies_showing"] = Movie.objects.filter(status='showing').prefetch_related('session_set')
        return context
    

    

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'pages/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
     
        context['sessions'] = Session.objects.select_related(
            'movie', 'hall'
        ).filter(movie=self.object)

        return context