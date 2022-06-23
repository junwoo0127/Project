import json
from pprint import pprint


def movie_info(movie, genres):

    my_dict ={}

    for i in movie :
        key_num = ['genre_ids', 'id', 'overview', 'poster_path', 'title', 'vote_average']
        for j in key_num:
            if i == j:
                #print(movie[j])
                my_dict[j] = movie[j]

    genres_dict = {}
    for genre in genres:
        genres_dict[genre.get('id')] = genre.get('name')


    name_list =[]
    for genre_id in my_dict['genre_ids']:
        name_list.append(genres_dict[genre_id])
        my_dict['genre_names'] = name_list

    del my_dict['genre_ids']
    return my_dict

      
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))