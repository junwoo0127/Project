from django.contrib import admin
from .models import Actor, Movie, Review

# Register your models here.
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','overview','release_date', 'poster_path',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title','content',)

admin.site.register(Actor, ActorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)