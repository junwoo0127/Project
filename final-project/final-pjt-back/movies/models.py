from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200, null=True)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    popularity = models.FloatField()
    vote_average = models.FloatField()
    video_id = models.TextField()
    runtime = models.IntegerField()
    views = models.IntegerField(default=0)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(null=True)