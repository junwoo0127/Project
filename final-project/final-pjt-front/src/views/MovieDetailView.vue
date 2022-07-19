<template>  
  <div class="detailhome">    
    <h1 class="title">
      <br>
      <span>Movie Detail</span>
    </h1>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <div class="detail">
      <div class="movieCard row">
        <div class="col" style="margin: 10px">
          <img :src="img_url" alt="Image">
        </div>
        <div class="movieCardText col" style="margin: 10px">
          <div class="movieTitle">
            <h1>{{ movie.title }}</h1>
            <div class="userRate">
              <div class="star-rating space-x-4 mx-auto" v-if=" !isRated">
                <input type="radio" id="5-stars" name="rating" value="5" v-model="score" @click="addRating"/>
                <label for="5-stars" class="star pr-4">★</label>
                <input type="radio" id="4-stars" name="rating" value="4" v-model="score" @click="addRating"/>
                <label for="4-stars" class="star">★</label>
                <input type="radio" id="3-stars" name="rating" value="3" v-model="score" @click="addRating"/>
                <label for="3-stars" class="star">★</label>
                <input type="radio" id="2-stars" name="rating" value="2" v-model="score" @click="addRating"/>
                <label for="2-stars" class="star">★</label>
                <input type="radio" id="1-star" name="rating" value="1" v-model="score" @click="addRating"/>
                <label for="1-star" class="star">★</label>
              </div>
              <div class="star-rating space-x-4 mx-auto" v-if="isRated">
                <input type="radio" id="5-stars" name="rating" value="5" v-model="score" @click="updateRating"/>
                <label for="5-stars" class="star pr-4">★</label>
                <input type="radio" id="4-stars" name="rating" value="4" v-model="score" @click="updateRating"/>
                <label for="4-stars" class="star">★</label>
                <input type="radio" id="3-stars" name="rating" value="3" v-model="score" @click="updateRating"/>
                <label for="3-stars" class="star">★</label>
                <input type="radio" id="2-stars" name="rating" value="2" v-model="score" @click="updateRating"/>
                <label for="2-stars" class="star">★</label>
                <input type="radio" id="1-star" name="rating" value="1" v-model="score" @click="updateRating"/>
                <label for="1-star" class="star">★</label>
              </div>
              <div style="margin: 5px; cursor: pointer;">
                <i class="fa-solid fa-heart fa-2xl" v-if="movie.like_users.includes(currentUser.pk)" @click="likeMovie(moviePk)" style="color:red"></i>
                <i class="fa-regular fa-heart fa-2xl" v-if="!movie.like_users.includes(currentUser.pk)" @click="likeMovie(moviePk)"></i>
              </div>
            </div>
          </div>
          <hr>
          <h4>개봉일 : {{movie.release_date }}</h4>
          <h4>상영시간 : {{movie.runtime }}</h4>
          <h4>
            출연배우 : <span v-for="i in [0,1,2]" :key="i">{{ movie.actors[i].name }},  </span>
          </h4>
          <h4>평점 : {{movie.vote_average }}</h4>
          <h4>인기도 : {{movie.popularity }}</h4>
          <h5>줄거리 : {{movie.overview}}</h5>
        </div>
      </div>
      <br>
      <div class="youtube">
        <iframe :src="videoURL" 
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
        ></iframe>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters,mapActions } from 'vuex'

export default {
  name: 'MovieDetailView', 
  data() {
    return {
      moviePk: this.$route.params.moviePk,      
      score: 0,
      isRated: false,
    }
  },  
  methods: {
    ...mapActions(['likeMovie', 'createReview', 'updateReview']),
    addRating(event) {
      this.isRated = true
      const data = {
        moviePk: this.moviePk,
        score: event.target.value
      }
      this.createReview(data)
    },
    updateRating(event) {
      console.log(event.target.value)
      const data = {
        moviePk: this.moviePk,
        reviewPk: this.review.pk,
        score: event.target.value
      }
      this.updateReview(data)
    },
  },    
  computed: {
    ...mapGetters(['movie', 'currentUser', 'review']),
    img_url () {
      return 'https://image.tmdb.org/t/p/w300/' + this.movie.poster_path
    },
    videoURL () {
      const videoId = this.movie.video_id
      return `https://www.youtube.com/embed/${videoId}`
    }
  },
  created() {
    this.$store.dispatch('fetchMovie', this.moviePk)
  }
}
</script>

<style scoped>
.youtube {
  position: relative;
  width: 100%;
  height: 0;
  padding-bottom: 56.25%;
}
.youtube iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
.userRate {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}
.movieTitle {
  display: flex;
  justify-content: space-between;
}
.movieCardText {
  text-align: left;
}
.movieCard {
  display: flex;
  justify-content: space-evenly;
  padding: 30px;
}
.detail {
  background-color: rgba(0, 0, 0, 0.9);
  margin: 0, 0;
  padding: 0, 50px;
}
.detailhome {

  color:azure;
  position: relative;
  bottom: 1rem;
  margin: 3rem 0;

}


.star-rating {
  display: flex;
  flex-direction: row-reverse;
  font-size: 1.9rem;
  line-height: 1.9rem;
  justify-content: space-around;
  /* padding: 0 0.2em; */
  text-align: center;
  width: 5em;
}
 
.star-rating input {
  display: none;
}
 
.star-rating label {
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1px;
  -webkit-text-stroke-color: #fafafa;
  cursor: pointer;
}
 
.star-rating :checked ~ label {
  -webkit-text-fill-color: gold;
}
 
