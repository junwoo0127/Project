import json
from pprint import pprint


def movie_info(movie):
    my_dict = {}   
    want = ['genre_ids', 'id', 'overview', 'poster_path', 'title', 'vote_average' ]
    for i in movie:
        for j in want:
            if i == j:
                my_dict[j] = movie[j]
                
    return my_dict
    


    
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))