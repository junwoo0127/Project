from django.contrib import admin
from .models import Movie, Actor, Genre, Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'score', 'movie')

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Review, ReviewAdmin)
