from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'producer', 'release_date', 'rating')
    search_fields = ('title', 'producer')
    list_filter = ('release_date',)