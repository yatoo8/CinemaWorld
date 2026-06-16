from django.contrib import admin
from django.urls import path
from apps.session.views import SessionListView

urlpatterns = [
    path('schedule/', SessionListView.as_view(), name='Расписание')
]
