<template>
  <div id="app" >
    <nav>      
      <nav-bar></nav-bar>            
    </nav>    
    <router-view/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'

import { mapActions } from 'vuex'

export default {
  name: 'App',
  components: {
    NavBar,
  },
  data () {
    return {
      page: 1
    }
  },
  methods: {
    ...mapActions(['nowPlayingMovies', 'fetchCurrentUser', 'fetchMovies']),
  },
  created () {
    this.nowPlayingMovies()
    this.fetchCurrentUser()
    this.fetchMovies(this.page)
  },
  mounted () {
    document.addEventListener('scroll', function () {
      const { scrollHeight, scrollTop, clientHeight } = document.documentElement
      if (scrollTop + clientHeight >= scrollHeight -5) {
        console.log(this.page)
        this.page++
        this.$store.dispatch('fetchMovies', this.page)
    }
  }.bind(this))
  }
}

</script>

<style>
@import url(https://fonts.googleapis.com/css?family=Abril+Fatface);

#app {
  font-family: 'Abril Fatface', sans-serif, Bold;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-image: url(https://www.4flix.co.kr/data/editor/1903/20190312224626_78c82c6f958b778bd2a1d7ac07cf614a_4bs8.jpg);
  background-position: 0;
  background-size: cover;
  height: 450px;
  width: 100%;
  z-index: 10;
}
#app::after {
  background-image: url(https://www.4flix.co.kr/data/editor/1903/20190312224626_78c82c6f958b778bd2a1d7ac07cf614a_4bs8.jpg);
  background-position: 0;
  background-size: cover;
  position:absolute;
  top: 0;
  left: 0;
  height: 450px;
  width: 100%;
  z-index: 1;
  opacity: 0.5;
}

h1 {
  font-size: xx-large;
}

@font-face {
  font-family: 'Abril Fatface';
  font-style: normal;
  font-weight: 400;
  src: url(https://fonts.gstatic.com/s/abrilfatface/v19/zOL64pLDlL1D99S8g8PtiKchq-lmjdLh.woff2) format('woff2');
  unicode-range: U+0100-024F, U+0259, U+1E00-1EFF, U+2020, U+20A0-20AB, U+20AD-20CF, U+2113, U+2C60-2C7F, U+A720-A7FF;
}

nav {  
  position: top;
  width: 100%;  
  top: 0;
  padding: 0;
  text-align: center;
  margin: 0;
  font-size: x-large;
  z-index: 99;
  justify-content: center;
  align-items: center; 
}
nav::after {  
  position: absolute;
  width: 100%;  
  top: 0;
  background-color: darkgrey;  
  padding: 0;
  text-align: center;
  margin: 0;
  font-size: x-large;
  z-index: -1;
  opacity: 1;
  justify-content: center;
  align-items: center; 
}

nav a {
  font-weight: bold;
  color: #f4f5f7;
}

nav a.router-link-exact-active {
  color: #f6f8f7;
}
</style>
