from django.db import models

GENRE_CHOICES = [
    ('액션', '액션'),
    ('스릴러', '스릴러'),
    ('코미디', '코미디'),
    ('SF','SF'),
    ('로맨스','로맨스'),
]

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField(null=True)
    release_date = models.DateField(null=True)
    genre = models.CharField(max_length=30, choices=GENRE_CHOICES)
    score = models.FloatField(null=True)
    poster_url = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
