from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField(null=True)
    release_date = models.DateField(null=True)
    genre = models.CharField(max_length=30)
    score = models.FloatField(null=True)
    poster_url = models.TextField()
    description = models.TextField()
# Create your models here.
