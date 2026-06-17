from django.contrib import admin
from apps.movies.models import Movie, Contacts

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'status')
    search_fields = ('title', 'genre')
    list_display_links = ('title', )
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('status', 'genre')

@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'address')
    search_fields = ('phone', 'address')
    list_display_links = ('phone', )
    