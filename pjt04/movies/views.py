from turtle import title
from django.shortcuts import render
import requests
import random

# Create your views here.

def index(request):
    context = {
        'movies': [
            {
                'title': '인셉션',
                'content': '내용1'
            }, 
            {
                'title': '반지의제왕',
                'content': '내용2'
            }, 
            {
                'title': '어벤져스',
                'content': '내용3'
            }, 
            {
                'title': '스파이더맨',
                'content': '내용4'
            },
            {
                'title': '배트맨',
                'content': '내용4'
            },
            {
                'title': '슈퍼맨',
                'content': '내용4'
            }, 
        ]
    }
    return render(request, 'index.html', context)

def recommendations(request): 
    URL = f'https://api.themoviedb.org/3/movie/278/recommendations'
    params = {
        'api_key' : '27c401733d90558d9160f01f1122cd6b' ,
        'region' : 'KR',
        'language' : 'ko'              
    }
    response = requests.get(URL, params=params).json()
    movie = random.choice(response.get('results'))

    context = {
        'movie': movie
    }   
    
    return render(request, 'recommendations.html', context)