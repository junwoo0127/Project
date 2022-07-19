from rest_framework import serializers
from ..models import Movie, Review, Actor

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)

class ActorSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Actor
        fields = ('name',)

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = ('id','actors','review_set','title','overview','release_date','poster_path',)