<template>  
  <div class="NowPlayingMovieCard">
    <img :src="img_url" alt="" @click="moveDetail">
  </div>
</template>

<script>
export default {
  name: 'NowPlayingMovieCard',
  props: {movie: Object},
  methods: {
    moveDetail() {
      this.$router.push({ name: 'movieDetail', params: {moviePk: this.movie.pk}})
    }
  },
  computed: {
    img_url () {
      return 'https://image.tmdb.org/t/p/w300/' + this.movie.poster_path
    }
  }
}
</script>

<style>
.NowPlayingMovieCard {
  transition: all 0.2s linear;
  height: 100%;
  cursor: pointer; 
  margin: 2rem;
}
.NowPlayingMovieCard:hover {
  transform: scale(1.2);
}

</style>