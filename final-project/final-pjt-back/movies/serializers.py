from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Actor, Movie, Review, Genre

class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name',)


class ActorSerializer(serializers.ModelSerializer):
    class MovieActorSerializer(serializers.ModelSerializer):

        class Meta:
            model = Movie
            fields = ('title',)

    movies = MovieActorSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'






class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('pk', 'score')

class ReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'score', 'user', 'movie')
        read_only_fields = ('movie', )





class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview', 'poster_path',)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class ActorOneSerializer(serializers.ModelSerializer):

        class Meta:
            model = Actor
            fields = ('pk', 'name',)

    actors = ActorOneSerializer(many=True, read_only=True)
    reviews = ReviewListSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview', 'poster_path', 'release_date', 'genres', 'actors', 
        'popularity', 'vote_average', 'video_id', 'runtime', 'views', 'like_users', 'reviews')
        read_only_fields = ('actors',)




class GenreMovieSerializer(serializers.ModelSerializer):

    movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = '__all__'