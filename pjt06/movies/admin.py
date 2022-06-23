from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description')
admin.site.register(Movie, MovieAdmin)
# Register your models here.
