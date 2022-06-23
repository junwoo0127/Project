import requests
from pprint import pprint


def vote_average_movies():
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
    return(my_list)
            

        
    
            

        
            

if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
