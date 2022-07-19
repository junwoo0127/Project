import requests
import json
from pprint import pprint

# tmdb에 요청 보낼 url, path, 변수
Base_URL = 'https://api.themoviedb.org/3'
path = '/genre/movie/list'
params = {
    'api_key': '2c7d28aa458a391931ccc39e32053cbb',
    'region' : 'KR',
    'language' : 'ko'
}

# 요청 보내고 받은 데이터를 json형태로 바꾸기
response = requests.get(Base_URL + path, params=params)
data = response.json()
genres = data.get('genres')

# DB에 들어갈 데이터를 추출하여 json형태로 저장
total_data = []
for genre in genres:
    fields = {
        'id': genre['id'],
        'name': genre['name']
    }
    temp = {
            "pk": genre['id'],
            "model": "movies.genre",
            "fields": fields
        }
    total_data.append(temp)

# json 파일 만들기
with open('./genres.json','w', encoding="utf-8") as f:
    json.dump(total_data, f, ensure_ascii=False, indent=4)