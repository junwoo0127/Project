import pandas as pd
import numpy as np
import json
from pandas import json_normalize
from sklearn.preprocessing import MinMaxScaler

def get_recommendation(genres=[]):
    with open('./movies/fixtures/data.json', encoding="UTF8") as f:
        data = json.load(f)
    df = json_normalize(data)
    df2 = json_normalize(data)
    # 불필요한 열 제거
    df = df.drop(['model', 'fields.id', 'fields.poster_path', 'fields.video_id', 'fields.runtime', 'fields.actors'], axis=1)
    df2 = df2.drop(['model', 'fields.id'], axis=1)
    # 열 이름 수정
    df.columns = ['pk', 'title', 'overview', 'release_date', 'genres', 'popularity', 'vote_average']
    df2.columns = ['pk', 'title', 'overview', 'poster_path', 'release_date', 'genres', 'popularity', 
    'vote_average', 'video_id', 'runtime', 'actors']

    # 평점 scaling
    scaler = MinMaxScaler()
    scaler.fit(df[['vote_average']])
    df['scaled_vote'] = scaler.transform(df[['vote_average']])
    # popularity scaling
    scaler = MinMaxScaler()
    scaler.fit(df[['popularity']])
    df['scaled_popularity'] = scaler.transform(df[['popularity']])
    # movie_rate 열 생성
    df['movie_rate'] = df['scaled_vote'] + df['scaled_popularity']

    if genres:
        for genre in genres:
            for idx, row in df.iterrows():
                if genre in row['genres']:
                    df.loc[idx, 'movie_rate'] += 0.5
    df = df.sort_values('movie_rate', ascending=False)
    id_list = []
    for idx, row in df.iterrows():
        id_list.append(idx)
    id = id_list[0:20]
    df_result = df2.iloc[id, :]
    result = df_result.to_dict('records')
    return(result)

# print(get_recommendation([12,28]))