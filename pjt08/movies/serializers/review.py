from rest_framework import serializers
from ..models import Review, Movie

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)

class ReviewListSerializer(serializers.ModelSerializer):
    movie_set = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ('title','content','movie_set',)

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ('id','movie','title','content',)
        read_only_fields = ('movie',)