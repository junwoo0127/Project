import requests
import json
from pprint import pprint

Base_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'

movies_data = []
actors_data = []
for i in range(1, 3):
    params = {
        'api_key': '2c7d28aa458a391931ccc39e32053cbb',
        'region' : 'KR',
        'language' : 'ko',
        'page' : f'{i}'
    }
    response = requests.get(Base_URL + path, params=params)
    data = response.json()
    movies = data.get('results') # data(dict)안에 'results'(list)를 가져옴 => list 안에는 영화별로 dict형태로 주어짐 
    for movie in movies:
        if movie.get('genre_ids'):
            movie_id = movie['id']
            response2 = requests.get(Base_URL + f'/movie/{movie_id}/videos', params=params)    # youtube 경로 가져오기

            if response2.json().get('results'):
                youtube = response2.json().get('results')[0]['key']

                response3 = requests.get(Base_URL + f'/movie/{movie_id}', params=params)    # 영화 detail에서 runtime 가져오기
                response4 = requests.get(Base_URL + f'/movie/{movie_id}/credits', params=params)    # 영화 credits에서 출연 배우 가져오기
                actors = []
                for actor in response4.json().get('cast'):
                    actors.append(actor['id'])
                    fields2 = {
                        'id': actor['id'],
                        'name': actor['name'],
                        'profile_path': actor['profile_path']
                    }
                    temp2 = {
                        'pk': actor['id'],
                        'model': 'movies.actor',
                        'fields': fields2
                    }
                    actors_data.append(temp2)
                fields1 = {
                    'id': movie['id'],
                    'title': movie['title'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'release_date': movie['release_date'],
                    'genres': movie['genre_ids'],
                    'popularity': movie['popularity'],
                    'vote_average': movie['vote_average'],
                    'video_id': youtube,
                    'runtime': response3.json().get('runtime'),
                    'actors': actors
                }
                temp1 = {
                        "pk": movie['id'],
                        "model": "movies.movie",
                        "fields": fields1
                    }
                movies_data.append(temp1)


with open('./data.json','w', encoding="utf-8") as f:
    json.dump(movies_data, f, ensure_ascii=False, indent=4)
with open('./actors.json','w', encoding="utf-8") as f:
    json.dump(actors_data, f, ensure_ascii=False, indent=4)