# DRF Prototype

> drf prototype vue에서 서버에 요청을 보내고 기초 기능을 구현하기 위해 만든 프로토타입



## 시작하기 

- clone 받은 후에 

```bash
# 가상환경 설정
python -m venv venv

# 설치
pip install -r requirements.txt

# migrate 
python manage.py migrate

# fixture loaddata
python manage.py loaddata genres.json actors.json data.json

# runserver
python manage.py runserver
```



### 요청 URL

- `http://127.0.0.1:8000/` 
- vue `http://localhost:8080/` 에서 요청 보내기
- 요청 예시

```javascript
createMovies ({ commit }) {
      const API_URL = 'http://127.0.0.1:8000/api/v1/movies/movies/'
      axios({
        method: 'get',
        url: API_URL,
        headers: { Authorization: 'Token 7fea7fb87d84d21609091cce89a7dfaf4b14bb5e' }
      })
        .then(response => {
          console.log(response)
          commit('CREATE_MOVIES', response.data)
        })
        .catch(error => {
          console.log(error)
        })
    }
```



## ERD
![image-20220519003911472](readme.assets/image-20220519003911472-16528883528161.png)