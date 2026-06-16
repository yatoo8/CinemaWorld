from django.contrib import admin
from apps.promotions.models import Promotion

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'valid_until')
    search_fields = ('title', )
    list_display_links = ('title', )
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('valid_until',) 