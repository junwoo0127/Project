from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.models import Article
from movies.models import Movie, Review
from .models import User

class ProfileSerializer(serializers.ModelSerializer):

    class ArticleSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Article
            fields = ('pk', 'title', 'content')

    like_articles = ArticleSerializer(many=True)
    articles = ArticleSerializer(many=True)

    class MovieSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Movie
            fields = ('pk', 'title', 'overview', 'poster_path')
    like_movies = MovieSerializer(many=True)

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'is_superuser', 'email', 'like_articles', 'articles', 'like_movies')

class UserSerializer(serializers.ModelSerializer):

    class ReviewSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Review
            fields = ('pk', 'score', 'movie',)
    
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = User
        fields = ['pk', 'username', 'reviews', 'is_superuser']