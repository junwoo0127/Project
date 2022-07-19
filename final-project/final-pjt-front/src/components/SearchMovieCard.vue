<template> 
  <div class="SearchMovieCard">
    <img :src="img_url" alt="" @click="moveDetail">
  </div>
  <!-- <b-card-group class="card">
    <b-card id="cards-box" :img-src="img_url" img-alt="Image" img-top @click="moveDetail">
      <b-card-text class="card-body">        
      </b-card-text>      
    </b-card>
  </b-card-group>          -->
</template>

<script>
export default {
  name: 'SearchMovieCard',
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
.SearchMovieCard {
  transition: all 0.2s linear;
  height: 100%;
  cursor: pointer; 
  margin: 2rem;
}
.SearchMovieCard:hover {
  transform: scale(1.2);
}

/* .card {
  display: flex;
  flex-wrap: wrap;
  float: left;
  width: 20%; 
  margin: 2rem;
  height: 10%;
  padding: 0;   
}

#cards-box {
  margin: 0;
}

.card-img-top {
  height: 20rem;
}

div.card-body {
  padding: 0;  
  height: 4rem;
} */

</style>