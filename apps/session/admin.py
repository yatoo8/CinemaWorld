from django.contrib import admin
from apps.session.models import Session

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('movie', 'hall', 'status')
    search_fields = ('movie__title', )
    list_display_links = ('movie', )
    