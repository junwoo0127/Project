<template>
  <div class="Moviecardhome">
    <img :src="img_url" alt="" @click="moveDetail">
    <!-- <b-card-group class="card-group">
      <b-card id="cards-box" :img-src="img_url" img-alt="Image" img-top @click="moveDetail">
        <b-card-text class="card-text">                      
        </b-card-text>      
      </b-card>
    </b-card-group>          -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'MovieCard',
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
.Moviecardhome {
  transition: all 0.2s linear;
  height: 100%;
  cursor: pointer; 
  margin: 2rem;
}
.Moviecardhome:hover {
  transform: scale(1.2);
}
/* .card-group {
  display: flex;
  flex-wrap: wrap;
  float: left;
  width: auto; 
  margin: 4rem;  
  padding: 0;
  justify-content: center;
  align-items: center;
  text-align: center;    
}

#cards-box {
  margin: 0;
  height: 20.3rem;
  cursor: pointer;      
}

.card-img-top {
  height: 20rem;
}

div.card-body {
  margin: 0;
  padding: 0;
  height: 10rem;
}

.card-text {
  padding: 0;
  height: 0;
} */

</style>