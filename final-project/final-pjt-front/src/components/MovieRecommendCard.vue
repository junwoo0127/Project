<template>  
  <div class="MovieRecommendCard">
    <img :src="img_url" alt="" @click="moveDetail">
  </div>    
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'MovieRecommendCard',
  props: {movie: Object},
  methods: {
    moveDetail() {
      this.$router.push({ name: 'movieDetail', params: {moviePk: this.movie.pk}})
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
    img_url () {
      return 'https://image.tmdb.org/t/p/w300/' + this.movie.poster_path
    }
  }
}
</script>

<style>
.MovieRecommendCard {
  transition: all 0.2s linear;
  height: 100%;
  cursor: pointer; 
  margin: 2rem;
}
.MovieRecommendCard:hover {
  transform: scale(1.2);
}
</style>