import requests
from pprint import pprint


def credits(title):
    Base_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '43887d8f3c4ff8d10cfc9844fdbe9ba8',
        'region' : 'KR',
        'language' : 'ko',
        'query': title
    }
    response = requests.get(Base_URL + path, params = params).json()

    movie_id = 0
    for move in response.get('results'):
        if title == move.get('title'):
            movie_id = move.get('id')
    # movie_id가 0이라면 없는 영화이기 때문에 None을 반환합니다.
    if movie_id == 0:
        return None
    
    params = {
        'api_key' : '43887d8f3c4ff8d10cfc9844fdbe9ba8',
        'language' : 'ko'
    }
    
    result = {}
    # movie_id를 기준으로 영화 credits 정보들을 받아옵니다.
    response = requests.get(Base_URL + '/movie/{}/credits'.format(movie_id), params = params).json()
    
    # cast_id가 10 이하인 배우의 이름을 result['cast']에 추가합니다.
    for movie in response.get('cast'):
        if movie.get('cast_id') < 10:
            result['cast'] = result.get('cast', []) + [movie.get('name')]
    # department가 Directing인 스태프의 이름을 result['crew']에 추가합니다.
    for movie in response.get('crew'):
        if movie.get('department') == 'Directing':
            result['crew'] = result.get('crew', []) + [movie.get('name')]
    
    return result
 


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None
