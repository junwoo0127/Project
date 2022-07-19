<template>
  <div class="Serieshome">    
    <h1 class="title">
      <br>      
      <span>Series</span>          
    </h1>
    <br>
    <br>
    <series-list class="selectbox" @refresh-page="refreshPage"></series-list>
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
    <div v-if="genrePk" class="SeriesMovieHome">
      <series-movie-card v-for="movie in movieGenre" :key="movie.pk" :movie="movie"></series-movie-card>
    </div>    
  </div>
</template>

<script>
import SeriesList from '@/components/SeriesList.vue'
import SeriesMovieCard from '@/components/SeriesMovieCard.vue'

import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'SeriesView',
  data() {
    return {
      genrePk: null,
    }
  },
  components: {
    SeriesList,
    SeriesMovieCard,
  },
  methods: {
    ...mapActions(['movieGenreList']),
    refreshPage(genrePk) {
      this.genrePk = genrePk
    }
  },
  computed: {
    ...mapGetters(['movieGenre'])
  },
  created () {
    this.movieGenreList()   
  }
}
</script>

<style scoped>
.SeriesMovieHome {
  display: flex;
  flex-wrap: wrap;
  float: left;
  width: auto; 
  margin: 0;
  padding: 0;
  justify-content: center;
  align-items: center;
  text-align: center;
  background-color: rgba(0, 0, 0, 1);
  background-size: cover;
}

.Serieshome {
  height: 20rem;
}

.selectbox{
  position: relative;
  top: 15rem;
}

@import url(https://fonts.googleapis.com/css?family=Abril+Fatface);

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