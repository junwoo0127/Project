from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import (ActorListSerializer, ActorSerializer, MovieListSerializer, 
MovieSerializer, ReviewListSerializer, ReviewSerializer, GenreSerializer, GenreMovieSerializer)
from .models import Actor, Movie, Review, Genre
from .get_nowplaying import get_nowplaying
from .recommendations import get_recommendation

# Create your views here.
@api_view(['GET'])
def recommendation(request):
    user = request.user
    movies = user.like_movies.all()
    total_genres = []
    for movie in movies:
        genres = movie.genres.all()
        for genre in genres:
            total_genres.append(genre.pk)
    result = get_recommendation(total_genres)
    # serializer = MovieSerializer(movies, many=True)
    return Response(result)

@api_view(['GET'])
def nowplaying(request):
    movies, actors = get_nowplaying()
    for movie in movies:
        if not Movie.objects.filter(pk=movie['pk']).exists():
            Movie.objects.create(pk=movie['pk'],title=movie['title'],
                    overview=movie['overview'],
                    poster_path=movie['poster_path'],
                    release_date=movie['release_date'],
                    genres=movie['genre_ids'],
                    actors=movie['actors'],
                    popularity=movie['popularity'],
                    vote_average=movie['vote_average'],
                    video_id=movie['video_id'],
                    runtime=movie['runtime'],)
    for actor in actors:
        if not Actor.objects.filter(pk=actor['pk']):
            Actor.objects.create(pk=actor['pk'], name=actor['name'],
            profile_path=actor['profile_path'])
    return Response(movies)

@api_view(['GET'])
def actor_list(request):
    actors = get_list_or_404(Actor)
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    paginator = Paginator(movies, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    serializer = MovieListSerializer(page_obj, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        is_liked = False
        context = {
            'is_liked': is_liked,
        }
        serializer = MovieSerializer(movie, context=context)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        is_liked = True
        context = {
            'is_liked': is_liked,
        }
        serializer = MovieSerializer(movie, context=context)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        if request.user == review.user:
            serializer = ReviewSerializer(review, request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                
                # reviews = movie.reviews.all()
                # serializer = ReviewSerializer(reviews, many=True)
                return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if request.user == review.user:
            review.delete()
            
            # reviews = movie.reviews.all()
            # serializer = ReviewSerializer(reviews, many=True)
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def create_review(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = movie.reviews.all()

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)

        # reviews = movie.reviews.all()
        # serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        # if not movie.reviews.filter(user = user).exists():
        # else:
        #     context = {
        #         'warning': '리뷰는 한번만 작성할 수 있습니다.'
        #     }
        #     return Response(context, status=status.HTTP_403_FORBIDDEN)




@api_view(['GET'])
def genre_list(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genre_movies(request, genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreMovieSerializer(genre)
    return Response(serializer.data)

@api_view(['GET'])
def search(request, query):
    if query:
        movies = Movie.objects.filter(title__contains=query)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
