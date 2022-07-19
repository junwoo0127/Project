<template>
  <div>
    <b-form-select @change="getMovieGenre" v-model="genrePk">
      <b-form-select-option :value="null" >Select your genre.</b-form-select-option>
      <b-form-select-option v-for="genre in movieGenreList" :key="genre.id" :value="genre.id">{{ genre.name }}</b-form-select-option>
    </b-form-select>    
    <!-- <select @change="getMovieGenre" v-model="genrePk">
      <option :value="null" >Select your genre.</option>
      <option v-for="genre in movieGenreList" :key="genre.id" :value="genre.id">{{ genre.name }}</option>      
    </select> -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'SeriesList',
  data() {
    return {
      genrePk: null,
    }
  },
  methods: {
    ...mapActions(['movieGenre']),
    getMovieGenre () {
      console.log(this.genrePk)
      this.$emit('refresh-page', this.genrePk)
      this.$store.dispatch('movieGenre', this.genrePk)
    }
  },
  computed: {
    ...mapGetters(['movieGenreList'])
  },
  created() {
    this.$emit('refresh-page', this.genrePk)
  }
}
</script>

<style>

</style>