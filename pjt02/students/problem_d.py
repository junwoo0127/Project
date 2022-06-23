import requests
from pprint import pprint


def recommendation(title):
    URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : '27c401733d90558d9160f01f1122cd6b' ,
        'language': 'ko' ,
        'query' : title       
    }

    response = requests.get(URL+path, params=params).json()
   
    if len(response['results']) == 0 :
        return None
    movie_id = response['results'][0]['id']
    
    path = f'/movie/{movie_id}/recommendations'                
    params = {
        'api_key' : '27c401733d90558d9160f01f1122cd6b' ,
        'language': 'ko'                  
    }
    response2 = requests.get(URL+path, params=params).json()

    my_tit = []
    for mov_tit in response2['results']:
        my_tit.append(mov_tit['original_title'])
    return my_tit
    
              
   

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None
