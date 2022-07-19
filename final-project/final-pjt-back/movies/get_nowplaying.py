import requests
import json
def get_nowplaying():
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '2c7d28aa458a391931ccc39e32053cbb',
        'region' : 'KR',
        'language' : 'ko'
    }

    response = requests.get(Base_URL + path, params=params)
    data = response.json()
    movies = data.get('results')
    movies_data = []
    actors_data = []
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
                        'pk': actor['id'],
                        'name': actor['name'],
                        'profile_path': actor['profile_path']
                    }
                    actors_data.append(fields2)
                fields1 = {
                    'pk': movie['id'],
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
                movies_data.append(fields1)
    return movies_data, actors_data