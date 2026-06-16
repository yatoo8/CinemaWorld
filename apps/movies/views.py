from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from apps.movies.models import Movie
from apps.session.models import Session
from apps.promotions.models import Promotion

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
         
        context['movies'] = Movie.objects.all()
        context['promotions'] = Promotion.objects.all()
        context['sessions'] = Session.objects.select_related(
            'movie', 'hall'
        ).order_by('data', 'time')[:5]

        return context

class MovieListView(ListView):
    model = Movie
    template_name = 'pages/movie_list.html'
    context_object_name = 'movies'

    

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