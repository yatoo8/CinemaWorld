from django.contrib import admin
from apps.movies.models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'status')
    search_fields = ('title', 'genre')
    list_display_links = ('title', )
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status', 'genre')
    