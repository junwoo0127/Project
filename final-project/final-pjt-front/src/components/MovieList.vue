<template>
  <div class="Movielisthome">              
    <movie-card v-for="movie in movies" :key="movie.id" :movie="movie"></movie-card>    
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'MovieList',
  components: {
    MovieCard,
  },  
  computed: {
    ...mapGetters(['movies']),
  }
}
</script>

<style>
.Movielisthome {
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

</style>