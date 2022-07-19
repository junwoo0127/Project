from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.actor_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/like/', views.like_movie),
    path('genres/', views.genre_list),
    path('genres/<int:genre_pk>/', views.genre_movies),
    path('<int:movie_pk>/reviews/', views.create_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail),
    path('nowplaying/', views.nowplaying),
    path('search/<str:query>/', views.search),
    path('recommendation/', views.recommendation),
]
