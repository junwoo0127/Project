import requests
from pprint import pprint


def popular_count():
    URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '27c401733d90558d9160f01f1122cd6b' ,
        'language': 'ko' ,
        'region' : 'KR'
    }

    response = requests.get(URL+path, params=params)
    data = response.json()
    

    return len(data['results'])


    pass 
    # 여기에 코드를 작성합니다.  


if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20