.star-rating label:hover,
.star-rating label:hover ~ label {
  -webkit-text-fill-color: #fff58c;
}

.title {
  -webkit-animation: 3s fade;
          animation: 3s fade;
  color: azure;
  font-family: "Abril Fatface", cursive;
  font-size: 5em;
  left: 0;
  position: absolute;
  text-align: center;  
  width: 100%;
  margin: 0;
  height: 10px;
}
.title span {
  display: inline-block;
  padding: 0.5em 1em;
  position: relative;
  bottom: 5.5rem;
}
.title span:before {
  content: "";
  -webkit-animation: 2.5s draw;
          animation: 2.5s draw;
  border-top: 1px solid #bf9107;
  display: block;
  margin-bottom: 5%;
  margin-left: -5%;
  width: 110%;
}
.title span:after {
  -webkit-animation: 2.5s draw-bottom;
          animation: 2.5s draw-bottom;
  border-bottom: 1px solid #af8300;
  bottom: 0;
  content: "";
  display: block;
  position: absolute;
  right: 0;
  width: 100%;
}
/* Film Animations */
@-webkit-keyframes grain {
  0%, 100% {
    transform: translate(0, 0, 0);
  }
  10% {
    transform: translate(-1%, -1%);
  }
  20% {
    transform: translate(1%, 1%);
  }
  30% {
    transform: translate(-2%, -2%);
  }
  40% {
    transform: translate(3%, 3%);
  }
  50% {
    transform: translate(-3%, -3%);
  }
  60% {
    transform: translate(4%, 4%);
  }
  70% {
    transform: translate(-4%, -4%);
  }
  80% {
    transform: translate(2%, 2%);
  }
  90% {
    transform: translate(-3%, -3%);
  }
}
@keyframes grain {
  0%, 100% {
    transform: translate(0, 0, 0);
  }
  10% {
    transform: translate(-1%, -1%);
  }
  20% {
    transform: translate(1%, 1%);
  }
  30% {
    transform: translate(-2%, -2%);
  }
  40% {
    transform: translate(3%, 3%);
  }
  50% {
    transform: translate(-3%, -3%);
  }
  60% {
    transform: translate(4%, 4%);
  }
  70% {
    transform: translate(-4%, -4%);
  }
  80% {
    transform: translate(2%, 2%);
  }
  90% {
    transform: translate(-3%, -3%);
  }
}
@-webkit-keyframes scratch {
  0%, 100% {
    opacity: 0.075;
    transform: translateX(0);
  }
  10% {
    transform: translateX(-1%);
  }
  20% {
    transform: translateX(1%);
  }
  30% {
    opacity: 0.09;
    transform: translateX(-2%);
  }
  40% {
    transform: translateX(3%);
  }
  50% {
    opacity: 0.05;
    transform: translateX(-3%);
  }
  60% {
    transform: translateX(8%);
  }
  70% {
    transform: translateX(-3%);
  }
  80% {
    opacity: 0.02;
    transform: translateX(10%);
  }
  90% {
    transform: translateX(-2%);
  }
}
@keyframes scratch {
  0%, 100% {
    opacity: 0.075;
    transform: translateX(0);
  }
  10% {
    transform: translateX(-1%);
  }
  20% {
    transform: translateX(1%);
  }
  30% {
    opacity: 0.09;
    transform: translateX(-2%);
  }
  40% {
    transform: translateX(3%);
  }
  50% {
    opacity: 0.05;
    transform: translateX(-3%);
  }
  60% {
    transform: translateX(8%);
  }
  70% {
    transform: translateX(-3%);
  }
  80% {
    opacity: 0.02;
    transform: translateX(10%);
  }
  90% {
    transform: translateX(-2%);
  }
}
@-webkit-keyframes inner-scratch {
  0% {
    opacity: 0.08;
    transform: translateX(0);
  }
  10% {
    transform: translateX(-1%);
  }
  20% {
    transform: translateX(1%);
  }
  30% {
    transform: translateX(-2%);
  }
  40% {
    transform: translateX(3%);
  }
  50% {
    opacity: 0.06;
    transform: translateX(-3%);
  }
  60% {
    transform: translateX(8%);
  }
  70% {
    transform: translateX(-3%);
  }
  80% {
    opacity: 0.03;
    transform: translateX(10%);
  }
  90% {
    transform: translateX(20%);
  }
  100% {
    transform: translateX(30%);
  }
}
@keyframes inner-scratch {
  0% {
    opacity: 0.08;
    transform: translateX(0);
  }
  10% {
    transform: translateX(-1%);
  }
  20% {
    transform: translateX(1%);
  }
  30% {
    transform: translateX(-2%);
  }
  40% {
    transform: translateX(3%);
  }
  50% {
    opacity: 0.06;
    transform: translateX(-3%);
  }
  60% {
    transform: translateX(8%);
  }
  70% {
    transform: translateX(-3%);
  }
  80% {
    opacity: 0.03;
    transform: translateX(10%);
  }
  90% {
    transform: translateX(20%);
  }
  100% {
    transform: translateX(30%);
  }
}
@-webkit-keyframes draw {
  0% {
    width: 0%;
  }
  100% {
    width: 110%;
  }
}
@keyframes draw {
  0% {
    width: 0%;
  }
  100% {
    width: 110%;
  }
}
@-webkit-keyframes draw-bottom {
  0% {
    width: 0%;
  }
  100% {
    width: 100%;
  }
}
@keyframes draw-bottom {
  0% {
    width: 0%;
  }
  100% {
    width: 100%;
  }
}
@-webkit-keyframes fade {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
@keyframes fade {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

</style>