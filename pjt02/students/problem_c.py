import requests
from pprint import pprint


def ranking():
    URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '27c401733d90558d9160f01f1122cd6b' ,
        'language': 'ko' ,
        'region' : 'KR'
    }

    response = requests.get(URL+path, params=params)
    data = response.json()

    my_list = []
    for movie in data['results'] :
        
        if movie['vote_average'] >= 8 :
            
            my_list.append(movie)
    return sorted(my_list, key = lambda k: k['vote_average'], reverse = True)          


if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
