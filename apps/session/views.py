from django.shortcuts import render
from apps.halls.models import Hall
from apps.movies.models import Movie
from apps.session.models import Session
from django.views.generic import ListView
from typing import Any

class ScheduleView(ListView):
    template_name = 'pages/schedule.html'
    model = Session
    context_object_name = 'sessions'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["halls"] = Hall.objects.all()
        context['movies'] = Movie.objects.prefetch_related('session_set')
        return context
    
    def get_queryset(self):
        queryset = Session.objects.select_related('movie', 'hall')

        date = self.request.GET.get('date')

        hall = self.request.GET.get('hall')

        hall_type = self.request.GET.get('hall_type')
        if date:
            queryset = queryset.filter(data=date)
        if hall:
            queryset = queryset.filter(hall=hall)
        if hall_type:
            queryset = queryset.filter(hall__hall_type=hall_type)
        return queryset
    
