from django.contrib import admin
from apps.halls.models import Hall

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('title', 'hall_type', 'seats_count')
    list_display_links = ('title', )
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title', )
    list_filter = ('hall_type', )