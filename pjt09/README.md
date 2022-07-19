# 과정

1. 인증 사용자만 받으려고 POST로 JS 짰던 내용

```javascript
   const userId = event.target.dataset.userId   
   const URL = `/accounts/${userId}/follow/`
   const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
   axios({
     method: 'post',
     url: URL,
     headers: {'X-CSRFToken': csrftoken}
   })
   .then( response => {
     console.log(response)
   })
 }) 
```

어차피 로그아웃 상태에서 유저 페이지를 볼 수 없었음 (로그인 해야 됐었음)

![image-20220506140912738](https://raw.githubusercontent.com/bmyusharp/TIL-assets/master/img/image-20220506140912738.png)



# 추천 알고리즘 구상

-좋아요 누른 영화가 하나도 없을 시 : 랜덤 10개

-좋아요를 하나 이상이라도 눌렀을 시 : 좋아요 한 영화의 태그를 전부 가져옴.. 중복시 +1

가장 많이 좋아요가 눌린 태그 





## 랜덤으로 가져오기

